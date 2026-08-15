# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: 2026-08-15 18:57 JST.

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

Current `main` before this handoff sync was:

`d5846f8618a65af52b5c8a5d61f101e67502ceb7`

which merged **PR #78 — `Gpt handoff protocol`**.

Latest merged mathematical PR remains **#76 — `Bundle H2 norm fields in real L2`**.

CI migration **PR #77 — `Cut hosted Lean CI usage and add cache`** is merged. Its replacement Lean run **#243** (`31876755438`) completed successfully after committing `lake-manifest.json` for the pinned dependency graph.

Documentation PR **#78** also completed Lean run **#244** (`31877304381`) successfully and is merged.

At the last check there were **no open pull requests**.

The active hosted-CI policy is now:

- PRs to `main` emit the Lean required check;
- automatic full Lean rebuilds on pushes to `main` are disabled;
- superseded PR runs are cancelled;
- `leanprover/lean-action@v1` restores/saves `.lake` and uses the mathlib cache;
- local/self-hosted Lean is the preferred normal compiler path;
- `workflow_dispatch` remains available.

See `docs/LEAN_CI_OPERATIONS.md`.

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

### Real Young Bochner estimates

`Formal/R3YoungRealL1L2Bochner.lean` defines the real `L²(R³)` Young construction and proves:

- translation is norm preserving and continuous;
- the `L²`-valued integrand is Bochner integrable for continuous real `L¹` data;
- `L¹ * L² → L²` Young;
- an argument-order `L² * L¹ → L²` wrapper and bound.

### Norm-field L² bundles

Merged #76 added `Formal/R3SchwartzNormFieldL2.lean`, defining:

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

`r3H2LeftScalarMajorant a b  ≈ representative of r3H2LeftMajorantYoungL2 a b`

and

`r3H2RightScalarMajorant a b ≈ representative of r3H2RightMajorantYoungL2 a b`

in the appropriate almost-everywhere sense.

### Do not assume

Do **not** silently identify these objects because their formulas look similar. `L²` elements are equivalence classes, the Bochner convolution is bundled, and the pointwise majorants are ordinary integrals. The bridge needs an actual Lean theorem using representative identities plus Fubini/Bochner-integral machinery, or an equivalent direct `L²` argument.

Pinned mathlib `Mathlib/Analysis/Convolution.lean` explicitly still lists general `L^p` convolution measurability/existence results as TODOs, so do not assume a ready-made generic Young-convolution theorem is present.

This is the immediate proof frontier.

## Intended next sequence

1. prove the representative/Fubini bridge for the real Young convolution, or an equivalent direct `L²` theorem for the ordinary scalar convolution;
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

The current ChatGPT execution environment has no local `lean`/`lake` binary. Therefore, a new mathematical change should be kept narrow and must not be reported as proved until reproduced by a local/self-hosted/pinned Lean build.

## Minimal continuation prompt

`@GitHub ns-mns2-flowmap-bridge を docs/GPT_WORKFLOW.md の resume protocol どおり確認して、最新 main/PR/CI と HANDOFF.md を照合して続きから。古い会話より実コードを優先して。`
