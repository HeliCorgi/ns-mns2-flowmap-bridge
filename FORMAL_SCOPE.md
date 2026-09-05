# Formal scope and theorem boundary

Last synchronized: **2026-09-06 JST**, after PR #92 (`Formal: integrate periodic Clay-B shear specialization`) was merged to `main` as commit `6b518faab2c313a89b61a88e612aa11b766ac7ac`.

This file is the current concise theorem/claim boundary. The pre-sync long-form formal history remains available in Git history at main commit `5ce0ebc321e7ccd3d51a489f80f184c86203f1d3` and in the dated records under `docs/formal/`.

`PROJECT_GOAL.md` is the repository-level acceptance specification. `SPEC.md` is the subordinate normative contract for the current primary physical track (`R^3`, `f = 0`, axisymmetric with swirl, breakdown side). If this file conflicts with either higher-level specification or the official Clay/Fefferman statement, the higher-level source controls.

No theorem currently in this repository proves Clay statement A, B, C, or D.

## 1. Accepted whole-space `R^3` Navier--Stokes formal stack

The main `R^3` formal stack is unchanged by PR #92. It contains genuine function-space Stokes/Leray operators, the projected convection map, endpoint-safe two-space Duhamel theory, local fixed-point existence, reality, quantitative lifespan, unrestricted uniqueness, restart/concatenation, continuation in blow-up-dichotomy form, decoded physical semantics, pressure reconstruction, and an admissible Schwartz-data entry point.

The strongest currently accepted `R^3` Navier--Stokes statement is local and explicitly scoped:

> For every viscosity `ν > 0` and every real, divergence-free Schwartz datum `φ` on `R^3`, there is a positive certified horizon and a mild solution whose decoded physical velocity `U` satisfies `U(0)=φ` in physical `L^2`, is physically real, has finite kinetic energy at every certified time, and at every interior time satisfies the incompressible Navier--Stokes momentum equation componentwise in tempered distributions with the explicit Helmholtz pressure, while the time derivative is a strong `L^2`-valued derivative.

Primary anchors:

- `MNS2.r3AdmissibleSchwartzDatum_navierStokes`;
- `MNS2.r3EndpointSafeProjectedMild_navierStokes`;
- `MNS2.r3EndpointSafeProjected_exists_realMildSolutionOn_mildLifespan`;
- `MNS2.r3EndpointSafeProjectedMildSolution_unique`;
- `MNS2.r3EndpointSafeProjected_blowup_dichotomy`.

Relevant implementation layers include:

- `Formal/R3StokesL2Operator.lean`;
- `Formal/R3LerayL2Operator.lean`;
- `Formal/R3ProjectedSobolevConvection.lean`;
- `Formal/R3StokesH2H3Smoothing.lean`;
- `Formal/EndpointSafeTwoSpaceDuhamel.lean`;
- `Formal/EndpointSafeTwoSpacePicard.lean`;
- `Formal/R3RealLocalMildSolution.lean`;
- `Formal/R3QuantitativeLifespan.lean`;
- `Formal/EndpointSafeTwoSpaceRestart.lean`;
- `Formal/EndpointSafeTwoSpaceUniqueness.lean`;
- `Formal/EndpointSafeTwoSpaceConcatenation.lean`;
- `Formal/R3MildContinuation.lean`;
- `Formal/R3NavierStokesEquation.lean`;
- `Formal/R3FiniteEnergy.lean`;
- `Formal/R3DecodedVelocityRealness.lean`;
- `Formal/R3SchwartzInitialData.lean`.

This whole-space result is **local in time** and the spatial PDE statement is distributional. It is not a global-regularity theorem and not a pointwise classical-solution theorem for arbitrary data.

## 2. Exact flow-map and mild-theory infrastructure

The abstract flow-map stack proves the exact path-integral identity for a `C^1` fixed-time map on an open admissible set. For an affine path `s |-> x + s d`, the path tangent is exactly the fixed, unnormalized direction `d`:

`integral_0^1 (DS(x+s d))[d] ds = S(x+d)-S(x)`.

The radial specialization is the corresponding identity from zero. These theorems are abstract functional-analysis results unless supplied with a concrete PDE solution map and its regularity/domain hypotheses.

Key files include `Formal/Bridge.lean`, `Formal/FlowMapFTC.lean`, `Formal/FlowMapChainRule.lean`, `Formal/PDEBridgeAdapter.lean`, and `Formal/NavierStokesTimeBridge.lean`.

The concrete `R^3` local mild theory is not to be silently identified with a globally defined `C^1` solution map through a singular time.

## 3. T-SEL conditional regularity assembly

The T-SEL statement/bridge layer remains unchanged by PR #92.

Proved pieces include:

- SEL-1 classical Sobolev comparability: `MNS2.r3TSel_classicalSobolevComparability`;
- SEL-2 decoded gradient/sup embedding;
- SEL-4 derivative-tuple commutator: `MNS2.r3TSel_katoPonceCommutator`;
- SEL-6 Gronwall--Bellman infrastructure;
- bookkeeping/realness/uniqueness-transfer pieces;
- the downstream **conditional** chain through `MNS2.r3TSel_conditional_globalContinuation`.

Still open or carried only as explicit hypotheses/formalization debt:

- research head `R3TSelGradientBound` / `R3TSelHead` (`N0`);
- `R3TSelH3Ladder` (SEL-5), currently formalization debt on known mathematics;
- `R3TSelInteriorSobolevSmoothing` (SEL-3), likewise on hold;
- EB-1 energy equality in the exact certified carrier, when/if a future commissioned route consumes it.

Do not cite a conditional T-SEL theorem as unconditional global regularity.

## 4. Accepted periodic CMI-B shear sidecar — merged PR #92

PR #92 adds an intentionally separate periodic-domain formalization under namespace `ClayNS`. It is a **sidecar** and is not an adapter from periodic fields to the whole-space Bessel/Fourier carriers.

Files:

- `Formal/PeriodicClayCore.lean`;
- `Formal/PeriodicExplicitShear.lean`;
- `Formal/PeriodicClayShear.lean`;
- `Formal/PeriodicClayEnergy.lean`;
- `Formal/PeriodicClayQuantifiers.lean`;
- `Formal/PeriodicClayCertificate.lean`.

The integrated general periodic proposition is

`ClayNS.ClayB`:

for every positive viscosity and **every** admissible smooth divergence-free unit-periodic datum, there exists a global smooth unit-periodic unforced solution with periodic pressure.

That universal proposition is **defined but not proved**.

### Explicit global shear certificate

For `ν > 0` and `a != 0`, define

`u0(x) = (a sin(2*pi*x_2), 0, 0)`,

`u(t,x) = (a exp(-4*pi^2*ν*t) sin(2*pi*x_2), 0, 0)`,

`p(t,x) = 0`.

`ClayNS.certified_nonzero_periodic_NS` proves that:

- the datum is admissible, smooth, divergence-free, unit-periodic, and nonzero;
- the displayed velocity/pressure pair is a global smooth periodic solution of the full coordinate three-dimensional unforced Navier--Stokes predicate;
- the convection term remains present in the general PDE definition and is proved to vanish for this shear family;
- the squared-velocity density is integrable on the unit cube and its cell integral lies in `[0,a^2]` for every nonnegative time.

The quantifier-visible theorem

`ClayNS.clayB_has_nonzero_smooth_specialization`

proves only

`forall ν > 0, exists u0 != 0, exists u p, AdmissiblePeriodicDatum u0 and GlobalPeriodicSolution ν u0 u p`.

It does **not** change the universal datum quantifier of `ClayB`.

### Periodic quantifier facts

`Formal/PeriodicClayQuantifiers.lean` proves:

- `ClayNS.not_clayB_iff_unforcedPeriodicObstruction`;
- `ClayNS.failure_of_clayB_has_nonzero_datum`;
- `ClayNS.covering_solved_family_implies_clayB`.

The last theorem exposes the exact missing bridge: a solved parameter family implies universal B only if a separate coverage theorem represents **every** admissible periodic datum. No coverage theorem for the shear family is proved.

The source of `PeriodicClayQuantifiers.lean` is repo-authored during integration because the supplied independent bundle contained `ClayQuantifiers.olean` and verification evidence, but not `ClayQuantifiers.lean` source. This provenance distinction is recorded in `docs/formal/PERIODIC_CMI_B_SHEAR_INTEGRATION_2026-09-06.md`.

## 5. Verification state

Pinned project environment:

- Lean: `leanprover/lean4:v4.32.1`;
- mathlib revision: `520045ab14e26149ee970e2e617ca04b09bde5d6`.

For PR #92:

- integration head: `198f1c68297b1d55aea0a5ea053ca2956e5bb13e`;
- GitHub Actions workflow `Lean 4 formalization` run **#277**, run id `33996261541`;
- forbidden-source scan: **PASS**;
- full repository `Formal.+` Lake build: **PASS**;
- merge commit on `main`: `6b518faab2c313a89b61a88e612aa11b766ac7ac`.

The periodic certificate and quantifier modules contain `#print axioms` commands for their principal declarations. The independent verification record reports only the standard foundational dependencies `propext`, `Classical.choice`, and `Quot.sound`, with no `sorryAx` in the audited dependency closure.

## 6. What is not proved

The accepted Lean development does **not** prove:

- Clay A, B, C, or D;
- universal periodic Clay B for arbitrary admissible periodic data;
- whole-space global regularity for arbitrary 3D data;
- a finite-time blow-up counterexample;
- a closed-form general Navier--Stokes solution;
- a global `C^1` solution map through a singular time;
- a canonical glued maximal whole-space trajectory with a pointwise `limsup` blow-up statement;
- uniform-in-time whole-space energy inequality/equality in the final certified carrier;
- arbitrary-carrier `H^3 => C^infty` or rapid decay;
- a rigorous finite-cylinder-to-`R^3` Clay transfer;
- convergence of the numerical MNS-2 bridge to a continuum Navier--Stokes solution map.

The periodic shear theorem is a genuine global classical special solution, but it gives no theorem about arbitrary periodic data and no whole-space rapidly decaying datum.

## 7. Formal stop rule

The 2026-08-23 Stage-9 readiness stop rule remains in force. Do not add formal plumbing merely for completeness. Reopen a missing formal edge only when a concrete commissioned research theorem consumes it or when a semantic defect in an accepted theorem is identified.

PR #92 is an explicit user-commissioned exception that adds a useful periodic positive-control/quantifier sidecar; it does not alter the active `R^3` breakdown research specification.

## 8. Audit policy

The formal source gate rejects `sorry`, `admit`, local `axiom`, and source-level `opaque` declarations under `Formal/`.

`Formal/AxiomAudit.lean` remains the main broad audit file; the periodic sidecar additionally prints the axioms of its own principal certificates in `PeriodicClayCertificate.lean` and `PeriodicClayQuantifiers.lean`.

Green verification is revision-specific. Unmerged feature-branch drafts are not part of this theorem boundary even if a separate branch CI run is green.
