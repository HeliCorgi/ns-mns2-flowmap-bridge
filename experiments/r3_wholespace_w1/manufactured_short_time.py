#!/usr/bin/env python3
"""Short-time manufactured nonlinear W1 gate.

This script implements the frozen gate in
`docs/gates/R3_AXISYM_WHOLESPACE_W1_MANUFACTURED_PREREG_2026-09-07.md`.
It is a finite-box numerical preflight only: no amplification, singularity,
regularity, continuum-convergence, or Clay claim is made.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np
from scipy import sparse
from scipy.sparse import linalg as spla

PI = math.pi
NU = 0.01
A0 = 0.16
RMAX = 2.0
ZMAX = 2.0
T_FINAL = 2.0e-4
DT = 2.5e-5
STABILITY_TOL = 1.0e-10
NTHETA = 1025
CORE_R = 0.8
CORE_Z = 0.8


def bump(s: np.ndarray | float) -> np.ndarray:
    a = np.asarray(s, dtype=float)
    out = np.zeros_like(a)
    mask = (a >= 0.0) & (a < 1.0)
    out[mask] = np.exp(-a[mask] / (1.0 - a[mask]))
    return out


def bump_prime(s: np.ndarray | float) -> np.ndarray:
    a = np.asarray(s, dtype=float)
    out = np.zeros_like(a)
    mask = (a >= 0.0) & (a < 1.0)
    bm = np.exp(-a[mask] / (1.0 - a[mask]))
    out[mask] = -bm / (1.0 - a[mask]) ** 2
    return out


def bump_second(s: np.ndarray | float) -> np.ndarray:
    a = np.asarray(s, dtype=float)
    out = np.zeros_like(a)
    mask = (a >= 0.0) & (a < 1.0)
    bm = np.exp(-a[mask] / (1.0 - a[mask]))
    out[mask] = bm * (2.0 * a[mask] - 1.0) / (1.0 - a[mask]) ** 4
    return out


def method_poly(z: np.ndarray, method: str) -> np.ndarray:
    if method == "rk4":
        return 1.0 + z + z**2 / 2.0 + z**3 / 6.0 + z**4 / 24.0
    if method == "ssprk3":
        return 1.0 + z + z**2 / 2.0 + z**3 / 6.0
    raise ValueError(method)


class RuntimeStabilityScanner:
    """Precomputed 1025x1025 frozen-symbol scanner for one grid spacing."""

    def __init__(self, h: float):
        theta = np.linspace(-PI, PI, NTHETA)
        self.sr = np.sin(theta)[:, None]
        self.sz = np.sin(theta)[None, :]
        q = 4.0 * np.sin(0.5 * theta) ** 2
        self.real = -NU * (q[:, None] / h**2 + q[None, :] / h**2)
        self.h = h
        self.radial_stress = 3.0 * NU / h

    def max_amp(self, method: str, max_ur: float, max_uz: float, dt: float) -> float:
        cr = abs(max_ur) + self.radial_stress
        cz = abs(max_uz)
        imag = -(cr * self.sr / self.h + cz * self.sz / self.h)
        lam = self.real + 1j * imag
        return float(np.max(np.abs(method_poly(dt * lam, method))))


def assemble_minus_l5(r: np.ndarray, z: np.ndarray, h: float) -> sparse.csr_matrix:
    """Assemble -L5 for unknowns i=0..nr-2, j=1..nz-2."""
    nr = len(r)
    nz = len(z)
    ni = nr - 1
    nj = nz - 2
    rows: List[int] = []
    cols: List[int] = []
    vals: List[float] = []
    h2 = h * h

    def idx(i: int, j: int) -> int:
        return i * nj + (j - 1)

    for i in range(ni):
        ri = float(r[i])
        for j in range(1, nz - 1):
            p = idx(i, j)
            diag = 2.0 / h2
            if j > 1:
                rows.append(p); cols.append(idx(i, j - 1)); vals.append(-1.0 / h2)
            if j < nz - 2:
                rows.append(p); cols.append(idx(i, j + 1)); vals.append(-1.0 / h2)

            if i == 0:
                diag += 8.0 / h2
                rows.append(p); cols.append(idx(1, j)); vals.append(-8.0 / h2)
            else:
                diag += 2.0 / h2
                cm = -1.0 / h2 + 3.0 / (2.0 * ri * h)
                cp = -1.0 / h2 - 3.0 / (2.0 * ri * h)
                rows.append(p); cols.append(idx(i - 1, j)); vals.append(cm)
                if i < ni - 1:
                    rows.append(p); cols.append(idx(i + 1, j)); vals.append(cp)
            rows.append(p); cols.append(p); vals.append(diag)

    n = ni * nj
    return sparse.csr_matrix((vals, (rows, cols)), shape=(n, n))


@dataclass
class GridSolver:
    h: float

    def __post_init__(self) -> None:
        self.nr = int(round(RMAX / self.h)) + 1
        self.nz = int(round(2.0 * ZMAX / self.h)) + 1
        self.r = np.linspace(0.0, RMAX, self.nr)
        self.z = np.linspace(-ZMAX, ZMAX, self.nz)
        if abs(self.r[1] - self.r[0] - self.h) > 1e-13 or abs(self.z[1] - self.z[0] - self.h) > 1e-13:
            raise ValueError("frozen grid spacing mismatch")
        self.rr = self.r[:, None]
        self.zz = self.z[None, :]
        self.ni = self.nr - 1
        self.nj = self.nz - 2
        self.op = assemble_minus_l5(self.r, self.z, self.h).tocsc()
        self.solve_factor = spla.factorized(self.op)
        self.scanner = RuntimeStabilityScanner(self.h)
        self.core = (self.rr <= CORE_R + 1e-14) & (np.abs(self.zz) <= CORE_Z + 1e-14)

    def initial_state(self) -> Tuple[np.ndarray, np.ndarray]:
        u = A0 * bump(self.rr**2) * self.zz * bump(self.zz**2)
        w = np.zeros_like(u)
        self.zero_outer(u)
        self.zero_outer(w)
        return u, w

    def zero_outer(self, f: np.ndarray) -> None:
        f[-1, :] = 0.0
        f[:, 0] = 0.0
        f[:, -1] = 0.0

    def pack_unknown(self, f: np.ndarray) -> np.ndarray:
        return np.asarray(f[:-1, 1:-1], dtype=float).reshape(-1)

    def unpack_unknown(self, x: np.ndarray) -> np.ndarray:
        f = np.zeros((self.nr, self.nz), dtype=float)
        f[:-1, 1:-1] = np.asarray(x).reshape((self.ni, self.nj))
        return f

    def solve_psi(self, w: np.ndarray) -> Tuple[np.ndarray, float]:
        rhs = self.pack_unknown(w)
        if float(np.linalg.norm(rhs)) == 0.0:
            return np.zeros_like(w), 0.0
        x = np.asarray(self.solve_factor(rhs), dtype=float)
        psi = self.unpack_unknown(x)
        res = self.op @ x - rhs
        rel = float(np.linalg.norm(res) / np.linalg.norm(rhs))
        return psi, rel

    def d_r(self, f: np.ndarray) -> np.ndarray:
        d = np.zeros_like(f)
        d[0, :] = 0.0
        d[1:-1, :] = (f[2:, :] - f[:-2, :]) / (2.0 * self.h)
        d[-1, :] = (3.0 * f[-1, :] - 4.0 * f[-2, :] + f[-3, :]) / (2.0 * self.h)
        return d

    def d_z(self, f: np.ndarray) -> np.ndarray:
        d = np.zeros_like(f)
        d[:, 1:-1] = (f[:, 2:] - f[:, :-2]) / (2.0 * self.h)
        d[:, 0] = (-3.0 * f[:, 0] + 4.0 * f[:, 1] - f[:, 2]) / (2.0 * self.h)
        d[:, -1] = (3.0 * f[:, -1] - 4.0 * f[:, -2] + f[:, -3]) / (2.0 * self.h)
        return d

    def l5(self, f: np.ndarray) -> np.ndarray:
        out = np.zeros_like(f)
        h2 = self.h**2
        # Axis: 4 f_rr + f_zz with even ghost, f_rr = 2(f1-f0)/h^2.
        out[0, 1:-1] = (
            8.0 * (f[1, 1:-1] - f[0, 1:-1]) / h2
            + (f[0, 2:] - 2.0 * f[0, 1:-1] + f[0, :-2]) / h2
        )
        if self.nr > 2:
            ri = self.r[1:-1, None]
            frr = (f[2:, 1:-1] - 2.0 * f[1:-1, 1:-1] + f[:-2, 1:-1]) / h2
            fr = (f[2:, 1:-1] - f[:-2, 1:-1]) / (2.0 * self.h)
            fzz = (f[1:-1, 2:] - 2.0 * f[1:-1, 1:-1] + f[1:-1, :-2]) / h2
            out[1:-1, 1:-1] = frr + 3.0 * fr / ri + fzz
        self.zero_outer(out)
        return out

    def velocities(self, psi: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        pr = self.d_r(psi)
        pz = self.d_z(psi)
        ur = -self.rr * pz
        uz = 2.0 * psi + self.rr * pr
        return ur, uz, pr, pz

    def spatial_rhs(self, u: np.ndarray, w: np.ndarray) -> Tuple[np.ndarray, np.ndarray, Dict[str, float]]:
        psi, pres = self.solve_psi(w)
        ur, uz, _pr, pz = self.velocities(psi)
        urad = self.d_r(u)
        uzed = self.d_z(u)
        wrad = self.d_r(w)
        wzed = self.d_z(w)
        du = -ur * urad - uz * uzed + 2.0 * pz * u + NU * self.l5(u)
        dw = -ur * wrad - uz * wzed + self.d_z(u * u) + NU * self.l5(w)
        self.zero_outer(du)
        self.zero_outer(dw)
        return du, dw, {
            "poisson_residual": pres,
            "max_abs_ur": float(np.max(np.abs(ur))),
            "max_abs_uz": float(np.max(np.abs(uz))),
        }

    def stage_record(self, method: str, dt: float, u: np.ndarray, w: np.ndarray, tag: str) -> Tuple[np.ndarray, np.ndarray, Dict[str, object]]:
        du, dw, meta = self.spatial_rhs(u, w)
        maxur = float(meta["max_abs_ur"])
        maxuz = float(meta["max_abs_uz"])
        amp = self.scanner.max_amp(method, maxur, maxuz, dt)
        cfl = dt * (maxur / self.h + maxuz / self.h)
        visc = NU * dt * (12.0 / self.h**2)
        finite = bool(np.isfinite(u).all() and np.isfinite(w).all() and np.isfinite(du).all() and np.isfinite(dw).all())
        rec: Dict[str, object] = {
            "tag": tag,
            "max_abs_ur": maxur,
            "max_abs_uz": maxuz,
            "cfl": float(cfl),
            "viscous_number": float(visc),
            "frozen_symbol_max_amplification": float(amp),
            "poisson_residual": float(meta["poisson_residual"]),
            "finite": finite,
        }
        rec["safe"] = bool(finite and amp <= 1.0 + STABILITY_TOL and cfl <= 0.10 and visc <= 0.05)
        return du, dw, rec

    def odd_defect(self, f: np.ndarray) -> float:
        scale = float(np.max(np.abs(f)))
        if scale == 0.0:
            return 0.0
        return float(np.max(np.abs(f + f[:, ::-1])) / scale)

    def state_diagnostics(self, u: np.ndarray, w: np.ndarray) -> Dict[str, float | bool]:
        psi, pres = self.solve_psi(w)
        ur, uz, _pr, _pz = self.velocities(psi)

        # Recovered axisymmetric divergence, evaluated independently from recovered velocities.
        dur = self.d_r(ur)
        duz = self.d_z(uz)
        div = np.zeros_like(u)
        div[1:, :] = dur[1:, :] + ur[1:, :] / self.rr[1:, :] + duz[1:, :]
        sl = np.zeros_like(u, dtype=bool)
        sl[2:-2, 2:-2] = True
        div_num = float(np.max(np.abs(div[sl]))) if np.any(sl) else 0.0
        div_den_field = np.zeros_like(u)
        div_den_field[1:, :] = np.abs(dur[1:, :]) + np.abs(ur[1:, :] / self.rr[1:, :]) + np.abs(duz[1:, :])
        div_den = float(np.max(div_den_field[sl])) if np.any(sl) else 0.0
        rel_div = div_num / max(div_den, 1e-30)

        utheta = self.rr * u
        energy_density = ur * ur + uz * uz + utheta * utheta
        energy = float(2.0 * PI * np.sum(self.rr * energy_density) * self.h**2)

        wr = -self.rr * self.d_z(u)
        wt = self.rr * w
        wz = 2.0 * u + self.rr * self.d_r(u)
        omega2 = wr * wr + wt * wt + wz * wz
        enstrophy = float(2.0 * PI * np.sum(self.rr * omega2) * self.h**2)

        return {
            "finite": bool(np.isfinite(u).all() and np.isfinite(w).all() and np.isfinite(psi).all()),
            "poisson_residual": float(pres),
            "odd_u1": self.odd_defect(u),
            "odd_omega1": self.odd_defect(w),
            "odd_psi1": self.odd_defect(psi),
            "relative_recovered_divergence": float(rel_div),
            "physical_energy": energy,
            "physical_enstrophy": enstrophy,
        }

    def exact_initial_derivatives(self) -> Tuple[np.ndarray, np.ndarray]:
        r2 = self.rr**2
        z2 = self.zz**2
        br = bump(r2)
        bp_r = bump_prime(r2)
        bpp_r = bump_second(r2)
        bz = bump(z2)
        bp_z = bump_prime(z2)
        bpp_z = bump_second(z2)
        g = self.zz * bz
        gz = bz + 2.0 * z2 * bp_z
        gzz = 6.0 * self.zz * bp_z + 4.0 * self.zz**3 * bpp_z
        radial = 8.0 * bp_r + 4.0 * r2 * bpp_r
        l5u = A0 * (radial * g + br * gzz)
        du = NU * l5u
        dw = 2.0 * A0**2 * br**2 * g * gz
        return du, dw

    def rel_core(self, a: np.ndarray, b: np.ndarray) -> float:
        av = np.asarray(a[self.core], dtype=float)
        bv = np.asarray(b[self.core], dtype=float)
        den = float(np.linalg.norm(bv))
        return float(np.linalg.norm(av - bv) / max(den, 1e-30))

    def combined_rel_core(self, ua: np.ndarray, wa: np.ndarray, ub: np.ndarray, wb: np.ndarray) -> float:
        du = np.asarray((ua - ub)[self.core], dtype=float)
        dw = np.asarray((wa - wb)[self.core], dtype=float)
        bu = np.asarray(ub[self.core], dtype=float)
        bw = np.asarray(wb[self.core], dtype=float)
        num = math.sqrt(float(np.dot(du, du) + np.dot(dw, dw)))
        den = math.sqrt(float(np.dot(bu, bu) + np.dot(bw, bw)))
        return num / max(den, 1e-30)


@dataclass
class RunResult:
    method: str
    h: float
    initial_u: np.ndarray
    initial_w: np.ndarray
    first_u: Optional[np.ndarray]
    first_w: Optional[np.ndarray]
    final_u: np.ndarray
    final_w: np.ndarray
    stage_rows: List[Dict[str, object]]
    step_rows: List[Dict[str, object]]
    rejected_steps: int
    completed: bool


def add_state(u: np.ndarray, du: np.ndarray, factor: float) -> np.ndarray:
    out = u + factor * du
    out[-1, :] = 0.0
    out[:, 0] = 0.0
    out[:, -1] = 0.0
    return out


def run_integrator(s: GridSolver, method: str) -> RunResult:
    u, w = s.initial_state()
    u0 = u.copy(); w0 = w.copy()
    first_u: Optional[np.ndarray] = None
    first_w: Optional[np.ndarray] = None
    stages: List[Dict[str, object]] = []
    steps: List[Dict[str, object]] = []
    rejected = 0
    d0 = s.state_diagnostics(u, w)
    e0 = float(d0["physical_energy"])
    prev_diag = d0

    nsteps = int(round(T_FINAL / DT))
    for n in range(nsteps):
        local: List[Dict[str, object]] = []
        if method == "rk4":
            k1u, k1w, r1 = s.stage_record(method, DT, u, w, f"step{n}:k1")
            local.append(r1)
            u2 = add_state(u, k1u, 0.5 * DT); w2 = add_state(w, k1w, 0.5 * DT)
            k2u, k2w, r2 = s.stage_record(method, DT, u2, w2, f"step{n}:k2")
            local.append(r2)
            u3 = add_state(u, k2u, 0.5 * DT); w3 = add_state(w, k2w, 0.5 * DT)
            k3u, k3w, r3 = s.stage_record(method, DT, u3, w3, f"step{n}:k3")
            local.append(r3)
            u4 = add_state(u, k3u, DT); w4 = add_state(w, k3w, DT)
            k4u, k4w, r4 = s.stage_record(method, DT, u4, w4, f"step{n}:k4")
            local.append(r4)
            if not all(bool(r["safe"]) for r in local):
                rejected += 1; stages.extend(local)
                return RunResult(method, s.h, u0, w0, first_u, first_w, u, w, stages, steps, rejected, False)
            un = u + (DT / 6.0) * (k1u + 2.0 * k2u + 2.0 * k3u + k4u)
            wn = w + (DT / 6.0) * (k1w + 2.0 * k2w + 2.0 * k3w + k4w)
        elif method == "ssprk3":
            f1u, f1w, r1 = s.stage_record(method, DT, u, w, f"step{n}:s1")
            local.append(r1)
            y1u = add_state(u, f1u, DT); y1w = add_state(w, f1w, DT)
            f2u, f2w, r2 = s.stage_record(method, DT, y1u, y1w, f"step{n}:s2")
            local.append(r2)
            y2u = 0.75 * u + 0.25 * (y1u + DT * f2u)
            y2w = 0.75 * w + 0.25 * (y1w + DT * f2w)
            s.zero_outer(y2u); s.zero_outer(y2w)
            f3u, f3w, r3 = s.stage_record(method, DT, y2u, y2w, f"step{n}:s3")
            local.append(r3)
            if not all(bool(r["safe"]) for r in local):
                rejected += 1; stages.extend(local)
                return RunResult(method, s.h, u0, w0, first_u, first_w, u, w, stages, steps, rejected, False)
            un = (1.0 / 3.0) * u + (2.0 / 3.0) * (y2u + DT * f3u)
            wn = (1.0 / 3.0) * w + (2.0 / 3.0) * (y2w + DT * f3w)
        else:
            raise ValueError(method)

        s.zero_outer(un); s.zero_outer(wn)
        stages.extend(local)
        if n == 0:
            first_u = un.copy(); first_w = wn.copy()

        diag = s.state_diagnostics(un, wn)
        old_e = float(prev_diag["physical_energy"])
        new_e = float(diag["physical_energy"])
        old_o = float(prev_diag["physical_enstrophy"])
        new_o = float(diag["physical_enstrophy"])
        diss = 2.0 * NU * 0.5 * (old_o + new_o)
        eb = abs((new_e - old_e) / DT + diss) / max(diss, 1e-30)
        step_row: Dict[str, object] = {
            "step": n + 1,
            "time": (n + 1) * DT,
            **diag,
            "energy_balance_defect": float(eb),
            "energy_ratio_to_initial": float(new_e / e0),
        }
        steps.append(step_row)
        u, w = un, wn
        prev_diag = diag

    return RunResult(method, s.h, u0, w0, first_u, first_w, u, w, stages, steps, rejected, True)


def streamed_summary(run: RunResult) -> Dict[str, object]:
    if run.stage_rows:
        max_amp = max(float(r["frozen_symbol_max_amplification"]) for r in run.stage_rows)
        max_cfl = max(float(r["cfl"]) for r in run.stage_rows)
        max_visc = max(float(r["viscous_number"]) for r in run.stage_rows)
        max_stage_pres = max(float(r["poisson_residual"]) for r in run.stage_rows)
        all_stage_finite = all(bool(r["finite"]) for r in run.stage_rows)
    else:
        max_amp = max_cfl = max_visc = max_stage_pres = math.inf
        all_stage_finite = False
    if run.step_rows:
        max_pres = max(float(r["poisson_residual"]) for r in run.step_rows)
        max_odd = max(max(float(r["odd_u1"]), float(r["odd_omega1"]), float(r["odd_psi1"])) for r in run.step_rows)
        max_div = max(float(r["relative_recovered_divergence"]) for r in run.step_rows)
        max_eratio = max(float(r["energy_ratio_to_initial"]) for r in run.step_rows)
        max_eb = max(float(r["energy_balance_defect"]) for r in run.step_rows)
        all_step_finite = all(bool(r["finite"]) for r in run.step_rows)
    else:
        max_pres = max_odd = max_div = max_eratio = max_eb = math.inf
        all_step_finite = False
    return {
        "completed": run.completed,
        "rejected_steps": run.rejected_steps,
        "all_stage_finite": all_stage_finite,
        "all_step_finite": all_step_finite,
        "max_frozen_symbol_amplification": max_amp,
        "max_cfl": max_cfl,
        "max_viscous_number": max_visc,
        "max_stage_poisson_residual": max_stage_pres,
        "max_step_poisson_residual": max_pres,
        "max_odd_z_defect": max_odd,
        "max_relative_recovered_divergence": max_div,
        "max_energy_ratio_to_initial": max_eratio,
        "max_energy_balance_defect": max_eb,
    }


def m1_initial_rhs(s: GridSolver) -> Dict[str, float]:
    u0, w0 = s.initial_state()
    du, dw, _ = s.spatial_rhs(u0, w0)
    eu, ew = s.exact_initial_derivatives()
    return {"u1": s.rel_core(du, eu), "omega1": s.rel_core(dw, ew)}


def m2_first_secant(s: GridSolver, run: RunResult) -> Dict[str, float]:
    if run.first_u is None or run.first_w is None:
        return {"u1": math.inf, "omega1": math.inf}
    eu, ew = s.exact_initial_derivatives()
    du = (run.first_u - run.initial_u) / DT
    dw = (run.first_w - run.initial_w) / DT
    return {"u1": s.rel_core(du, eu), "omega1": s.rel_core(dw, ew)}


def restrict_fine_to_coarse(f: np.ndarray) -> np.ndarray:
    return f[::2, ::2]


def run_gate() -> Dict[str, object]:
    solvers = {h: GridSolver(h) for h in (0.04, 0.02)}
    m1 = {f"h_{h:.2f}": m1_initial_rhs(solvers[h]) for h in (0.04, 0.02)}

    runs: Dict[Tuple[float, str], RunResult] = {}
    for h in (0.04, 0.02):
        for method in ("rk4", "ssprk3"):
            runs[(h, method)] = run_integrator(solvers[h], method)

    m2 = {f"h_{h:.2f}": m2_first_secant(solvers[h], runs[(h, "rk4")]) for h in (0.04, 0.02)}
    summaries = {f"h_{h:.2f}_{method}": streamed_summary(runs[(h, method)]) for h in (0.04, 0.02) for method in ("rk4", "ssprk3")}

    m5_integrator: Dict[str, float] = {}
    for h in (0.04, 0.02):
        r4 = runs[(h, "rk4")]
        r3 = runs[(h, "ssprk3")]
        m5_integrator[f"h_{h:.2f}"] = solvers[h].combined_rel_core(r4.final_u, r4.final_w, r3.final_u, r3.final_w)

    coarse = solvers[0.04]
    rc = runs[(0.04, "rk4")]
    rf = runs[(0.02, "rk4")]
    fu = restrict_fine_to_coarse(rf.final_u)
    fw = restrict_fine_to_coarse(rf.final_w)
    m5_resolution = {
        "u1": coarse.rel_core(rc.final_u, fu),
        "omega1": coarse.rel_core(rc.final_w, fw),
    }

    checks: Dict[str, bool] = {}
    # M1
    checks["M1_h04_u"] = m1["h_0.04"]["u1"] <= 0.020
    checks["M1_h04_w"] = m1["h_0.04"]["omega1"] <= 0.025
    checks["M1_h02_u"] = m1["h_0.02"]["u1"] <= 0.006
    checks["M1_h02_w"] = m1["h_0.02"]["omega1"] <= 0.006
    checks["M1_reduction_u"] = m1["h_0.02"]["u1"] <= 0.35 * m1["h_0.04"]["u1"]
    checks["M1_reduction_w"] = m1["h_0.02"]["omega1"] <= 0.35 * m1["h_0.04"]["omega1"]
    # M2
    checks["M2_h04_u"] = m2["h_0.04"]["u1"] <= 0.025
    checks["M2_h04_w"] = m2["h_0.04"]["omega1"] <= 0.030
    checks["M2_h02_u"] = m2["h_0.02"]["u1"] <= 0.008
    checks["M2_h02_w"] = m2["h_0.02"]["omega1"] <= 0.008
    checks["M2_decrease_u"] = m2["h_0.02"]["u1"] < m2["h_0.04"]["u1"]
    checks["M2_decrease_w"] = m2["h_0.02"]["omega1"] < m2["h_0.04"]["omega1"]
    # M3/M4 all runs
    for key, ss in summaries.items():
        checks[f"{key}_completed"] = bool(ss["completed"])
        checks[f"{key}_no_reject"] = int(ss["rejected_steps"]) == 0
        checks[f"{key}_finite"] = bool(ss["all_stage_finite"] and ss["all_step_finite"])
        checks[f"{key}_amp"] = float(ss["max_frozen_symbol_amplification"]) <= 1.0 + STABILITY_TOL
        checks[f"{key}_cfl"] = float(ss["max_cfl"]) <= 0.10
        checks[f"{key}_visc"] = float(ss["max_viscous_number"]) <= 0.05
        checks[f"{key}_poisson"] = max(float(ss["max_stage_poisson_residual"]), float(ss["max_step_poisson_residual"])) <= 1e-10
        checks[f"{key}_odd"] = float(ss["max_odd_z_defect"]) <= 1e-12
        checks[f"{key}_div"] = float(ss["max_relative_recovered_divergence"]) <= 1e-10
        checks[f"{key}_energy"] = float(ss["max_energy_ratio_to_initial"]) <= 1.0 + 1e-5
        checks[f"{key}_energy_balance"] = float(ss["max_energy_balance_defect"]) <= 0.20
    # M5
    checks["M5_integrator_h04"] = m5_integrator["h_0.04"] <= 2e-6
    checks["M5_integrator_h02"] = m5_integrator["h_0.02"] <= 2e-6
    checks["M5_resolution_u"] = m5_resolution["u1"] <= 2e-4
    checks["M5_resolution_w"] = m5_resolution["omega1"] <= 0.030

    passed = bool(all(checks.values()))
    return {
        "schema": "r3-w1-manufactured-v1",
        "frozen_parameters": {
            "nu": NU, "A": A0, "R": 1.0, "Z": 1.0, "alpha": 16.0, "kappa": 1.0,
            "Rmax": RMAX, "Zmax": ZMAX, "h": [0.04, 0.02], "T": T_FINAL, "dt": DT,
            "primary_integrator": "rk4", "comparison_integrator": "ssprk3",
        },
        "M1_initial_rhs_relative_errors": m1,
        "M2_first_step_secant_relative_errors": m2,
        "M3_M4_streamed_summaries": summaries,
        "M5_integrator_relative_state_difference": m5_integrator,
        "M5_resolution_relative_difference": m5_resolution,
        "checks": checks,
        "decision": "PASS" if passed else "STOP_REPAIR_W1_MANUFACTURED",
        "pass": passed,
        "claim_boundary": "short-time finite-box manufactured nonlinear preflight only",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("experiments/r3_wholespace_w1/results/W1_MANUFACTURED_SHORT_TIME.json"))
    args = parser.parse_args()
    result = run_gate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"decision": result["decision"], "output": str(args.output)}, indent=2))
    return 0 if result["pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
