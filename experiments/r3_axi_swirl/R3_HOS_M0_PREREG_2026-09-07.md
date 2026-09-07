# R3 high-order s-coordinate method M0 preregistration — 2026-09-07

**Classification:** `NUMERICAL METHOD QUALIFICATION / PRE-EXECUTION CONTRACT`.

The centered-second-order / zero-Dirichlet qualification path is parked after the bounded R3S04
E2R failure and the single R3S02 alternate-datum failure. This document opens a genuinely new
numerical-method gate before any further nonlinear candidate evolution.

The new method exploits the exact smooth axisymmetric variable `s=r^2`. For every smooth even
normalized scalar `f(r,z)=g(s,z)`,

\[
\mathcal L_5 f
=\partial_r^2 f+\frac3r\partial_r f+\partial_z^2f
=4s\,g_{ss}+8g_s+g_{zz}.
\]

The method therefore differentiates in nonuniform `s_i=r_i^2` with local high-order polynomial
stencils, while retaining the physical 3D measure `2*pi*r dr dz` and the original `r,z` physical
domain. This is a scalar-coordinate discretization only; it is not a five-dimensional fluid.

## M0 scope

M0 qualifies only:

1. the high-order nonperiodic elliptic inversion `-L5 psi=omega`;
2. the high-order `s`/`z` first-derivative operators needed for reconstruction/evolution;
3. artificial-boundary sensitivity and a low-axial-frequency stress.

No Navier--Stokes time evolution is permitted to inherit qualification from the old centered-FD
E1/E2 stack. A nonlinear HOS evolution contract may be written only if this M0 passes.

## Frozen discrete method

Use node-centered physical `r` grids with `r_i=i*Rmax/nr` and nonperiodic `z` grids with
`z_j=-Zmax+j*(2 Zmax/nz)`. Transform only the radial differentiation coordinate to
`s_i=r_i^2`.

At each derivative location, use a deterministic local **7-node polynomial differentiation
stencil**. Choose the nearest contiguous seven nodes, biased only as required near an outer
boundary. Compute weights from the scaled local Vandermonde moment conditions so polynomials
through degree six are differentiated exactly in floating arithmetic up to solver roundoff.

For the radial scalar operator use directly

\[
-(4sD_{ss}+8D_s),
\]

including at `s=0`, where it becomes `-8 D_s`; no singular `3/r` expression or post-hoc axis
condition is evaluated.

For `z`, use the same seven-node local polynomial construction for `-D_{zz}` with strictly
nonperiodic outer Dirichlet values. The sparse elliptic system includes unknowns at the axis,
excludes the outer radial boundary, and excludes both axial boundaries. Known boundary
contributions are moved to the right-hand side exactly.

The method is `float64` for M0. It is not interval arithmetic.

## Frozen M0-A — smooth Gaussian free-space reference

Use the existing exact 5D-radial scalar reference

\[
\omega=e^{-(r^2+z^2)/a^2},\qquad a=0.25,
\]

with exact free-space Dirichlet values on the artificial boundary, on
`(Rmax,Zmax)=(1.0,1.2)` and the ladder

```text
nr x nz
20 x 48
30 x 72
40 x 96
```

Record `psi` Linf, physical weighted-L2, radial/axial first-derivative Linf, combined derivative
weighted-L2, and algebraic residual. Require every error metric to decrease strictly through the
ladder and the final algebraic residual to be `<1e-9`.

No minimum observed convergence order is selected post hoc; monotonicity is the M0-A gate.

## Frozen M0-B — direct derivative manufactured audit

For the exact compact continuum fields of both `R3S04` and `R3S02`, on the base box
`(Rmax,Zmax)=(1.0,0.9)`, test the high-order operators directly on exact sampled data at

```text
160 x 288
200 x 360
240 x 432
```

Compare numerical versus analytic

```text
psi1_s, psi1_z, u1_s, u1_z
```

using Linf and physical weighted-L2 norms on the full unknown grid. Require every one of these
eight seed/norm sequences to decrease strictly from 160 -> 200 -> 240 for **both** R3S04 and
R3S02.

This gate is independent of elliptic inversion and directly targets the derivative nonmonotonicity
that stopped the centered-FD path.

## Frozen M0-C — compact elliptic recovery for both stopped data

Recover the exact compact `psi1` from its analytically derived `omega1=-L5 psi1`, with zero outer
Dirichlet values, on the same `160/200/240` ladder and base box `(1.0,0.9)`, separately for
R3S04 and R3S02.

For each seed require strict decrease through the ladder for

```text
psi Linf
psi physical weighted-L2
grad-r Linf
grad-z Linf
grad combined physical weighted-L2
```

and on the 240 grid require

```text
psi Linf                 < 1e-3
psi physical weighted-L2 < 1e-4
algebraic residual Linf  < 1e-9
```

The thresholds match the prior compact E0 qualification; none is weakened for the new method.

## Frozen M0-D — low-axial-frequency stress

Use the existing manufactured profile

\[
\psi=\exp(-r^2/0.20^2-z^2/0.80^2)
\]

on a strictly nonperiodic box with exact boundary values and the same `24/48/96`-scale stress
used by the old E0 audit. Require every field/first-derivative error metric to decrease strictly
through refinement and final algebraic residual `<1e-9`.

This prevents a periodic Fourier gap from entering the new method by construction.

## Frozen M0-E — artificial-boundary sensitivity

For the nonzero-tail Gaussian source with zero artificial Dirichlet values, hold physical mesh
scale approximately `0.02` and measure error on the fixed inner core `r<=0.45`, `|z|<=0.45`.
Require strict decrease of core Linf and physical weighted-L2 error under each of:

```text
square:      (0.6,0.6) -> (0.8,0.8) -> (1.0,1.0) -> (1.5,1.5)
radial-only: (0.6,1.5) -> (0.8,1.5) -> (1.0,1.5) -> (1.5,1.5)
axial-only:  (1.5,0.6) -> (1.5,0.8) -> (1.5,1.0) -> (1.5,1.5)
```

This is only a truncation-sensitivity diagnostic, not a rigorous whole-space tail enclosure.

## Decision

M0 passes only if all M0-A through M0-E pass:

```text
R3-HOS-M0-METHOD-QUALIFICATION = PASS
```

Only then may an HOS nonlinear E1 contract be preregistered. If any gate fails:

```text
R3-HOS-M0-METHOD-QUALIFICATION = FAIL
```

and no nonlinear run may rescue it. A method defect may be repaired only on a new revision with
the same frozen mathematical tests and explicit hosted provenance; thresholds or test fields may
not be changed after observing results.

## Nonclaims

M0 is a floating-point method qualification. PASS would not establish continuum convergence,
validated free-space inversion, finite-time singularity, global regularity, or Clay A/B/C/D.
