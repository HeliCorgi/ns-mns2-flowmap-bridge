#!/usr/bin/env python3
import json
import subprocess
import sys
import tempfile
from pathlib import Path

repo = Path(__file__).resolve().parents[1]
runner = repo / "src" / "bridge" / "mns2_predictive_path_pod_bridge_v2.12.py"
generator = repo / "tests" / "data" / "generate_mns2_synthetic_seed_v2_2.py"
meta = repo / "tests" / "data" / "MNS2_SYNTHETIC_2COMP_BRIDGE_META_V2.2.json"
schedule = repo / "tests" / "data" / "MNS2_SYNTHETIC_2COMP_BRIDGE_SCHEDULE_V2.2.json"

with tempfile.TemporaryDirectory(prefix="mns2_v212_ci_") as td:
    td = Path(td)
    seed = td / "MNS2_SYNTHETIC_2COMP_BRIDGE_SEED_V2.2.npz"
    out = td / "v212"
    subprocess.run([sys.executable, str(generator), str(seed)], check=True, stdout=subprocess.DEVNULL)
    subprocess.run([
        sys.executable, str(runner), str(seed), str(meta), str(schedule),
        "--out", str(out),
    ], check=True, stdout=subprocess.DEVNULL)
    d = json.loads(Path(str(out) + ".json").read_text())

assert d["status"] == "PREDICTIVE-PATH-POD-BRIDGE-AUDIT-COMPLETE"
assert d["stack_audit"]["status"] == "STACK-COMPLETE"
assert d["rank"] == 4
assert d["training_amplitudes"] == [0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 0.75, 1.0]
assert abs(d["direct_endpoint_delta_metric_norm"] - 0.8948215172977055) < 5e-10

inv = d["important_invariants"]
for key in [
    "predictor_formed_before_true_JVP_at_certification_nodes",
    "coefficient_models_use_training_nodes_only",
    "certification_nodes_are_held_out_from_training",
    "same_frozen_schedule_all_amplitudes",
    "path_direction_fixed_unnormalized_y0",
    "synthetic_seed_not_Hou_late_state",
    "no_discrete_to_continuum_promotion",
    "residual_integral_is_quadrature_estimate_not_rigorous_enclosure",
]:
    assert inv[key] is True

f = d["final_record"]
assert f["panels"] == 12
assert f["true_bridge_rel_error_vs_direct"] < 2e-8
assert f["predictive_endpoint_rel_error_vs_direct"] < 3e-8
assert f["predictive_vs_true_integral_rel_direct"] < 3e-8
assert f["quadrature_residual_integral_rel_direct"] < 6e-8
assert f["numerical_triangle_ratio"] <= 1.05
assert f["predictive_quadrature_drift_from_previous"] < 1e-8

print("v2.12 predictive reproducibility smoke: PASS")
