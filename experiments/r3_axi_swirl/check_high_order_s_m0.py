"""Preregistered M0 audit for the high-order s=r^2 / nonperiodic-z method."""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Callable

import numpy as np

import compact_family as cf
import free_space_elliptic_prototype as old_ep
import high_order_s_elliptic as hos
from check_low_axial_frequency_e0 import exact_grad as lowk_grad
from check_low_axial_frequency_e0 import exact_omega as lowk_omega
from check_low_axial_frequency_e0 import exact_psi as lowk_psi


HERE = Path(__file__).resolve().parent
OUTDIR = HERE / "results_hos_m0"


def strictly_decreasing(values: list[float]) -> bool:
    return all(a > b for a, b in zip(values, values[1:]))


def solve_case(
    box: hos.HOSBox,
    omega_fn: Callable,
    exact_fn: Callable,
    boundary_fn: Callable,
    exact_grad_fn: Callable,
) -> dict:
    system = hos.build_minus_l5(box, boundary_fn)
    R, Z = np.meshgrid(system.r, system.z, indexing="ij")
    omega = np.asarray(omega_fn(R, Z), dtype=float)
    exact = np.asarray(exact_fn(R, Z), dtype=float)
    psi = hos.solve(system, omega)
    err = psi - exact
    res = hos.residual(system, psi, omega)
    num_r, num_z = hos.physical_grad_r_z(system, psi, boundary_fn)
    ex_r, ex_z = exact_grad_fn(R, Z)
    er = num_r - np.asarray(ex_r, dtype=float)
    ez = num_z - np.asarray(ex_z, dtype=float)
    return {
        "nr": box.nr,
        "nz": box.nz,
        "Rmax": box.Rmax,
        "Zmax": box.Zmax,
        "dr": system.dr,
        "dz": system.dz,
        "linf": float(np.max(np.abs(err))),
        "weighted_l2": hos.physical_weighted_l2(system, err),
        "grad_r_linf": float(np.max(np.abs(er))),
        "grad_z_linf": float(np.max(np.abs(ez))),
        "grad_weighted_l2": math.sqrt(
            hos.physical_weighted_l2(system, er) ** 2
            + hos.physical_weighted_l2(system, ez) ** 2
        ),
        "algebraic_residual_linf": float(np.max(np.abs(res))),
    }


def gaussian_reference() -> list[dict]:
    a = 0.25
    return [
        solve_case(
            hos.HOSBox(1.0, 1.2, nr, nz),
            lambda r, z: old_ep.gaussian5_source(r, z, a),
            lambda r, z: old_ep.gaussian5_free_space_psi(r, z, a),
            lambda r, z: old_ep.gaussian5_free_space_psi(r, z, a),
            lambda r, z: old_ep.gaussian5_free_space_grad(r, z, a),
        )
        for nr, nz in ((20, 48), (30, 72), (40, 96))
    ]


def direct_derivative_seed(seed_index: int) -> list[dict]:
    p = cf.FROZEN_GEOMETRY_LATTICE[seed_index]
    rows: list[dict] = []
    zero = lambda r, z: 0.0
    for nr, nz in ((160, 288), (200, 360), (240, 432)):
        system = hos.build_minus_l5(hos.HOSBox(1.0, 0.9, nr, nz), zero)
        R, Z = np.meshgrid(system.r, system.z, indexing="ij")
        f = cf.scalar_fields(R, Z, p)
        row: dict[str, float | int] = {"nr": nr, "nz": nz}
        for field_name, exact_s_name, exact_z_name in (
            ("psi1", "psi1_s", "psi1_z"),
            ("u1", "u1_s", "u1_z"),
        ):
            arr = np.asarray(f[field_name], dtype=float)
            num_s, num_z = hos.differentiate_s_z(system, arr, zero)
            es = num_s - np.asarray(f[exact_s_name], dtype=float)
            ez = num_z - np.asarray(f[exact_z_name], dtype=float)
            row[f"{field_name}_s_linf"] = float(np.max(np.abs(es)))
            row[f"{field_name}_s_l2"] = hos.physical_weighted_l2(system, es)
            row[f"{field_name}_z_linf"] = float(np.max(np.abs(ez)))
            row[f"{field_name}_z_l2"] = hos.physical_weighted_l2(system, ez)
        rows.append(row)
    return rows


def compact_recovery(seed_index: int) -> list[dict]:
    p = cf.FROZEN_GEOMETRY_LATTICE[seed_index]
    zero = lambda r, z: 0.0

    def omega(r, z):
        return cf.scalar_fields(r, z, p)["omega1"]

    def exact(r, z):
        return cf.scalar_fields(r, z, p)["psi1"]

    def exact_grad(r, z):
        f = cf.scalar_fields(r, z, p)
        return 2.0 * np.asarray(r) * f["psi1_s"], f["psi1_z"]

    return [
        solve_case(hos.HOSBox(1.0, 0.9, nr, nz), omega, exact, zero, exact_grad)
        for nr, nz in ((160, 288), (200, 360), (240, 432))
    ]


def low_axial_frequency() -> list[dict]:
    return [
        solve_case(
            hos.HOSBox(1.0, 1.5, nr, 3 * nr),
            lowk_omega,
            lowk_psi,
            lowk_psi,
            lowk_grad,
        )
        for nr in (24, 48, 96)
    ]


def gaussian_zero_boundary_box(Rmax: float, Zmax: float, h: float = 0.02) -> dict:
    a = 0.25
    nr = int(round(Rmax / h))
    nz = int(round(2.0 * Zmax / h))
    system = hos.build_minus_l5(hos.HOSBox(Rmax, Zmax, nr, nz), lambda r, z: 0.0)
    R, Z = np.meshgrid(system.r, system.z, indexing="ij")
    omega = old_ep.gaussian5_source(R, Z, a)
    exact = old_ep.gaussian5_free_space_psi(R, Z, a)
    psi = hos.solve(system, omega)
    err = psi - exact
    core = (R <= 0.45) & (np.abs(Z) <= 0.45)
    core_linf = float(np.max(np.abs(err[core])))
    density = 2.0 * math.pi * R[core] * err[core] ** 2
    core_l2 = math.sqrt(max(0.0, float(np.sum(density) * system.dr * system.dz)))
    return {
        "Rmax": Rmax,
        "Zmax": Zmax,
        "nr": nr,
        "nz": nz,
        "core_linf": core_linf,
        "core_weighted_l2": core_l2,
    }


def domain_sensitivity() -> dict[str, list[dict]]:
    vals = (0.6, 0.8, 1.0, 1.5)
    return {
        "square": [gaussian_zero_boundary_box(v, v) for v in vals],
        "radial_only": [gaussian_zero_boundary_box(v, 1.5) for v in vals],
        "axial_only": [gaussian_zero_boundary_box(1.5, v) for v in vals],
    }


def monotone_error_rows(rows: list[dict], keys: tuple[str, ...]) -> bool:
    return all(strictly_decreasing([float(row[key]) for row in rows]) for key in keys)


def main() -> None:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    errors = ("linf", "weighted_l2", "grad_r_linf", "grad_z_linf", "grad_weighted_l2")

    gaussian = gaussian_reference()
    m0a = monotone_error_rows(gaussian, errors) and gaussian[-1]["algebraic_residual_linf"] < 1e-9

    direct: dict[str, list[dict]] = {
        "R3S04": direct_derivative_seed(4),
        "R3S02": direct_derivative_seed(2),
    }
    direct_keys = (
        "psi1_s_linf", "psi1_s_l2", "psi1_z_linf", "psi1_z_l2",
        "u1_s_linf", "u1_s_l2", "u1_z_linf", "u1_z_l2",
    )
    m0b = all(monotone_error_rows(rows, direct_keys) for rows in direct.values())

    compact = {
        "R3S04": compact_recovery(4),
        "R3S02": compact_recovery(2),
    }
    m0c = True
    for rows in compact.values():
        m0c = bool(
            m0c
            and monotone_error_rows(rows, errors)
            and rows[-1]["linf"] < 1e-3
            and rows[-1]["weighted_l2"] < 1e-4
            and rows[-1]["algebraic_residual_linf"] < 1e-9
        )

    lowk = low_axial_frequency()
    m0d = monotone_error_rows(lowk, errors) and lowk[-1]["algebraic_residual_linf"] < 1e-9

    domain = domain_sensitivity()
    m0e = all(
        strictly_decreasing([row["core_linf"] for row in rows])
        and strictly_decreasing([row["core_weighted_l2"] for row in rows])
        for rows in domain.values()
    )

    failures: list[str] = []
    if not m0a:
        failures.append("M0-A Gaussian exact-boundary refinement FAIL")
    for seed, rows in direct.items():
        for key in direct_keys:
            vals = [float(row[key]) for row in rows]
            if not strictly_decreasing(vals):
                failures.append(f"M0-B {seed} {key} not strictly decreasing: {vals}")
    for seed, rows in compact.items():
        for key in errors:
            vals = [float(row[key]) for row in rows]
            if not strictly_decreasing(vals):
                failures.append(f"M0-C {seed} {key} not strictly decreasing: {vals}")
        if not rows[-1]["linf"] < 1e-3:
            failures.append(f"M0-C {seed} final Linf {rows[-1]['linf']:.12e} >= 1e-3")
        if not rows[-1]["weighted_l2"] < 1e-4:
            failures.append(f"M0-C {seed} final L2 {rows[-1]['weighted_l2']:.12e} >= 1e-4")
        if not rows[-1]["algebraic_residual_linf"] < 1e-9:
            failures.append(
                f"M0-C {seed} residual {rows[-1]['algebraic_residual_linf']:.12e} >= 1e-9"
            )
    if not m0d:
        failures.append("M0-D low-axial-frequency refinement FAIL")
    for kind, rows in domain.items():
        for key in ("core_linf", "core_weighted_l2"):
            vals = [float(row[key]) for row in rows]
            if not strictly_decreasing(vals):
                failures.append(f"M0-E {kind} {key} not strictly decreasing: {vals}")

    summary = {
        "classification": "NUMERICAL METHOD QUALIFICATION / HIGH-ORDER S-COORDINATE M0",
        "preregistration": "R3_HOS_M0_PREREG_2026-09-07.md",
        "method": {
            "radial_coordinate": "s=r^2",
            "local_stencil_nodes": 7,
            "local_polynomial_degree": 6,
            "z_topology": "strictly nonperiodic",
            "outer_boundary": "artificial Dirichlet",
            "precision": "float64",
        },
        "gaussian_reference": gaussian,
        "direct_derivative_audit": direct,
        "compact_elliptic_recovery": compact,
        "low_axial_frequency": lowk,
        "domain_sensitivity": domain,
        "M0_A_pass": bool(m0a),
        "M0_B_pass": bool(m0b),
        "M0_C_pass": bool(m0c),
        "M0_D_pass": bool(m0d),
        "M0_E_pass": bool(m0e),
        "failures": failures,
        "M0_pass": len(failures) == 0,
        "nonclaim": (
            "Floating-point numerical-method qualification only; not validated free-space "
            "inversion, continuum convergence, singularity, global regularity, or a Clay result."
        ),
    }
    path = OUTDIR / "summary.json"
    path.write_text(json.dumps(summary, indent=2, allow_nan=False))

    print("HOS M0 Gaussian:")
    for row in gaussian:
        print(
            f"  {row['nr']}x{row['nz']} Linf={row['linf']:.6e} L2={row['weighted_l2']:.6e} "
            f"gr={row['grad_r_linf']:.6e} gz={row['grad_z_linf']:.6e}"
        )
    for seed, rows in compact.items():
        print(f"HOS M0 compact {seed}:")
        for row in rows:
            print(
                f"  {row['nr']}x{row['nz']} Linf={row['linf']:.6e} L2={row['weighted_l2']:.6e} "
                f"gr={row['grad_r_linf']:.6e} gz={row['grad_z_linf']:.6e}"
            )
    print(
        f"M0_pass={summary['M0_pass']} A={m0a} B={m0b} C={m0c} D={m0d} E={m0e} "
        f"failures={len(failures)} summary={path}"
    )
    for failure in failures:
        print(f"FAIL: {failure}")
    if failures:
        raise SystemExit("R3 HOS M0 FAIL")


if __name__ == "__main__":
    main()
