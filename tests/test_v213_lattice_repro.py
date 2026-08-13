#!/usr/bin/env python3
import json
import subprocess
import sys
import tempfile
from pathlib import Path

repo = Path(__file__).resolve().parents[1]
runner = repo / "src" / "lattice" / "mns2_predictive_convergence_lattice_v2.13.py"

with tempfile.TemporaryDirectory(prefix="mns2_v213_ci_") as td:
    out = Path(td) / "v213"
    subprocess.run(
        [sys.executable, str(runner), "--panels", "8", "--rank", "4", "--out", str(out)],
        check=True,
        stdout=subprocess.DEVNULL,
    )
    d = json.loads(Path(str(out) + ".json").read_text())

assert d["status"] == "PREDICTIVE-CONVERGENCE-LATTICE-AUDIT-COMPLETE"
assert d["unique_case_count"] == 7
assert d["axes"]["dt"]["exact_representability_checked"] is True

for axis in ["grid", "dt", "physical_time"]:
    assert len(d["axes"][axis]["records"]) == 3
    for rec in d["axes"][axis]["records"]:
        assert rec["certification_nodes_are_held_out_from_training"] is True
        assert rec["same_frozen_schedule_all_amplitudes"] is True
        assert rec["predictive_endpoint_rel_error_vs_direct"] < 2e-6
        assert rec["predictive_residual_to_true_correction_integral_ratio"] < 0.15
        assert rec["numerical_triangle_ratio"] <= 1.05

for value in d["promotion_guardrails"].values():
    assert value is True

print("v2.13 predictive convergence lattice: PASS")
