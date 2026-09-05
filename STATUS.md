# STATUS — 2026-09-06

This is the current concise repository status after merge of PR #92. The pre-sync long-form status/history remains available at main commit `5ce0ebc321e7ccd3d51a489f80f184c86203f1d3` and in the dated records under `docs/gates/`, `docs/formal/`, and `docs/reports/`.

## 1. Project-level status

Ultimate target: one exact official Clay/Fefferman Navier--Stokes statement A/B/C/D.

Current primary research specification remains:

- domain: `R^3`;
- force: `f = 0`;
- three-dimensional incompressible Navier--Stokes;
- axisymmetric with swirl;
- breakdown/nonextendibility side.

`SPEC.md` is unchanged by PR #92. The new periodic formalization is a sidecar and does not redirect the primary research program to Clay B.

**Clay status: UNSOLVED in this repository.**

## 2. Accepted formal `R^3` frontier

The whole-space formal stack remains theorem-closed through:

`R^3` Stokes/Leray operators -> projected convection -> endpoint-safe Duhamel -> local Picard existence -> physically real local solution -> explicit lifespan -> unrestricted uniqueness -> restart/concatenation -> continuation blow-up dichotomy -> decoded physical semantics -> pressure reconstruction -> incompressible Navier--Stokes equation in `S'` at interior times -> admissible real divergence-free Schwartz datum entry.

Primary accepted anchors include:

- `MNS2.r3AdmissibleSchwartzDatum_navierStokes`;
- `MNS2.r3EndpointSafeProjectedMild_navierStokes`;
- `MNS2.r3EndpointSafeProjected_exists_realMildSolutionOn_mildLifespan`;
- `MNS2.r3EndpointSafeProjectedMildSolution_unique`;
- `MNS2.r3EndpointSafeProjected_blowup_dichotomy`.

Exact strength: local in time; physical velocity real; finite kinetic energy at each certified time; strong `L^2` time derivative; spatial momentum/divergence statement in tempered distributions at interior times. It is **not** a global-regularity or arbitrary-data classical-solution theorem.

The T-SEL assembly remains conditional. SEL-1 and SEL-4 are proved, but research head `N0` remains open; SEL-3/SEL-5 are on-hold formalization debt. No T-SEL conditional theorem may be paraphrased as unconditional global continuation.

See `FORMAL_SCOPE.md` for the current exact theorem boundary.

## 3. Newly accepted periodic formal sidecar — PR #92

PR #92, `Formal: integrate periodic Clay-B shear specialization`, is merged into `main` as:

`6b518faab2c313a89b61a88e612aa11b766ac7ac`.

It adds:

- `Formal/PeriodicClayCore.lean`;
- `Formal/PeriodicExplicitShear.lean`;
- `Formal/PeriodicClayShear.lean`;
- `Formal/PeriodicClayEnergy.lean`;
- `Formal/PeriodicClayQuantifiers.lean`;
- `Formal/PeriodicClayCertificate.lean`.

For every `ν > 0` and nonzero amplitude `a`, Lean certifies the explicit unit-periodic shear

`u0(x) = (a sin(2*pi*x_2),0,0)`,

`u(t,x) = (a exp(-4*pi^2*ν*t) sin(2*pi*x_2),0,0)`,

`p = 0`,

as a global smooth solution of the full unforced coordinate 3D periodic Navier--Stokes predicate. The datum is nonzero, smooth, divergence-free, and unit-periodic; the pressure is periodic; the convection term is present in the predicate and vanishes for this family; the unit-cell squared-velocity density is integrable with energy bound `0 <= E(t) <= a^2`.

Main theorem:

`ClayNS.certified_nonzero_periodic_NS`.

Quantifier-visible specialization:

`ClayNS.clayB_has_nonzero_smooth_specialization`.

The general proposition `ClayNS.ClayB` has the universal quantifier over **every** admissible periodic datum. That universal proposition is **not proved**.

The following logical facts are also accepted:

- `ClayNS.not_clayB_iff_unforcedPeriodicObstruction`;
- `ClayNS.failure_of_clayB_has_nonzero_datum`;
- `ClayNS.covering_solved_family_implies_clayB`.

The coverage theorem makes the missing bridge explicit: a solved family gives universal B only after proving that every admissible periodic datum is covered. No such coverage theorem is proved for the shear family.

Detailed provenance/scope: `docs/formal/PERIODIC_CMI_B_SHEAR_INTEGRATION_2026-09-06.md`.

## 4. Verification state

Pinned environment:

- Lean `4.32.1`;
- mathlib `520045ab14e26149ee970e2e617ca04b09bde5d6`.

PR #92 integration head:

`198f1c68297b1d55aea0a5ea053ca2956e5bb13e`.

GitHub Actions `Lean 4 formalization` run **#277** (`33996261541`) completed **SUCCESS**:

- forbidden-source scan PASS;
- full cached `Formal.+` Lake build PASS.

The principal periodic certificate/quantifier declarations expose `#print axioms`; the independent supplied verification record reports only `propext`, `Classical.choice`, and `Quot.sound`, with no `sorryAx` in the audited dependency closure.

The accepted formal frontier is therefore green at the PR #92 source tree and merged to `main`.

## 5. Breakdown research status on accepted `main`

Accepted `main` contains the B2 Gamma-max curvature decision from merged PR #89:

- `B2-GAMMA-CURVATURE-BUDGET = YES`;
- `B2-GAMMA-ONESCALE(beta>=1/2) = NO` for the stated nondegenerate one-scale peak hypothesis;
- the full B2 middle limb remains open through flat-top, max-displacement, or multiscale escapes.

There are currently two **open, unmerged** analytic PRs:

- PR #90: flat-top / transition enstrophy and residence audit;
- PR #91: stacked stochastic/Bessel hitting-strain audit on top of #90.

Those branches contain later research conclusions, but because they are not merged they are **not part of the accepted `main` theorem/research boundary**. Do not silently treat them as landed state.

S15 remains parked by default. The FDT regularity cross-track remains parked. Their recorded reopen conditions still control.

## 6. Claims that remain forbidden

Do not claim that this repository has proved any of the following:

- Clay A, B, C, or D;
- global regularity for arbitrary 3D Navier--Stokes data;
- universal periodic Clay B;
- a finite-time Navier--Stokes blow-up counterexample;
- a closed-form general solution;
- continuum validity of a numerical/discrete flow-map bridge without an explicit convergence theorem;
- a finite-cylinder Hou computation as an `R^3` or periodic Clay solution without a domain-transfer theorem.

The periodic shear result is a genuine nonzero arbitrary-amplitude global special solution, not a universal-data theorem.

## 7. Operating rule

Formal plumbing remains stopped unless a concrete research theorem consumes a missing edge, a semantic defect is found, or the user explicitly commissions formal work. PR #92 was an explicit commissioned periodic sidecar integration.

For research continuation, inspect `HANDOFF.md` plus the current open PRs before selecting the next gate. For formal claims, `FORMAL_SCOPE.md` and current source statements control.
