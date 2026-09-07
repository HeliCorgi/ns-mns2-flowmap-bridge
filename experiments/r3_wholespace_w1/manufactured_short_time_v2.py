#!/usr/bin/env python3
"""Versioned W1 short-time manufactured nonlinear gate with repaired divergence audit.

All non-divergence thresholds are inherited unchanged from manufactured-v1.
The divergence acceptance is exactly the separately preregistered v2 diagnostic.
This is a finite-box numerical preflight only.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Dict, Tuple

import numpy as np

import manufactured_short_time as v1

DIV_CORE_R_MIN = 0.16
DIV_IDENTITY_TOL = 1.0e-9
DIV_COMPAT_TOL = 1.0e-12
DIV_REFINEMENT_RATIO = 0.35


class V2GridSolver(v1.GridSolver):
    def state_diagnostics(self, u: np.ndarray, w: np.ndarray) -> Dict[str, float | bool]:
        base = dict(super().state_diagnostics(u, w))
        legacy_div = float(base.pop("relative_recovered_divergence"))

        psi, _pres = self.solve_psi(w)
        pr = self.d_r(psi)
        q = self.d_z(psi)
        ur = -self.rr * q
        uz = 2.0 * psi + self.rr * pr
        dur = self.d_r(ur)
        duz = self.d_z(uz)

        ur_over_r = np.zeros_like(ur)
        ur_over_r[1:, :] = ur[1:, :] / self.rr[1:, :]
        div_ind = dur + ur_over_r + duz

        div_pred = np.zeros_like(div_ind)
        div_pred[1:-1, :] = q[1:-1, :] - 0.5 * (q[2:, :] + q[:-2, :])

        dzdr = self.d_z(pr)
        drdz = self.d_r(q)
        div_compat = self.rr * (dzdr - drdz)

        mask = (
            (self.rr >= DIV_CORE_R_MIN - 1e-14)
            & (self.rr <= v1.CORE_R + 1e-14)
            & (np.abs(self.zz) <= v1.CORE_Z + 1e-14)
        )

        def infnorm(a: np.ndarray) -> float:
            return float(np.max(np.abs(a[mask])))

        div_ind_inf = infnorm(div_ind)
        div_pred_inf = infnorm(div_pred)
        identity_rel = infnorm(div_ind - div_pred) / max(div_ind_inf, div_pred_inf, 1e-30)

        term_norm = infnorm(dur) + infnorm(ur_over_r) + infnorm(duz)
        independent_rel = div_ind_inf / max(term_norm, 1e-30)

        compat_den = infnorm(self.rr * dzdr) + infnorm(self.rr * drdz)
        compat_rel = infnorm(div_compat) / max(compat_den, 1e-30)

        base.update(
            {
                "legacy_relative_recovered_divergence": legacy_div,
                "independent_divergence_relative_core": independent_rel,
                "divergence_defect_identity_relative_error": identity_rel,
                "compatible_divergence_commutator_relative_error": compat_rel,
            }
        )
        return base


def streamed_summary_v2(run: v1.RunResult) -> Dict[str, object]:
    out = dict(v1.streamed_summary(run))
    out["max_legacy_relative_recovered_divergence"] = out.pop("max_relative_recovered_divergence")
    if run.step_rows:
        out["accepted_steps"] = len(run.step_rows)
        out["max_independent_divergence_relative_core"] = max(
            float(r["independent_divergence_relative_core"]) for r in run.step_rows
        )
        out["max_divergence_defect_identity_relative_error"] = max(
            float(r["divergence_defect_identity_relative_error"]) for r in run.step_rows
        )
        out["max_compatible_divergence_commutator_relative_error"] = max(
            float(r["compatible_divergence_commutator_relative_error"]) for r in run.step_rows
        )
    else:
        out["accepted_steps"] = 0
        out["max_independent_divergence_relative_core"] = math.inf
        out["max_divergence_defect_identity_relative_error"] = math.inf
        out["max_compatible_divergence_commutator_relative_error"] = math.inf
    return out


def restrict_fine_to_coarse(f: np.ndarray) -> np.ndarray:
    return f[::2, ::2]


def run_gate() -> Dict[str, object]:
    solvers = {h: V2GridSolver(h) for h in (0.04, 0.02)}
    m1 = {f"h_{h:.2f}": v1.m1_initial_rhs(solvers[h]) for h in (0.04, 0.02)}

    runs: Dict[Tuple[float, str], v1.RunResult] = {}
    for h in (0.04, 0.02):
        for method in ("rk4", "ssprk3"):
            runs[(h, method)] = v1.run_integrator(solvers[h], method)

    m2 = {
        f"h_{h:.2f}": v1.m2_first_secant(solvers[h], runs[(h, "rk4")])
        for h in (0.04, 0.02)
    }
    summaries = {
        f"h_{h:.2f}_{method}": streamed_summary_v2(runs[(h, method)])
        for h in (0.04, 0.02)
        for method in ("rk4", "ssprk3")
    }

    m5_integrator: Dict[str, float] = {}
    for h in (0.04, 0.02):
        r4 = runs[(h, "rk4")]
        r3 = runs[(h, "ssprk3")]
        m5_integrator[f"h_{h:.2f}"] = solvers[h].combined_rel_core(
            r4.final_u, r4.final_w, r3.final_u, r3.final_w
        )

    coarse = solvers[0.04]
    rc = runs[(0.04, "rk4")]
    rf = runs[(0.02, "rk4")]
    fu = restrict_fine_to_coarse(rf.final_u)
    fw = restrict_fine_to_coarse(rf.final_w)
    m5_resolution = {
        "u1": coarse.rel_core(rc.final_u, fu),
        "omega1": coarse.rel_core(rc.final_w, fw),
    }

    divergence_refinement: Dict[str, object] = {}
    for method in ("rk4", "ssprk3"):
        coarse_rows = runs[(0.04, method)].step_rows
        fine_rows = runs[(0.02, method)].step_rows
        ratios = []
        rows = []
        if len(coarse_rows) == len(fine_rows):
            for cr, fr in zip(coarse_rows, fine_rows):
                c = float(cr["independent_divergence_relative_core"])
                f = float(fr["independent_divergence_relative_core"])
                ratio = f / max(c, 1e-30)
                ratios.append(ratio)
                rows.append(
                    {
                        "step": int(cr["step"]),
                        "time": float(cr["time"]),
                        "coarse": c,
                        "fine": f,
                        "fine_over_coarse": ratio,
                    }
                )
        divergence_refinement[method] = {
            "rows": rows,
            "max_fine_over_coarse": max(ratios) if ratios else math.inf,
        }

    checks: Dict[str, bool] = {}

    # M1 inherited unchanged.
    checks["M1_h04_u"] = m1["h_0.04"]["u1"] <= 0.020
    checks["M1_h04_w"] = m1["h_0.04"]["omega1"] <= 0.025
    checks["M1_h02_u"] = m1["h_0.02"]["u1"] <= 0.006
    checks["M1_h02_w"] = m1["h_0.02"]["omega1"] <= 0.006
    checks["M1_reduction_u"] = m1["h_0.02"]["u1"] <= 0.35 * m1["h_0.04"]["u1"]
    checks["M1_reduction_w"] = m1["h_0.02"]["omega1"] <= 0.35 * m1["h_0.04"]["omega1"]

    # M2 inherited unchanged.
    checks["M2_h04_u"] = m2["h_0.04"]["u1"] <= 0.025
    checks["M2_h04_w"] = m2["h_0.04"]["omega1"] <= 0.030
    checks["M2_h02_u"] = m2["h_0.02"]["u1"] <= 0.008
    checks["M2_h02_w"] = m2["h_0.02"]["omega1"] <= 0.008
    checks["M2_decrease_u"] = m2["h_0.02"]["u1"] < m2["h_0.04"]["u1"]
    checks["M2_decrease_w"] = m2["h_0.02"]["omega1"] < m2["h_0.04"]["omega1"]

    # M3 and inherited non-divergence M4 rows, plus D1/D3.
    for key, ss in summaries.items():
        checks[f"{key}_completed"] = bool(ss["completed"])
        checks[f"{key}_eight_steps"] = int(ss["accepted_steps"]) == 8
        checks[f"{key}_no_reject"] = int(ss["rejected_steps"]) == 0
        checks[f"{key}_finite"] = bool(ss["all_stage_finite"] and ss["all_step_finite"])
        checks[f"{key}_amp"] = float(ss["max_frozen_symbol_amplification"]) <= 1.0 + v1.STABILITY_TOL
        checks[f"{key}_cfl"] = float(ss["max_cfl"]) <= 0.10
        checks[f"{key}_visc"] = float(ss["max_viscous_number"]) <= 0.05
        checks[f"{key}_poisson"] = max(
            float(ss["max_stage_poisson_residual"]), float(ss["max_step_poisson_residual"])
        ) <= 1e-10
        checks[f"{key}_odd"] = float(ss["max_odd_z_defect"]) <= 1e-12
        checks[f"{key}_energy"] = float(ss["max_energy_ratio_to_initial"]) <= 1.0 + 1e-5
        checks[f"{key}_energy_balance"] = float(ss["max_energy_balance_defect"]) <= 0.20
        checks[f"{key}_div_identity"] = (
            float(ss["max_divergence_defect_identity_relative_error"]) <= DIV_IDENTITY_TOL
        )
        checks[f"{key}_div_compat"] = (
            float(ss["max_compatible_divergence_commutator_relative_error"]) <= DIV_COMPAT_TOL
        )

    # D2 requires second-order reduction at every matched accepted time.
    for method in ("rk4", "ssprk3"):
        rows = divergence_refinement[method]["rows"]
        checks[f"M4_D2_{method}_eight_matched_times"] = len(rows) == 8
        for row in rows:
            checks[f"M4_D2_{method}_step{row['step']}"] = (
                float(row["fine_over_coarse"]) <= DIV_REFINEMENT_RATIO
            )

    # M5 inherited unchanged.
    checks["M5_integrator_h04"] = m5_integrator["h_0.04"] <= 2e-6
    checks["M5_integrator_h02"] = m5_integrator["h_0.02"] <= 2e-6
    checks["M5_resolution_u"] = m5_resolution["u1"] <= 2e-4
    checks["M5_resolution_w"] = m5_resolution["omega1"] <= 0.030

    passed = bool(all(checks.values()))
    return {
        "schema": "r3-w1-manufactured-v2",
        "frozen_parameters": {
            "nu": v1.NU,
            "A": v1.A0,
            "R": 1.0,
            "Z": 1.0,
            "alpha": 16.0,
            "kappa": 1.0,
            "Rmax": v1.RMAX,
            "Zmax": v1.ZMAX,
            "h": [0.04, 0.02],
            "T": v1.T_FINAL,
            "dt": v1.DT,
            "primary_integrator": "rk4",
            "comparison_integrator": "ssprk3",
            "divergence_core_r": [DIV_CORE_R_MIN, v1.CORE_R],
            "divergence_core_abs_z_max": v1.CORE_Z,
            "divergence_identity_tolerance": DIV_IDENTITY_TOL,
            "divergence_compatible_tolerance": DIV_COMPAT_TOL,
            "divergence_refinement_ratio": DIV_REFINEMENT_RATIO,
        },
        "M1_initial_rhs_relative_errors": m1,
        "M2_first_step_secant_relative_errors": m2,
        "M3_M4_streamed_summaries": summaries,
        "M4_divergence_refinement": divergence_refinement,
        "M5_integrator_relative_state_difference": m5_integrator,
        "M5_resolution_relative_difference": m5_resolution,
        "checks": checks,
        "decision": "PASS" if passed else "STOP_REPAIR_W1_MANUFACTURED_V2",
        "pass": passed,
        "v1_status": "STOP_REPAIR_W1_MANUFACTURED (unchanged)",
        "claim_boundary": "short-time finite-box manufactured nonlinear preflight v2 only",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/r3_wholespace_w1/results/W1_MANUFACTURED_SHORT_TIME_V2.json"),
    )
    args = parser.parse_args()
    result = run_gate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"decision": result["decision"], "output": str(args.output)}, indent=2))
    return 0 if result["pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
