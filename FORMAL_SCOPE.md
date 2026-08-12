# Formal scope and theorem boundary

This file records what the Lean layer proves and, equally importantly, what remains outside the formalized result.

## Current strongest bridge statement

The current endpoint of the abstract formalization is the open-domain `C¹` bridge in `Formal/FlowMapLocalContDiff.lean`.

Informally, let `X` and `Y` be real normed spaces, with `Y` complete. Let `U ⊂ X` be open, let `S : X → Y`, and suppose `S` is `C¹` on `U`. If the affine path

`γ(s) = x + s d`, `s ∈ [0,1]`,

remains inside `U`, then

`∫₀¹ (DS(x + s d))[d] ds = S(x + d) - S(x)`.

The radial specialization is obtained by taking `x = 0`:

`∫₀¹ (DS(s d))[d] ds = S(d) - S(0)`.

The path tangent is the fixed, unnormalized vector `d`.

## Theorem dependency ladder

### `Formal/Bridge.lean`

Proves purely algebraic endpoint telescoping identities, including two-segment cancellation and rectangle/path endpoint cancellation. These are algebraic identities and do not by themselves provide an analytic line-integral theorem.

### `Formal/FlowMapFTC.lean`

Uses mathlib interval-integral FTC machinery to prove Banach-valued path endpoint reconstruction from an explicitly supplied scalar derivative and continuity assumption.

### `Formal/FlowMapChainRule.lean`

Proves that the affine path derivative is exactly the fixed direction `d`, and uses the Fréchet chain rule to derive the scalar-path tangent `J(s) d` from a derivative family `J(s)`.

### `Formal/FlowMapOperatorContinuity.lean`

Derives continuity of `s ↦ J(s) d` from operator-valued continuity of `J`, using continuity of evaluation of continuous linear maps.

### `Formal/FlowMapContDiffOne.lean`

Replaces the externally supplied derivative family with mathlib's canonical `fderiv` and derives differentiability plus operator continuity from the global assumption `ContDiff ℝ 1 S`.

### `Formal/FlowMapLocalContDiff.lean`

Localizes the previous result to `ContDiffOn ℝ 1 S U` for an open set `U`, requiring only that the chosen affine or radial path stay inside `U`.

This is the preferred theorem for eventual PDE application.

## What is not formalized

The Lean files do **not** currently construct a Navier–Stokes solution map. They do not prove that, for arbitrary 3D initial data and arbitrary positive time, there exists an open set `U` and a fixed-time map `S_t` satisfying the hypotheses above.

In particular, the repository has not formalized or proved:

- global existence of smooth 3D Navier–Stokes solutions;
- global uniqueness sufficient to define a global fixed-time solution map;
- `C¹` dependence of a Navier–Stokes solution map through a possible singular time;
- a blow-up counterexample;
- a closed-form general solution;
- convergence of the MNS-2 discrete solution-map bridge to a continuum Navier–Stokes solution map.

## PDE adapter obligation

To instantiate the abstract theorem with a fixed-time Navier–Stokes map `S_t`, a future PDE-specific layer must supply, for the time and path under consideration:

1. a function space `X` of admissible initial data;
2. a target Banach space `Y` for the evolved state;
3. an open admissible set `U ⊂ X`;
4. a genuine fixed-time solution map `S_t : X → Y` whose values on the path are the corresponding Navier–Stokes solutions;
5. `ContDiffOn ℝ 1 S_t U` or assumptions sufficient to derive it;
6. proof that the full initial-data path lies in `U`.

Only after these obligations are discharged may the abstract bridge be called a Navier–Stokes flow-map bridge at that time.

## Numerical scope

Finite-dimensional and discrete path-integral identities are useful validation and reduction tools, but they remain separate from the continuum theorem. A continuum promotion requires explicit convergence of the relevant solution maps and pathwise tangent actions on a common time interval.

## Audit policy

CI rejects `sorry`, `admit`, local `axiom`, and source-level `opaque` declarations under `Formal/`. `Formal/AxiomAudit.lean` prints the axiom dependencies of the strongest bridge theorems into the Lean build log for inspection.
