# R3 W1 arbitrary-source Green quadrature repair — preregistration

Date: 2026-09-07 JST

Status: **FROZEN BEFORE ANY OUTPUT FROM THE REPAIRED QUADRATURE RULE**

## Purpose and inherited negative knowledge

The stopped dynamic-domain audit in PR #112 produced the binding machine decision

```text
R3-W1-DYNAMIC-DOMAIN-AUDIT = STOP_REPAIR_GREEN_QUADRATURE
```

because its independent Green self-check compared midpoint source quadratures `(dr=dz=.04, ntheta=48)` and `(dr=dz=.02, ntheta=80)` and observed combined relative difference `5.475750929947053e-3 > 2e-3`.

That stopped result is permanent and is not reclassified here. In particular, PR #112's A4 finite-box-versus-Green trend is not promoted because its Green reference failed first.

This new gate repairs **only** the arbitrary-source free-space Green quadrature. No box, datum, PDE, timestep, receiver, interpolation family, or late-time claim is changed.

## Frozen source and receivers

The source is regenerated deterministically from the same B44 early-time evolution used by PR #112:

```text
nu = .01
A = .16
R = Z = 1
alpha = 16
box = (Rmax,Zmax) = (4,4)
h = .04
integrator = RK4
T = 2e-4
dt = 2.5e-5
accepted steps = 8
```

The Green source is the final numerical `omega1` on that B44 nodal grid. The four receivers remain exactly

```text
(0.12,  0.00)
(0.24,  0.20)
(0.28, -0.24)
(0.20,  0.32)
```

The nodal source is reconstructed by the same exact cubic `RectBivariateSpline(kx=3, ky=3, s=0)` used in the stopped PR #112 Green path. Changing the interpolation family after seeing this repair output is forbidden.

## Frozen Green representation

The reduced five-dimensional free-space representation and its receiver derivatives are unchanged from PR #112. For each receiver `(r,z)` the quadrature evaluates the same three quantities

```text
psi, d_r psi, d_z psi
```

with angular Gauss-Legendre integration on `[0,pi]` and the same coefficient `1/(2*pi)`, `rho^3` lifted measure, and kernels

```text
D  = r^2 + rho^2 - 2 r rho cos(theta) + (z-zeta)^2
K0 = D^(-3/2)
Kr = -3 (r-rho cos(theta)) D^(-5/2)
Kz = -3 (z-zeta) D^(-5/2).
```

## Repair: cellwise source quadrature

The failed global midpoint rule is replaced by a tensor Gauss-Legendre rule **inside every original h=.04 source grid cell**. No source-cell midpoint approximation is used.

For source order `q`, every radial cell `[r_i,r_{i+1}]` and axial cell `[z_j,z_{j+1}]` receives the mapped `q`-point Gauss-Legendre nodes and weights in each coordinate. The cubic spline is evaluated at those cellwise nodes. All B44 cells are included; there is no source truncation, thresholding, or post-output masking.

Three predeclared increasing production levels are

```text
Q2: source cell order q=2, theta order 64
Q4: source cell order q=4, theta order 96
Q6: source cell order q=6, theta order 144
```

Two isolation evaluations are also frozen:

```text
Q4T: source cell order q=4, theta order 144
Q6T: source cell order q=6, theta order 96
```

Thus the final reference candidate is exactly `Q6`.

## Norms

For two 4x3 receiver arrays `A,B`, define

```text
rel(A,B) = ||A-B||_2 / max(||B||_2, 1e-30).
```

For componentwise comparison, let

```text
scale = max(abs(Q6))
active components = {k : abs(Q6_k) >= 1e-3 * scale}
component_relative_k = abs(A_k-B_k) / max(abs(B_k), 1e-30).
```

The active-component mask excludes symmetry-forced near-zero components but includes every receiver component carrying at least 0.1% of the largest final-reference magnitude.

## Gate G0 — deterministic source/runtime reproduction

The B44 source generation must complete exactly eight accepted RK4 steps, zero rejected steps, finite stages and states, frozen-symbol amplification `<= 1 + STABILITY_TOL`, CFL `<= .10`, viscous number `<= .05`, Poisson residual `<= 1e-10`, odd-z defect `<= 1e-12`, energy ratio `<= 1+1e-5`, and energy-balance defect `<= .20`.

The inherited source checks must also satisfy

```text
outside-B22 lifted-L1 fraction <= 1e-12
normalized lifted odd monopole <= 1e-12.
```

Failure of G0 gives `STOP_REPAIR_GREEN_SOURCE_REPRODUCTION`.

## Gate G1 — three-level combined convergence

Define

```text
d24 = rel(Q2,Q4)
d46 = rel(Q4,Q6).
```

G1 passes iff both

```text
d46 < d24
d46 <= 1.0e-3.
```

The strict decrease establishes directional convergence of the repaired family; the absolute `1e-3` requirement is twice as strict as the failed PR #112 Green self-check tolerance and is frozen before repaired output.

## Gate G2 — angular isolation

At fixed source cell order 6,

```text
dtheta = rel(Q6T,Q6)
```

must satisfy

```text
dtheta <= 7.5e-4.
```

This prevents a nominal source-cell repair from hiding an unresolved angular integral.

## Gate G3 — source-cell isolation

At fixed theta order 144,

```text
dsource = rel(Q4T,Q6)
```

must satisfy

```text
dsource <= 7.5e-4.
```

This directly tests the repaired cellwise source quadrature at the final angular order.

## Gate G4 — active-component stability

On the active-component mask defined above, the maximum componentwise relative difference between `Q4T` and `Q6` must be

```text
<= 1.0e-2.
```

This is a guard against a small combined norm concealing an unresolved physically non-negligible receiver component.

## Exact decision rule

If G0 fails:

```text
R3-W1-GREEN-QUADRATURE-REPAIR = STOP_REPAIR_GREEN_SOURCE_REPRODUCTION
```

Else if any of G1–G4 fails:

```text
R3-W1-GREEN-QUADRATURE-REPAIR = STOP_REPAIR_GREEN_QUADRATURE
```

Only if G0–G4 all pass:

```text
R3-W1-GREEN-QUADRATURE-REPAIR = PASS
```

A PASS certifies only that this numerical free-space Green evaluation is sufficiently self-resolved for a **versioned rerun** of the stopped early dynamic-domain audit. It does not retroactively change PR #112 and does not itself certify any finite-box trend.

## Forbidden post-output changes

After production output, do not change any of the following in this gate:

- B44 source evolution or timestep;
- receivers;
- cubic source interpolation family;
- reduced Green kernel or lifted measure;
- source orders 2/4/6;
- theta orders 64/96/144;
- isolation evaluations Q4T/Q6T;
- active-component mask;
- G0–G4 tolerances or decision hierarchy.

If the gate stops, archive the stop and open a separately versioned repair rather than loosening this preregistration.

## Nonclaims

This gate is not:

- a long-time production evolution;
- a continuum convergence theorem;
- a whole-space truncation theorem;
- evidence for finite-time blow-up or global regularity;
- a Clay A/B/C/D result.
