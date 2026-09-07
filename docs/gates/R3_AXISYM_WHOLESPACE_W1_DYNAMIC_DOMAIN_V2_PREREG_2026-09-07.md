# R3 W1 early dynamic-domain / elliptic-boundary audit v2 — preregistration

Date: 2026-09-07 JST

Status: **FROZEN BEFORE V2 OUTPUT**

## Parent history and version boundary

The original audit in PR #112 is permanently archived as

```text
R3-W1-DYNAMIC-DOMAIN-AUDIT = STOP_REPAIR_GREEN_QUADRATURE
```

because its midpoint-based free-space Green reference failed its own self-check before A4 could be interpreted.

The separate Green repair in PR #113 then passed the preregistered cellwise quadrature gate:

```text
R3-W1-GREEN-QUADRATURE-REPAIR = PASS
```

with final repaired reference candidate exactly

```text
Q6 = source-cell Gauss-Legendre order 6, theta Gauss-Legendre order 144.
```

This v2 audit changes **only** the version of the independent Green reference. All original dynamic boxes, PDE/data/time/grid choices, A0/A1/A2 rules, finite-box Poisson construction, receiver extraction, and A4 monotonic direction rules are inherited unchanged from PR #112.

The stopped PR #112 result is not retroactively changed regardless of v2 outcome.

## Frozen dynamics and boxes

Use the same datum and early-time RK4 evolution as PR #112:

```text
nu = .01
A = .16
R = Z = 1
alpha = 16
h = .04
T = 2e-4
dt = 2.5e-5
integrator = RK4
```

Six nonperiodic boxes are unchanged:

```text
B22 = (2,2)
B32 = (3,2)
B42 = (4,2)
B23 = (2,3)
B24 = (2,4)
B44 = (4,4)
```

The common dynamic comparison core remains

```text
r <= .8, |z| <= .8.
```

The four receiver locations remain exactly

```text
(0.12,  0.00)
(0.24,  0.20)
(0.28, -0.24)
(0.20,  0.32).
```

## A0 — inherited all-step runtime gate

For every one of the six dynamic runs, require exactly eight accepted steps, zero rejected steps, completed run, finite stages/states, frozen-symbol amplification `<= 1 + STABILITY_TOL`, CFL `<= .10`, viscous number `<= .05`, max stage/step Poisson residual `<= 1e-10`, odd-z defect `<= 1e-12`, energy ratio `<= 1+1e-5`, and energy-balance defect `<= .20`.

No reconstructed-divergence threshold is added here; the divergence diagnostic was separately repaired and certified before manufactured-v2.

## A1 — inherited dynamic common-core sensitivity

Define the same combined relative state differences in `(u1,omega1)` on the common core:

```text
dR23 = B22 vs B32
dR34 = B32 vs B42
dZ23 = B22 vs B23
dZ34 = B23 vs B24.
```

The inherited floor-aware rules remain

```text
radial PASS iff max(dR23,dR34) <= 1e-10 OR dR34 <= .50 dR23
axial  PASS iff max(dZ23,dZ34) <= 1e-10 OR dZ34 <= .50 dZ23.
```

The B42-vs-B44 and B24-vs-B44 common-core differences remain descriptive only.

## A2 — inherited common B44 source audit

The common elliptic source is still the final B44 numerical `omega1` field. Require

```text
outside-B22 lifted-L1 fraction <= 1e-12
normalized lifted odd monopole <= 1e-12.
```

No source truncation is used in the Green reference.

## A3-v2 — repaired free-space Green reference reproduction

Construct the same cubic source interpolant used by the passed Green repair:

```text
RectBivariateSpline(kx=3, ky=3, s=0)
```

and evaluate the full B44 source with the repaired cellwise rule.

The production reference is exactly

```text
Q6 = source-cell order 6, theta order 144.
```

To ensure that the repaired reference is reproduced on the v2 source, also evaluate

```text
Q4T = source-cell order 4, theta order 144
Q6T = source-cell order 6, theta order 96.
```

Require the same isolation tolerances frozen in the passed repair:

```text
rel(Q4T,Q6) <= 7.5e-4
rel(Q6T,Q6) <= 7.5e-4.
```

If either A3-v2 row fails, the exact v2 decision is

```text
STOP_REPAIR_GREEN_QUADRATURE
```

and A4 is not promoted.

## A4 — inherited same-source finite-box / Green direction gate

For every box, restrict the **same B44 final source** to that box, solve the unchanged finite-difference zero-boundary Poisson problem, and extract `(psi,psi_r,psi_z)` at the same four receivers.

Define

```text
e_B = rel(receiver_vector_B, Q6).
```

The original PR #112 A4 direction rules are inherited verbatim:

```text
B32 < B22
B42 < B32
B23 < B22
B24 < B23
B44 <= min(B42,B24).
```

Each finite-box Poisson solve must also retain residual `<=1e-10`.

These monotonic rules are intentionally not changed after seeing the repaired Green output. If they fail, v2 stops even if adjacent finite-box differences themselves decrease.

For descriptive audit only, record the same adjacent receiver changes

```text
B22 vs B32
B32 vs B42
B22 vs B23
B23 vs B24.
```

## Exact decision hierarchy

1. If any A0/A1/A2 source/dynamic prerequisite fails, or any A4 non-Green Poisson row fails:

```text
R3-W1-DYNAMIC-DOMAIN-AUDIT-V2 = STOP_REPAIR_DYNAMIC_DOMAIN
```

2. If A3-v2 repaired-reference reproduction fails:

```text
R3-W1-DYNAMIC-DOMAIN-AUDIT-V2 = STOP_REPAIR_GREEN_QUADRATURE
```

3. If A3-v2 passes but any inherited A4 direction row fails:

```text
R3-W1-DYNAMIC-DOMAIN-AUDIT-V2 = STOP_REPAIR_DYNAMIC_DOMAIN
```

4. Only if every frozen row passes:

```text
R3-W1-DYNAMIC-DOMAIN-AUDIT-V2 = PASS
```

## Interpretation boundary

A v2 PASS would certify only this early-time numerical dynamic-domain/elliptic-boundary gate at the frozen discretization. A v2 STOP must be archived and diagnosed before any long-time candidate scan.

In particular, no A4 rule may be relaxed post hoc to compensate for fixed-grid discretization error, boundary error, or source interpolation error. Those effects require separately versioned gates if they become the next obstruction.

## Nonclaims

This v2 gate is not a continuum convergence theorem, not a whole-space truncation theorem, not a long-time production evolution, not evidence of finite-time blow-up or global regularity, and not a Clay A/B/C/D result.
