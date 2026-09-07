"""Bounded preregistered E2R rescue for the R^3 axisymmetric-with-swirl track."""
from __future__ import annotations

from dataclasses import asdict
import json
import math
from pathlib import Path
from typing import Any

import numpy as np

from check_evolution_e1 import sampled_linear_stability_box
from check_evolution_e2 import (
    FIELD_NAMES,
    compare,
    field_bundle,
    inherited_e1_pass,
    interpolate_bundle,
    replay_final_state,
    sha256_file,
)
from whole_space_evolution_e1 import E1Config, WholeSpaceE1


HERE = Path(__file__).resolve().parent
OUTDIR = HERE / "results_evolution_e2r"

RUN_CONFIGS: dict[str, E1Config] = {
    "B160": E1Config(nr=160, nz=288, Rmax=1.0, Zmax=0.9, dt_cap=1.0e-3),
    "B200": E1Config(nr=200, nz=360, Rmax=1.0, Zmax=0.9, dt_cap=1.0e-3),
    "B240": E1Config(nr=240, nz=432, Rmax=1.0, Zmax=0.9, dt_cap=1.0e-3),
    "B240H": E1Config(nr=240, nz=432, Rmax=1.0, Zmax=0.9, dt_cap=1.5e-4),
    "RPLUS2": E1Config(nr=240, nz=360, Rmax=1.2, Zmax=0.9, dt_cap=1.0e-3),
    "ZPLUS2": E1Config(nr=200, nz=440, Rmax=1.0, Zmax=1.1, dt_cap=1.0e-3),
}


def main() -> None:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    stability = sampled_linear_stability_box(0.40, 0.80)

    results: dict[str, dict[str, Any]] = {}
    runners: dict[str, WholeSpaceE1] = {}
    final_states: dict[str, tuple[np.ndarray, np.ndarray]] = {}

    for name, cfg in RUN_CONFIGS.items():
        print(f"E2R run {name}: {asdict(cfg)}")
        runner = WholeSpaceE1(cfg)
        result = runner.run()
        result["inherited_E1_pass"] = inherited_e1_pass(result, cfg, stability)
        u1, omega1 = replay_final_state(runner)
        replay_diag = runner.diagnostics(u1, omega1)
        if not math.isclose(
            replay_diag.energy,
            float(result["final"]["energy"]),
            rel_tol=2.0e-13,
            abs_tol=2.0e-15,
        ):
            raise RuntimeError(f"{name}: deterministic replay energy mismatch")
        if not math.isclose(
            replay_diag.max_abs_omega1,
            float(result["final"]["max_abs_omega1"]),
            rel_tol=2.0e-13,
            abs_tol=2.0e-13,
        ):
            raise RuntimeError(f"{name}: deterministic replay omega mismatch")
        results[name] = result
        runners[name] = runner
        final_states[name] = (u1, omega1)
        print(
            f"  inherited_E1_pass={result['inherited_E1_pass']} "
            f"steps={result['accepted_steps']} max_dt={result['max_dt']:.9e} "
            f"scale={result['min_gradient_scale_points']:.6f} "
            f"tail={result['max_curvature_tail']:.6f}"
        )

    common_r = np.linspace(0.0, 0.55, 65)
    common_z = np.linspace(-0.45, 0.45, 97)
    common: dict[str, dict[str, np.ndarray]] = {}
    for name in RUN_CONFIGS:
        u1, omega1 = final_states[name]
        common[name] = interpolate_bundle(
            runners[name],
            field_bundle(runners[name], u1, omega1),
            common_r,
            common_z,
        )

    comparisons = {
        "B160_B200": compare(common["B160"], common["B200"], common_r, common_z),
        "B200_B240": compare(common["B200"], common["B240"], common_r, common_z),
        "B240_B240H": compare(common["B240"], common["B240H"], common_r, common_z),
        "B200_RPLUS2": compare(common["B200"], common["RPLUS2"], common_r, common_z),
        "B200_ZPLUS2": compare(common["B200"], common["ZPLUS2"], common_r, common_z),
    }

    failures: list[str] = []
    for name, result in results.items():
        if not result["inherited_E1_pass"]:
            failures.append(f"{name}: inherited E1 gate FAIL")

    spatial_coarse = comparisons["B160_B200"]
    spatial_fine = comparisons["B200_B240"]
    for field in FIELD_NAMES:
        for norm in ("relative_linf", "relative_l2"):
            if not spatial_fine[field][norm] < spatial_coarse[field][norm]:
                failures.append(
                    f"spatial {field} {norm}: "
                    f"fine={spatial_fine[field][norm]:.12e} "
                    f">= coarse={spatial_coarse[field][norm]:.12e}"
                )

    scales = [results[n]["min_gradient_scale_points"] for n in ("B160", "B200", "B240")]
    if not (scales[0] < scales[1] < scales[2]):
        failures.append(f"spatial min-gradient-scale not increasing: {scales}")
    if not scales[2] >= 2.0:
        failures.append(f"B240 min-gradient-scale {scales[2]:.12e} < 2.0")

    tails = [results[n]["max_curvature_tail"] for n in ("B160", "B200", "B240")]
    if not (tails[0] > tails[1] > tails[2]):
        failures.append(f"spatial curvature-tail not decreasing: {tails}")
    if not tails[2] <= 1.0:
        failures.append(f"B240 curvature-tail {tails[2]:.12e} > 1.0")

    if not results["B240H"]["max_dt"] <= 0.51 * results["B240"]["max_dt"]:
        failures.append(
            f"time ratio: B240H max_dt={results['B240H']['max_dt']:.12e} "
            f"> 0.51*B240={0.51 * results['B240']['max_dt']:.12e}"
        )

    time_diff = comparisons["B240_B240H"]
    for field in FIELD_NAMES:
        for norm in ("relative_linf", "relative_l2"):
            if not time_diff[field][norm] <= spatial_fine[field][norm]:
                failures.append(
                    f"time {field} {norm}: "
                    f"dt2={time_diff[field][norm]:.12e} "
                    f"> fine-space={spatial_fine[field][norm]:.12e}"
                )

    for pair in ("B200_RPLUS2", "B200_ZPLUS2"):
        for field in FIELD_NAMES:
            for norm in ("relative_linf", "relative_l2"):
                value = comparisons[pair][field][norm]
                if not value <= 1.0e-3:
                    failures.append(
                        f"domain {pair} {field} {norm}: {value:.12e} > 1e-3"
                    )

    npz_path = OUTDIR / "final_states.npz"
    payload: dict[str, np.ndarray] = {}
    for name, (u1, omega1) in final_states.items():
        payload[f"{name}_u1"] = u1
        payload[f"{name}_omega1"] = omega1
    np.savez(npz_path, **payload)
    with np.load(npz_path) as reloaded:
        reload_equal = all(np.array_equal(payload[key], reloaded[key]) for key in payload)
    if not reload_equal:
        failures.append("NPZ exact reload mismatch")
    npz_sha256 = sha256_file(npz_path)

    comparison_extrema: dict[str, dict[str, float]] = {}
    for pair, table in comparisons.items():
        comparison_extrema[pair] = {
            "max_relative_linf": max(v["relative_linf"] for v in table.values()),
            "max_relative_l2": max(v["relative_l2"] for v in table.values()),
        }

    summary = {
        "classification": "NUMERICAL CANDIDATE INFRASTRUCTURE / BOUNDED E2R RESCUE",
        "preregistration": "R3_EVOLUTION_E2R_PREREG_2026-09-07.md",
        "precision": "float64",
        "stability_box": stability,
        "run_configs": {name: asdict(cfg) for name, cfg in RUN_CONFIGS.items()},
        "run_results": results,
        "common_grid": {
            "r_min": 0.0,
            "r_max": 0.55,
            "nr": 65,
            "z_min": -0.45,
            "z_max": 0.45,
            "nz": 97,
        },
        "comparisons": comparisons,
        "comparison_extrema": comparison_extrema,
        "npz_exact_reload_equal": reload_equal,
        "npz_sha256": npz_sha256,
        "failures": failures,
        "E2R_pass": len(failures) == 0,
        "bounded_stop": (
            "If E2R fails, park the R3S04 + centered-FD + zero-Dirichlet stack; "
            "do not add another rescue lattice without a genuinely new numerical-method contract."
        ),
        "nonclaim": (
            "E2R is a finite-resolution numerical qualification gate only. "
            "It proves neither continuum convergence nor singularity/global regularity."
        ),
    }

    summary_path = OUTDIR / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, allow_nan=False))

    print("E2R comparison extrema:")
    for pair, ext in comparison_extrema.items():
        print(
            f"  {pair}: max_rel_Linf={ext['max_relative_linf']:.6e} "
            f"max_rel_L2={ext['max_relative_l2']:.6e}"
        )
    print(f"npz_reload_equal={reload_equal} npz_sha256={npz_sha256}")
    print(
        f"E2R_pass={summary['E2R_pass']} failures={len(failures)} "
        f"summary={summary_path}"
    )
    for failure in failures:
        print(f"FAIL: {failure}")
    if failures:
        raise SystemExit("R3 E2R FAIL")


if __name__ == "__main__":
    main()
