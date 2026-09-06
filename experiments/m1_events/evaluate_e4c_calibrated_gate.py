"""Evaluate the preregistered E4c frozen-calibration cross-datum gate.

The primary row is fixed before E4c execution to (c,sigma)=(16,0.125).  This script does not
search the ladder for a more favorable row.  It consumes only the output of
certify_nearfar_with_calibration.py and emits the predeclared GO_TO_DT2 vs STOP/PARK decision.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

PRIMARY_KEY = "c=16,sigma=0.125"
GO = "GO_TO_DT2"
STOP = "STOP_PARK_FILTERED_NEARFAR"


def evaluate(d: dict) -> dict:
    if not d.get("classification", "").startswith("NUMERICAL OBSERVATION / FROZEN-CALIBRATION"):
        raise ValueError("unexpected certification classification")
    if d.get("lo", {}).get("name") != "E4c96" or int(d.get("lo", {}).get("N", -1)) != 96:
        raise ValueError("low-grid input is not E4c96/N96")
    if d.get("hi", {}).get("name") != "E4c128" or int(d.get("hi", {}).get("N", -1)) != 128:
        raise ValueError("high-grid input is not E4c128/N128")
    if d.get("envelope_reference_pair") != [160, 192]:
        raise ValueError("unexpected frozen calibration reference pair")

    times = list(d.get("common_positive_global_growth_times", []))
    row = d.get("combos", {}).get(PRIMARY_KEY)
    if row is None:
        return {
            "classification": "NUMERICAL OBSERVATION / PREREGISTERED E4c GATE ONLY",
            "primary_row": PRIMARY_KEY,
            "decision": STOP,
            "reasons": ["primary row absent from certification output"],
            "common_positive_global_growth_times": times,
            "primary_pair_counts": {},
            "primary_n": 0,
        }

    n = int(row.get("n_common_positive_global_growth_samples_with_combo", 0))
    pairs = dict(row.get("pair_counts", {}))
    farfar = int(pairs.get("FAR->FAR", 0))
    reasons = []
    if not times:
        reasons.append("no common positive-forward global-enstrophy time")
    if n <= 0:
        reasons.append("primary row has no common positive-growth sample")
    if farfar != n:
        reasons.append(f"primary row is not all FAR->FAR ({farfar}/{n})")
    other_pairs = {k: v for k, v in pairs.items() if k != "FAR->FAR" and int(v) != 0}
    if other_pairs:
        reasons.append(f"primary row contains non-FAR/FAR outcomes: {other_pairs}")

    # FAR certification itself guarantees calibration coverage, positive local growth,
    # near-field absorption, signed-residual positivity, and pairwise winner separation.
    decision = GO if not reasons else STOP
    return {
        "classification": "NUMERICAL OBSERVATION / PREREGISTERED E4c GATE ONLY",
        "primary_row": PRIMARY_KEY,
        "decision": decision,
        "reasons": reasons,
        "common_positive_global_growth_times": times,
        "primary_pair_counts": pairs,
        "primary_n": n,
        "primary_far_far": farfar,
        "all_combo_same_certified_residual_counts": d.get("all_combo_same_certified_residual_counts", {}),
        "decision_boundary": (
            "The primary row was frozen to (16,0.125) before E4c execution. "
            "No secondary row can replace it for GO_TO_DT2."
        ),
    }


def main(argv: list[str]) -> None:
    if len(argv) != 3:
        raise SystemExit("usage: evaluate_e4c_calibrated_gate.py CERT.json OUT.json")
    d = json.loads(Path(argv[1]).read_text())
    out = evaluate(d)
    p = Path(argv[2])
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, allow_nan=False))
    print(f"decision={out['decision']}")
    print(f"primary_row={out['primary_row']} farfar={out.get('primary_far_far', 0)}/{out['primary_n']}")
    if out["reasons"]:
        for reason in out["reasons"]:
            print(f"reason: {reason}")


if __name__ == "__main__":
    main(sys.argv)
