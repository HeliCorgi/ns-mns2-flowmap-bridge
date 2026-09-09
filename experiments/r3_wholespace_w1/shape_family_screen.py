#!/usr/bin/env python3
"""Preregistered shape-family screen for the R3 whole-space track.

Implements:
  docs/gates/R3_AXISYM_WHOLESPACE_SHAPE_FAMILY_SCREEN_PREREG_2026-09-09.md
  docs/gates/R3_AXISYM_WHOLESPACE_SHAPE_FAMILY_SCREEN_IMPLEMENTATION_FREEZE_2026-09-09.md

Finite-resolution triage only. No singularity, regularity, continuum, or Clay claim.
"""

from __future__ import annotations

import argparse
import gc
import json
import math
from pathlib import Path
from typing import Dict, Tuple

import numpy as np

import manufactured_short_time as v1
import green_quadrature_repair as gq
import dynamic_resolution_audit as dra
import candidate_time_pilot as ctp

TSCREEN = 0.25
H = 0.08
DT = 0.002
KAPPA = 0.75
ALPHAS: Tuple[float, ...] = (64.0, 128.0)
SHAPES: Tuple[str, ...] = ("C-Z0", "C-Z1", "C-Z2", "A-Z0", "A-Z1", "A-Z2")
BOXES: Tuple[Tuple[str, float, float], ...] = (("B22", 2.0, 2.0), ("B44", 4.0, 4.0))

STATE_BOX_LIMIT = 0.01
VELOCITY_BOX_LIMIT = 0.05
ENSTROPHY_BOX_DELTA_LIMIT = 0.01
VORTICITY_BOX_DELTA_LIMIT = 0.02
ENSTROPHY_TRIGGER = 1.02
VORTICITY_TRIGGER = 1.05


def annular_radial(s: np.ndarray) -> np.ndarray:
    return v1.bump(((s - 0.45) / 0.35) ** 2)


def axial_profile(zeta: np.ndarray, code: str) -> np.ndarray:
    b = v1.bump(zeta**2)
    if code == "Z0":
        return zeta * b
    if code == "Z1":
        return zeta * b * b
    if code == "Z2":
        return zeta * (1.0 - 2.0 * zeta**2) * b
    raise ValueError(code)


class ShapeGridSolver(gq.DomainGridSolver):
    def __init__(self, h: float, rmax: float, zmax: float):
        super().__init__(h, rmax, zmax)
        self.alpha = 64.0
        self.shape = "C-Z0"
        self.amplitude = self.alpha * v1.NU

    def set_parameters(self, alpha: float, shape: str) -> None:
        if shape not in SHAPES:
            raise ValueError(shape)
        self.alpha = float(alpha)
        self.shape = str(shape)
        self.amplitude = self.alpha * v1.NU

    def initial_state(self):
        radial_code, axial_code = self.shape.split("-")
        s = self.rr**2
        if radial_code == "C":
            radial = v1.bump(s)
        elif radial_code == "A":
            radial = annular_radial(s)
        else:
            raise ValueError(radial_code)
        zeta = self.zz / KAPPA
        axial = axial_profile(zeta, axial_code)
        u = self.amplitude * radial * axial
        w = np.zeros_like(u)
        self.zero_outer(u)
        self.zero_outer(w)
        return u, w


def rel_vec(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.linalg.norm((a - b).ravel()) / max(np.linalg.norm(b.ravel()), 1e-30))


def run_one(s: ShapeGridSolver, alpha: float, shape: str, box_name: str) -> Dict[str, object]:
    s.set_parameters(alpha, shape)
    v1.T_FINAL = TSCREEN
    v1.DT = DT
    print(f"row alpha={alpha:g} shape={shape} {box_name} h={H} dt={DT} T={TSCREEN}", flush=True)

    run = v1.run_integrator(s, "rk4")
    summary = dict(v1.streamed_summary(run))
    summary["accepted_steps"] = len(run.step_rows)
    summary["expected_steps"] = int(round(TSCREEN / DT))

    init_diag = s.state_diagnostics(run.initial_u, run.initial_w)
    e0 = float(init_diag["physical_enstrophy"])
    estep = [float(row["physical_enstrophy"]) for row in run.step_rows]
    emax = max([e0, *estep]) if estep else math.inf
    efinal = estep[-1] if estep else math.inf

    w0sup = ctp.physical_vorticity_sup(s, run.initial_u, run.initial_w)
    wfsup = ctp.physical_vorticity_sup(s, run.final_u, run.final_w)
    u0sup = float(np.max(np.abs(run.initial_u)))
    ufsup = float(np.max(np.abs(run.final_u)))
    omega1sup = float(np.max(np.abs(run.final_w)))

    psi, pres = s.solve_psi(run.final_w)
    pvec = ctp.spline_psi_receivers(s, psi)
    vvec = ctp.velocity_receivers(pvec)

    out: Dict[str, object] = {
        "r": s.r.copy(),
        "z": s.z.copy(),
        "u": run.final_u.copy(),
        "w": run.final_w.copy(),
        "summary": summary,
        "final_poisson_residual": float(pres),
        "psi_receivers": pvec,
        "velocity_receivers": vvec,
        "diagnostics": {
            "initial_physical_enstrophy": e0,
            "final_physical_enstrophy": float(efinal),
            "max_physical_enstrophy": float(emax),
            "max_enstrophy_ratio": float(emax / max(e0, 1e-30)),
            "final_enstrophy_ratio": float(efinal / max(e0, 1e-30)),
            "initial_physical_vorticity_sup": w0sup,
            "final_physical_vorticity_sup": wfsup,
            "final_physical_vorticity_sup_ratio": float(wfsup / max(w0sup, 1e-30)),
            "initial_u1_sup": u0sup,
            "final_u1_sup": ufsup,
            "final_u1_sup_ratio": float(ufsup / max(u0sup, 1e-30)),
            "final_omega1_sup": omega1sup,
            "final_omega1_sup_over_Acoef": float(omega1sup / max(s.amplitude, 1e-30)),
        },
    }

    del run, psi
    gc.collect()
    return out


def runtime_checks(row: Dict[str, object]) -> Dict[str, bool]:
    ss = dict(row["summary"])
    return {
        "completed": bool(ss["completed"]),
        "expected_steps": int(ss["accepted_steps"]) == int(round(TSCREEN / DT)),
        "no_reject": int(ss["rejected_steps"]) == 0,
        "finite": bool(ss["all_stage_finite"] and ss["all_step_finite"]),
        "amp": float(ss["max_frozen_symbol_amplification"]) <= 1.0 + v1.STABILITY_TOL,
        "cfl": float(ss["max_cfl"]) <= 0.10,
        "visc": float(ss["max_viscous_number"]) <= 0.05,
        "poisson": max(float(ss["max_stage_poisson_residual"]), float(ss["max_step_poisson_residual"])) <= 1e-10,
        "odd": float(ss["max_odd_z_defect"]) <= 1e-12,
        "energy": float(ss["max_energy_ratio_to_initial"]) <= 1.0 + 1e-5,
        "energy_balance": float(ss["max_energy_balance_defect"]) <= 0.20,
        "final_poisson": float(row["final_poisson_residual"]) <= 1e-10,
    }


def compact(row: Dict[str, object]) -> Dict[str, object]:
    return {
        "summary": row["summary"],
        "final_poisson_residual": row["final_poisson_residual"],
        "diagnostics": row["diagnostics"],
        "psi_receivers": np.asarray(row["psi_receivers"], dtype=float).tolist(),
        "velocity_receivers": np.asarray(row["velocity_receivers"], dtype=float).tolist(),
    }


def run_gate() -> Dict[str, object]:
    solvers = {name: ShapeGridSolver(H, rmax, zmax) for name, rmax, zmax in BOXES}
    rows: Dict[str, object] = {}
    promotions = []
    valid_count = 0

    for alpha in ALPHAS:
        for shape in SHAPES:
            key = f"a{alpha:g}_{shape.replace('-', '_')}"
            pair = {name: run_one(solvers[name], alpha, shape, name) for name, _r, _z in BOXES}

            rchecks = {name: runtime_checks(pair[name]) for name, _r, _z in BOXES}
            runtime_pass = all(all(c.values()) for c in rchecks.values())

            sbox = dra.state_rel_same_resolution(pair["B22"], pair["B44"])
            vbox = rel_vec(
                np.asarray(pair["B22"]["velocity_receivers"], dtype=float),
                np.asarray(pair["B44"]["velocity_receivers"], dtype=float),
            )
            d22 = dict(pair["B22"]["diagnostics"])
            d44 = dict(pair["B44"]["diagnostics"])
            e22 = float(d22["max_enstrophy_ratio"])
            e44 = float(d44["max_enstrophy_ratio"])
            w22 = float(d22["final_physical_vorticity_sup_ratio"])
            w44 = float(d44["final_physical_vorticity_sup_ratio"])

            domain_checks = {
                "state_box_rel": sbox <= STATE_BOX_LIMIT,
                "velocity_box_rel": vbox <= VELOCITY_BOX_LIMIT,
                "enstrophy_ratio_delta": abs(e22 - e44) <= ENSTROPHY_BOX_DELTA_LIMIT,
                "vorticity_ratio_delta": abs(w22 - w44) <= VORTICITY_BOX_DELTA_LIMIT,
            }
            domain_pass = all(domain_checks.values())

            g_e = min(e22, e44) >= ENSTROPHY_TRIGGER
            g_w = min(w22, w44) >= VORTICITY_TRIGGER

            if not runtime_pass:
                classification = "INVALID_RUNTIME"
            elif not domain_pass:
                classification = "INVALID_DOMAIN"
                valid_count += 1
            elif g_e or g_w:
                classification = "PROMOTE_HIGH_RES"
                valid_count += 1
                promotions.append({
                    "alpha": alpha,
                    "kappa": KAPPA,
                    "shape": shape,
                    "trigger_enstrophy": bool(g_e),
                    "trigger_vorticity": bool(g_w),
                })
            else:
                classification = "NO_GROWTH_TRIGGER"
                valid_count += 1

            rows[key] = {
                "alpha": alpha,
                "kappa": KAPPA,
                "shape": shape,
                "Acoef": alpha * v1.NU,
                "B22": compact(pair["B22"]),
                "B44": compact(pair["B44"]),
                "runtime_checks": rchecks,
                "runtime_pass": runtime_pass,
                "domain_metrics": {
                    "state_box_relative": sbox,
                    "velocity_box_relative": vbox,
                    "max_enstrophy_ratio_B22": e22,
                    "max_enstrophy_ratio_B44": e44,
                    "max_enstrophy_ratio_abs_delta": abs(e22 - e44),
                    "final_vorticity_ratio_B22": w22,
                    "final_vorticity_ratio_B44": w44,
                    "final_vorticity_ratio_abs_delta": abs(w22 - w44),
                },
                "domain_checks": domain_checks,
                "domain_pass": domain_pass,
                "growth_triggers": {
                    "G_E_both_boxes_enstrophy": bool(g_e),
                    "G_W_both_boxes_final_vorticity": bool(g_w),
                },
                "classification": classification,
            }
            print(
                f"classification {key}: {classification} "
                f"E=({e22:.6g},{e44:.6g}) W=({w22:.6g},{w44:.6g}) "
                f"Sbox={sbox:.3g} Vbox={vbox:.3g}",
                flush=True,
            )
            del pair
            gc.collect()

    if valid_count == 0:
        decision = "STOP_REPAIR_SHAPE_SCREEN"
        passed = False
    elif promotions:
        decision = "PASS_WITH_PROMOTIONS"
        passed = True
    else:
        decision = "PASS_NO_PROMOTIONS"
        passed = True

    return {
        "schema": "r3-shape-family-screen-v1",
        "frozen_parameters": {
            "nu": v1.NU,
            "R": 1.0,
            "alphas": list(ALPHAS),
            "kappa": KAPPA,
            "shapes": list(SHAPES),
            "shape_formulas": {
                "C": "b(r^2)",
                "A": "b(((r^2-.45)/.35)^2)",
                "Z0": "zeta*b(zeta^2)",
                "Z1": "zeta*b(zeta^2)^2",
                "Z2": "zeta*(1-2*zeta^2)*b(zeta^2)",
            },
            "Tscreen": TSCREEN,
            "h": H,
            "dt": DT,
            "integrator": "rk4",
            "boxes": {name: [rmax, zmax] for name, rmax, zmax in BOXES},
            "state_box_limit": STATE_BOX_LIMIT,
            "velocity_box_limit": VELOCITY_BOX_LIMIT,
            "enstrophy_box_delta_limit": ENSTROPHY_BOX_DELTA_LIMIT,
            "vorticity_box_delta_limit": VORTICITY_BOX_DELTA_LIMIT,
            "enstrophy_trigger": ENSTROPHY_TRIGGER,
            "vorticity_trigger": VORTICITY_TRIGGER,
        },
        "rows": rows,
        "promotion_set": promotions,
        "valid_row_count": valid_count,
        "decision": decision,
        "pass": passed,
        "claim_boundary": "coarse matched-box six-shape pure-swirl triage through T=.25 only",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/r3_wholespace_w1/results/SHAPE_FAMILY_SCREEN.json"),
    )
    args = parser.parse_args()
    result = run_gate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "decision": result["decision"],
        "promotions": result["promotion_set"],
        "output": str(args.output),
    }, indent=2))
    return 0 if result["pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
