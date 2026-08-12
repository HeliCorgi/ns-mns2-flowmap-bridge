#!/usr/bin/env python3
"""
MNS-2 v2.0 prototype: path-integrated tangent bridge.

For an unforced flow map S_t with S_t(0)=0 and C^1 dependence on initial data
along the segment {lambda*u0 : 0<=lambda<=1},

    S_t(u0) = int_0^1 DS_t(lambda*u0)[u0] d lambda.

This module provides a generic Gauss-Legendre path integrator and a manufactured
Riccati positive control. It is a bridge identity, not a Navier-Stokes solver.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from typing import Callable, Any
import numpy as np

Array = np.ndarray


def gauss_legendre_unit(n: int):
    if n < 1:
        raise ValueError("n must be >= 1")
    x, w = np.polynomial.legendre.leggauss(n)
    lam = 0.5 * (x + 1.0)
    wt = 0.5 * w
    return lam, wt


def path_integrated_tangent(u0: Array, jvp_at_scaled_initial_data: Callable[[float, Array], Array], nquad: int = 16) -> Array:
    u0 = np.asarray(u0, dtype=float)
    lam, wt = gauss_legendre_unit(nquad)
    acc = np.zeros_like(u0, dtype=float)
    for a, b in zip(lam, wt):
        acc += b * np.asarray(jvp_at_scaled_initial_data(float(a), u0), dtype=float)
    return acc


@dataclass
class RiccatiFlow:
    t: float

    def S(self, y0: Array) -> Array:
        y0 = np.asarray(y0, dtype=float)
        den = 1.0 - self.t * y0
        if np.any(den <= 0):
            raise ValueError("Riccati solution crosses blow-up before requested time")
        return y0 / den

    def jvp_scaled(self, lam: float, direction: Array) -> Array:
        d = np.asarray(direction, dtype=float)
        den = 1.0 - self.t * lam * d
        if np.any(den <= 0):
            raise ValueError("path crosses Riccati blow-up")
        return d / den**2


def riccati_regression(t: float = 0.7, y0: float = 0.8, nquad: int = 16) -> dict[str, Any]:
    flow = RiccatiFlow(t=t)
    u0 = np.array([y0], dtype=float)
    exact = flow.S(u0)
    recon = path_integrated_tangent(u0, flow.jvp_scaled, nquad=nquad)
    abs_err = float(np.linalg.norm(recon - exact))
    rel_err = abs_err / max(float(np.linalg.norm(exact)), 1e-300)
    return {"status": "PASS" if rel_err < 1e-12 else "FAIL", "model": "y'=y^2", "t": t, "y0": y0, "nquad": nquad, "exact": exact.tolist(), "reconstructed": recon.tolist(), "abs_error": abs_err, "rel_error": rel_err}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--t", type=float, default=0.7)
    ap.add_argument("--y0", type=float, default=0.8)
    ap.add_argument("--nquad", type=int, default=16)
    args = ap.parse_args()
    out = riccati_regression(args.t, args.y0, args.nquad)
    print(json.dumps(out, indent=2))
    raise SystemExit(0 if out["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
