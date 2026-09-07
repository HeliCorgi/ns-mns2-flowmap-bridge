"""Preregistered E1 SSPRK3 smoke gate for the R^3 axisymmetric-with-swirl track."""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

from whole_space_evolution_e1 import E1Config, WholeSpaceE1

HERE = Path(__file__).resolve().parent


def ssprk3_stability_polynomial(z):
    return 1.0 + z + 0.5 * z * z + (z * z * z) / 6.0


def sampled_linear_stability_box(cfl_limit: float, viscous_limit: float) -> dict:
    # For frozen centered advection plus nonpositive real diffusion, scan the preregistered
    # rectangle z=-a+i*b. This is a sampled smoke cross-check, not a proof for the
    # variable-coefficient nonlinear operator.
    a = np.linspace(0.0, viscous_limit, 401)
    b = np.linspace(-cfl_limit, cfl_limit, 401)
    A, B = np.meshgrid(a, b, indexing="ij")
    amp = np.abs(ssprk3_stability_polynomial(-A + 1j * B))
    return {
        "max_amplification": float(np.max(amp)),
        "cfl_limit": cfl_limit,
        "viscous_limit": viscous_limit,
        "grid": [401, 401],
        "pass": bool(np.max(amp) <= 1.0 + 5.0e-13),
    }


def main() -> None:
    cfg = E1Config()
    stability = sampled_linear_stability_box(cfg.cfl_limit, cfg.viscous_limit)
    runner = WholeSpaceE1(cfg)
    result = runner.run()

    scientific_gate = bool(
        stability["pass"]
        and result["accepted_steps"] > 0
        and result["rejected_steps"] <= cfg.max_rejected_steps
        and result["min_dt"] >= cfg.min_dt
        and max(
            result["max_cfl_pre"],
            result["max_cfl_stage1"],
            result["max_cfl_stage2"],
            result["max_cfl_post"],
        )
        <= cfg.cfl_limit * (1.0 + 1.0e-12)
        and result["max_viscous_number"] <= cfg.viscous_limit * (1.0 + 1.0e-12)
        and result["max_positive_single_step_relative_energy_change"] <= 1.0e-4
        and result["gamma_max_principle_overshoot_relative"] <= 1.0e-3
        and result["max_axis_regular_defect"] <= 1.0e-12
        and result["max_divergence_rel_linf"] <= 1.0e-2
        and result["max_elliptic_residual_linf"] <= 1.0e-8
        and result["min_gradient_scale_points"] >= 1.0
        and math.isfinite(result["max_curvature_tail"])
        and result["max_boundary_shell_ratio"] <= 1.0e-6
        and result["initial"]["finite"]
        and result["final"]["finite"]
    )
    result["sampled_linear_stability_box"] = stability
    result["E1_pass"] = scientific_gate
    result["E1_gate"] = {
        "max_positive_single_step_relative_energy_change": 1.0e-4,
        "gamma_max_principle_overshoot_relative": 1.0e-3,
        "max_axis_regular_defect": 1.0e-12,
        "max_divergence_rel_linf": 1.0e-2,
        "max_elliptic_residual_linf": 1.0e-8,
        "min_gradient_scale_points": 1.0,
        "max_boundary_shell_ratio": 1.0e-6,
        "curvature_tail": "streamed and required finite; refinement verdict deferred to E2",
    }

    outdir = HERE / "results_evolution_e1"
    outdir.mkdir(parents=True, exist_ok=True)
    path = outdir / "summary.json"
    path.write_text(json.dumps(result, indent=2, allow_nan=False))
    print(
        f"sampled SSPRK3 box max_amp={stability['max_amplification']:.12e} "
        f"pass={stability['pass']}"
    )
    for key in (
        "accepted_steps",
        "rejected_steps",
        "min_dt",
        "max_cfl_pre",
        "max_cfl_stage1",
        "max_cfl_stage2",
        "max_cfl_post",
        "max_viscous_number",
        "max_positive_single_step_relative_energy_change",
        "gamma_max_principle_overshoot_relative",
        "max_axis_regular_defect",
        "max_divergence_rel_linf",
        "max_elliptic_residual_linf",
        "min_gradient_scale_points",
        "max_curvature_tail",
        "max_boundary_shell_ratio",
    ):
        print(f"{key}={result[key]}")
    print(f"E1_pass={scientific_gate} summary={path}")
    if not scientific_gate:
        raise SystemExit("R3 E1 FAIL")


if __name__ == "__main__":
    main()
