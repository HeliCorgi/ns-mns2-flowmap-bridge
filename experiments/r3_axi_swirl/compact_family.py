"""Explicit compact smooth axisymmetric-with-swirl seed family for the R^3 track.

This module constructs continuum formulas in s=r^2 and z.  It does not evolve Navier--Stokes.
The formulas are chosen so Cartesian smoothness at r=0 is built in, and omega1 is defined exactly
from -L5 psi1.

Claim scope: candidate-data infrastructure only; not a blow-up or Clay result.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import math
from typing import Iterable

import numpy as np


@dataclass(frozen=True)
class SeedParams:
    s0: float
    ws: float
    wz: float
    zu: float
    Au: float = 1.0
    Apsi: float = 0.10

    def validate(self) -> None:
        vals = (self.s0, self.ws, self.wz, self.zu, self.Au, self.Apsi)
        if not all(math.isfinite(float(x)) for x in vals):
            raise ValueError(f"non-finite seed parameter: {self}")
        if self.s0 < 0.0:
            raise ValueError("s0 must be nonnegative")
        if self.ws <= 0.0 or self.wz <= 0.0:
            raise ValueError("ws and wz must be positive")
        if self.Au == 0.0:
            raise ValueError("Au must be nonzero for a swirl seed")

    def to_dict(self) -> dict:
        return asdict(self)


FROZEN_GEOMETRY_LATTICE = tuple(
    SeedParams(s0=s0, ws=0.05, wz=wz, zu=zu, Au=1.0, Apsi=0.10)
    for s0 in (0.04, 0.09, 0.16)
    for wz in (0.18, 0.28)
    for zu in (0.00, 0.08)
)


def bump(q):
    """Normalized C-infinity bump, B(0)=1, support |q|<1."""
    q = np.asarray(q, dtype=float)
    out = np.zeros_like(q)
    m = np.abs(q) < 1.0
    qm = q[m]
    out[m] = np.exp(1.0 - 1.0 / (1.0 - qm * qm))
    return out


def bump_d1(q):
    q = np.asarray(q, dtype=float)
    out = np.zeros_like(q)
    m = np.abs(q) < 1.0
    qm = q[m]
    d = 1.0 - qm * qm
    b = np.exp(1.0 - 1.0 / d)
    out[m] = b * (-2.0 * qm / d**2)
    return out


def bump_d2(q):
    q = np.asarray(q, dtype=float)
    out = np.zeros_like(q)
    m = np.abs(q) < 1.0
    qm = q[m]
    d = 1.0 - qm * qm
    b = np.exp(1.0 - 1.0 / d)
    lp = -2.0 * qm / d**2
    lpp = -2.0 / d**2 - 8.0 * qm * qm / d**3
    out[m] = b * (lp * lp + lpp)
    return out


def odd_bump(q):
    q = np.asarray(q, dtype=float)
    return q * bump(q)


def odd_bump_d1(q):
    q = np.asarray(q, dtype=float)
    return bump(q) + q * bump_d1(q)


def odd_bump_d2(q):
    q = np.asarray(q, dtype=float)
    return 2.0 * bump_d1(q) + q * bump_d2(q)


def _coords(r, z):
    r = np.asarray(r, dtype=float)
    z = np.asarray(z, dtype=float)
    return np.broadcast_arrays(r, z)


def scalar_fields(r, z, p: SeedParams) -> dict[str, np.ndarray]:
    """Return u1, psi1, omega1 and derivatives needed for exact reconstruction."""
    p.validate()
    r, z = _coords(r, z)
    s = r * r
    qs = (s - p.s0) / p.ws
    qu = (z - p.zu) / p.wz
    qp = z / p.wz

    bs = bump(qs)
    bs1 = bump_d1(qs)
    bs2 = bump_d2(qs)
    bu = bump(qu)
    bu1 = bump_d1(qu)
    gp = odd_bump(qp)
    gp1 = odd_bump_d1(qp)
    gp2 = odd_bump_d2(qp)

    u1 = p.Au * bs * bu
    u1_s = p.Au * (bs1 / p.ws) * bu
    u1_z = p.Au * bs * (bu1 / p.wz)

    psi1 = p.Apsi * bs * gp
    psi1_s = p.Apsi * (bs1 / p.ws) * gp
    psi1_ss = p.Apsi * (bs2 / p.ws**2) * gp
    psi1_z = p.Apsi * bs * (gp1 / p.wz)
    psi1_zz = p.Apsi * bs * (gp2 / p.wz**2)
    psi1_sz = p.Apsi * (bs1 / p.ws) * (gp1 / p.wz)

    l5_psi1 = 4.0 * s * psi1_ss + 8.0 * psi1_s + psi1_zz
    omega1 = -l5_psi1

    return {
        "s": s,
        "u1": u1,
        "u1_s": u1_s,
        "u1_z": u1_z,
        "psi1": psi1,
        "psi1_s": psi1_s,
        "psi1_ss": psi1_ss,
        "psi1_z": psi1_z,
        "psi1_zz": psi1_zz,
        "psi1_sz": psi1_sz,
        "omega1": omega1,
    }


def cylindrical_velocity(r, z, p: SeedParams) -> dict[str, np.ndarray]:
    r, z = _coords(r, z)
    f = scalar_fields(r, z, p)
    s = f["s"]
    ur = -r * f["psi1_z"]
    uz = 2.0 * f["psi1"] + 2.0 * s * f["psi1_s"]
    utheta = r * f["u1"]
    return {**f, "ur": ur, "utheta": utheta, "uz": uz}


def cylindrical_vorticity(r, z, p: SeedParams) -> dict[str, np.ndarray]:
    r, z = _coords(r, z)
    f = scalar_fields(r, z, p)
    s = f["s"]
    omega_r = -r * f["u1_z"]
    omega_theta = r * f["omega1"]
    omega_z = 2.0 * f["u1"] + 2.0 * s * f["u1_s"]
    return {**f, "omega_r": omega_r, "omega_theta": omega_theta, "omega_z": omega_z}


def cartesian_velocity(x, y, z, p: SeedParams) -> dict[str, np.ndarray]:
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    z = np.asarray(z, dtype=float)
    x, y, z = np.broadcast_arrays(x, y, z)
    r = np.sqrt(x * x + y * y)
    f = scalar_fields(r, z, p)
    s = f["s"]
    ux = -x * f["psi1_z"] - y * f["u1"]
    uy = -y * f["psi1_z"] + x * f["u1"]
    uz = 2.0 * f["psi1"] + 2.0 * s * f["psi1_s"]
    return {**f, "ux": ux, "uy": uy, "uz": uz}


def divergence_terms(r, z, p: SeedParams) -> dict[str, np.ndarray]:
    """Analytic cylindrical divergence terms for the reconstructed velocity.

    The sum is identically zero:
      d_r ur + ur/r + d_z uz
      = (-psi_z - 2s psi_sz) + (-psi_z) + (2psi_z + 2s psi_sz).
    At r=0 the displayed decomposition is the smooth limiting identity.
    """
    f = scalar_fields(r, z, p)
    s = f["s"]
    d_r_ur = -f["psi1_z"] - 2.0 * s * f["psi1_sz"]
    ur_over_r = -f["psi1_z"]
    d_z_uz = 2.0 * f["psi1_z"] + 2.0 * s * f["psi1_sz"]
    return {
        "d_r_ur": d_r_ur,
        "ur_over_r": ur_over_r,
        "d_z_uz": d_z_uz,
        "div": d_r_ur + ur_over_r + d_z_uz,
    }


def support_bounds(p: SeedParams) -> dict[str, float]:
    p.validate()
    s_hi = max(0.0, p.s0 + p.ws)
    # psi support is centered at z=0; u1 support is centered at zu.
    z_lo = min(-p.wz, p.zu - p.wz)
    z_hi = max(p.wz, p.zu + p.wz)
    return {
        "r_max": math.sqrt(s_hi),
        "z_min": z_lo,
        "z_max": z_hi,
        "s_min_raw": p.s0 - p.ws,
        "s_max": p.s0 + p.ws,
    }


def physical_energy(p: SeedParams, nr: int = 801, nz: int = 1201) -> float:
    """Deterministic quadrature of 1/2 int_R3 |u|^2 dx for audit metadata."""
    b = support_bounds(p)
    rmax = b["r_max"] * 1.05 + 1e-12
    zpad = 0.05 * max(1.0, b["z_max"] - b["z_min"])
    zmin, zmax = b["z_min"] - zpad, b["z_max"] + zpad
    r = np.linspace(0.0, rmax, nr)
    z = np.linspace(zmin, zmax, nz)
    R, Z = np.meshgrid(r, z, indexing="ij")
    v = cylindrical_velocity(R, Z, p)
    speed2 = v["ur"]**2 + v["utheta"]**2 + v["uz"]**2
    integrand = 0.5 * 2.0 * math.pi * R * speed2
    return float(np.trapezoid(np.trapezoid(integrand, z, axis=1), r, axis=0))


def seed_manifest(params: Iterable[SeedParams] = FROZEN_GEOMETRY_LATTICE) -> list[dict]:
    out = []
    for i, p in enumerate(params):
        p.validate()
        rec = {
            "name": f"R3S{i:02d}",
            "params": p.to_dict(),
            "support": support_bounds(p),
        }
        out.append(rec)
    return out
