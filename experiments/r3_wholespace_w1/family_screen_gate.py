#!/usr/bin/env python3
"""Production decision wrapper for the preregistered R3 family screen.

The underlying implementation records every row. This wrapper enforces the
preregistered overall rule exactly: INVALID_RUNTIME and INVALID_DOMAIN rows do
not count as valid screen rows.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import family_screen as fs


def run_gate():
    result = fs.run_gate()
    rows = dict(result["rows"])
    usable = [
        key for key, row in rows.items()
        if row["classification"] in ("NO_GROWTH_TRIGGER", "PROMOTE_HIGH_RES")
    ]
    promotions = list(result["promotion_set"])
    result["valid_row_count"] = len(usable)
    result["valid_rows"] = usable
    if not usable:
        result["decision"] = "STOP_REPAIR_SCREEN"
        result["pass"] = False
    elif promotions:
        result["decision"] = "PASS_WITH_PROMOTIONS"
        result["pass"] = True
    else:
        result["decision"] = "PASS_NO_PROMOTIONS"
        result["pass"] = True
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("experiments/r3_wholespace_w1/results/FAMILY_SCREEN.json"))
    args = parser.parse_args()
    result = run_gate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"decision": result["decision"], "valid_rows": result["valid_rows"], "promotions": result["promotion_set"], "output": str(args.output)}, indent=2))
    return 0 if result["pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
