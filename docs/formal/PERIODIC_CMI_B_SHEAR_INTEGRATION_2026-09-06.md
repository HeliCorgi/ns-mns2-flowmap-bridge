# Periodic CMI-B shear specialization integration — 2026-09-06

**Classification:** `INFRASTRUCTURE / FORMALIZATION` with a proved **specialization** of the periodic unforced CMI alternative B. It is **not** a proof of Clay B for arbitrary periodic data and it does not modify the current `R^3`, unforced, axisymmetric breakdown `SPEC.md` track.

## Imported independent development

The user supplied an independently developed Astra/Lean bundle containing source for

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
- the audited named theorems depending only on `propext`, `Classical.choice`, and `Quot.sound`;
- no `sorryAx` in the audited dependency closure.

The repository already pins the same Lean version and the same mathlib commit through `lean-toolchain` and `lake-manifest.json`. Therefore no dependency or toolchain change is needed.

## Integration choices

The standalone package files are integrated under the repository's existing `Formal.+` target:

- `Formal/PeriodicClayCore.lean`;
- `Formal/PeriodicExplicitShear.lean`;
- `Formal/PeriodicClayShear.lean`;
- `Formal/PeriodicClayEnergy.lean`;
- `Formal/PeriodicClayQuantifiers.lean`;
- `Formal/PeriodicClayCertificate.lean`.

The mathematical source of the first four modules and the final certificate is preserved except for repository import paths and integration comments.

The uploaded bundle did **not** contain `ClayQuantifiers.lean`; it contained only `ClayQuantifiers.olean` plus documentation and verification evidence naming its three theorems. `Formal/PeriodicClayQuantifiers.lean` is therefore a **repo-authored source reconstruction**, not a byte-for-byte import. It proves the documented logical roles directly from the integrated `ClayB` definition:

- `ClayNS.not_clayB_iff_unforcedPeriodicObstruction`;
- `ClayNS.failure_of_clayB_has_nonzero_datum`;
- `ClayNS.covering_solved_family_implies_clayB`.

The compiled `.olean` files are deliberately not vendored. The standalone `lakefile.lean`, `lean-toolchain`, and `verify.ps1` are also not vendored because this repository already has the matching pinned dependency graph and its own verification contract. The independent log remains provenance; repository Lean CI must recompile the integrated source.

## Mathematical certificate

For every `ν > 0` and every `a ≠ 0`, define

\[
u_0(x)=\bigl(a\sin(2\pi x_2),0,0\bigr),
\]

\[
u(t,x)=\bigl(a e^{-4\pi^2\nu t}\sin(2\pi x_2),0,0\bigr),
\qquad p(t,x)=0.
\]

The integrated predicate contains the full coordinate momentum equation with convection present, divergence-free condition, initial condition, joint smoothness on nonnegative time, and spatial unit periodicity of both velocity and pressure. For this shear family the convection term is proved to vanish.

The main certificate is

`ClayNS.certified_nonzero_periodic_NS`.

It proves, for positive viscosity and nonzero amplitude:

1. the shear datum is smooth, divergence-free, unit-periodic, and nonzero;
2. the explicit shear is a global smooth periodic solution of the unforced three-dimensional Navier--Stokes predicate;
3. the squared-velocity density is integrable on the unit cube and its cell integral lies in `[0,a^2]` for every nonnegative time.

The quantifier-visible theorem

`ClayNS.clayB_has_nonzero_smooth_specialization`

proves

\[
\forall \nu>0\;\exists u_0\neq0\;\exists u,p:
\operatorname{AdmissiblePeriodicDatum}(u_0)\land
\operatorname{GlobalPeriodicSolution}(\nu,u_0,u,p).
\]

## Exact claim boundary

The integrated definition

`ClayNS.ClayB`

has the universal datum quantifier

\[
\forall u_0\;\operatorname{AdmissiblePeriodicDatum}(u_0)\to\exists u,p\;\cdots.
\]

That universal statement is **not proved**. The shear family covers only a special infinite-parameter class. `covering_solved_family_implies_clayB` makes the missing logical bridge explicit: a solved family would imply B only after a separate coverage theorem showing that every admissible periodic datum belongs to that family. No such coverage theorem is claimed for the shear data.

This result also does not supply whole-space rapidly decaying data and therefore is not a Clay-A construction. It does not prove blow-up and is unrelated to the active B2 breakdown mechanism except at the repository-level A/B/C/D target.

## Relation to the existing formal stack

This is intentionally a **sidecar periodic-domain certificate** rather than an adapter to the existing `R^3` Bessel/Fourier mild-solution stack. It should not be used to identify periodic fields with the whole-space `R^3` carriers.

Its value to the project is different:

- it gives a concrete global, nonzero, arbitrary-amplitude sanity-check solution of the actual nonlinear periodic PDE predicate;
- it supplies a machine-checked periodic-B endpoint formulation and explicit scope/quantifier examples;
- it gives a regression target for any future periodic-domain (`B` or `D`) formal layer;
- it exposes the exact universal-data coverage gap rather than allowing a special family to be paraphrased as Clay B.

No change to `SPEC.md` is made. The current primary attack remains the `R^3`, `f=0`, axisymmetric-with-swirl breakdown track.

## Verification ruling

The user's independent bundle has a green local verification record on the exact Lean/mathlib revisions already pinned by this repository. That evidence does **not** by itself certify the renamed/import-adapted repository files, and it does not certify the repo-authored quantifier reconstruction.

The integration branch must therefore pass the repository's own forbidden-source scan and full `Formal.+` build before this formal frontier is treated as green or merge-ready.
