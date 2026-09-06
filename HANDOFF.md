# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: **2026-09-06 JST (fiftieth session)**.

This is the durable continuation point. Current theorem/source files and merged `main` control accepted state. Numerical artifacts are evidence only for the exact revisions/runs recorded below. No current result proves Clay A/B/C/D.

## Accepted main boundary

Current accepted `main` head at this session start:

`b65b00758cd7691df3bb19e7938ac7278c94b180`

(PR #99 merge: `Numerics: screen fixed-continuum E3c resolution pair`).

Accepted formal state is unchanged:

- whole-space `R^3` local actual-NS mild stack for real divergence-free Schwartz data, anchored by `MNS2.r3AdmissibleSchwartzDatum_navierStokes` and `MNS2.r3EndpointSafeProjectedMild_navierStokes`;
- periodic special-family sidecar from PR #92, including `ClayNS.certified_nonzero_periodic_NS` and `ClayNS.clayB_has_nonzero_smooth_specialization`;
- `ClayNS.ClayB` remains defined but unproved.

The strongest whole-space theorem is local in time and distributional in space. The periodic shear theorem is a genuine global special solution, not the universal Clay-B proposition. `FORMAL_SCOPE.md` is intentionally unchanged.

Latest accepted hosted Lean evidence before the current PR:

- PR #99 head `795797d4d889702788867069e0eccddb55c5b948`;
- workflow `Lean 4 formalization`, run #283 / run id `34013942237`;
- result: **PASS**.

No Lean/formal source changed in the active numerical work. Stage-9 formal plumbing remains stopped unless a concrete commissioned theorem consumes a missing formal edge or a semantic defect is found.

## Breakdown analytic state

The parent B2 middle limb remains **OPEN**. Existing narrowed/parked lanes remain unchanged:

- S15 `(q,d)` cone parked after pressure and fourth-jet counterfamilies;
- FDT cross-track parked under its deformation/Cauchy-Green reopen conditions;
- Gamma-saturation microgeometry static-enstrophy kill failed, while the mandatory transition-vorticity lower bound survived;
- fixed-profile ancient/steady-Euler route parked;
- `B2-ANCIENT-EULER-COMPACTNESS = NO`;
- `B2-MODULATION-SHAPE-STATIONARITY = NO`;
- `B2-MODULATION-STRONG-COMPACTNESS = NO`;
- K11's exponent cut remains valid, but the old unconditional phrase `interior => quasi-static steady-Euler core` is withdrawn.

Do not reopen these lanes merely because the numerical M-1 program is inconclusive.

## Active lane — periodic M-1 resolution rescue

Governing records:

- `experiments/m1_events/PREREG.md`;
- `M1_INDEPENDENT_PROBE/M1_INDEPENDENT_PROBE_2026-09-04.md`;
- `Stateflow M-1/M1_BOUNDARY_LOCALIZATION_ESTIMATE_AUDIT_2026-09-04.md`;
- `experiments/m1_events/M1_RESOLUTION_RESCUE_PREREG_2026-09-06.md`.

This is periodic `T^3` evidence-grade work only. It is not an `R^3` candidate and not a blow-up/regularity theorem.

Standing fail-closed R0 gate:

```text
max_tail <= 1e-5 over the entire run
and finite numerical state
```

Per-snapshot masks do not repair a globally unresolved run. Legacy E3/E4 FFT-array random seeds are not fixed continuum data across changing `N`; only the new E3c/E4c continuum-seeded families may be used for fixed-datum refinement comparisons.

## Accepted numerical results on main

### E1R96 — PR #98

Workflow run `34005553913`, PR head `99541d2202c9394926b46a82dda991a892f0f4e5`:

```text
E1R96
N = 96
max_tail = 6.086987397920e-07
tail_pass = True
finite_pass = True
max_relative_single_step_energy_growth = 0
```

Artifact `m1-e1r96-resolution-screen`, id `9980926946`, digest
`sha256:d15de290da07776781a36a2337723899d0703b7ee01873d0a370bd559dd03c53`.

### E3c64 / E3c96 — PR #99

Workflow run `34013942287`, PR head `795797d4d889702788867069e0eccddb55c5b948`:

```text
E3c64
max_tail = 5.956860730357e-05
TAIL GATE = FAIL
finite_pass = True

E3c96
max_tail = 3.274744131023e-07
TAIL GATE = PASS
finite_pass = True
```

Artifacts:

- `m1-E3c64-resolution-screen`, id `9983329156`, digest `sha256:1ed22f6775fbb347e367b665769e8bce1b83e5675da9575478183deee285758b`;
- `m1-E3c96-resolution-screen`, id `9983371155`, digest `sha256:c8775148c3a9d00614fd474561e14f592711efe799e09934382c8f495000815b`.

Durable record: `experiments/m1_events/M1_RESOLUTION_RESCUE_RUN2_RESULT_2026-09-06.md` on the current PR branch.

## Session 50 — E3c128 refinement gate

Current branch:

`numerics/m1-e3c128-run`

Current PR:

PR #100 `Numerics: screen fixed-continuum E3c128 refinement`.

The exact preregistered configuration was executed without changing solver, datum, threshold, or diagnostics:

```text
E3c128
N = 128
nu = 0.02
T = 3.5
dt = 1/160
```

Revision-qualified numerical evidence:

- checked PR head: `44c119292bd9c0ef0f37a8d97fd8a42487b8a267`;
- workflow: `M-1 E3c128 resolution screen`;
- run id: `34015004075`;
- job id: `101437192765`;
- GitHub-hosted Ubuntu 24.04, Python 3.12.14, NumPy 2.5.2, SciPy 1.18.1;
- fixed-continuum seed self-check: **PASS**.

Exact result:

```text
max_tail = 2.845872144398e-09
tail_tolerance = 1.000000000000e-05
tail_pass = True
finite_pass = True
max_relative_single_step_energy_growth = 0.000000000000e+00
walltime_s = 777.279
```

Therefore:

```text
E3c128 WHOLE-RUN RESOLUTION SCREEN = PASS
```

Artifact:

- `m1-E3c128-resolution-screen`;
- id `9983774115`;
- size 2507 bytes;
- digest `sha256:9f8dd8f4cb79f3d84cab81701b98d85189c3ae74f3b01d56b51788f44455fc8e`.

The post-result documentation commit is later than the checked numerical head and does not retroactively change the evidence revision. The stage-3 workflow is left `workflow_dispatch`-only after the qualified execution to avoid rerunning the expensive N=128 screen on docs-only PR synchronizations.

## What the E3c result now means

The fixed continuum E3c datum now has two retained whole-run tail-qualified resolutions:

```text
E3c96  PASS   max_tail = 3.274744131023e-07
E3c128 PASS   max_tail = 2.845872144398e-09
```

`E3c64` remains excluded. This is **R0 qualification of a same-datum 96/128 pair**. It is not yet a statement that the near/far mechanism diagnostics are refinement-stable.

Only E3c96 and E3c128 may enter the E3c near/far/refinement verdict. E3c64 may not.

## Next work

Primary next gate after PR #100 is merged:

```text
M1-E3c-R1/R2: run nearfar_rescue.py on E3c96 and E3c128,
then compare on common physical times the preregistered growth-event and residual diagnostics.
```

Compare at least:

- growth-event start/end times;
- max enstrophy and max vorticity;
- `A_N`, `A_F`, `A_C`, `A_L`, `g`;
- residual-class labels at positive-growth samples;
- `R/dx` and `ell/dx`;
- filtered-budget residual.

Do not invent a percentage convergence tolerance after seeing the result. A mechanism promotion needs a separately justified/manufactured-test-first tolerance, and the highest accepted spatial grid must later be rerun with `dt/2`.

After the E3c refinement/near-far decision, continue the preregistered cross-datum R0 order with `E4c64` and `E4c96`, then `E2R128` as needed. The broader M-1 GO rule still requires at least two genuinely different continuum data with tail-qualified, refinement-stable growth events and the same residual class carrying the positive surplus after near-field absorption.

## Commission boundaries / forbidden shortcuts

Do **not**:

- claim Clay A/B/C/D, numerical blow-up, or numerical global regularity;
- call the periodic M-1 program an `R^3` candidate;
- identify CI success with scientific tail-gate success;
- treat a per-snapshot mask as repair of a globally unresolved run;
- compare legacy E3/E4 at different `N` as one fixed continuum datum;
- use E3c64 in a near/far mechanism verdict;
- select a convergence tolerance after seeing which tolerance gives the preferred residual class;
- call the historical FAR pattern universal before at least two distinct fixed continuum data are resolved and refinement-stable;
- revive the killed Betchov-boundary mechanism as an independent physical transport mechanism;
- reopen S15, FDT, Gamma microgeometry, or fixed-profile ancient-Euler lanes without satisfying their recorded reopen conditions;
- add Lean plumbing merely for completeness.

## Resume protocol

At substantive resume inspect `PROJECT_GOAL.md`, `SPEC.md`, `AGENTS.md`, `FORMAL_SCOPE.md`, this file, `docs/GPT_WORKFLOW.md`, `docs/LEAN_CI_OPERATIONS.md`, the four M-1 governing records, `resolution_invariant_ic.py`, `resolution_rescue.py`, `nearfar_rescue.py`, external `ns-singularity-certificate-lab@fable5-mainline/FABLE5_NEXT_TASK_AUDIT.md`, current `main`, open PRs, and exact workflow artifacts/logs.

The current objective is evidence-grade mechanism selection and candidate infrastructure only. No current result proves a 3D Navier--Stokes singularity or a global-regularity theorem.
