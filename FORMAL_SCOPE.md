# Formal scope and theorem boundary

Last synchronized: 2026-08-13 (JST), after merged PR #35.

This file records what the Lean layer has actually established and what remains outside the proof boundary.

`PROJECT_GOAL.md` is the repository-level acceptance specification. `SPEC.md` is the subordinate normative contract for the current primary physical track (`R^3`, `f = 0`, axisymmetric with swirl, breakdown side). If this file conflicts with either higher-level specification, the higher-level specification controls.

No theorem described here is a Clay A/B/C/D result.

## 1. Exact flow-map bridge

For real normed spaces with complete target, an open admissible set `U`, a map `S`, and affine path

`γ(s) = x + s d`, `s ∈ [0,1]`,

if `S` is `C¹` on `U` and the full path remains in `U`, Lean proves

`∫₀¹ (DS(x + s d))[d] ds = S(x + d) - S(x)`.

The radial specialization is

`∫₀¹ (DS(s d))[d] ds = S(d) - S(0)`.

The tangent is the fixed, unnormalized direction `d`.

Formal files:

- `Formal/Bridge.lean`
- `Formal/FlowMapFTC.lean`
- `Formal/FlowMapChainRule.lean`
- `Formal/FlowMapOperatorContinuity.lean`
- `Formal/FlowMapContDiffOne.lean`
- `Formal/FlowMapLocalContDiff.lean`
- `Formal/PDEBridgeAdapter.lean`
- `Formal/NavierStokesTimeBridge.lean`

`PDEBridgeAdapter` and `NavierStokesTimeBridge` package the analytic bridge with externally supplied PDE semantic relations. They do not themselves construct Navier--Stokes evolution.

## 2. Mild-solution semantics

`Formal/MildSolutionSemantics.lean` defines a Banach-space mild kernel with time-indexed continuous linear evolution `H(t)` and nonlinearity `B`.

A trajectory satisfies the Duhamel equation

`u(t) = H(t)u₀ - ∫₀ᵗ H(t-s) B(u(s)) ds`

with explicit continuity, initial-value, and interval-integrability requirements.

Endpoint evolution is existential in a witnessing trajectory. Positive-time uniqueness is not hidden in the definition.

`Formal/MildFlowMapBridge.lean` connects certified flow-map slices to mild endpoint witnesses. `Formal/MildZeroUniqueness.lean` derives zero-fixed endpoint behavior only under explicit endpoint/trajectory uniqueness assumptions.

## 3. Quadratic nonlinearity and linearized mild semantics

For a continuous bilinear map

`Q : V →L[ℝ] V →L[ℝ] V`,

`Formal/QuadraticMildNonlinearity.lean` defines

`B(u) = Q(u,u)`

and proves

`DB(u)[v] = Q(u,v) + Q(v,u)`.

The later formal stack establishes the linearized mild semantics and derives tangent identities from differentiable quadratic mild fixed-point families under explicit dominated-differentiation hypotheses.

Relevant files:

- `Formal/QuadraticLinearizedMild.lean`
- `Formal/QuadraticMildTangentAdapter.lean`
- `Formal/QuadraticDuhamelDifferentiation.lean`
- `Formal/QuadraticMildFixedPointDerivative.lean`
- `Formal/QuadraticMildTangentRealization.lean`
- `Formal/QuadraticMildCoherentFamilyAdapter.lean`

A representative derived directional equation is

`J(t)h = H(t)h - ∫₀ᵗ H(t-s) (Q(u(s), J(s)h) + Q(J(s)h, u(s))) ds`,

subject to the concrete hypotheses encoded in the formal certificates.

These theorems remain abstract Banach-space results. They do not construct the concrete Navier--Stokes solution family whose derivative is `J`.

## 4. Leray-projected quadratic operator contract

`Formal/LerayProjectedQuadratic.lean` defines `LerayProjectedQuadraticContract` with:

- a certified solenoidal submodule;
- a continuous linear Leray map;
- a raw continuous bilinear convection map;
- a projected continuous bilinear map;
- exact identification of projected convection with Leray applied to raw convection;
- range-in-solenoidal and fixed-on-solenoidal properties.

Lean derives:

- Leray idempotence;
- projected bilinear outputs are solenoidal;
- the quadratic diagonal is solenoidal;
- the quadratic derivative is solenoidal;
- the derivative of the packaged mild nonlinearity is solenoidal.

This is an operator-level contract, not yet the physical `R^3` function-space Leray projector or `P div(u ⊗ v)`.

## 5. Concrete `R^3` Leray frequency symbol

`Formal/R3LerayFrequencySymbol.lean` sets

`R3 := EuclideanSpace ℝ (Fin 3)`

and defines the solenoidal fiber at frequency `ξ` as

`(ℝ ∙ ξ)ᗮ`.

`r3LeraySymbol ξ` is the orthogonal projection onto that plane.

Lean proves:

- `v` lies in the solenoidal fiber iff `inner ℝ ξ v = 0`;
- every projected vector is transverse;
- transverse vectors are fixed;
- idempotence;
- norm non-expansion;
- zero-frequency identity;
- `P(ξ)ξ = 0`;
- the explicit formula

`P(ξ)v = v - (inner ℝ ξ v / ‖ξ‖^2) • ξ`.

This is the real matrix action underlying the Fourier Leray multiplier at one physical three-dimensional frequency. It is **not yet** a bounded operator on a bundled `R^3` PDE function space.

## 6. Concrete `R^3` Stokes/heat frequency symbol

`Formal/R3StokesFrequencySymbol.lean` follows the pinned mathlib Fourier convention

`widehat(Δf)(ξ) = -(2π)^2 |ξ|^2 widehat(f)(ξ)`.

It defines the scalar viscosity decay factor

`exp(-(2π)^2 ν t |ξ|^2)`

and the corresponding scalar continuous-linear operator on the three-dimensional velocity fiber.

Lean proves:

- nonnegative decay rate when `ν ≥ 0`;
- strict positivity of the scalar factor;
- factor `≤ 1` for `ν,t ≥ 0`;
- identity at time zero;
- identity at zero frequency;
- exact time-semigroup law;
- preservation of the solenoidal fiber;
- exact commutation with `r3LeraySymbol`;
- pointwise norm contraction for forward time;
- the combined Stokes--Leray frequency symbol lands in the solenoidal fiber.

This is again a frequency-fiber theorem, not yet a function-space Stokes semigroup.

## 7. Reduced/finite-rank bridge infrastructure

The repository also contains reduced tangent/residual infrastructure in:

- `Formal/ReducedBridgeResidual.lean`
- `Formal/FiniteRankReducedBridge.lean`

These theorems separate exact bridge identities from approximation error and do not provide discrete-to-continuum promotion by themselves.

## What is not formalized

The Lean development does **not** currently establish:

- Clay statement A, B, C, or D;
- global smoothness or global existence for arbitrary 3D data;
- a blow-up counterexample;
- a closed-form general solution;
- continuation of a `C¹` solution map through a singular time;
- a concrete divergence-free Banach solution space on physical `R^3` carrying the full mild equation;
- a bounded function-space Stokes semigroup obtained by Fourier lifting the scalar frequency symbol;
- a bounded function-space Leray projector obtained by lifting the matrix/operator-valued frequency symbol;
- the physical convection map `div(u ⊗ v)` with the mapping estimates required by the selected mild theory;
- the concrete projected quadratic term `P div(u ⊗ v)` on the selected spaces;
- local existence and uniqueness for that concrete `R^3` mild equation;
- an open admissible initial-data domain with `C¹` solution-map dependence;
- a rigorous finite-cylinder Hou to official Clay-domain transfer;
- convergence of the MNS-2 discrete/reduced bridge to a continuum Navier--Stokes bridge.

## Remaining Navier--Stokes obligations

A concrete PDE layer must still supply, in order:

1. a specific physical `R^3` function-space carrier compatible with the intended local mild theory;
2. viscosity assumptions, normally `ν > 0`;
3. a genuine function-space Stokes/heat operator obtained from the scalar frequency symbol or an equivalent construction;
4. a genuine function-space Leray projector corresponding to the matrix-valued symbol;
5. the physical bilinear convection map and the estimates required to make its Leray projection well-defined between the selected spaces;
6. proof that these objects instantiate the existing `MildEvolutionKernel`/quadratic interfaces with the intended PDE meaning;
7. local existence and, when a single-valued state map is used, uniqueness;
8. an open admissible-data domain and `C¹` dependence of the fixed-time solution map;
9. path inclusion in that domain;
10. zero-data evolution when endpoint reconstruction uses `S(0)=0`;
11. for any breakdown-side claim, a separate rigorous argument matching the exact Clay C/D hypotheses and official domain.

Only after items 1--10 are discharged may the flow-map bridge be interpreted as a concrete continuum Navier--Stokes solution-map theorem. Only after the separate final Clay gate may a Clay-level result be claimed.

## Important implementation boundary for the next step

Mathlib has scalar Fourier-multiplier infrastructure that may support the Stokes lift. The Leray symbol is matrix/operator-valued, so a scalar multiplier API must **not** be used as if it automatically handled the Leray projector.

If the required function-space lift is unavailable in current mathlib, expose the missing boundedness/multiplier theorem as an explicit contract or prove the needed infrastructure. Do not bury it inside a semantic adapter.

## Numerical and domain scope

Finite-dimensional path identities, POD/SVD reductions, modal tangent reconstruction, and synthetic Hou-like data remain numerical/reduction tools only.

A continuum promotion requires explicit convergence of solution maps and pathwise tangent actions on a common time interval. A finite-cylinder Hou computation is not an official `R^3` or periodic Clay-domain computation without a rigorous transfer theorem.

## Audit policy

CI rejects proof holes and local proof-bypassing declarations under `Formal/`, including `sorry`, `admit`, local `axiom`, and source-level `opaque` declarations.

`Formal/AxiomAudit.lean` prints axiom dependencies of the strongest formal theorems into the Lean build log.

Green Lean CI is the repository's manual formal merge gate.
