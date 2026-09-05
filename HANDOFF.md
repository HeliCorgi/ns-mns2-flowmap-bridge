# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: **2026-09-06 JST (forty-second session)**.

This is the durable short-form continuation point. Current source/theorem statements and merged `main` control accepted state. Open PRs may contain later research results but are not accepted `main` state until merged.

## What changed in this session

The user supplied an independently developed Astra/Lean periodic Navier--Stokes bundle and commissioned integration into the existing repository.

PR #92, `Formal: integrate periodic Clay-B shear specialization`, was reviewed against the repository scope and merged to `main` as:

`6b518faab2c313a89b61a88e612aa11b766ac7ac`.

The integration is intentionally a **periodic-domain sidecar** rather than an identification with the existing whole-space `R^3` Bessel/Fourier carriers.

Added accepted modules:

- `Formal/PeriodicClayCore.lean`;
- `Formal/PeriodicExplicitShear.lean`;
- `Formal/PeriodicClayShear.lean`;
- `Formal/PeriodicClayEnergy.lean`;
- `Formal/PeriodicClayQuantifiers.lean`;
- `Formal/PeriodicClayCertificate.lean`.

Accepted main periodic anchors:

- `ClayNS.certified_nonzero_periodic_NS`;
- `ClayNS.clayB_has_nonzero_smooth_specialization`;
- `ClayNS.not_clayB_iff_unforcedPeriodicObstruction`;
- `ClayNS.failure_of_clayB_has_nonzero_datum`;
- `ClayNS.covering_solved_family_implies_clayB`.

The universal proposition `ClayNS.ClayB` remains **unproved**.

`FORMAL_SCOPE.md` and `STATUS.md` have been synchronized to this accepted boundary. The pre-sync detailed histories remain recoverable from Git history and the dated gate/formal records.

## Exact periodic theorem boundary

For every `ν > 0` and every `a != 0`, the explicit periodic shear

`u0(x) = (a sin(2*pi*x_2), 0, 0)`,

`u(t,x) = (a exp(-4*pi^2*ν*t) sin(2*pi*x_2), 0, 0)`,

`p(t,x) = 0`

is certified as a global smooth solution of the full unforced coordinate three-dimensional periodic Navier--Stokes predicate. The datum is smooth, divergence-free, unit-periodic, and nonzero; velocity and pressure are periodic; convection is present in the general PDE definition and vanishes for this family; unit-cell squared-velocity density is integrable and uniformly bounded by `a^2`.

This gives

`forall ν > 0, exists nonzero admissible u0, exists u p, GlobalPeriodicSolution ν u0 u p`,

not the Clay-B quantifier

`forall ν > 0, forall admissible u0, exists u p, ...`.

Do not collapse this existential specialization into universal B.

## Verification

Pinned environment:

- Lean `4.32.1`;
- mathlib revision `520045ab14e26149ee970e2e617ca04b09bde5d6`.

Independent supplied bundle:

- all six delivered modules compiled locally;
- audited principal declarations reported only `propext`, `Classical.choice`, `Quot.sound`;
- no `sorryAx` in the audited dependency closure.

Repository integration:

- PR #92 head: `198f1c68297b1d55aea0a5ea053ca2956e5bb13e`;
- hosted workflow `Lean 4 formalization` run **#277**, id `33996261541`;
- forbidden-source scan: **PASS**;
- full cached `Formal.+` Lake build: **PASS**;
- merge commit: `6b518faab2c313a89b61a88e612aa11b766ac7ac`.

No new Lean theorem was added during the post-merge documentation synchronization itself.

## Accepted whole-space formal frontier

The existing `R^3` local theory remains unchanged by PR #92. The accepted chain still reaches:

- genuine Stokes/Leray/projected-convection operators;
- endpoint-safe mild equation;
- local existence;
- physically real solution;
- explicit lifespan;
- unrestricted uniqueness;
- restart/concatenation;
- continuation blow-up dichotomy;
- decoded physical velocity/pressure semantics;
- actual incompressible Navier--Stokes equation in tempered distributions at interior times;
- admissible real divergence-free Schwartz initial data.

Primary anchors remain `MNS2.r3AdmissibleSchwartzDatum_navierStokes` and `MNS2.r3EndpointSafeProjectedMild_navierStokes`.

This is local and distributional in space. It is not a global-regularity result.

T-SEL remains conditional: SEL-1 and SEL-4 are proved; head `N0` remains open; SEL-3/SEL-5 remain on-hold formalization debt.

## Research lane state

Accepted `main` research state still includes merged PR #89, the B2 Gamma-max curvature gate:

- `B2-GAMMA-CURVATURE-BUDGET = YES`;
- `B2-GAMMA-ONESCALE(beta>=1/2) = NO` under its one-scale nondegeneracy hypothesis;
- the full B2 middle limb remains open.

Two later analytic PRs are currently open and unmerged:

- PR #90, `research/b2-gamma-flattop-enstrophy`;
- PR #91, `research/b2-gamma-stochastic-hitting`, stacked on #90.

PR #90 contains the flat-top/transition-enstrophy and residence analysis. PR #91 contains the later Bessel-hitting/inward-strain necessity and the proposed parking of Gamma-saturation microgeometry. These are useful live branches, but **do not treat their conclusions as merged `main` state until the user decides their integration**.

S15 remains parked by default. The FDT regularity cross-track remains parked. Do not reopen either without its recorded reopen condition.

## Next work

If continuing formal work: there is **no automatic next formal plumbing task**. The Stage-9 stop rule remains active. Reopen formalization only for a concrete consumed research theorem, a semantic defect, or an explicit user commission.

If continuing breakdown research: first decide the disposition/order of open PRs #90 and #91. If they are integrated, the next research selection should respect their latest park ruling and move to a Gamma-location-independent breakdown obstruction, preferably an ancient-limit / steady-Euler / globally propagated signed-quantity route rather than another local saturation escape variable.

If they are not integrated, resume from accepted main PR #89 and keep the later branch conclusions clearly branch-local.

## Commission boundaries / forbidden shortcuts

Do not:

- claim Clay A/B/C/D;
- claim universal periodic B from the explicit shear family;
- identify periodic fields with the whole-space `R^3` carriers;
- treat a green special-family theorem as a coverage theorem for all periodic data;
- treat open PR #90/#91 conclusions as merged state;
- reopen S15 or FDT without satisfying their recorded reopen conditions;
- use numerical evidence as a continuum blow-up proof;
- equate a finite-cylinder Hou computation with an official Clay-domain construction without a rigorous transfer theorem;
- add formal plumbing merely for completeness.

## Resume order

At substantive resume, read:

1. `PROJECT_GOAL.md`;
2. `SPEC.md`;
3. `AGENTS.md`;
4. `FORMAL_SCOPE.md`;
5. this `HANDOFF.md`;
6. `docs/LEAN_CI_OPERATIONS.md`;
7. `docs/formal/PERIODIC_CMI_B_SHEAR_INTEGRATION_2026-09-06.md` if touching the periodic sidecar;
8. the latest relevant B2 gate record if touching breakdown research;
9. current `main`, open PRs, and current CI state.

## Project claim boundary

The repository now contains both:

- a strong **local whole-space** actual-NS formal stack for admissible Schwartz data; and
- a genuine **global periodic special-family** actual-NS certificate for nonzero arbitrary-amplitude shear data.

Neither is a Clay solution. The whole-space result is local; the periodic result is special-family only.
