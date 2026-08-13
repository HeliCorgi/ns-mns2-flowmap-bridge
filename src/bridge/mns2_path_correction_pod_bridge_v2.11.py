#!/usr/bin/env python3
"""
MNS-2 v2.11 — path-specific nonlinear tangent-correction POD bridge certificate.

For the same frozen finite-dimensional discrete map S_T used by the v2.2 bridge,
write along the radial data path

    g(lambda) = J_T(lambda y0)[y0]
              = g0 + c(lambda),
    g0 = J_T(0)[y0].

A physical-energy POD basis is learned from coarse amplitude snapshots of c(lambda).
For rank r, define

    q_r(lambda) = g0 + P_r c(lambda),

where P_r is the metric-orthogonal projector onto the learned POD space. Composite
Gauss-4 quadrature then compares

    integral g, integral q_r, and integral ||g-q_r||_E

against the direct frozen-map endpoint difference S_T(y0)-S_T(0).

This is a finite-discrete certification experiment. It is not a continuum theorem,
not a universal low-rank solution operator, and not Hou late-state evidence.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path

import numpy as np
from scipy.interpolate import RectBivariateSpline

HERE = Path(__file__).resolve().parent
CORE = HERE.parent / "core"

CANONICAL_STACK = {
    "adjoint": "mns2_full_holomorphic_adjoint_v1.2.py",
    "pilot": "mns2_full_holomorphic_pilot_v1.1.py",
    "core11": "mns2_conservative_lf_weno7_holomorphic_v1.1.py",
    "core10": "mns2_conservative_lf_weno7_holomorphic_v1.0.py",
}
_ADJ_MODULE = None


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def jsonable(obj):
    if isinstance(obj, dict):
        return {str(k): jsonable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [jsonable(v) for v in obj]
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, (np.floating, np.integer, np.bool_)):
        return obj.item()
    return obj


def find_stack_file(stack_dir, canonical):
    stack_dir = Path(stack_dir)
    exact = stack_dir / canonical
    if exact.exists():
        return exact
    stem = canonical[:-3]
    candidates = sorted(stack_dir.glob(stem + "*.py"))
    return candidates[0] if candidates else None


def audit_stack(stack_dir):
    root = Path(stack_dir).resolve()
    records = {}
    complete = True
    for key, canonical in CANONICAL_STACK.items():
        p = find_stack_file(root, canonical)
        if p is None:
            records[key] = {"canonical": canonical, "status": "MISSING"}
            complete = False
        else:
            records[key] = {
                "canonical": canonical,
                "status": "FOUND",
                "source": str(p),
                "sha256": sha256(p),
            }
    return {
        "status": "STACK-COMPLETE" if complete else "STACK-INCOMPLETE",
        "stack_dir": str(root),
        "files": records,
    }


def stage_stack(stack_dir):
    audit = audit_stack(stack_dir)
    if audit["status"] != "STACK-COMPLETE":
        missing = [v["canonical"] for v in audit["files"].values() if v["status"] == "MISSING"]
        raise RuntimeError("MNS runtime stack incomplete; missing: " + ", ".join(missing))
    td = tempfile.TemporaryDirectory(prefix="mns2_v211_stack_")
    dst = Path(td.name)
    for rec in audit["files"].values():
        shutil.copy2(rec["source"], dst / rec["canonical"])
    return td, dst, audit


def load_adjoint_from_staged(staged_dir):
    global _ADJ_MODULE
    path = staged_dir / CANONICAL_STACK["adjoint"]
    spec = importlib.util.spec_from_file_location("mns2_v211_adj12", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot import adjoint stack")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    _ADJ_MODULE = mod
    return mod


def check_meta(path):
    meta = json.load(open(path))
    if not str(meta.get("provenance", "")).strip():
        raise RuntimeError("missing provenance")
    if not bool(meta.get("z_periodic", False)):
        raise RuntimeError("z_periodic=true required")
    if abs(float(meta.get("z_period", 0.0)) - 1.0) > 1e-12:
        raise RuntimeError("current pilot requires z_period=1")
    return meta


def load_shared_schedule(path, seed_hash):
    obj = json.load(open(path))
    if "seed_sha256" in obj and obj["seed_sha256"] != seed_hash:
        raise RuntimeError("shared frozen schedule seed hash mismatch")
    frozen = obj.get("frozen_schedule", obj)
    need = ("alpha_r", "alpha_z", "eps_g", "eps_o")
    if any(k not in frozen for k in need):
        raise RuntimeError("incomplete frozen schedule")
    return {k: float(frozen[k]) for k in need}


def pinterp(sr, sz, F, r, z, L=1.0):
    k = min(4, max(1, len(sz) // 3))
    ze = np.concatenate([sz[-k:] - L, sz, sz[:k] + L])
    Fe = np.concatenate([F[:, -k:], F, F[:, :k]], axis=1)
    return RectBivariateSpline(
        sr, ze, Fe, kx=min(3, len(sr) - 1), ky=min(3, len(ze) - 1), s=0
    )(r, z, grid=True)


def alpha_gate(P, Phi, frozen):
    return _ADJ_MODULE.c.alpha_gate_real(
        Phi, P.r, P.dr, P.dz, frozen["alpha_r"], frozen["alpha_z"]
    )


def evolve_base(P, g0, o0, dt, steps, frozen):
    g, o = g0.copy(), o0.copy()
    for k in range(steps):
        _, Phi, _, _ = P.reconstruct(o)
        if not alpha_gate(P, Phi, frozen)["pass_gate"]:
            raise RuntimeError(f"frozen LF envelope exceeded before base step {k}")
        g, o = P.ssprk3_step(g, o, dt, frozen)
    _, Phi, _, _ = P.reconstruct(o)
    if not alpha_gate(P, Phi, frozen)["pass_gate"]:
        raise RuntimeError("frozen LF envelope exceeded after base evolution")
    return g, o


def add(a, c):
    return a[0] + c[0], a[1] + c[1]


def sub(a, c):
    return a[0] - c[0], a[1] - c[1]


def scale(a, s: float):
    return s * a[0], s * a[1]


def zeros(a):
    return np.zeros_like(a[0]), np.zeros_like(a[1])


def composite_gauss4(panels: int):
    if panels < 1:
        raise ValueError("panels must be positive")
    x, w = np.polynomial.legendre.leggauss(4)
    nodes = []
    weights = []
    h = 1.0 / panels
    for p in range(panels):
        lo = p * h
        hi = (p + 1) * h
        mid = 0.5 * (lo + hi)
        half = 0.5 * h
        nodes.extend(mid + half * x)
        weights.extend(half * w)
    return np.asarray(nodes), np.asarray(weights)


def jvp_at(P, y0, lam: float, dt: float, steps: int, frozen):
    base = scale(y0, lam)
    T = _ADJ_MODULE.WindowPropagator(P, base[0], base[1], dt, steps, frozen, 1, 1)
    for kk, (_, o) in enumerate(T.states):
        _, Phi, _, _ = P.reconstruct(o)
        gate = alpha_gate(P, Phi, frozen)
        if not gate["pass_gate"]:
            raise RuntimeError(f"frozen LF envelope exceeded at lambda={lam:.17g}, step={kk}")
    return T.matvec(y0)


def pod_basis(P, snapshots, rel_floor: float = 1e-13):
    m = len(snapshots)
    Gram = np.empty((m, m), dtype=float)
    for i in range(m):
        for j in range(i, m):
            v = P.metric_inner(snapshots[i], snapshots[j])
            Gram[i, j] = Gram[j, i] = v
    evals, evecs = np.linalg.eigh(Gram)
    order = np.argsort(evals)[::-1]
    evals = np.maximum(evals[order], 0.0)
    evecs = evecs[:, order]
    if evals.size == 0 or evals[0] <= 0:
        return [], evals, Gram
    basis = []
    for k, ev in enumerate(evals):
        if ev <= rel_floor * evals[0]:
            continue
        phi = zeros(snapshots[0])
        for i, snap in enumerate(snapshots):
            phi = add(phi, scale(snap, float(evecs[i, k] / np.sqrt(ev))))
        nrm = P.metric_norm(phi)
        phi = scale(phi, 1.0 / nrm)
        basis.append(phi)
    return basis, evals, Gram


def project(P, basis, c, rank: int):
    out = zeros(c)
    coeffs = []
    for phi in basis[:rank]:
        coeff = P.metric_inner(phi, c)
        coeffs.append(float(coeff))
        out = add(out, scale(phi, coeff))
    return out, coeffs


def rel(P, a, ref):
    return float(P.metric_norm(sub(a, ref))) / max(float(P.metric_norm(ref)), 1e-300)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("seed", nargs="?")
    ap.add_argument("meta", nargs="?")
    ap.add_argument("schedule", nargs="?")
    ap.add_argument("--stack-dir", default=str(CORE))
    ap.add_argument("--grid", default="12x24")
    ap.add_argument("--nu", type=float, default=5e-3)
    ap.add_argument("--dt", type=float, default=2e-8)
    ap.add_argument("--steps", type=int, default=2)
    ap.add_argument("--train", default="0.25,0.5,0.75,1.0")
    ap.add_argument("--panels", default="2,4,6,8,12")
    ap.add_argument("--ranks", default="1,2,3")
    ap.add_argument("--out", default="MNS2_V2.11_PATH_CORRECTION_POD_BRIDGE")
    ap.add_argument("--audit-stack", action="store_true")
    args = ap.parse_args()

    if args.audit_stack:
        out = audit_stack(args.stack_dir)
        print(json.dumps(out, indent=2))
        raise SystemExit(0 if out["status"] == "STACK-COMPLETE" else 2)

    if not args.seed or not args.meta or not args.schedule:
        ap.error("normal mode requires seed, meta, and schedule")

    seed_hash = sha256(args.seed)
    meta = check_meta(args.meta)
    frozen = load_shared_schedule(args.schedule, seed_hash)
    train = [float(x) for x in args.train.split(",") if x.strip()]
    panels_list = [int(x) for x in args.panels.split(",") if x.strip()]
    ranks = [int(x) for x in args.ranks.split(",") if x.strip()]

    td, staged, audit = stage_stack(args.stack_dir)
    try:
        load_adjoint_from_staged(staged)
        nr, nz = map(int, args.grid.split("x"))
        P = _ADJ_MODULE.AdjointPilot(nr, nz, nu=args.nu, alpha_safety=1.5)
        z = (np.arange(nz) + 0.5) * P.dz
        d = np.load(args.seed)
        G = pinterp(d["r"], d["z"], d["Gamma"], P.r, z)
        O = pinterp(d["r"], d["z"], d["omega1"], P.r, z)
        y0 = (G, O)
        zero = zeros(y0)

        target = evolve_base(P, G, O, args.dt, args.steps, frozen)
        zeroT = evolve_base(P, zero[0], zero[1], args.dt, args.steps, frozen)
        direct = sub(target, zeroT)
        direct_norm = float(P.metric_norm(direct))

        g0 = jvp_at(P, y0, 0.0, args.dt, args.steps, frozen)
        snapshots = []
        train_records = []
        for lam in train:
            g = jvp_at(P, y0, lam, args.dt, args.steps, frozen)
            c = sub(g, g0)
            snapshots.append(c)
            train_records.append({
                "lambda": lam,
                "correction_norm": float(P.metric_norm(c)),
                "correction_to_tangent_ratio": float(P.metric_norm(c)) /
                    max(float(P.metric_norm(g)), 1e-300),
            })

        basis, evals, Gram = pod_basis(P, snapshots)
        if not basis:
            raise RuntimeError("POD basis is empty")
        max_rank = min(max(ranks), len(basis))
        ranks = [r for r in ranks if 1 <= r <= max_rank]

        Bgram = np.array([
            [P.metric_inner(a, c) for c in basis[:max_rank]]
            for a in basis[:max_rank]
        ])
        basis_gram_error = float(np.max(np.abs(Bgram - np.eye(max_rank))))

        records = []
        payload = {
            "r": P.r,
            "z": z,
            "Gamma0": G,
            "omega10": O,
            "Gamma_direct": direct[0],
            "omega_direct": direct[1],
            "Gamma_g0": g0[0],
            "omega_g0": g0[1],
        }
        for j, phi in enumerate(basis[:max_rank]):
            payload[f"Gamma_phi{j+1}"] = phi[0]
            payload[f"omega_phi{j+1}"] = phi[1]

        prev_true = None
        prev_reduced = {r: None for r in ranks}
        for panels in panels_list:
            nodes, weights = composite_gauss4(panels)
            true_int = zeros(y0)
            reduced_int = {r: zeros(y0) for r in ranks}
            residual_integral = {r: 0.0 for r in ranks}
            coeff_integrals = {r: np.zeros(r, dtype=float) for r in ranks}
            node_records = []

            for lam, wt in zip(nodes, weights):
                g = jvp_at(P, y0, float(lam), args.dt, args.steps, frozen)
                c = sub(g, g0)
                true_int = add(true_int, scale(g, float(wt)))
                nr_rec = {"lambda": float(lam), "weight": float(wt)}
                for rnk in ranks:
                    pc, coeffs = project(P, basis, c, rnk)
                    q = add(g0, pc)
                    res = sub(g, q)
                    reduced_int[rnk] = add(reduced_int[rnk], scale(q, float(wt)))
                    residual_integral[rnk] += float(wt) * float(P.metric_norm(res))
                    coeff_integrals[rnk] += float(wt) * np.asarray(coeffs)
                    nr_rec[f"rank{rnk}_residual_norm"] = float(P.metric_norm(res))
                node_records.append(nr_rec)

            true_rel = rel(P, true_int, direct)
            true_drift = None if prev_true is None else rel(P, true_int, prev_true)
            rank_records = {}
            for rnk in ranks:
                red = reduced_int[rnk]
                red_rel = rel(P, red, direct)
                red_true_abs = float(P.metric_norm(sub(red, true_int)))
                red_true_rel_direct = red_true_abs / max(direct_norm, 1e-300)
                bound_abs = float(residual_integral[rnk])
                bound_rel_direct = bound_abs / max(direct_norm, 1e-300)
                triangle_ratio = red_true_abs / max(bound_abs, 1e-300)
                drift = None if prev_reduced[rnk] is None else rel(P, red, prev_reduced[rnk])
                rank_records[str(rnk)] = {
                    "reduced_endpoint_rel_error_vs_direct": red_rel,
                    "reduced_vs_true_integral_abs_error": red_true_abs,
                    "reduced_vs_true_integral_rel_direct": red_true_rel_direct,
                    "quadrature_residual_integral_abs": bound_abs,
                    "quadrature_residual_integral_rel_direct": bound_rel_direct,
                    "numerical_triangle_ratio": triangle_ratio,
                    "quadrature_drift_from_previous": drift,
                    "integrated_pod_coefficients": coeff_integrals[rnk].tolist(),
                }
                payload[f"Gamma_reduced_r{rnk}_p{panels}"] = red[0]
                payload[f"omega_reduced_r{rnk}_p{panels}"] = red[1]
                prev_reduced[rnk] = red
            payload[f"Gamma_true_p{panels}"] = true_int[0]
            payload[f"omega_true_p{panels}"] = true_int[1]
            records.append({
                "panels": panels,
                "gauss_order_per_panel": 4,
                "node_count": int(len(nodes)),
                "true_bridge_rel_error_vs_direct": true_rel,
                "true_quadrature_drift_from_previous": true_drift,
                "ranks": rank_records,
                "nodes": node_records,
            })
            prev_true = true_int

        eval_rel = evals / max(float(evals[0]), 1e-300)
        final = records[-1]
        out = {
            "status": "PATH-CORRECTION-POD-BRIDGE-AUDIT-COMPLETE",
            "claim_scope": "path-specific finite-discrete reduced tangent bridge only",
            "grid": args.grid,
            "nu": args.nu,
            "dt": args.dt,
            "steps": args.steps,
            "physical_time": args.dt * args.steps,
            "seed_sha256": seed_hash,
            "meta_provenance": meta.get("provenance"),
            "frozen_schedule": frozen,
            "stack_audit": audit,
            "target_initial_metric_norm": float(P.metric_norm(y0)),
            "direct_endpoint_delta_metric_norm": direct_norm,
            "zero_reference_tangent_metric_norm": float(P.metric_norm(g0)),
            "training_amplitudes": train,
            "training_records": train_records,
            "pod_gram_eigenvalues": evals.tolist(),
            "pod_gram_eigenvalues_relative": eval_rel.tolist(),
            "basis_metric_gram_max_error": basis_gram_error,
            "panel_ladder": panels_list,
            "ranks": ranks,
            "quadrature_records": records,
            "final_record": final,
            "important_invariants": {
                "same_frozen_schedule_all_amplitudes": True,
                "path_direction_fixed_unnormalized_y0": True,
                "linear_reference_is_J_at_zero_applied_to_y0": True,
                "POD_compresses_only_path_specific_nonlinear_correction": True,
                "residual_integral_kept_explicit": True,
                "quadrature_residual_bound_is_numerical_not_formal": True,
                "synthetic_seed_not_Hou_late_state": True,
                "no_discrete_to_continuum_promotion": True,
            },
        }

        outstem = Path(args.out)
        outstem.parent.mkdir(parents=True, exist_ok=True)
        Path(str(outstem) + ".json").write_text(
            json.dumps(jsonable(out), indent=2), encoding="utf-8"
        )
        np.savez_compressed(Path(str(outstem) + ".npz"), **payload)
        print(json.dumps(jsonable(out), indent=2))
    finally:
        td.cleanup()
        globals()["_ADJ_MODULE"] = None


if __name__ == "__main__":
    main()
