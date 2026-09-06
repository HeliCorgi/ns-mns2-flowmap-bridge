# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: **2026-09-06 JST (fifty-first session)**.

This is the durable continuation point. Current theorem/source files and merged `main` control accepted state. Numerical artifacts are evidence only for the exact revisions/runs recorded below. No current result proves Clay A/B/C/D.

## Accepted main boundary

Current accepted `main` head at this session start:

`4c85971a936dec68b69d17dd451989e14e4f5556`

(PR #100 merge: `Numerics: screen fixed-continuum E3c128 refinement`).

Accepted formal state is unchanged:

- whole-space `R^3` local actual-NS mild stack for real divergence-free Schwartz data, anchored by `MNS2.r3AdmissibleSchwartzDatum_navierStokes` and `MNS2.r3EndpointSafeProjectedMild_navierStokes`;
- periodic special-family sidecar from PR #92, including `ClayNS.certified_nonzero_periodic_NS` and `ClayNS.clayB_has_nonzero_smooth_specialization`;
- `ClayNS.ClayB` remains defined but unproved.

The strongest whole-space theorem is local in time and distributional in space. The periodic shear theorem is a genuine global special solution, not universal Clay B. `FORMAL_SCOPE.md` and `STATUS.md` are intentionally unchanged by the active numerical work.

No Lean/formal source changed in the current numerical lane. Stage-9 formal plumbing remains stopped unless a concrete commissioned theorem consumes a missing formal edge or a semantic defect is found.

## Breakdown analytic state

The parent B2 middle limb remains **OPEN**. Existing narrowed/parked lanes remain unchanged:

- S15 `(q,d)` cone parked after pressure and fourth-jet counterfamilies;
- FDT cross-track parked under its deformation/Cauchy-Green reopen conditions;
- Gamma flat-top/residence sublane parked; transition-vorticity lower bound survives;
- fixed-profile ancient/steady-Euler route parked;
- `B2-ANCIENT-EULER-COMPACTNESS = NO`;
- `B2-MODULATION-SHAPE-STATIONARITY = NO`;
- `B2-MODULATION-STRONG-COMPACTNESS = NO`;
- K11's exponent cut remains valid, but the old unconditional phrase `interior => quasi-static steady-Euler core` is withdrawn.

Do not reopen these lanes merely because the numerical M-1 program is inconclusive.

## Active lane — periodic M-1 resolution rescue / mechanism selection

Governing records:

- `experiments/m1_events/PREREG.md`;
- `M1_INDEPENDENT_PROBE/M1_INDEPENDENT_PROBE_2026-09-04.md`;
- `Stateflow M-1/M1_BOUNDARY_LOCALIZATION_ESTIMATE_AUDIT_2026-09-04.md`;
- `experiments/m1_events/M1_RESOLUTION_RESCUE_PREREG_2026-09-06.md`;
- current result record `experiments/m1_events/M1_E3C_NEARFAR_R1R2_RESULT_2026-09-06.md`.

This is periodic `T^3` evidence-grade work only. It is not an `R^3` candidate and not a blow-up/regularity theorem.

Standing fail-closed R0 gate:

```text
max_tail <= 1e-5 over the entire run
and finite numerical state
```

Per-snapshot masks do not repair a globally unresolved run. Legacy E3/E4 FFT-array random seeds are not fixed continuum data across changing `N`; only E3c/E4c continuum-seeded families may be used for fixed-datum refinement comparisons.

## Accepted numerical results on main before the current draft PR

### E1R96 — PR #98

```text
N = 96
max_tail = 6.086987397920e-07
tail_pass = True
finite_pass = True
```

Artifact `9980926946`, digest `sha256:d15de290da07776781a36a2337723899d0703b7ee01873d0a370bd559dd03c53`.

### E3c64 / E3c96 — PR #99

```text
E3c64: max_tail = 5.956860730357e-05, FAIL, finite
E3c96: max_tail = 3.274744131023e-07, PASS, finite
```

Artifacts:

- E3c64 id `9983329156`, digest `sha256:1ed22f6775fbb347e367b665769e8bce1b83e5675da9575478183deee285758b`;
- E3c96 id `9983371155`, digest `sha256:c8775148c3a9d00614fd474561e14f592711efe799e09934382c8f495000815b`.

### E3c128 — PR #100

```text
N = 128
nu = 0.02
T = 3.5
dt = 1/160
max_tail = 2.845872144398e-09
tail_pass = True
finite_pass = True
max_relative_single_step_energy_growth = 0
```

Workflow run `34015004075`; artifact id `9983774115`, digest `sha256:9f8dd8f4cb79f3d84cab81701b98d85189c3ae74f3b01d56b51788f44455fc8e`.

Therefore E3c96/E3c128 are the first same-continuum-datum pair both qualified at R0. E3c64 remains excluded.

## Session 51 — E3c R1/R2 near/far refinement

Current branch:

`numerics/m1-e3c-nearfar-r1r2`

Current PR:

PR #102 `Numerics: run E3c near/far R1-R2 refinement gate`.

**PR #102 is intentionally DRAFT. Do not merge until the user explicitly decides.**

Numerical workflow head:

`10b55fd43ad34fa8bddf971509311cefdbc13bd5`

Workflow:

`M-1 E3c near-far R1-R2`, run id `34017370158`.

Both R1 jobs recovered and verified the accepted R0 artifacts rather than rerunning R0. Both R1 jobs and downstream R2 completed successfully.

### R1 artifacts

E3c96:

```text
samples = 36
sampled_max_tail = 3.241168846865e-07
walltime_s = 512.641
```

Artifact id `9984447543`, digest `sha256:445c4cbbb0c9431a2d1bc14cc589b01d06941b733569576b5c0310b02975ada7`.

E3c128:

```text
samples = 36
sampled_max_tail = 2.834145621030e-09
walltime_s = 2182.173
```

Artifact id `9984844033`, digest `sha256:8f0722332854e022c3a0976d015e46ee4a36fda0a0c2158235148ee2b422970e`.

R2 artifact:

- id `9984845801`;
- digest `sha256:89e3284a6c3e377de9b4d32df38d2bf7b1f846d8e2b3dca38f1affccb3f6b320`.

### Stable global event

Both resolutions identify the same sampled growth event:

```text
t = 0.1 -> 1.8
E3c96 : 2059.1878655576575 -> 4681.591249147496
E3c128: 2059.1878657581206 -> 4681.591072571599
```

Across all 36 common times, symmetric relative differences are:

```text
E      max 1.143e-07, mean 3.895e-08
Lambda max 1.797e-02, mean 2.046e-03
s_v    max 9.026e-03, mean 1.025e-03
```

This is strong numerical same-datum agreement, not a continuum convergence theorem.

### Near/far categorical result

At the 17 common positive-global-growth samples:

- `(c,sigma)=(16,0.125)`: exact `17/17`, all `FAR -> FAR`;
- `(16,0.25)`: `16/17` exact, with one `FAR -> NO_POSITIVE_LOCAL_GROWTH` mismatch at `t=1.4`;
- `(32,0.125)`: 10 available positive-growth samples, exact `10/10`: `7 FAR->FAR`, `3 NO_POSITIVE_LOCAL_GROWTH->same`;
- `(32,0.25)`: exact `10/10`, but all `NO_POSITIVE_LOCAL_GROWTH`;
- `c=8`: one `NEAR_NOT_ABSORBED -> FAR` mismatch at `t=0.7` for each sigma.

The cleanest continuous comparison is `(32,0.125)`, where mean symmetric relative differences are about `0.294%` (`A_N`), `0.172%` (`A_F`), `0.238%` (`A_C`), and `1.37%` (`g`).

However filter sampling varies substantially. Examples:

```text
(c,sigma)=(16,0.125): ell/dx N96 1.127..1.779, N128 1.503..2.373
(c,sigma)=(32,0.125): ell/dx N96 2.254..2.941, N128 3.006..3.920
(c,sigma)=(32,0.25):  ell/dx N96 4.508..5.882, N128 6.012..7.839
```

No filter-resolution threshold or percentage convergence tolerance was selected after seeing these results.

### Exact decision

```text
M1-E3c-R1-EXECUTION = PASS
M1-E3c-GLOBAL-GROWTH-EVENT-96/128 = STABLE (numerical observation)
M1-E3c-FAR-CATEGORICAL-STABILITY = PROMISING BUT LADDER-CONDITIONAL
M1-E3c-MECHANISM-PROMOTION = NOT YET
```

No common positive-growth sample flips FAR to COMM or LOC. Therefore the result is not a mechanism STOP. But the mixed filter sampling, one near-field absorption mismatch, one local-growth disappearance, and lack of manufactured-test tolerance mean it is also not a GO/promotion decision.

## Next work

The next preregistered numerical gate is:

```text
M1-E4c-R0: run E4c64 and E4c96 whole-run resolution screens.
```

Use the existing fixed-continuum `ic_e4_continuum` family and unchanged R0 threshold. If only one grid passes, follow the already-preregistered ladder to E4c128; do not move the threshold or insert an ad-hoc resolution.

In parallel with or before any cross-datum mechanism promotion, construct the separately justified manufactured/filter-resolution test required by the R2 preregistration. Its tolerance and minimum filter-resolution adequacy must be fixed before applying it to E3c/E4c outputs.

After spatial qualification, the highest accepted grid must later be rerun with `dt/2` before promotion beyond diagnostic-only status.

The broader M-1 GO rule still requires at least two genuinely different continuum data with tail-qualified, refinement-stable growth events and the same residual class carrying positive surplus after near-field absorption.

## Commission boundaries / forbidden shortcuts

Do **not**:

- claim Clay A/B/C/D, numerical blow-up, or numerical global regularity;
- call the periodic M-1 program an `R^3` candidate;
- identify CI success with scientific tail-gate success;
- treat a per-snapshot mask as repair of a globally unresolved run;
- compare legacy E3/E4 at different `N` as one fixed continuum datum;
- use E3c64 in a near/far mechanism verdict;
- call E3c96/E3c128 a continuum convergence theorem;
- infer a universal FAR law from the E3c result;
- select a convergence percentage or filter-resolution cutoff after seeing which value gives the preferred residual class;
- discard the `(16,0.25)` or `c=8` mismatches post hoc;
- call `(32,0.25)` FAR evidence when it has no positive local growth;
- revive the killed Betchov-boundary mechanism as an independent physical transport mechanism;
- reopen S15, FDT, Gamma residence, or fixed-profile ancient-Euler lanes without satisfying recorded reopen conditions;
- add Lean plumbing merely for completeness.

## Resume protocol

At substantive resume inspect `PROJECT_GOAL.md`, `SPEC.md`, `AGENTS.md`, `FORMAL_SCOPE.md`, this file, `docs/GPT_WORKFLOW.md`, `docs/LEAN_CI_OPERATIONS.md`, the M-1 governing records, `resolution_invariant_ic.py`, `resolution_rescue.py`, `nearfar_rescue.py`, `compare_nearfar_refinement.py`, external `ns-singularity-certificate-lab@fable5-mainline/FABLE5_NEXT_TASK_AUDIT.md`, current `main`, open PRs, and exact workflow artifacts/logs.

The current objective is evidence-grade mechanism selection and candidate infrastructure only. No current result proves a 3D Navier--Stokes singularity or a global-regularity theorem.