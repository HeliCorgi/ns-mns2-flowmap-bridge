#!/usr/bin/env python3
"""Preregistered candidate-time pilot for the R3 axisymmetric-with-swirl track.

Implements:
  docs/gates/R3_AXISYM_WHOLESPACE_CANDIDATE_TIME_PILOT_PREREG_2026-09-09.md
  docs/gates/R3_AXISYM_WHOLESPACE_CANDIDATE_TIME_PILOT_IMPLEMENTATION_FREEZE_2026-09-09.md

This is a finite-resolution numerical diagnostic only. It does not fit a
singular time, certify whole-space continuum evolution, or make a Clay claim.
"""

from __future__ import annotations

import argparse
import gc
import json
import math
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
from scipy.interpolate import RectBivariateSpline

import manufactured_short_time as v1
import green_quadrature_repair as gq
import dynamic_resolution_audit as dra

TPILOT = 0.25
CHECKPOINTS: Tuple[float, ...] = (0.05, 0.10, 0.25)
CORE_R = 0.8
CORE_Z = 0.8
RECEIVERS = gq.RECEIVERS

# name, rmax, zmax, h, dt
RUN_SPECS: Tuple[Tuple[str, float, float, float, float], ...] = (
    ("B22_h08", 2.0, 2.0, 0.08, 0.002),
    ("B22_h04", 2.0, 2.0, 0.04, 0.0005),
    ("B22_h02", 2.0, 2.0, 0.02, 0.000125),
    ("B22_h04_dt025", 2.0, 2.0, 0.04, 0.00025),
    ("B44_h04", 4.0, 4.0, 0.04, 0.0005),
)


def rel_vec(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.linalg.norm((a - b).ravel()) / max(np.linalg.norm(b.ravel()), 1e-30))


def spline_psi_receivers(s: gq.DomainGridSolver, psi: np.ndarray) -> np.ndarray:
    """Evaluate psi, psi_r, psi_z at the frozen physical receivers."""
    spl = RectBivariateSpline(s.r, s.z, psi, kx=3, ky=3, s=0.0)
    out = np.zeros((len(RECEIVERS), 3), dtype=float)
    for k, (rr, zz) in enumerate(RECEIVERS):
        out[k, 0] = float(spl.ev(rr, zz))
        out[k, 1] = float(spl.ev(rr, zz, dx=1, dy=0))
        out[k, 2] = float(spl.ev(rr, zz, dx=0, dy=1))
    return out


def velocity_receivers(p: np.ndarray) -> np.ndarray:
    out = np.zeros((len(RECEIVERS), 2), dtype=float)
    for k, (rr, _zz) in enumerate(RECEIVERS):
        psi, pr, pz = p[k]
        out[k, 0] = -rr * pz
        out[k, 1] = 2.0 * psi + rr * pr
    return out


def physical_vorticity_sup(s: gq.DomainGridSolver, u: np.ndarray, w: np.ndarray) -> float:
    wr = -s.rr * s.d_z(u)
    wt = s.rr * w
    wz = 2.0 * u + s.rr * s.d_r(u)
    mag = np.sqrt(wr * wr + wt * wt + wz * wz)
    return float(np.max(mag))


def checkpoint_enstrophy_ratios(
    step_rows: List[Dict[str, object]], initial_enstrophy: float, dt: float
) -> Dict[str, float]:
    out: Dict[str, float] = {}
    if not step_rows:
        return {f"t_{t:.2f}": math.inf for t in CHECKPOINTS}
    times = np.asarray([float(r["time"]) for r in step_rows], dtype=float)
    vals = np.asarray([float(r["physical_enstrophy"]) for r in step_rows], dtype=float)
    for target in CHECKPOINTS:
        idx = int(np.argmin(np.abs(times - target)))
        if abs(times[idx] - target) > 0.51 * dt + 1e-13:
            out[f"t_{target:.2f}"] = math.inf
        else:
            out[f"t_{target:.2f}"] = float(vals[idx] / max(initial_enstrophy, 1e-30))
    return out


def run_one(name: str, rmax: float, zmax: float, h: float, dt: float) -> Dict[str, object]:
    print(f"run {name}: box=({rmax},{zmax}) h={h} dt={dt} T={TPILOT}", flush=True)

    # The inherited driver reads these globals. Runs are sequential.
    v1.T_FINAL = TPILOT
    v1.DT = dt

    s = gq.DomainGridSolver(h, rmax, zmax)
    run = v1.run_integrator(s, "rk4")
    summary = dict(v1.streamed_summary(run))
    summary["accepted_steps"] = len(run.step_rows)
    summary["expected_steps"] = int(round(TPILOT / dt))

    init_diag = s.state_diagnostics(run.initial_u, run.initial_w)
    initial_enstrophy = float(init_diag["physical_enstrophy"])
    initial_omega_sup = physical_vorticity_sup(s, run.initial_u, run.initial_w)
    initial_u1_sup = float(np.max(np.abs(run.initial_u)))

    if run.step_rows:
        step_enstrophy = [float(row["physical_enstrophy"]) for row in run.step_rows]
        max_enstrophy = max([initial_enstrophy, *step_enstrophy])
    else:
        max_enstrophy = math.inf

    final_omega_sup = physical_vorticity_sup(s, run.final_u, run.final_w)
    final_u1_sup = float(np.max(np.abs(run.final_u)))
    final_omega1_sup = float(np.max(np.abs(run.final_w)))

    psi, final_pres = s.solve_psi(run.final_w)
    pvec = spline_psi_receivers(s, psi)
    vvec = velocity_receivers(pvec)

    out: Dict[str, object] = {
        "name": name,
        "r": s.r.copy(),
        "z": s.z.copy(),
        "u": run.final_u.copy(),
        "w": run.final_w.copy(),
        "summary": summary,
        "final_poisson_residual": float(final_pres),
        "psi_receivers": pvec,
        "velocity_receivers": vvec,
        "diagnostics": {
            "initial_enstrophy": initial_enstrophy,
            "max_enstrophy": float(max_enstrophy),
            "max_enstrophy_ratio": float(max_enstrophy / max(initial_enstrophy, 1e-30)),
            "final_enstrophy_ratio": (
                float(run.step_rows[-1]["physical_enstrophy"]) / max(initial_enstrophy, 1e-30)
                if run.step_rows else math.inf
            ),
            "initial_physical_vorticity_sup": initial_omega_sup,
            "final_physical_vorticity_sup": final_omega_sup,
            "final_physical_vorticity_sup_ratio": final_omega_sup / max(initial_omega_sup, 1e-30),
            "initial_u1_sup": initial_u1_sup,
            "final_u1_sup": final_u1_sup,
            "final_u1_sup_ratio": final_u1_sup / max(initial_u1_sup, 1e-30),
            "final_omega1_sup": final_omega1_sup,
            "final_omega1_sup_over_A": final_omega1_sup / v1.A0,
            "checkpoint_enstrophy_ratios": checkpoint_enstrophy_ratios(
                run.step_rows, initial_enstrophy, dt
            ),
        },
    }

    del run, psi, s
    gc.collect()
    return out


def runtime_checks(row: Dict[str, object], dt: float) -> Dict[str, bool]:
    ss = dict(row["summary"])
    expected = int(round(TPILOT / dt))
    return {
        "completed": bool(ss["completed"]),
        "expected_steps": int(ss["accepted_steps"]) == expected,
        "no_reject": int(ss["rejected_steps"]) == 0,
        "finite": bool(ss["all_stage_finite"] and ss["all_step_finite"]),
        "amp": float(ss["max_frozen_symbol_amplification"]) <= 1.0 + v1.STABILITY_TOL,
        "cfl": float(ss["max_cfl"]) <= 0.10,
        "visc": float(ss["max_viscous_number"]) <= 0.05,
        "poisson": max(
            float(ss["max_stage_poisson_residual"]),
            float(ss["max_step_poisson_residual"]),
        ) <= 1e-10,
        "odd": float(ss["max_odd_z_defect"]) <= 1e-12,
        "energy": float(ss["max_energy_ratio_to_initial"]) <= 1.0 + 1e-5,
        "energy_balance": float(ss["max_energy_balance_defect"]) <= 0.20,
        "final_poisson": float(row["final_poisson_residual"]) <= 1e-10,
    }


def compact_report_row(row: Dict[str, object]) -> Dict[str, object]:
    return {
        "summary": row["summary"],
        "final_poisson_residual": row["final_poisson_residual"],
        "diagnostics": row["diagnostics"],
        "psi_receivers": np.asarray(row["psi_receivers"], dtype=float).tolist(),
        "velocity_receivers": np.asarray(row["velocity_receivers"], dtype=float).tolist(),
    }


def run_gate() -> Dict[str, object]:
    runs: Dict[str, Dict[str, object]] = {}
    for name, rmax, zmax, h, dt in RUN_SPECS:
        runs[name] = run_one(name, rmax, zmax, h, dt)

    checks: Dict[str, bool] = {}
    for name, _rmax, _zmax, _h, dt in RUN_SPECS:
        for key, value in runtime_checks(runs[name], dt).items():
            checks[f"C0_{name}_{key}"] = bool(value)

    # C1: three-level final nonlinear state refinement on B22.
    s84 = dra.state_rel_coarse_fine(runs["B22_h08"], runs["B22_h04"])
    s42 = dra.state_rel_coarse_fine(runs["B22_h04"], runs["B22_h02"])
    s_ratio = s42 / max(s84, 1e-30)
    checks["C1_state_refinement"] = s42 <= 0.45 * s84

    # C2: three-level recovered meridional velocity refinement.
    v08 = np.asarray(runs["B22_h08"]["velocity_receivers"], dtype=float)
    v04 = np.asarray(runs["B22_h04"]["velocity_receivers"], dtype=float)
    v02 = np.asarray(runs["B22_h02"]["velocity_receivers"], dtype=float)
    v84 = rel_vec(v08, v04)
    v42 = rel_vec(v04, v02)
    v_ratio = v42 / max(v84, 1e-30)
    checks["C2_velocity_refinement"] = v42 <= 0.45 * v84

    # C3: independent dt/2 shadow at fixed B22 h=.04.
    stime = dra.state_rel_same_resolution(runs["B22_h04"], runs["B22_h04_dt025"])
    vtime = rel_vec(
        np.asarray(runs["B22_h04"]["velocity_receivers"], dtype=float),
        np.asarray(runs["B22_h04_dt025"]["velocity_receivers"], dtype=float),
    )
    checks["C3_time_state_subordinate"] = bool(
        max(stime, s42) <= 1e-10 or stime <= 0.10 * s42
    )
    checks["C3_time_velocity_subordinate"] = vtime <= 0.10 * v42

    # C4: later-time domain veto at the same h=.04 and dt=.0005.
    sbox = dra.state_rel_same_resolution(runs["B22_h04"], runs["B44_h04"])
    vbox = rel_vec(
        np.asarray(runs["B22_h04"]["velocity_receivers"], dtype=float),
        np.asarray(runs["B44_h04"]["velocity_receivers"], dtype=float),
    )
    checks["C4_domain_state_subordinate"] = bool(
        max(sbox, s42) <= 1e-10 or sbox <= 0.50 * s42
    )
    checks["C4_domain_velocity_subordinate"] = vbox <= 0.50 * v42

    numeric_pass = bool(all(checks.values()))

    fine = dict(runs["B22_h02"]["diagnostics"])
    g1 = float(fine["max_enstrophy_ratio"]) >= 1.01
    g2 = float(fine["final_physical_vorticity_sup_ratio"]) >= 1.05
    g3 = float(fine["final_u1_sup_ratio"]) >= 1.02
    growth_triggers = {
        "G1_max_enstrophy_ratio_ge_1p01": bool(g1),
        "G2_final_vorticity_sup_ratio_ge_1p05": bool(g2),
        "G3_final_u1_sup_ratio_ge_1p02": bool(g3),
    }

    if not numeric_pass:
        decision = "STOP_REPAIR_PILOT_NUMERICS"
        passed = False
    elif any(growth_triggers.values()):
        decision = "PASS_TRIGGER_FOLLOWUP"
        passed = True
    else:
        decision = "PASS_NO_GROWTH_TRIGGER_THROUGH_T025"
        passed = True

    report_runs = {name: compact_report_row(row) for name, row in runs.items()}

    return {
        "schema": "r3-candidate-time-pilot-v1",
        "frozen_parameters": {
            "nu": v1.NU,
            "A": v1.A0,
            "R": 1.0,
            "Z": 1.0,
            "alpha": 16.0,
            "kappa": 1.0,
            "Tpilot": TPILOT,
            "integrator": "rk4",
            "runs": {
                name: {"box": [rmax, zmax], "h": h, "dt": dt}
                for name, rmax, zmax, h, dt in RUN_SPECS
            },
            "core": {"r_max": CORE_R, "abs_z_max": CORE_Z},
            "receivers": [list(p) for p in RECEIVERS],
            "receiver_evaluation": "RectBivariateSpline kx=3 ky=3 s=0; analytic spline derivatives",
            "state_refinement_ratio_limit": 0.45,
            "velocity_refinement_ratio_limit": 0.45,
            "time_to_fine_spatial_limit": 0.10,
            "domain_to_fine_spatial_limit": 0.50,
        },
        "runs": report_runs,
        "C1_state_refinement": {
            "S84_h08_h04": s84,
            "S42_h04_h02": s42,
            "fine_over_coarse": s_ratio,
        },
        "C2_velocity_refinement": {
            "V84_h08_h04": v84,
            "V42_h04_h02": v42,
            "fine_over_coarse": v_ratio,
        },
        "C3_time_shadow": {
            "state_dt0005_dt00025": stime,
            "velocity_dt0005_dt00025": vtime,
            "state_time_over_S42": stime / max(s42, 1e-30),
            "velocity_time_over_V42": vtime / max(v42, 1e-30),
        },
        "C4_later_domain": {
            "state_B22_B44_h04": sbox,
            "velocity_B22_B44_h04": vbox,
            "state_domain_over_S42": sbox / max(s42, 1e-30),
            "velocity_domain_over_V42": vbox / max(v42, 1e-30),
        },
        "finest_B22_growth_diagnostics": fine,
        "growth_triggers": growth_triggers,
        "checks": checks,
        "numeric_pass": numeric_pass,
        "decision": decision,
        "pass": passed,
        "claim_boundary": "finite-resolution candidate-time numerical pilot through T=0.25 only",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/r3_wholespace_w1/results/CANDIDATE_TIME_PILOT.json"),
    )
    args = parser.parse_args()
    result = run_gate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"decision": result["decision"], "output": str(args.output)}, indent=2))
    return 0 if result["pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
