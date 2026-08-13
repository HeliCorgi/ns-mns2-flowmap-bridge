#!/usr/bin/env python3
"""Generate the smooth synthetic two-component v2.2 regression seed.

This is deliberately source-controlled as an analytic generator rather than as an NPZ
binary. The prior checked-in NPZ container was discovered by CI to be corrupted.

Grid and fields
---------------

    r_i = (i + 1/2) / 32
    z_j = (j + 1/2) / 64

    Gamma(r,z)
      = 120 r^2 (1-r^2)^18 sin(2 pi z)
        / (1 + 12.5 sin(pi z)^2)

    omega1(r,z)
      = 0.088 (1-r^2)^6
        [cos(2 pi z) + (1/11) cos(6 pi z)].

The state is synthetic regression data. It is NOT Hou late-state evidence.
"""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import numpy as np


def generate_seed():
    r = (np.arange(32, dtype=np.float64) + 0.5) / 32.0
    z = (np.arange(64, dtype=np.float64) + 0.5) / 64.0
    R, Z = np.meshgrid(r, z, indexing="ij")

    Gamma = (
        120.0
        * R**2
        * (1.0 - R**2) ** 18
        * np.sin(2.0 * np.pi * Z)
        / (1.0 + 12.5 * np.sin(np.pi * Z) ** 2)
    )
    omega1 = (
        0.088
        * (1.0 - R**2) ** 6
        * (np.cos(2.0 * np.pi * Z) + (1.0 / 11.0) * np.cos(6.0 * np.pi * Z))
    )
    return {"r": r, "z": z, "Gamma": Gamma, "omega1": omega1}


def canonical_content_sha256(arrays) -> str:
    """Hash numerical content independent of the NPZ/ZIP container bytes."""
    h = hashlib.sha256()
    for key in sorted(arrays):
        a = np.ascontiguousarray(arrays[key])
        h.update(key.encode("utf-8") + b"\0")
        h.update(a.dtype.str.encode("ascii") + b"\0")
        h.update(str(a.shape).encode("ascii") + b"\0")
        h.update(a.tobytes(order="C"))
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out", type=Path)
    args = ap.parse_args()

    arrays = generate_seed()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(args.out, **arrays)
    print(canonical_content_sha256(arrays))


if __name__ == "__main__":
    main()
