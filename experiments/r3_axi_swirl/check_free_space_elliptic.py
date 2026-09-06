"""E0 checks for the nonperiodic whole-space elliptic prototype."""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

import compact_family as cf
import free_space_elliptic_prototype as ep


HERE = Path(__file__).resolve().parent


def _solve_case(box: ep.Box, omega_fn, exact_fn, boundary_fn) -> dict:
    sys = ep.build_minus_l5(box, boundary_fn)
    R, Z = np.meshgrid(sys.r, sys.z, indexing="ij")
    omega = np.asarray(omega_fn(R, Z), dtype=float)
    exact = np.asarray(exact_fn(R, Z), dtype=float)
    psi = ep.solve(sys, omega)
    err = psi - exact
    res = ep.residual(sys, psi, omega)
    return {
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


def gaussian_exact_boundary_refinement() -> list[dict]:
    a = 0.25
    boundary = lambda r, z: ep.gaussian5_free_space_psi(r, z, a)
    omega = lambda r, z: ep.gaussian5_source(r, z, a)
    exact = lambda r, z: ep.gaussian5_free_space_psi(r, z, a)
    return [
        _solve_case(ep.Box(1.0, 1.2, nr, 2 * nr), omega, exact, boundary)
        for nr in (24, 48, 96)
    ]


def gaussian_zero_boundary_domain_enlargement() -> list[dict]:
    """Hold mesh scale about 0.02 and enlarge the artificial box.

    Errors are measured only on a fixed inner core.  This is a truncation-sensitivity diagnostic,
    not a rigorous tail bound.
    """
    a = 0.25
    out = []
    for B in (0.6, 0.8, 1.0, 1.5):
        nr = int(round(B / 0.02))
        nz = int(round(2.0 * B / 0.02))
        box = ep.Box(B, B, nr, nz)
        sys = ep.build_minus_l5(box, lambda r, z: 0.0)
        R, Z = np.meshgrid(sys.r, sys.z, indexing="ij")
        omega = ep.gaussian5_source(R, Z, a)
        exact = ep.gaussian5_free_space_psi(R, Z, a)
        psi = ep.solve(sys, omega)
        err = psi - exact
        core = (R <= 0.45) & (np.abs(Z) <= 0.45)
        core_linf = float(np.max(np.abs(err[core])))
        core_l2 = math.sqrt(float(np.sum(2.0 * math.pi * R[core] * err[core] ** 2) * sys.dr * sys.dz))
        out.append({
            "Rmax": B,
            "Zmax": B,
            "nr": nr,
            "nz": nz,
            "dr": sys.dr,
            "dz": sys.dz,
            "core_linf": core_linf,
            "core_weighted_l2": core_l2,
        })
    return out


def compact_seed_refinement() -> list[dict]:
    """Recover one preregistered compact seed from its exact derived omega1.

    The compact bump is intentionally sharp in s, so this uses a higher-resolution ladder than
    the smooth Gaussian scheme check.  Zero artificial-boundary data are exact here because the
    manufactured psi1 itself is compactly supported strictly inside the box.
    """
    p = cf.FROZEN_GEOMETRY_LATTICE[4]  # R3S04: s0=.09, wz=.18, zu=0
    boundary = lambda r, z: 0.0

    def omega(r, z):
        return cf.scalar_fields(r, z, p)["omega1"]

    def exact(r, z):
        return cf.scalar_fields(r, z, p)["psi1"]

    return [
        _solve_case(ep.Box(0.7, 0.6, nr, 2 * nr), omega, exact, boundary)
        for nr in (96, 128, 160)
    ]


def _strictly_decreasing(xs: list[float]) -> bool:
    return all(a > b for a, b in zip(xs, xs[1:]))


def main() -> None:
    gaussian_ref = gaussian_exact_boundary_refinement()
    domain = gaussian_zero_boundary_domain_enlargement()
    compact = compact_seed_refinement()

    # Smooth reference: exact-boundary Linf/L2 should exhibit clear second-order reduction when h halves.
    gl = [r["linf"] for r in gaussian_ref]
    gw = [r["weighted_l2"] for r in gaussian_ref]
    gaussian_spatial_pass = bool(
        gl[0] > 3.0 * gl[1] and gl[1] > 3.0 * gl[2]
        and gw[0] > 3.0 * gw[1] and gw[1] > 3.0 * gw[2]
        and gaussian_ref[-1]["algebraic_residual_linf"] < 1e-10
    )

    # Zero-boundary approximation to the nonzero-tail Gaussian must improve as the box expands.
    dl = [r["core_linf"] for r in domain]
    dw = [r["core_weighted_l2"] for r in domain]
    domain_sensitivity_pass = _strictly_decreasing(dl) and _strictly_decreasing(dw)

    # The sharp compact seed only requires clear monotone recovery on this first high-resolution ladder.
    cl = [r["linf"] for r in compact]
    cw = [r["weighted_l2"] for r in compact]
    compact_pass = bool(
        _strictly_decreasing(cl)
        and _strictly_decreasing(cw)
        and cl[-1] < 1e-3
        and cw[-1] < 1e-4
        and compact[-1]["algebraic_residual_linf"] < 1e-9
    )

    summary = {
        "classification": "NUMERICAL CANDIDATE INFRASTRUCTURE / E0 PROTOTYPE ONLY",
        "gaussian_exact_boundary_refinement": gaussian_ref,
        "gaussian_zero_boundary_domain_enlargement": domain,
        "compact_seed_R3S04_refinement": compact,
        "gaussian_spatial_pass": gaussian_spatial_pass,
        "domain_sensitivity_pass": domain_sensitivity_pass,
        "compact_seed_pass": compact_pass,
        "all_pass": gaussian_spatial_pass and domain_sensitivity_pass and compact_pass,
        "decision_boundary": (
            "Passing this check validates only the finite-difference prototype on manufactured tests. "
            "The zero-boundary domain sequence is a truncation-sensitivity observation, not a rigorous free-space tail enclosure."
        ),
    }

    outdir = HERE / "results_elliptic_e0"
    outdir.mkdir(parents=True, exist_ok=True)
    path = outdir / "summary.json"
    path.write_text(json.dumps(summary, indent=2, allow_nan=False))

    print("Gaussian exact-boundary refinement:")
    for r in gaussian_ref:
        print(f"  nr={r['nr']:3d} Linf={r['linf']:.6e} L2w={r['weighted_l2']:.6e}")
    print("Gaussian zero-boundary domain enlargement:")
    for r in domain:
        print(f"  B={r['Rmax']:.2f} core_Linf={r['core_linf']:.6e} core_L2w={r['core_weighted_l2']:.6e}")
    print("Compact R3S04 refinement:")
    for r in compact:
        print(f"  nr={r['nr']:3d} Linf={r['linf']:.6e} L2w={r['weighted_l2']:.6e}")
    print(
        f"all_pass={summary['all_pass']} gaussian={gaussian_spatial_pass} "
        f"domain={domain_sensitivity_pass} compact={compact_pass} summary={path}"
    )
    if not summary["all_pass"]:
        raise SystemExit("E0 prototype FAIL")


if __name__ == "__main__":
    main()
