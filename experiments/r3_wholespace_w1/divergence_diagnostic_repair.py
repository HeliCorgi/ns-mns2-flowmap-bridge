#!/usr/bin/env python3
"""Manufactured repair gate for the W1 recovered-divergence diagnostic.

This script implements
`docs/gates/R3_AXISYM_WHOLESPACE_W1_DIVERGENCE_REPAIR_PREREG_2026-09-07.md`.
It does not alter the stopped W1 manufactured-v1 decision.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Dict, Tuple

import numpy as np

RMAX = 2.0
ZMAX = 2.0
CORE_R_MIN = 0.16
CORE_R_MAX = 0.80
CORE_Z = 0.80
GRIDS = (0.08, 0.04, 0.02)


def bump(s: np.ndarray) -> np.ndarray:
    a = np.asarray(s, dtype=float)
    out = np.zeros_like(a)
    mask = (a >= 0.0) & (a < 1.0)
    out[mask] = np.exp(-a[mask] / (1.0 - a[mask]))
    return out


def bump_prime(s: np.ndarray) -> np.ndarray:
    a = np.asarray(s, dtype=float)
    out = np.zeros_like(a)
    mask = (a >= 0.0) & (a < 1.0)
    bm = np.exp(-a[mask] / (1.0 - a[mask]))
    out[mask] = -bm / (1.0 - a[mask]) ** 2
    return out


def bump_second(s: np.ndarray) -> np.ndarray:
    a = np.asarray(s, dtype=float)
    out = np.zeros_like(a)
    mask = (a >= 0.0) & (a < 1.0)
    bm = np.exp(-a[mask] / (1.0 - a[mask]))
    out[mask] = bm * (2.0 * a[mask] - 1.0) / (1.0 - a[mask]) ** 4
    return out


def d_r(f: np.ndarray, h: float) -> np.ndarray:
    d = np.zeros_like(f)
    d[1:-1, :] = (f[2:, :] - f[:-2, :]) / (2.0 * h)
    d[0, :] = (-3.0 * f[0, :] + 4.0 * f[1, :] - f[2, :]) / (2.0 * h)
    d[-1, :] = (3.0 * f[-1, :] - 4.0 * f[-2, :] + f[-3, :]) / (2.0 * h)
    return d


def d_z(f: np.ndarray, h: float) -> np.ndarray:
    d = np.zeros_like(f)
    d[:, 1:-1] = (f[:, 2:] - f[:, :-2]) / (2.0 * h)
    d[:, 0] = (-3.0 * f[:, 0] + 4.0 * f[:, 1] - f[:, 2]) / (2.0 * h)
    d[:, -1] = (3.0 * f[:, -1] - 4.0 * f[:, -2] + f[:, -3]) / (2.0 * h)
    return d


def profile_arrays(name: str, rr: np.ndarray, zz: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    br = bump(rr**2)
    bz = bump(zz**2)
    bpz = bump_prime(zz**2)
    if name == "even":
        psi = br * bz
        gz = 2.0 * zz * bpz
    elif name == "odd":
        psi = br * zz * bz
        gz = bz + 2.0 * zz**2 * bpz
    else:
        raise ValueError(name)
    return psi, gz


def one_case(name: str, h: float) -> Dict[str, float]:
    nr = int(round(RMAX / h)) + 1
    nz = int(round(2.0 * ZMAX / h)) + 1
    r = np.linspace(0.0, RMAX, nr)
    z = np.linspace(-ZMAX, ZMAX, nz)
    if abs((r[1] - r[0]) - h) > 1e-13 or abs((z[1] - z[0]) - h) > 1e-13:
        raise RuntimeError("grid mismatch")
    rr = r[:, None]
    zz = z[None, :]
    psi, gz_exact = profile_arrays(name, rr, zz)

    pr = d_r(psi, h)
    q = d_z(psi, h)
    ur = -rr * q
    uz = 2.0 * psi + rr * pr

    dur = d_r(ur, h)
    duz = d_z(uz, h)
    ur_over_r = np.zeros_like(ur)
    ur_over_r[1:, :] = ur[1:, :] / rr[1:, :]
    div_ind = dur + ur_over_r + duz

    div_pred = np.zeros_like(div_ind)
    div_pred[1:-1, :] = q[1:-1, :] - 0.5 * (q[2:, :] + q[:-2, :])

    dzdr = d_z(pr, h)
    drdz = d_r(q, h)
    div_compat = rr * (dzdr - drdz)

    mask = (
        (rr >= CORE_R_MIN - 1e-14)
        & (rr <= CORE_R_MAX + 1e-14)
        & (np.abs(zz) <= CORE_Z + 1e-14)
    )

    def infnorm(a: np.ndarray) -> float:
        return float(np.max(np.abs(a[mask])))

    div_ind_inf = infnorm(div_ind)
    div_pred_inf = infnorm(div_pred)
    identity_rel = infnorm(div_ind - div_pred) / max(div_ind_inf, div_pred_inf, 1e-30)

    term_norm = infnorm(dur) + infnorm(ur_over_r) + infnorm(duz)
    rel_div = div_ind_inf / max(term_norm, 1e-30)

    frr = 2.0 * bump_prime(rr**2) + 4.0 * rr**2 * bump_second(rr**2)
    leading = -0.5 * frr * gz_exact
    scaled = div_ind / (h * h)
    lead_num = float(np.linalg.norm((scaled - leading)[mask]))
    lead_den = float(np.linalg.norm(leading[mask]))
    lead_err = lead_num / max(lead_den, 1e-30)

    compat_den = infnorm(rr * dzdr) + infnorm(rr * drdz)
    compat_rel = infnorm(div_compat) / max(compat_den, 1e-30)

    return {
        "identity_relative_error": identity_rel,
        "relative_independent_divergence": rel_div,
        "leading_term_relative_l2_error": lead_err,
        "compatible_commutator_relative_error": compat_rel,
        "independent_divergence_inf": div_ind_inf,
        "predicted_defect_inf": div_pred_inf,
    }


def run_gate() -> Dict[str, object]:
    cases: Dict[str, Dict[str, Dict[str, float]]] = {}
    for name in ("even", "odd"):
        cases[name] = {}
        for h in GRIDS:
            cases[name][f"h_{h:.2f}"] = one_case(name, h)

    checks: Dict[str, bool] = {}
    for name in ("even", "odd"):
        for h in GRIDS:
            row = cases[name][f"h_{h:.2f}"]
            checks[f"D1_{name}_h{h:.2f}"] = row["identity_relative_error"] <= 1e-10
            checks[f"D4_{name}_h{h:.2f}"] = row["compatible_commutator_relative_error"] <= 1e-12

        r08 = cases[name]["h_0.08"]["relative_independent_divergence"]
        r04 = cases[name]["h_0.04"]["relative_independent_divergence"]
        r02 = cases[name]["h_0.02"]["relative_independent_divergence"]
        checks[f"D2_{name}_strict_08_04"] = r04 < r08
        checks[f"D2_{name}_strict_04_02"] = r02 < r04
        checks[f"D2_{name}_ratio_08_04"] = r04 <= 0.35 * r08
        checks[f"D2_{name}_ratio_04_02"] = r02 <= 0.35 * r04

        e08 = cases[name]["h_0.08"]["leading_term_relative_l2_error"]
        e04 = cases[name]["h_0.04"]["leading_term_relative_l2_error"]
        e02 = cases[name]["h_0.02"]["leading_term_relative_l2_error"]
        checks[f"D3_{name}_strict_08_04"] = e04 < e08
        checks[f"D3_{name}_strict_04_02"] = e02 < e04
        checks[f"D3_{name}_ratio_08_04"] = e04 <= 0.40 * e08
        checks[f"D3_{name}_ratio_04_02"] = e02 <= 0.40 * e04

    passed = bool(all(checks.values()))
    return {
        "schema": "r3-w1-divergence-diagnostic-repair-v1",
        "frozen_parameters": {
            "Rmax": RMAX,
            "Zmax": ZMAX,
            "h": list(GRIDS),
            "core_r": [CORE_R_MIN, CORE_R_MAX],
            "core_abs_z_max": CORE_Z,
            "profiles": ["even", "odd"],
        },
        "cases": cases,
        "checks": checks,
        "decision": "PASS" if passed else "STOP_REPAIR_DIAGNOSTIC",
        "pass": passed,
        "claim_boundary": "recovered-divergence diagnostic repair only; manufactured-v1 remains stopped",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/r3_wholespace_w1/results/W1_DIVERGENCE_REPAIR.json"),
    )
    args = parser.parse_args()
    result = run_gate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"decision": result["decision"], "output": str(args.output)}, indent=2))
    return 0 if result["pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
