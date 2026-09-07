# R3 W1 resolution-aware early-time nonlinear dynamic audit — preregistration

Date: 2026-09-07 JST

Status: **FROZEN BEFORE OUTPUT**

## Purpose and parent state

The static elliptic decomposition gate in PR #115 passed and showed that the fixed-`h=.04` A4 failure in PR #114 was dominated by leading second-order spatial discretization error rather than by a growing box-boundary effect.

Permanent parent statuses remain:

```text
PR #112  dynamic-domain v1          = STOP_REPAIR_GREEN_QUADRATURE
PR #113  Green quadrature repair    = PASS
PR #114  dynamic-domain v2          = STOP_REPAIR_DYNAMIC_DOMAIN
PR #115  elliptic decomposition     = PASS
```

This gate asks the next narrower question: does the **nonlinear early-time dynamic implementation itself** exhibit the expected spatial refinement behavior, including its recovered elliptic/meridional velocity observables, while the remaining B22-vs-B44 boundary sensitivity is smaller than the measured discretization correction?

No candidate-time growth is inspected in this gate.

## Frozen PDE/data/time/integrator

Use the exact manufactured-v2 dynamic implementation and datum:

```text
nu=.01
A=.16
R=Z=1
alpha=16
RK4
T=2e-4
dt=2.5e-5
```

The five production dynamic runs are exactly

```text
B22 h=.04
B22 h=.02
B22 h=.01
B44 h=.04
B44 h=.02
```

No other box, resolution, timestep, or integrator is used for a binding row.

The common state-comparison core remains

```text
r <= .8, |z| <= .8.
```

The four elliptic/velocity receivers remain exactly

```text
(0.12,  0.00)
(0.24,  0.20)
(0.28, -0.24)
(0.20,  0.32).
```

All receivers are aligned on `.04/.02/.01` grids.

## R0 — all-step runtime gate on all five runs

Every dynamic run must complete exactly eight accepted RK4 steps with zero rejected steps, finite stages and states, frozen-symbol amplification `<=1+STABILITY_TOL`, CFL `<=.10`, viscous number `<=.05`, max stage/step Poisson residual `<=1e-10`, odd-z defect `<=1e-12`, energy ratio `<=1+1e-5`, and energy-balance defect `<=.20`.

The h=.01 run is intentionally included because its frozen viscous number remains below the already established `.05` runtime limit.

Failure of any R0 row gives

```text
R3-W1-DYNAMIC-RESOLUTION = STOP_REPAIR_DYNAMIC_RESOLUTION
```

## Frozen final-state comparison

For two same-box resolutions, restrict the finer `(u1,omega1)` arrays to the coarser grid by exact integer stride and compare only on the common core.

Define the combined relative state difference

```text
S(a,b) = sqrt(||u_a-u_b||_2^2 + ||w_a-w_b||_2^2)
         / max(sqrt(||u_b||_2^2 + ||w_b||_2^2),1e-30).
```

For B22 define

```text
S42 = S(h=.04, restricted h=.02)
S21 = S(h=.02, restricted h=.01).
```

## R1 — nonlinear state second-order refinement

R1 passes iff

```text
S21 <= .35 * S42.
```

This uses the same preregistered `.35` second-order refinement convention validated by the static elliptic decomposition.

## Frozen recovered elliptic and velocity receivers

At the final accepted time of each run, solve for `psi1` from the run's own final `omega1` on that same box/resolution and extract receiver triples

```text
P = (psi, psi_r, psi_z).
```

Convert these to meridional physical velocity pairs at each receiver using

```text
u_r = -r psi_z
u_z = 2 psi + r psi_r.
```

Let `V_h(B)` be the resulting 4x2 receiver array. Use the same Euclidean relative norm as the Green/elliptic gates.

For B22 define

```text
V42 = rel(V_.04, V_.02)
V21 = rel(V_.02, V_.01).
```

Every final elliptic solve must have algebraic Poisson residual `<=1e-10`.

## R2 — recovered-velocity second-order refinement

R2 passes iff

```text
V21 <= .35 * V42.
```

This is binding because the meridional velocity is the dynamic quantity through which the elliptic inversion feeds back into the nonlinear transport.

## R3 — boundary sensitivity subordinate to discretization correction

At h=.02 compare B22 and B44 on the common state core and at the receiver velocities.

Define

```text
Sbox02 = combined relative final-state difference B22 vs B44 at h=.02
Vbox02 = rel(V_.02(B22), V_.02(B44)).
```

Define the measured `.04/.02` discretization corrections

```text
Sres = max(S42(B22), S42(B44))
Vres = max(V42(B22), V42(B44)).
```

where `S42(B44)` and `V42(B44)` are the analogous B44 `.04/.02` differences.

R3 state passes iff

```text
max(Sbox02,Sres) <= 1e-10
OR
Sbox02 <= .50 * Sres.
```

R3 velocity passes iff

```text
Vbox02 <= .50 * Vres.
```

The `.50` factor is frozen before output and encodes the specific separation required by this gate: remaining box-boundary sensitivity must be clearly smaller than the directly measured discretization correction.

For audit only, also record the B22-vs-B44 state/velocity differences at h=.04 and the ratio of h=.02 to h=.04 box sensitivity. These rows are descriptive and cannot replace the binding R3 tests.

## R4 — resolution consistency across B22 and B44

Record the B44 `.04/.02` state and velocity differences. They are not required to match B22 numerically, but they must be finite and their final Poisson receiver solve must pass. No extra post-output ratio is introduced.

## Exact decision rule

If any R0 or final receiver-Poisson row fails, or if R1, R2, either R3 row fails:

```text
R3-W1-DYNAMIC-RESOLUTION = STOP_REPAIR_DYNAMIC_RESOLUTION
```

Only if every binding row passes:

```text
R3-W1-DYNAMIC-RESOLUTION = PASS
```

## Interpretation boundary

A PASS would certify only that the short-time nonlinear implementation is resolution-aware in the frozen `.04/.02/.01` hierarchy and that the residual early-time B22-vs-B44 effect is subordinate to the measured discretization correction.

Only then may a **separately preregistered candidate-time pilot** be designed. Such a pilot must retain streaming stability/finite/Poisson/parity/energy diagnostics, use matched resolutions, and remain diagnostic rather than claim singularity or regularity.

## Nonclaims

This gate is not a continuum theorem, not a rigorous whole-space truncation enclosure, not a long-time production evolution, not evidence of finite-time blow-up or global regularity, and not a Clay A/B/C/D result.
