# Periodic CMI-B shear specialization integration — 2026-09-06

**Classification:** `INFRASTRUCTURE / FORMALIZATION` with a proved **specialization** of the periodic unforced CMI alternative B. It is **not** a proof of Clay B for arbitrary periodic data and it does not modify the current `R^3`, unforced, axisymmetric breakdown `SPEC.md` track.

## Provenance

The user supplied an independently developed Astra/Lean bundle containing source for:

- `ClayCore.lean`;
- `ExplicitShear.lean`;
- `ClayShear.lean`;
- `ClayEnergy.lean`;
- `Main.lean`;

plus compiled `.olean` artifacts, an independent `verification.log`, `TRIALS.md`, `SCOPE_AUDIT.md`, a standalone Lake configuration, and a PowerShell verification script.

The independent verification record reports:

- Lean `4.32.1`;
- mathlib revision `520045ab14e26149ee970e2e617ca04b09bde5d6`;
- successful compilation of `ClayCore`, `ExplicitShear`, `ClayShear`, `ClayEnergy`, `ClayQuantifiers`, and `Main`;
- audited named theorems depending only on `propext`, `Classical.choice`, and `Quot.sound`;
- no `sorryAx` in the audited dependency closure.

The repository already pinned the same Lean version and mathlib commit, so no dependency/toolchain migration was needed.

## Repository integration

The independent development was integrated into the existing `Formal.+` target as:

- `Formal/PeriodicClayCore.lean`;
- `Formal/PeriodicExplicitShear.lean`;
- `Formal/PeriodicClayShear.lean`;
- `Formal/PeriodicClayEnergy.lean`;
- `Formal/PeriodicClayQuantifiers.lean`;
- `Formal/PeriodicClayCertificate.lean`.

The first four mathematical source modules and the final certificate preserve the delivered mathematics apart from repository import paths and integration comments.

The uploaded bundle did **not** contain `ClayQuantifiers.lean`; it contained `ClayQuantifiers.olean` plus documentation/verification evidence naming the three logical theorems. Therefore `Formal/PeriodicClayQuantifiers.lean` is a **repo-authored source reconstruction**, not a byte-for-byte import. It proves directly from the integrated definitions:

- `ClayNS.not_clayB_iff_unforcedPeriodicObstruction`;
- `ClayNS.failure_of_clayB_has_nonzero_datum`;
- `ClayNS.covering_solved_family_implies_clayB`.

Compiled `.olean` files, the standalone Lake files, and the Windows verification script were deliberately not vendored. The repository rebuilds source under its normal pinned gate.

## Mathematical certificate

For every `ν > 0` and every `a != 0`, define

`u0(x) = (a sin(2*pi*x_2),0,0)`,

`u(t,x) = (a exp(-4*pi^2*ν*t) sin(2*pi*x_2),0,0)`,

`p(t,x) = 0`.

The integrated periodic predicate contains the full coordinate momentum equation with convection present, the divergence-free condition, initial condition, joint smoothness on nonnegative time, and spatial unit periodicity of both velocity and pressure. For this shear family the convection term is proved to vanish.

The main certificate

`ClayNS.certified_nonzero_periodic_NS`

proves, for positive viscosity and nonzero amplitude:

1. the shear datum is smooth, divergence-free, unit-periodic, and nonzero;
2. the explicit shear is a global smooth periodic solution of the unforced three-dimensional Navier--Stokes predicate;
3. the squared-velocity density is integrable on the unit cube and its cell integral lies in `[0,a^2]` for every nonnegative time.

The quantifier-visible theorem

`ClayNS.clayB_has_nonzero_smooth_specialization`

proves only

`forall ν > 0, exists u0 != 0, exists u p, AdmissiblePeriodicDatum u0 and GlobalPeriodicSolution ν u0 u p`.

## Exact Clay-B boundary

The integrated definition `ClayNS.ClayB` has the universal datum quantifier:

`forall ν > 0, forall u0, AdmissiblePeriodicDatum u0 -> exists u p, GlobalPeriodicSolution ν u0 u p`.

That universal statement is **not proved**.

`ClayNS.covering_solved_family_implies_clayB` exposes the exact missing logical bridge: a solved family implies universal B only if a separate coverage theorem proves that every admissible periodic datum is represented by that family. No such coverage theorem is proved for the shear data.

This result is also not a whole-space Clay-A construction: a nonzero periodic shear is not a rapidly decreasing finite-energy datum on all of `R^3`.

## Relation to the existing whole-space formal stack

This is intentionally a **periodic-domain sidecar** rather than an adapter to the existing `R^3` Bessel/Fourier mild-solution stack. Do not identify the periodic fields with the whole-space carriers.

The sidecar gives:

- a concrete global nonzero arbitrary-amplitude positive-control solution of the actual nonlinear periodic PDE predicate;
- a machine-checked periodic-B endpoint formulation with correct universal-data quantifiers;
- a regression target for future periodic B/D formal work;
- an explicit formal coverage gap preventing special-family results from being paraphrased as Clay B.

The active `SPEC.md` research track remains the `R^3`, `f=0`, axisymmetric-with-swirl breakdown program.

## Final repository verification ruling

PR #92 integration head:

`198f1c68297b1d55aea0a5ea053ca2956e5bb13e`.

Repository-hosted verification:

- workflow: `Lean 4 formalization`;
- run: **#277**;
- run id: `33996261541`;
- forbidden-source scan: **PASS**;
- full cached `Formal.+` Lake build: **PASS**.

PR #92 was merged to `main` as:

`6b518faab2c313a89b61a88e612aa11b766ac7ac`.

Therefore the renamed/import-adapted periodic modules and the repo-authored quantifier reconstruction are **accepted repo-green source**, not merely external verification evidence.

This verification changes only the status of the stated specialization and logical sidecar. It does not prove the universal proposition `ClayNS.ClayB`, Clay A/C/D, arbitrary-data global regularity, or blow-up.
