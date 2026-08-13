#!/usr/bin/env python3
"""MNS-2 v2.13 — predictive bridge convergence/robustness lattice.

Runs the v2.12 predictive coefficient model on three deliberately separated axes:

1. spatial grid: 8x16, 12x24, 16x32 at fixed dt and physical time;
2. timestep: dt = 4e-8, 2e-8, 1e-8 at exactly fixed T = 4e-8;
3. physical-time robustness: T = 2e-8, 4e-8, 8e-8 at fixed dt = 2e-8.

There are seven unique configurations because the 12x24 / dt=2e-8 / 2-step
baseline is shared among all axes.

This script records scalar diagnostics only.  Cross-grid scalar stability is NOT an
operator/subspace convergence theorem and is NOT a discrete-to-continuum promotion.
"""
from __future__ import annotations

import argparse
import json
import math
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
V212 = REPO / "src" / "bridge" / "mns2_predictive_path_pod_bridge_v2.12.py"
GEN = REPO / "tests" / "data" / "generate_mns2_synthetic_seed_v2_2.py"
META = REPO / "tests" / "data" / "MNS2_SYNTHETIC_2COMP_BRIDGE_META_V2.2.json"
SCHEDULE = REPO / "tests" / "data" / "MNS2_SYNTHETIC_2COMP_BRIDGE_SCHEDULE_V2.2.json"

BASE_GRID = "12x24"
BASE_DT = 2e-8
BASE_STEPS = 2
BASE_T = BASE_DT * BASE_STEPS


def case_key(grid: str, dt: float, steps: int) -> str:
    return f"{grid}|dt={dt:.17g}|steps={steps}"


def summarize(raw: dict) -> dict:
    f = raw["final_record"]
    return {
        "grid": raw["grid"],
        "dt": raw["dt"],
        "steps": raw["steps"],
        "physical_time": raw["physical_time"],
        "rank": raw["rank"],
        "direct_endpoint_delta_metric_norm": raw["direct_endpoint_delta_metric_norm"],
        "zero_reference_tangent_metric_norm": raw["zero_reference_tangent_metric_norm"],
        "pod_eigenvalues_relative": raw["pod_eigenvalues_relative"],
        "predictive_endpoint_rel_error_vs_direct": f["predictive_endpoint_rel_error_vs_direct"],
        "true_bridge_rel_error_vs_direct": f["true_bridge_rel_error_vs_direct"],
        "predictive_vs_true_integral_rel_direct": f["predictive_vs_true_integral_rel_direct"],
        "quadrature_residual_integral_rel_direct": f["quadrature_residual_integral_rel_direct"],
        "quadrature_true_correction_norm_integral_abs": f[
            "quadrature_true_correction_norm_integral_abs"
        ],
        "predictive_residual_to_true_correction_integral_ratio": f[
            "predictive_residual_to_true_correction_integral_ratio"
        ],
        "numerical_triangle_ratio": f["numerical_triangle_ratio"],
        "certification_nodes_are_held_out_from_training": raw["important_invariants"][
            "certification_nodes_are_held_out_from_training"
        ],
        "same_frozen_schedule_all_amplitudes": raw["important_invariants"][
            "same_frozen_schedule_all_amplitudes"
        ],
    }


def relative_drift(a: float, b: float) -> float:
    return abs(a - b) / max(abs(b), 1e-300)


def adjacent_axis_diagnostics(records: list[dict]) -> list[dict]:
    out = []
    for prev, cur in zip(records[:-1], records[1:]):
        out.append(
            {
                "from": {
                    "grid": prev["grid"],
                    "dt": prev["dt"],
                    "steps": prev["steps"],
                    "physical_time": prev["physical_time"],
                },
                "to": {
                    "grid": cur["grid"],
                    "dt": cur["dt"],
                    "steps": cur["steps"],
                    "physical_time": cur["physical_time"],
                },
                "direct_endpoint_norm_relative_drift": relative_drift(
                    cur["direct_endpoint_delta_metric_norm"],
                    prev["direct_endpoint_delta_metric_norm"],
                ),
                "predictive_error_absolute_drift": abs(
                    cur["predictive_endpoint_rel_error_vs_direct"]
                    - prev["predictive_endpoint_rel_error_vs_direct"]
                ),
                "residual_to_correction_ratio_absolute_drift": abs(
                    cur["predictive_residual_to_true_correction_integral_ratio"]
                    - prev["predictive_residual_to_true_correction_integral_ratio"]
                ),
            }
        )
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="MNS2_V2.13_PREDICTIVE_CONVERGENCE_LATTICE")
    ap.add_argument("--panels", type=int, default=8)
    ap.add_argument("--rank", type=int, default=4)
    ap.add_argument("--max-predictive-error", type=float, default=2e-6)
    ap.add_argument("--max-residual-to-correction", type=float, default=0.15)
    args = ap.parse_args()

    if args.panels < 1:
        raise ValueError("panels must be positive")

    specs = [
        ("8x16", BASE_DT, BASE_STEPS),
        ("12x24", BASE_DT, BASE_STEPS),
        ("16x32", BASE_DT, BASE_STEPS),
        (BASE_GRID, 4e-8, 1),
        (BASE_GRID, 1e-8, 4),
        (BASE_GRID, BASE_DT, 1),
        (BASE_GRID, BASE_DT, 4),
    ]

    # Exact-representability gate for the fixed-time dt axis. No silent rounding.
    dt_axis_specs = [(BASE_GRID, 4e-8, 1), (BASE_GRID, BASE_DT, 2), (BASE_GRID, 1e-8, 4)]
    for grid, dt, steps in dt_axis_specs:
        if not math.isclose(dt * steps, BASE_T, rel_tol=0.0, abs_tol=1e-30):
            raise RuntimeError(f"dt-axis physical time is not exactly represented: {grid} {dt} {steps}")

    cache: dict[str, dict] = {}
    with tempfile.TemporaryDirectory(prefix="mns2_v213_") as td:
        td = Path(td)
        seed = td / "seed.npz"
        subprocess.run([sys.executable, str(GEN), str(seed)], check=True, stdout=subprocess.DEVNULL)

        for grid, dt, steps in specs:
            key = case_key(grid, dt, steps)
            if key in cache:
                continue
            out = td / ("case_" + str(len(cache)))
            subprocess.run(
                [
                    sys.executable,
                    str(V212),
                    str(seed),
                    str(META),
                    str(SCHEDULE),
                    "--grid",
                    grid,
                    "--dt",
                    repr(dt),
                    "--steps",
                    str(steps),
                    "--panels",
                    str(args.panels),
                    "--rank",
                    str(args.rank),
                    "--out",
                    str(out),
                ],
                check=True,
                stdout=subprocess.DEVNULL,
            )
            raw = json.loads(Path(str(out) + ".json").read_text())
            if raw["status"] != "PREDICTIVE-PATH-POD-BRIDGE-AUDIT-COMPLETE":
                raise RuntimeError(f"v2.12 failed for {key}")
            rec = summarize(raw)
            if not rec["certification_nodes_are_held_out_from_training"]:
                raise RuntimeError(f"training/certification leakage for {key}")
            if not rec["same_frozen_schedule_all_amplitudes"]:
                raise RuntimeError(f"schedule retuning detected for {key}")
            if rec["predictive_endpoint_rel_error_vs_direct"] > args.max_predictive_error:
                raise RuntimeError(f"predictive error gate failed for {key}: {rec}")
            if (
                rec["predictive_residual_to_true_correction_integral_ratio"]
                > args.max_residual_to_correction
            ):
                raise RuntimeError(f"correction-relative residual gate failed for {key}: {rec}")
            cache[key] = rec

    def get(grid, dt, steps):
        return cache[case_key(grid, dt, steps)]

    grid_axis = [
        get("8x16", BASE_DT, BASE_STEPS),
        get("12x24", BASE_DT, BASE_STEPS),
        get("16x32", BASE_DT, BASE_STEPS),
    ]
    dt_axis = [
        get(BASE_GRID, 4e-8, 1),
        get(BASE_GRID, BASE_DT, 2),
        get(BASE_GRID, 1e-8, 4),
    ]
    time_axis = [
        get(BASE_GRID, BASE_DT, 1),
        get(BASE_GRID, BASE_DT, 2),
        get(BASE_GRID, BASE_DT, 4),
    ]

    payload = {
        "status": "PREDICTIVE-CONVERGENCE-LATTICE-AUDIT-COMPLETE",
        "claim_scope": "finite-discrete scalar diagnostic lattice; not operator/subspace or continuum convergence",
        "baseline": {
            "grid": BASE_GRID,
            "dt": BASE_DT,
            "steps": BASE_STEPS,
            "physical_time": BASE_T,
            "panels": args.panels,
            "rank": args.rank,
        },
        "unique_case_count": len(cache),
        "cases": cache,
        "axes": {
            "grid": {
                "fixed_dt": BASE_DT,
                "fixed_steps": BASE_STEPS,
                "fixed_physical_time": BASE_T,
                "records": grid_axis,
                "adjacent_diagnostics": adjacent_axis_diagnostics(grid_axis),
            },
            "dt": {
                "fixed_grid": BASE_GRID,
                "fixed_physical_time": BASE_T,
                "exact_representability_checked": True,
                "records": dt_axis,
                "adjacent_diagnostics": adjacent_axis_diagnostics(dt_axis),
            },
            "physical_time": {
                "fixed_grid": BASE_GRID,
                "fixed_dt": BASE_DT,
                "records": time_axis,
                "adjacent_diagnostics": adjacent_axis_diagnostics(time_axis),
            },
        },
        "promotion_guardrails": {
            "scalar_grid_stability_is_not_operator_subspace_convergence": True,
            "grid_dt_physical_time_axes_kept_distinct": True,
            "no_silent_dt_rounding": True,
            "same_training_amplitudes_across_cases": True,
            "same_frozen_schedule_contract_across_cases": True,
            "residual_reported_relative_to_nonlinear_correction": True,
            "synthetic_seed_not_Hou_late_state": True,
            "no_discrete_to_continuum_promotion": True,
        },
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    Path(str(out) + ".json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
