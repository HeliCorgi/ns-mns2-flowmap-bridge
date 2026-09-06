# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: **2026-09-07 JST (stack integration after sessions 51–55)**.

This is the durable continuation point. Merged `main` controls accepted repository state; Actions artifacts are evidence only for the exact revisions/runs recorded below. No current result proves Clay A/B/C/D.

## Accepted boundary

Immediately before PR #105 integration, `main` is:

`08105f8c89414f628e51dc2fe24afb177531dc6d`

and already includes PR #102 (E3c raw R1/R2), PR #103 (E4c R0 qualification), and PR #104 (independent filter-resolution calibration). This branch is PR #105, the final integration step for the calibrated E3c certification. **After PR #105 is merged, accepted main includes PRs #102–#105.**

Formal state is unchanged by this numerical stack:

- whole-space `R^3` local actual-NS mild stack for real divergence-free Schwartz data, including `MNS2.r3AdmissibleSchwartzDatum_navierStokes` and `MNS2.r3EndpointSafeProjectedMild_navierStokes`;
- periodic special-family sidecar from PR #92, including `ClayNS.certified_nonzero_periodic_NS` and `ClayNS.clayB_has_nonzero_smooth_specialization`;
- `ClayNS.ClayB` remains defined but unproved.

No Lean/formal source changed. `FORMAL_SCOPE.md` and `STATUS.md` remain unchanged.

## Breakdown analytic state

The B2 middle limb remains **OPEN**. Current in-house analytic sublanes remain parked/narrowed: S15 `(q,d)`, FDT deformation route, Gamma flat-top/residence microgeometry, and fixed-profile ancient/steady-Euler. In particular:

```text
B2-ANCIENT-EULER-COMPACTNESS = NO
B2-MODULATION-SHAPE-STATIONARITY = NO
B2-MODULATION-STRONG-COMPACTNESS = NO
```

K11's exponent cut survives; the old unconditional phrase `interior => quasi-static steady-Euler core` is withdrawn.

## Active lane — periodic M-1 mechanism selection

This is periodic `T^3` evidence-grade work only. It is not an `R^3` candidate and not a blow-up/regularity theorem.

Standing fail-closed R0 gate:

```text
max_tail <= 1e-5 over the entire run
and finite numerical state
```

Legacy E3/E4 array-random initializers cannot be compared across changing `N`; only E3c/E4c fixed-continuum families enter same-datum refinement.

### Accepted E3c raw R1/R2 — PR #102

R0-qualified pair:

```text
E3c96  max_tail = 3.274744131023e-07  PASS
E3c128 max_tail = 2.845872144398e-09  PASS
```

R1/R2 workflow run `34017370158`:

- E3c96 R1 artifact `9984447543`, `sha256:445c4cbbb0c9431a2d1bc14cc589b01d06941b733569576b5c0310b02975ada7`;
- E3c128 R1 artifact `9984844033`, `sha256:8f0722332854e022c3a0976d015e46ee4a36fda0a0c2158235148ee2b422970e`;
- R2 artifact `9984845801`, `sha256:89e3284a6c3e377de9b4d32df38d2bf7b1f846d8e2b3dca38f1affccb3f6b320`.

Both identify sampled global enstrophy growth `t=0.1 -> 1.8`. Raw `(c,sigma)=(16,0.125)` was `17/17 FAR->FAR`, but raw labels alone were not promoted.

### Accepted E4c R0 qualification — PR #103

```text
E4c64  max_tail = 7.564561392480e-05  FAIL
E4c96  max_tail = 1.134755892947e-06  PASS
E4c128 max_tail = 3.536985710923e-08  PASS
```

Retained R0 artifacts:

- E4c96 `9985091027`, `sha256:ca63edd772797ad325e819b682f8187f6aa1500eb34484400e0c30cd5ddae8da`;
- E4c128 `9985610481`, `sha256:9f17b8e926f9a90c69b33a61701a22e724a15da46931e3e19f8eb914d1aeef88`.

E4c96/E4c128 identify the same sampled global-enstrophy growth event `t=0.1 -> 1.8`. E4c64 is excluded.

### Accepted independent filter calibration — PR #104

Five manufactured grids `N=64,96,128,160,192` completed. Frozen-envelope rescue run `34049373265`, job `101530085033`, artifact:

```text
9994071254
sha256:6d6ca58697a1659d814dc5ae9736e105847ebdd690423d5233997f547129506e
```

Frozen empirical envelopes:

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

Production classification uses signed `B_F=V_far/P`, `B_C=Rcomm/P`, `B_L=Lloc/P`; `A_F` is not a winner score. B3 remains uncertified with no interpolation or borrowing. This is an empirical numerical calibration, not a rigorous continuum discretization bound.

### Calibrated E3c certification — PR #105

Scientific workflow:

```text
M-1 E3c calibrated near-far certification
run 34049792061
job 101531200494
execution head f578cda07f9267f0ad9c9e6a90479785b264e717
PASS
```

Output artifact:

```text
9994185333
sha256:f9a7e8eadddbba79ec42f70324854eb3e7066de97edf38856c645c46d9480d26
```

All 17 common positive-forward global-enstrophy samples are `t=0.1,...,1.7`.

Load-bearing calibrated result:

```text
(c,sigma)=(16,0.125): 17/17 FAR -> FAR
```

Other rows retain the preregistered uncertainty/mismatch structure; in particular B3 samples remain `NUMERICALLY_UNCERTIFIED_RESOLUTION` and the c=8 near-absorption mismatch is not discarded.

Across all `(time,c,sigma)` cells the descriptive same-certified residual count is:

```text
FAR = 47
COMM = 0
LOC = 0
```

This is not 47 independent trials. Exact decision:

```text
M1-E3c-CALIBRATED-CERT-EXECUTION = PASS
M1-E3c-CALIBRATED-CLEAN-ROW-(16,0.125) = 17/17 FAR/FAR
M1-E3c-CALIBRATED-FAR = YES on covered production rows
M1-E3c-CALIBRATED-B3-ROWS = UNCERTIFIED, as preregistered
M1-E3c-MECHANISM-PROMOTION = NOT YET
```

## Open next gate — PR #106, do not merge yet

PR #106 `Numerics: test E4c with frozen near-far calibration` remains **DRAFT / UNMERGED**. Its preregistration fixes the same load-bearing row `(c,sigma)=(16,0.125)` before E4c execution; no secondary row may rescue the result post hoc.

Scientific workflow run `34060612610`, execution head `0c41109662a0aac1dfd869156089f01d0c1e23d5`, is currently **in progress** at this handoff update. Only the R0-qualified E4c96/E4c128 pair is used.

Decision rule:

```text
GO_TO_DT2
```

only if every common positive-forward global-enstrophy sample on `(16,0.125)` is calibration-covered on both grids and independently certified `FAR->FAR`, with at least one sample. Otherwise:

```text
STOP_PARK_FILTERED_NEARFAR
```

If GO occurs, the next preregistered step is the highest accepted grid `dt/2` confirmation. GO remains a numerical mechanism-selection milestone only.

## Commission boundaries / forbidden shortcuts

Do **not**:

- merge PR #106 before its experiment/result audit and explicit user instruction;
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
- reopen killed Betchov-boundary mechanics or parked analytic lanes without recorded reopen conditions;
- add Lean plumbing merely for completeness.

## Resume protocol

At substantive resume inspect `PROJECT_GOAL.md`, `SPEC.md`, `AGENTS.md`, `FORMAL_SCOPE.md`, this file, current `main`, PR #106, exact Actions artifacts/logs, and the M-1 prereg/result records. Relevant implementation files are `resolution_invariant_ic.py`, `resolution_rescue.py`, `nearfar_rescue.py`, `compare_nearfar_refinement.py`, `filter_resolution_calibration.py`, and `certify_nearfar_with_calibration.py`.

Current objective: determine whether the same independently calibrated FAR residual mechanism survives the second fixed-continuum datum. No current result proves a 3D Navier–Stokes singularity or global regularity.