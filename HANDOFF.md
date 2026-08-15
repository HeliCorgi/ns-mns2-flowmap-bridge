# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: 2026-08-16 JST.

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
- PR #78 (`Gpt handoff protocol`) is merged.
- PR #79 (`R3 young real set integral bridge`) is merged.
- PR #79 head `e1ea4f787d0b16e4e7be6e0ec0db6bcba1864a46` passed Lean run #251 (`31896417121`). The proof-hole/local-axiom scan and cached full Lake build both succeeded.
- Current `main` HEAD is merge commit `a3a455581a086129bf3c6999aab11be7f4cc1a23`.
- At the latest check there are no open PRs.
- Automatic full Lean builds on pushes to `main` remain disabled.
- PR-to-`main` Lean checks remain, with concurrency cancellation and `.lake`/mathlib caching.
- Local/self-hosted Lean is the preferred compiler path; hosted Actions are a scarce fallback.

## Project claim boundary

Ultimate target: an exact official Clay/Fefferman Navier–Stokes A/B/C/D statement.

Current physical research specialization remains the `R^3`, preferably unforced `f = 0`, axisymmetric-with-swirl breakdown track governed by `SPEC.md`.

No current Lean theorem is a Clay result. Do not claim global regularity, blow-up, local well-posedness of the full concrete `R^3` problem, finite-cylinder transfer, or discrete-to-continuum promotion unless separately proved.

## Current formal target

The active near-term target remains

`R3SchwartzConvectionTermSobolevEstimate 3`

from `Formal/R3SchwartzConvectionSobolevReduction.lean`.

Once the one-coordinate term estimate is proved, the existing `.to_convection` reduction supplies the full summed convection estimate with the factor-three summation loss.

## Newly merged infrastructure from PR #79

The former representative/Fubini blocker is now closed on green `main`.

Merged files/theorems include:

- `Formal/R3YoungRealSetIntegralBridge.lean`: generic a.e. representative theorem for the bundled real Young convolution under the stated continuous bounded representative hypotheses;
- `Formal/R3YoungRealConvolutionCommutativity.lean`: real scalar convolution commutativity helper;
- `Formal/R3SchwartzMajorantYoungRepresentative.lean`:
  - `coeFn_r3H2RightMajorantYoungL2_eq_scalarMajorant`;
  - `coeFn_r3H2LeftMajorantYoungL2_eq_scalarMajorant`;
- `Formal/R3SchwartzScalarMajorantL2.lean`: `MemLp`, canonical `L²` bundles, and transferred Young bounds for the two ordinary scalar majorants;
- `Formal/R3SchwartzConvectionH2L2Majorant.lean`:
  - `norm_r3H2WeightedVelocitySchwartz_fourier_convectionTerm_toLp_le_scalarMajorants`;
  - `norm_r3H2WeightedVelocitySchwartz_fourier_convectionTerm_toLp_le_YoungFactors`.

Therefore the old warning

`ordinary scalar convolution majorant = bundled Bochner Young convolution representative`

is no longer the active gap on `main`.

## Active unverified working branch

Branch:

`r3-schwartz-convection-h3-closure`

Latest branch commit at this handoff:

`a1c36f9216d8efaddbe1c31c45abdfcb43833e03`

The branch is two commits ahead of `main` and has no associated workflow run. It is intentionally **not opened as a PR yet** because this ChatGPT runtime has no Lean/Lake binary and hosted Actions should not be used as an interactive compiler.

The branch is **candidate code only until a pinned local/self-hosted Lean build accepts it**.

### Candidate changes

`Formal/R3H2CoordinateFourierBounds.lean`

Drafts the bookkeeping bridge that was explicitly left after #79:

- `fourier_r3SchwartzCoordinate_eq`;
- `integral_norm_fourier_r3SchwartzCoordinate_le_H3`;
- `norm_r3H2WeightedScalarSchwartz_fourier_coordinate_toLp_le_H3`.

The intended exact identity is

`𝓕 (r3SchwartzCoordinate i f) = r3SchwartzCoordinate i (𝓕 f)`.

The proof uses the pinned mathlib Fourier integral formula plus `ContinuousLinearMap.integral_comp_comm`; this application syntax is unverified until Lean runs.

`Formal/R3SchwartzConvectionH3Closure.lean`

Drafts the next analytic combination:

- `norm_r3H2WeightedVelocitySchwartz_fourier_convectionTerm_toLp_le_H3`;
- `norm_r3SchwartzToHsCLM_two_convectionTerm_le_H3`.

The intended per-coordinate bound is

`‖uᵢ ∂ᵢv‖_{H²} ≤ 4 ‖⟨ξ⟩⁻²‖_{L²} Kᵢ ‖u‖_{H³} ‖v‖_{H³}`

where `Kᵢ = r3CoordinateDerivativeFrequencyConstant i` is the already formalized derivative-frequency constant.

## Exact next verification gate

Do not add more mathematical layers before checking these two candidate modules under the pinned toolchain.

Run locally/self-hosted in dependency order:

```bash
bash scripts/lean-ci-local.sh Formal.R3H2CoordinateFourierBounds
bash scripts/lean-ci-local.sh Formal.R3SchwartzConvectionH3Closure
```

If the first target fails, inspect first:

- definitional reduction from Schwartz Fourier evaluation to the underlying `Real.fourier_eq` integral;
- the orientation and elaboration of `(r3CoordinateFiberAux i).integral_comp_comm`;
- simplification of the coordinate map through the Fourier phase scalar.

If the second target fails, inspect first:

- multiplication-order inference in `mul_le_mul_of_nonneg_left/right`;
- the final `ring` normalization of the two identical Young contributions;
- rewriting `norm_r3SchwartzToHsCLM_eq_frequencyCoordinate` with `r3H2WeightedVelocitySchwartz_fourier_eq_frequencyCoordinate`.

## After the working branch is green

Continue in this order:

1. obtain a uniform nonnegative constant over `i : Fin 3` (a finite sum or finite maximum of `r3CoordinateDerivativeFrequencyConstant i` is sufficient; no sharp constant is required);
2. prove `R3SchwartzConvectionTermSobolevEstimate 3`;
3. invoke `.to_convection` to prove `R3SchwartzConvectionSobolevEstimate 3`;
4. only then connect the concrete convection estimate to the projected quadratic / mild-theory layer;
5. update `FORMAL_SCOPE.md` again once the H³→H² theorem boundary actually lands on green `main`.

## Nonclaims / guardrails

- no `sorry`;
- no `admit`;
- no new local `axiom`;
- no source-level `opaque` proof hiding;
- do not report the active branch as proved before Lean verification;
- do not merge an ungreen mathematical PR;
- do not auto-merge unless the user explicitly asks;
- the closed representative/Fubini bridge does not by itself prove the H³→H² convection estimate;
- do not spend hosted Actions as an interactive compiler while quota is scarce.

## Minimal continuation prompt

`@GitHub ns-mns2-flowmap-bridge を docs/GPT_WORKFLOW.md の resume protocol どおり確認して、最新 main/PR/CI と HANDOFF.md を照合して続きから。古い会話より実コードを優先して。`
