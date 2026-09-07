#!/usr/bin/env python3
"""Versioned early-time dynamic-domain audit using the repaired Q6 Green reference.

Implements
`docs/gates/R3_AXISYM_WHOLESPACE_W1_DYNAMIC_DOMAIN_V2_PREREG_2026-09-07.md`.
The stopped PR #112 result remains unchanged.
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

H = 0.04
CORE_R = 0.80
CORE_Z = 0.80
BOXES: Tuple[Tuple[str, float, float], ...] = (
    ("B22", 2.0, 2.0),
    ("B32", 3.0, 2.0),
    ("B42", 4.0, 2.0),
    ("B23", 2.0, 3.0),
    ("B24", 2.0, 4.0),
    ("B44", 4.0, 4.0),
)
RECEIVERS = gq.RECEIVERS


def dynamic_run(rmax: float, zmax: float) -> Dict[str, object]:
    s = gq.DomainGridSolver(H, rmax, zmax)
    run = v1.run_integrator(s, "rk4")
    summary = dict(v1.streamed_summary(run))
    result: Dict[str, object] = {
        "r": s.r.copy(),
        "z": s.z.copy(),
        "u": run.final_u.copy(),
        "w": run.final_w.copy(),
        "summary": summary,
        "accepted_steps": len(run.step_rows),
    }
    del run, s
    gc.collect()
    return result


def core_view(row: Dict[str, object], field: str) -> np.ndarray:
    r = np.asarray(row["r"], dtype=float)
    z = np.asarray(row["z"], dtype=float)
    f = np.asarray(row[field], dtype=float)
    ii = np.where(r <= CORE_R + 1e-14)[0]
    jj = np.where(np.abs(z) <= CORE_Z + 1e-14)[0]
    return f[np.ix_(ii, jj)]


def combined_state_difference(a: Dict[str, object], b: Dict[str, object]) -> float:
    ua = core_view(a, "u")
    wa = core_view(a, "w")
    ub = core_view(b, "u")
    wb = core_view(b, "w")
    if ua.shape != ub.shape or wa.shape != wb.shape:
        raise RuntimeError("common-core grids are not aligned")
    du = ua - ub
    dw = wa - wb
    num = math.sqrt(float(np.sum(du * du) + np.sum(dw * dw)))
    den = math.sqrt(float(np.sum(ub * ub) + np.sum(wb * wb)))
    return num / max(den, 1e-30)


def restrict_full_source(
    full_r: np.ndarray,
    full_z: np.ndarray,
    full_w: np.ndarray,
    small_r: np.ndarray,
    small_z: np.ndarray,
) -> np.ndarray:
    if abs(full_r[0]) > 1e-14:
        raise RuntimeError("unexpected radial origin")
    i1 = int(round(small_r[-1] / H))
    j0 = int(round((small_z[0] - full_z[0]) / H))
    j1 = j0 + len(small_z)
    out = np.asarray(full_w[: i1 + 1, j0:j1], dtype=float).copy()
    if out.shape != (len(small_r), len(small_z)):
        raise RuntimeError("source restriction shape mismatch")
    if np.max(np.abs(full_r[: i1 + 1] - small_r)) > 2e-13:
        raise RuntimeError("radial grids not aligned")
    if np.max(np.abs(full_z[j0:j1] - small_z)) > 2e-13:
        raise RuntimeError("axial grids not aligned")
    return out


def receiver_vector(s: gq.DomainGridSolver, psi: np.ndarray) -> np.ndarray:
    out = np.zeros((len(RECEIVERS), 3), dtype=float)
    for k, (rr, zz) in enumerate(RECEIVERS):
        i = int(round(rr / H))
        j = int(round((zz - s.z[0]) / H))
        if abs(s.r[i] - rr) > 2e-13 or abs(s.z[j] - zz) > 2e-13:
            raise RuntimeError("receiver not aligned")
        out[k, 0] = psi[i, j]
        out[k, 1] = (psi[i + 1, j] - psi[i - 1, j]) / (2.0 * H)
        out[k, 2] = (psi[i, j + 1] - psi[i, j - 1]) / (2.0 * H)
    return out


def rel_vec(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.linalg.norm((a - b).ravel()) / max(np.linalg.norm(b.ravel()), 1e-30))


def run_gate() -> Dict[str, object]:
    dynamic: Dict[str, Dict[str, object]] = {}
    for name, rmax, zmax in BOXES:
        print(f"dynamic run {name} box=({rmax},{zmax})", flush=True)
        dynamic[name] = dynamic_run(rmax, zmax)

    checks: Dict[str, bool] = {}
    dyn_summary: Dict[str, Dict[str, object]] = {}

    # A0: inherited runtime gate.
    for name, _rmax, _zmax in BOXES:
        ss = dict(dynamic[name]["summary"])
        ss["accepted_steps"] = int(dynamic[name]["accepted_steps"])
        dyn_summary[name] = ss
        checks[f"A0_{name}_eight_steps"] = int(ss["accepted_steps"]) == 8
        checks[f"A0_{name}_completed"] = bool(ss["completed"])
        checks[f"A0_{name}_no_reject"] = int(ss["rejected_steps"]) == 0
        checks[f"A0_{name}_finite"] = bool(ss["all_stage_finite"] and ss["all_step_finite"])
        checks[f"A0_{name}_amp"] = float(ss["max_frozen_symbol_amplification"]) <= 1.0 + v1.STABILITY_TOL
        checks[f"A0_{name}_cfl"] = float(ss["max_cfl"]) <= 0.10
        checks[f"A0_{name}_visc"] = float(ss["max_viscous_number"]) <= 0.05
        checks[f"A0_{name}_poisson"] = max(
            float(ss["max_stage_poisson_residual"]), float(ss["max_step_poisson_residual"])
        ) <= 1e-10
        checks[f"A0_{name}_odd"] = float(ss["max_odd_z_defect"]) <= 1e-12
        checks[f"A0_{name}_energy"] = float(ss["max_energy_ratio_to_initial"]) <= 1.0 + 1e-5
        checks[f"A0_{name}_energy_balance"] = float(ss["max_energy_balance_defect"]) <= 0.20

    # A1: inherited floor-aware common-core sensitivity.
    dR23 = combined_state_difference(dynamic["B22"], dynamic["B32"])
    dR34 = combined_state_difference(dynamic["B32"], dynamic["B42"])
    dZ23 = combined_state_difference(dynamic["B22"], dynamic["B23"])
    dZ34 = combined_state_difference(dynamic["B23"], dynamic["B24"])
    dR_full = combined_state_difference(dynamic["B42"], dynamic["B44"])
    dZ_full = combined_state_difference(dynamic["B24"], dynamic["B44"])
    dynamic_sensitivity = {
        "radial_B22_B32": dR23,
        "radial_B32_B42": dR34,
        "axial_B22_B23": dZ23,
        "axial_B23_B24": dZ34,
        "descriptive_B42_B44": dR_full,
        "descriptive_B24_B44": dZ_full,
    }
    checks["A1_radial"] = bool(max(dR23, dR34) <= 1e-10 or dR34 <= 0.50 * dR23)
    checks["A1_axial"] = bool(max(dZ23, dZ34) <= 1e-10 or dZ34 <= 0.50 * dZ23)

    # A2: inherited common B44 source audit.
    full = dynamic["B44"]
    full_r = np.asarray(full["r"], dtype=float)
    full_z = np.asarray(full["z"], dtype=float)
    full_w = np.asarray(full["w"], dtype=float)
    source_audit = gq.lifted_source_audit(full_r, full_z, full_w)
    checks["A2_source_containment"] = float(source_audit["outside_B22_fraction"]) <= 1e-12
    checks["A2_odd_monopole"] = float(source_audit["normalized_odd_monopole"]) <= 1e-12

    # A3-v2: independently passed repaired reference, reproduced on this exact source.
    evaluator = gq.CellwiseGreenEvaluator(full_r, full_z, full_w)
    print("A3-v2 evaluating Q6", flush=True)
    q6 = evaluator.evaluate(6, 144)
    print("A3-v2 evaluating Q4T", flush=True)
    q4t = evaluator.evaluate(4, 144)
    print("A3-v2 evaluating Q6T", flush=True)
    q6t = evaluator.evaluate(6, 96)
    a3_source = rel_vec(q4t, q6)
    a3_theta = rel_vec(q6t, q6)
    checks["A3_source_isolation"] = a3_source <= 7.5e-4
    checks["A3_angular_isolation"] = a3_theta <= 7.5e-4

    # A4: original same-source finite-box / Green direction rules, unchanged.
    receiver_rows: Dict[str, List[List[float]]] = {}
    ebox: Dict[str, float] = {}
    for name, rmax, zmax in BOXES:
        s = gq.DomainGridSolver(H, rmax, zmax)
        src = restrict_full_source(full_r, full_z, full_w, s.r, s.z)
        psi, pres = s.solve_psi(src)
        checks[f"A4_{name}_poisson"] = pres <= 1e-10
        rv = receiver_vector(s, psi)
        receiver_rows[name] = rv.tolist()
        ebox[name] = rel_vec(rv, q6)
        del s, src, psi
        gc.collect()

    checks["A4_radial_22_32"] = ebox["B32"] < ebox["B22"]
    checks["A4_radial_32_42"] = ebox["B42"] < ebox["B32"]
    checks["A4_axial_22_23"] = ebox["B23"] < ebox["B22"]
    checks["A4_axial_23_24"] = ebox["B24"] < ebox["B23"]
    checks["A4_full"] = ebox["B44"] <= min(ebox["B42"], ebox["B24"])

    receiver_changes = {
        "radial_small_mid": rel_vec(np.asarray(receiver_rows["B22"]), np.asarray(receiver_rows["B32"])),
        "radial_mid_large": rel_vec(np.asarray(receiver_rows["B32"]), np.asarray(receiver_rows["B42"])),
        "axial_small_mid": rel_vec(np.asarray(receiver_rows["B22"]), np.asarray(receiver_rows["B23"])),
        "axial_mid_large": rel_vec(np.asarray(receiver_rows["B23"]), np.asarray(receiver_rows["B24"])),
    }

    a0_a2_keys = [k for k in checks if k.startswith("A0_") or k.startswith("A1_") or k.startswith("A2_")]
    a4_poisson_keys = [k for k in checks if k.startswith("A4_") and k.endswith("_poisson")]
    prereq_pass = bool(all(checks[k] for k in a0_a2_keys + a4_poisson_keys))
    a3_pass = bool(checks["A3_source_isolation"] and checks["A3_angular_isolation"])
    a4_direction_keys = [
        "A4_radial_22_32",
        "A4_radial_32_42",
        "A4_axial_22_23",
        "A4_axial_23_24",
        "A4_full",
    ]
    a4_direction_pass = bool(all(checks[k] for k in a4_direction_keys))

    if not prereq_pass:
        decision = "STOP_REPAIR_DYNAMIC_DOMAIN"
        passed = False
    elif not a3_pass:
        decision = "STOP_REPAIR_GREEN_QUADRATURE"
        passed = False
    elif not a4_direction_pass:
        decision = "STOP_REPAIR_DYNAMIC_DOMAIN"
        passed = False
    else:
        decision = "PASS"
        passed = True

    return {
        "schema": "r3-w1-dynamic-domain-audit-v2",
        "frozen_parameters": {
            "nu": v1.NU,
            "A": v1.A0,
            "R": 1.0,
            "Z": 1.0,
            "alpha": 16.0,
            "kappa": 1.0,
            "integrator": "rk4",
            "h": H,
            "T": v1.T_FINAL,
            "dt": v1.DT,
            "boxes": {name: [rmax, zmax] for name, rmax, zmax in BOXES},
            "core": {"r_max": CORE_R, "abs_z_max": CORE_Z},
            "receivers": [list(p) for p in RECEIVERS],
            "green_reference": {"source_cell_order": 6, "theta_order": 144, "name": "Q6"},
            "green_source_isolation": {"source_cell_order": 4, "theta_order": 144, "tolerance": 7.5e-4},
            "green_angular_isolation": {"source_cell_order": 6, "theta_order": 96, "tolerance": 7.5e-4},
        },
        "A0_dynamic_summaries": dyn_summary,
        "A1_dynamic_state_sensitivity": dynamic_sensitivity,
        "A2_common_source_audit": source_audit,
        "A3_repaired_green": {
            "Q6_receivers": q6.tolist(),
            "Q4T_receivers": q4t.tolist(),
            "Q6T_receivers": q6t.tolist(),
            "source_isolation_relative": a3_source,
            "angular_isolation_relative": a3_theta,
        },
        "A4_receiver_rows": receiver_rows,
        "A4_receiver_relative_error_to_Q6": ebox,
        "A4_adjacent_receiver_changes": receiver_changes,
        "checks": checks,
        "decision": decision,
        "pass": passed,
        "parent_v1_status": "PR112 R3-W1-DYNAMIC-DOMAIN-AUDIT = STOP_REPAIR_GREEN_QUADRATURE (unchanged)",
        "green_repair_status": "PR113 R3-W1-GREEN-QUADRATURE-REPAIR = PASS",
        "claim_boundary": "early-time finite-box dynamic-domain / elliptic-boundary numerical audit v2 only",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/r3_wholespace_w1/results/W1_DYNAMIC_DOMAIN_AUDIT_V2.json"),
    )
    args = parser.parse_args()
    result = run_gate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"decision": result["decision"], "output": str(args.output)}, indent=2))
    return 0 if result["pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
