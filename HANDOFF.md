# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: **2026-09-06 JST (forty-third session)**.

This is the durable short-form continuation point. Current source/theorem statements and merged `main` control accepted state. Open PRs may contain later research results but are not accepted `main` state until merged.

## Accepted main boundary

Main accepted head before the present PR-90 synchronization was

`327c2fdc382d4a40cc7779552ae898ec70959ed5`.

PR #92 is merged. The repository therefore contains the accepted periodic-domain sidecar

- `Formal/PeriodicClayCore.lean`;
- `Formal/PeriodicExplicitShear.lean`;
- `Formal/PeriodicClayShear.lean`;
- `Formal/PeriodicClayEnergy.lean`;
- `Formal/PeriodicClayQuantifiers.lean`;
- `Formal/PeriodicClayCertificate.lean`;

with anchors

- `ClayNS.certified_nonzero_periodic_NS`;
- `ClayNS.clayB_has_nonzero_smooth_specialization`;
- `ClayNS.not_clayB_iff_unforcedPeriodicObstruction`;
- `ClayNS.failure_of_clayB_has_nonzero_datum`;
- `ClayNS.covering_solved_family_implies_clayB`.

The universal proposition `ClayNS.ClayB` remains **unproved**. The periodic shear result is a global special-family certificate, not Clay B and not a whole-space result.

The accepted whole-space `R^3` formal frontier is unchanged: local actual-NS mild theory for real divergence-free Schwartz data, explicit lifespan, unrestricted uniqueness, restart/continuation dichotomy, decoded velocity/pressure semantics, and the actual incompressible Navier--Stokes equation at interior times. Primary anchors remain `MNS2.r3AdmissibleSchwartzDatum_navierStokes` and `MNS2.r3EndpointSafeProjectedMild_navierStokes`.

PR #92 head `198f1c68297b1d55aea0a5ea053ca2956e5bb13e` passed hosted Lean workflow #277 (`33996261541`): forbidden-source scan PASS and full cached `Formal.+` build PASS under Lean 4.32.1 / mathlib `520045ab14e26149ee970e2e617ca04b09bde5d6`.

## Breakdown research accepted on main

Merged PR #89 established the B2 Gamma-maximum curvature gate:

- `B2-GAMMA-CURVATURE-BUDGET = YES`;
- under one-scale nondegeneracy, `B2-GAMMA-ONESCALE(beta>=1/2) = NO`;
- the parent B2 middle limb remains OPEN.

S15 remains parked by default. The FDT regularity cross-track remains parked. Do not reopen either without its recorded reopen condition.

## Branch-local research now carried by PR #90

PR #90 is `research/b2-gamma-flattop-enstrophy`. It now also contains the former stacked PR #91, which was merged **into the PR-90 branch**, not into `main`.

Session 39 — flat-top / transition enstrophy:

- exact transition vorticity: `omega^r=-Gamma_z/r`, `omega^z=Gamma_r/r`;
- if `|Gamma(R,z)|>=m`, then `int_0^R |Gamma_r|^2/r dr >= 2m^2/R^2`;
- over axial length `L_z`, `E_Gamma >= 4pi m^2 L_z/R^2`;
- `B2-GAMMA-FLATTOP-ENSTROPHY-KILL = NO`;
- `B2-GAMMA-TRANSITION-VORTICITY = YES` with `||omega||_infinity >= c R^{-2}`.

Session 40 — transition residence:

- the local diffusive clock `nu int R^{-2}` diverges for `R~tau^{beta_v}`, `beta_v>=1/2`;
- actual B2 hypotheses do not force one high-Gamma packet to remain resident;
- late arrival / conveyor transport fits below the Type-II amplitude envelope;
- exact affine NS conveyor provides a mechanism no-go for drift-independent residence decay;
- `B2-GAMMA-LATE-ARRIVAL-BARRIER = NO`;
- `B2-GAMMA-TRANSITION-RESIDENCE-KILL = NO`;
- `B2-GAMMA-FLATTOP / RESIDENCE SUBLANE = PARKED`.

Session 41 — Bessel/stochastic hitting:

with `y=r^2`, `G(y,z,t)=Gamma(sqrt(y),z,t)`, `S=-u^r/r`, the exact equation is

`G_t - 2 S y G_y + u^z G_z = 4 nu y G_yy + nu G_zz`.

For frozen inward strain `A>=0`, the outer-before-axis harmonic measure is

`p_A(y;L)=(1-exp(-A y/(2 nu)))/(1-exp(-A L^2/(2 nu)))`,

and the actual-PDE comparison barrier yields the necessary condition

`A(t) R^2 >= c(1-e^{-1}) nu`

for fixed-fraction Gamma saturation at `R<<L`. Hence arbitrarily late saturation at `R~tau^{beta_v}` forces inward strain of order

`S^+ >= c nu tau^{-2 beta_v}`

along a sequence.

Exact decisions:

- `B2-GAMMA-HITTING-STRAIN = YES`;
- `B2-GAMMA-HITTING-NEW-EXPONENT-CUT = NO`;
- `B2-GAMMA-STRAIN-ELLIPTIC-KILL = NO`;
- `B2-GAMMA-SATURATION-MICROGEOMETRY = PARKED`.

The local harmonic model `psi_1=A z` has `S=A` but `L5 psi_1=0`, so large local strain need not produce local `omega_1`; compact localization pushes the source to a shell and critical strain `A~nu/R^2` has vanishing small-scale energy cost. Do not restart the same route by adding co-location, max-displacement, packet thickness, or another residence variable unless a genuinely propagated theorem appears.

Relevant branch-local records:

- `docs/gates/B2_GAMMA_FLATTOP_ENSTROPHY_DECISION_2026-09-06.md`;
- `docs/gates/B2_GAMMA_TRANSITION_RESIDENCE_DECISION_2026-09-06.md`;
- `docs/gates/B2_GAMMA_STOCHASTIC_HITTING_DECISION_2026-09-06.md`.

## PR #90 conflict resolution — session 43

The conflict was caused by both `main` and PR #90 changing `HANDOFF.md` after their common base. The research gate files themselves did not conflict.

Resolution policy:

- keep all accepted main content, including the PR-92 periodic formal sidecar and synchronized formal claim boundary;
- keep all three PR-90 research gate records, including the PR-91 Bessel-hitting result now merged into the PR-90 branch;
- replace the conflicting handoff with this combined continuation point;
- do not treat the PR-90 research conclusions as accepted main state until PR #90 itself is merged.

No Lean/runtime source is changed by this conflict resolution.

## Next research gate

The Gamma-saturation microgeometry family is parked. The next breakdown-side selection must be **orthogonal to the location of the bad set**.

Start from the post-K11 dominant-balance split:

- edge `gamma+alpha=1`: generalized self-similar Euler balance, already under conditional Seregin/Liouville pressure;
- interior `gamma+alpha>1`: quasi-static Euler core, with convection/pressure leading and viscosity/time derivative lower order.

The next theorem-shaped target is therefore a **steady-Euler / ancient-limit compatibility gate**, not another Gamma-location variable. It must ask whether an interior B2 sequence can have a nontrivial rescaled inviscid limit compatible simultaneously with finite local energy, axisymmetric-with-swirl structure, non-evanescent circulation, and the frozen Type-II bookkeeping.

Before promoting any steady/self-similar profile route, respect the read-only negative-knowledge registry: the previously studied continuous self-similar steady-front profile is already KILLED by Liouville results and must not be reopened under a renamed ansatz. A new gate must state exactly why its quasi-static/local/ancient limit is outside that old hypothesis class.

Recommended first decision object:

`B2-ANCIENT-EULER-COMPACTNESS`:

> Given one fixed hypothetical B2 solution in the interior `gamma+alpha>1`, can one choose a sequence of core times and normalized core frames so that a subsequence converges on compact spacetime sets to a nonzero bounded/finite-local-energy ancient Euler solution with the required axisymmetric swirl/circulation signature?

This is a YES/NO compactness gate, not yet a Liouville theorem. If NO, identify the precise missing compactness quantity and decide whether it is controlled by existing B2 budgets. If YES, the next gate is a Liouville/structure theorem for exactly that limit class.

Do not replace compactness by formal power counting, and do not assume convergence of pressure or derivatives without a proved local bound.

## Resume protocol

At substantive resume read, in order:

1. `PROJECT_GOAL.md`;
2. `SPEC.md`;
3. `AGENTS.md`;
4. `FORMAL_SCOPE.md`;
5. this `HANDOFF.md`;
6. `docs/GPT_WORKFLOW.md`;
7. `docs/LEAN_CI_OPERATIONS.md`;
8. `docs/gates/TYPE2_KILL_TABLE_2026-08-19.md`;
9. `docs/gates/DOMINANT_BALANCE_INVERSION_2026-08-19.md`;
10. `docs/gates/B2_GAMMA_MAX_CURVATURE_DECISION_2026-09-06.md`;
11. the three branch-local Gamma records listed above;
12. the external read-only no-go registry;
13. current `main`, PR #90, and latest CI.

## Claim boundary / forbidden shortcuts

Do not:

- claim Clay A/B/C/D;
- claim universal periodic B from the explicit shear family;
- identify periodic fields with the whole-space `R^3` carriers;
- treat branch-local PR-90 conclusions as merged state;
- reopen S15 or FDT without their recorded reopen conditions;
- continue the parked Gamma-saturation microgeometry route by adding another local escape variable;
- reopen the killed continuous self-similar steady-front route under renamed variables;
- use numerical evidence as a continuum blow-up proof;
- equate a finite-cylinder Hou computation with an official Clay-domain construction without a transfer theorem;
- add Lean plumbing merely for completeness.

The parent B2 middle limb remains OPEN. Neither the accepted formal stack nor the branch-local B2 reductions prove blow-up or global regularity.
