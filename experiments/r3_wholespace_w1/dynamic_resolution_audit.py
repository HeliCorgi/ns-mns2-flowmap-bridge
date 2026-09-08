#!/usr/bin/env python3
"""Resolution-aware early-time nonlinear dynamic audit for the R3 W1 track.

Implements
`docs/gates/R3_AXISYM_WHOLESPACE_W1_DYNAMIC_RESOLUTION_PREREG_2026-09-07.md`.
No candidate-time growth or long-time claim is inspected here.
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

CORE_R = 0.8
CORE_Z = 0.8
RECEIVERS = gq.RECEIVERS
RUN_SPECS: Tuple[Tuple[str, float, float, float], ...] = (
    ("B22_h04", 2.0, 2.0, 0.04),
    ("B22_h02", 2.0, 2.0, 0.02),
    ("B22_h01", 2.0, 2.0, 0.01),
    ("B44_h04", 4.0, 4.0, 0.04),
    ("B44_h02", 4.0, 4.0, 0.02),
)


def psi_receiver_vector(s: gq.DomainGridSolver, psi: np.ndarray) -> np.ndarray:
    h = float(s.h)
    out = np.zeros((len(RECEIVERS), 3), dtype=float)
    for k, (rr, zz) in enumerate(RECEIVERS):
        i = int(round(rr / h))
        j = int(round((zz - s.z[0]) / h))
        if abs(s.r[i] - rr) > 2e-12 or abs(s.z[j] - zz) > 2e-12:
            raise RuntimeError(f"receiver {(rr, zz)} not aligned at h={h}")
        out[k, 0] = psi[i, j]
        out[k, 1] = (psi[i + 1, j] - psi[i - 1, j]) / (2.0 * h)
        out[k, 2] = (psi[i, j + 1] - psi[i, j - 1]) / (2.0 * h)
    return out


def velocity_receivers_from_psi(p: np.ndarray) -> np.ndarray:
    out = np.zeros((len(RECEIVERS), 2), dtype=float)
    for k, (rr, _zz) in enumerate(RECEIVERS):
        psi, pr, pz = p[k]
        out[k, 0] = -rr * pz
        out[k, 1] = 2.0 * psi + rr * pr
    return out


def dynamic_run(rmax: float, zmax: float, h: float) -> Dict[str, object]:
    s = gq.DomainGridSolver(h, rmax, zmax)
    run = v1.run_integrator(s, "rk4")
    summary = dict(v1.streamed_summary(run))
    summary["accepted_steps"] = len(run.step_rows)
    psi, pres = s.solve_psi(run.final_w)
    pvec = psi_receiver_vector(s, psi)
    vvec = velocity_receivers_from_psi(pvec)
    out: Dict[str, object] = {
        "r": s.r.copy(),
        "z": s.z.copy(),
        "u": run.final_u.copy(),
        "w": run.final_w.copy(),
        "summary": summary,
        "final_poisson_residual": float(pres),
        "psi_receivers": pvec,
        "velocity_receivers": vvec,
    }
    del run, s, psi
    gc.collect()
    return out


def rel_vec(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.linalg.norm((a - b).ravel()) / max(np.linalg.norm(b.ravel()), 1e-30))


def common_core_arrays(row: Dict[str, object]) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    r = np.asarray(row["r"], dtype=float)
    z = np.asarray(row["z"], dtype=float)
    u = np.asarray(row["u"], dtype=float)
    w = np.asarray(row["w"], dtype=float)
    ii = np.where(r <= CORE_R + 1e-13)[0]
    jj = np.where(np.abs(z) <= CORE_Z + 1e-13)[0]
    return r[ii], z[jj], u[np.ix_(ii, jj)], w[np.ix_(ii, jj)]


def state_rel_same_resolution(a: Dict[str, object], b: Dict[str, object]) -> float:
    ra, za, ua, wa = common_core_arrays(a)
    rb, zb, ub, wb = common_core_arrays(b)
    if ua.shape != ub.shape or wa.shape != wb.shape:
        raise RuntimeError("same-resolution common-core shape mismatch")
    if np.max(np.abs(ra - rb)) > 2e-12 or np.max(np.abs(za - zb)) > 2e-12:
        raise RuntimeError("same-resolution common-core coordinate mismatch")
    du = ua - ub
    dw = wa - wb
    num = math.sqrt(float(np.sum(du * du) + np.sum(dw * dw)))
    den = math.sqrt(float(np.sum(ub * ub) + np.sum(wb * wb)))
    return num / max(den, 1e-30)


def state_rel_coarse_fine(coarse: Dict[str, object], fine: Dict[str, object]) -> float:
    rc, zc, uc, wc = common_core_arrays(coarse)
    rf, zf, uf, wf = common_core_arrays(fine)
    hc = float(rc[1] - rc[0]) if len(rc) > 1 else math.nan
    hf = float(rf[1] - rf[0]) if len(rf) > 1 else math.nan
    stride = int(round(hc / hf))
    if stride < 1 or abs(stride * hf - hc) > 2e-12:
        raise RuntimeError("noninteger refinement stride")
    ufr = uf[::stride, ::stride]
    wfr = wf[::stride, ::stride]
    rfr = rf[::stride]
    zfr = zf[::stride]
    if ufr.shape != uc.shape or wfr.shape != wc.shape:
        raise RuntimeError("restricted fine state shape mismatch")
    if np.max(np.abs(rfr - rc)) > 2e-12 or np.max(np.abs(zfr - zc)) > 2e-12:
        raise RuntimeError("restricted fine coordinate mismatch")
    du = uc - ufr
    dw = wc - wfr
    num = math.sqrt(float(np.sum(du * du) + np.sum(dw * dw)))
    den = math.sqrt(float(np.sum(ufr * ufr) + np.sum(wfr * wfr)))
    return num / max(den, 1e-30)


def runtime_checks(summary: Dict[str, object]) -> Dict[str, bool]:
    return {
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
    }


def run_gate() -> Dict[str, object]:
    runs: Dict[str, Dict[str, object]] = {}
    for name, rmax, zmax, h in RUN_SPECS:
        print(f"dynamic {name}: box=({rmax},{zmax}) h={h}", flush=True)
        runs[name] = dynamic_run(rmax, zmax, h)

    checks: Dict[str, bool] = {}
    summaries: Dict[str, Dict[str, object]] = {}
    final_poisson: Dict[str, float] = {}
    for name, _rmax, _zmax, _h in RUN_SPECS:
        ss = dict(runs[name]["summary"])
        summaries[name] = ss
        for key, value in runtime_checks(ss).items():
            checks[f"R0_{name}_{key}"] = bool(value)
        pres = float(runs[name]["final_poisson_residual"])
        final_poisson[name] = pres
        checks[f"R0_{name}_final_receiver_poisson"] = pres <= 1e-10

    # R1: nonlinear final-state three-level refinement on B22.
    s42_b22 = state_rel_coarse_fine(runs["B22_h04"], runs["B22_h02"])
    s21_b22 = state_rel_coarse_fine(runs["B22_h02"], runs["B22_h01"])
    state_ratio_b22 = s21_b22 / max(s42_b22, 1e-30)
    checks["R1_state_second_order_B22"] = s21_b22 <= 0.35 * s42_b22

    # R2: recovered meridional velocity three-level refinement on B22.
    v04_b22 = np.asarray(runs["B22_h04"]["velocity_receivers"], dtype=float)
    v02_b22 = np.asarray(runs["B22_h02"]["velocity_receivers"], dtype=float)
    v01_b22 = np.asarray(runs["B22_h01"]["velocity_receivers"], dtype=float)
    v42_b22 = rel_vec(v04_b22, v02_b22)
    v21_b22 = rel_vec(v02_b22, v01_b22)
    velocity_ratio_b22 = v21_b22 / max(v42_b22, 1e-30)
    checks["R2_velocity_second_order_B22"] = v21_b22 <= 0.35 * v42_b22

    # B44 .04/.02 discretization corrections used in R3.
    s42_b44 = state_rel_coarse_fine(runs["B44_h04"], runs["B44_h02"])
    v04_b44 = np.asarray(runs["B44_h04"]["velocity_receivers"], dtype=float)
    v02_b44 = np.asarray(runs["B44_h02"]["velocity_receivers"], dtype=float)
    v42_b44 = rel_vec(v04_b44, v02_b44)

    # R3: h=.02 box sensitivity must be subordinate to measured resolution correction.
    sbox02 = state_rel_same_resolution(runs["B22_h02"], runs["B44_h02"])
    vbox02 = rel_vec(v02_b22, v02_b44)
    sres = max(s42_b22, s42_b44)
    vres = max(v42_b22, v42_b44)
    checks["R3_state_boundary_subordinate"] = bool(
        max(sbox02, sres) <= 1e-10 or sbox02 <= 0.50 * sres
    )
    checks["R3_velocity_boundary_subordinate"] = vbox02 <= 0.50 * vres

    # Descriptive h=.04 B22-vs-B44 box sensitivity.
    sbox04 = state_rel_same_resolution(runs["B22_h04"], runs["B44_h04"])
    vbox04 = rel_vec(v04_b22, v04_b44)

    passed = bool(all(checks.values()))
    decision = "PASS" if passed else "STOP_REPAIR_DYNAMIC_RESOLUTION"

    return {
        "schema": "r3-w1-dynamic-resolution-v1",
        "frozen_parameters": {
            "nu": v1.NU,
            "A": v1.A0,
            "R": 1.0,
            "Z": 1.0,
            "alpha": 16.0,
            "kappa": 1.0,
            "T": v1.T_FINAL,
            "dt": v1.DT,
            "integrator": "rk4",
            "runs": {
                name: {"box": [rmax, zmax], "h": h}
                for name, rmax, zmax, h in RUN_SPECS
            },
            "core": {"r_max": CORE_R, "abs_z_max": CORE_Z},
            "receivers": [list(p) for p in RECEIVERS],
            "second_order_ratio_tolerance": 0.35,
            "boundary_to_resolution_tolerance": 0.50,
        },
        "R0_streamed_summaries": summaries,
        "R0_final_receiver_poisson_residuals": final_poisson,
        "R1_state_refinement_B22": {
            "S42_h04_h02": s42_b22,
            "S21_h02_h01": s21_b22,
            "fine_over_coarse": state_ratio_b22,
        },
        "R2_velocity_refinement_B22": {
            "V42_h04_h02": v42_b22,
            "V21_h02_h01": v21_b22,
            "fine_over_coarse": velocity_ratio_b22,
        },
        "R3_resolution_corrections": {
            "state_B22_h04_h02": s42_b22,
            "state_B44_h04_h02": s42_b44,
            "state_resolution_max": sres,
            "velocity_B22_h04_h02": v42_b22,
            "velocity_B44_h04_h02": v42_b44,
            "velocity_resolution_max": vres,
        },
        "R3_box_sensitivity": {
            "state_B22_B44_h02": sbox02,
            "velocity_B22_B44_h02": vbox02,
            "state_box_over_resolution": sbox02 / max(sres, 1e-30),
            "velocity_box_over_resolution": vbox02 / max(vres, 1e-30),
        },
        "descriptive_box_sensitivity_h04": {
            "state_B22_B44": sbox04,
            "velocity_B22_B44": vbox04,
            "state_h02_over_h04": sbox02 / max(sbox04, 1e-30),
            "velocity_h02_over_h04": vbox02 / max(vbox04, 1e-30),
        },
        "final_psi_receivers": {
            name: np.asarray(runs[name]["psi_receivers"]).tolist() for name, _rmax, _zmax, _h in RUN_SPECS
        },
        "final_velocity_receivers": {
            name: np.asarray(runs[name]["velocity_receivers"]).tolist() for name, _rmax, _zmax, _h in RUN_SPECS
        },
        "checks": checks,
        "decision": decision,
        "pass": passed,
        "parent_statuses": {
            "PR112": "STOP_REPAIR_GREEN_QUADRATURE",
            "PR113": "PASS",
            "PR114": "STOP_REPAIR_DYNAMIC_DOMAIN",
            "PR115": "PASS",
        },
        "claim_boundary": "resolution-aware nonlinear evolution through T=2e-4 only",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/r3_wholespace_w1/results/W1_DYNAMIC_RESOLUTION.json"),
    )
    args = parser.parse_args()
    result = run_gate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"decision": result["decision"], "output": str(args.output)}, indent=2))
    return 0 if result["pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
