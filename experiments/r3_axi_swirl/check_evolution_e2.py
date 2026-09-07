"""Preregistered E2 same-continuum-datum convergence lattice for the R^3 swirl track."""
from __future__ import annotations

from dataclasses import asdict
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import numpy as np
from scipy.interpolate import RegularGridInterpolator

from check_evolution_e1 import sampled_linear_stability_box
from whole_space_evolution_e1 import E1Config, WholeSpaceE1

HERE = Path(__file__).resolve().parent
OUTDIR = HERE / "results_evolution_e2"

RUN_CONFIGS: dict[str, E1Config] = {
    "S96": E1Config(nr=96, nz=168, Rmax=0.8, Zmax=0.7, dt_cap=1.0e-3),
    "S128": E1Config(nr=128, nz=224, Rmax=0.8, Zmax=0.7, dt_cap=1.0e-3),
    "S160": E1Config(nr=160, nz=280, Rmax=0.8, Zmax=0.7, dt_cap=1.0e-3),
    "S160H": E1Config(nr=160, nz=280, Rmax=0.8, Zmax=0.7, dt_cap=2.25e-4),
    "RPLUS": E1Config(nr=160, nz=224, Rmax=1.0, Zmax=0.7, dt_cap=1.0e-3),
    "ZPLUS": E1Config(nr=128, nz=288, Rmax=0.8, Zmax=0.9, dt_cap=1.0e-3),
}

FIELD_NAMES = (
    "u1",
    "omega1",
    "ur",
    "uz",
    "utheta",
    "u1_r",
    "u1_z",
    "omega1_r",
    "omega1_z",
    "ur_r",
    "ur_z",
    "uz_r",
    "uz_z",
    "utheta_r",
    "utheta_z",
)


def inherited_e1_pass(result: dict[str, Any], cfg: E1Config, stability: dict[str, Any]) -> bool:
    return bool(
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


def replay_final_state(runner: WholeSpaceE1) -> tuple[np.ndarray, np.ndarray]:
    """Deterministically replay the exact fail-closed step selector and return the final arrays."""
    u1, omega1 = runner.initial_state()
    t = 0.0
    rejected = 0
    cfg = runner.cfg
    while t < cfg.T - 1.0e-15:
        dt = runner.choose_dt(omega1, cfg.T - t)
        if dt < cfg.min_dt:
            raise RuntimeError(f"E2 replay dt underflow before attempt: {dt}")
        while True:
            u_new, o_new, stage = runner.ssprk3_attempt(u1, omega1, dt)
            stage_cfl = max(
                stage["cfl_pre"], stage["cfl_stage1"], stage["cfl_stage2"], stage["cfl_post"]
            )
            stage_finite = bool(np.all(np.isfinite(u_new)) and np.all(np.isfinite(o_new)))
            if (
                stage_finite
                and stage_cfl <= cfg.cfl_limit * (1.0 + 1.0e-12)
                and stage["viscous_number"] <= cfg.viscous_limit * (1.0 + 1.0e-12)
            ):
                break
            rejected += 1
            if rejected > cfg.max_rejected_steps:
                raise RuntimeError("E2 replay exceeded max_rejected_steps")
            dt *= 0.5
            if dt < cfg.min_dt:
                raise RuntimeError("E2 replay dt underflow after stage rejection")
        u1, omega1 = u_new, o_new
        t += dt
    return np.asarray(u1), np.asarray(omega1)


def field_bundle(runner: WholeSpaceE1, u1: np.ndarray, omega1: np.ndarray) -> dict[str, np.ndarray]:
    _, ur, uz = runner.reconstruct(omega1)
    utheta = runner.r[:, None] * u1
    bundle = {
        "u1": u1,
        "omega1": omega1,
        "ur": ur,
        "uz": uz,
        "utheta": utheta,
        "u1_r": runner.d_r_even(u1),
        "u1_z": runner.d_z_zero(u1),
        "omega1_r": runner.d_r_even(omega1),
        "omega1_z": runner.d_z_zero(omega1),
        "ur_r": runner.d_r_odd(ur),
        "ur_z": runner.d_z_zero(ur),
        "uz_r": runner.d_r_even(uz),
        "uz_z": runner.d_z_zero(uz),
        "utheta_r": runner.d_r_odd(utheta),
        "utheta_z": runner.d_z_zero(utheta),
    }
    if tuple(bundle) != FIELD_NAMES:
        raise AssertionError("E2 comparison field registry mismatch")
    if not all(np.all(np.isfinite(v)) for v in bundle.values()):
        raise RuntimeError("non-finite E2 comparison field")
    return bundle


def interpolate_bundle(
    runner: WholeSpaceE1, bundle: dict[str, np.ndarray], common_r: np.ndarray, common_z: np.ndarray
) -> dict[str, np.ndarray]:
    R, Z = np.meshgrid(common_r, common_z, indexing="ij")
    pts = np.column_stack([R.ravel(), Z.ravel()])
    out: dict[str, np.ndarray] = {}
    for name, arr in bundle.items():
        interp = RegularGridInterpolator(
            (runner.r, runner.z), np.asarray(arr), method="linear", bounds_error=True
        )
        out[name] = interp(pts).reshape(R.shape)
    return out


def weighted_l2(common_r: np.ndarray, common_z: np.ndarray, f: np.ndarray) -> float:
    R = common_r[:, None]
    density = 2.0 * math.pi * R * np.asarray(f, dtype=float) ** 2
    int_z = np.trapezoid(density, common_z, axis=1)
    return math.sqrt(max(0.0, float(np.trapezoid(int_z, common_r, axis=0))))


def compare(
    a: dict[str, np.ndarray], b: dict[str, np.ndarray], common_r: np.ndarray, common_z: np.ndarray
) -> dict[str, dict[str, float]]:
    out: dict[str, dict[str, float]] = {}
    for name in FIELD_NAMES:
        fa = a[name]
        fb = b[name]
        diff = fa - fb
        linf_den = max(float(np.max(np.abs(fa))), float(np.max(np.abs(fb))), 1.0e-14)
        l2a = weighted_l2(common_r, common_z, fa)
        l2b = weighted_l2(common_r, common_z, fb)
        l2_den = max(l2a, l2b, 1.0e-14)
        out[name] = {
            "relative_linf": float(np.max(np.abs(diff)) / linf_den),
            "relative_l2": float(weighted_l2(common_r, common_z, diff) / l2_den),
        }
    return out


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    stability = sampled_linear_stability_box(0.40, 0.80)
    results: dict[str, dict[str, Any]] = {}
    runners: dict[str, WholeSpaceE1] = {}
    final_states: dict[str, tuple[np.ndarray, np.ndarray]] = {}

    for name, cfg in RUN_CONFIGS.items():
        print(f"E2 run {name}: {asdict(cfg)}")
        runner = WholeSpaceE1(cfg)
        result = runner.run()
        result["inherited_E1_pass"] = inherited_e1_pass(result, cfg, stability)
        u1, omega1 = replay_final_state(runner)
        replay_diag = runner.diagnostics(u1, omega1)
        # The replay uses the same deterministic selector. Assert that it really reproduces the
        # final summary before its arrays are consumed by the cross-grid comparison.
        if not math.isclose(
            replay_diag.energy, float(result["final"]["energy"]), rel_tol=2.0e-13, abs_tol=2.0e-15
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
            f"  inherited_E1_pass={result['inherited_E1_pass']} steps={result['accepted_steps']} "
            f"max_dt={result['max_dt']:.9e} scale={result['min_gradient_scale_points']:.6f} "
            f"tail={result['max_curvature_tail']:.6f}"
        )

    common_r = np.linspace(0.0, 0.55, 65)
    common_z = np.linspace(-0.45, 0.45, 97)
    common: dict[str, dict[str, np.ndarray]] = {}
    for name in RUN_CONFIGS:
        u1, omega1 = final_states[name]
        common[name] = interpolate_bundle(
            runners[name], field_bundle(runners[name], u1, omega1), common_r, common_z
        )

    comparisons = {
        "S96_S128": compare(common["S96"], common["S128"], common_r, common_z),
        "S128_S160": compare(common["S128"], common["S160"], common_r, common_z),
        "S160_S160H": compare(common["S160"], common["S160H"], common_r, common_z),
        "S128_RPLUS": compare(common["S128"], common["RPLUS"], common_r, common_z),
        "S128_ZPLUS": compare(common["S128"], common["ZPLUS"], common_r, common_z),
    }

    failures: list[str] = []
    for name, result in results.items():
        if not result["inherited_E1_pass"]:
            failures.append(f"{name}: inherited E1 gate FAIL")

    # Spatial convergence: every preregistered field and norm must improve on the fine pair.
    spatial_coarse = comparisons["S96_S128"]
    spatial_fine = comparisons["S128_S160"]
    for field in FIELD_NAMES:
        for norm in ("relative_linf", "relative_l2"):
            if not spatial_fine[field][norm] < spatial_coarse[field][norm]:
                failures.append(
                    f"spatial {field} {norm}: fine={spatial_fine[field][norm]:.12e} "
                    f">= coarse={spatial_coarse[field][norm]:.12e}"
                )

    scales = [results[n]["min_gradient_scale_points"] for n in ("S96", "S128", "S160")]
    if not (scales[0] < scales[1] < scales[2]):
        failures.append(f"spatial min-gradient-scale not increasing: {scales}")
    if not scales[2] >= 2.0:
        failures.append(f"S160 min-gradient-scale {scales[2]:.12e} < 2.0")

    tails = [results[n]["max_curvature_tail"] for n in ("S96", "S128", "S160")]
    if not (tails[0] > tails[1] > tails[2]):
        failures.append(f"spatial curvature-tail not decreasing: {tails}")
    if not tails[2] <= 1.0:
        failures.append(f"S160 curvature-tail {tails[2]:.12e} > 1.0")

    # Time refinement must actually halve the maximum accepted dt and be subdominant to fine space.
    if not results["S160H"]["max_dt"] <= 0.51 * results["S160"]["max_dt"]:
        failures.append(
            f"time ratio: S160H max_dt={results['S160H']['max_dt']:.12e} "
            f"> 0.51*S160={0.51 * results['S160']['max_dt']:.12e}"
        )
    time_diff = comparisons["S160_S160H"]
    for field in FIELD_NAMES:
        for norm in ("relative_linf", "relative_l2"):
            if not time_diff[field][norm] <= spatial_fine[field][norm]:
                failures.append(
                    f"time {field} {norm}: dt2={time_diff[field][norm]:.12e} "
                    f"> fine-space={spatial_fine[field][norm]:.12e}"
                )

    # One-coordinate domain enlargement at exactly the S128 spacing.
    for pair in ("S128_RPLUS", "S128_ZPLUS"):
        for field in FIELD_NAMES:
            for norm in ("relative_linf", "relative_l2"):
                value = comparisons[pair][field][norm]
                if not value <= 1.0e-3:
                    failures.append(f"domain {pair} {field} {norm}: {value:.12e} > 1e-3")

    # Save/reload exact-state provenance.
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

    # Compact extrema make the audit legible without post-processing the full comparison table.
    comparison_extrema: dict[str, dict[str, float]] = {}
    for pair, table in comparisons.items():
        comparison_extrema[pair] = {
            "max_relative_linf": max(v["relative_linf"] for v in table.values()),
            "max_relative_l2": max(v["relative_l2"] for v in table.values()),
        }

    summary = {
        "classification": "NUMERICAL CANDIDATE INFRASTRUCTURE / E2 SAME-DATUM LATTICE ONLY",
        "preregistration": "R3_EVOLUTION_E2_PREREG_2026-09-07.md",
        "precision": "float64",
        "stability_box": stability,
        "run_configs": {name: asdict(cfg) for name, cfg in RUN_CONFIGS.items()},
        "run_results": results,
        "common_grid": {
            "r": [0.0, 0.55, 65],
            "z": [-0.45, 0.45, 97],
            "interpolation": "scipy RegularGridInterpolator linear",
            "fields": list(FIELD_NAMES),
        },
        "comparisons": comparisons,
        "comparison_extrema": comparison_extrema,
        "npz_exact_reload_equal": reload_equal,
        "npz_sha256": npz_sha256,
        "failures": failures,
        "E2_pass": len(failures) == 0,
        "nonclaim": (
            "This is a short finite-box same-datum numerical convergence lattice. Passing does not "
            "establish a continuum convergence theorem or a rigorous free-space truncation bound."
        ),
    }
    summary_path = OUTDIR / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, allow_nan=False))

    print("E2 comparison extrema:")
    for pair, ext in comparison_extrema.items():
        print(
            f"  {pair}: max_rel_Linf={ext['max_relative_linf']:.6e} "
            f"max_rel_L2={ext['max_relative_l2']:.6e}"
        )
    print(f"npz_reload_equal={reload_equal} npz_sha256={npz_sha256}")
    print(f"E2_pass={summary['E2_pass']} failures={len(failures)} summary={summary_path}")
    for failure in failures:
        print(f"FAIL: {failure}")
    if failures:
        raise SystemExit("R3 E2 FAIL")


if __name__ == "__main__":
    main()
