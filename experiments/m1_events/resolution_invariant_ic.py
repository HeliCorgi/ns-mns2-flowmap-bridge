"""Resolution-invariant low-band initial data for M-1 convergence studies.

The legacy E3/E4 helpers draw random numbers into FFT arrays whose shape changes with N.
That is fine for one-grid diagnostics but not for a spatial-convergence sequence: changing N
changes the continuum datum. This module instead draws coefficients on a canonical finite
integer-wavevector set, then samples the same trigonometric polynomial on every grid.

EVIDENCE-GRADE / DIAGNOSTIC ONLY. These periodic T^3 data are not R^3/Clay candidates.
"""
from __future__ import annotations

import numpy as np


def canonical_modes(kmin: int, kmax: int) -> list[tuple[int, int, int]]:
    """One representative of each pair {k,-k}, sorted lexicographically."""
    modes: list[tuple[int, int, int]] = []
    for kx in range(-kmax, kmax + 1):
        for ky in range(-kmax, kmax + 1):
            for kz in range(-kmax, kmax + 1):
                k = (kx, ky, kz)
                k2 = kx * kx + ky * ky + kz * kz
                if k2 == 0:
                    continue
                kmag = np.sqrt(float(k2))
                if not (kmin <= kmag <= kmax):
                    continue
                first = next(c for c in k if c != 0)
                if first > 0:
                    modes.append(k)
    modes.sort()
    return modes


def _project_perp(v: np.ndarray, k: np.ndarray) -> np.ndarray:
    return v - k * (float(np.dot(k, v)) / float(np.dot(k, k)))


def random_band_field(g, kmin: int, kmax: int, seed: int, *, anisotropy: bool = False,
                      amp: float = 1.0) -> np.ndarray:
    """Sample one deterministic divergence-free trigonometric polynomial on grid ``g``.

    ``amp`` uses the historical M-1 convention
    ``sqrt(mean_x |u|^2 / 3) = amp``.
    """
    rng = np.random.default_rng(seed)
    modes = canonical_modes(kmin, kmax)
    coeffs: list[tuple[tuple[int, int, int], np.ndarray, np.ndarray]] = []
    mean_sq = 0.0
    for kt in modes:
        k = np.asarray(kt, dtype=float)
        a = _project_perp(rng.standard_normal(3), k)
        b = _project_perp(rng.standard_normal(3), k)
        if anisotropy:
            weight = 1.0 + 2.0 * (k[2] * k[2]) / float(np.dot(k, k))
            a *= weight
            b *= weight
        coeffs.append((kt, a, b))
        mean_sq += 0.5 * (float(np.dot(a, a)) + float(np.dot(b, b)))
    if mean_sq <= 0.0:
        raise ValueError("empty/degenerate random band")
    scale = amp / np.sqrt(mean_sq / 3.0)

    u = np.zeros((3, g.N, g.N, g.N), dtype=float)
    X, Y, Z = g.X
    for (kx, ky, kz), a, b in coeffs:
        phase = kx * X + ky * Y + kz * Z
        cph = np.cos(phase)
        sph = np.sin(phase)
        for j in range(3):
            u[j] += scale * (a[j] * cph + b[j] * sph)
    return u


def ic_random_band_continuum(g, kmin: int, kmax: int, seed: int, *, anisotropy: bool = False,
                              amp: float = 1.0):
    u = random_band_field(g, kmin, kmax, seed, anisotropy=anisotropy, amp=amp)
    uh = np.array([g.rfft(u[i]) for i in range(3)])
    return g.project(uh) * g.DEALIAS


def ic_r4_continuum(g):
    """Resolution-invariant analogue of the historical E3 shear+10% low-band datum."""
    X, Y, Z = g.X
    u = np.zeros((3, g.N, g.N, g.N), dtype=float)
    u[2] += np.sin(X)
    u[0] += 0.8 * np.sin(2.0 * Y + Z)
    u += 0.1 * random_band_field(g, 1, 4, seed=3, amp=1.0)
    urms = np.sqrt(np.mean(np.sum(u * u, axis=0)) / 3.0)
    u /= urms
    uh = np.array([g.rfft(u[i]) for i in range(3)])
    return g.project(uh) * g.DEALIAS


def ic_e4_continuum(g):
    return ic_random_band_continuum(g, 1, 2, seed=11, amp=1.0)
