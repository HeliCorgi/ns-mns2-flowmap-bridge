# M1 stateflow pass — 2026-09-04

## Scope

First direct use of the `kernel-dynamics-viewer/stateflow` design on the current M-1 observables. No repository was modified. The local adapter follows the core `FeatureSeries` / `Trajectory` / `TransitionAnalyzer` semantics from `stateflow/core.py` and keeps continuous measurements primary; labels below are only exploratory transition markers.

The input is a fresh E0 Taylor–Green rerun using the current `experiments/m1_events/events.py` solver conventions: periodic `[0,2π)^3`, `N=64`, `ν=0.02`, `dt=0.0125`. Full diagnostics were sampled every `0.1` on `0 ≤ t ≤ 1.3`. This segment is numerically resolved by the standing tail rule: max recorded tail `1.7e-12 << 1e-5`.

## Axes

The state vector is

`(E, Λ, C1, β_top1, β_intense, ΔB, C4, cos²θ2_intense, twist_share, tail)`

with

- `C1 = (net stretching)/(gross stretching)`;
- `β_top1 = (-4∫ det S)/(∫q)` on the top 1% of positive `q = ωᵀSω`;
- `β_intense` on `{λ2>0} ∩ {|ω|>0.25Λ}`;
- `ΔB = β_intense - β_top1`;
- `C4 = (vortical λ2 source + pressure-Hessian term)/(vortical λ2 source)` on the same intense set.

The exact whole-domain Betchov validation remains `β_global = 1` to floating-point accuracy in the underlying cross-check.

## Stateflow transition test

I used three labels only as interpretable threshold probes:

1. `NESTED_FLUX_CORE_SOURCE_OUTER` iff `β_top1 < 0.5` and `β_intense > 0.5`. These `0.5` thresholds have a direct majority meaning: more than half of the top-core net production is the divergence/Betchov contribution while more than half of the broader intense-region production is determinant-source contribution.
2. `PRESSURE_SHIELDED` iff `C4 < 0.5` (pressure removes more than half of the vortical λ2 source in the chosen normalization).
3. `ENSTROPHY_GROWTH` iff the centered finite-difference `E'(t) > 0`.

Detected transitions:

- `t = 0.5`: `OTHER -> NESTED_FLUX_CORE_SOURCE_OUTER`;
- `t = 0.5`: `PRESSURE_SHIELDED -> PRESSURE_SURVIVES`;
- `t = 0.8`: `NO_GROWTH -> ENSTROPHY_GROWTH`.

Thus, in this resolved E0 onset segment, the majority-level Betchov localization split and the loss of majority pressure shielding occur about `0.3` time units before the enstrophy-growth sign change.

Representative values:

| t | β_top1 | β_intense | ΔB | C4 | E |
|---:|---:|---:|---:|---:|---:|
| 0.4 | 0.519 | 0.812 | 0.293 | 0.471 | 180.074 |
| 0.5 | 0.430 | 0.847 | 0.417 | 0.505 | 179.395 |
| 0.7 | 0.303 | 0.936 | 0.634 | 0.563 | 178.844 |
| 0.8 | 0.263 | 0.975 | 0.712 | 0.592 | 178.931 |
| 0.9 | 0.220 | 1.029 | 0.808 | 0.617 | 179.233 |
| 1.3 | 0.118 | 1.169 | 1.051 | 0.704 | 182.150 |

## What survives the check

The stateflow view is useful: it turns the previous snapshot observation into an episode/transition question. E0 does contain a persistent transition from an initially source-balanced core to a flux-majority hot core embedded in a source-majority intense region, and that transition is already present before positive enstrophy growth begins.

However, this is **not yet a precursor theorem or even strong precursor evidence**. The conclusion is threshold-sensitive. A stricter state `β_top1 < 0.25` and `β_intense > 0.75` begins only at `t = 0.9`, after the growth sign change. Also `C1`, `ΔB`, and `C4` are all smooth strongly trending variables in this short Taylor–Green onset; same-time descriptive correlations are very high (`corr(ΔB,C4) ≈ 0.93`, `corr(ΔB,E') ≈ 0.99`). Those correlations are not independence evidence and can simply reflect a common deterministic transient.

The cross-datum event summaries still suggest different mechanisms, but they do not yet satisfy stateflow's stronger independence standard at evidence grade because E3/E4/E2 are unresolved under the standing tail rule and no E2b `β_B(θ,t)` trajectory has been measured.

## Verdict

**TRANSITION-CANDIDATE / DIAGNOSTIC-ONLY.**

`stateflow` is a good analysis harness for M-1. It exposed a concrete, falsifiable temporal statement that was hidden by event medians:

> In E0, a majority-level `flux-core / source-outer` localization state appears before the enstrophy-growth onset and coincides with the transition from majority pressure shielding to majority pressure survival.

The statement is currently one-datum numerical structure, not a regularity criterion. No proof head should be promoted yet.

## Files

- `E0_stateflow_timeseries_partial.json` — fresh resolved E0 time series, 0.1 cadence, t≤1.3.
- `M1_STATEFLOW_E0_ANALYSIS.json` — stateflow-style feature matrix and detected transitions.
- `m1_stateflow_adapter.py` — local adapter implementing the relevant stateflow core semantics.
