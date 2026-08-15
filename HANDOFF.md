# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: 2026-08-15 18:25 JST.

This is the short-form continuation point for future GPT/Codex sessions. The repository is expected to be developed primarily through repeated GPT sessions; do not rely on chat history as durable state.

## Resume protocol

Read `docs/GPT_WORKFLOW.md` and follow it. In short, read in order:

1. `PROJECT_GOAL.md`;
2. `SPEC.md`;
3. `AGENTS.md`;
4. `FORMAL_SCOPE.md`;
5. this file;
6. `docs/LEAN_CI_OPERATIONS.md`;
7. current GitHub `main`, relevant `Formal/` files, open PRs, and latest Lean CI.

For research constraints and claim boundaries, the governing specifications control. For the actual formal frontier, current theorem statements and repository state control. If this handoff is stale, update it after inspecting the code.

## Current repository state

Latest merged mathematical PR: **#76 — `Bundle H2 norm fields in real L2`**.

`main` at the start of the current CI transition is `b9a67a3289cc06b53a035c3d171e6c0f301a2b9a`.

Open CI-infrastructure PR: **#77 — `Cut hosted Lean CI usage and add cache`**.

PR #77 head at the last check:

`546c946668c1e52f48cbe220ae0001b4a777930d`

Its first official `leanprover/lean-action@v1` run (#242) failed before compilation because the repository had no committed `lake-manifest.json`. The PR was then updated with a manifest matching pinned mathlib `v4.32.1`. Replacement run **#243** (`31876755438`) was `in_progress` at the time this handoff was written. Check GitHub for the current result; do not assume it passed.

The intended #77 policy is:

- no automatic full Lean rebuild on push to `main`;
- PR-to-`main` required Lean check remains;
- superseded PR runs are cancelled;
- official lean-action restores/saves `.lake` and uses the mathlib cache;
- local/self-hosted Lean becomes the normal compiler path.

See `docs/LEAN_CI_OPERATIONS.md`.

## Documentation transition

A separate branch **`gpt-handoff-protocol`** was prepared from the #77 head so that documentation work does not push another commit to #77 and consume another hosted PR build.

That branch updates/creates:

- `AGENTS.md`;
- `FORMAL_SCOPE.md`;
- `HANDOFF.md`;
- `docs/GPT_WORKFLOW.md`;
- `docs/LEAN_CI_OPERATIONS.md`.

Do not open a PR for this documentation branch while hosted minutes are scarce unless the user intentionally wants to spend the required PR check. Once the #77 workflow policy is safely integrated, move these documentation changes onto `main` using a path that does not unnecessarily trigger another full hosted Lean build.

## Governing project target

Ultimate acceptance target: rigorously establish one of the official Clay/Fefferman Navier--Stokes statements A/B/C/D with the exact official hypotheses and domain.

Current primary physical research track: breakdown side (C/D), preferably unforced `f = 0` when mathematically supportable, with the `R^3` axisymmetric-with-swirl specialization governed by `SPEC.md`.

No current Lean theorem is a Clay result.

## Current formal target

The active near-term theorem target is:

`R3SchwartzConvectionTermSobolevEstimate 3`

from `Formal/R3SchwartzConvectionSobolevReduction.lean`.

The existing reduction converts the one-coordinate convection estimate into the full summed convection estimate once the one-coordinate bound is available.

## Completed infrastructure for the current H³ → H² convection track

### Exact product/convolution representation

`Formal/R3SchwartzProductConvolution.lean` proves the exact Fourier convolution formula for each physical convection summand.

### H² weight geometry and pointwise frequency majorant

The additive Bessel-weight stack includes:

- `Formal/R3H2BesselWeightGeometry.lean`;
- `Formal/R3H2WeightedConvolutionKernel.lean`;
- `Formal/R3H2AdditiveConvolutionWeight.lean`;
- `Formal/R3H2YoungWeightedBridge.lean`;
- `Formal/R3SchwartzConvectionH2FrequencyMajorant.lean`.

It bounds the H²-weighted Fourier norm of one convection summand by two scalar convolution-type integrals.

### Ordinary scalar majorants

`Formal/R3SchwartzConvectionScalarMajorants.lean` defines:

- `r3H2LeftScalarMajorant`;
- `r3H2RightScalarMajorant`.

Lean proves the integrands are integrable, the majorants are nonnegative, and they are exactly ordinary real scalar convolutions of the relevant pointwise norm fields.

The pointwise one-coordinate H² bound is rewritten in terms of these names.

### Real Young Bochner estimates

`Formal/R3YoungRealL1L2Bochner.lean` defines the real `L²(R³)` Young construction and proves:

- translation is norm preserving and continuous;
- the `L²`-valued integrand is Bochner integrable for continuous real `L¹` data;
- `L¹ * L² → L²` Young;
- an argument-order `L² * L¹ → L²` wrapper and bound.

### Norm-field L² bundles

Merged #76 added `Formal/R3SchwartzNormFieldL2.lean`.

It defines:

- `r3SchwartzScalarNormL2`;
- `r3SchwartzVelocityNormL2`;
- `r3H2LeftMajorantYoungL2`;
- `r3H2RightMajorantYoungL2`.

Lean proves the norm-field bundles agree a.e. with the literal pointwise norms, preserve the corresponding `L²` norms, and the two bundled Young candidates satisfy the expected Young bounds.

### H³-side Fourier estimates already available

Relevant existing files include:

- `Formal/R3H2FourierL1Bound.lean`;
- `Formal/R3H2VelocityFourierL1Bound.lean`;
- `Formal/R3H2CoordinateFourierBounds.lean`;
- `Formal/R3H3DerivativeWeightGeometry.lean`;
- `Formal/R3SchwartzDerivativeFrequencyBound.lean`;
- `Formal/R3SchwartzDerivativeH3LpBounds.lean`.

These supply the H³-side `L¹`/`L²` factors intended for the final convection estimate.

## Exact next analytic gate

The missing theorem is an a.e. representative/Fubini identification between the **ordinary pointwise scalar convolutions** and the **bundled `L²` Bochner Young candidates**.

In shorthand, the project still needs to justify

`r3H2LeftScalarMajorant a b  ≈  representative of r3H2LeftMajorantYoungL2 a b`

and

`r3H2RightScalarMajorant a b ≈ representative of r3H2RightMajorantYoungL2 a b`

in the appropriate almost-everywhere sense.

### Do not assume

Do **not** silently identify these objects because their formulas look similar. `L²` elements are equivalence classes, the Bochner convolution is bundled, and the pointwise majorants are ordinary integrals. The bridge needs an actual Lean theorem using representative identities plus Fubini/Bochner-integral machinery, or an equivalent direct `L²` argument.

This is the immediate proof frontier.

## Intended next sequence

1. prove the representative/Fubini bridge for the real Young convolution;
2. specialize it to the left and right H² scalar majorants;
3. obtain `L²` bounds for both ordinary majorants from the bundled Young estimates;
4. insert the existing H³ Fourier `L¹`/`L²` bounds;
5. prove `R3SchwartzConvectionTermSobolevEstimate 3`;
6. use the existing reduction to prove the full `R3SchwartzConvectionSobolevEstimate 3`;
7. only after that connect the estimate to the projected quadratic/mild operator layer.

## Concrete function-space progress already completed

Do not regress to the old statement that only frequency-fiber Stokes/Leray objects exist.

The repository now has genuine bundled `L²(R³; ℂ³)` infrastructure:

- `Formal/R3StokesL2Operator.lean` constructs a Fourier-conjugated bounded Stokes operator;
- `Formal/R3LerayL2Operator.lean` constructs the orthogonal `L²` Leray projector onto the closed solenoidal submodule;
- later bridge files establish relevant Fourier/pointwise identifications and solenoidal preservation.

What is still missing is not “any function-space lift”; the current blocker is the nonlinear Sobolev mapping estimate and the subsequent concrete mild-theory instantiation.

## Hard nonclaims

The repository still does **not** establish:

- Clay A/B/C/D;
- a Navier--Stokes blow-up counterexample;
- arbitrary 3D global regularity;
- a closed-form general solution;
- `R3SchwartzConvectionTermSobolevEstimate 3`;
- a complete local-wellposedness/C¹ solution-map theorem for the concrete `R^3` Navier--Stokes mild problem;
- finite-cylinder-to-Clay-domain transfer;
- discrete-to-continuum promotion of MNS-2 numerics.

## External no-go preflight

Before opening a new singularity mechanism or numerical promotion route, cross-check the read-only Fable5 registry named in `AGENTS.md`. Do not reopen `KILLED`/`REJECTED` routes without an explicit hypothesis escape, and preserve exact conditions on `CONDITIONAL` routes.

This preflight is mainly for new physical/singularity mechanisms. It is not a substitute for the current function-space analytic proof work.

## Lean and GitHub guardrails

- no `sorry`;
- no `admit`;
- no new local `axiom`;
- no source-level `opaque` proof hiding;
- prefer mathlib APIs;
- do not merge an ungreen mathematical PR;
- do not auto-merge unless the user explicitly asks;
- do not use hosted Actions as an interactive compiler while quota is scarce;
- read exact CI logs before attempting a fix.

## Minimal continuation prompt

`@GitHub ns-mns2-flowmap-bridge を docs/GPT_WORKFLOW.md の resume protocol どおり確認して、最新 main/PR/CI と HANDOFF.md を照合して続きから。古い会話より実コードを優先して。`
