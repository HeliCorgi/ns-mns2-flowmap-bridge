#!/usr/bin/env python3
"""Preregistered arbitrary-source Green quadrature repair for R3 W1.

This script implements
`docs/gates/R3_AXISYM_WHOLESPACE_W1_GREEN_QUADRATURE_REPAIR_PREREG_2026-09-07.md`.
It repairs only the independent free-space Green quadrature that stopped PR #112.
No dynamic-domain, long-time, singularity, regularity, or Clay claim is made.
"""

from __future__ import annotations

import argparse
import gc
import json
import math
import time
from pathlib import Path
from typing import Dict, Tuple

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.interpolate import RectBivariateSpline
from scipy.sparse import linalg as spla

import manufactured_short_time as v1

PI = math.pi
H = 0.04
RMAX = 4.0
ZMAX = 4.0
RECEIVERS: Tuple[Tuple[float, float], ...] = (
    (0.12, 0.00),
    (0.24, 0.20),
    (0.28, -0.24),
    (0.20, 0.32),
)


class DomainGridSolver(v1.GridSolver):
    """Frozen v1 spatial/time scheme on the B44 nonperiodic box."""

    def __init__(self, h: float, rmax: float, zmax: float):
        self.h = float(h)
        self.rmax = float(rmax)
        self.zmax = float(zmax)
        self.nr = int(round(self.rmax / self.h)) + 1
        self.nz = int(round(2.0 * self.zmax / self.h)) + 1
        self.r = np.linspace(0.0, self.rmax, self.nr)
        self.z = np.linspace(-self.zmax, self.zmax, self.nz)
        if abs(self.r[1] - self.r[0] - self.h) > 1e-13 or abs(self.z[1] - self.z[0] - self.h) > 1e-13:
            raise ValueError("frozen grid spacing mismatch")
        self.rr = self.r[:, None]
        self.zz = self.z[None, :]
        self.ni = self.nr - 1
        self.nj = self.nz - 2
        self.op = v1.assemble_minus_l5(self.r, self.z, self.h).tocsc()
        self.solve_factor = spla.factorized(self.op)
        self.scanner = v1.RuntimeStabilityScanner(self.h)
        self.core = (self.rr <= v1.CORE_R + 1e-14) & (np.abs(self.zz) <= v1.CORE_Z + 1e-14)


def trap_weights(n: int) -> np.ndarray:
    w = np.ones(n, dtype=float)
    w[0] = 0.5
    w[-1] = 0.5
    return w


def lifted_source_audit(r: np.ndarray, z: np.ndarray, omega: np.ndarray) -> Dict[str, float]:
    wr = trap_weights(len(r))[:, None]
    wz = trap_weights(len(z))[None, :]
    weight = wr * wz * (r[:, None] ** 3) * H * H
    total = float(np.sum(weight * np.abs(omega)))
    inside = (r[:, None] <= 2.0 + 1e-14) & (np.abs(z[None, :]) <= 2.0 + 1e-14)
    outside = float(np.sum(weight * np.abs(omega) * (~inside)))
    monopole = float(np.sum(weight * omega))
    return {
        "lifted_L1": total,
        "outside_B22_fraction": outside / max(total, 1e-30),
        "normalized_odd_monopole": abs(monopole) / max(total, 1e-30),
    }


def cellwise_axis_rule(grid: np.ndarray, order: int) -> Tuple[np.ndarray, np.ndarray]:
    """Mapped Gauss-Legendre nodes/weights in every original grid cell."""
    if order < 1:
        raise ValueError("cell order must be positive")
    x, w = leggauss(order)
    lo = np.asarray(grid[:-1], dtype=float)
    hi = np.asarray(grid[1:], dtype=float)
    mid = 0.5 * (lo + hi)
    half = 0.5 * (hi - lo)
    nodes = (mid[:, None] + half[:, None] * x[None, :]).reshape(-1)
    weights = (half[:, None] * np.ones((1, order), dtype=float) * w[None, :]).reshape(-1)
    return nodes, weights


class CellwiseGreenEvaluator:
    """Independent reduced 5-D Green evaluator over the cubic source interpolant."""

    def __init__(self, r: np.ndarray, z: np.ndarray, omega: np.ndarray):
        self.r = np.asarray(r, dtype=float)
        self.z = np.asarray(z, dtype=float)
        self.omega = np.asarray(omega, dtype=float)
        self.spline = RectBivariateSpline(self.r, self.z, self.omega, kx=3, ky=3, s=0.0)
        self._source_cache: Dict[int, Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]] = {}

    def source_rule(self, order: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        if order not in self._source_cache:
            rho, wr = cellwise_axis_rule(self.r, order)
            zeta, wz = cellwise_axis_rule(self.z, order)
            om = np.asarray(self.spline(rho, zeta, grid=True), dtype=float)
            self._source_cache[order] = (rho, wr, zeta, wz, om)
        return self._source_cache[order]

    def evaluate(self, source_order: int, theta_order: int) -> np.ndarray:
        rho, wr, zeta, wz, om = self.source_rule(source_order)
        xt, wt = leggauss(theta_order)
        theta = 0.5 * PI * (xt + 1.0)
        wtheta = 0.5 * PI * wt
        ct = np.cos(theta)
        st2w = (np.sin(theta) ** 2) * wtheta

        # Full cellwise tensor source weight, including lifted rho^3 measure.
        base2 = (rho[:, None] ** 3) * om * wr[:, None] * wz[None, :]
        coeff = 1.0 / (2.0 * PI)
        ans = np.zeros((len(RECEIVERS), 3), dtype=float)

        # Keep the main 3-D work arrays around O(1e6) entries each.
        target_entries = 1_200_000
        chunk = max(1, min(len(rho), target_entries // max(len(zeta) * theta_order, 1)))
        c = ct[None, None, :]
        wa = st2w[None, None, :]
        zb = zeta[None, :, None]

        for pidx, (rp, zp) in enumerate(RECEIVERS):
            acc0 = 0.0
            accr = 0.0
            accz = 0.0
            for a in range(0, len(rho), chunk):
                b = min(a + chunk, len(rho))
                rb = rho[a:b, None, None]
                weighted = base2[a:b, :, None] * wa
                d = rp * rp + rb * rb - 2.0 * rp * rb * c + (zp - zb) ** 2
                if np.any(d <= 0.0):
                    raise RuntimeError("unexpected Green quadrature singular sample")
                invd = 1.0 / d
                k0 = invd * np.sqrt(invd)
                k5 = k0 * invd
                acc0 += float(np.sum(weighted * k0))
                accr += float(np.sum(weighted * (-3.0 * (rp - rb * c)) * k5))
                accz += float(np.sum(weighted * (-3.0 * (zp - zb)) * k5))
            ans[pidx, :] = coeff * np.array([acc0, accr, accz])
        return ans


def rel_vec(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.linalg.norm((a - b).ravel()) / max(np.linalg.norm(b.ravel()), 1e-30))


def runtime_source() -> Tuple[np.ndarray, np.ndarray, np.ndarray, Dict[str, object], Dict[str, float]]:
    s = DomainGridSolver(H, RMAX, ZMAX)
    run = v1.run_integrator(s, "rk4")
    summary = dict(v1.streamed_summary(run))
    summary["accepted_steps"] = len(run.step_rows)
    r = s.r.copy()
    z = s.z.copy()
    w = run.final_w.copy()
    audit = lifted_source_audit(r, z, w)
    del run, s
    gc.collect()
    return r, z, w, summary, audit


def run_gate() -> Dict[str, object]:
    r, z, omega, summary, source_audit = runtime_source()

    g0_checks: Dict[str, bool] = {
        "completed": bool(summary["completed"]),
        "eight_steps": int(summary["accepted_steps"]) == 8,
        "no_reject": int(summary["rejected_steps"]) == 0,
        "finite": bool(summary["all_stage_finite"] and summary["all_step_finite"]),
        "amp": float(summary["max_frozen_symbol_amplification"]) <= 1.0 + v1.STABILITY_TOL,
        "cfl": float(summary["max_cfl"]) <= 0.10,
        "visc": float(summary["max_viscous_number"]) <= 0.05,
        "poisson": max(float(summary["max_stage_poisson_residual"]), float(summary["max_step_poisson_residual"])) <= 1e-10,
        "odd": float(summary["max_odd_z_defect"]) <= 1e-12,
        "energy": float(summary["max_energy_ratio_to_initial"]) <= 1.0 + 1e-5,
        "energy_balance": float(summary["max_energy_balance_defect"]) <= 0.20,
        "source_containment": float(source_audit["outside_B22_fraction"]) <= 1e-12,
        "odd_monopole": float(source_audit["normalized_odd_monopole"]) <= 1e-12,
    }

    evaluator = CellwiseGreenEvaluator(r, z, omega)
    specs = {
        "Q2": (2, 64),
        "Q4": (4, 96),
        "Q6": (6, 144),
        "Q4T": (4, 144),
        "Q6T": (6, 96),
    }
    values: Dict[str, np.ndarray] = {}
    timings: Dict[str, float] = {}
    for name in ("Q2", "Q4", "Q6", "Q4T", "Q6T"):
        q, nt = specs[name]
        print(f"evaluating {name}: source_order={q}, theta_order={nt}", flush=True)
        t0 = time.perf_counter()
        values[name] = evaluator.evaluate(q, nt)
        timings[name] = time.perf_counter() - t0
        print(f"finished {name} in {timings[name]:.3f}s", flush=True)

    d24 = rel_vec(values["Q2"], values["Q4"])
    d46 = rel_vec(values["Q4"], values["Q6"])
    dtheta = rel_vec(values["Q6T"], values["Q6"])
    dsource = rel_vec(values["Q4T"], values["Q6"])

    scale = float(np.max(np.abs(values["Q6"])))
    active = np.abs(values["Q6"]) >= 1e-3 * scale
    component_rel = np.zeros_like(values["Q6"])
    component_rel[active] = np.abs(values["Q4T"][active] - values["Q6"][active]) / np.maximum(np.abs(values["Q6"][active]), 1e-30)
    max_active_component_rel = float(np.max(component_rel[active])) if np.any(active) else math.inf

    checks: Dict[str, bool] = {}
    for key, value in g0_checks.items():
        checks[f"G0_{key}"] = bool(value)
    checks["G1_strict_decrease"] = d46 < d24
    checks["G1_final_delta"] = d46 <= 1.0e-3
    checks["G2_angular_isolation"] = dtheta <= 7.5e-4
    checks["G3_source_isolation"] = dsource <= 7.5e-4
    checks["G4_active_component_stability"] = max_active_component_rel <= 1.0e-2

    g0_pass = bool(all(g0_checks.values()))
    g1_to_g4_pass = bool(
        checks["G1_strict_decrease"]
        and checks["G1_final_delta"]
        and checks["G2_angular_isolation"]
        and checks["G3_source_isolation"]
        and checks["G4_active_component_stability"]
    )
    if not g0_pass:
        decision = "STOP_REPAIR_GREEN_SOURCE_REPRODUCTION"
        passed = False
    elif not g1_to_g4_pass:
        decision = "STOP_REPAIR_GREEN_QUADRATURE"
        passed = False
    else:
        decision = "PASS"
        passed = True

    return {
        "schema": "r3-w1-green-quadrature-repair-v1",
        "frozen_parameters": {
            "nu": v1.NU,
            "A": v1.A0,
            "R": 1.0,
            "Z": 1.0,
            "alpha": 16.0,
            "kappa": 1.0,
            "box": [RMAX, ZMAX],
            "h": H,
            "T": v1.T_FINAL,
            "dt": v1.DT,
            "integrator": "rk4",
            "receivers": [list(p) for p in RECEIVERS],
            "source_interpolation": "RectBivariateSpline(kx=3,ky=3,s=0)",
            "levels": {name: {"source_cell_order": q, "theta_order": nt} for name, (q, nt) in specs.items()},
            "active_component_fraction_of_max": 1.0e-3,
            "G1_final_delta_tolerance": 1.0e-3,
            "G2_angular_tolerance": 7.5e-4,
            "G3_source_tolerance": 7.5e-4,
            "G4_component_tolerance": 1.0e-2,
        },
        "G0_runtime_summary": summary,
        "G0_source_audit": source_audit,
        "quadrature_receiver_values": {name: arr.tolist() for name, arr in values.items()},
        "quadrature_timings_seconds": timings,
        "convergence": {
            "d24_rel_Q2_Q4": d24,
            "d46_rel_Q4_Q6": d46,
            "dtheta_rel_Q6T_Q6": dtheta,
            "dsource_rel_Q4T_Q6": dsource,
            "active_component_count": int(np.sum(active)),
            "active_component_mask": active.tolist(),
            "active_component_relative_Q4T_Q6": component_rel.tolist(),
            "max_active_component_relative_Q4T_Q6": max_active_component_rel,
        },
        "checks": checks,
        "decision": decision,
        "pass": passed,
        "stopped_parent_status": "PR112 R3-W1-DYNAMIC-DOMAIN-AUDIT = STOP_REPAIR_GREEN_QUADRATURE (unchanged)",
        "claim_boundary": "arbitrary-source numerical free-space Green quadrature repair only",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/r3_wholespace_w1/results/W1_GREEN_QUADRATURE_REPAIR.json"),
    )
    args = parser.parse_args()
    result = run_gate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"decision": result["decision"], "output": str(args.output)}, indent=2))
    return 0 if result["pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
