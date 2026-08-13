#!/usr/bin/env python3
"""MNS-2 v2.12 — predictive path-correction POD coefficient bridge.

Training computes true JVP corrections only at registered training amplitudes. A POD
basis is learned there, and scalar coefficient functions are fit with PCHIP including
the exact c(0)=0 anchor. At certification quadrature nodes the predictor q_pred is
formed from the trained coefficient model BEFORE the true JVP is evaluated. The true
JVP at those held-out nodes is used only to audit residual/error.

The default training mesh resolves the sharp low-amplitude coefficient crossover that
was missed by the coarse v2.11 training amplitudes. The default rank is four; rank two
is deliberately not promoted after the richer training set exposed additional resolved
correction directions.

Finite-discrete synthetic experiment only; no continuum/Clay promotion.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
from scipy.interpolate import PchipInterpolator

HERE = Path(__file__).resolve().parent
V211 = HERE / "mns2_path_correction_pod_bridge_v2.11.py"
spec = importlib.util.spec_from_file_location("mns2_v211_for_v212", V211)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot import v2.11")
v = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = v
spec.loader.exec_module(v)

DEFAULT_TRAIN = "0.005,0.01,0.025,0.05,0.1,0.25,0.5,0.75,1.0"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("seed")
    ap.add_argument("meta")
    ap.add_argument("schedule")
    ap.add_argument("--stack-dir", default=str(v.CORE))
    ap.add_argument("--grid", default="12x24")
    ap.add_argument("--nu", type=float, default=5e-3)
    ap.add_argument("--dt", type=float, default=2e-8)
    ap.add_argument("--steps", type=int, default=2)
    ap.add_argument("--train", default=DEFAULT_TRAIN)
    ap.add_argument("--panels", default="2,4,6,8,12")
    ap.add_argument("--rank", type=int, default=4)
    ap.add_argument("--out", default="MNS2_V2.12_PREDICTIVE_PATH_POD_BRIDGE")
    args = ap.parse_args()

    seed_container_hash = v.sha256(args.seed)
    meta = v.check_meta(args.meta)
    frozen = v.load_shared_schedule(args.schedule, seed_container_hash)
    train = np.asarray([float(x) for x in args.train.split(",") if x.strip()])
    panels_list = [int(x) for x in args.panels.split(",") if x.strip()]
    if np.any(train <= 0) or np.any(train > 1) or np.any(np.diff(train) <= 0):
        raise ValueError("train amplitudes must be strictly increasing in (0,1]")
    if args.rank < 1:
        raise ValueError("rank must be positive")

    td, staged, audit = v.stage_stack(args.stack_dir)
    try:
        v.load_adjoint_from_staged(staged)
        nr, nz = map(int, args.grid.split("x"))
        P = v._ADJ_MODULE.AdjointPilot(nr, nz, nu=args.nu, alpha_safety=1.5)
        z = (np.arange(nz) + 0.5) * P.dz
        d = np.load(args.seed)
        G = v.pinterp(d["r"], d["z"], d["Gamma"], P.r, z)
        O = v.pinterp(d["r"], d["z"], d["omega1"], P.r, z)
        y0 = (G, O)
        zero = v.zeros(y0)

        target = v.evolve_base(P, G, O, args.dt, args.steps, frozen)
        zeroT = v.evolve_base(P, zero[0], zero[1], args.dt, args.steps, frozen)
        direct = v.sub(target, zeroT)
        direct_norm = P.metric_norm(direct)
        g0 = v.jvp_at(P, y0, 0.0, args.dt, args.steps, frozen)

        # TRAINING PHASE: true JVPs are evaluated only at registered train amplitudes.
        corrections = []
        correction_norms = []
        for lam in train:
            c = v.sub(v.jvp_at(P, y0, float(lam), args.dt, args.steps, frozen), g0)
            corrections.append(c)
            correction_norms.append(float(P.metric_norm(c)))

        basis, evals, _ = v.pod_basis(P, corrections)
        if len(basis) < args.rank:
            raise RuntimeError("insufficient POD rank")
        basis = basis[: args.rank]

        coeff_train = np.empty((len(train), args.rank))
        train_residual = []
        for i, c in enumerate(corrections):
            pc, coeff = v.project(P, basis, c, args.rank)
            coeff_train[i] = coeff
            train_residual.append(float(P.metric_norm(v.sub(c, pc))))

        # Exact correction anchor c(0)=0, hence every POD coefficient is zero at lambda=0.
        model_x = np.concatenate([[0.0], train])
        model_y = np.vstack([np.zeros(args.rank), coeff_train])
        models = [
            PchipInterpolator(model_x, model_y[:, j], extrapolate=False)
            for j in range(args.rank)
        ]

        def predict(lam):
            pc = v.zeros(y0)
            coeff = []
            for phi, model in zip(basis, models):
                aj = float(model(lam))
                coeff.append(aj)
                pc = v.add(pc, v.scale(phi, aj))
            return v.add(g0, pc), coeff

        records = []
        prev_pred = None
        for panels in panels_list:
            nodes, weights = v.composite_gauss4(panels)
            pred_int = v.zeros(y0)
            true_int = v.zeros(y0)
            residual_q = 0.0
            correction_norm_q = 0.0
            coeff_int = np.zeros(args.rank)
            node_records = []

            for lam, wt in zip(nodes, weights):
                # Crucial FC-078 guard: predictor is finalized without held-out true JVP.
                q_pred, coeff = predict(float(lam))
                pred_int = v.add(pred_int, v.scale(q_pred, float(wt)))
                coeff_int += float(wt) * np.asarray(coeff)

                # Certification-only truth evaluation happens after prediction is fixed.
                g_true = v.jvp_at(P, y0, float(lam), args.dt, args.steps, frozen)
                true_int = v.add(true_int, v.scale(g_true, float(wt)))
                true_correction = v.sub(g_true, g0)
                correction_norm = P.metric_norm(true_correction)
                correction_norm_q += float(wt) * correction_norm
                res = v.sub(g_true, q_pred)
                rn = P.metric_norm(res)
                residual_q += float(wt) * rn
                node_records.append(
                    {
                        "lambda": float(lam),
                        "weight": float(wt),
                        "predicted_coefficients": coeff,
                        "true_correction_norm": float(correction_norm),
                        "certification_residual_norm": float(rn),
                        "residual_to_true_correction_ratio": float(
                            rn / max(correction_norm, 1e-300)
                        ),
                    }
                )

            pred_direct = v.rel(P, pred_int, direct)
            true_direct = v.rel(P, true_int, direct)
            pred_true_abs = P.metric_norm(v.sub(pred_int, true_int))
            pred_true_rel = pred_true_abs / max(direct_norm, 1e-300)
            bound_rel = residual_q / max(direct_norm, 1e-300)
            residual_to_correction = residual_q / max(correction_norm_q, 1e-300)
            drift = None if prev_pred is None else v.rel(P, pred_int, prev_pred)
            records.append(
                {
                    "panels": panels,
                    "node_count": len(nodes),
                    "predictive_endpoint_rel_error_vs_direct": float(pred_direct),
                    "true_bridge_rel_error_vs_direct": float(true_direct),
                    "predictive_vs_true_integral_abs_error": float(pred_true_abs),
                    "predictive_vs_true_integral_rel_direct": float(pred_true_rel),
                    "quadrature_residual_integral_abs": float(residual_q),
                    "quadrature_residual_integral_rel_direct": float(bound_rel),
                    "quadrature_true_correction_norm_integral_abs": float(correction_norm_q),
                    "predictive_residual_to_true_correction_integral_ratio": float(
                        residual_to_correction
                    ),
                    "numerical_triangle_ratio": float(pred_true_abs / max(residual_q, 1e-300)),
                    "predictive_quadrature_drift_from_previous": drift,
                    "integrated_predicted_coefficients": coeff_int.tolist(),
                    "nodes": node_records,
                }
            )
            prev_pred = pred_int

        max_panel_nodes = v.composite_gauss4(max(panels_list))[0]
        held_out = bool(
            all(np.min(np.abs(train - node)) > 1e-14 for node in max_panel_nodes)
        )
        out = {
            "status": "PREDICTIVE-PATH-POD-BRIDGE-AUDIT-COMPLETE",
            "claim_scope": "path-specific finite-discrete predictive coefficient audit only",
            "grid": args.grid,
            "nu": args.nu,
            "dt": args.dt,
            "steps": args.steps,
            "physical_time": args.dt * args.steps,
            "generated_seed_container_sha256": seed_container_hash,
            "meta_provenance": meta.get("provenance"),
            "frozen_schedule": frozen,
            "stack_audit": audit,
            "training_amplitudes": train.tolist(),
            "training_correction_norms": correction_norms,
            "training_coefficients": coeff_train.tolist(),
            "training_projection_residual_norms": train_residual,
            "pod_eigenvalues_relative": (evals / max(float(evals[0]), 1e-300)).tolist(),
            "coefficient_model": "PCHIP with exact c(0)=0 anchor",
            "rank": args.rank,
            "direct_endpoint_delta_metric_norm": float(direct_norm),
            "zero_reference_tangent_metric_norm": float(P.metric_norm(g0)),
            "records": records,
            "final_record": records[-1],
            "important_invariants": {
                "predictor_formed_before_true_JVP_at_certification_nodes": True,
                "coefficient_models_use_training_nodes_only": True,
                "certification_nodes_are_held_out_from_training": held_out,
                "same_frozen_schedule_all_amplitudes": True,
                "path_direction_fixed_unnormalized_y0": True,
                "synthetic_seed_not_Hou_late_state": True,
                "no_discrete_to_continuum_promotion": True,
                "residual_integral_is_quadrature_estimate_not_rigorous_enclosure": True,
                "correction_relative_error_reported_separately_from_direct_endpoint_error": True,
            },
        }
        if not held_out:
            raise RuntimeError("certification quadrature node leaked into coefficient training set")

        outstem = Path(args.out)
        outstem.parent.mkdir(parents=True, exist_ok=True)
        Path(str(outstem) + ".json").write_text(
            json.dumps(v.jsonable(out), indent=2), encoding="utf-8"
        )
        print(json.dumps(v.jsonable(out), indent=2))
    finally:
        td.cleanup()
        v._ADJ_MODULE = None


if __name__ == "__main__":
    main()
