"""Threshold-free R2 comparison for two tail-qualified M-1 near/far runs.

This script does not decide numerical convergence by a fitted percentage tolerance.  It implements
only comparisons already preregistered in M1_RESOLUTION_RESCUE_PREREG_2026-09-06.md:

* enstrophy-growth intervals at the common 0.1-time outputs;
* max vorticity / enstrophy and the filtered near/far axes;
* residual-class labels on common positive-growth samples;
* R/dx, ell/dx and filtered-budget residuals.

The residual label is defined before looking at the E3c96/E3c128 outputs.  At a sample/filter:

1. if g <= 0, label NO_POSITIVE_LOCAL_GROWTH;
2. if A_N >= 1, label NEAR_NOT_ABSORBED;
3. otherwise choose the largest strictly positive *signed budget* contribution among
   V_far, Rcomm and Lloc, labelled FAR / COMM / LOC respectively;
4. exact equal maxima are reported as TIE(...), and absence of a positive residual is NONE.

No numerical closeness threshold is introduced here.  Continuous-axis differences are reported,
not passed/failed.  Exact categorical label agreement is reported separately.
"""
from __future__ import annotations

import json
import math
import os
import sys
from collections import Counter, defaultdict
from pathlib import Path

METRICS = ("A_N", "A_F", "A_C", "A_L", "g", "R", "ell", "R_over_dx", "ell_over_dx")


def _finite(x):
    return isinstance(x, (int, float)) and math.isfinite(float(x))


def _sym_rel(a, b):
    a = float(a); b = float(b)
    if not (math.isfinite(a) and math.isfinite(b)):
        return None
    return abs(a - b) / max(abs(a), abs(b), 1.0e-300)


def _time_key(t):
    return round(float(t), 10)


def _time_index(d):
    out = {}
    for t, s in zip(d["t"], d["snap"]):
        k = _time_key(t)
        if k in out:
            raise ValueError(f"duplicate output time {k}")
        out[k] = s
    return out


def growth_events(d):
    ts = [_time_key(t) for t in d["t"]]
    es = [float(s["E"]) for s in d["snap"]]
    if len(ts) != len(es):
        raise ValueError("time/snapshot length mismatch")
    flags = [es[i + 1] > es[i] for i in range(len(es) - 1)]
    events = []
    i = 0
    while i < len(flags):
        if not flags[i]:
            i += 1
            continue
        j = i
        while j + 1 < len(flags) and flags[j + 1]:
            j += 1
        events.append({
            "t_start": ts[i],
            "t_end": ts[j + 1],
            "E_start": es[i],
            "E_end": es[j + 1],
            "gain": es[j + 1] - es[i],
            "relative_gain": (es[j + 1] - es[i]) / max(abs(es[i]), 1.0e-300),
        })
        i = j + 1
    positive_forward_times = {ts[i] for i, flag in enumerate(flags) if flag}
    return events, positive_forward_times


def _rows_by_c(snap):
    return {float(row["c"]): row for row in snap.get("ladder", [])}


def _filters_by_sigma(row):
    return {float(f["sigma"]): f for f in row.get("filters", [])}


def residual_label(f):
    g = float(f["g"])
    an = float(f["A_N"])
    if not math.isfinite(g) or not math.isfinite(an):
        return "NONFINITE"
    if g <= 0.0:
        return "NO_POSITIVE_LOCAL_GROWTH"
    if an >= 1.0:
        return "NEAR_NOT_ABSORBED"
    vals = {
        "FAR": float(f["V_far"]),
        "COMM": float(f["Rcomm"]),
        "LOC": float(f["Lloc"]),
    }
    pos = {k: v for k, v in vals.items() if math.isfinite(v) and v > 0.0}
    if not pos:
        return "NONE"
    vmax = max(pos.values())
    winners = sorted(k for k, v in pos.items() if v == vmax)
    return winners[0] if len(winners) == 1 else "TIE(" + ",".join(winners) + ")"


def _metric_summary(values):
    vals = [v for v in values if v is not None and math.isfinite(v)]
    if not vals:
        return {"n": 0, "max": None, "mean": None}
    return {"n": len(vals), "max": max(vals), "mean": sum(vals) / len(vals)}


def compare(lo, hi):
    if lo["name"] == hi["name"]:
        raise ValueError("expected two different resolution run names")
    if float(lo["nu"]) != float(hi["nu"]) or float(lo["T"]) != float(hi["T"]):
        raise ValueError("runs do not share nu/T")

    ilo, ihi = _time_index(lo), _time_index(hi)
    common = sorted(set(ilo) & set(ihi))
    if not common:
        raise ValueError("no common output times")

    ev_lo, grow_lo = growth_events(lo)
    ev_hi, grow_hi = growth_events(hi)
    common_growth = sorted((grow_lo & grow_hi) & set(common))

    global_rel = defaultdict(list)
    combo_rel = defaultdict(lambda: defaultdict(list))
    combo_budget_abs = defaultdict(list)
    combo_labels = defaultdict(lambda: {"lo": Counter(), "hi": Counter(), "pairs": Counter(), "mismatches": []})
    combo_grid = defaultdict(lambda: {"Rdx_lo": [], "Rdx_hi": [], "elldx_lo": [], "elldx_hi": []})
    common_combo_counts = Counter()

    for t in common:
        slo, shi = ilo[t], ihi[t]
        for key in ("E", "Lam", "sv"):
            global_rel[key].append(_sym_rel(slo[key], shi[key]))

        rlo, rhi = _rows_by_c(slo), _rows_by_c(shi)
        for c in sorted(set(rlo) & set(rhi)):
            flo, fhi = _filters_by_sigma(rlo[c]), _filters_by_sigma(rhi[c])
            for sig in sorted(set(flo) & set(fhi)):
                key = f"c={c:g},sigma={sig:g}"
                common_combo_counts[key] += 1
                a, b = flo[sig], fhi[sig]
                # filter-level metrics
                for m in ("A_N", "A_F", "A_C", "A_L", "g"):
                    combo_rel[key][m].append(_sym_rel(a[m], b[m]))
                combo_rel[key]["R"].append(_sym_rel(rlo[c]["R"], rhi[c]["R"]))
                combo_rel[key]["ell"].append(_sym_rel(a["ell"], b["ell"]))
                combo_budget_abs[key].append(abs(float(a["budget_resid"]) - float(b["budget_resid"])))
                combo_grid[key]["Rdx_lo"].append(float(rlo[c]["R_over_dx"]))
                combo_grid[key]["Rdx_hi"].append(float(rhi[c]["R_over_dx"]))
                combo_grid[key]["elldx_lo"].append(float(a["ell_over_dx"]))
                combo_grid[key]["elldx_hi"].append(float(b["ell_over_dx"]))

                if t in common_growth:
                    la, lb = residual_label(a), residual_label(b)
                    rec = combo_labels[key]
                    rec["lo"][la] += 1
                    rec["hi"][lb] += 1
                    rec["pairs"][(la, lb)] += 1
                    if la != lb:
                        rec["mismatches"].append({"t": t, "lo": la, "hi": lb})

    combos = {}
    for key in sorted(common_combo_counts):
        labels = combo_labels[key]
        nlab = sum(labels["pairs"].values())
        ngr = combo_grid[key]
        combos[key] = {
            "common_time_samples": common_combo_counts[key],
            "continuous_symmetric_relative_difference": {
                m: _metric_summary(vs) for m, vs in combo_rel[key].items()
            },
            "filtered_budget_residual_absolute_difference": _metric_summary(combo_budget_abs[key]),
            "grid_resolution_samples": {
                k: {"min": min(v) if v else None, "max": max(v) if v else None}
                for k, v in ngr.items()
            },
            "common_positive_global_growth_samples": nlab,
            "residual_labels_lo": dict(labels["lo"]),
            "residual_labels_hi": dict(labels["hi"]),
            "residual_label_pairs": {f"{a}->{b}": n for (a, b), n in labels["pairs"].items()},
            "residual_label_exact_agreement_count": nlab - len(labels["mismatches"]),
            "residual_label_mismatches": labels["mismatches"],
        }

    return {
        "classification": "NUMERICAL OBSERVATION / THRESHOLD-FREE R2 COMPARISON ONLY",
        "lo": {"name": lo["name"], "N": lo["N"], "dt": lo["dt"]},
        "hi": {"name": hi["name"], "N": hi["N"], "dt": hi["dt"]},
        "common_times": common,
        "growth_events_lo": ev_lo,
        "growth_events_hi": ev_hi,
        "common_positive_global_growth_times": common_growth,
        "global_symmetric_relative_difference": {k: _metric_summary(v) for k, v in global_rel.items()},
        "combos": combos,
        "decision_boundary": (
            "No percentage convergence tolerance is applied here. Exact categorical label agreement and raw/relative "
            "continuous-axis differences are reported for later manufactured-test-first tolerance work."
        ),
    }


def main(argv):
    if len(argv) != 4:
        raise SystemExit("usage: compare_nearfar_refinement.py LO.json HI.json OUT.json")
    lo = json.loads(Path(argv[1]).read_text())
    hi = json.loads(Path(argv[2]).read_text())
    out = compare(lo, hi)
    p = Path(argv[3]); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, allow_nan=True))
    print(f"common_times={len(out['common_times'])}")
    print(f"growth_events_lo={out['growth_events_lo']}")
    print(f"growth_events_hi={out['growth_events_hi']}")
    print(f"common_positive_global_growth_samples={len(out['common_positive_global_growth_times'])}")
    for key, row in out["combos"].items():
        n = row["common_positive_global_growth_samples"]
        a = row["residual_label_exact_agreement_count"]
        print(f"{key}: label_agreement={a}/{n} pairs={row['residual_label_pairs']}")
        for m in ("A_N", "A_F", "A_C", "A_L", "g", "R", "ell"):
            s = row["continuous_symmetric_relative_difference"].get(m, {})
            print(f"  {m}: rel_max={s.get('max')} rel_mean={s.get('mean')}")
        print(f"  budget_resid_abs={row['filtered_budget_residual_absolute_difference']}")


if __name__ == "__main__":
    main(sys.argv)
