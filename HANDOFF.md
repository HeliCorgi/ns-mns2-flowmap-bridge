# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: **2026-09-07 JST (fifty-second session)**.

This is the durable continuation point. Merged `main` controls accepted repository state; draft/stacked PR numerical artifacts are evidence only for the exact revisions and runs recorded below. No current result proves Clay A/B/C/D.

## Accepted main boundary

Accepted `main` at the start of this numerical stack is the post-PR-#100 state. The formal boundary is unchanged by sessions 51–52:

- whole-space `R^3` local actual-NS mild stack for real divergence-free Schwartz data, including `MNS2.r3AdmissibleSchwartzDatum_navierStokes` and `MNS2.r3EndpointSafeProjectedMild_navierStokes`;
- periodic special-family sidecar from PR #92, including `ClayNS.certified_nonzero_periodic_NS` and `ClayNS.clayB_has_nonzero_smooth_specialization`;
- `ClayNS.ClayB` remains defined but unproved.

The strongest whole-space theorem remains local in time and distributional in space. The periodic shear theorem is a genuine global special solution, not universal Clay B. No Lean/formal source changed in the active numerical work, so `FORMAL_SCOPE.md` and `STATUS.md` remain unchanged.

## Breakdown analytic state

The parent B2 middle limb remains **OPEN**, but current in-house analytic sublanes stay parked/narrowed:

- S15 `(q,d)` cone parked after pressure and fourth-jet counterfamilies;
- FDT cross-track parked under its deformation/Cauchy-Green reopen conditions;
- Gamma flat-top/residence sublane parked; transition-vorticity lower bound survives;
- fixed-profile ancient/steady-Euler route parked;
- `B2-ANCIENT-EULER-COMPACTNESS = NO`;
- `B2-MODULATION-SHAPE-STATIONARITY = NO`;
- `B2-MODULATION-STRONG-COMPACTNESS = NO`;
- K11's exponent cut remains valid; the old unconditional phrase `interior => quasi-static steady-Euler core` is withdrawn.

Do not reopen these lanes merely because the numerical M-1 program is inconclusive.

## Active lane — periodic M-1 resolution rescue / mechanism selection

Governing records:

- `experiments/m1_events/PREREG.md`;
- `M1_INDEPENDENT_PROBE/M1_INDEPENDENT_PROBE_2026-09-04.md`;
- `Stateflow M-1/M1_BOUNDARY_LOCALIZATION_ESTIMATE_AUDIT_2026-09-04.md`;
- `experiments/m1_events/M1_RESOLUTION_RESCUE_PREREG_2026-09-06.md`;
- `experiments/m1_events/M1_E3C_NEARFAR_R1R2_RESULT_2026-09-06.md`;
- `experiments/m1_events/M1_E4C_R0_RESULT_2026-09-06.md`;
- `experiments/m1_events/M1_FILTER_RESOLUTION_CALIBRATION_PREREG_2026-09-06.md`;
- `experiments/m1_events/M1_FILTER_RESOLUTION_CALIBRATION_PREREG_ADDENDUM_2026-09-06.md`.

This is periodic `T^3` evidence-grade work only. It is not an `R^3` candidate and not a blow-up/regularity theorem.

Standing fail-closed R0 gate:

```text
max_tail <= 1e-5 over the entire run
and finite numerical state
```

Per-snapshot masks do not repair a globally unresolved run. Legacy E3/E4 array-seeded random data are not fixed continuum data across changing `N`; only E3c/E4c continuum-seeded families may be used for same-datum refinement.

## Session 51 — E3c R1/R2

PR #102 `Numerics: run E3c near/far R1-R2 refinement gate` is intentionally **DRAFT / UNMERGED**.

R0-qualified pair:

```text
E3c96  max_tail = 3.274744131023e-07  PASS
E3c128 max_tail = 2.845872144398e-09  PASS
```

R1/R2 workflow `M-1 E3c near-far R1-R2`, run id `34017370158`, numerical head `10b55fd43ad34fa8bddf971509311cefdbc13bd5`.

R1 artifacts:

- E3c96 id `9984447543`, digest `sha256:445c4cbbb0c9431a2d1bc14cc589b01d06941b733569576b5c0310b02975ada7`;
- E3c128 id `9984844033`, digest `sha256:8f0722332854e022c3a0976d015e46ee4a36fda0a0c2158235148ee2b422970e`;
- R2 id `9984845801`, digest `sha256:89e3284a6c3e377de9b4d32df38d2bf7b1f846d8e2b3dca38f1affccb3f6b320`.

Both resolutions identify the same sampled global enstrophy-growth event:

```text
t = 0.1 -> 1.8
E3c96 : 2059.1878655576575 -> 4681.591249147496
E3c128: 2059.1878657581206 -> 4681.591072571599
```

Categorical near/far comparison on common positive-global-growth samples:

- `(c,sigma)=(16,0.125)`: `17/17`, all `FAR -> FAR`;
- `(16,0.25)`: `16/17`, one `FAR -> NO_POSITIVE_LOCAL_GROWTH` at `t=1.4`;
- `(32,0.125)`: `10/10`, seven FAR and three no-positive-local-growth on both grids;
- `(32,0.25)`: `10/10`, all no-positive-local-growth;
- `c=8`: one `NEAR_NOT_ABSORBED -> FAR` mismatch at `t=0.7` for each sigma.

Exact decision:

```text
M1-E3c-R1-EXECUTION = PASS
M1-E3c-GLOBAL-GROWTH-EVENT-96/128 = STABLE (numerical observation)
M1-E3c-FAR-CATEGORICAL-STABILITY = PROMISING BUT LADDER-CONDITIONAL
M1-E3c-MECHANISM-PROMOTION = NOT YET
```

No percentage convergence threshold or post-hoc `ell/dx` cutoff was selected.

## Session 52 — E4c R0 pair qualification

PR #103 `Numerics: screen fixed-continuum E4c64/96 R0 pair` is **DRAFT / STACKED ON #102 / UNMERGED**. Its base is `numerics/m1-e3c-nearfar-r1r2`, not `main`.

The same continuum datum `ic_e4_continuum` is used at all resolutions.

### E4c64 / E4c96

Workflow `M-1 E4c R0 resolution pair`, run id `34019449248`, numerical head `61fc0e00e43f4c6537a1e30ebe8e8a28bde81475`.

```text
E4c64
N = 64, dt = 1/80
max_tail = 7.564561392480e-05
finite_pass = True
R0 = FAIL
artifact id = 9985002533
digest = sha256:f366ea3072b2165b6a78917b0e284ea9a7dc17ec40ab687801dc40d89c454c07

E4c96
N = 96, dt = 1/120
max_tail = 1.134755892947e-06
finite_pass = True
R0 = PASS
artifact id = 9985091027
digest = sha256:ca63edd772797ad325e819b682f8187f6aa1500eb34484400e0c30cd5ddae8da
```

Because only E4c96 passed, the preregistered ladder required E4c128.

### E4c128

The first E4c128 attempt was cancelled by a documentation commit and is discarded. Replacement workflow `M-1 E4c128 R0 resolution screen`, run id `34020092555`, job id `101451020079`, numerical head `c02c17301d154a3388ca7da9d8bb40c5ec1dbc67`, completed successfully.

```text
N = 128
nu = 0.02
T = 6.0
dt = 1/160
max_tail = 3.536985710923e-08
tail_pass = True
finite_pass = True
max_relative_single_step_energy_growth = 0
walltime_s = 1717.853
```

Artifact:

- id `9985610481`;
- digest `sha256:9f17b8e926f9a90c69b33a61701a22e724a15da46931e3e19f8eb914d1aeef88`.

### Same-datum E4c96/E4c128 global event

Both retained grids identify the same sampled growth event:

```text
t = 0.1 -> 1.8
E4c96 : 1930.6694699911316 -> 4138.01500670631
E4c128: 1930.6694702433779 -> 4138.014223376773
```

Across common outputs, maximum relative differences are approximately:

```text
energy        1.2364e-07
enstrophy     2.2052e-07
max_vorticity 1.3724e-02
advective_CFL 5.8685e-03
```

Exact decision:

```text
M1-E4c64-R0 = FAIL
M1-E4c96-R0 = PASS
M1-E4c128-R0 = PASS
M1-E4c-GLOBAL-GROWTH-EVENT-96/128 = STABLE (numerical observation)
M1-E4c-R0-PAIR = QUALIFIED at N=96,128
```

E4c64 is excluded. Only E4c96/E4c128 may enter E4c R1/R2.

## Filter-resolution calibration

A separate branch `numerics/m1-filter-calibration` was created from the E4c stack before applying any production-label tolerance. It contains:

- `M1_FILTER_RESOLUTION_CALIBRATION_PREREG_2026-09-06.md`;
- its no-discretion addendum;
- `filter_resolution_calibration.py`.

The calibration uses three explicit non-production divergence-free trigonometric fields, fixed physical geometry, grids `64,96,128,160,192`, and frozen `ell/dx` bins. It defines empirical envelopes

```text
eps_q(B) = max_manufactured ( |q_N-q_192| + |q_160-q_192| )
```

for `q in {A_N,g,B_F,B_C,B_L}`. Every finite N160/N192 disagreement is retained as a penalty rather than censored by a post-hoc stability percentage.

Production FAR/COMM/LOC labels count only when their sign/order margins exceed the frozen binwise envelopes on each grid independently. This is empirical numerical certification, not a rigorous continuum error theorem.

## Next work

1. Execute the manufactured filter-resolution calibration exactly as preregistered and freeze the resulting envelopes before applying them to E3c/E4c.
2. Run E4c96/E4c128 through the unchanged Yu-structured `nearfar_rescue.py`, compare at common physical times, then apply only the frozen calibration rule.
3. Re-evaluate E3c labels under the same frozen calibration envelope.
4. If two genuinely different continuum data retain the same certified residual mechanism, perform the preregistered highest-grid `dt/2` checks before any mechanism promotion.
5. If calibration cannot certify the relevant scales, or E3c/E4c select different residual classes, STOP/PARK the filtered near/far M-1 mechanism rather than inventing another threshold.

## Commission boundaries / forbidden shortcuts

Do **not**:

- merge PR #102 or #103 without explicit user instruction;
- claim Clay A/B/C/D, numerical blow-up, or numerical global regularity;
- call periodic M-1 an `R^3` candidate;
- identify CI success with scientific tail-gate success;
- use E3c64 or E4c64 in mechanism verdicts;
- compare legacy E3/E4 at different `N` as one fixed continuum datum;
- call E3c96/128 or E4c96/128 a continuum convergence theorem;
- infer a universal FAR law from raw same-grid categorical agreement;
- select a percentage convergence tolerance or `ell/dx` cutoff after inspecting production labels;
- relax the manufactured calibration envelope if it makes FAR ambiguous;
- discard the E3c mismatches post hoc;
- revive the killed Betchov-boundary mechanism as an independent transport mechanism;
- reopen S15, FDT, Gamma residence, or fixed-profile ancient-Euler lanes without their recorded reopen conditions;
- add Lean plumbing merely for completeness.

## Resume protocol

At substantive resume inspect `PROJECT_GOAL.md`, `SPEC.md`, `AGENTS.md`, `FORMAL_SCOPE.md`, this file, `docs/GPT_WORKFLOW.md`, `docs/LEAN_CI_OPERATIONS.md`, the M-1 governing records, `resolution_invariant_ic.py`, `resolution_rescue.py`, `nearfar_rescue.py`, `compare_nearfar_refinement.py`, `filter_resolution_calibration.py`, current `main`, open PRs, and exact workflow artifacts/logs.

The current objective is evidence-grade mechanism selection and candidate infrastructure only. No current result proves a 3D Navier–Stokes singularity or global regularity.