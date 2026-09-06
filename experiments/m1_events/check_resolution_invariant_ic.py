"""Small deterministic self-check for resolution_invariant_ic.py.

This is not a PDE validation. It checks the construction property needed before a convergence run:
shared physical grid points sample the same continuum field, the historical RMS normalization is
resolution independent, and the Fourier coefficients are divergence-free to roundoff.
"""
from __future__ import annotations

import numpy as np

import events as ev
import resolution_invariant_ic as ric


def main() -> None:
    fields = {}
    coeff_norm = []
    for N in (24, 48):
        g = ev.Grid(N)
        u = ric.random_band_field(g, 1, 2, seed=11, amp=1.0)
        rms = float(np.sqrt(np.mean(np.sum(u * u, axis=0)) / 3.0))
        if abs(rms - 1.0) > 1.0e-12:
            raise AssertionError((N, "rms", rms))
        uh = ric.ic_e4_continuum(g)
        divh = sum(1j * g.K[i] * uh[i] for i in range(3))
        divmax = float(np.max(np.abs(divh)))
        if divmax > 1.0e-12:
            raise AssertionError((N, "divmax", divmax))
        fields[N] = u
        coeff_norm.append(float(np.sum(np.abs(uh) ** 2)))

    shared = float(np.max(np.abs(fields[24] - fields[48][:, ::2, ::2, ::2])))
    if shared > 1.0e-12:
        raise AssertionError(("shared-grid mismatch", shared))
    if abs(coeff_norm[0] - coeff_norm[1]) > 1.0e-12:
        raise AssertionError(("coefficient norm mismatch", coeff_norm))
    print(f"PASS shared={shared:.3e} coeff_norm_delta={abs(coeff_norm[0]-coeff_norm[1]):.3e}")


if __name__ == "__main__":
    main()
