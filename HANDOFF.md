# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: **2026-09-06 JST (forty-ninth session)**.

This is the durable continuation point. Current theorem/source files and merged `main` control accepted state. Numerical artifacts are evidence only for the exact revision/run recorded below. No current result proves Clay A/B/C/D.

## Accepted main boundary

Current accepted `main` head at this session start:

`64848e3912021be870d3aa19866f1e37b41a0059`

(PR #98 merge: `Numerics: run first M1 resolution rescue screen`).

Immediately preceding accepted research integration:

- PR #97 merged as `25954382b1db85fcd5fc2a35b6b6e70c34240327`;
- its B2 records establish only the negative compactness/stationarity decisions already stated there; they do not kill the parent B2 middle limb.

Accepted formal state remains unchanged:

- whole-space `R^3` local actual-NS mild stack for real divergence-free Schwartz data, anchored by `MNS2.r3AdmissibleSchwartzDatum_navierStokes` and `MNS2.r3EndpointSafeProjectedMild_navierStokes`;
- periodic special-family sidecar from PR #92, including `ClayNS.certified_nonzero_periodic_NS` and `ClayNS.clayB_has_nonzero_smooth_specialization`;
- `ClayNS.ClayB` remains defined but unproved.

The whole-space theorem is local in time and distributional in space. The periodic theorem is a special-family global certificate, not the universal Clay-B proposition.

Latest hosted Lean evidence on the most recent numerical PR head:

- PR #98 head `99541d2202c9394926b46a82dda991a892f0f4e5`;
- workflow `Lean 4 formalization`, run #282 / run id `34005553922`;
- result: **PASS**.

No Lean/formal source changed in PR #97 or #98, so `FORMAL_SCOPE.md` is intentionally unchanged. Stage-9 formal plumbing remains stopped unless a concrete commissioned theorem consumes a missing formal edge or a semantic defect is found.

## Breakdown analytic state

The parent B2 middle limb remains **OPEN**. Accepted negative/narrowing results include:

- S15 `(q,d)` cone parked after the pressure and fourth-jet counterfamilies;
- FDT cross-track parked under its recorded deformation/Cauchy-Green reopen conditions;
- Gamma-saturation microgeometry static-enstrophy kill failed, while the mandatory transition-vorticity lower bound survived;
- fixed-profile ancient/steady-Euler route parked;
- `B2-ANCIENT-EULER-COMPACTNESS = NO` from current B2 controls;
- `B2-MODULATION-SHAPE-STATIONARITY = NO` from current hypotheses;
- `B2-MODULATION-STRONG-COMPACTNESS = NO` from current budgets;
- K11's exponent cut itself remains valid, but the old unconditional phrase `interior => quasi-static steady-Euler core` is withdrawn.

Do not reopen these lanes merely because the numerical M-1 program is inconclusive.

## Active lane — periodic M-1 resolution rescue

The user commissioned a return to the M-1 numerical candidate/mechanism-selection lane. The governing records are:

- `experiments/m1_events/PREREG.md`;
- `M1_INDEPENDENT_PROBE/M1_INDEPENDENT_PROBE_2026-09-04.md`;
- `Stateflow M-1/M1_BOUNDARY_LOCALIZATION_ESTIMATE_AUDIT_2026-09-04.md`;
- `experiments/m1_events/M1_RESOLUTION_RESCUE_PREREG_2026-09-06.md`.

This is periodic `T^3` evidence-grade work only. It is not an `R^3` candidate and not a blow-up/regularity theorem.

The standing fail-closed resolution rule is

```text
max_tail <= 1e-5 over the entire run
```

plus finite numerical state. Per-snapshot masks do not repair a globally unresolved run.

The legacy E3/E4 random FFT-array seeds are not one fixed continuum datum across changing `N`. Only the new `E3c*`/`E4c*` resolution-invariant seed families may be used for fixed-datum convergence comparisons.

## Session 49 — first executed rescue result

PR #98 is merged. Its revision-qualified numerical workflow completed successfully.

Workflow evidence:

- workflow: `M-1 resolution rescue`;
- run id: `34005553913`;
- PR head: `99541d2202c9394926b46a82dda991a892f0f4e5`;
- GitHub-hosted Ubuntu 24.04;
- Python 3.12.14, NumPy 2.5.2, SciPy 1.18.1.

Seed self-check:

```text
PASS shared=0.000e+00 coeff_norm_delta=4.441e-16
```

`E1R96` result:

```text
N = 96
nu = 0.01
T = 8
dt = 1/150
nsteps = 1200
max_tail = 6.086987397920e-07
tail_tolerance = 1.000000000000e-05
tail_pass = True
finite_pass = True
max_relative_single_step_energy_growth = 0.000000000000e+00
walltime_s = 519.108
```

Therefore

```text
E1R96 WHOLE-RUN RESOLUTION SCREEN = PASS
```

at the preregistered tail gate.

Artifact:

- `m1-e1r96-resolution-screen`;
- id `9980926946`;
- ZIP digest `sha256:d15de290da07776781a36a2337723899d0703b7ee01873d0a370bd559dd03c53`.

Durable result record added on the current continuation branch:

`experiments/m1_events/M1_RESOLUTION_RESCUE_RUN1_RESULT_2026-09-06.md`.

Consequence: `E1R96` is eligible for `nearfar_rescue.py`. This is still only one periodic fixed datum and does not establish FAR/COMM/LOC universality or refinement stability.

## Current continuation branch

Branch:

`numerics/m1-resolution-run2`

Purpose: execute the next preregistered R0 pair before any new observable is invented.

New workflow:

`.github/workflows/m1-resolution-rescue-stage2.yml`

It runs the exact fixed-continuum seed self-check and then screens in parallel:

- `E3c64`;
- `E3c96`.

Scientific `tail_pass=false` remains a numerical result, not a CI failure. Exceptions, non-finite state, timeout, missing artifact, or seed-self-check failure remain real execution failures.

At this handoff write the branch is prepared but the PR/workflow result is not yet assigned. Do not infer an E3c PASS/FAIL until the actual workflow artifacts/logs are inspected.

## Next work

1. Open the focused PR from `numerics/m1-resolution-run2` to `main` and inspect the `E3c64` / `E3c96` workflow outputs.
2. If both E3c runs pass the whole-run tail gate, retain them as the first fixed-continuum two-resolution pair and proceed to the preregistered E4c pair before selecting a mechanism. `E1R96` may also enter `nearfar_rescue.py`, but one-datum near/far evidence is not yet a cross-datum verdict.
3. If one E3c resolution fails, follow the preregistered ladder to `E3c128` only as needed; do not move the `1e-5` tail gate.
4. After the E3c decision, screen `E4c64` and `E4c96`, then `E2R128` in the recorded order.
5. Only after a run is whole-run tail-qualified may `nearfar_rescue.py` be run for it.
6. Mechanism promotion requires at least two genuinely different continuum data with tail-qualified, refinement-stable growth events and the same residual class (FAR/COMM/LOC) carrying the positive surplus after near-field absorption.
7. Before promotion beyond diagnostic-only status, justify a convergence tolerance independently/manufactured-test-first and rerun the highest accepted spatial grid with `dt/2`.

## Commission boundaries / forbidden shortcuts

Do **not**:

- claim Clay A/B/C/D, numerical blow-up, or numerical global regularity;
- call the periodic M-1 program an `R^3` candidate;
- identify CI success with scientific tail-gate success;
- treat a per-snapshot stateflow mask as repair of a globally unresolved run;
- compare legacy E3/E4 at different `N` as one fixed continuum datum;
- run expensive near/far diagnostics on an unresolved run;
- select a convergence tolerance after seeing which tolerance gives the preferred residual class;
- call the historical FAR pattern universal before at least two distinct fixed continuum data are resolved and refinement-stable;
- revive the killed Betchov-boundary mechanism as an independent physical transport mechanism;
- reopen S15, FDT, Gamma microgeometry, or fixed-profile ancient-Euler lanes without satisfying their recorded reopen conditions;
- add Lean plumbing merely for completeness.

## Resume protocol

At substantive resume inspect, in order:

1. `PROJECT_GOAL.md`;
2. `SPEC.md`;
3. `AGENTS.md`;
4. `FORMAL_SCOPE.md`;
5. this file;
6. `docs/GPT_WORKFLOW.md`;
7. `docs/LEAN_CI_OPERATIONS.md`;
8. Stage-9 readiness/selection records as required by `docs/GPT_WORKFLOW.md`;
9. the four M-1 records listed above;
10. `resolution_invariant_ic.py`, `resolution_rescue.py`, `nearfar_rescue.py`;
11. external `ns-singularity-certificate-lab@fable5-mainline/FABLE5_NEXT_TASK_AUDIT.md` numerical guardrails;
12. current `main`, open PRs, workflow artifacts/logs, and the exact numerical revision under discussion.

The current objective is evidence-grade mechanism selection and candidate infrastructure only. No current result proves a 3D Navier--Stokes singularity or a global-regularity theorem.
