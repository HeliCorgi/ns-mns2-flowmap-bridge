# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: 2026-08-15 19:20 JST.

This is the short-form continuation point for future GPT/Codex sessions. The repository is expected to be developed primarily through repeated GPT sessions; do not rely on chat history as durable state.

## Resume protocol

Follow `docs/GPT_WORKFLOW.md`. Read, in order:

1. `PROJECT_GOAL.md`;
2. `SPEC.md`;
3. `AGENTS.md`;
4. `FORMAL_SCOPE.md`;
5. this file;
6. `docs/LEAN_CI_OPERATIONS.md`;
7. current GitHub `main`, relevant `Formal/` files, open PRs, and latest Lean CI.

Current code and theorem statements override stale prose.

## Repository / CI state

- PR #77 (`Cut hosted Lean CI usage and add cache`) is merged.
- Its corrected Lean run #243 (`31876755438`) completed successfully.
- PR #78 (`Gpt handoff protocol`) is merged.
- Its Lean run #244 (`31877304381`) completed successfully.
- At the last check there were no open PRs.
- Automatic full Lean builds on pushes to `main` are disabled.
- PR-to-`main` Lean checks remain, with concurrency cancellation and `.lake`/mathlib caching.
- Local/self-hosted Lean is the preferred compiler path; hosted Actions are a scarce fallback.

`main` before this handoff update was `31fbb516a43ed7fa2ade5e4ecebea51f33a1befe`.

## Project claim boundary

Ultimate target: an exact official Clay/Fefferman Navier–Stokes A/B/C/D statement.

Current physical research specialization remains the `R^3`, preferably unforced `f = 0`, axisymmetric-with-swirl breakdown track governed by `SPEC.md`.

No current Lean theorem is a Clay result. Do not claim global regularity, blow-up, local well-posedness of the full concrete `R^3` problem, finite-cylinder transfer, or discrete-to-continuum promotion unless separately proved.

## Current formal target

The active near-term target is

`R3SchwartzConvectionTermSobolevEstimate 3`

from `Formal/R3SchwartzConvectionSobolevReduction.lean`.

Once the one-coordinate term estimate is proved, the existing `.to_convection` reduction supplies the full summed convection estimate with the factor-three summation loss.

## Merged infrastructure already available

The merged stack contains:

- exact Fourier product/convolution representation for `uᵢ ∂ᵢv`;
- order-two Bessel-weight geometry and the pointwise H² frequency majorant;
- named ordinary scalar majorants `r3H2LeftScalarMajorant` and `r3H2RightScalarMajorant`;
- real bundled `L¹ * L² → L²` / `L² * L¹ → L²` Young estimates;
- norm-field `L²` bundles and bundled Young candidates from merged PR #76;
- H³-side Fourier `L¹`/`L²` estimates for coordinates and coordinate derivatives;
- genuine function-space `L²(R³; ℂ³)` Stokes and Leray operators.

Relevant files include:

- `Formal/R3SchwartzProductConvolution.lean`;
- `Formal/R3SchwartzConvectionH2FrequencyMajorant.lean`;
- `Formal/R3SchwartzConvectionScalarMajorants.lean`;
- `Formal/R3YoungRealL1L2Bochner.lean`;
- `Formal/R3SchwartzNormFieldL2.lean`;
- `Formal/R3H2CoordinateFourierBounds.lean`;
- `Formal/R3SchwartzDerivativeH3LpBounds.lean`;
- `Formal/R3StokesL2Operator.lean`;
- `Formal/R3LerayL2Operator.lean`.

## Active unverified working branch

Branch:

`r3-young-real-set-integral-bridge`

Latest branch commit at the time of this handoff:

`38cb22387b2576c80b4d886c8d0e1ed99b13e67e`

This branch is intentionally **not opened as a PR yet** because the current ChatGPT runtime has no local Lean/Lake binary and hosted Actions should not be used as an interactive compiler while quota is scarce. No workflow run was associated with the branch head at the last check.

The branch is **candidate code only until a pinned local/self-hosted Lean build accepts it**.

### Candidate files on the working branch

`Formal/R3YoungRealSetIntegralBridge.lean`

Drafts the missing representative/Fubini bridge using actual mathlib APIs:

- a.e. representative of `r3L2RealTranslate`;
- a.e. representative of `r3RealYoungL1L2Integrand`;
- finite-set integral identity for the bundled Young convolution via `L2.inner_indicatorConstLp_one` and `integral_inner`;
- transport of an explicit `L²` representative through translations;
- finite-measure product integrability for a continuous uniformly bounded kernel;
- Fubini swap via `integral_integral_swap`;
- local integrability of the ordinary scalar convolution;
- a.e. uniqueness via `ae_eq_of_forall_setIntegral_eq_of_sigmaFinite`.

The intended generic conclusion is

`r3RealYoungL1L2Convolution f g =ᵐ convolution f g₀`

when `g =ᵐ g₀`, `f` is continuous/integrable, and `g₀` is continuous and uniformly bounded.

`Formal/R3YoungRealConvolutionCommutativity.lean`

Drafts the real scalar convolution commutativity helper needed for the left majorant orientation.

`Formal/R3SchwartzMajorantYoungRepresentative.lean`

Drafts the two specializations

- `coeFn_r3H2RightMajorantYoungL2_eq_scalarMajorant`;
- `coeFn_r3H2LeftMajorantYoungL2_eq_scalarMajorant`.

These are the exact a.e. identifications that were missing after PR #76.

`Formal/R3SchwartzScalarMajorantL2.lean`

Drafts:

- `MemLp` proofs for both ordinary scalar majorants;
- canonical `L²` bundles for them;
- equality of those bundles with the existing Young candidates;
- transfer of the existing Young norm bounds to the ordinary majorants.

`Formal/R3SchwartzConvectionH2L2Majorant.lean`

Drafts the lift from the pointwise H² frequency majorant to an `L²` norm estimate for one physical convection summand, first in terms of the two scalar-majorant `L²` norms and then in terms of the four Young factors.

## Exact proof frontier after the branch draft

Do not assume the branch compiles. The next action is **not** to add more mathematics blindly. First run the pinned targeted builds locally/self-hosted, in dependency order:

```bash
bash scripts/lean-ci-local.sh Formal.R3YoungRealSetIntegralBridge
bash scripts/lean-ci-local.sh Formal.R3YoungRealConvolutionCommutativity
bash scripts/lean-ci-local.sh Formal.R3SchwartzMajorantYoungRepresentative
bash scripts/lean-ci-local.sh Formal.R3SchwartzScalarMajorantL2
bash scripts/lean-ci-local.sh Formal.R3SchwartzConvectionH2L2Majorant
```

Fix compiler errors locally without opening a PR merely to obtain compiler feedback.

Likely syntax/inference hotspots to inspect first if Lean fails:

- `L2.inner_indicatorConstLp_one` inference;
- `integral_inner` orientation;
- `Lp.coeFn_compMeasurePreserving` / translated a.e. equality transport;
- `integral_integral_swap` with the restricted first measure;
- `ae_eq_of_forall_setIntegral_eq_of_sigmaFinite` local-integrability arguments;
- `ContinuousLinearMap.mul_apply'` simplification;
- `change`/definitional reduction of the left/right Young candidates;
- `Lp.coeFn_add` and `MemLp.coeFn_toLp` rewrites in the final H² `L²` lift.

The mathlib APIs named above were checked against pinned mathlib `v4.32.1`, but theorem application syntax remains unverified until Lean runs.

## After the working branch is green

Then continue in this order:

1. merge/land the representative and ordinary-majorant `L²` bridge;
2. combine `Formal/R3SchwartzConvectionH2L2Majorant.lean` with the existing H³ coordinate/derivative Fourier estimates;
3. handle the small commutation/bookkeeping gap between `𝓕 (r3SchwartzCoordinate i u)` and the coordinate of `𝓕 u` if it is not already available under a reusable theorem;
4. obtain a uniform constant over `i : Fin 3` (a finite sum/max of the nonnegative derivative-frequency constants is sufficient if no sharper unit-coordinate lemma is used);
5. prove `R3SchwartzConvectionTermSobolevEstimate 3`;
6. invoke the existing reduction for the full `R3SchwartzConvectionSobolevEstimate 3`;
7. only then connect the resulting nonlinear estimate to the projected quadratic / mild-theory layer.

## Nonclaims / guardrails

- no `sorry`;
- no `admit`;
- no new local `axiom`;
- no source-level `opaque` proof hiding;
- do not report the working branch as proved before Lean verification;
- do not merge an ungreen mathematical PR;
- do not auto-merge unless the user explicitly asks;
- do not silently identify ordinary convolution with bundled Bochner convolution;
- do not spend hosted Actions as an interactive compiler while quota is scarce.

## Minimal continuation prompt

`@GitHub ns-mns2-flowmap-bridge を docs/GPT_WORKFLOW.md の resume protocol どおり確認して、最新 main/PR/CI と HANDOFF.md を照合して続きから。古い会話より実コードを優先して。`
