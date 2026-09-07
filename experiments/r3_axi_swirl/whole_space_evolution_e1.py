"""Fail-closed E1 nonlinear prototype for the R^3 axisymmetric-with-swirl track.

This is a truncated-box finite-difference approximation to the normalized axisymmetric
Navier--Stokes system from SPEC.md. It uses strictly nonperiodic z, zero artificial outer
Dirichlet data, a factorized -L5 elliptic solve, centered second-order derivatives and SSPRK3.

The artificial boundary is NOT a validated free-space boundary condition. E1 is an integrator
and streaming-diagnostics gate only; domain/truncation convergence remains an E2 obligation.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import math
from typing import Any

import numpy as np
import scipy.sparse.linalg as spla

import compact_family as cf
import free_space_elliptic_prototype as ep


@dataclass(frozen=True)
class E1Config:
    seed_index: int = 4
    nu: float = 2.0e-3
    T: float = 2.0e-2
    Rmax: float = 0.8
    Zmax: float = 0.7
    nr: int = 96
    nz: int = 168
    dt_cap: float = 1.0e-3
    cfl_limit: float = 0.40
    viscous_limit: float = 0.80
    min_dt: float = 1.0e-8
    max_rejected_steps: int = 20
    boundary_shell_cells: int = 4

    def validate(self) -> None:
        if not (0 <= self.seed_index < len(cf.FROZEN_GEOMETRY_LATTICE)):
            raise ValueError("invalid seed_index")
        positive = (
            self.nu,
            self.T,
            self.Rmax,
            self.Zmax,
            self.dt_cap,
            self.cfl_limit,
            self.viscous_limit,
            self.min_dt,
        )
        if not all(math.isfinite(float(x)) and float(x) > 0.0 for x in positive):
            raise ValueError("E1 positive parameters must be finite and positive")
        if self.nr < 16 or self.nz < 32:
            raise ValueError("E1 grid is too small")
        if self.boundary_shell_cells < 1:
            raise ValueError("boundary_shell_cells must be positive")


@dataclass
class StateDiagnostics:
    finite: bool
    energy: float
    gamma_abs_max: float
    axis_regular_defect: float
    divergence_rel_linf: float
    elliptic_residual_linf: float
    min_gradient_scale_points: float
    curvature_tail_max: float
    boundary_shell_ratio: float
    max_speed: float
    max_abs_u1: float
    max_abs_omega1: float


class WholeSpaceE1:
    def __init__(self, cfg: E1Config):
        cfg.validate()
        self.cfg = cfg
        self.system = ep.build_minus_l5(
            ep.Box(cfg.Rmax, cfg.Zmax, cfg.nr, cfg.nz),
            lambda r, z: 0.0,
        )
        self.r = self.system.r
        self.z = self.system.z
        self.dr = self.system.dr
        self.dz = self.system.dz
        self.A = self.system.A
        self._solve = spla.factorized(self.A.tocsc())
        self._row_abs_bound = float(np.asarray(abs(self.A).sum(axis=1)).ravel().max())
        if not math.isfinite(self._row_abs_bound) or self._row_abs_bound <= 0.0:
            raise RuntimeError("invalid -L5 row-absolute-sum bound")

    @property
    def viscous_rate_bound(self) -> float:
        return self.cfg.nu * self._row_abs_bound

    def initial_state(self) -> tuple[np.ndarray, np.ndarray]:
        p = cf.FROZEN_GEOMETRY_LATTICE[self.cfg.seed_index]
        R, Z = np.meshgrid(self.r, self.z, indexing="ij")
        f = cf.scalar_fields(R, Z, p)
        return np.asarray(f["u1"], dtype=float), np.asarray(f["omega1"], dtype=float)

    def solve_psi(self, omega1: np.ndarray) -> np.ndarray:
        arr = np.asarray(omega1, dtype=float)
        if arr.shape != self.system.boundary_rhs.shape:
            raise ValueError("omega1 shape mismatch")
        psi = self._solve(arr.ravel()).reshape(arr.shape)
        return np.asarray(psi, dtype=float)

    def d_r_even(self, f: np.ndarray) -> np.ndarray:
        f = np.asarray(f, dtype=float)
        out = np.empty_like(f)
        out[0, :] = 0.0
        out[1:-1, :] = (f[2:, :] - f[:-2, :]) / (2.0 * self.dr)
        out[-1, :] = (0.0 - f[-2, :]) / (2.0 * self.dr)
        return out

    def d_r_odd(self, f: np.ndarray) -> np.ndarray:
        f = np.asarray(f, dtype=float)
        out = np.empty_like(f)
        out[0, :] = f[1, :] / self.dr
        out[1:-1, :] = (f[2:, :] - f[:-2, :]) / (2.0 * self.dr)
        out[-1, :] = (0.0 - f[-2, :]) / (2.0 * self.dr)
        return out

    def d_z_zero(self, f: np.ndarray) -> np.ndarray:
        f = np.asarray(f, dtype=float)
        out = np.empty_like(f)
        out[:, 1:-1] = (f[:, 2:] - f[:, :-2]) / (2.0 * self.dz)
        out[:, 0] = f[:, 1] / (2.0 * self.dz)
        out[:, -1] = -f[:, -2] / (2.0 * self.dz)
        return out

    def d_rr_even(self, f: np.ndarray) -> np.ndarray:
        f = np.asarray(f, dtype=float)
        out = np.empty_like(f)
        out[0, :] = 2.0 * (f[1, :] - f[0, :]) / self.dr**2
        out[1:-1, :] = (f[2:, :] - 2.0 * f[1:-1, :] + f[:-2, :]) / self.dr**2
        out[-1, :] = (f[-2, :] - 2.0 * f[-1, :]) / self.dr**2
        return out

    def d_zz_zero(self, f: np.ndarray) -> np.ndarray:
        f = np.asarray(f, dtype=float)
        out = np.empty_like(f)
        out[:, 1:-1] = (f[:, 2:] - 2.0 * f[:, 1:-1] + f[:, :-2]) / self.dz**2
        out[:, 0] = (f[:, 1] - 2.0 * f[:, 0]) / self.dz**2
        out[:, -1] = (f[:, -2] - 2.0 * f[:, -1]) / self.dz**2
        return out

    def apply_l5_zero_boundary(self, f: np.ndarray) -> np.ndarray:
        return -(self.A @ np.asarray(f, dtype=float).ravel()).reshape(f.shape)

    def reconstruct(self, omega1: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        psi1 = self.solve_psi(omega1)
        psi_r = self.d_r_even(psi1)
        psi_z = self.d_z_zero(psi1)
        ur = -self.r[:, None] * psi_z
        uz = 2.0 * psi1 + self.r[:, None] * psi_r
        return psi1, ur, uz

    def advective_rate(self, omega1: np.ndarray) -> float:
        _, ur, uz = self.reconstruct(omega1)
        return float(np.max(np.abs(ur)) / self.dr + np.max(np.abs(uz)) / self.dz)

    def rhs(self, u1: np.ndarray, omega1: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        psi1, ur, uz = self.reconstruct(omega1)
        u1_r = self.d_r_even(u1)
        u1_z = self.d_z_zero(u1)
        omega_r = self.d_r_even(omega1)
        omega_z = self.d_z_zero(omega1)
        psi_z = self.d_z_zero(psi1)
        du = (
            -ur * u1_r
            - uz * u1_z
            + 2.0 * psi_z * u1
            + self.cfg.nu * self.apply_l5_zero_boundary(u1)
        )
        domega = (
            -ur * omega_r
            - uz * omega_z
            + self.d_z_zero(u1 * u1)
            + self.cfg.nu * self.apply_l5_zero_boundary(omega1)
        )
        return du, domega

    def ssprk3_attempt(
        self, u1: np.ndarray, omega1: np.ndarray, dt: float
    ) -> tuple[np.ndarray, np.ndarray, dict[str, float]]:
        cfl_pre = dt * self.advective_rate(omega1)
        k1u, k1o = self.rhs(u1, omega1)
        u_stage1 = u1 + dt * k1u
        o_stage1 = omega1 + dt * k1o
        cfl_stage1 = dt * self.advective_rate(o_stage1)

        k2u, k2o = self.rhs(u_stage1, o_stage1)
        u_stage2 = 0.75 * u1 + 0.25 * (u_stage1 + dt * k2u)
        o_stage2 = 0.75 * omega1 + 0.25 * (o_stage1 + dt * k2o)
        cfl_stage2 = dt * self.advective_rate(o_stage2)

        k3u, k3o = self.rhs(u_stage2, o_stage2)
        u_new = (u1 + 2.0 * (u_stage2 + dt * k3u)) / 3.0
        o_new = (omega1 + 2.0 * (o_stage2 + dt * k3o)) / 3.0
        cfl_post = dt * self.advective_rate(o_new)
        return u_new, o_new, {
            "cfl_pre": float(cfl_pre),
            "cfl_stage1": float(cfl_stage1),
            "cfl_stage2": float(cfl_stage2),
            "cfl_post": float(cfl_post),
            "viscous_number": float(dt * self.viscous_rate_bound),
        }

    def _weighted_l2(self, f: np.ndarray) -> float:
        weight = 2.0 * math.pi * self.r[:, None]
        return math.sqrt(float(np.sum(weight * np.asarray(f, dtype=float) ** 2) * self.dr * self.dz))

    def _gradient_scale_points(self, f: np.ndarray) -> tuple[float, float]:
        amp = float(np.max(np.abs(f)))
        if amp == 0.0:
            return math.inf, math.inf
        fr = float(np.max(np.abs(self.d_r_even(f))))
        fz = float(np.max(np.abs(self.d_z_zero(f))))
        pr = math.inf if fr == 0.0 else amp / fr / self.dr
        pz = math.inf if fz == 0.0 else amp / fz / self.dz
        return pr, pz

    def _curvature_tail(self, f: np.ndarray) -> tuple[float, float]:
        norm = self._weighted_l2(f)
        if norm == 0.0:
            return 0.0, 0.0
        tr = self.dr**2 * self._weighted_l2(self.d_rr_even(f)) / norm
        tz = self.dz**2 * self._weighted_l2(self.d_zz_zero(f)) / norm
        return float(tr), float(tz)

    def _boundary_shell_ratio(self, f: np.ndarray) -> float:
        amp = float(np.max(np.abs(f)))
        if amp == 0.0:
            return 0.0
        k = min(
            self.cfg.boundary_shell_cells,
            max(1, f.shape[0] // 4),
            max(1, f.shape[1] // 4),
        )
        vals = [
            np.max(np.abs(f[-k:, :])),
            np.max(np.abs(f[:, :k])),
            np.max(np.abs(f[:, -k:])),
        ]
        return float(max(vals) / amp)

    def diagnostics(self, u1: np.ndarray, omega1: np.ndarray) -> StateDiagnostics:
        psi1, ur, uz = self.reconstruct(omega1)
        utheta = self.r[:, None] * u1
        omega_theta = self.r[:, None] * omega1
        energy = 0.5 * float(
            np.sum(2.0 * math.pi * self.r[:, None] * (ur**2 + uz**2 + utheta**2))
            * self.dr
            * self.dz
        )
        gamma = self.r[:, None] ** 2 * u1

        dur_dr = self.d_r_odd(ur)
        duz_dz = self.d_z_zero(uz)
        div = np.empty_like(u1)
        div[0, :] = 2.0 * dur_dr[0, :] + duz_dz[0, :]
        div[1:, :] = dur_dr[1:, :] + ur[1:, :] / self.r[1:, None] + duz_dz[1:, :]
        max_speed = float(max(np.max(np.abs(ur)), np.max(np.abs(uz)), np.max(np.abs(utheta))))
        divergence_scale = max(max_speed / min(self.dr, self.dz), 1.0e-30)
        divergence_rel = float(np.max(np.abs(div)) / divergence_scale)

        residual = (self.A @ psi1.ravel()).reshape(psi1.shape) - omega1
        elliptic_residual = float(np.max(np.abs(residual)))
        axis_defect = float(
            max(
                np.max(np.abs(ur[0, :])),
                np.max(np.abs(utheta[0, :])),
                np.max(np.abs(omega_theta[0, :])),
                np.max(np.abs(self.d_r_even(u1)[0, :])),
                np.max(np.abs(self.d_r_even(omega1)[0, :])),
                np.max(np.abs(self.d_r_even(psi1)[0, :])),
            )
        )

        scales = (*self._gradient_scale_points(u1), *self._gradient_scale_points(omega1))
        tails = (*self._curvature_tail(u1), *self._curvature_tail(omega1))
        boundary_ratio = max(self._boundary_shell_ratio(u1), self._boundary_shell_ratio(omega1))
        finite = bool(all(np.all(np.isfinite(x)) for x in (u1, omega1, psi1, ur, uz)))
        scalar_finite = all(
            math.isfinite(float(x))
            for x in (
                energy,
                np.max(np.abs(gamma)),
                axis_defect,
                divergence_rel,
                elliptic_residual,
                min(scales),
                max(tails),
                boundary_ratio,
                max_speed,
            )
        )
        return StateDiagnostics(
            finite=finite and scalar_finite,
            energy=energy,
            gamma_abs_max=float(np.max(np.abs(gamma))),
            axis_regular_defect=axis_defect,
            divergence_rel_linf=divergence_rel,
            elliptic_residual_linf=elliptic_residual,
            min_gradient_scale_points=float(min(scales)),
            curvature_tail_max=float(max(tails)),
            boundary_shell_ratio=float(boundary_ratio),
            max_speed=max_speed,
            max_abs_u1=float(np.max(np.abs(u1))),
            max_abs_omega1=float(np.max(np.abs(omega1))),
        )

    def choose_dt(self, omega1: np.ndarray, remaining: float) -> float:
        adv = self.advective_rate(omega1)
        adv_dt = math.inf if adv == 0.0 else 0.90 * self.cfg.cfl_limit / adv
        visc_dt = 0.90 * self.cfg.viscous_limit / self.viscous_rate_bound
        return float(min(self.cfg.dt_cap, adv_dt, visc_dt, remaining))

    def run(self) -> dict[str, Any]:
        u1, omega1 = self.initial_state()
        initial = self.diagnostics(u1, omega1)
        if not initial.finite:
            raise RuntimeError("non-finite E1 initial state")

        t = 0.0
        accepted = 0
        rejected = 0
        min_dt = math.inf
        max_dt = 0.0
        max_cfl_pre = 0.0
        max_cfl_stage1 = 0.0
        max_cfl_stage2 = 0.0
        max_cfl_post = 0.0
        max_viscous = 0.0
        max_positive_energy_change = 0.0
        max_gamma = initial.gamma_abs_max
        max_axis = initial.axis_regular_defect
        max_div = initial.divergence_rel_linf
        max_elliptic = initial.elliptic_residual_linf
        min_scale_points = initial.min_gradient_scale_points
        max_curvature_tail = initial.curvature_tail_max
        max_boundary_shell = initial.boundary_shell_ratio
        previous_energy = initial.energy
        snapshots = [{"t": 0.0, **asdict(initial)}]
        next_snapshot = self.cfg.T / 4.0

        while t < self.cfg.T - 1.0e-15:
            dt = self.choose_dt(omega1, self.cfg.T - t)
            if dt < self.cfg.min_dt:
                raise RuntimeError(f"E1 dt underflow before attempt: {dt}")

            while True:
                u_new, o_new, stage = self.ssprk3_attempt(u1, omega1, dt)
                stage_cfl = max(
                    stage["cfl_pre"],
                    stage["cfl_stage1"],
                    stage["cfl_stage2"],
                    stage["cfl_post"],
                )
                stage_finite = bool(np.all(np.isfinite(u_new)) and np.all(np.isfinite(o_new)))
                if (
                    stage_finite
                    and stage_cfl <= self.cfg.cfl_limit * (1.0 + 1.0e-12)
                    and stage["viscous_number"] <= self.cfg.viscous_limit * (1.0 + 1.0e-12)
                ):
                    break
                rejected += 1
                if rejected > self.cfg.max_rejected_steps:
                    raise RuntimeError("E1 exceeded max_rejected_steps")
                dt *= 0.5
                if dt < self.cfg.min_dt:
                    raise RuntimeError("E1 dt underflow after stage rejection")

            u1, omega1 = u_new, o_new
            t += dt
            accepted += 1
            min_dt = min(min_dt, dt)
            max_dt = max(max_dt, dt)
            d = self.diagnostics(u1, omega1)
            if not d.finite:
                raise RuntimeError("non-finite accepted E1 state")

            rel_energy_change = (d.energy - previous_energy) / max(previous_energy, 1.0e-300)
            max_positive_energy_change = max(
                max_positive_energy_change, max(0.0, rel_energy_change)
            )
            previous_energy = d.energy
            max_gamma = max(max_gamma, d.gamma_abs_max)
            max_axis = max(max_axis, d.axis_regular_defect)
            max_div = max(max_div, d.divergence_rel_linf)
            max_elliptic = max(max_elliptic, d.elliptic_residual_linf)
            min_scale_points = min(min_scale_points, d.min_gradient_scale_points)
            max_curvature_tail = max(max_curvature_tail, d.curvature_tail_max)
            max_boundary_shell = max(max_boundary_shell, d.boundary_shell_ratio)
            max_cfl_pre = max(max_cfl_pre, stage["cfl_pre"])
            max_cfl_stage1 = max(max_cfl_stage1, stage["cfl_stage1"])
            max_cfl_stage2 = max(max_cfl_stage2, stage["cfl_stage2"])
            max_cfl_post = max(max_cfl_post, stage["cfl_post"])
            max_viscous = max(max_viscous, stage["viscous_number"])

            if t + 1.0e-14 >= next_snapshot or t + 1.0e-14 >= self.cfg.T:
                snapshots.append({"t": float(t), **asdict(d)})
                next_snapshot += self.cfg.T / 4.0

        final = self.diagnostics(u1, omega1)
        gamma_overshoot = max(
            0.0, max_gamma / max(initial.gamma_abs_max, 1.0e-300) - 1.0
        )
        return {
            "classification": "NUMERICAL CANDIDATE INFRASTRUCTURE / E1 PROTOTYPE ONLY",
            "config": asdict(self.cfg),
            "seed_name": f"R3S{self.cfg.seed_index:02d}",
            "seed_params": cf.FROZEN_GEOMETRY_LATTICE[self.cfg.seed_index].to_dict(),
            "discretization": {
                "z_boundary": "strictly nonperiodic zero artificial Dirichlet",
                "r_outer_boundary": "zero artificial Dirichlet",
                "axis": "even scalar regular limit",
                "elliptic": "factorized second-order finite-difference -L5",
                "advection": "second-order centered nonconservative normalized equations",
                "time_integrator": "SSPRK3 with fail-closed stage CFL rejection",
                "free_space_boundary_validated": False,
            },
            "l5_row_absolute_sum_bound": self._row_abs_bound,
            "accepted_steps": accepted,
            "rejected_steps": rejected,
            "min_dt": float(min_dt),
            "max_dt": float(max_dt),
            "max_cfl_pre": max_cfl_pre,
            "max_cfl_stage1": max_cfl_stage1,
            "max_cfl_stage2": max_cfl_stage2,
            "max_cfl_post": max_cfl_post,
            "max_viscous_number": max_viscous,
            "max_positive_single_step_relative_energy_change": max_positive_energy_change,
            "gamma_max_principle_overshoot_relative": gamma_overshoot,
            "max_axis_regular_defect": max_axis,
            "max_divergence_rel_linf": max_div,
            "max_elliptic_residual_linf": max_elliptic,
            "min_gradient_scale_points": min_scale_points,
            "max_curvature_tail": max_curvature_tail,
            "max_boundary_shell_ratio": max_boundary_shell,
            "initial": asdict(initial),
            "final": asdict(final),
            "snapshots": snapshots,
            "nonclaim": (
                "This is a short truncated-box integrator audit. It is not a resolved R^3 trajectory, "
                "not a free-space truncation certificate, and not singularity or Clay evidence."
            ),
        }
