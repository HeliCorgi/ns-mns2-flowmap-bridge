"""Fail-closed S0 checks for the explicit compact R^3 axisymmetric swirl seed family."""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

import compact_family as cf


HERE = Path(__file__).resolve().parent


def _cart_div_fd(x: float, y: float, z: float, p: cf.SeedParams, h: float) -> float:
    def ux(xx):
        return float(cf.cartesian_velocity(xx, y, z, p)["ux"])
    def uy(yy):
        return float(cf.cartesian_velocity(x, yy, z, p)["uy"])
    def uz(zz):
        return float(cf.cartesian_velocity(x, y, zz, p)["uz"])
    return (
        (ux(x + h) - ux(x - h)) / (2.0 * h)
        + (uy(y + h) - uy(y - h)) / (2.0 * h)
        + (uz(z + h) - uz(z - h)) / (2.0 * h)
    )


def _minus_l5_fd(r: float, z: float, p: cf.SeedParams, h: float) -> float:
    def psi(rr, zz):
        return float(cf.scalar_fields(rr, zz, p)["psi1"])
    f0 = psi(r, z)
    frr = (psi(r + h, z) - 2.0 * f0 + psi(r - h, z)) / h**2
    fr = (psi(r + h, z) - psi(r - h, z)) / (2.0 * h)
    fzz = (psi(r, z + h) - 2.0 * f0 + psi(r, z - h)) / h**2
    return -(frr + 3.0 * fr / r + fzz)


def _second_order(errors: list[float]) -> bool:
    # The first two refinements should improve strongly unless already at roundoff.
    if errors[-1] < 5e-9:
        return True
    return errors[0] > 2.5 * errors[1] and errors[1] > 2.5 * errors[2]


def audit_seed(name: str, p: cf.SeedParams) -> dict:
    p.validate()
    b = cf.support_bounds(p)
    r0 = math.sqrt(p.s0)
    z0 = min(0.03, 0.20 * p.wz)

    # Analytic cylindrical divergence identity on a deterministic audit mesh.
    r = np.linspace(0.0, b["r_max"] * 1.02 + 1e-12, 129)
    z = np.linspace(b["z_min"] - 0.02, b["z_max"] + 0.02, 193)
    R, Z = np.meshgrid(r, z, indexing="ij")
    div = cf.divergence_terms(R, Z, p)["div"]
    analytic_div_max = float(np.max(np.abs(div)))

    # Axis regularity of the physical odd components.
    axis = cf.cylindrical_velocity(np.zeros_like(z), z, p)
    axis_vort = cf.cylindrical_vorticity(np.zeros_like(z), z, p)
    axis_odd_max = float(max(
        np.max(np.abs(axis["ur"])),
        np.max(np.abs(axis["utheta"])),
        np.max(np.abs(axis_vort["omega_theta"])),
    ))

    # Independent Cartesian divergence convergence at an interior point.
    xy = r0 / math.sqrt(2.0)
    hs = [2.0e-3, 1.0e-3, 5.0e-4]
    div_fd = [abs(_cart_div_fd(xy, xy, z0, p, h)) for h in hs]

    # Independent cylindrical finite-difference elliptic check away from r=0.
    omega_exact = float(cf.scalar_fields(r0, z0, p)["omega1"])
    l5_fd = [abs(_minus_l5_fd(r0, z0, p, h) - omega_exact) for h in hs]

    # Explicit compact support: evaluate strictly outside both analytic supports.
    outside_r = b["r_max"] + max(0.1, 0.25 * b["r_max"])
    outside_z = b["z_max"] + max(0.1, 0.25 * (b["z_max"] - b["z_min"]))
    out_r = cf.cylindrical_velocity(outside_r, 0.0, p)
    out_z = cf.cylindrical_velocity(r0, outside_z, p)
    support_leak = float(max(
        abs(float(out_r["ur"])), abs(float(out_r["utheta"])), abs(float(out_r["uz"])),
        abs(float(out_z["ur"])), abs(float(out_z["utheta"])), abs(float(out_z["uz"])),
    ))

    # Resolution-invariant pointwise sampling on nested grids.
    rr0 = np.linspace(0.0, b["r_max"] * 1.02 + 1e-12, 33)
    zz0 = np.linspace(b["z_min"] - 0.02, b["z_max"] + 0.02, 49)
    rr1 = np.linspace(rr0[0], rr0[-1], 65)
    zz1 = np.linspace(zz0[0], zz0[-1], 97)
    R0, Z0 = np.meshgrid(rr0, zz0, indexing="ij")
    R1, Z1 = np.meshgrid(rr1, zz1, indexing="ij")
    f0 = cf.scalar_fields(R0, Z0, p)
    f1 = cf.scalar_fields(R1, Z1, p)
    shared_err = 0.0
    for key in ("u1", "psi1", "omega1"):
        shared_err = max(shared_err, float(np.max(np.abs(f0[key] - f1[key][::2, ::2]))))

    # Finite positive physical energy and nonzero swirl.
    energy = cf.physical_energy(p, nr=241, nz=361)
    core = cf.cylindrical_velocity(r0, p.zu, p)
    swirl_probe = abs(float(core["utheta"]))

    finite = all(math.isfinite(x) for x in [
        analytic_div_max, axis_odd_max, *div_fd, *l5_fd, support_leak,
        shared_err, energy, swirl_probe,
    ])
    passed = bool(
        finite
        and analytic_div_max <= 1e-12
        and axis_odd_max <= 1e-14
        and _second_order(div_fd)
        and div_fd[-1] <= 2e-5
        and _second_order(l5_fd)
        and l5_fd[-1] <= 5e-3
        and support_leak == 0.0
        and shared_err <= 5e-13
        and energy > 0.0
        and swirl_probe > 0.0
    )

    return {
        "name": name,
        "params": p.to_dict(),
        "support": b,
        "finite": finite,
        "analytic_divergence_max": analytic_div_max,
        "axis_odd_components_max": axis_odd_max,
        "cartesian_divergence_fd_h": hs,
        "cartesian_divergence_fd_error": div_fd,
        "elliptic_minus_L5_fd_error": l5_fd,
        "support_leak": support_leak,
        "nested_grid_shared_point_error": shared_err,
        "physical_energy": energy,
        "swirl_probe": swirl_probe,
        "S0_pass": passed,
    }


def main() -> None:
    results = []
    for rec, p in zip(cf.seed_manifest(), cf.FROZEN_GEOMETRY_LATTICE):
        out = audit_seed(rec["name"], p)
        results.append(out)
        print(
            f"{out['name']} S0_pass={out['S0_pass']} "
            f"E={out['physical_energy']:.6e} "
            f"div_fd={out['cartesian_divergence_fd_error'][-1]:.3e} "
            f"L5_fd={out['elliptic_minus_L5_fd_error'][-1]:.3e}"
        )
    summary = {
        "classification": "NUMERICAL CANDIDATE INFRASTRUCTURE / S0 ONLY",
        "family": "R3 compact axisymmetric-with-swirl s=r^2 bump family",
        "n_seeds": len(results),
        "n_pass": sum(int(r["S0_pass"]) for r in results),
        "all_pass": all(r["S0_pass"] for r in results),
        "seeds": results,
        "nonclaim": "No time evolution, singularity, nonextendability, or Clay result is established.",
    }
    outdir = HERE / "results_seed_preflight"
    outdir.mkdir(parents=True, exist_ok=True)
    path = outdir / "summary.json"
    path.write_text(json.dumps(summary, indent=2, allow_nan=False))
    print(f"summary={path} all_pass={summary['all_pass']} n_pass={summary['n_pass']}/{summary['n_seeds']}")
    if not summary["all_pass"]:
        raise SystemExit("S0 FAIL: at least one seed did not pass the preregistered static audit")


if __name__ == "__main__":
    main()
