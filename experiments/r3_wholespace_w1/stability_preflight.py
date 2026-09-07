#!/usr/bin/env python3
"""Frozen-coefficient W1 stability preflight.

This is a detector audit only. It contains no nonlinear time evolution and makes no
amplification, singularity, regularity, continuum-convergence, or Clay claim.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Dict

import numpy as np

TOL = 1e-10
NTHETA = 1025


def stability_polynomial(z: np.ndarray, method: str) -> np.ndarray:
    if method == "heun":
        return 1.0 + z + 0.5 * z**2
    if method == "ssprk3":
        return 1.0 + z + 0.5 * z**2 + z**3 / 6.0
    if method == "rk4":
        return 1.0 + z + 0.5 * z**2 + z**3 / 6.0 + z**4 / 24.0
    raise ValueError(method)


def symbol_grid(
    c_r: float,
    c_z: float,
    nu: float,
    dr: float,
    dz: float,
    include_l5_radial_stress: bool,
) -> np.ndarray:
    theta = np.linspace(-math.pi, math.pi, NTHETA)
    sr = np.sin(theta)[:, None]
    sz = np.sin(theta)[None, :]
    qr = 4.0 * np.sin(0.5 * theta) ** 2
    qz = qr.copy()

    real = -nu * (qr[:, None] / dr**2 + qz[None, :] / dz**2)
    c_r_eff = abs(c_r)
    if include_l5_radial_stress and nu > 0.0:
        r_min = dr
        c_r_eff += 3.0 * nu / r_min
    imag = -(c_r_eff * sr / dr + abs(c_z) * sz / dz)
    return real + 1j * imag


def max_amplification(
    method: str,
    c_r: float,
    c_z: float,
    nu: float,
    dr: float,
    dz: float,
    dt: float,
    include_l5_radial_stress: bool,
) -> float:
    lam = symbol_grid(c_r, c_z, nu, dr, dz, include_l5_radial_stress)
    return float(np.max(np.abs(stability_polynomial(dt * lam, method))))


def row(
    c_r: float,
    c_z: float,
    nu: float,
    dr: float,
    dz: float,
    dt: float,
    include_l5_radial_stress: bool,
) -> Dict[str, float]:
    return {
        method: max_amplification(method, c_r, c_z, nu, dr, dz, dt, include_l5_radial_stress)
        for method in ("heun", "ssprk3", "rk4")
    }


def run() -> Dict[str, object]:
    s1 = row(1.0, 0.0, 0.0, 0.05, 0.05, 0.02, False)
    s2 = row(0.5, 0.75, 0.01, 0.025, 0.025, 0.001, True)
    s3 = row(0.5, 0.75, 0.01, 0.025, 0.025, 0.03, True)

    checks = {
        "S1_heun_detects_instability": s1["heun"] >= 1.0 + 1e-4,
        "S1_rk4_stable": s1["rk4"] <= 1.0 + TOL,
        "S1_ssprk3_stable": s1["ssprk3"] <= 1.0 + TOL,
        "S2_rk4_stable": s2["rk4"] <= 1.0 + TOL,
        "S2_ssprk3_stable": s2["ssprk3"] <= 1.0 + TOL,
        "S3_rk4_rejects": s3["rk4"] >= 1.0 + 1e-2,
        "S3_ssprk3_rejects": s3["ssprk3"] >= 1.0 + 1e-2,
    }
    passed = bool(all(checks.values()))
    return {
        "schema": "r3-w1-stability-preflight-v1",
        "theta_grid": NTHETA,
        "tolerance": TOL,
        "rows": {
            "S1_pure_centered_advection": {
                "parameters": {"c_r": 1.0, "c_z": 0.0, "nu": 0.0, "dr": 0.05, "dz": 0.05, "dt": 0.02, "l5_radial_stress": False},
                "max_amplification": s1,
            },
            "S2_stable_advection_diffusion": {
                "parameters": {"c_r": 0.5, "c_z": 0.75, "nu": 0.01, "dr": 0.025, "dz": 0.025, "dt": 0.001, "l5_radial_stress": True},
                "max_amplification": s2,
            },
            "S3_oversized_step": {
                "parameters": {"c_r": 0.5, "c_z": 0.75, "nu": 0.01, "dr": 0.025, "dz": 0.025, "dt": 0.03, "l5_radial_stress": True},
                "max_amplification": s3,
            },
        },
        "checks": checks,
        "decision": "PASS" if passed else "STOP_REPAIR_W1_STABILITY_DETECTOR",
        "pass": passed,
        "claim_boundary": "detector audit only; no nonlinear evolution",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("experiments/r3_wholespace_w1/results/W1_STABILITY_PREFLIGHT.json"))
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"decision": result["decision"], "output": str(args.output)}, indent=2))
    return 0 if result["pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
