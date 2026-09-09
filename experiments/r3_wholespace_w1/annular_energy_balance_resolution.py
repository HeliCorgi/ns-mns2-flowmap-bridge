#!/usr/bin/env python3
"""Preregistered annular energy-balance resolution audit.

Implements
  docs/gates/R3_AXISYM_WHOLESPACE_ANNULAR_ENERGY_BALANCE_RESOLUTION_PREREG_2026-09-09.md

This audits only the coarse-grid physical energy-balance diagnostic that
invalidated the annular rows of PR #119.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, Tuple

import manufactured_short_time as v1
import shape_family_screen as sfs

T_REPAIR = 0.002
ALPHAS: Tuple[float, ...] = (64.0, 128.0)
SHAPES: Tuple[str, ...] = ("A-Z0", "A-Z1", "A-Z2")
LEVELS: Tuple[Tuple[float, float], ...] = (
    (0.08, 0.002),
    (0.04, 0.0005),
    (0.02, 0.000125),
)

COARSE_REFERENCE = {
    "a64_A-Z0": 0.2769415986484736,
    "a64_A-Z1": 0.25902774147980734,
    "a64_A-Z2": 0.25263199842185224,
    "a128_A-Z0": 0.2769509735222076,
    "a128_A-Z1": 0.25903329857106117,
    "a128_A-Z2": 0.2526358254831897,
}


def runtime_preconditions(summary: Dict[str, object], expected_steps: int) -> Dict[str, bool]:
    return {
        "completed": bool(summary["completed"]),
        "expected_steps": int(summary["accepted_steps"]) == expected_steps,
        "no_reject": int(summary["rejected_steps"]) == 0,
        "finite": bool(summary["all_stage_finite"] and summary["all_step_finite"]),
        "amp": float(summary["max_frozen_symbol_amplification"]) <= 1.0 + v1.STABILITY_TOL,
        "cfl": float(summary["max_cfl"]) <= 0.10,
        "visc": float(summary["max_viscous_number"]) <= 0.05,
        "poisson": max(
            float(summary["max_stage_poisson_residual"]),
            float(summary["max_step_poisson_residual"]),
        ) <= 1e-10,
        "odd": float(summary["max_odd_z_defect"]) <= 1e-12,
        "energy": float(summary["max_energy_ratio_to_initial"]) <= 1.0 + 1e-5,
    }


def run_level(alpha: float, shape: str, h: float, dt: float) -> Dict[str, object]:
    v1.T_FINAL = T_REPAIR
    v1.DT = dt
    s = sfs.ShapeGridSolver(h, 2.0, 2.0)
    s.set_parameters(alpha, shape)
    run = v1.run_integrator(s, "rk4")
    summary = dict(v1.streamed_summary(run))
    summary["accepted_steps"] = len(run.step_rows)
    summary["expected_steps"] = int(round(T_REPAIR / dt))
    pre = runtime_preconditions(summary, int(round(T_REPAIR / dt)))
    return {
        "h": h,
        "dt": dt,
        "summary": summary,
        "runtime_preconditions": pre,
        "runtime_preconditions_pass": bool(all(pre.values())),
        "max_energy_balance_defect": float(summary["max_energy_balance_defect"]),
    }


def run_gate() -> Dict[str, object]:
    rows: Dict[str, object] = {}
    checks: Dict[str, bool] = {}

    for alpha in ALPHAS:
        for shape in SHAPES:
            key = f"a{alpha:g}_{shape}"
            print(f"audit {key}", flush=True)
            level_rows: Dict[str, object] = {}
            defects: Dict[str, float] = {}
            runtime_ok = True
            for h, dt in LEVELS:
                lr = run_level(alpha, shape, h, dt)
                hk = f"h{h:.2f}"
                level_rows[hk] = lr
                defects[hk] = float(lr["max_energy_balance_defect"])
                runtime_ok = runtime_ok and bool(lr["runtime_preconditions_pass"])

            d08 = defects["h0.08"]
            d04 = defects["h0.04"]
            d02 = defects["h0.02"]
            ref = COARSE_REFERENCE[key]
            row_checks = {
                "runtime_all_levels": runtime_ok,
                "R0_reproduce_coarse": abs(d08 - ref) <= 5e-5,
                "R1_strict_08_04": d04 < d08,
                "R1_strict_04_02": d02 < d04,
                "R1_ratio_04_08": d04 / max(d08, 1e-30) <= 0.40,
                "R1_ratio_02_04": d02 / max(d04, 1e-30) <= 0.40,
                "R2_D04": d04 <= 0.12,
                "R2_D02": d02 <= 0.05,
            }
            for ck, cv in row_checks.items():
                checks[f"{key}_{ck}"] = bool(cv)

            rows[key] = {
                "alpha": alpha,
                "shape": shape,
                "levels": level_rows,
                "coarse_reference_PR119": ref,
                "coarse_abs_difference": abs(d08 - ref),
                "defects": defects,
                "ratios": {
                    "D04_over_D08": d04 / max(d08, 1e-30),
                    "D02_over_D04": d02 / max(d04, 1e-30),
                },
                "checks": row_checks,
                "pass": bool(all(row_checks.values())),
            }
            print(
                f"{key}: D08={d08:.9g} D04={d04:.9g} D02={d02:.9g} "
                f"ratios=({d04/max(d08,1e-30):.4g},{d02/max(d04,1e-30):.4g})",
                flush=True,
            )

    passed = bool(all(checks.values()))
    decision = "PASS" if passed else "STOP_REPAIR_ANNULAR_ENERGY_BALANCE"
    return {
        "schema": "r3-annular-energy-balance-resolution-v1",
        "frozen_parameters": {
            "nu": v1.NU,
            "kappa": sfs.KAPPA,
            "alphas": list(ALPHAS),
            "shapes": list(SHAPES),
            "box": [2.0, 2.0],
            "Trepair": T_REPAIR,
            "levels": [{"h": h, "dt": dt} for h, dt in LEVELS],
            "dt_over_h2": 0.3125,
            "integrator": "rk4",
            "R0_abs_tolerance": 5e-5,
            "R1_ratio_limit": 0.40,
            "R2_D04_limit": 0.12,
            "R2_D02_limit": 0.05,
        },
        "rows": rows,
        "checks": checks,
        "decision": decision,
        "pass": passed,
        "parent_status": "PR119 annular rows INVALID_RUNTIME at h=.08; unchanged",
        "claim_boundary": "short-time annular physical energy-balance discretization audit only",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/r3_wholespace_w1/results/ANNULAR_ENERGY_BALANCE_RESOLUTION.json"),
    )
    args = parser.parse_args()
    result = run_gate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"decision": result["decision"], "output": str(args.output)}, indent=2))
    return 0 if result["pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
