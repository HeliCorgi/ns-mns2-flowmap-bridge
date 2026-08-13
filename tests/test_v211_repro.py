#!/usr/bin/env python3
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np

repo = Path(__file__).resolve().parents[1]
runner = repo / "src" / "bridge" / "mns2_path_correction_pod_bridge_v2.11.py"
generator = repo / "tests" / "data" / "generate_mns2_synthetic_seed_v2_2.py"
meta = repo / "tests" / "data" / "MNS2_SYNTHETIC_2COMP_BRIDGE_META_V2.2.json"
schedule = repo / "tests" / "data" / "MNS2_SYNTHETIC_2COMP_BRIDGE_SCHEDULE_V2.2.json"


def canonical_seed_content_hash(path: Path) -> str:
    d = np.load(path)
    h = hashlib.sha256()
    for key in sorted(d.files):
        a = np.ascontiguousarray(d[key])
        h.update(key.encode() + b"\0")
        h.update(a.dtype.str.encode() + b"\0")
        h.update(str(a.shape).encode() + b"\0")
        h.update(a.tobytes(order="C"))
    return h.hexdigest()


with tempfile.TemporaryDirectory(prefix="mns2_v211_ci_") as td:
    td = Path(td)
    seed = td / "MNS2_SYNTHETIC_2COMP_BRIDGE_SEED_V2.2.npz"
    out = td / "v211"

    subprocess.run([sys.executable, str(generator), str(seed)], check=True)
    expected_content_hash = json.loads(schedule.read_text())["seed_content_sha256"]
    content_hash = canonical_seed_content_hash(seed)
    print("seed canonical content sha256:", content_hash, flush=True)
    assert content_hash == expected_content_hash

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
