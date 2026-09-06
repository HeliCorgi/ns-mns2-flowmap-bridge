"""Apply the preregistered manufactured filter-resolution envelope to production near/far JSON.

This script does not fit a tolerance to production data.  It implements exactly the margin rules in
M1_FILTER_RESOLUTION_CALIBRATION_PREREG_2026-09-06.md plus its addenda.

Usage:
  python certify_nearfar_with_calibration.py ENVELOPE.json LO.json HI.json OUT.json

The two production runs are compared only on common sampled times where global enstrophy has a
positive forward increment on both grids.  A residual label counts as a certified mechanism label
only when each grid independently clears growth, near-absorption, coverage and signed-residual
margin tests.
"""
from __future__ import annotations

import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path

RESIDUALS = ("FAR", "COMM", "LOC")
EPS_KEY = {"FAR": "B_F", "COMM": "B_C", "LOC": "B_L"}


def _time_key(t: float) -> float:
    return round(float(t), 10)


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


def _eps(envelope: dict, b: str, q: str) -> float | None:
    row = envelope["frozen_envelopes"][b][q]
    value = row.get("epsilon")
    if value is None or int(row.get("n", 0)) <= 0:
        return None
    value = float(value)
    if not math.isfinite(value) or value < 0.0:
        raise ValueError(f"invalid epsilon {b}/{q}: {row}")
    return value


def certify_filter(envelope: dict, filt: dict) -> dict:
    ell_dx = float(filt["ell_over_dx"])
    b = ell_bin(ell_dx)
    eps_an = _eps(envelope, b, "A_N")
    eps_g = _eps(envelope, b, "g")
    eps_bf = _eps(envelope, b, "B_F")
    eps_bc = _eps(envelope, b, "B_C")
    eps_bl = _eps(envelope, b, "B_L")
    eps = {"FAR": eps_bf, "COMM": eps_bc, "LOC": eps_bl}

    p = float(filt["P"])
    vals = [ell_dx, p, float(filt["g"]), float(filt["A_N"]),
            float(filt["V_far"]), float(filt["Rcomm"]), float(filt["Lloc"])]
    if not all(math.isfinite(v) for v in vals) or p <= 0.0:
        return {"label": "NONFINITE_OR_BAD_P", "bin": b, "ell_over_dx": ell_dx}

    if any(v is None for v in (eps_an, eps_g, eps_bf, eps_bc, eps_bl)):
        return {
            "label": "NUMERICALLY_UNCERTIFIED_RESOLUTION",
            "bin": b,
            "ell_over_dx": ell_dx,
        }

    g = float(filt["g"])
    an = float(filt["A_N"])
    scores = {
        "FAR": float(filt["V_far"]) / p,
        "COMM": float(filt["Rcomm"]) / p,
        "LOC": float(filt["Lloc"]) / p,
    }

    # Frozen local-growth sign rule.  All covered eps_g are strictly positive in the frozen result.
    if g <= -eps_g:
        return {
            "label": "NO_POSITIVE_LOCAL_GROWTH",
            "bin": b,
            "ell_over_dx": ell_dx,
            "g": g,
            "eps_g": eps_g,
        }
    if g < eps_g:
        return {
            "label": "NUMERICALLY_AMBIGUOUS_G",
            "bin": b,
            "ell_over_dx": ell_dx,
            "g": g,
            "eps_g": eps_g,
        }

    # Frozen near-field absorption rule around A_N = 1.
    if an >= 1.0 + eps_an:
        return {
            "label": "NEAR_NOT_ABSORBED",
            "bin": b,
            "ell_over_dx": ell_dx,
            "g": g,
            "A_N": an,
            "eps_A_N": eps_an,
        }
    if an > 1.0 - eps_an:
        return {
            "label": "NUMERICALLY_AMBIGUOUS_NEAR",
            "bin": b,
            "ell_over_dx": ell_dx,
            "g": g,
            "A_N": an,
            "eps_A_N": eps_an,
        }

    # Signed residual-winner margin rule.  A_F is deliberately not used here.
    winners = []
    for j in RESIDUALS:
        ej = eps[j]
        assert ej is not None
        if scores[j] <= ej:
            continue
        separated = True
        for k in RESIDUALS:
            if k == j:
                continue
            ek = eps[k]
            assert ek is not None
            if scores[j] - scores[k] <= ej + ek:
                separated = False
                break
        if separated:
            winners.append(j)

    if len(winners) == 1:
        label = winners[0]
    elif len(winners) == 0:
        label = "NUMERICALLY_AMBIGUOUS_RESIDUAL"
    else:
        # Strict pairwise inequalities should make this impossible; fail closed if floating data
        # somehow creates an inconsistent result.
        label = "INCONSISTENT_MULTIPLE_WINNERS"

    return {
        "label": label,
        "bin": b,
        "ell_over_dx": ell_dx,
        "g": g,
        "A_N": an,
        "scores": scores,
        "eps": {"A_N": eps_an, "g": eps_g, **eps},
    }


def _snap_index(d: dict) -> dict[float, dict]:
    if len(d["t"]) != len(d["snap"]):
        raise ValueError("time/snapshot length mismatch")
    out = {}
    for t, snap in zip(d["t"], d["snap"]):
        k = _time_key(t)
        if k in out:
            raise ValueError(f"duplicate time {k}")
        out[k] = snap
    return out


def positive_forward_times(d: dict) -> set[float]:
    ts = [_time_key(t) for t in d["t"]]
    es = [float(s["E"]) for s in d["snap"]]
    return {ts[i] for i in range(len(es) - 1) if es[i + 1] > es[i]}


def _combo_index(snap: dict) -> dict[tuple[float, float], dict]:
    out = {}
    for row in snap.get("ladder", []):
        c = float(row["c"])
        for filt in row.get("filters", []):
            key = (c, float(filt["sigma"]))
            if key in out:
                raise ValueError(f"duplicate combo {key}")
            out[key] = filt
    return out


def compare(envelope: dict, lo: dict, hi: dict) -> dict:
    if lo["name"] == hi["name"]:
        raise ValueError("expected distinct resolution run names")
    if float(lo["nu"]) != float(hi["nu"]) or float(lo["T"]) != float(hi["T"]):
        raise ValueError("production runs do not share nu/T")

    ilo, ihi = _snap_index(lo), _snap_index(hi)
    grow = positive_forward_times(lo) & positive_forward_times(hi)
    common_growth = sorted(grow & set(ilo) & set(ihi))

    by_combo = defaultdict(lambda: {
        "pairs": Counter(),
        "lo_labels": Counter(),
        "hi_labels": Counter(),
        "samples": [],
    })

    for t in common_growth:
        clo = _combo_index(ilo[t])
        chi = _combo_index(ihi[t])
        for combo in sorted(set(clo) & set(chi)):
            a = certify_filter(envelope, clo[combo])
            b = certify_filter(envelope, chi[combo])
            key = f"c={combo[0]:g},sigma={combo[1]:g}"
            rec = by_combo[key]
            rec["pairs"][(a["label"], b["label"])] += 1
            rec["lo_labels"][a["label"]] += 1
            rec["hi_labels"][b["label"]] += 1
            rec["samples"].append({"t": t, "lo": a, "hi": b})

    combos = {}
    total_same_certified = Counter()
    for key in sorted(by_combo):
        rec = by_combo[key]
        pairs = rec["pairs"]
        certified_same = {r: pairs[(r, r)] for r in RESIDUALS if pairs[(r, r)]}
        for r, n in certified_same.items():
            total_same_certified[r] += n
        combos[key] = {
            "n_common_positive_global_growth_samples_with_combo": sum(pairs.values()),
            "pair_counts": {f"{a}->{b}": n for (a, b), n in sorted(pairs.items())},
            "lo_label_counts": dict(rec["lo_labels"]),
            "hi_label_counts": dict(rec["hi_labels"]),
            "same_certified_residual_counts": certified_same,
            "samples": rec["samples"],
        }

    return {
        "classification": "NUMERICAL OBSERVATION / FROZEN-CALIBRATION CERTIFICATION ONLY",
        "envelope_reference_pair": envelope.get("reference_pair"),
        "lo": {"name": lo["name"], "N": lo["N"], "dt": lo["dt"]},
        "hi": {"name": hi["name"], "N": hi["N"], "dt": hi["dt"]},
        "common_positive_global_growth_times": common_growth,
        "combos": combos,
        "all_combo_same_certified_residual_counts": dict(total_same_certified),
        "decision_boundary": (
            "Labels are certified only by the frozen manufactured envelope. B3 is uncovered. "
            "No percentage or post-hoc ell/dx cutoff is applied. A_F is not used as the FAR score."
        ),
    }


def main(argv: list[str]) -> None:
    if len(argv) != 5:
        raise SystemExit("usage: certify_nearfar_with_calibration.py ENVELOPE.json LO.json HI.json OUT.json")
    envelope = json.loads(Path(argv[1]).read_text())
    lo = json.loads(Path(argv[2]).read_text())
    hi = json.loads(Path(argv[3]).read_text())
    out = compare(envelope, lo, hi)
    p = Path(argv[4])
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, allow_nan=False))
    print(f"common_positive_global_growth_times={out['common_positive_global_growth_times']}")
    for key, row in out["combos"].items():
        print(f"{key}: n={row['n_common_positive_global_growth_samples_with_combo']} pairs={row['pair_counts']}")
        print(f"  same_certified={row['same_certified_residual_counts']}")
    print(f"all_combo_same_certified={out['all_combo_same_certified_residual_counts']}")


if __name__ == "__main__":
    main(sys.argv)
