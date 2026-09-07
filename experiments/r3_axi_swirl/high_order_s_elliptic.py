"""High-order s=r^2 / nonperiodic-z scalar elliptic prototype for the R^3 swirl track.

This is the M0 method-development implementation.  It discretizes

    L5 f = 4 s f_ss + 8 f_s + f_zz,  s=r^2,

with deterministic local seven-node polynomial differentiation stencils.  The physical domain,
velocity reconstruction and volume measure remain three-dimensional.  This module is not a
validated free-space solver and does not evolve Navier--Stokes.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Callable

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla


Boundary = Callable[[np.ndarray | float, np.ndarray | float], np.ndarray | float]


@dataclass(frozen=True)
class HOSBox:
    Rmax: float
    Zmax: float
    nr: int
    nz: int
    stencil_width: int = 7

    def validate(self) -> None:
        if not (math.isfinite(self.Rmax) and self.Rmax > 0.0):
            raise ValueError("Rmax must be finite and positive")
        if not (math.isfinite(self.Zmax) and self.Zmax > 0.0):
            raise ValueError("Zmax must be finite and positive")
        if self.nr < 12 or self.nz < 16:
            raise ValueError("HOS box resolution too small")
        if self.stencil_width != 7:
            raise ValueError("M0 freezes stencil_width=7")
        if self.nr + 1 < self.stencil_width or self.nz + 1 < self.stencil_width:
            raise ValueError("not enough nodes for HOS stencil")


@dataclass
class HOSSystem:
    A: sp.csr_matrix
    radial_Ds_full: sp.csr_matrix
    radial_Dss_full: sp.csr_matrix
    axial_Dz_full: sp.csr_matrix
    axial_Dzz_full: sp.csr_matrix
    r_full: np.ndarray
    z_full: np.ndarray
    s_full: np.ndarray
    r: np.ndarray
    z: np.ndarray
    s: np.ndarray
    dr: float
    dz: float
    boundary_rhs: np.ndarray
    box: HOSBox


def _stencil_indices(total_nodes: int, center: int, width: int = 7) -> np.ndarray:
    if not (0 <= center < total_nodes):
        raise ValueError("stencil center out of range")
    if total_nodes < width:
        raise ValueError("not enough nodes for stencil")
    half = width // 2
    start = center - half
    start = max(0, min(start, total_nodes - width))
    return np.arange(start, start + width, dtype=int)


def polynomial_fd_weights(nodes: np.ndarray, x0: float, derivative_order: int) -> np.ndarray:
    """Return local polynomial finite-difference weights with scaled moment equations."""
    x = np.asarray(nodes, dtype=float)
    if x.ndim != 1 or x.size < derivative_order + 1:
        raise ValueError("invalid finite-difference node set")
    if np.unique(x).size != x.size:
        raise ValueError("finite-difference nodes must be distinct")
    dx = x - float(x0)
    scale = float(np.max(np.abs(dx)))
    if not (math.isfinite(scale) and scale > 0.0):
        raise ValueError("degenerate finite-difference stencil")
    t = dx / scale
    n = x.size
    moment = np.vstack([t**k for k in range(n)])
    rhs = np.zeros(n, dtype=float)
    rhs[derivative_order] = float(math.factorial(derivative_order))
    weights_t = np.linalg.solve(moment, rhs)
    weights = weights_t / scale**derivative_order
    residual = moment @ weights_t - rhs
    if not np.all(np.isfinite(weights)) or float(np.max(np.abs(residual))) > 5.0e-10:
        raise RuntimeError("unstable local polynomial differentiation weights")
    return weights


def _derivative_matrix(full_nodes: np.ndarray, target_indices: np.ndarray, order: int) -> sp.csr_matrix:
    rows: list[int] = []
    cols: list[int] = []
    vals: list[float] = []
    total = full_nodes.size
    for row, center in enumerate(np.asarray(target_indices, dtype=int)):
        idx = _stencil_indices(total, int(center), 7)
        w = polynomial_fd_weights(full_nodes[idx], float(full_nodes[center]), order)
        rows.extend([row] * idx.size)
        cols.extend(idx.tolist())
        vals.extend(w.tolist())
    return sp.csr_matrix((vals, (rows, cols)), shape=(target_indices.size, total))


def build_minus_l5(box: HOSBox, boundary: Boundary) -> HOSSystem:
    """Build the M0 high-order approximation to -L5 with artificial Dirichlet boundaries."""
    box.validate()
    r_full = np.linspace(0.0, box.Rmax, box.nr + 1)
    z_full = np.linspace(-box.Zmax, box.Zmax, box.nz + 1)
    s_full = r_full * r_full
    r = r_full[:-1]
    s = s_full[:-1]
    z = z_full[1:-1]
    dr = box.Rmax / box.nr
    dz = 2.0 * box.Zmax / box.nz
    nzu = box.nz - 1

    ri = np.arange(box.nr, dtype=int)
    zj = np.arange(1, box.nz, dtype=int)
    Ds = _derivative_matrix(s_full, ri, 1)
    Dss = _derivative_matrix(s_full, ri, 2)
    Dz = _derivative_matrix(z_full, zj, 1)
    Dzz = _derivative_matrix(z_full, zj, 2)

    radial_full = -(sp.diags(4.0 * s) @ Dss + 8.0 * Ds).tocsr()
    axial_full = (-Dzz).tocsr()
    radial_unknown = radial_full[:, : box.nr]
    axial_unknown = axial_full[:, 1:box.nz]

    A = (
        sp.kron(radial_unknown, sp.eye(nzu, format="csr"), format="csr")
        + sp.kron(sp.eye(box.nr, format="csr"), axial_unknown, format="csr")
    ).tocsr()

    radial_outer_coeff = np.asarray(radial_full[:, box.nr].todense()).ravel()
    br = np.asarray(boundary(box.Rmax, z), dtype=float)
    if br.ndim == 0:
        br = np.full_like(z, float(br))
    br = np.broadcast_to(br, z.shape).astype(float)
    contribution = radial_outer_coeff[:, None] * br[None, :]

    zlo_coeff = np.asarray(axial_full[:, 0].todense()).ravel()
    zhi_coeff = np.asarray(axial_full[:, box.nz].todense()).ravel()
    blo = np.asarray(boundary(r, -box.Zmax), dtype=float)
    bhi = np.asarray(boundary(r, box.Zmax), dtype=float)
    if blo.ndim == 0:
        blo = np.full_like(r, float(blo))
    if bhi.ndim == 0:
        bhi = np.full_like(r, float(bhi))
    blo = np.broadcast_to(blo, r.shape).astype(float)
    bhi = np.broadcast_to(bhi, r.shape).astype(float)
    contribution += blo[:, None] * zlo_coeff[None, :]
    contribution += bhi[:, None] * zhi_coeff[None, :]
    boundary_rhs = -contribution

    if not np.all(np.isfinite(boundary_rhs)):
        raise RuntimeError("non-finite HOS boundary rhs")

    return HOSSystem(
        A=A,
        radial_Ds_full=Ds,
        radial_Dss_full=Dss,
        axial_Dz_full=Dz,
        axial_Dzz_full=Dzz,
        r_full=r_full,
        z_full=z_full,
        s_full=s_full,
        r=r,
        z=z,
        s=s,
        dr=dr,
        dz=dz,
        boundary_rhs=boundary_rhs,
        box=box,
    )


def solve(system: HOSSystem, omega: np.ndarray) -> np.ndarray:
    arr = np.asarray(omega, dtype=float)
    if arr.shape != system.boundary_rhs.shape:
        raise ValueError(f"omega shape {arr.shape} != {system.boundary_rhs.shape}")
    rhs = arr + system.boundary_rhs
    if not np.all(np.isfinite(rhs)):
        raise ValueError("non-finite HOS elliptic rhs")
    psi = spla.spsolve(system.A, rhs.ravel()).reshape(arr.shape)
    if not np.all(np.isfinite(psi)):
        raise RuntimeError("non-finite HOS elliptic solution")
    return np.asarray(psi, dtype=float)


def residual(system: HOSSystem, psi: np.ndarray, omega: np.ndarray) -> np.ndarray:
    lhs = (system.A @ np.asarray(psi, dtype=float).ravel()).reshape(system.boundary_rhs.shape)
    return lhs - system.boundary_rhs - np.asarray(omega, dtype=float)


def full_array(system: HOSSystem, interior: np.ndarray, boundary: Boundary) -> np.ndarray:
    arr = np.asarray(interior, dtype=float)
    if arr.shape != system.boundary_rhs.shape:
        raise ValueError("interior shape mismatch")
    full = np.empty((system.box.nr + 1, system.box.nz + 1), dtype=float)
    full[:-1, 1:-1] = arr
    full[-1, :] = np.asarray(boundary(system.box.Rmax, system.z_full), dtype=float)
    full[:-1, 0] = np.asarray(boundary(system.r, -system.box.Zmax), dtype=float)
    full[:-1, -1] = np.asarray(boundary(system.r, system.box.Zmax), dtype=float)
    if not np.all(np.isfinite(full)):
        raise RuntimeError("non-finite augmented HOS array")
    return full


def differentiate_s_z(
    system: HOSSystem, interior: np.ndarray, boundary: Boundary
) -> tuple[np.ndarray, np.ndarray]:
    full = full_array(system, interior, boundary)
    ds = np.asarray(system.radial_Ds_full @ full[:, 1:-1], dtype=float)
    dz = np.asarray((system.axial_Dz_full @ full[:-1, :].T).T, dtype=float)
    if not np.all(np.isfinite(ds)) or not np.all(np.isfinite(dz)):
        raise RuntimeError("non-finite HOS first derivative")
    return ds, dz


def physical_grad_r_z(
    system: HOSSystem, interior: np.ndarray, boundary: Boundary
) -> tuple[np.ndarray, np.ndarray]:
    ds, dz = differentiate_s_z(system, interior, boundary)
    return 2.0 * system.r[:, None] * ds, dz


def physical_weighted_l2(system: HOSSystem, f: np.ndarray) -> float:
    arr = np.asarray(f, dtype=float)
    if arr.shape != system.boundary_rhs.shape:
        raise ValueError("weighted-L2 shape mismatch")
    R = system.r[:, None]
    return math.sqrt(max(0.0, float(np.sum(2.0 * math.pi * R * arr**2) * system.dr * system.dz)))
