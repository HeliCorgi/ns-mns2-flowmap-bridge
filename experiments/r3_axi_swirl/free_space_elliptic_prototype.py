"""Nonperiodic node-centered prototype for -L5 psi = omega on a truncated R^3-axisymmetric box.

This is an E0 development solver, not a validated free-space solver. It exists to test the
manufactured compact seeds and independent free-space tail references before nonlinear evolution.

The radial operator is L5 = d_rr + 3/r d_r + d_zz. At r=0 we use the regular limit
L5 f(0,z) = 4 f_rr(0,z) + f_zz(0,z), with the even-axis second derivative discretized by a
symmetric ghost value. z is strictly nonperiodic.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Callable

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.integrate import quad
from scipy.special import gamma, gammainc


Boundary = Callable[[np.ndarray | float, np.ndarray | float], np.ndarray | float]
Source = Callable[[np.ndarray, np.ndarray], np.ndarray]


@dataclass(frozen=True)
class Box:
    Rmax: float
    Zmax: float
    nr: int   # number of radial intervals; unknown nodes i=0,...,nr-1
    nz: int   # number of axial intervals; unknown nodes j=1,...,nz-1

    def validate(self) -> None:
        if not (self.Rmax > 0.0 and self.Zmax > 0.0):
            raise ValueError("Rmax and Zmax must be positive")
        if self.nr < 4 or self.nz < 8:
            raise ValueError("box resolution too small")


@dataclass
class EllipticSystem:
    A: sp.csr_matrix
    r: np.ndarray
    z: np.ndarray
    boundary_rhs: np.ndarray
    dr: float
    dz: float
    box: Box


def build_minus_l5(box: Box, boundary: Boundary) -> EllipticSystem:
    """Build A approximating -L5 on nonperiodic z with Dirichlet outer boundaries.

    Unknowns include the axis r=0, exclude r=Rmax, and exclude z=+-Zmax.
    Boundary values are supplied only on the artificial outer faces. No radial wall/no-slip
    Navier--Stokes boundary condition is implied by this elliptic Dirichlet test.
    """
    box.validate()
    nr, nz = box.nr, box.nz
    dr = box.Rmax / nr
    dz = 2.0 * box.Zmax / nz
    r = np.arange(nr, dtype=float) * dr
    z = -box.Zmax + np.arange(1, nz, dtype=float) * dz
    nzu = nz - 1

    rows: list[int] = []
    cols: list[int] = []
    vals: list[float] = []
    brhs = np.zeros((nr, nzu), dtype=float)

    def idx(i: int, jj: int) -> int:
        return i * nzu + jj

    for i, ri in enumerate(r):
        for jj, zj in enumerate(z):
            row = idx(i, jj)
            center = 0.0

            # - (d_rr + 3/r d_r). At the axis, 4 f_rr with an even ghost gives
            # 8 (f_1-f_0)/dr^2 for +L5, hence +8/-8 in -L5.
            if i == 0:
                center += 8.0 / dr**2
                rows.append(row); cols.append(idx(1, jj)); vals.append(-8.0 / dr**2)
            else:
                cm = 1.0 / dr**2 - 3.0 / (2.0 * ri * dr)
                cp = 1.0 / dr**2 + 3.0 / (2.0 * ri * dr)
                center += 2.0 / dr**2
                rows.append(row); cols.append(idx(i - 1, jj)); vals.append(-cm)
                if i < nr - 1:
                    rows.append(row); cols.append(idx(i + 1, jj)); vals.append(-cp)
                else:
                    brhs[i, jj] += cp * float(boundary(box.Rmax, zj))

            # -d_zz with nonperiodic Dirichlet values at z=+-Zmax.
            center += 2.0 / dz**2
            if jj > 0:
                rows.append(row); cols.append(idx(i, jj - 1)); vals.append(-1.0 / dz**2)
            else:
                brhs[i, jj] += float(boundary(ri, -box.Zmax)) / dz**2
            if jj < nzu - 1:
                rows.append(row); cols.append(idx(i, jj + 1)); vals.append(-1.0 / dz**2)
            else:
                brhs[i, jj] += float(boundary(ri, box.Zmax)) / dz**2

            rows.append(row); cols.append(row); vals.append(center)

    A = sp.csr_matrix((vals, (rows, cols)), shape=(nr * nzu, nr * nzu))
    return EllipticSystem(A=A, r=r, z=z, boundary_rhs=brhs, dr=dr, dz=dz, box=box)


def solve(system: EllipticSystem, omega: np.ndarray) -> np.ndarray:
    if omega.shape != system.boundary_rhs.shape:
        raise ValueError(f"omega shape {omega.shape} != {system.boundary_rhs.shape}")
    rhs = np.asarray(omega, dtype=float) + system.boundary_rhs
    if not np.all(np.isfinite(rhs)):
        raise ValueError("non-finite elliptic rhs")
    psi = spla.spsolve(system.A, rhs.ravel()).reshape(rhs.shape)
    if not np.all(np.isfinite(psi)):
        raise RuntimeError("non-finite elliptic solution")
    return psi


def residual(system: EllipticSystem, psi: np.ndarray, omega: np.ndarray) -> np.ndarray:
    lhs = (system.A @ np.asarray(psi, dtype=float).ravel()).reshape(psi.shape)
    return lhs - system.boundary_rhs - np.asarray(omega, dtype=float)


def physical_weighted_l2(system: EllipticSystem, f: np.ndarray) -> float:
    """Axisymmetric 3D-weighted L2 diagnostic using 2*pi*r dr dz.

    This is a physical-axisymmetric diagnostic, not the R^5 measure associated with the scalar
    L5 analogy.
    """
    R = system.r[:, None]
    return math.sqrt(float(np.sum(2.0 * math.pi * R * np.asarray(f)**2) * system.dr * system.dz))


def gaussian5_source(r, z, a: float = 0.25):
    """Smooth 5D-radial source exp(-(r^2+z^2)/a^2) for a free-space tail stress test."""
    r = np.asarray(r, dtype=float)
    z = np.asarray(z, dtype=float)
    return np.exp(-(r * r + z * z) / a**2)


def _gaussian_radial_mass(rho, a: float):
    rho = np.asarray(rho, dtype=float)
    x = (rho / a) ** 2
    return 0.5 * a**5 * gamma(2.5) * gammainc(2.5, x)


def gaussian5_free_space_psi(r, z, a: float = 0.25):
    """Exact radial free-space solution of -Delta_5 psi = exp(-rho^2/a^2).

    For rho=sqrt(r^2+z^2), radial integration gives
      psi(rho) = (1/3) [rho^-3 int_0^rho s^4 f(s) ds + int_rho^inf s f(s) ds].
    The integrals are evaluated through the incomplete gamma function. The solution decays as
    rho^-3 and therefore explicitly tests a nonzero whole-space elliptic tail.
    """
    r = np.asarray(r, dtype=float)
    z = np.asarray(z, dtype=float)
    r, z = np.broadcast_arrays(r, z)
    rho = np.sqrt(r * r + z * z)
    x = (rho / a) ** 2
    i1 = _gaussian_radial_mass(rho, a)
    i2 = 0.5 * a**2 * np.exp(-x)
    first = np.zeros_like(rho)
    m = rho > 1.0e-14
    first[m] = i1[m] / rho[m] ** 3
    return (first + i2) / 3.0


def gaussian5_free_space_grad(r, z, a: float = 0.25):
    """Exact first derivatives of the radial Gaussian free-space solution."""
    r = np.asarray(r, dtype=float)
    z = np.asarray(z, dtype=float)
    r, z = np.broadcast_arrays(r, z)
    rho = np.sqrt(r * r + z * z)
    mass = _gaussian_radial_mass(rho, a)
    radial_derivative = np.zeros_like(rho)
    m = rho > 1.0e-14
    # For -Delta_5 psi=f: psi'(rho) = -rho^-4 int_0^rho s^4 f(s) ds.
    radial_derivative[m] = -mass[m] / rho[m] ** 4
    d_r = np.zeros_like(rho)
    d_z = np.zeros_like(rho)
    d_r[m] = radial_derivative[m] * r[m] / rho[m]
    d_z[m] = radial_derivative[m] * z[m] / rho[m]
    return d_r, d_z


def gaussian5_green_axis_quadrature(z: float, a: float = 0.25, cutoff: float = 1.5) -> float:
    """Independent 5D Green-integral reference at physical-axis points r=0.

    With G5(X)=1/(8*pi^2 |X|^3), integrating the four transverse angular variables gives

      psi(0,z) = (1/4) int_R int_0^inf
                 a_r^3 exp(-(a_r^2+zeta^2)/a^2)
                 / (a_r^2+(z-zeta)^2)^(3/2) da_r dzeta.

    This routine evaluates the two integrals adaptively and independently of the incomplete-gamma
    radial closed form. The finite cutoff is chosen many Gaussian widths away; it is a reference
    cross-check, not a generic tail-enclosure engine.
    """
    if not (a > 0.0 and cutoff > 0.0 and math.isfinite(z)):
        raise ValueError("invalid Gaussian Green-reference parameters")

    def outer(zeta: float) -> float:
        ez = math.exp(-(zeta * zeta) / a**2)
        d = abs(z - zeta)

        def inner(ar: float) -> float:
            if ar == 0.0 and d == 0.0:
                # The limiting integrand is finite: ar^3 / ar^3 -> 1.
                return 1.0
            return ar**3 * math.exp(-(ar * ar) / a**2) / (ar * ar + d * d) ** 1.5

        val, _ = quad(inner, 0.0, cutoff, epsabs=1e-12, epsrel=1e-11, limit=200)
        return 0.25 * ez * val

    if -cutoff < z < cutoff:
        left, _ = quad(outer, -cutoff, z, epsabs=1e-11, epsrel=1e-10, limit=200)
        right, _ = quad(outer, z, cutoff, epsabs=1e-11, epsrel=1e-10, limit=200)
        return float(left + right)
    val, _ = quad(outer, -cutoff, cutoff, epsabs=1e-11, epsrel=1e-10, limit=200)
    return float(val)
