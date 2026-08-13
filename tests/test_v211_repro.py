#!/usr/bin/env python3
import json
import subprocess
import sys
import tempfile
from pathlib import Path

repo = Path(__file__).resolve().parents[1]
runner = repo / "src" / "bridge" / "mns2_path_correction_pod_bridge_v2.11.py"
seed = repo / "tests" / "data" / "MNS2_SYNTHETIC_2COMP_BRIDGE_SEED_V2.2.npz"
meta = repo / "tests" / "data" / "MNS2_SYNTHETIC_2COMP_BRIDGE_META_V2.2.json"
schedule = repo / "tests" / "data" / "MNS2_SYNTHETIC_2COMP_BRIDGE_SCHEDULE_V2.2.json"

with tempfile.TemporaryDirectory(prefix="mns2_v211_ci_") as td:
    out = Path(td) / "v211"
    subprocess.run([
        sys.executable, str(runner), str(seed), str(meta), str(schedule),
        "--out", str(out),
    ], check=True, stdout=subprocess.DEVNULL)
    d = json.loads(Path(str(out) + ".json").read_text())

assert d["status"] == "PATH-CORRECTION-POD-BRIDGE-AUDIT-COMPLETE"
assert d["stack_audit"]["status"] == "STACK-COMPLETE"
assert abs(d["direct_endpoint_delta_metric_norm"] - 0.8948215172977055) < 5e-10
assert d["basis_metric_gram_max_error"] < 1e-8

f = d["final_record"]
assert f["panels"] == 12
assert f["true_bridge_rel_error_vs_direct"] < 2e-8
r2 = f["ranks"]["2"]
assert r2["reduced_endpoint_rel_error_vs_direct"] < 2e-8
assert r2["reduced_vs_true_integral_rel_direct"] < 2e-8
assert r2["quadrature_residual_integral_rel_direct"] < 5e-8
assert r2["reduced_vs_true_integral_abs_error"] <= 1.05 * r2["quadrature_residual_integral_abs"]
assert r2["numerical_triangle_ratio"] <= 1.05

inv = d["important_invariants"]
for key in [
    "same_frozen_schedule_all_amplitudes",
    "path_direction_fixed_unnormalized_y0",
    "POD_compresses_only_path_specific_nonlinear_correction",
    "synthetic_seed_not_Hou_late_state",
    "no_discrete_to_continuum_promotion",
]:
    assert inv[key] is True

print("v2.11 reproducibility smoke: PASS")
