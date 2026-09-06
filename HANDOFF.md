# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: **2026-09-07 JST (fifty-fourth session)**.

This is the durable continuation point. Merged `main` controls accepted repository state; draft/stacked PRs and numerical artifacts are evidence only for the exact revisions/runs recorded below. No current result proves Clay A/B/C/D.

## Accepted main boundary

Current accepted `main` head:

`4c85971a936dec68b69d17dd451989e14e4f5556`

(PR #100 merge: `Numerics: screen fixed-continuum E3c128 refinement`).

Formal state is unchanged by the active numerical stack:

- whole-space `R^3` local actual-NS mild stack for real divergence-free Schwartz data, including `MNS2.r3AdmissibleSchwartzDatum_navierStokes` and `MNS2.r3EndpointSafeProjectedMild_navierStokes`;
- periodic special-family sidecar from PR #92, including `ClayNS.certified_nonzero_periodic_NS` and `ClayNS.clayB_has_nonzero_smooth_specialization`;
- `ClayNS.ClayB` remains defined but unproved.

No Lean/formal source changed. `FORMAL_SCOPE.md` and `STATUS.md` remain unchanged.

## Breakdown analytic state

The B2 middle limb remains **OPEN**, but the current in-house analytic sublanes remain parked/narrowed: S15 `(q,d)`, FDT deformation route, Gamma flat-top/residence microgeometry, and fixed-profile ancient/steady-Euler. In particular:

```text
B2-ANCIENT-EULER-COMPACTNESS = NO
B2-MODULATION-SHAPE-STATIONARITY = NO
B2-MODULATION-STRONG-COMPACTNESS = NO
```

K11's exponent cut survives; the old unconditional phrase `interior => quasi-static steady-Euler core` is withdrawn. Do not reopen parked lanes merely because M-1 later becomes inconclusive.

## Active lane — periodic M-1 mechanism selection

This is periodic `T^3` evidence-grade work only. It is not an `R^3` candidate and not a blow-up/regularity theorem.

Standing fail-closed R0 gate:

```text
max_tail <= 1e-5 over the entire run
and finite numerical state
```

Legacy E3/E4 array-random initializers cannot be compared across changing `N`; only E3c/E4c fixed-continuum families enter same-datum refinement.

Core records now include:

- `experiments/m1_events/M1_RESOLUTION_RESCUE_PREREG_2026-09-06.md`;
- `experiments/m1_events/M1_E3C_NEARFAR_R1R2_RESULT_2026-09-06.md`;
- `experiments/m1_events/M1_E4C_R0_RESULT_2026-09-06.md`;
- `experiments/m1_events/M1_FILTER_RESOLUTION_CALIBRATION_PREREG_2026-09-06.md` plus both addenda;
- `experiments/m1_events/M1_FILTER_RESOLUTION_CALIBRATION_RESULT_2026-09-07.md`;
- `experiments/m1_events/M1_E3C_CALIBRATED_CERT_RESULT_2026-09-07.md`.

## Open stacked PRs — do not merge without explicit user instruction

### PR #102 — E3c raw R1/R2

`Numerics: run E3c near/far R1-R2 refinement gate` — **DRAFT / UNMERGED**.

R0-qualified E3c pair:

```text
E3c96  max_tail = 3.274744131023e-07  PASS
E3c128 max_tail = 2.845872144398e-09  PASS
```

R1/R2 run `34017370158`, numerical head `10b55fd43ad34fa8bddf971509311cefdbc13bd5`.

Artifacts:

- E3c96 R1 `9984447543`, `sha256:445c4cbbb0c9431a2d1bc14cc589b01d06941b733569576b5c0310b02975ada7`;
- E3c128 R1 `9984844033`, `sha256:8f0722332854e022c3a0976d015e46ee4a36fda0a0c2158235148ee2b422970e`;
- R2 `9984845801`, `sha256:89e3284a6c3e377de9b4d32df38d2bf7b1f846d8e2b3dca38f1affccb3f6b320`.

Both grids identify global enstrophy growth `t=0.1 -> 1.8`. Raw labels were promising but ladder-conditional; no promotion was made.

### PR #103 — E4c R0 qualification

`Numerics: qualify fixed-continuum E4c96/128 R0 pair` — **DRAFT / STACKED ON #102 / UNMERGED**.

```text
E4c64  max_tail = 7.564561392480e-05  FAIL
E4c96  max_tail = 1.134755892947e-06  PASS
E4c128 max_tail = 3.536985710923e-08  PASS
```

Retained artifacts:

- E4c96 `9985091027`, `sha256:ca63edd772797ad325e819b682f8187f6aa1500eb34484400e0c30cd5ddae8da`;
- E4c128 `9985610481`, `sha256:9f17b8e926f9a90c69b33a61701a22e724a15da46931e3e19f8eb914d1aeef88`.

E4c96/E4c128 identify the same sampled global enstrophy-growth event `t=0.1 -> 1.8`. E4c64 is excluded.

### PR #104 — independent filter-resolution calibration

`Numerics: calibrate M1 near-far filter resolution` — **DRAFT / STACKED ON #103 / UNMERGED**.

Five manufactured grids `N=64,96,128,160,192` completed successfully. Frozen-envelope rescue run `34049373265`, job `101530085033`, output artifact:

```text
id = 9994071254
sha256:6d6ca58697a1659d814dc5ae9736e105847ebdd690423d5233997f547129506e
```

Frozen envelope values:

```text
B0: eps_A_N=6.8945663460310835e-3, eps_g=3.5413556715919725e-3,
    eps_B_F=1.960161040038466e-2, eps_B_C=3.19599675328297e-5,
    eps_B_L=2.6387636755327293e-3
B1: eps_A_N=6.475448975403433e-3, eps_g=8.936244899508949e-4,
    eps_B_F=2.4584563268122694e-2, eps_B_C=2.057052509252255e-5,
    eps_B_L=6.695920656003551e-4
B2: eps_A_N=6.628136031402332e-3, eps_g=1.023851486348093e-4,
    eps_B_F=2.4259403812155134e-2, eps_B_C=9.872584358694425e-6,
    eps_B_L=6.761854101378431e-5
B3: NO_CALIBRATION_COVERAGE
B4: eps_A_N=3.881200655061423e-3, eps_g=5.45962783382592e-6,
    eps_B_F=1.3268696673768676e-2, eps_B_C=7.912242151464355e-7,
    eps_B_L=3.3276714978824895e-6
```

Production classification uses signed `B_F=V_far/P`, `B_C=Rcomm/P`, `B_L=Lloc/P`; `A_F` is not a winner score. B3 stays uncertified with no interpolation or borrowing.

### PR #105 — calibrated E3c certification

`Numerics: certify E3c near-far labels with frozen calibration` — **DRAFT / STACKED ON #104 / UNMERGED**.

Workflow:

```text
M-1 E3c calibrated near-far certification
run 34049792061
job 101531200494
head f578cda07f9267f0ad9c9e6a90479785b264e717
PASS
```

Output artifact:

```text
id = 9994185333
sha256:f9a7e8eadddbba79ec42f70324854eb3e7066de97edf38856c645c46d9480d26
```

All 17 common positive-forward global-enstrophy samples are `t=0.1,...,1.7`.

Calibrated pair counts:

```text
(c,sigma)=(16,0.125):
  17 FAR -> FAR

(16,0.25):
  10 FAR -> NUMERICALLY_UNCERTIFIED_RESOLUTION
   7 NUMERICALLY_UNCERTIFIED_RESOLUTION -> FAR

(32,0.125):
   7 FAR -> NUMERICALLY_UNCERTIFIED_RESOLUTION
   3 NO_POSITIVE_LOCAL_GROWTH -> NUMERICALLY_UNCERTIFIED_RESOLUTION

(32,0.25):
  10 NO_POSITIVE_LOCAL_GROWTH -> NO_POSITIVE_LOCAL_GROWTH

c=8, each sigma:
  15 FAR -> FAR
   1 NEAR_NOT_ABSORBED -> FAR
   1 NO_POSITIVE_LOCAL_GROWTH -> NO_POSITIVE_LOCAL_GROWTH
```

Across `(time,c,sigma)` cells the same-certified residual count is:

```text
FAR = 47
COMM = 0
LOC = 0
```

This aggregate is descriptive, not 47 independent trials. The load-bearing result is the complete covered row

```text
(c,sigma)=(16,0.125): 17/17 independently certified FAR/FAR.
```

Exact decision:

```text
M1-E3c-CALIBRATED-CERT-EXECUTION = PASS
M1-E3c-CALIBRATED-CLEAN-ROW-(16,0.125) = 17/17 FAR/FAR
M1-E3c-CALIBRATED-FAR = YES on covered production rows
M1-E3c-CALIBRATED-B3-ROWS = UNCERTIFIED, as preregistered
M1-E3c-MECHANISM-PROMOTION = NOT YET
```

The independent calibration therefore did **not** kill E3c FAR. It removed the uncovered B3 rows from promotion evidence while leaving the clean `(16,0.125)` row intact.

## Next work

Primary next gate:

```text
M1-E4c-R1/R2 + FROZEN-CALIBRATION CERTIFICATION
```

Use only the R0-qualified E4c96/E4c128 pair. Run the unchanged `nearfar_rescue.py`, compare at common physical times, and apply the exact same frozen calibration envelope. Do not modify the filter ladder, B3 coverage, or error margins.

Decision:

- if E4c also supplies a covered, refinement-stable, independently certified FAR row, the two-distinct-datum spatial/mechanism requirement is met numerically and the next step is the preregistered highest-grid `dt/2` confirmation;
- if E4c selects COMM/LOC or cannot be certified on a comparable covered row, STOP/PARK the filtered near/far mechanism rather than retuning calibration.

## Commission boundaries / forbidden shortcuts

Do **not**:

- merge PR #102/#103/#104/#105 without explicit user instruction;
- claim Clay A/B/C/D, numerical blow-up, or numerical global regularity;
- call periodic M-1 an `R^3` candidate;
- use E3c64/E4c64 in mechanism verdicts;
- call E3c96/128 or E4c96/128 continuum convergence theorems;
- infer a universal FAR law from E3c alone;
- select a convergence percentage or `ell/dx` cutoff post hoc;
- relax the frozen calibration envelope;
- borrow/interpolate B3 calibration;
- use `A_F` instead of signed `B_F` for residual winner;
- discard the c=8 near-absorption mismatch;
- revive killed Betchov-boundary mechanics or parked analytic lanes without recorded reopen conditions;
- add Lean plumbing merely for completeness.

## Resume protocol

At substantive resume inspect `PROJECT_GOAL.md`, `SPEC.md`, `AGENTS.md`, `FORMAL_SCOPE.md`, this file, M-1 prereg/result records, `resolution_invariant_ic.py`, `resolution_rescue.py`, `nearfar_rescue.py`, `compare_nearfar_refinement.py`, `filter_resolution_calibration.py`, `certify_nearfar_with_calibration.py`, current `main`, open PRs, and exact Actions artifacts/logs.

Current objective: determine whether the same calibrated residual mechanism survives a second fixed-continuum datum. No current result proves a 3D Navier–Stokes singularity or global regularity.