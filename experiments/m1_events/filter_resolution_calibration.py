"""Manufactured resolution calibration for the M-1 Yu-structured near/far diagnostic.

Governed by:
  M1_FILTER_RESOLUTION_CALIBRATION_PREREG_2026-09-06.md
  M1_FILTER_RESOLUTION_CALIBRATION_PREREG_ADDENDUM_2026-09-06.md

This is evidence-grade numerical calibration only.  It does not use E3c/E4c data and does not
provide a rigorous continuum error bound.

Usage
-----
Run one grid:
    python filter_resolution_calibration.py run 64 OUT.json

Aggregate N=64,96,128,160,192 JSON files in one directory:
    python filter_resolution_calibration.py aggregate INPUT_DIR OUT.json
"""
from __future__ import annotations

import gc
import json
import math
import sys
from pathlib import Path

import numpy as np

import events as ev
import nearfar_yu as nf
from nearfar_decomp import cutoff, quad

NU = 0.02
DT_CAL = 1.0e-4
RHO = 0.25
RADII = (math.pi / 12.0, math.pi / 6.0, math.pi / 3.0)
SIGMAS = (0.125, 0.25)
GRIDS = (64, 96, 128, 160, 192)
COARSE_GRIDS = (64, 96, 128)
REF1 = 160
REF2 = 192
DIV_TOL = 1.0e-10
QUANTITIES = ("A_N", "g", "B_F", "B_C", "B_L")

# Three explicit finite trigonometric polynomials.  For every mode both the cosine and sine
# coefficient vector are exactly perpendicular to k over the rationals/integers.  No RNG and no
# production initializer is involved.
MANUFACTURED = {
    "M0": (
        ((1, 1, 0), (1.0, -1.0, 0.5), (0.5, -0.5, 1.0)),
        ((0, 1, 2), (1.0, 2.0, -1.0), (2.0, -2.0, 1.0)),
        ((2, -1, 1), (1.0, 1.0, -1.0), (0.0, 1.0, 1.0)),
    ),
    "M1": (
        ((1, 0, 2), (2.0, 1.0, -1.0), (0.0, 1.0, 0.0)),
        ((2, 1, 1), (0.0, 1.0, -1.0), (1.0, -1.0, -1.0)),
        ((1, -2, 0), (2.0, 1.0, 1.0), (0.0, 0.0, 1.0)),
    ),
    "M2": (
        ((3, 1, 0), (1.0, -3.0, 1.0), (0.0, 0.0, 1.0)),
        ((1, 2, 2), (0.0, 1.0, -1.0), (2.0, -1.0, 0.0)),
        ((2, 0, -1), (1.0, 1.0, 2.0), (0.0, 1.0, 0.0)),
    ),
}


def _validate_mode_table() -> None:
    for name, modes in MANUFACTURED.items():
        for k, ac, ass in modes:
            kk = np.asarray(k, dtype=float)
            if not (1.0 <= float(np.linalg.norm(kk)) <= 4.0):
                raise RuntimeError(f"{name}: k={k} outside preregistered band")
            if float(np.dot(kk, np.asarray(ac, dtype=float))) != 0.0:
                raise RuntimeError(f"{name}: cosine coefficient not perpendicular to {k}")
            if float(np.dot(kk, np.asarray(ass, dtype=float))) != 0.0:
                raise RuntimeError(f"{name}: sine coefficient not perpendicular to {k}")


def manufactured_uh(g: ev.Grid, name: str) -> tuple[np.ndarray, float]:
    modes = MANUFACTURED[name]
    X, Y, Z = g.X
    u = np.zeros((3, g.N, g.N, g.N), dtype=float)
    for k, ac, ass in modes:
        phase = k[0] * X + k[1] * Y + k[2] * Z
        cph = np.cos(phase)
        sph = np.sin(phase)
        for j in range(3):
            u[j] += ac[j] * cph + ass[j] * sph
    uh = np.array([g.rfft(u[j]) for j in range(3)]) * g.DEALIAS
    divh = g.K[0] * uh[0] + g.K[1] * uh[1] + g.K[2] * uh[2]
    div_max = float(np.max(np.abs(divh)))
    if not math.isfinite(div_max) or div_max > DIV_TOL:
        raise RuntimeError(f"{name} N={g.N}: manufactured Fourier divergence {div_max:.3e}")
    return uh, div_max


def commutator_forcing_lowmem(g: ev.Grid, uh: np.ndarray, Uh: np.ndarray, Gh: np.ndarray) -> np.ndarray:
    """Algebraically identical to nearfar_yu.commutator_forcing with lower peak memory."""
    u = [g.irfft(uh[c]) for c in range(3)]
    U = [g.irfft(Uh[c]) for c in range(3)]
    divtau_h = [np.zeros_like(uh[0]) for _ in range(3)]
    for i in range(3):
        for j in range(3):
            tau_h = g.rfft(u[i] * u[j]) * Gh - g.rfft(U[i] * U[j])
            divtau_h[i] += 1j * g.K[j] * tau_h
            del tau_h
    curl_h = g.curl_h(divtau_h)
    out = np.array([g.irfft(curl_h[c]) for c in range(3)])
    del u, U, divtau_h, curl_h
    return out


def _cell(
    g: ev.Grid,
    uh: np.ndarray,
    uh1: np.ndarray,
    chi: np.ndarray,
    gchi: list[np.ndarray],
    lchi: np.ndarray,
    R: float,
    sigma: float,
) -> dict:
    ell = sigma * R
    Uh, Oh, U, Om, S, gradO2, Gh = nf.filtered_fields(g, uh, ell)
    Sfar = nf.far_strain(g, Oh, RHO * R)

    # S_near = S - Sfar, but compute the quadratic form by subtraction to avoid another
    # N^3 x 3 x 3 allocation.  This is the same algebraic decomposition used in nearfar_yu.
    q_total = quad(Om, S)
    q_far = quad(Om, Sfar)
    q_near = q_total - q_far
    O2 = np.sum(Om * Om, axis=0)

    dx3 = g.dx3
    P = NU * dx3 * float(np.sum(chi * gradO2))
    if not math.isfinite(P) or P <= 0.0:
        raise RuntimeError(f"N={g.N} R={R} sigma={sigma}: nonpositive/nonfinite P={P}")

    Vn = dx3 * float(np.sum(chi * q_near))
    Vf = dx3 * float(np.sum(chi * q_far))
    Vnp = dx3 * float(np.sum(chi * np.maximum(q_near, 0.0)))
    Vfp = dx3 * float(np.sum(chi * np.maximum(q_far, 0.0)))

    cdt = commutator_forcing_lowmem(g, uh, Uh, Gh)
    Rc = -dx3 * float(np.sum(chi * np.sum(Om * cdt, axis=0)))
    Ll = (
        dx3 * float(np.sum(0.5 * O2 * sum(U[i] * gchi[i] for i in range(3))))
        + NU * dx3 * float(np.sum(0.5 * O2 * lchi))
    )

    Oh1 = g.curl_h(np.array([uh1[c] * Gh for c in range(3)]))
    Om1 = np.array([g.irfft(Oh1[c]) for c in range(3)])
    O2_1 = np.sum(Om1 * Om1, axis=0)
    dfd = (dx3 * float(np.sum(chi * O2_1)) - dx3 * float(np.sum(chi * O2))) / (2.0 * DT_CAL)
    dpred = Vn + Vf - P + Rc + Ll
    budget_resid = (dfd - dpred) / max(abs(dfd) + abs(dpred), 1.0e-300)

    values = {
        "R": R,
        "sigma": sigma,
        "ell": ell,
        "R_over_dx": R / g.dx,
        "ell_over_dx": ell / g.dx,
        "P": P,
        "V_near": Vn,
        "V_far": Vf,
        "Vp_near": Vnp,
        "Vp_far": Vfp,
        "Rcomm": Rc,
        "Lloc": Ll,
        "dfd": dfd,
        "dpred": dpred,
        "budget_resid": budget_resid,
        "A_N": Vnp / P,
        "A_F": Vfp / P,
        "g": dpred / P,
        "B_F": Vf / P,
        "B_C": Rc / P,
        "B_L": Ll / P,
    }
    for key, value in values.items():
        if isinstance(value, float) and not math.isfinite(value):
            raise RuntimeError(f"N={g.N} R={R} sigma={sigma}: nonfinite {key}")

    del Uh, Oh, U, Om, S, gradO2, Gh, Sfar, q_total, q_far, q_near, O2
    del cdt, Oh1, Om1, O2_1
    gc.collect()
    return values


def run_grid(N: int) -> dict:
    if N not in GRIDS:
        raise ValueError(f"N must be one of {GRIDS}")
    _validate_mode_table()
    g = ev.Grid(N)
    out = {
        "classification": "NUMERICAL CALIBRATION / EVIDENCE-GRADE ONLY",
        "N": N,
        "nu": NU,
        "dt_cal": DT_CAL,
        "rho": RHO,
        "radii": list(RADII),
        "sigmas": list(SIGMAS),
        "divergence_tolerance": DIV_TOL,
        "fields": {},
    }
    idx = (0, 0, 0)
    for name in MANUFACTURED:
        uh, div_max = manufactured_uh(g, name)
        uh1 = g.step(uh, NU, DT_CAL)
        rows = []
        for R in RADII:
            chi, gchi, lchi = cutoff(g, idx, R)
            for sigma in SIGMAS:
                rows.append(_cell(g, uh, uh1, chi, gchi, lchi, R, sigma))
            # far-kernel cache is useful across the two sigma values at fixed R but is deliberately
            # released before the next radius to keep N=192 peak/resident memory bounded.
            nf._kernel_cache.clear()
            del chi, gchi, lchi
            gc.collect()
        out["fields"][name] = {"fourier_divergence_max": div_max, "cells": rows}
        del uh, uh1
        gc.collect()
    return out


def ell_bin(x: float) -> str:
    if x < 1.0:
        return "B0"
    if x < 2.0:
        return "B1"
    if x < 3.0:
        return "B2"
    if x < 4.0:
        return "B3"
    return "B4"


def _cell_index(d: dict) -> dict[tuple[str, str, str], dict]:
    out = {}
    for field, fd in d["fields"].items():
        for cell in fd["cells"]:
            # Decimal-string keys avoid relying on exact binary equality across JSON loads.
            key = (field, f"{float(cell['R']):.16g}", f"{float(cell['sigma']):.16g}")
            if key in out:
                raise RuntimeError(f"duplicate cell {key}")
            out[key] = cell
    return out


def aggregate(directory: Path) -> dict:
    data = {}
    for N in GRIDS:
        p = directory / f"N{N}.json"
        if not p.exists():
            raise FileNotFoundError(p)
        d = json.loads(p.read_text())
        if int(d["N"]) != N:
            raise RuntimeError(f"{p}: N mismatch")
        data[N] = d

    idx = {N: _cell_index(d) for N, d in data.items()}
    keys = sorted(idx[REF2])
    for N in GRIDS:
        if set(idx[N]) != set(keys):
            raise RuntimeError(f"N={N}: manufactured cell set differs from N={REF2}")

    envelopes = {b: {q: [] for q in QUANTITIES} | {"budget_resid": []} for b in ("B0", "B1", "B2", "B3", "B4")}
    records = []
    for N in COARSE_GRIDS:
        for key in keys:
            c = idx[N][key]
            c160 = idx[REF1][key]
            c192 = idx[REF2][key]
            b = ell_bin(float(c["ell_over_dx"]))
            rec = {
                "N": N,
                "field": key[0],
                "R": float(c["R"]),
                "sigma": float(c["sigma"]),
                "ell_over_dx": float(c["ell_over_dx"]),
                "bin": b,
                "errors": {},
            }
            for q in QUANTITIES:
                vals = (float(c[q]), float(c160[q]), float(c192[q]))
                if not all(math.isfinite(v) for v in vals):
                    raise RuntimeError(f"reference/coarse nonfinite {q} at {key}, N={N}")
                err = abs(vals[0] - vals[2]) + abs(vals[1] - vals[2])
                rec["errors"][q] = err
                envelopes[b][q].append(err)
            vals = tuple(float(x["budget_resid"]) for x in (c, c160, c192))
            if not all(math.isfinite(v) for v in vals):
                raise RuntimeError(f"reference/coarse nonfinite budget_resid at {key}, N={N}")
            berr = abs(vals[0] - vals[2]) + abs(vals[1] - vals[2])
            rec["errors"]["budget_resid"] = berr
            envelopes[b]["budget_resid"].append(berr)
            records.append(rec)

    frozen = {}
    for b, qs in envelopes.items():
        frozen[b] = {}
        for q, vals in qs.items():
            frozen[b][q] = {
                "n": len(vals),
                "epsilon": max(vals) if vals else None,
                "mean_error": sum(vals) / len(vals) if vals else None,
            }

    # Reference-pair disagreement is always reported; it is never used to censor a finite cell.
    ref_diffs = {q: [] for q in QUANTITIES + ("budget_resid",)}
    for key in keys:
        for q in QUANTITIES + ("budget_resid",):
            a, b = float(idx[REF1][key][q]), float(idx[REF2][key][q])
            ref_diffs[q].append(abs(a - b))
    ref_summary = {
        q: {"max_abs": max(v), "mean_abs": sum(v) / len(v)} for q, v in ref_diffs.items()
    }

    return {
        "classification": "NUMERICAL CALIBRATION / EMPIRICAL ERROR ENVELOPE ONLY",
        "coarse_grids": list(COARSE_GRIDS),
        "reference_pair": [REF1, REF2],
        "reference_grid": REF2,
        "bin_definition": {
            "B0": "ell/dx < 1",
            "B1": "1 <= ell/dx < 2",
            "B2": "2 <= ell/dx < 3",
            "B3": "3 <= ell/dx < 4",
            "B4": "ell/dx >= 4",
        },
        "quantities": list(QUANTITIES),
        "frozen_envelopes": frozen,
        "reference_pair_absolute_difference": ref_summary,
        "cell_error_records": records,
        "decision_boundary": (
            "Empirical manufactured-field envelope only; not a rigorous continuum error bound. "
            "No E3c/E4c production values were used to choose bins or epsilon values."
        ),
    }


def main(argv: list[str]) -> None:
    if len(argv) < 2:
        raise SystemExit("usage: filter_resolution_calibration.py run N OUT.json | aggregate DIR OUT.json")
    mode = argv[1]
    if mode == "run":
        if len(argv) != 4:
            raise SystemExit("usage: ... run N OUT.json")
        N = int(argv[2])
        out = run_grid(N)
        p = Path(argv[3]); p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(out, indent=2, allow_nan=False))
        ncells = sum(len(fd["cells"]) for fd in out["fields"].values())
        print(f"N={N}: calibration cells={ncells} fields={len(out['fields'])}")
        for name, fd in out["fields"].items():
            print(f"  {name}: Fourier div max={fd['fourier_divergence_max']:.3e}")
        return
    if mode == "aggregate":
        if len(argv) != 4:
            raise SystemExit("usage: ... aggregate DIR OUT.json")
        out = aggregate(Path(argv[2]))
        p = Path(argv[3]); p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(out, indent=2, allow_nan=False))
        for b, qs in out["frozen_envelopes"].items():
            print(b, {q: row["epsilon"] for q, row in qs.items()})
        return
    raise SystemExit(f"unknown mode {mode}")


if __name__ == "__main__":
    main(sys.argv)
