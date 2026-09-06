"""E0 checks for the nonperiodic whole-space elliptic prototype."""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

import compact_family as cf
import free_space_elliptic_prototype as ep


HERE = Path(__file__).resolve().parent


def _gradient_errors(system: ep.EllipticSystem, psi: np.ndarray, exact_grad_fn) -> dict:
    R, Z = np.meshgrid(system.r, system.z, indexing="ij")
    exact_r, exact_z = exact_grad_fn(R, Z)
    num_r = (psi[2:, :] - psi[:-2, :]) / (2.0 * system.dr)
    num_z = (psi[:, 2:] - psi[:, :-2]) / (2.0 * system.dz)
    err_r = num_r[:, 1:-1] - np.asarray(exact_r)[1:-1, 1:-1]
    err_z = num_z[1:-1, :] - np.asarray(exact_z)[1:-1, 1:-1]
    Ri = R[1:-1, 1:-1]
    weighted = math.sqrt(float(
        np.sum(2.0 * math.pi * Ri * (err_r**2 + err_z**2)) * system.dr * system.dz
    ))
    return {
        "grad_r_linf": float(np.max(np.abs(err_r))),
        "grad_z_linf": float(np.max(np.abs(err_z))),
        "grad_weighted_l2": weighted,
    }


def _solve_case(box: ep.Box, omega_fn, exact_fn, boundary_fn, exact_grad_fn=None) -> dict:
    sys = ep.build_minus_l5(box, boundary_fn)
    R, Z = np.meshgrid(sys.r, sys.z, indexing="ij")
    omega = np.asarray(omega_fn(R, Z), dtype=float)
    exact = np.asarray(exact_fn(R, Z), dtype=float)
    psi = ep.solve(sys, omega)
    err = psi - exact
    res = ep.residual(sys, psi, omega)
    out = {
        "nr": box.nr,
        "nz": box.nz,
        "Rmax": box.Rmax,
        "Zmax": box.Zmax,
        "dr": sys.dr,
        "dz": sys.dz,
        "linf": float(np.max(np.abs(err))),
        "weighted_l2": ep.physical_weighted_l2(sys, err),
        "algebraic_residual_linf": float(np.max(np.abs(res))),
    }
    if exact_grad_fn is not None:
        out.update(_gradient_errors(sys, psi, exact_grad_fn))
    return out


def gaussian_exact_boundary_refinement() -> list[dict]:
    a = 0.25
    boundary = lambda r, z: ep.gaussian5_free_space_psi(r, z, a)
    omega = lambda r, z: ep.gaussian5_source(r, z, a)
    exact = lambda r, z: ep.gaussian5_free_space_psi(r, z, a)
    exact_grad = lambda r, z: ep.gaussian5_free_space_grad(r, z, a)
    return [
        _solve_case(ep.Box(1.0, 1.2, nr, 2 * nr), omega, exact, boundary, exact_grad)
        for nr in (24, 48, 96)
    ]


def _gaussian_zero_boundary_box(Rmax: float, Zmax: float, h: float = 0.02) -> dict:
    a = 0.25
    nr = int(round(Rmax / h))
    nz = int(round(2.0 * Zmax / h))
    box = ep.Box(Rmax, Zmax, nr, nz)
    sys = ep.build_minus_l5(box, lambda r, z: 0.0)
    R, Z = np.meshgrid(sys.r, sys.z, indexing="ij")
    omega = ep.gaussian5_source(R, Z, a)
    exact = ep.gaussian5_free_space_psi(R, Z, a)
    psi = ep.solve(sys, omega)
    err = psi - exact
    core = (R <= 0.45) & (np.abs(Z) <= 0.45)
    core_linf = float(np.max(np.abs(err[core])))
    core_l2 = math.sqrt(float(
        np.sum(2.0 * math.pi * R[core] * err[core] ** 2) * sys.dr * sys.dz
    ))
    return {
        "Rmax": Rmax,
        "Zmax": Zmax,
        "nr": nr,
        "nz": nz,
        "dr": sys.dr,
        "dz": sys.dz,
        "core_linf": core_linf,
        "core_weighted_l2": core_l2,
    }


def gaussian_zero_boundary_domain_enlargement() -> dict[str, list[dict]]:
    """Hold mesh scale about 0.02 and enlarge artificial boundaries independently.

    Errors are measured only on a fixed inner core. These are truncation-sensitivity diagnostics,
    not rigorous tail bounds.
    """
    vals = (0.6, 0.8, 1.0, 1.5)
    return {
        "square": [_gaussian_zero_boundary_box(B, B) for B in vals],
        "radial_only": [_gaussian_zero_boundary_box(B, 1.5) for B in vals],
        "axial_only": [_gaussian_zero_boundary_box(1.5, B) for B in vals],
    }


def gaussian_green_axis_crosscheck() -> dict:
    """Compare the closed radial solution with an independent 5D Green integral on r=0."""
    a = 0.25
    z_values = (0.0, 0.10, 0.25, 0.40)
    samples = []
    for z in z_values:
        green = ep.gaussian5_green_axis_quadrature(z, a=a, cutoff=1.5)
        exact = float(ep.gaussian5_free_space_psi(0.0, z, a))
        samples.append({
            "z": z,
            "green_axis": green,
            "closed_radial": exact,
            "abs_error": abs(green - exact),
        })
    return {
        "samples": samples,
        "max_abs_error": max(s["abs_error"] for s in samples),
        "note": "Adaptive 5D Green integral truncated at 1.5; Gaussian tail is tiny but not an interval enclosure.",
    }


def compact_seed_refinement() -> list[dict]:
    """Recover one preregistered compact seed from its exact derived omega1.

    The compact bump is intentionally sharp in s, so this uses a higher-resolution ladder than
    the smooth Gaussian scheme check. Zero artificial-boundary data are exact here because the
    manufactured psi1 itself is compactly supported strictly inside the box.
    """
    p = cf.FROZEN_GEOMETRY_LATTICE[4]  # R3S04: s0=.09, wz=.18, zu=0
    boundary = lambda r, z: 0.0

    def omega(r, z):
        return cf.scalar_fields(r, z, p)["omega1"]

    def exact(r, z):
        return cf.scalar_fields(r, z, p)["psi1"]

    def exact_grad(r, z):
        f = cf.scalar_fields(r, z, p)
        return 2.0 * np.asarray(r) * f["psi1_s"], f["psi1_z"]

    return [
        _solve_case(ep.Box(0.7, 0.6, nr, 2 * nr), omega, exact, boundary, exact_grad)
        for nr in (96, 128, 160)
    ]


def _strictly_decreasing(xs: list[float]) -> bool:
    return all(a > b for a, b in zip(xs, xs[1:]))


def _domain_sequence_pass(rows: list[dict]) -> bool:
    return (
        _strictly_decreasing([r["core_linf"] for r in rows])
        and _strictly_decreasing([r["core_weighted_l2"] for r in rows])
    )


def main() -> None:
    gaussian_ref = gaussian_exact_boundary_refinement()
    domain = gaussian_zero_boundary_domain_enlargement()
    green = gaussian_green_axis_crosscheck()
    compact = compact_seed_refinement()

    # Smooth reference: exact-boundary values and first derivatives should exhibit clear
    # second-order reduction when h halves. These are prototype smoke thresholds, not a later
    # production candidate-resolution criterion.
    gaussian_fields = (
        "linf", "weighted_l2", "grad_r_linf", "grad_z_linf", "grad_weighted_l2"
    )
    gaussian_spatial_pass = all(
        gaussian_ref[0][key] > 3.0 * gaussian_ref[1][key]
        and gaussian_ref[1][key] > 3.0 * gaussian_ref[2][key]
        for key in gaussian_fields
    ) and gaussian_ref[-1]["algebraic_residual_linf"] < 1e-10

    # A separate Green-integral path checks the closed radial free-space reference itself.
    green_reference_pass = green["max_abs_error"] < 1e-11

    # Zero-boundary approximation to the nonzero-tail Gaussian must improve under square-box,
    # radial-only and axial-only enlargement. This does not turn domain doubling into a tail proof.
    domain_sensitivity_pass = all(_domain_sequence_pass(rows) for rows in domain.values())

    # The sharp compact seed requires monotone field and derivative recovery on this first
    # high-resolution ladder. The absolute field thresholds are prototype checks only.
    compact_fields = ("linf", "weighted_l2", "grad_r_linf", "grad_z_linf", "grad_weighted_l2")
    compact_pass = bool(
        all(_strictly_decreasing([r[key] for r in compact]) for key in compact_fields)
        and compact[-1]["linf"] < 1e-3
        and compact[-1]["weighted_l2"] < 1e-4
        and compact[-1]["algebraic_residual_linf"] < 1e-9
    )

    summary = {
        "classification": "NUMERICAL CANDIDATE INFRASTRUCTURE / E0 PROTOTYPE ONLY",
        "gaussian_exact_boundary_refinement": gaussian_ref,
        "gaussian_green_axis_crosscheck": green,
        "gaussian_zero_boundary_domain_enlargement": domain,
        "compact_seed_R3S04_refinement": compact,
        "gaussian_spatial_pass": gaussian_spatial_pass,
        "green_reference_pass": green_reference_pass,
        "domain_sensitivity_pass": domain_sensitivity_pass,
        "compact_seed_pass": compact_pass,
        "all_pass": gaussian_spatial_pass and green_reference_pass and domain_sensitivity_pass and compact_pass,
        "decision_boundary": (
            "Passing this check validates only the finite-difference prototype on manufactured tests. "
            "The zero-boundary domain sequences are truncation-sensitivity observations, and the Green "
            "quadrature is a floating-point cross-check, not a rigorous free-space tail enclosure."
        ),
    }

    outdir = HERE / "results_elliptic_e0"
    outdir.mkdir(parents=True, exist_ok=True)
    path = outdir / "summary.json"
    path.write_text(json.dumps(summary, indent=2, allow_nan=False))

    print("Gaussian exact-boundary refinement:")
    for r in gaussian_ref:
        print(
            f"  nr={r['nr']:3d} Linf={r['linf']:.6e} L2w={r['weighted_l2']:.6e} "
            f"dr={r['grad_r_linf']:.6e} dz={r['grad_z_linf']:.6e}"
        )
    print(f"Green-axis cross-check max_abs={green['max_abs_error']:.6e}")
    for kind, rows in domain.items():
        print(f"Gaussian zero-boundary {kind} enlargement:")
        for r in rows:
            print(
                f"  R={r['Rmax']:.2f} Z={r['Zmax']:.2f} "
                f"core_Linf={r['core_linf']:.6e} core_L2w={r['core_weighted_l2']:.6e}"
            )
    print("Compact R3S04 refinement:")
    for r in compact:
        print(
            f"  nr={r['nr']:3d} Linf={r['linf']:.6e} L2w={r['weighted_l2']:.6e} "
            f"dr={r['grad_r_linf']:.6e} dz={r['grad_z_linf']:.6e}"
        )
    print(
        f"all_pass={summary['all_pass']} gaussian={gaussian_spatial_pass} "
        f"green={green_reference_pass} domain={domain_sensitivity_pass} "
        f"compact={compact_pass} summary={path}"
    )
    if not summary["all_pass"]:
        raise SystemExit("E0 prototype FAIL")


if __name__ == "__main__":
    main()
