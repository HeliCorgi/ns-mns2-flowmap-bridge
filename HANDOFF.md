# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: **2026-09-06 JST (forty-seventh session)**.

This is the durable short-form continuation point. Current theorem/source files and merged `main` control accepted state. Open/stacked research PRs and numerical branches are not accepted `main` state until merged.

## Accepted main boundary

Current accepted `main` head at this session start:

`6d70e3c9a8040d7d6e6570f0f62379fdb9b313c9`

(PR #90 merge).

Accepted formal state includes:

- the existing whole-space `R^3` local actual-NS mild stack for real divergence-free Schwartz data, with anchors `MNS2.r3AdmissibleSchwartzDatum_navierStokes` and `MNS2.r3EndpointSafeProjectedMild_navierStokes`;
- the periodic special-family sidecar from PR #92, including `ClayNS.certified_nonzero_periodic_NS` and `ClayNS.clayB_has_nonzero_smooth_specialization`.

The whole-space theorem is local/distributional; the periodic theorem is a special-family global certificate. `ClayNS.ClayB` remains unproved. No Clay A/B/C/D statement is proved.

Latest accepted hosted Lean evidence remains:

- PR #92 head `198f1c68297b1d55aea0a5ea053ca2956e5bb13e`, workflow #277: PASS;
- PR #90 reconciled head `cf8ea8b0ba502223e83c03383abc4187ba1ccfe2`, workflow #278: PASS.

No Lean/runtime formal source changed in sessions 39–47.

## Breakdown analytic state

Merged PR #89 and PR #90 leave the parent B2 middle limb OPEN while parking the Gamma-saturation microgeometry route.

Two later analytic branches remain outside accepted main:

- PR #94 `Research: decide B2 modulation compactness gate` — the exact convective normalization shows slow fitted parameters do not imply shape stationarity; strong compactness is not supplied by current B2 budgets; the fixed-profile ancient/steady-Euler lane is parked.
- PR #95 `Research: audit B2 signed global budgets` — bounded audit of standard exact signed/global identities returns `B2-SIGNED-BUDGET-SELECTION = NO-CHANNEL`.

These analytic records motivate the present numerical pivot but must not be treated as merged main state unless separately integrated.

S15, FDT, Gamma-saturation microgeometry, and the fixed-profile ancient/steady-Euler lane remain parked under their recorded reopen conditions.

## Session 47 — return to numerical candidate / M-1

User commissioned a return to the `SPEC.md` numerical candidate / M-1 lane rather than opening another analytic escape variable.

Current branch:

`numerics/m1-resolution-rescue`

The immediate decision was **not** to invent another observable. The standing M-1 prerequisite is to repair resolution/convergence evidence first.

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

This branch adds a resolution-independent continuum seeding layer instead of silently reusing the old provenance.

## New numerical files

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

An equivalent isolated mock-grid check was run during development and passed (shared-grid difference `0`, Fourier divergence about `3e-17`). The repository script itself has not yet been executed against a checked-out branch in this environment.

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

Durable preregistration for the resolution rescue and stop/go rule.

GO only if at least two genuinely different continuum data produce tail-qualified, refinement-stable growth events with the same residual class carrying the positive surplus after near-field absorption. STOP/park if residual dominance changes with datum/refinement or cannot be resolved without moving to impractical scales.

No post-hoc percentage convergence tolerance is introduced. A mechanism promotion needs a separately justified tolerance/manufactured filter-resolution test, and the highest accepted spatial grid must also be rerun with `dt/2` before moving beyond diagnostic-only status.

## Verification state

No production M-1 rescue simulation has been executed in this ChatGPT environment yet.

Completed development checks:

- new Python source was syntax-checked in isolated form;
- the continuum-seeding construction was checked with an equivalent mock spectral grid: RMS normalization exact to floating precision, shared-grid values identical, Fourier divergence approximately `3e-17`.

Not yet verified here:

- repository execution of `check_resolution_invariant_ic.py`;
- E1R96/E2R128/E3c*/E4c* whole-run screens;
- any rescued filtered near/far run;
- any spatial/time convergence verdict.

Do not report the rescue as numerically passed until those runs exist.

## Next work

Execute the **cheap resolution screen first**, not the filtered diagnostic.

Recommended order:

1. repository self-check `check_resolution_invariant_ic.py`;
2. `E1R96` (analytic fixed datum; simplest unresolved historical case);
3. `E3c64` and `E3c96`;
4. `E4c64` and `E4c96`;
5. `E2R128`;
6. advance to N=128/160/192 only when the previous resolution fails the tail gate or a second qualified resolution is needed for convergence.

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
14. current main, open PRs, branch state, and current numerical outputs.

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
- add Lean plumbing merely for completeness.

The present objective is evidence-grade mechanism selection and candidate infrastructure only. No current result proves 3D Navier--Stokes blow-up or global regularity.
