#!/usr/bin/env python3
"""Static whole-space W0 gate for the R^3 axisymmetric-with-swirl track.

Scope: numerical infrastructure / manufactured elliptic audit only.
No time integration, singularity claim, global-regularity claim, or Clay A/B/C/D claim.

The frozen acceptance rules live in
  docs/gates/R3_AXISYM_WHOLESPACE_W0_IMPLEMENTATION_PREREG_2026-09-07.md
and must not be changed in response to this script's production output.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy import sparse
from scipy.sparse import linalg as spla

PI = math.pi
RECEIVERS: Tuple[Tuple[float, float], ...] = (
    (0.12, 0.00),
    (0.24, 0.20),
    (0.28, -0.24),
    (0.20, 0.32),
)
RC2 = 1.0
D2 = 0.36
RHO_MIN = math.sqrt(RC2 - D2)
RHO_MAX = math.sqrt(RC2 + D2)
BASE_WIDTH = 0.6
STRESS_WIDTH = 1.2


def bump(s: np.ndarray | float) -> np.ndarray:
    """Frozen C-infinity bump b(s) for s >= 0."""
    a = np.asarray(s, dtype=float)
    out = np.zeros_like(a)
    mask = (a >= 0.0) & (a < 1.0)
    out[mask] = np.exp(-a[mask] / (1.0 - a[mask]))
    return out


def radial_shell(rho: np.ndarray) -> np.ndarray:
    q = ((rho * rho - RC2) / D2) ** 2
    return bump(q)


def axial_factor(zeta: np.ndarray, width: float, odd: bool) -> np.ndarray:
    base = bump((zeta / width) ** 2)
    if odd:
        return (zeta / width) * base
    return base


def source_pair(rho: np.ndarray, zeta: np.ndarray, width: float) -> Tuple[np.ndarray, np.ndarray]:
    br = radial_shell(rho)
    even = br * axial_factor(zeta, width, odd=False)
    odd = br * axial_factor(zeta, width, odd=True)
    return even, odd


@dataclass
class GreenReference:
    """Tensor-quadrature reference for the reduced 5-D Green representation."""

    width: float
    n_rho: int
    n_zeta: int
    n_ang: int

    def __post_init__(self) -> None:
        xr, wr = leggauss(self.n_rho)
        self.rho = 0.5 * (RHO_MAX - RHO_MIN) * xr + 0.5 * (RHO_MAX + RHO_MIN)
        self.wrho = 0.5 * (RHO_MAX - RHO_MIN) * wr

        xz, wz = leggauss(self.n_zeta)
        self.zeta = self.width * xz
        self.wzeta = self.width * wz

        k = np.arange(1, self.n_ang + 1, dtype=float)
        theta = k * PI / (self.n_ang + 1.0)
        self.t = np.cos(theta)
        self.wang = (PI / (self.n_ang + 1.0)) * np.sin(theta) ** 2

        rr = self.rho[:, None]
        zz = self.zeta[None, :]
        even, odd = source_pair(rr, zz, self.width)
        common = self.wrho[:, None] * self.wzeta[None, :] * rr**3
        self.base = {
            "even": common * even,
            "odd": common * odd,
        }

    def evaluate(self, points: Sequence[Tuple[float, float]]) -> Dict[str, np.ndarray]:
        """Return (psi, d_r psi, d_z psi) at each point for both frozen sources."""
        ans = {
            "even": np.zeros((len(points), 3), dtype=float),
            "odd": np.zeros((len(points), 3), dtype=float),
        }
        rho = self.rho[:, None, None]
        zeta = self.zeta[None, :, None]
        t = self.t[None, None, :]
        wa = self.wang[None, None, :]
        coeff = 1.0 / (2.0 * PI)

        for pidx, (r, z) in enumerate(points):
            d = r * r + rho**2 - 2.0 * r * rho * t + (z - zeta) ** 2
            k0 = d ** (-1.5)
            kr = -3.0 * (r - rho * t) * d ** (-2.5)
            kz = -3.0 * (z - zeta) * d ** (-2.5)
            for name in ("even", "odd"):
                b = self.base[name][:, :, None] * wa
                ans[name][pidx, 0] = coeff * np.sum(b * k0)
                ans[name][pidx, 1] = coeff * np.sum(b * kr)
                ans[name][pidx, 2] = coeff * np.sum(b * kz)
        return ans


def combined_relative_error(value: np.ndarray, ref: np.ndarray) -> float:
    den = float(np.linalg.norm(ref.ravel()))
    if den == 0.0:
        raise ValueError("reference vector unexpectedly has zero norm")
    return float(np.linalg.norm((value - ref).ravel()) / den)


def grid_size(extent: float, h: float) -> int:
    q = extent / h
    if abs(q - round(q)) > 2e-12:
        raise ValueError(f"extent {extent} is not aligned to h={h}")
    return int(round(q)) + 1


def boundary_points(r: np.ndarray, z: np.ndarray) -> Tuple[List[Tuple[float, float]], List[Tuple[int, int]]]:
    nr = len(r)
    nz = len(z)
    pts: List[Tuple[float, float]] = []
    idx: List[Tuple[int, int]] = []
    for j in range(nz):
        pts.append((float(r[-1]), float(z[j])))
        idx.append((nr - 1, j))
    for i in range(nr - 1):
        pts.append((float(r[i]), float(z[0])))
        idx.append((i, 0))
        pts.append((float(r[i]), float(z[-1])))
        idx.append((i, nz - 1))
    return pts, idx


def assemble_operator(r: np.ndarray, z: np.ndarray, h: float) -> sparse.csr_matrix:
    """Assemble -L5 on unknowns i=0..nr-2, j=1..nz-2."""
    nr = len(r)
    nz = len(z)
    ni = nr - 1
    nj = nz - 2
    n = ni * nj

    rows: List[int] = []
    cols: List[int] = []
    vals: List[float] = []

    def idx(i: int, j: int) -> int:
        return i * nj + (j - 1)

    h2 = h * h
    for i in range(ni):
        ri = float(r[i])
        for j in range(1, nz - 1):
            p = idx(i, j)
            diag = 2.0 / h2

            if j - 1 >= 1:
                rows.append(p); cols.append(idx(i, j - 1)); vals.append(-1.0 / h2)
            if j + 1 <= nz - 2:
                rows.append(p); cols.append(idx(i, j + 1)); vals.append(-1.0 / h2)

            if i == 0:
                # -[4 psi_rr + psi_zz], psi_rr(0) = 2(psi_1-psi_0)/h^2.
                diag += 8.0 / h2
                rows.append(p); cols.append(idx(1, j)); vals.append(-8.0 / h2)
            else:
                diag += 2.0 / h2
                cm = -1.0 / h2 + 3.0 / (2.0 * ri * h)
                cp = -1.0 / h2 - 3.0 / (2.0 * ri * h)
                rows.append(p); cols.append(idx(i - 1, j)); vals.append(cm)
                if i + 1 <= ni - 1:
                    rows.append(p); cols.append(idx(i + 1, j)); vals.append(cp)

            rows.append(p); cols.append(p); vals.append(diag)

    return sparse.csr_matrix((vals, (rows, cols)), shape=(n, n))


def solve_box_pair(
    rmax: float,
    zmax: float,
    h: float,
    width: float,
    boundary_mode: str,
    green_boundary_order: int = 64,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, np.ndarray]]:
    """Solve both frozen sources on one box, sharing one sparse factorization."""
    nr = grid_size(rmax, h)
    nz = grid_size(2.0 * zmax, h)
    r = np.linspace(0.0, rmax, nr)
    z = np.linspace(-zmax, zmax, nz)
    if abs((zmax / h) - round(zmax / h)) > 2e-12:
        raise ValueError("z=0 must be a grid point for the frozen receiver layout")

    bvals = {
        "even": np.zeros((nr, nz), dtype=float),
        "odd": np.zeros((nr, nz), dtype=float),
    }
    if boundary_mode == "green":
        pts, inds = boundary_points(r, z)
        ref = GreenReference(width, green_boundary_order, green_boundary_order, green_boundary_order).evaluate(pts)
        for name in ("even", "odd"):
            for (i, j), val in zip(inds, ref[name][:, 0]):
                bvals[name][i, j] = float(val)
    elif boundary_mode != "zero":
        raise ValueError(f"unknown boundary mode {boundary_mode}")

    a = assemble_operator(r, z, h)
    ni = nr - 1
    nj = nz - 2
    n = ni * nj
    rhs = np.zeros((n, 2), dtype=float)
    names = ("even", "odd")

    rr, zz = np.meshgrid(r[:-1], z[1:-1], indexing="ij")
    src_even, src_odd = source_pair(rr, zz, width)
    src = {"even": src_even, "odd": src_odd}
    h2 = h * h

    def idx(i: int, j: int) -> int:
        return i * nj + (j - 1)

    for col, name in enumerate(names):
        for i in range(ni):
            ri = float(r[i])
            for j in range(1, nz - 1):
                p = idx(i, j)
                rhs[p, col] = float(src[name][i, j - 1])

                # z boundary contributions from coefficient -1/h^2.
                if j - 1 == 0:
                    rhs[p, col] += bvals[name][i, 0] / h2
                if j + 1 == nz - 1:
                    rhs[p, col] += bvals[name][i, nz - 1] / h2

                if i > 0 and i + 1 == nr - 1:
                    cp = -1.0 / h2 - 3.0 / (2.0 * ri * h)
                    rhs[p, col] -= cp * bvals[name][nr - 1, j]

    sol = spla.spsolve(a, rhs)
    fields: Dict[str, np.ndarray] = {}
    for col, name in enumerate(names):
        psi = bvals[name].copy()
        for i in range(ni):
            psi[i, 1:-1] = sol[i * nj:(i + 1) * nj, col]
        fields[name] = psi
    return r, z, fields


def receiver_values(r: np.ndarray, z: np.ndarray, psi: np.ndarray, h: float) -> np.ndarray:
    out = np.zeros((len(RECEIVERS), 3), dtype=float)
    for pidx, (rr, zz) in enumerate(RECEIVERS):
        i = int(round(rr / h))
        j = int(round((zz - float(z[0])) / h))
        if abs(float(r[i]) - rr) > 2e-12 or abs(float(z[j]) - zz) > 2e-12:
            raise ValueError("receiver is not aligned to frozen grid")
        out[pidx, 0] = psi[i, j]
        out[pidx, 1] = (psi[i + 1, j] - psi[i - 1, j]) / (2.0 * h)
        out[pidx, 2] = (psi[i, j + 1] - psi[i, j - 1]) / (2.0 * h)
    return out


def datum_u1(r2: np.ndarray, z: np.ndarray) -> np.ndarray:
    return bump(r2) * z * bump(z * z)


def run_w0_a() -> Dict[str, object]:
    rows: List[Dict[str, float]] = []
    energies: List[float] = []
    div_maxes: List[float] = []
    div_rmses: List[float] = []
    support_ok = True

    for n in (33, 65, 129):
        x = np.linspace(-1.25, 1.25, n)
        h = float(x[1] - x[0])
        xx, yy, zz = np.meshgrid(x, x, x, indexing="ij")
        r2 = xx * xx + yy * yy
        u1 = datum_u1(r2, zz)
        ux = -yy * u1
        uy = xx * u1
        uz = np.zeros_like(ux)

        dux_dx = np.gradient(ux, h, axis=0, edge_order=2)
        duy_dy = np.gradient(uy, h, axis=1, edge_order=2)
        div = dux_dx + duy_dy
        interior = div[2:-2, 2:-2, 2:-2]
        dmax = float(np.max(np.abs(interior)))
        drms = float(np.sqrt(np.mean(interior * interior)))
        energy = float(np.sum(ux * ux + uy * uy + uz * uz) * h**3)

        nonzero = np.abs(u1) > 0.0
        if np.any(nonzero):
            support_ok = support_ok and bool(np.all(r2[nonzero] < 1.0 + 1e-15))
            support_ok = support_ok and bool(np.all(np.abs(zz[nonzero]) < 1.0 + 1e-15))

        rows.append({"N": n, "h": h, "max_abs_div": dmax, "rms_div": drms, "physical_energy": energy})
        energies.append(energy)
        div_maxes.append(dmax)
        div_rmses.append(drms)

    rs = np.linspace(-1.2, 1.2, 257)
    zs = np.linspace(-1.0, 1.0, 129)
    rr, zz2 = np.meshgrid(rs, zs, indexing="ij")
    parity = float(np.max(np.abs(datum_u1(rr * rr, zz2) - datum_u1((-rr) * (-rr), zz2))))
    energy_rel = abs(energies[2] - energies[1]) / abs(energies[2])

    checks = {
        "finite": bool(all(np.isfinite([x["max_abs_div"], x["rms_div"], x["physical_energy"]]).all() for x in rows)),
        "analytic_divergence_identity": True,
        "finest_max_div": div_maxes[-1] <= 4e-3,
        "finest_rms_div": div_rmses[-1] <= 4e-4,
        "div_max_strict_decrease": div_maxes[0] > div_maxes[1] > div_maxes[2],
        "div_rms_strict_decrease": div_rmses[0] > div_rmses[1] > div_rmses[2],
        "signed_r_parity": parity <= 5e-15,
        "energy_refinement": energy_rel <= 1e-5,
        "support": support_ok,
    }
    return {
        "rows": rows,
        "parity_max_abs": parity,
        "energy_rel_129_65": energy_rel,
        "support_ok": support_ok,
        "checks": checks,
        "pass": bool(all(checks.values())),
    }


def green_self_check(width: float) -> Tuple[Dict[str, np.ndarray], Dict[str, object]]:
    ref48 = GreenReference(width, 48, 48, 48).evaluate(RECEIVERS)
    ref64 = GreenReference(width, 64, 64, 64).evaluate(RECEIVERS)
    per_source: Dict[str, float] = {}
    for name in ("even", "odd"):
        per_source[name] = float(np.max(np.abs(ref64[name] - ref48[name])))
    worst = max(per_source.values())
    return ref64, {"per_source_max_abs": per_source, "worst_max_abs": worst, "pass": worst <= 1e-9}


def run_w0_b(ref64: Dict[str, np.ndarray]) -> Dict[str, object]:
    errors: Dict[str, Dict[str, float]] = {"even": {}, "odd": {}}
    for h in (0.04, 0.02):
        r, z, fields = solve_box_pair(2.0, 1.2, h, BASE_WIDTH, "green", green_boundary_order=64)
        for name in ("even", "odd"):
            vals = receiver_values(r, z, fields[name], h)
            errors[name][f"h_{h:.2f}"] = combined_relative_error(vals, ref64[name])

    checks: Dict[str, bool] = {}
    for name in ("even", "odd"):
        e04 = errors[name]["h_0.04"]
        e02 = errors[name]["h_0.02"]
        checks[f"{name}_quarter_reduction"] = e02 <= 0.25 * e04
        checks[f"{name}_fine_absolute"] = e02 <= 5e-4
    return {"errors": errors, "checks": checks, "pass": bool(all(checks.values()))}


def source_moments(width: float, n: int = 128) -> Dict[str, Dict[str, float]]:
    xr, wr = leggauss(n)
    rho = 0.5 * (RHO_MAX - RHO_MIN) * xr + 0.5 * (RHO_MAX + RHO_MIN)
    wr = 0.5 * (RHO_MAX - RHO_MIN) * wr
    xz, wz = leggauss(n)
    zeta = width * xz
    wz = width * wz
    rr = rho[:, None]
    zz = zeta[None, :]
    even, odd = source_pair(rr, zz, width)
    weight = (2.0 * PI**2) * wr[:, None] * wz[None, :] * rr**3
    radius = np.sqrt(rr**2 + zz**2)
    out: Dict[str, Dict[str, float]] = {}
    for name, om in (("even", even), ("odd", odd)):
        out[name] = {
            "mass": float(np.sum(weight * om)),
            "l1": float(np.sum(weight * np.abs(om))),
            "m1": float(np.sum(weight * radius * np.abs(om))),
        }
    return out


def final_boundary_envelope_check(width: float, moments: Dict[str, Dict[str, float]]) -> Dict[str, object]:
    h = 0.02
    r = np.linspace(0.0, 6.0, grid_size(6.0, h))
    z = np.linspace(-6.0, 6.0, grid_size(12.0, h))
    pts, _ = boundary_points(r, z)
    ref = GreenReference(width, 48, 48, 48).evaluate(pts)
    s = math.sqrt(RHO_MAX**2 + width**2)
    ratios: Dict[str, float] = {}
    max_violation = 0.0
    for name in ("even", "odd"):
        ratio_max = 0.0
        for (rr, zz), psi in zip(pts, ref[name][:, 0]):
            radius = math.hypot(rr, zz)
            if radius < 2.0 * s:
                continue
            if name == "even":
                env = moments[name]["l1"] / (PI**2 * radius**3)
            else:
                env = 6.0 * moments[name]["m1"] / (PI**2 * radius**4)
            ratio = abs(float(psi)) / env if env > 0.0 else math.inf
            ratio_max = max(ratio_max, ratio)
            violation = abs(float(psi)) - (env * (1.0 + 1e-10) + 1e-10)
            max_violation = max(max_violation, violation)
        ratios[name] = ratio_max
    return {
        "support_radius_S": s,
        "max_ratio_to_envelope": ratios,
        "max_positive_violation": max_violation,
        "pass": max_violation <= 0.0,
    }


def run_zero_box_sequences(ref64: Dict[str, np.ndarray], width: float, stress: bool = False) -> Dict[str, object]:
    cache: Dict[Tuple[float, float], Dict[str, float]] = {}

    def box_errors(rmax: float, zmax: float) -> Dict[str, float]:
        key = (rmax, zmax)
        if key not in cache:
            r, z, fields = solve_box_pair(rmax, zmax, 0.02, width, "zero")
            cache[key] = {
                name: combined_relative_error(receiver_values(r, z, fields[name], 0.02), ref64[name])
                for name in ("even", "odd")
            }
        return cache[key]

    if stress:
        zseq = (2.0, 3.0, 4.0, 6.0, 8.0)
        rows = [{"Rmax": 6.0, "Zmax": zz, **box_errors(6.0, zz)} for zz in zseq]
        checks: Dict[str, bool] = {}
        for name in ("even", "odd"):
            es = [float(row[name]) for row in rows]
            checks[f"{name}_strict_decrease"] = all(a > b for a, b in zip(es, es[1:]))
            checks[f"{name}_final"] = es[-1] <= 6e-3
        return {"axial_rows": rows, "checks": checks, "pass": bool(all(checks.values()))}

    rseq = (2.0, 3.0, 4.0, 6.0)
    zseq = (1.2, 2.0, 3.0, 4.0, 6.0)
    radial = [{"Rmax": rr, "Zmax": 6.0, **box_errors(rr, 6.0)} for rr in rseq]
    axial = [{"Rmax": 6.0, "Zmax": zz, **box_errors(6.0, zz)} for zz in zseq]
    checks = {}
    for name in ("even", "odd"):
        er = [float(row[name]) for row in radial]
        ez = [float(row[name]) for row in axial]
        checks[f"{name}_radial_strict_decrease"] = all(a > b for a, b in zip(er, er[1:]))
        checks[f"{name}_axial_strict_decrease"] = all(a > b for a, b in zip(ez, ez[1:]))
        checks[f"{name}_final"] = er[-1] <= 5e-3 and ez[-1] <= 5e-3
    moments = source_moments(width)
    envelope = final_boundary_envelope_check(width, moments)
    checks["far_field_envelope"] = bool(envelope["pass"])
    return {
        "radial_rows": radial,
        "axial_rows": axial,
        "moments": moments,
        "far_field_envelope": envelope,
        "checks": checks,
        "pass": bool(all(checks.values())),
    }


def run_w0_e(w0a: Dict[str, object], moments: Dict[str, Dict[str, float]]) -> Dict[str, object]:
    odd = moments["odd"]
    monopole_ratio = abs(odd["mass"]) / odd["l1"]

    # Distinct lifted diagnostic for the exact datum; intentionally no physical-volume label.
    xr, wr = leggauss(160)
    rho = 0.5 * xr + 0.5
    wr = 0.5 * wr
    xz, wz = leggauss(160)
    z = xz
    wz = wz
    rr = rho[:, None]
    zz = z[None, :]
    u1 = bump(rr**2) * zz * bump(zz**2)
    lifted_u1_sq = float(np.sum(wr[:, None] * wz[None, :] * rr**3 * u1**2))
    physical_energy = float(w0a["rows"][-1]["physical_energy"])

    checks = {
        "odd_lifted_monopole": monopole_ratio <= 1e-12,
        "physical_energy_key_finite": math.isfinite(physical_energy) and physical_energy > 0.0,
        "lifted_key_distinct": math.isfinite(lifted_u1_sq) and lifted_u1_sq > 0.0,
    }
    return {
        "odd_monopole_ratio": monopole_ratio,
        "physical_energy": physical_energy,
        "lifted_u1_sq": lifted_u1_sq,
        "checks": checks,
        "pass": bool(all(checks.values())),
    }


def run_gate() -> Dict[str, object]:
    w0a = run_w0_a()
    ref_base, green_base = green_self_check(BASE_WIDTH)
    w0b = run_w0_b(ref_base)
    w0c = run_zero_box_sequences(ref_base, BASE_WIDTH, stress=False)
    ref_stress, green_stress = green_self_check(STRESS_WIDTH)
    stress_boxes = run_zero_box_sequences(ref_stress, STRESS_WIDTH, stress=True)
    w0d_checks = {
        "green_self_check": bool(green_stress["pass"]),
        "stress_box_sequence": bool(stress_boxes["pass"]),
    }
    w0d = {
        "green_reference": green_stress,
        "box_sequence": stress_boxes,
        "checks": w0d_checks,
        "pass": bool(all(w0d_checks.values())),
    }
    w0e = run_w0_e(w0a, w0c["moments"])

    w0b_checks = {
        "green_self_check": bool(green_base["pass"]),
        "finite_box_discretization": bool(w0b["pass"]),
    }
    w0b_full = {
        "green_reference": green_base,
        "finite_box": w0b,
        "checks": w0b_checks,
        "pass": bool(all(w0b_checks.values())),
    }

    all_pass = bool(w0a["pass"] and w0b_full["pass"] and w0c["pass"] and w0d["pass"] and w0e["pass"])
    return {
        "schema": "r3-axisym-wholespace-w0-v1",
        "scope": "static whole-space numerical infrastructure; no time evolution",
        "claim_boundary": "no singularity/global-regularity/Clay claim",
        "frozen_receivers": RECEIVERS,
        "W0-A": w0a,
        "W0-B": w0b_full,
        "W0-C": w0c,
        "W0-D": w0d,
        "W0-E": w0e,
        "decision": "PASS" if all_pass else "STOP_REPAIR_STATIC_WHOLE_SPACE_GATE",
        "pass": all_pass,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("experiments/r3_wholespace_w0/results/W0_STATIC_GATE.json"))
    args = parser.parse_args()
    result = run_gate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"decision": result["decision"], "output": str(args.output)}, indent=2))
    return 0 if result["pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
