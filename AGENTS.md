# AGENTS.md

This repository contains numerical experiments and Lean 4 formalization for the MNS-2 flow-map bridge program.

## Non-negotiable claim boundary

Do **not** claim that this repository proves any of the following:

- global existence or smoothness for 3D Navier–Stokes;
- a Navier–Stokes blow-up counterexample;
- a closed-form or global general solution of Navier–Stokes;
- continuation of a solution map through a singular time;
- that the Hou late-state singular regime has been reproduced or validated here;
- that a discrete/numerical bridge automatically implies the continuum bridge.

The strongest currently formalized analytic implication is local and conditional:

> If a fixed-time map `S` is `C¹` on an open set `U` containing the entire initial-data path, then the exact path-integral reconstruction identity holds on that path.

For the affine path `s ↦ x + s • d`, the tangent is the fixed, unnormalized direction `d`.

## Tangent-direction invariant

Never replace the path derivative `d` by any of the following unless the path itself has actually been changed and the derivative is rederived:

- `s • d`;
- a normalized copy of `d`;
- an arbitrary amplitude vector such as `q_amp`;
- a state-dependent retuned direction.

For a radial path `s ↦ s • d`, the derivative with respect to `s` is exactly `d`.

## Lean proof discipline

- No `sorry`.
- No `admit`.
- No new local `axiom` declarations.
- No `opaque` declarations used to hide missing proofs.
- Prefer existing mathlib theorems over restating analytic facts as assumptions.
- If a theorem is only algebraic endpoint cancellation, do not describe it as an analytic FTC theorem.
- Keep assumptions explicit in theorem statements or immediately documented above them.
- Do not weaken assumptions in prose after proving a theorem under stronger assumptions.

The CI safety gate scans `Formal/**/*.lean` for proof holes and local axiom-like declarations before running `lake build`.

## Formal/analytic layers

Treat these as distinct layers:

1. algebraic endpoint telescoping;
2. Banach-valued FTC along a path;
3. Fréchet chain rule producing `DS[path]` applied to the fixed path tangent;
4. continuity of tangent action from operator-valued continuity;
5. `C¹` regularity implying differentiability plus continuous `fderiv`;
6. localization to an open admissible-data domain;
7. PDE-specific construction of a genuine fixed-time solution map and its domain.

Layers 1–6 are abstract functional analysis. Layer 7 is where Navier–Stokes-specific existence/regularity assumptions enter.

## Numerical-to-continuum guardrail

Never promote a discrete bridge, grid-converged scalar diagnostic, SVD approximation, or finite-dimensional coordinate identity to a continuum Navier–Stokes theorem without an explicit convergence argument strong enough to pass the solution map and pathwise tangent through the limit.

Keep these errors separate when reporting results:

- PDE discretization error;
- time-integration error;
- path quadrature error;
- low-rank/modal truncation error;
- operator/invariant-subspace error;
- discrete-to-continuum error.

## MNS-2 numerical invariants

When touching the numerical stack, preserve the project conventions unless a change is explicitly justified and tested:

- conservative cylindrical transport;
- LF-WENO7-JS transport where specified;
- frozen real LF speeds during holomorphic tangent windows;
- fixed positive WENO epsilon during a tangent/scan window;
- no state-dependent `max`, `abs`, or `sign` inserted inside a perturbed holomorphic map;
- physical-energy metric for tangent geometry;
- clustered singular subspaces rather than individual singular-vector identities through degeneracy;
- no per-path or per-amplitude schedule retuning when comparing path integrals.

## Provenance guardrail

Synthetic or analytic seeds are not Hou late-state evidence. Do not label them as such. A genuine late-state comparison requires explicit provenance for the numerical state and schedule.

## Pull requests

Every mathematical PR should state:

- the mathematical claim;
- the exact new assumptions;
- the Lean theorem(s) or numerical artifact(s) implementing it;
- what the change does **not** prove;
- whether it changes any numerical/runtime behavior;
- CI status.

Use `FORMAL_SCOPE.md` as the current theorem/claim boundary.
