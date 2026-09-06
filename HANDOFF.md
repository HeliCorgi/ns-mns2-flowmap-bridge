# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: **2026-09-07 JST (fifty-third session)**.

This is the durable continuation point. Merged `main` controls accepted repository state. Draft/stacked PRs and numerical artifacts are evidence only for the exact revisions/runs recorded below. No current result proves Clay A/B/C/D.

## Accepted main boundary

Current accepted `main` head:

`4c85971a936dec68b69d17dd451989e14e4f5556`

(PR #100 merge: `Numerics: screen fixed-continuum E3c128 refinement`).

Formal state is unchanged by sessions 51–53:

- whole-space `R^3` local actual-NS mild stack for real divergence-free Schwartz data, including `MNS2.r3AdmissibleSchwartzDatum_navierStokes` and `MNS2.r3EndpointSafeProjectedMild_navierStokes`;
- periodic special-family sidecar from PR #92, including `ClayNS.certified_nonzero_periodic_NS` and `ClayNS.clayB_has_nonzero_smooth_specialization`;
- `ClayNS.ClayB` remains defined but unproved.

No Lean/formal source changed in the active numerical stack. `FORMAL_SCOPE.md` and `STATUS.md` remain unchanged.

## Breakdown analytic state

The B2 middle limb remains **OPEN**, but current in-house analytic sublanes stay parked/narrowed:

- S15 `(q,d)` cone parked after pressure and fourth-jet counterfamilies;
- FDT cross-track parked under deformation/Cauchy-Green reopen conditions;
- Gamma flat-top/residence sublane parked; transition-vorticity lower bound survives;
- fixed-profile ancient/steady-Euler route parked;
- `B2-ANCIENT-EULER-COMPACTNESS = NO`;
- `B2-MODULATION-SHAPE-STATIONARITY = NO`;
- `B2-MODULATION-STRONG-COMPACTNESS = NO`;
- K11 exponent cut remains valid; the old unconditional phrase `interior => quasi-static steady-Euler core` is withdrawn.

Do not reopen these lanes merely because M-1 is inconclusive.

## Active lane — periodic M-1 mechanism selection

Governing records:

- `experiments/m1_events/PREREG.md`;
- `M1_INDEPENDENT_PROBE/M1_INDEPENDENT_PROBE_2026-09-04.md`;
- `Stateflow M-1/M1_BOUNDARY_LOCALIZATION_ESTIMATE_AUDIT_2026-09-04.md`;
- `experiments/m1_events/M1_RESOLUTION_RESCUE_PREREG_2026-09-06.md`;
- `experiments/m1_events/M1_E3C_NEARFAR_R1R2_RESULT_2026-09-06.md`;
- `experiments/m1_events/M1_E4C_R0_RESULT_2026-09-06.md`;
- `experiments/m1_events/M1_FILTER_RESOLUTION_CALIBRATION_PREREG_2026-09-06.md`;
- `experiments/m1_events/M1_FILTER_RESOLUTION_CALIBRATION_PREREG_ADDENDUM_2026-09-06.md`;
- `experiments/m1_events/M1_FILTER_RESOLUTION_CALIBRATION_PREREG_COVERAGE_ADDENDUM_2026-09-07.md`;
- `experiments/m1_events/M1_FILTER_RESOLUTION_CALIBRATION_RESULT_2026-09-07.md`.

This is periodic `T^3` evidence-grade numerical work only. It is not an `R^3` candidate and not a blow-up/regularity theorem.

Standing R0 gate:

```text
max_tail <= 1e-5 over the entire run
and finite numerical state
```

A scientific tail failure is not a CI failure. Per-snapshot masks do not repair a globally unresolved run. Legacy E3/E4 random array seeds are not fixed continuum data across `N`; only E3c/E4c are used for same-datum refinement.

## Open numerical stack — do not merge without explicit instruction

### PR #102 — E3c R1/R2

PR #102 `Numerics: run E3c near/far R1-R2 refinement gate` is **DRAFT / UNMERGED**.

R0-qualified pair:

```text
E3c96  max_tail = 3.274744131023e-07  PASS
E3c128 max_tail = 2.845872144398e-09  PASS
```

R1/R2 run `34017370158` used numerical head `10b55fd43ad34fa8bddf971509311cefdbc13bd5`.

Artifacts:

- E3c96 R1 `9984447543`, `sha256:445c4cbbb0c9431a2d1bc14cc589b01d06941b733569576b5c0310b02975ada7`;
- E3c128 R1 `9984844033`, `sha256:8f0722332854e022c3a0976d015e46ee4a36fda0a0c2158235148ee2b422970e`;
- R2 `9984845801`, `sha256:89e3284a6c3e377de9b4d32df38d2bf7b1f846d8e2b3dca38f1affccb3f6b320`.

Both grids identify the sampled global enstrophy-growth event

```text
t = 0.1 -> 1.8
E3c96 : 2059.1878655576575 -> 4681.591249147496
E3c128: 2059.1878657581206 -> 4681.591072571599
```

Raw near/far comparison on common positive-global-growth samples:

- `(c,sigma)=(16,0.125)`: `17/17` `FAR -> FAR`;
- `(16,0.25)`: `16/17`, one `FAR -> NO_POSITIVE_LOCAL_GROWTH` at `t=1.4`;
- `(32,0.125)`: `10/10`, seven FAR/FAR and three no-positive-local-growth/same;
- `(32,0.25)`: `10/10`, all no-positive-local-growth;
- `c=8`: one `NEAR_NOT_ABSORBED -> FAR` mismatch at `t=0.7` for each sigma.

Decision:

```text
M1-E3c-R1-EXECUTION = PASS
M1-E3c-GLOBAL-GROWTH-EVENT-96/128 = STABLE (numerical observation)
M1-E3c-FAR-CATEGORICAL-STABILITY = PROMISING BUT LADDER-CONDITIONAL
M1-E3c-MECHANISM-PROMOTION = NOT YET
```

### PR #103 — E4c R0

PR #103 `Numerics: qualify fixed-continuum E4c96/128 R0 pair` is **DRAFT / STACKED ON #102 / UNMERGED**.

Same-continuum E4c results:

```text
E4c64
max_tail = 7.564561392480e-05
finite = True
R0 = FAIL
artifact 9985002533
sha256:f366ea3072b2165b6a78917b0e284ea9a7dc17ec40ab687801dc40d89c454c07

E4c96
max_tail = 1.134755892947e-06
finite = True
R0 = PASS
artifact 9985091027
sha256:ca63edd772797ad325e819b682f8187f6aa1500eb34484400e0c30cd5ddae8da

E4c128
max_tail = 3.536985710923e-08
finite = True
R0 = PASS
artifact 9985610481
sha256:9f17b8e926f9a90c69b33a61701a22e724a15da46931e3e19f8eb914d1aeef88
```

The qualified E4c96/E4c128 pair identifies the same sampled global growth event:

```text
t = 0.1 -> 1.8
E4c96 : 1930.6694699911316 -> 4138.01500670631
E4c128: 1930.6694702433779 -> 4138.014223376773
```

Maximum relative differences on common outputs are approximately `1.24e-7` in energy, `2.21e-7` in enstrophy, `1.37%` in max vorticity, and `0.587%` in advective CFL.

Decision:

```text
M1-E4c64-R0 = FAIL
M1-E4c96-R0 = PASS
M1-E4c128-R0 = PASS
M1-E4c-GLOBAL-GROWTH-EVENT-96/128 = STABLE (numerical observation)
M1-E4c-R0-PAIR = QUALIFIED at N=96,128
```

Only E4c96/E4c128 may enter E4c R1/R2.

### PR #104 — independent filter-resolution calibration

PR #104 `Numerics: calibrate M1 near-far filter resolution` is **DRAFT / STACKED ON #103 / UNMERGED**.

The calibration uses three explicit non-production divergence-free trigonometric fields, fixed physical geometry, and grids `64,96,128,160,192`. It freezes empirical binwise errors for the signed residual-label quantities without looking at E3c/E4c production values.

Primary manufactured run `34049061871` produced five valid grid artifacts:

- N64 `9993994132`, `sha256:d1f907731ff938cb5841741a44b2b7ea0ce51e838ab72e1abb68225ebf908d16`;
- N96 `9993989152`, `sha256:2e5666cac45392520e951975baf14fe638cf4083009048a9d61aa95fcaf29ac9`;
- N128 `9993997487`, `sha256:f5a40bce399f00e898efe1c7c394f1d3fde79e3039865708d632fe0cc178008e`;
- N160 `9994020260`, `sha256:d37ce9a6578782468d9590d534bbaf3556da30a6fe7f67cc82de743fd046647f`;
- N192 `9994041502`, `sha256:8fb8f8868855e5439f3ca5de6dcfbe08b0fad33cebe478de177612395d8d845c`.

All five grid jobs passed: 18 finite cells each, positive `P`, Fourier divergence at roundoff.

The first aggregate job failed only because its job omitted NumPy installation. It did not alter/invalidate the five source artifacts. Rescue run `34049373265`, job `101530085033`, recovered the exact source artifacts, installed requirements, aggregated, and passed the preregistered coverage check.

Frozen envelope artifact:

- id `9994071254`;
- digest `sha256:6d6ca58697a1659d814dc5ae9736e105847ebdd690423d5233997f547129506e`.

Frozen epsilons:

```text
B0: eps_A_N=6.8945663460310835e-3
    eps_g  =3.5413556715919725e-3
    eps_B_F=1.960161040038466e-2
    eps_B_C=3.19599675328297e-5
    eps_B_L=2.6387636755327293e-3

B1: eps_A_N=6.475448975403433e-3
    eps_g  =8.936244899508949e-4
    eps_B_F=2.4584563268122694e-2
    eps_B_C=2.057052509252255e-5
    eps_B_L=6.695920656003551e-4

B2: eps_A_N=6.628136031402332e-3
    eps_g  =1.023851486348093e-4
    eps_B_F=2.4259403812155134e-2
    eps_B_C=9.872584358694425e-6
    eps_B_L=6.761854101378431e-5

B3: NO_CALIBRATION_COVERAGE

B4: eps_A_N=3.881200655061423e-3
    eps_g  =5.45962783382592e-6
    eps_B_F=1.3268696673768676e-2
    eps_B_C=7.912242151464355e-7
    eps_B_L=3.3276714978824895e-6
```

The B3 empty-bin treatment was frozen before calibration execution. Do not interpolate/borrow adjacent envelopes or add geometry after seeing production labels.

Production certification is now fixed:

- growth sign must exceed `eps_g`;
- near absorption/non-absorption must be separated from `A_N=1` by `eps_A_N`;
- residual winner uses signed `B_F=V_far/P`, `B_C=Rcomm/P`, `B_L=Lloc/P`;
- winner `j` must be positive beyond its envelope and pairwise separated by the sum of both envelopes;
- `A_F=Vp_far/P` is not a residual-winner score;
- B3 production samples are `NUMERICALLY_UNCERTIFIED_RESOLUTION`.

Exact calibration decision:

```text
M1-FILTER-CALIBRATION-FIVE-GRID-EXECUTION = PASS
M1-FILTER-CALIBRATION-ENVELOPE = FROZEN
M1-FILTER-CALIBRATION-B3-COVERAGE = NO
M1-FILTER-CALIBRATION-RIGOROUS-CONTINUUM-BOUND = NO
```

## Next work

Primary next gate:

```text
M1-E3c-CALIBRATED-CERTIFICATION
```

Before spending another long run on E4c near/far, recover the already-computed E3c96/E3c128 R1 artifacts and apply the frozen calibration mechanically on each grid. Compare only independently certified labels at common positive-global-growth samples.

If the relevant E3c evidence remains certified FAR on both grids, proceed to E4c96/E4c128 R1/R2 and apply the same frozen envelope. If E3c becomes mostly ambiguous/uncovered or a different residual is certified, record that outcome without relaxing calibration and reconsider/park the current filtered near/far mechanism.

Only after two distinct data survive calibrated spatial/mechanism certification should the highest-grid `dt/2` checks be run.

## Commission boundaries / forbidden shortcuts

Do **not**:

- merge PR #102, #103, or #104 without explicit user instruction;
- claim Clay A/B/C/D, numerical blow-up, or numerical global regularity;
- call periodic M-1 an `R^3` candidate;
- identify CI success with scientific tail-gate success;
- use E3c64 or E4c64 in mechanism verdicts;
- call E3c96/128 or E4c96/128 a continuum convergence theorem;
- infer universal FAR from raw label agreement;
- choose a convergence percentage or `ell/dx` cutoff post hoc;
- relax the frozen calibration envelope if FAR becomes ambiguous;
- borrow/interpolate calibration into B3;
- use `A_F` in place of signed `B_F` for residual classification;
- discard E3c mismatches post hoc;
- revive the killed Betchov-boundary mechanism as an independent transport mechanism;
- reopen S15, FDT, Gamma residence, or fixed-profile ancient-Euler lanes without recorded reopen conditions;
- add Lean plumbing merely for completeness.

## Resume protocol

At substantive resume inspect `PROJECT_GOAL.md`, `SPEC.md`, `AGENTS.md`, `FORMAL_SCOPE.md`, this file, `docs/GPT_WORKFLOW.md`, `docs/LEAN_CI_OPERATIONS.md`, the M-1 governing/result records, `resolution_invariant_ic.py`, `resolution_rescue.py`, `nearfar_rescue.py`, `compare_nearfar_refinement.py`, `filter_resolution_calibration.py`, current `main`, open PRs, and exact Actions artifacts/logs.

The current objective is evidence-grade mechanism selection and candidate infrastructure only. No current result proves a 3D Navier–Stokes singularity or global regularity.