#!/usr/bin/env python3
"""Early-time dynamic-domain / elliptic-boundary audit for the R3 W1 track.

Implements the frozen gate in
`docs/gates/R3_AXISYM_WHOLESPACE_W1_DYNAMIC_DOMAIN_PREREG_2026-09-07.md`.
No long-time amplification, continuum-convergence, singularity, regularity, or Clay claim.
"""

from __future__ import annotations

import argparse
import gc
import json
import math
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.interpolate import RectBivariateSpline
from scipy import sparse
from scipy.sparse import linalg as spla

import manufactured_short_time as v1

PI = math.pi
H = 0.04
RECEIVERS: Tuple[Tuple[float, float], ...] = (
    (0.12, 0.00),
    (0.24, 0.20),
    (0.28, -0.24),
    (0.20, 0.32),
)
BOXES: Tuple[Tuple[str, float, float], ...] = (
    ("B22", 2.0, 2.0),
    ("B32", 3.0, 2.0),
    ("B42", 4.0, 2.0),
    ("B23", 2.0, 3.0),
    ("B24", 2.0, 4.0),
    ("B44", 4.0, 4.0),
)
CORE_R = 0.80
CORE_Z = 0.80


class DomainGridSolver(v1.GridSolver):
    """The v1 spatial/time implementation with configurable nonperiodic box extents."""

    def __init__(self, h: float, rmax: float, zmax: float):
        self.h = float(h)
        self.rmax = float(rmax)
        self.zmax = float(zmax)
        self.nr = int(round(self.rmax / self.h)) + 1
        self.nz = int(round(2.0 * self.zmax / self.h)) + 1
        self.r = np.linspace(0.0, self.rmax, self.nr)
        self.z = np.linspace(-self.zmax, self.zmax, self.nz)
        if abs(self.r[1] - self.r[0] - self.h) > 1e-13 or abs(self.z[1] - self.z[0] - self.h) > 1e-13:
            raise ValueError("frozen grid spacing mismatch")
        self.rr = self.r[:, None]
        self.zz = self.z[None, :]
        self.ni = self.nr - 1
        self.nj = self.nz - 2
        self.op = v1.assemble_minus_l5(self.r, self.z, self.h).tocsc()
        self.solve_factor = spla.factorized(self.op)
        self.scanner = v1.RuntimeStabilityScanner(self.h)
        self.core = (self.rr <= CORE_R + 1e-14) & (np.abs(self.zz) <= CORE_Z + 1e-14)


def dynamic_run(rmax: float, zmax: float) -> Dict[str, object]:
    s = DomainGridSolver(H, rmax, zmax)
    run = v1.run_integrator(s, "rk4")
    summary = v1.streamed_summary(run)
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
    ua = core_view(a, "u"); wa = core_view(a, "w")
    ub = core_view(b, "u"); wb = core_view(b, "w")
    if ua.shape != ub.shape or wa.shape != wb.shape:
        raise RuntimeError("common-core grids are not aligned")
    du = ua - ub; dw = wa - wb
    num = math.sqrt(float(np.sum(du * du) + np.sum(dw * dw)))
    den = math.sqrt(float(np.sum(ub * ub) + np.sum(wb * wb)))
    return num / max(den, 1e-30)


def trap_weights(n: int) -> np.ndarray:
    w = np.ones(n, dtype=float)
    w[0] = 0.5; w[-1] = 0.5
    return w


def lifted_source_audit(r: np.ndarray, z: np.ndarray, omega: np.ndarray) -> Dict[str, float]:
    wr = trap_weights(len(r))[:, None]
    wz = trap_weights(len(z))[None, :]
    weight = wr * wz * (r[:, None] ** 3) * H * H
    total = float(np.sum(weight * np.abs(omega)))
    inside = (r[:, None] <= 2.0 + 1e-14) & (np.abs(z[None, :]) <= 2.0 + 1e-14)
    outside = float(np.sum(weight * np.abs(omega) * (~inside)))
    monopole = float(np.sum(weight * omega))
    return {
        "lifted_L1": total,
        "outside_B22_fraction": outside / max(total, 1e-30),
        "normalized_odd_monopole": abs(monopole) / max(total, 1e-30),
    }


def restrict_full_source(full_r: np.ndarray, full_z: np.ndarray, full_w: np.ndarray,
                         small_r: np.ndarray, small_z: np.ndarray) -> np.ndarray:
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


def receiver_vector(s: DomainGridSolver, psi: np.ndarray) -> np.ndarray:
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


def green_from_grid_source(
    r: np.ndarray,
    z: np.ndarray,
    omega: np.ndarray,
    source_spacing: float,
    ntheta: int,
) -> np.ndarray:
    """Independent reduced 5-D Green evaluation using spline + midpoint source quadrature."""
    if source_spacing <= 0.0:
        raise ValueError("source spacing must be positive")
    rmax = float(r[-1]); zmin = float(z[0]); zmax = float(z[-1])
    nrq = int(round(rmax / source_spacing))
    nzq = int(round((zmax - zmin) / source_spacing))
    if abs(nrq * source_spacing - rmax) > 2e-12 or abs(nzq * source_spacing - (zmax - zmin)) > 2e-12:
        raise ValueError("quadrature spacing does not align with source box")
    rho = (np.arange(nrq, dtype=float) + 0.5) * source_spacing
    zeta = zmin + (np.arange(nzq, dtype=float) + 0.5) * source_spacing

    spline = RectBivariateSpline(r, z, omega, kx=3, ky=3, s=0.0)
    om = np.asarray(spline(rho, zeta, grid=True), dtype=float)

    xt, wt = leggauss(ntheta)
    theta = 0.5 * PI * (xt + 1.0)
    wtheta = 0.5 * PI * wt
    ct = np.cos(theta)
    st2w = (np.sin(theta) ** 2) * wtheta

    coeff = 1.0 / (2.0 * PI)
    ans = np.zeros((len(RECEIVERS), 3), dtype=float)
    # Chunk in rho to cap memory. Midpoint source quadrature has weight dr dz rho^3.
    chunk = 12
    for pidx, (rp, zp) in enumerate(RECEIVERS):
        acc0 = 0.0; accr = 0.0; accz = 0.0
        for a in range(0, len(rho), chunk):
            rb = rho[a:a + chunk, None, None]
            zb = zeta[None, :, None]
            c = ct[None, None, :]
            base = (
                (rb[:, :, 0] ** 3)
                * om[a:a + chunk, :]
                * (source_spacing ** 2)
            )[:, :, None]
            d = rp * rp + rb * rb - 2.0 * rp * rb * c + (zp - zb) ** 2
            if np.any(d <= 0.0):
                raise RuntimeError("unexpected Green quadrature singular sample")
            wa = st2w[None, None, :]
            k0 = d ** (-1.5)
            kr = -3.0 * (rp - rb * c) * d ** (-2.5)
            kz = -3.0 * (zp - zb) * d ** (-2.5)
            acc0 += float(np.sum(base * wa * k0))
            accr += float(np.sum(base * wa * kr))
            accz += float(np.sum(base * wa * kz))
        ans[pidx, :] = coeff * np.array([acc0, accr, accz])
    return ans


def rel_vec(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.linalg.norm((a - b).ravel()) / max(np.linalg.norm(b.ravel()), 1e-30))


def run_gate() -> Dict[str, object]:
    dynamic: Dict[str, Dict[str, object]] = {}
    for name, rmax, zmax in BOXES:
        dynamic[name] = dynamic_run(rmax, zmax)

    # A0 inherited runtime checks.
    checks: Dict[str, bool] = {}
    dyn_summary: Dict[str, Dict[str, object]] = {}
    for name, _rmax, _zmax in BOXES:
        ss = dict(dynamic[name]["summary"])
        ss["accepted_steps"] = int(dynamic[name]["accepted_steps"])
        dyn_summary[name] = ss
        checks[f"A0_{name}_eight_steps"] = int(dynamic[name]["accepted_steps"]) == 8
        checks[f"A0_{name}_completed"] = bool(ss["completed"])
        checks[f"A0_{name}_no_reject"] = int(ss["rejected_steps"]) == 0
        checks[f"A0_{name}_finite"] = bool(ss["all_stage_finite"] and ss["all_step_finite"])
        checks[f"A0_{name}_amp"] = float(ss["max_frozen_symbol_amplification"]) <= 1.0 + v1.STABILITY_TOL
        checks[f"A0_{name}_cfl"] = float(ss["max_cfl"]) <= 0.10
        checks[f"A0_{name}_visc"] = float(ss["max_viscous_number"]) <= 0.05
        checks[f"A0_{name}_poisson"] = max(float(ss["max_stage_poisson_residual"]), float(ss["max_step_poisson_residual"])) <= 1e-10
        checks[f"A0_{name}_odd"] = float(ss["max_odd_z_defect"]) <= 1e-12
        checks[f"A0_{name}_energy"] = float(ss["max_energy_ratio_to_initial"]) <= 1.0 + 1e-5
        checks[f"A0_{name}_energy_balance"] = float(ss["max_energy_balance_defect"]) <= 0.20

    # A1 dynamic common-core increments.
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

    # A2 common B44 source containment and odd monopole.
    full = dynamic["B44"]
    full_r = np.asarray(full["r"], dtype=float)
    full_z = np.asarray(full["z"], dtype=float)
    full_w = np.asarray(full["w"], dtype=float)
    source_audit = lifted_source_audit(full_r, full_z, full_w)
    checks["A2_source_containment"] = source_audit["outside_B22_fraction"] <= 1e-12
    checks["A2_odd_monopole"] = source_audit["normalized_odd_monopole"] <= 1e-12

    # A3 independent free-space Green self-check.
    qlow = green_from_grid_source(full_r, full_z, full_w, source_spacing=0.04, ntheta=48)
    qhigh = green_from_grid_source(full_r, full_z, full_w, source_spacing=0.02, ntheta=80)
    green_self = rel_vec(qlow, qhigh)
    checks["A3_green_self"] = green_self <= 2e-3

    # A4 same-source elliptic boundary sensitivity.
    receiver_rows: Dict[str, List[List[float]]] = {}
    ebox: Dict[str, float] = {}
    for name, rmax, zmax in BOXES:
        s = DomainGridSolver(H, rmax, zmax)
        src = restrict_full_source(full_r, full_z, full_w, s.r, s.z)
        psi, pres = s.solve_psi(src)
        if pres > 1e-10:
            checks[f"A4_{name}_poisson"] = False
        else:
            checks[f"A4_{name}_poisson"] = True
        rv = receiver_vector(s, psi)
        receiver_rows[name] = rv.tolist()
        ebox[name] = rel_vec(rv, qhigh)
        del s, psi, src
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

    if not checks["A3_green_self"]:
        decision = "STOP_REPAIR_GREEN_QUADRATURE"
        passed = False
    else:
        passed = bool(all(checks.values()))
        decision = "PASS" if passed else "STOP_REPAIR_DYNAMIC_DOMAIN"

    # Remove large arrays from the machine report.
    return {
        "schema": "r3-w1-dynamic-domain-audit-v1",
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
            "green_low": {"source_midpoint_spacing": 0.04, "theta_order": 48},
            "green_high": {"source_midpoint_spacing": 0.02, "theta_order": 80},
        },
        "A0_dynamic_summaries": dyn_summary,
        "A1_dynamic_state_sensitivity": dynamic_sensitivity,
        "A2_common_source_audit": source_audit,
        "A3_green_self_relative_difference": green_self,
        "A3_green_low_receivers": qlow.tolist(),
        "A3_green_high_receivers": qhigh.tolist(),
        "A4_receiver_rows": receiver_rows,
        "A4_receiver_relative_error_to_green": ebox,
        "A4_adjacent_receiver_changes": receiver_changes,
        "checks": checks,
        "decision": decision,
        "pass": passed,
        "claim_boundary": "early-time finite-box dynamic-domain / elliptic-boundary numerical audit only",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/r3_wholespace_w1/results/W1_DYNAMIC_DOMAIN_AUDIT.json"),
    )
    args = parser.parse_args()
    result = run_gate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"decision": result["decision"], "output": str(args.output)}, indent=2))
    return 0 if result["pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
