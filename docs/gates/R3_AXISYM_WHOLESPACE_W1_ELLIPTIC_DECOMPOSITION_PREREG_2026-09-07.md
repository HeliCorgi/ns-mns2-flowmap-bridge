# R3 W1 elliptic discretization / boundary-error decomposition — preregistration

Date: 2026-09-07 JST

Status: **FROZEN BEFORE OUTPUT**

## Motivation and parent stops

The repaired Green reference passed independently in PR #113, but the versioned dynamic-domain audit v2 in PR #114 stopped because the original fixed-grid A4 rule compared `h=.04` finite-difference box solutions directly to the continuum Q6 Green reference and the absolute error increased under box expansion.

Permanent parent statuses:

```text
PR #112  R3-W1-DYNAMIC-DOMAIN-AUDIT    = STOP_REPAIR_GREEN_QUADRATURE
PR #113  R3-W1-GREEN-QUADRATURE-REPAIR = PASS
PR #114  R3-W1-DYNAMIC-DOMAIN-AUDIT-V2 = STOP_REPAIR_DYNAMIC_DOMAIN
```

PR #114 also showed that adjacent same-discretization box changes decreased strongly while the Q6 absolute error did not. A plausible diagnostic hypothesis is that fixed-grid spatial discretization error dominates the continuum comparison and can partially cancel finite-box boundary error on smaller boxes.

This gate tests that hypothesis without changing any stopped parent decision.

## Frozen common source and continuum reference

Regenerate exactly the same B44 final `omega1` source as PRs #112–#114:

```text
nu=.01, A=.16, R=Z=1, alpha=16
B44=(4,4)
dynamic h=.04
RK4, T=2e-4, dt=2.5e-5, eight accepted steps
```

Build the same exact cubic continuous source interpolant

```text
RectBivariateSpline(kx=3, ky=3, s=0)
```

through that B44 nodal source.

The independent continuum free-space receiver reference remains exactly the passed Q6 rule from PR #113:

```text
source-cell Gauss-Legendre order 6
theta Gauss-Legendre order 144
```

at the same four receivers

```text
(0.12,  0.00)
(0.24,  0.20)
(0.28, -0.24)
(0.20,  0.32).
```

## Frozen finite-box family

Use the same six zero-Dirichlet nonperiodic boxes:

```text
B22=(2,2), B32=(3,2), B42=(4,2),
B23=(2,3), B24=(2,4), B44=(4,4).
```

For every box, solve the same discrete `-L5 psi = omega1` problem at

```text
h=.04 and h=.02
```

using source values obtained by evaluating the same frozen cubic B44 source interpolant on that box/grid.

For the spatial-order validation box B22 only, also solve at

```text
h=.01.
```

All receivers are grid-aligned at `.04/.02/.01`. Every Poisson solve must have algebraic relative residual `<=1e-10`.

No dynamic evolution is rerun at `.02` or `.01`; this is an elliptic decomposition gate only.

## E0 — source / Green reproduction

The B44 source-generation run must satisfy the same runtime/source checks used in the passed Green repair: eight accepted steps, zero rejects, finite values, frozen stability/CFL/viscous gates, Poisson residual `<=1e-10`, odd-z defect `<=1e-12`, energy ratio `<=1+1e-5`, energy-balance defect `<=.20`, outside-B22 lifted-L1 fraction `<=1e-12`, and normalized lifted odd monopole `<=1e-12`.

Reproduce Q6 together with

```text
Q4T = source-cell order 4, theta 144
Q6T = source-cell order 6, theta 96
```

and require the independently frozen repair isolations

```text
rel(Q4T,Q6) <= 7.5e-4
rel(Q6T,Q6) <= 7.5e-4.
```

E0 failure gives the corresponding source/Green repair stop and no decomposition is promoted.

## E1 — finite-box spatial-order validation on B22

Let `R_h(B22)` be the 4x3 receiver vector for the zero-boundary B22 solve at spacing `h`.

Define

```text
d42 = rel(R_.04, R_.02)
d21 = rel(R_.02, R_.01).
```

E1 passes iff

```text
d21 <= .35 * d42.
```

This is the predeclared second-order consistency requirement. The `.35` ratio matches the established refinement convention used elsewhere in the R3 numerical stack while allowing modest pre-asymptotic deviation from the ideal `.25`.

## E2 — Richardson stabilization on B22

Assuming second-order leading spatial error, define

```text
X42 = (4 R_.02 - R_.04) / 3
X21 = (4 R_.01 - R_.02) / 3.
```

Require

```text
rel(X42, X21) <= .35 * d21.
```

This tests that the predeclared second-order extrapolation is itself stabilizing rather than merely fitting one refinement ratio.

## E3 — discretization-reduced box-direction test

For each of the six boxes define the frozen second-order Richardson receiver estimate

```text
X_B = (4 R_.02(B) - R_.04(B)) / 3
```

and continuum-reference error

```text
e_B = rel(X_B, Q6).
```

Retest the **same original radial/axial direction question** using these discretization-reduced estimates:

```text
e_B32 < e_B22
e_B42 < e_B32
e_B23 < e_B22
e_B24 < e_B23
e_B44 <= min(e_B42,e_B24).
```

All five rows are binding. No post-output monotonicity replacement is allowed.

## Descriptive rows

Record, but do not use as substitutes for E1–E3:

- raw `.04` and `.02` errors to Q6 for each box;
- raw inter-resolution difference `rel(R_.04,R_.02)` for each box;
- adjacent box changes at `.04`, `.02`, and after Richardson extrapolation;
- Richardson correction magnitude for each box.

These rows are diagnostic only.

## Exact decision hierarchy

If E0 source reproduction fails:

```text
R3-W1-ELLIPTIC-DECOMPOSITION = STOP_REPAIR_GREEN_SOURCE_REPRODUCTION
```

If E0 Green isolation fails:

```text
R3-W1-ELLIPTIC-DECOMPOSITION = STOP_REPAIR_GREEN_QUADRATURE
```

If any finite-box Poisson residual, E1, or E2 fails:

```text
R3-W1-ELLIPTIC-DECOMPOSITION = STOP_REPAIR_ELLIPTIC_DISCRETIZATION
```

If E1/E2 pass but any E3 box-direction row fails:

```text
R3-W1-ELLIPTIC-DECOMPOSITION = STOP_REPAIR_DYNAMIC_DOMAIN
```

Only if E0–E3 all pass:

```text
R3-W1-ELLIPTIC-DECOMPOSITION = PASS
```

## Interpretation boundary

A PASS would support the narrow diagnosis that the PR #114 fixed-`h` A4 failure was contaminated by leading spatial discretization error and that the original box-direction trend reappears after a separately validated second-order extrapolation.

It would not retroactively convert PR #114 into a PASS, would not certify long-time dynamics, and would not by itself authorize a claim that `h=.04` is quantitatively accurate enough for a candidate scan. Any later dynamic pilot still requires its own resolution and streaming diagnostics.

## Nonclaims

This gate is not a continuum theorem, not a rigorous whole-space truncation enclosure, not a long-time production evolution, not evidence of finite-time blow-up or global regularity, and not a Clay A/B/C/D result.
