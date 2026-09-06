# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: **2026-09-06 JST (forty-eighth session)**.

This is the durable short-form continuation point. Current theorem/source files and merged `main` control accepted state. Open/stacked research PRs and numerical branches are not accepted `main` state until merged.

## Accepted main boundary

Current accepted `main` head at this session start:

`6d824e274cd116036a08ed2781dd1368e89863b8`

(PR #96 merge: `Numerics: preregister M1 resolution rescue`).

Accepted formal state includes:

- the existing whole-space `R^3` local actual-NS mild stack for real divergence-free Schwartz data, with anchors `MNS2.r3AdmissibleSchwartzDatum_navierStokes` and `MNS2.r3EndpointSafeProjectedMild_navierStokes`;
- the periodic special-family sidecar from PR #92, including `ClayNS.certified_nonzero_periodic_NS` and `ClayNS.clayB_has_nonzero_smooth_specialization`.

The whole-space theorem is local/distributional; the periodic theorem is a special-family global certificate. `ClayNS.ClayB` remains unproved. No Clay A/B/C/D statement is proved.

Latest accepted hosted Lean evidence remains:

- PR #92 head `198f1c68297b1d55aea0a5ea053ca2956e5bb13e`, workflow #277: PASS;
- PR #90 reconciled head `cf8ea8b0ba502223e83c03383abc4187ba1ccfe2`, workflow #278: PASS.

No Lean/runtime formal source changed in sessions 39–48.

## Breakdown analytic state

Merged PR #89 and PR #90 leave the parent B2 middle limb OPEN while parking the Gamma-saturation microgeometry route.

The later analytic records remain outside accepted main unless PR #97 is merged:

- `B2-ANCIENT-EULER-COMPACTNESS = NO` from current B2 controls;
- `B2-MODULATION-SHAPE-STATIONARITY = NO` from current hypotheses;
- `B2-MODULATION-STRONG-COMPACTNESS = NO` from current budgets;
- the fixed-profile ancient/steady-Euler lane is parked;
- the old unconditional phrase `interior => quasi-static steady-Euler core` is withdrawn, while the K11 cut `gamma+alpha>=1` itself remains valid.

S15, FDT, Gamma-saturation microgeometry, and the fixed-profile ancient/steady-Euler lane remain parked under their recorded reopen conditions.

## Session 47 — return to numerical candidate / M-1

User commissioned a return to the `SPEC.md` numerical candidate / M-1 lane rather than opening another analytic escape variable.

PR #96 added and merged the resolution-rescue infrastructure. The immediate decision was **not** to invent another observable. The standing M-1 prerequisite is to repair resolution/convergence evidence first.

### Existing run-level resolution audit

The preregistered M-1 rule admits a run into the mechanism verdict only if its spectral tail remains `<= 1e-5` over the whole run.

Stored `experiments/m1_events/results/summary.json` gives:

| run | N | max tail | run-level status |
|---|---:|---:|---|
| E0 | 64 | `2.8691770713435234e-08` | PASS |
| E1 | 64 | `3.969158378526758e-05` | FAIL |
| E3 | 64 | `4.8422283231966924e-05` | FAIL |
| E4 | 64 | `5.9967246781271955e-05` | FAIL |
| E2 | 64 | `9.939773706363298e-04` | FAIL |
| E2b | 96 | `1.3196230254612794e-04` | FAIL |

Thus only E0 currently satisfies the standing **whole-run** resolution rule. Per-snapshot masks in `stateflow_harness.py` do not upgrade E1/E2/E3/E4 to resolved runs.

The existing Yu-structured filtered near/far outputs remain useful only as a hypothesis generator: at locally admissible growth samples, positive near-field stretching is absorbed and the positive surplus is classified as FAR rather than COMM/LOC. This is not yet a cross-datum conclusion because the other runs fail the whole-run tail gate.

### Fixed-datum convergence defect found

The legacy random initializers `ic_random_band` and the random perturbation inside `ic_r4` draw random numbers directly into FFT arrays whose shape depends on `N`.

Therefore holding the RNG seed fixed while changing `N` does **not** define one fixed continuum datum. Old E3/E4 remain valid one-grid diagnostics, but a naive `N=64 -> 96 -> 128` rerun is not a spatial-convergence sequence for one datum.

PR #96 adds a resolution-independent continuum seeding layer instead of silently reusing the old provenance.

## M-1 resolution-rescue files now on main

### `experiments/m1_events/resolution_invariant_ic.py`

Introduces a canonical finite integer-wavevector list, resolution-independent sine/cosine random coefficients, coefficientwise divergence-free projection, and grid sampling of one fixed trigonometric polynomial.

New fixed-datum families:

- `E3c*`: deterministic two-mode backbone plus a 10% resolution-independent low-band perturbation;
- `E4c*`: resolution-independent random band `1 <= |k| <= 2`.

Old E3/E4 data and files are not rewritten.

### `experiments/m1_events/check_resolution_invariant_ic.py`

Deterministic construction self-check for N=24/48:

- historical RMS normalization;
- Fourier divergence to roundoff;
- exact agreement on shared physical grid points;
- invariant Fourier coefficient norm.

### `experiments/m1_events/resolution_rescue.py`

Cheap fail-closed whole-run screen performed **before** the expensive filtered near/far diagnostics.

Every accepted RK4 step records/updates:

- spectral tail and full-run maximum tail;
- finite-value status;
- kinetic energy and maximum positive single-step relative energy growth.

At `0.1` physical-time cadence it additionally records enstrophy, maximum vorticity, and an advective CFL diagnostic.

Preregistered ladder:

- E1 Taylor--Green: `E1R96`, then `E1R128` if needed/valuable;
- E2 antiparallel tubes: `E2R128`, then `E2R160`, then `E2R192` only as needed;
- fixed-continuum E3c and E4c: N=64,96,128 with `dt` proportional to `1/N`.

A run advances only if `max_tail <= 1e-5` over the entire interval and all values remain finite.

### `experiments/m1_events/nearfar_rescue.py`

Runs the expensive existing `nearfar_yu.snapshot` diagnostic only after the matching resolution-screen JSON reports `tail_pass=true` and `finite_pass=true`. It refuses unresolved runs.

### `experiments/m1_events/M1_RESOLUTION_RESCUE_PREREG_2026-09-06.md`

GO only if at least two genuinely different continuum data produce tail-qualified, refinement-stable growth events with the same residual class carrying the positive surplus after near-field absorption. STOP/park if residual dominance changes with datum/refinement or cannot be resolved without moving to impractical scales.

No post-hoc percentage convergence tolerance is introduced. A mechanism promotion needs a separately justified tolerance/manufactured filter-resolution test, and the highest accepted spatial grid must also be rerun with `dt/2` before moving beyond diagnostic-only status.

## Session 48 — PR #97 repair and first repository M-1 execution

The user reported an error on PR #97. Inspection showed **no CI failure** on its old head. The error was a stale-branch merge conflict after PR #96 advanced `main`, primarily because both histories changed `HANDOFF.md`.

PR #97 was synchronized with current `main` by a two-parent merge commit while retaining only its three analytic research documents over the post-#96 tree:

- branch: `research/b2-ancient-euler-compactness`;
- synchronized head: `ffec0c9ec667daf12387231407ea943a2106ccb8`;
- PR #97 is now open and mergeable, not merged;
- the stale branch-local `HANDOFF.md` was deliberately replaced by current-main M-1 handoff content;
- PR title/body were repaired to state the actual analytic claim boundary.

Do not merge PR #97 without explicit user instruction. Numerical M-1 remains the active lane.

### First execution branch / PR

Current numerical branch:

`numerics/m1-resolution-run1`

Current PR:

PR #98 `Numerics: run first M1 resolution rescue screen`.

A focused workflow `.github/workflows/m1-resolution-rescue.yml` was added. It runs:

1. the exact repository `check_resolution_invariant_ic.py` self-check;
2. only after that passes, the preregistered `E1R96` whole-run screen;
3. uploads `E1R96.json` as `m1-e1r96-resolution-screen`.

Scientific `tail_pass=false` is **not** converted into a red CI result; exceptions, non-finite state, timeout, missing artifact, and self-check failure remain infrastructure failures.

Workflow run #1 / run id `34005384433` is the relevant numerical run.

Verified so far on the actual PR checkout:

- `seed-self-check`: **PASS**;
- exact output: `PASS shared=0.000e+00 coeff_norm_delta=4.441e-16`;
- Python 3.12.14, NumPy 2.5.2, SciPy 1.18.1 on Ubuntu 24.04 hosted runner;
- `e1r96-screen`: **IN PROGRESS** at this handoff update.

A local/container reproduction made from the current-main source fragments gave the same self-check output before the hosted run. The hosted PR checkout is the revision-qualified evidence.

Opening PR #98 also triggered the repository's ordinary Lean PR workflow even though no Lean source changed. Do not interpret that unrelated check as numerical evidence; no Lean theorem frontier changes in this PR.

## Next work

First inspect workflow run `34005384433` and the `E1R96` artifact/result.

If `E1R96` has `tail_pass=true` and `finite_pass=true`, it becomes eligible for `nearfar_rescue.py`; this is still one-datum periodic evidence only. If it fails the tail gate, proceed to `E1R128` before any near/far diagnostic for Taylor--Green.

After the E1 decision, continue the preregistered order:

1. `E3c64` and `E3c96`;
2. `E4c64` and `E4c96`;
3. `E2R128`;
4. advance to N=128/160/192 only when the previous resolution fails the tail gate or a second qualified resolution is needed for convergence.

Only after a run passes the **whole-run** tail gate may `nearfar_rescue.py` be run for it.

If at least two distinct fixed continuum data become resolved, compare growth-event timing and the axes `A_N`, `A_F`, `A_C`, `A_L`, `g`, residual-class labels, `R/dx`, `ell/dx`, and filtered-budget residual on common physical times before selecting a mechanism.

## Resume protocol

At substantive resume read:

1. `PROJECT_GOAL.md`;
2. `SPEC.md`;
3. `AGENTS.md`;
4. `FORMAL_SCOPE.md`;
5. this `HANDOFF.md`;
6. `docs/GPT_WORKFLOW.md`;
7. `docs/LEAN_CI_OPERATIONS.md`;
8. `experiments/m1_events/PREREG.md`;
9. `M1_INDEPENDENT_PROBE/M1_INDEPENDENT_PROBE_2026-09-04.md`;
10. `Stateflow M-1/M1_BOUNDARY_LOCALIZATION_ESTIMATE_AUDIT_2026-09-04.md`;
11. `experiments/m1_events/M1_RESOLUTION_RESCUE_PREREG_2026-09-06.md`;
12. `resolution_invariant_ic.py`, `resolution_rescue.py`, `nearfar_rescue.py`;
13. external `FABLE5_NEXT_TASK_AUDIT.md` numerical guardrails;
14. current main, PR #97, PR #98, and current numerical outputs/artifacts.

## Claim boundary / forbidden shortcuts

Do not:

- claim Clay A/B/C/D or numerical blow-up;
- call periodic M-1 data an `R^3` candidate;
- treat a per-snapshot stateflow mask as repair of a globally unresolved run;
- compare old E3/E4 at different `N` as one fixed-datum convergence sequence;
- run the expensive near/far diagnostic before the corresponding whole-run tail screen passes;
- select a convergence tolerance after seeing which tolerance makes the desired mechanism pass;
- call the historical FAR pattern universal before at least two distinct fixed continuum data are resolved and refinement-stable;
- reopen parked analytic lanes merely because numerical data are inconclusive;
- identify a scientific tail FAIL with a software/CI failure;
- add Lean plumbing merely for completeness.

The present objective is evidence-grade mechanism selection and candidate infrastructure only. No current result proves 3D Navier--Stokes blow-up or global regularity.
