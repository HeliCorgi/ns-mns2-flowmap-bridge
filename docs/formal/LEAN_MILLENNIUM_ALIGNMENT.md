# Lean Millennium Navier–Stokes alignment

This note records a source-level comparison with
`lean-dojo/LeanMillenniumPrizeProblems`, especially its Navier–Stokes formalization.

The external repository is used here as a **mechanized statement/reference cross-check**, not as an
authoritative replacement for the Clay/Fefferman statement and not as proof that this repository
has reached a Clay result.

## External source and license

Reference repository:

- `https://github.com/lean-dojo/LeanMillenniumPrizeProblems`
- cited release metadata: *Formalization of the Millennium Prize Problem Statements in Lean 4*,
  Robert Joseph George, version 2.0.0 (2026-07-11)
- repository license: Apache License 2.0

Apache-2.0 permits reuse and derivative works, but redistributed copied/modified source must retain
applicable notices, include the license, and mark modified files. This repository currently does
**not** vendor source code from LeanMillenniumPrizeProblems. The comparison below uses declaration
names, mathematical interfaces, and design ideas only. If code is copied later, add the required
Apache-2.0 attribution/license material in the same PR.

## What overlaps with `Formal/R3LerayL2Operator.lean`

There is **no direct duplicate of the function-space Leray projector** in the external repository.
In particular, a repository search found no `Leray` declaration, and its Navier–Stokes layer does
not define the closed `L²` solenoidal submodule, an orthogonal projection onto that submodule, the
Fourier Leray matrix symbol, or the Plancherel conjugacy used here.

The overlap is at the semantic/type boundary:

1. Their whole-space spatial carrier `Space3` reduces to Mathlib's
   `EuclideanSpace ℝ (Fin 3)`, the same underlying real Euclidean type used here as `MNS2.R3`.
2. Their `divergence` / `divergence_free_at` express incompressibility in physical coordinates by
   spatial derivatives of a spacetime velocity field.
3. Our `r3L2SolenoidalSubmodule` expresses the same physical constraint after Fourier transform,
   as the kernel of the bundled normalized Fourier-divergence operator on
   `L²(R³; ℂ³)`.
4. Our `r3LerayL2Operator` is therefore an analytic/function-space realization that their statement
   formalization does not supply.

So `R3LerayL2Operator.lean` should not be replaced by the Lean Millennium code. The useful relation
is instead a future theorem connecting our Fourier/L² incompressibility semantics to their
physical-coordinate solution semantics under enough regularity.

## Parts that are useful as formal endpoint specifications

The external Navier–Stokes files provide a clean endpoint vocabulary that is useful for auditing
our later PDE bridge:

- `NavierStokes.NavierStokesEquations`: viscosity, force, initial velocity, and initial
  divergence-free data.
- `NavierStokes.GlobalSolution`: momentum equation, incompressibility, and initial condition on
  `ℝ³ × [0,∞)`.
- `NavierStokes.GlobalSmoothSolution`: smoothness of velocity and pressure on the global time
  half-space.
- `NavierStokesOnR3.SmoothRapidDecayInitial`: the whole-space rapid-decay condition for initial
  data.
- `NavierStokesOnR3.SmoothRapidDecayForce`: the corresponding force condition.
- `NavierStokesOnR3.FiniteEnergy`: a uniform-in-time finite-energy condition.
- `NavierStokesOnR3.SmoothExistence` and `NavierStokesOnR3.Breakdown`: machine-checkable versions
  of the whole-space Fefferman A/C targets.
- `MillenniumNavierStokes.ClayNavierStokes`: the top-level disjunction of the four A/B/C/D cases.

Their top-level prize theorem remains intentionally open with a placeholder; the value to this
project is the statement/interface layer, not a solution.

## Important consequence for the current breakdown route

The external whole-space `Breakdown` statement makes the final target quantifiers explicit: the
claim is parametrized by every positive viscosity, then asks for admissible data/forcing for which
no global smooth finite-energy solution exists.

Our preferred `f = 0` route is therefore a stronger specialization on the forcing side. If this
repository eventually proves a candidate only at one normalized viscosity, a separate rigorous
viscosity-scaling bridge is needed before it can be promoted to the full whole-space breakdown
statement.

The external repository also proves that the zero force satisfies its rapid-decay force condition.
That is a useful final-gate simplification once our own PDE semantics are connected to the same
statement shape.

## Useful future bridge targets

The best use of the external formalization is not to import its PDE engine, but to make our later
conversion obligations explicit. A future compatibility layer should prove, under sufficient
regularity, statements of the following shape:

1. our physical/Fourier solenoidal condition implies the coordinate divergence-free condition;
2. our projected mild equation implies the coordinate momentum equation with a pressure witness;
3. our initial-data carrier implies the required smooth rapid decay when the candidate data are in
   the intended Clay class;
4. our energy norm/estimates imply the finite-energy predicate used by the final statement;
5. a verified breakdown theorem on our concrete `R³` solution class implies the corresponding
   whole-space breakdown proposition.

These are semantic promotion theorems. They must not be replaced by definitional adapters that
simply assume the desired PDE meaning.

## Parts useful outside the current `R³` lane

`Problems/NavierStokes/Torus.lean` uses Mathlib's product torus and an explicit quotient map from
`ℝ³` coordinates to `(ℝ/ℤ)³`. If the project returns to the periodic B/D lane, that construction is
a useful reference for avoiding an ad-hoc periodic-domain model.

## Dependency note

LeanMillenniumPrizeProblems currently pins Mathlib `v4.31.0` and also depends on PhysLean. This
repository uses a different pinned Mathlib revision/Lean toolchain. Adding the external repository
as a direct Lake dependency would therefore introduce unnecessary dependency/version risk.

For now the preferred policy is:

- keep our analytic `R³` operator layer native to the current pinned Mathlib;
- use LeanMillenniumPrizeProblems as a statement/semantic cross-check;
- copy source only if a concrete helper is genuinely missing and worth the license/dependency cost;
- if copying occurs, preserve Apache-2.0 attribution and mark modifications explicitly.
