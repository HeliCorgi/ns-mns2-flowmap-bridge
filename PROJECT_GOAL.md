# PROJECT_GOAL.md

This file is the top-level goal and acceptance specification for this repository.

All research direction, numerical experiments, Lean formalization, handoff notes, and claim language in this repository are subordinate to this document.

## Ultimate target

The ultimate target is a rigorous resolution of the Clay Mathematics Institute Millennium Prize problem for the three-dimensional incompressible Navier--Stokes equations, in the sense of the official Fefferman problem statement.

Authoritative external target:

- Clay Millennium problem page: `https://www.claymath.org/millennium/navier-stokes-equation/`

A final project-level success must establish one of the official statement classes A/B/C/D, with all hypotheses and domain conditions matched exactly rather than approximately or heuristically.

Operationally:

- **A**: global existence and smoothness on `R^3` for the stated smooth divergence-free rapidly decaying initial data, with the official unforced setting.
- **B**: global existence and smoothness on the periodic three-dimensional domain for the stated smooth divergence-free periodic initial data, with the official unforced setting.
- **C**: breakdown/nonexistence of a global smooth solution on `R^3` for admissible smooth data and forcing as allowed by the official statement.
- **D**: breakdown/nonexistence of a global smooth solution on the periodic three-dimensional domain for admissible smooth data and forcing as allowed by the official statement.

If wording here ever conflicts with the current official Clay/Fefferman statement, the official statement controls and this file must be corrected before any claim is promoted.

## Current primary attack

The current primary attack is the **breakdown side**, i.e. a route intended eventually to satisfy statement C or D rather than a global-regularity proof under A or B.

Within the breakdown side, prefer the stronger target

`f = 0`

whenever the route can support it. An unforced finite-time breakdown result that otherwise satisfies the relevant Clay hypotheses is preferred over a forced construction. This preference does not weaken or alter the official acceptance criterion: every final claim must still be checked directly against the exact Clay statement.

The project may change attack direction if a rigorous A/B route becomes stronger than the breakdown route, but such a change should be recorded explicitly in this file and in `HANDOFF.md`.

## What counts as progress but not completion

The following can be valid intermediate results but are not by themselves a Clay solution:

- an exact abstract flow-map identity;
- a mild-solution or Duhamel semantic interface;
- a Lean proof of a conditional functional-analytic theorem;
- a discrete or finite-dimensional solution-map reconstruction;
- a low-rank, POD, SVD, modal, or tangent approximation;
- numerical growth, fitted singular scaling, or apparent blow-up;
- a Hou-like axisymmetric computation in a finite cylinder;
- a candidate singular profile in a domain different from the official Clay domain;
- convergence of a scalar diagnostic without convergence of the PDE solution and the relevant derivatives;
- validated numerics that certify only a reduced or incorrectly reconstructed system.

Intermediate work is useful only insofar as it either advances an admissible A/B/C/D route or rigorously eliminates a route from future search.

## Domain and equation fidelity

A result may be promoted toward the ultimate target only after checking that it concerns the actual three-dimensional incompressible Navier--Stokes equations in the relevant official domain.

In particular:

- physical three-dimensional incompressibility must be verified after every change of variables or dimensional lift;
- transformed scalar or higher-dimensional weighted identities do not replace the original three-dimensional divergence constraint;
- a finite cylindrical Hou computation is not automatically an `R^3` or periodic-box Clay construction;
- periodic-image effects, radial-wall effects, truncation, and whole-space limits must remain separate until a rigorous transfer is proved;
- a discrete numerical map must not be identified with a continuum solution map without an explicit convergence theorem strong enough for the promoted claim.

## Breakdown-side final gate

For a breakdown-side result to be promoted as a candidate resolution, the project must be able to point to a complete chain matching the applicable official statement. At minimum the chain must identify and justify:

1. the exact Clay domain and equation;
2. the viscosity and force, including whether `f = 0`;
3. explicit admissible smooth divergence-free initial data;
4. all required decay or periodicity conditions;
5. existence and smoothness on the pre-breakdown time interval when the argument requires it;
6. a finite physical time or another exact failure mode sufficient for the official breakdown statement;
7. a proof that the claimed failure is a failure of the original three-dimensional Navier--Stokes solution, not only of a reduced/discrete model;
8. every analytic, truncation, discretization, roundoff, spectral-tail, and reconstruction error bound used by a computer-assisted proof;
9. independent reproduction/certificate checks appropriate to the method;
10. mechanized verification of the final load-bearing argument where feasible, with Lean assumptions kept explicit.

Numerical evidence may motivate this chain but cannot substitute for a missing implication in it.

## Negative-knowledge preflight

Before opening or promoting a new singularity mechanism, consult the read-only exclusion/no-go registry at

`https://github.com/HeliCorgi/ns-singularity-certificate-lab/tree/fable5-mainline`

and obey the detailed rules already pinned in `AGENTS.md` and `HANDOFF.md`.

A route previously marked `KILLED` or `REJECTED` must not be reopened unless the new proposal identifies the exact old binding obstruction and proves why it no longer applies.

## Claim discipline

Until one of A/B/C/D has actually been established with the exact official hypotheses, do not say that this repository has solved the Clay Navier--Stokes problem.

Every major artifact should be classifiable as one of:

- `CLAY-A/B/C/D CANDIDATE` -- only when an explicit remaining-obligations list is attached;
- `CONDITIONAL THEOREM`;
- `NUMERICAL OBSERVATION`;
- `COMPUTER-ASSISTED SUBPROBLEM`;
- `NO-GO / KILLED ROUTE`;
- `INFRASTRUCTURE / FORMALIZATION`.

Passing CI, passing a numerical gate, or obtaining a small residual changes verification status only within the stated scope; none of these automatically changes the project-level Clay status.
