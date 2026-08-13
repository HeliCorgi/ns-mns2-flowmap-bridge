# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: 2026-08-13 (JST), after merged PR #35.

This file is the short-form continuation point for future GPT/Codex/Claude sessions.

Read, in order:

1. `PROJECT_GOAL.md` — top-level acceptance target;
2. `SPEC.md` — normative contract for the current primary `R^3`, `f = 0`, axisymmetric-with-swirl breakdown track;
3. `AGENTS.md` — repository rules and claim hygiene;
4. `FORMAL_SCOPE.md` — exact Lean theorem boundary;
5. this handoff;
6. the latest GitHub `main`, open PRs, and Lean CI.

## Source-of-truth rule

Progress notes can drift. For **research constraints and claim boundaries**, `PROJECT_GOAL.md`, `SPEC.md`, and `AGENTS.md` control. For the **actual formal frontier**, the current `main` branch, the contents of `Formal/`, the latest PR, and its CI are the source of truth.

Do not infer the current theorem frontier from an old conversation or an old PR number list without checking GitHub.

## Governing project target

Ultimate acceptance target: rigorously establish one of the official Clay/Fefferman Navier--Stokes statements A/B/C/D with the exact official hypotheses and domain.

Current primary attack: the breakdown side (C/D), with an unforced route `f = 0` preferred when supportable. The working research specialization in `SPEC.md` is physical three-dimensional `R^3`, axisymmetric with swirl. Hou-cylinder numerics, MNS-2, flow-map identities, mild-solution semantics, POD/SVD reductions, and Lean theorems are intermediate infrastructure unless a rigorous chain reaches an exact Clay statement.

## Current formal frontier

The merged formal stack now contains four distinct layers.

### 1. Exact flow-map bridge

The repository proves the Banach-valued affine-path identity

`∫₀¹ (DS(x + s d))[d] ds = S(x + d) - S(x)`

under an open admissible domain, `C¹` regularity, and path inclusion. The radial specialization is

`∫₀¹ (DS(s d))[d] ds = S(d) - S(0)`.

The tangent is always the fixed, unnormalized direction `d`.

Key files:

- `Formal/Bridge.lean`
- `Formal/FlowMapFTC.lean`
- `Formal/FlowMapChainRule.lean`
- `Formal/FlowMapOperatorContinuity.lean`
- `Formal/FlowMapContDiffOne.lean`
- `Formal/FlowMapLocalContDiff.lean`
- `Formal/PDEBridgeAdapter.lean`
- `Formal/NavierStokesTimeBridge.lean`

### 2. Abstract mild and tangent semantics

The repository formalizes a Banach-valued Duhamel relation

`u(t) = H(t)u₀ - ∫₀ᵗ H(t-s) B(u(s)) ds`

with existential endpoint witnesses rather than hidden positive-time uniqueness.

For a continuous bilinear `Q`, the quadratic diagonal and derivative are formalized:

`B(u) = Q(u,u)`

`DB(u)[v] = Q(u,v) + Q(v,u)`.

The formal stack also differentiates the parameterized quadratic Duhamel term under explicit dominated-differentiation hypotheses, identifies the derivative of a quadratic mild fixed point by uniqueness of the Fréchet derivative, expands the resulting directional equation into the linearized mild equation, and packages this into derived tangent/coherent-family semantics.

Key files:

- `Formal/MildSolutionSemantics.lean`
- `Formal/MildFlowMapBridge.lean`
- `Formal/MildZeroUniqueness.lean`
- `Formal/QuadraticMildNonlinearity.lean`
- `Formal/QuadraticLinearizedMild.lean`
- `Formal/QuadraticMildTangentAdapter.lean`
- `Formal/QuadraticDuhamelDifferentiation.lean`
- `Formal/QuadraticMildFixedPointDerivative.lean`
- `Formal/QuadraticMildTangentRealization.lean`
- `Formal/QuadraticMildCoherentFamilyAdapter.lean`

The representative derived tangent equation has the intended form

`J(t)h = H(t)h - ∫₀ᵗ H(t-s) (Q(u(s), J(s)h) + Q(J(s)h, u(s))) ds`

under the explicit hypotheses carried by the formal certificates.

### 3. Leray-projected quadratic operator contract

Merged PR #33 added `Formal/LerayProjectedQuadratic.lean`.

`LerayProjectedQuadraticContract` separates:

- a certified solenoidal submodule;
- a continuous linear Leray map;
- a raw continuous bilinear convection map;
- the projected continuous bilinear map used by the mild kernel.

Lean derives, from the contract fields:

- idempotence of the Leray map;
- projected bilinear outputs are solenoidal;
- the quadratic diagonal is solenoidal;
- the exact quadratic derivative is solenoidal;
- the derivative of the packaged mild nonlinearity remains solenoidal.

This is still an operator contract. It does **not** identify the Banach carrier with a concrete function space on `R^3`, nor does it construct physical `P div(u ⊗ v)`.

### 4. Concrete physical `R^3` frequency-fiber symbols

Merged PR #34 added `Formal/R3LerayFrequencySymbol.lean`.

For `R3 := EuclideanSpace ℝ (Fin 3)`, the solenoidal frequency fiber is

`(span ξ)⊥`,

and `r3LeraySymbol ξ` is the orthogonal projection onto that plane. Lean proves:

- `v` is in the fiber iff `inner ξ v = 0`;
- every projected vector is transverse;
- already-transverse vectors are fixed;
- idempotence;
- norm contraction;
- identity at zero frequency;
- annihilation of the longitudinal vector `ξ`;
- the explicit formula

`P(ξ)v = v - ((ξ·v)/|ξ|²) ξ`.

Merged PR #35 added `Formal/R3StokesFrequencySymbol.lean`.

Using the pinned mathlib Fourier convention

`widehat(Δf)(ξ) = -(2π)^2 |ξ|^2 widehat(f)(ξ)`,

the scalar heat/Stokes factor is

`exp(-(2π)^2 ν t |ξ|^2)`.

Lean proves at the frequency-fiber level:

- nonnegative decay rate for `ν ≥ 0`;
- positivity and forward-time bound by one;
- identity at time zero and zero frequency;
- exact semigroup law;
- preservation of the solenoidal fiber;
- exact commutation with the Leray symbol;
- pointwise norm contraction;
- the combined Stokes--Leray symbol lands in the transverse fiber.

These are genuine physical three-dimensional **frequency-fiber** statements. They are not yet a Fourier-transform lift to a PDE function space.

## What is still not formalized

The repository still does **not** prove or construct:

- a Clay A/B/C/D theorem;
- a blow-up counterexample;
- global smoothness or global existence for arbitrary 3D data;
- a closed-form general solution;
- a concrete divergence-free Banach solution space on `R^3` carrying the full mild theory;
- a bounded function-space Leray projector obtained by lifting the matrix-valued frequency symbol;
- a bounded function-space Stokes semigroup obtained by lifting the scalar frequency symbol;
- the physical bilinear convection operator `div(u ⊗ v)` and its Leray projection in the chosen spaces;
- local existence/uniqueness for the concrete `R^3` mild equation;
- `C¹` dependence of that concrete solution map on an admissible open domain;
- continuation of a `C¹` solution map through a possible singular time;
- a rigorous finite-cylinder-to-`R^3` or periodic Clay-domain transfer;
- discrete-to-continuum promotion of the numerical MNS-2 bridge without an explicit convergence theorem.

## Next formal step

The next high-value task is the **function-space lift**.

Preferred order:

1. choose and formalize a concrete `R^3` function-space carrier compatible with the intended local mild theory;
2. lift the scalar Stokes symbol first, because mathlib has scalar Fourier-multiplier infrastructure;
3. prove the semigroup/contraction properties on that carrier;
4. lift the Leray symbol carefully as a matrix/operator-valued multiplier — do not silently treat it as a scalar multiplier;
5. construct the physical projected convection mapping between the required spaces;
6. instantiate `MildEvolutionKernel` with those concrete objects;
7. only then attack local existence, uniqueness, and `C¹` solution-map dependence.

If the concrete function-space lift becomes blocked by missing mathlib infrastructure, isolate the missing theorem/API as a formal contract rather than smuggling the desired boundedness in as an unlabelled assumption.

## Numerical/research track

The numerical MNS-2 bridge remains separate from the continuum Lean theorem. Exact finite-dimensional path identities, reduced tangent reconstruction, POD/SVD, or synthetic Hou-like data are not continuum Navier--Stokes proofs.

Continuum promotion requires explicit convergence of the relevant solution maps and pathwise tangent actions on a common time interval. Finite-cylinder Hou behavior is not an `R^3` or periodic Clay construction without a rigorous domain-transfer theorem.

## External exclusion / no-go registry — mandatory preflight

Before opening a new singularity mechanism, ansatz family, shadowing route, numerical promotion argument, or whole-space interpretation, cross-check the read-only Fable5 registry:

- root: `https://github.com/HeliCorgi/ns-singularity-certificate-lab/tree/fable5-mainline`
- binding verdicts: `https://github.com/HeliCorgi/ns-singularity-certificate-lab/blob/fable5-mainline/docs/research_notes/verification_sprint_v1/VERDICTS.md`
- numerical/whole-space audit: `https://github.com/HeliCorgi/ns-singularity-certificate-lab/blob/fable5-mainline/FABLE5_NEXT_TASK_AUDIT.md`
- equation audit: `https://github.com/HeliCorgi/ns-singularity-certificate-lab/blob/fable5-mainline/docs/equation_audit.md`
- external research rules: `https://github.com/HeliCorgi/ns-singularity-certificate-lab/blob/fable5-mainline/AGENTS.md`

Operational rule:

- `KILLED` / `REJECTED`: do not reopen unless the new route explicitly identifies a hypothesis escape from the recorded obstruction;
- `CONDITIONAL`: preserve the exact condition;
- do not use formulas marked `未確認`, `不整合`, or `誤り` as implementation premises;
- treat `ns-singularity-certificate-lab` as read-only provenance unless the user explicitly requests edits there.

## Hard guardrails

Never claim any of the following unless a new proof actually establishes it:

- the Clay Navier–Stokes problem is solved;
- a blow-up counterexample exists;
- arbitrary 3D global regularity is proved;
- a discrete bridge has converged to the continuum without an explicit convergence theorem;
- numerical path-independence proves regularity or blow-up;
- finite-cylinder Hou dynamics have been promoted to an official Clay domain without transfer;
- a frequency-fiber multiplier has automatically become a bounded PDE function-space operator.

Keep separate:

- exact analytic identity;
- quadrature error;
- low-rank/modal truncation error;
- PDE discretization error;
- continuum-promotion error;
- domain-transfer error;
- model/provenance scope.

## Lean proof hygiene and GitHub workflow

CI rejects `sorry`, `admit`, local `axiom`, and source-level `opaque` declarations under `Formal/`. `Formal/AxiomAudit.lean` prints axiom dependencies of the strongest formal theorems.

Branch protection is not the merge gate in practice; **green Lean CI is the manual merge gate**.

Before resuming work, inspect the latest `main`, open PRs, and Actions result.

## Resume prompt

A short continuation prompt should be enough:

`@GitHub ns-mns2-flowmap-bridge の PROJECT_GOAL.md、SPEC.md、AGENTS.md、FORMAL_SCOPE.md、HANDOFF.md を読んで、Fable5 registry と最新main/PR/CIを照合して続きから。古い進捗記述より実コードを優先して。`
