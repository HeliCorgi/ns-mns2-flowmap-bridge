#!/usr/bin/env python3
"""Preregistered elliptic discretization / boundary-error decomposition gate.

Implements
`docs/gates/R3_AXISYM_WHOLESPACE_W1_ELLIPTIC_DECOMPOSITION_PREREG_2026-09-07.md`.
This is a static elliptic diagnostic on the frozen early-time B44 source only.
"""

from __future__ import annotations

import argparse
import gc
import json
import math
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np

import manufactured_short_time as v1
import green_quadrature_repair as gq

BOXES: Tuple[Tuple[str, float, float], ...] = (
    ("B22", 2.0, 2.0),
    ("B32", 3.0, 2.0),
    ("B42", 4.0, 2.0),
    ("B23", 2.0, 3.0),
    ("B24", 2.0, 4.0),
    ("B44", 4.0, 4.0),
)
RECEIVERS = gq.RECEIVERS


def rel_vec(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.linalg.norm((a - b).ravel()) / max(np.linalg.norm(b.ravel()), 1e-30))


def receiver_vector(s: gq.DomainGridSolver, psi: np.ndarray) -> np.ndarray:
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


def static_box_solve(
    evaluator: gq.CellwiseGreenEvaluator,
    h: float,
    rmax: float,
    zmax: float,
) -> Tuple[np.ndarray, float]:
    s = gq.DomainGridSolver(h, rmax, zmax)
    source = np.asarray(evaluator.spline(s.r, s.z, grid=True), dtype=float)
    psi, pres = s.solve_psi(source)
    rv = receiver_vector(s, psi)
    del s, source, psi
    gc.collect()
    return rv, float(pres)


def adjacent_changes(rows: Dict[str, np.ndarray]) -> Dict[str, float]:
    return {
        "radial_small_mid": rel_vec(rows["B22"], rows["B32"]),
        "radial_mid_large": rel_vec(rows["B32"], rows["B42"]),
        "axial_small_mid": rel_vec(rows["B22"], rows["B23"]),
        "axial_mid_large": rel_vec(rows["B23"], rows["B24"]),
    }


def source_runtime_checks(summary: Dict[str, object], audit: Dict[str, float]) -> Dict[str, bool]:
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
        "source_containment": float(audit["outside_B22_fraction"]) <= 1e-12,
        "odd_monopole": float(audit["normalized_odd_monopole"]) <= 1e-12,
    }


def run_gate() -> Dict[str, object]:
    # E0: exact source reproduction and independently passed Green reference.
    full_r, full_z, full_w, summary, source_audit = gq.runtime_source()
    e0_source_checks = source_runtime_checks(summary, source_audit)
    evaluator = gq.CellwiseGreenEvaluator(full_r, full_z, full_w)

    print("E0 evaluating Q6/Q4T/Q6T", flush=True)
    q6 = evaluator.evaluate(6, 144)
    q4t = evaluator.evaluate(4, 144)
    q6t = evaluator.evaluate(6, 96)
    green_source_iso = rel_vec(q4t, q6)
    green_theta_iso = rel_vec(q6t, q6)
    e0_green_checks = {
        "source_isolation": green_source_iso <= 7.5e-4,
        "angular_isolation": green_theta_iso <= 7.5e-4,
    }

    # Static elliptic family at h=.04 and h=.02 on all six boxes.
    rows04: Dict[str, np.ndarray] = {}
    rows02: Dict[str, np.ndarray] = {}
    residuals: Dict[str, float] = {}
    for name, rmax, zmax in BOXES:
        print(f"static solve {name} h=.04", flush=True)
        rv04, p04 = static_box_solve(evaluator, 0.04, rmax, zmax)
        print(f"static solve {name} h=.02", flush=True)
        rv02, p02 = static_box_solve(evaluator, 0.02, rmax, zmax)
        rows04[name] = rv04
        rows02[name] = rv02
        residuals[f"{name}_h04"] = p04
        residuals[f"{name}_h02"] = p02

    # B22 h=.01 validation solve.
    print("static solve B22 h=.01", flush=True)
    b22_01, p01 = static_box_solve(evaluator, 0.01, 2.0, 2.0)
    residuals["B22_h01"] = p01

    poisson_checks = {key: value <= 1e-10 for key, value in residuals.items()}

    # E1: second-order receiver convergence on B22.
    d42 = rel_vec(rows04["B22"], rows02["B22"])
    d21 = rel_vec(rows02["B22"], b22_01)
    e1_ratio = d21 / max(d42, 1e-30)
    e1_pass = d21 <= 0.35 * d42

    # E2: stabilization of the predeclared second-order Richardson extrapolation.
    x42_b22 = (4.0 * rows02["B22"] - rows04["B22"]) / 3.0
    x21_b22 = (4.0 * b22_01 - rows02["B22"]) / 3.0
    e2_delta = rel_vec(x42_b22, x21_b22)
    e2_ratio = e2_delta / max(d21, 1e-30)
    e2_pass = e2_delta <= 0.35 * d21

    # E3: Richardson-reduced box-direction test against Q6.
    extrap: Dict[str, np.ndarray] = {
        name: (4.0 * rows02[name] - rows04[name]) / 3.0 for name, _rmax, _zmax in BOXES
    }
    raw04_err = {name: rel_vec(rows04[name], q6) for name, _rmax, _zmax in BOXES}
    raw02_err = {name: rel_vec(rows02[name], q6) for name, _rmax, _zmax in BOXES}
    ext_err = {name: rel_vec(extrap[name], q6) for name, _rmax, _zmax in BOXES}
    inter_resolution = {name: rel_vec(rows04[name], rows02[name]) for name, _rmax, _zmax in BOXES}
    richardson_correction = {name: rel_vec(rows02[name], extrap[name]) for name, _rmax, _zmax in BOXES}

    e3_checks = {
        "radial_22_32": ext_err["B32"] < ext_err["B22"],
        "radial_32_42": ext_err["B42"] < ext_err["B32"],
        "axial_22_23": ext_err["B23"] < ext_err["B22"],
        "axial_23_24": ext_err["B24"] < ext_err["B23"],
        "full": ext_err["B44"] <= min(ext_err["B42"], ext_err["B24"]),
    }

    checks: Dict[str, bool] = {}
    for k, v in e0_source_checks.items():
        checks[f"E0_source_{k}"] = bool(v)
    for k, v in e0_green_checks.items():
        checks[f"E0_green_{k}"] = bool(v)
    for k, v in poisson_checks.items():
        checks[f"poisson_{k}"] = bool(v)
    checks["E1_second_order_B22"] = bool(e1_pass)
    checks["E2_richardson_stabilization_B22"] = bool(e2_pass)
    for k, v in e3_checks.items():
        checks[f"E3_{k}"] = bool(v)

    source_ok = bool(all(e0_source_checks.values()))
    green_ok = bool(all(e0_green_checks.values()))
    poisson_ok = bool(all(poisson_checks.values()))
    e3_ok = bool(all(e3_checks.values()))

    if not source_ok:
        decision = "STOP_REPAIR_GREEN_SOURCE_REPRODUCTION"
        passed = False
    elif not green_ok:
        decision = "STOP_REPAIR_GREEN_QUADRATURE"
        passed = False
    elif not poisson_ok or not e1_pass or not e2_pass:
        decision = "STOP_REPAIR_ELLIPTIC_DISCRETIZATION"
        passed = False
    elif not e3_ok:
        decision = "STOP_REPAIR_DYNAMIC_DOMAIN"
        passed = False
    else:
        decision = "PASS"
        passed = True

    return {
        "schema": "r3-w1-elliptic-decomposition-v1",
        "frozen_parameters": {
            "dynamic_source": {"box": [4.0, 4.0], "h": 0.04, "T": v1.T_FINAL, "dt": v1.DT, "integrator": "rk4"},
            "elliptic_boxes": {name: [rmax, zmax] for name, rmax, zmax in BOXES},
            "elliptic_h": [0.04, 0.02],
            "validation_box": "B22",
            "validation_h": [0.04, 0.02, 0.01],
            "green_reference": {"name": "Q6", "source_cell_order": 6, "theta_order": 144},
            "green_source_isolation": {"source_cell_order": 4, "theta_order": 144, "tolerance": 7.5e-4},
            "green_angular_isolation": {"source_cell_order": 6, "theta_order": 96, "tolerance": 7.5e-4},
            "refinement_ratio_tolerance": 0.35,
            "richardson_formula": "(4*R_h/2 - R_h)/3",
            "receivers": [list(p) for p in RECEIVERS],
            "source_interpolation": "RectBivariateSpline(kx=3,ky=3,s=0)",
        },
        "E0_runtime_summary": summary,
        "E0_source_audit": source_audit,
        "E0_green": {
            "Q6": q6.tolist(),
            "Q4T": q4t.tolist(),
            "Q6T": q6t.tolist(),
            "source_isolation_relative": green_source_iso,
            "angular_isolation_relative": green_theta_iso,
        },
        "poisson_residuals": residuals,
        "receiver_rows_h04": {k: v.tolist() for k, v in rows04.items()},
        "receiver_rows_h02": {k: v.tolist() for k, v in rows02.items()},
        "receiver_row_B22_h01": b22_01.tolist(),
        "E1_B22_spatial_order": {
            "d42_rel_h04_h02": d42,
            "d21_rel_h02_h01": d21,
            "fine_over_coarse": e1_ratio,
        },
        "E2_B22_richardson_stabilization": {
            "X42": x42_b22.tolist(),
            "X21": x21_b22.tolist(),
            "relative_X42_X21": e2_delta,
            "relative_to_d21": e2_ratio,
        },
        "E3_richardson_receiver_rows": {k: v.tolist() for k, v in extrap.items()},
        "E3_richardson_error_to_Q6": ext_err,
        "descriptive_raw_h04_error_to_Q6": raw04_err,
        "descriptive_raw_h02_error_to_Q6": raw02_err,
        "descriptive_inter_resolution_h04_h02": inter_resolution,
        "descriptive_richardson_correction": richardson_correction,
        "descriptive_adjacent_box_changes_h04": adjacent_changes(rows04),
        "descriptive_adjacent_box_changes_h02": adjacent_changes(rows02),
        "descriptive_adjacent_box_changes_richardson": adjacent_changes(extrap),
        "checks": checks,
        "decision": decision,
        "pass": passed,
        "parent_statuses": {
            "PR112": "STOP_REPAIR_GREEN_QUADRATURE",
            "PR113": "PASS",
            "PR114": "STOP_REPAIR_DYNAMIC_DOMAIN",
        },
        "claim_boundary": "static elliptic discretization/boundary decomposition on frozen early-time source only",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/r3_wholespace_w1/results/W1_ELLIPTIC_DECOMPOSITION.json"),
    )
    args = parser.parse_args()
    result = run_gate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"decision": result["decision"], "output": str(args.output)}, indent=2))
    return 0 if result["pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
