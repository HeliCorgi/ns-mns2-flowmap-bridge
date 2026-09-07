"""Low-axial-frequency manufactured E0 stress test for the nonperiodic -L5 prototype."""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

import free_space_elliptic_prototype as ep

HERE = Path(__file__).resolve().parent


def exact_psi(r, z, ar: float = 0.20, az: float = 0.80):
    r = np.asarray(r, dtype=float)
    z = np.asarray(z, dtype=float)
    return np.exp(-(r * r) / ar**2 - (z * z) / az**2)


def exact_omega(r, z, ar: float = 0.20, az: float = 0.80):
    r = np.asarray(r, dtype=float)
    z = np.asarray(z, dtype=float)
    p = exact_psi(r, z, ar, az)
    return (8.0 / ar**2 + 2.0 / az**2 - 4.0 * r * r / ar**4 - 4.0 * z * z / az**4) * p


def exact_grad(r, z, ar: float = 0.20, az: float = 0.80):
    p = exact_psi(r, z, ar, az)
    return -2.0 * np.asarray(r) * p / ar**2, -2.0 * np.asarray(z) * p / az**2


def solve_case(nr: int) -> dict:
    # Rmax=1, Zmax=1.5 and nz=3*nr give dr=dz. az=0.8 is deliberately broad in z:
    # its characteristic axial wavenumber is O(1), so no periodic 2*pi/L gap is present.
    box = ep.Box(1.0, 1.5, nr, 3 * nr)
    sys = ep.build_minus_l5(box, exact_psi)
    R, Z = np.meshgrid(sys.r, sys.z, indexing="ij")
    omega = exact_omega(R, Z)
    exact = exact_psi(R, Z)
    psi = ep.solve(sys, omega)
    err = psi - exact
    res = ep.residual(sys, psi, omega)

    num_r = (psi[2:, :] - psi[:-2, :]) / (2.0 * sys.dr)
    num_z = (psi[:, 2:] - psi[:, :-2]) / (2.0 * sys.dz)
    grad_r, grad_z = exact_grad(R, Z)
    er = num_r[:, 1:-1] - grad_r[1:-1, 1:-1]
    ez = num_z[1:-1, :] - grad_z[1:-1, 1:-1]
    Ri = R[1:-1, 1:-1]
    grad_l2 = math.sqrt(float(np.sum(2.0 * math.pi * Ri * (er * er + ez * ez)) * sys.dr * sys.dz))
    return {
        "nr": nr,
        "nz": 3 * nr,
        "dr": sys.dr,
        "dz": sys.dz,
        "linf": float(np.max(np.abs(err))),
        "weighted_l2": ep.physical_weighted_l2(sys, err),
        "grad_r_linf": float(np.max(np.abs(er))),
        "grad_z_linf": float(np.max(np.abs(ez))),
        "grad_weighted_l2": grad_l2,
        "algebraic_residual_linf": float(np.max(np.abs(res))),
    }


def main() -> None:
    rows = [solve_case(n) for n in (24, 48, 96)]
    fields = ("linf", "weighted_l2", "grad_r_linf", "grad_z_linf", "grad_weighted_l2")
    spatial_pass = all(
        rows[0][k] > 3.0 * rows[1][k] and rows[1][k] > 3.0 * rows[2][k]
        for k in fields
    )
    passed = bool(
        spatial_pass
        and rows[-1]["linf"] < 2.0e-3
        and rows[-1]["algebraic_residual_linf"] < 1.0e-10
    )
    summary = {
        "classification": "NUMERICAL CANDIDATE INFRASTRUCTURE / E0 LOW-AXIAL-FREQUENCY STRESS",
        "manufactured_psi": "exp(-r^2/0.20^2-z^2/0.80^2)",
        "characteristic_axial_wavenumber": 1.25,
        "strictly_nonperiodic_z": True,
        "rows": rows,
        "spatial_pass": spatial_pass,
        "all_pass": passed,
        "nonclaim": "Manufactured finite-box stress test only; not a free-space truncation enclosure.",
    }
    outdir = HERE / "results_elliptic_e0_lowk"
    outdir.mkdir(parents=True, exist_ok=True)
    path = outdir / "summary.json"
    path.write_text(json.dumps(summary, indent=2, allow_nan=False))
    for row in rows:
        print(
            f"nr={row['nr']:3d} nz={row['nz']:3d} Linf={row['linf']:.6e} "
            f"L2w={row['weighted_l2']:.6e} dr={row['grad_r_linf']:.6e} dz={row['grad_z_linf']:.6e}"
        )
    print(f"low-k E0 all_pass={passed} summary={path}")
    if not passed:
        raise SystemExit("E0 low-axial-frequency stress FAIL")


if __name__ == "__main__":
    main()
