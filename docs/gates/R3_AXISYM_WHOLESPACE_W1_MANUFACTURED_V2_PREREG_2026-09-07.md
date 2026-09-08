# R3 W1 short-time manufactured nonlinear gate v2 — preregistration (2026-09-07)

**Status:** frozen before any v2 production output. This is a new version after the independently preregistered divergence-diagnostic repair passed. It does not alter the permanent v1 decision

```text
R3-W1-MANUFACTURED-v1 = STOP_REPAIR_W1_MANUFACTURED.
```

No long-time amplification, singularity, regularity, continuum-convergence, or Clay A/B/C/D claim is made.

## 1. Inherited frozen scope

V2 keeps the v1 PDE, datum, box, grids, time horizon, time step, integrators, exact initial-derivative formulas, and every non-divergence M1–M5 threshold unchanged.

Exactly:

```text
nu = 0.01
A = 0.16
R = Z = 1
alpha = 16
kappa = 1
Rmax = Zmax = 2
h = 0.04, 0.02
T = 2.0e-4
dt = 2.5e-5
primary integrator = classical RK4
comparison integrator = SSPRK3
```

Each run must complete exactly eight accepted steps with zero post-hoc retry.

The normalized system remains

```text
u1_t + ur u1_r + uz u1_z = 2 psi_z u1 + nu L5 u1
omega1_t + ur omega1_r + uz omega1_z = d_z(u1^2) + nu L5 omega1
-L5 psi = omega1
ur = -r psi_z
uz = 2 psi + r psi_r
L5 = d_rr + (3/r)d_r + d_zz.
```

Outer finite-box values remain homogeneous. This is still a short-time finite-box manufactured preflight; W0 is the independent static whole-space audit and evolved-source tail control remains open.

## 2. Inherited M1, M2, M3, and M5 conditions

All thresholds are copied without relaxation from manufactured-v1.

### M1 initial RHS

```text
h=.04: u1 <= .020, omega1 <= .025
h=.02: u1 <= .006, omega1 <= .006
fine <= .35 * coarse for both fields.
```

### M2 first-step RK4 secant

```text
h=.04: u1 <= .025, omega1 <= .030
h=.02: u1 <= .008, omega1 <= .008
fine < coarse for both fields.
```

### M3 per-stage stability/CFL

For RK4 and SSPRK3 on both grids:

```text
all stage/state values finite
max frozen-symbol amplification <= 1 + 1e-10
max CFL <= .10
max viscous number <= .05
rejected_steps = 0.
```

### M5 integrator/resolution cross-check

```text
RK4 vs SSPRK3 combined-state difference:
  h=.04 <= 2e-6
  h=.02 <= 2e-6

RK4 h=.04 vs injected h=.02:
  u1 <= 2e-4
  omega1 <= .030.
```

## 3. Inherited M4 non-divergence conditions

For every accepted step of every run, keep the v1 conditions unchanged:

```text
max relative Poisson residual <= 1e-10
max odd-z defect <= 1e-12
max_t E(t)/E(0) <= 1 + 1e-5
max stepwise energy-balance defect <= .20
all states finite.
```

Physical energy/enstrophy use `2 pi r dr dz` and the same reconstructed vorticity as v1.

## 4. Repaired divergence diagnostic — frozen before v2 output

The repair gate `R3-W1-DIVERGENCE-DIAGNOSTIC-REPAIR` passed on two manufactured streamfunctions and three aligned grids. It verified that, for the same centered reconstruction,

```text
q = D_z psi
ur = -r q
uz = 2 psi + r D_r psi
```

the independently differentiated divergence obeys the exact discrete identity

```text
div_ind = D_r ur + ur/r + D_z uz
         = q_i - (q_{i+1}+q_{i-1})/2
         =: div_pred,
```

on the common centered interior stencil, while the independent residual itself is `O(h^2)`. It separately verified roundoff cancellation of

```text
div_compat = r (D_z D_r psi - D_r D_z psi).
```

V2 therefore does **not** reuse the invalid v1 absolute requirement `relative recovered divergence <= 1e-10`.

All v2 divergence checks use the frozen core

```text
0.16 <= r <= 0.80
|z| <= 0.80.
```

For each accepted step define

```text
identity_rel = ||div_ind-div_pred||_inf /
               max(||div_ind||_inf, ||div_pred||_inf, 1e-30)

independent_rel = ||div_ind||_inf /
                  max(||D_r ur||_inf + ||ur/r||_inf + ||D_z uz||_inf, 1e-30)

compat_rel = ||div_compat||_inf /
             max(||r D_z D_r psi||_inf + ||r D_r D_z psi||_inf, 1e-30).
```

### M4-D1 exact defect identity

For every accepted step, both integrators, both grids:

```text
identity_rel <= 1e-9.
```

The repair manufactured test achieved a worst value `6.2e-12`; `1e-9` is frozen here before nonlinear v2 output to allow scaling/roundoff effects when `psi` is initially very small. This is a new versioned tolerance, not a retroactive v1 relaxation.

### M4-D2 second-order refinement of the independent diagnostic

At each of the eight matched accepted times, separately for RK4 and SSPRK3, require

```text
independent_rel(h=.02) <= .35 * independent_rel(h=.04).
```

The factor `.35` is inherited from the independently preregistered repair gate. No absolute magnitude threshold is imposed on `independent_rel`; the quantity is a truncation diagnostic, not an algebraic invariant.

### M4-D3 compatible roundoff check

For every accepted step, both integrators, both grids:

```text
compat_rel <= 1e-12.
```

This is the discrete algebraic check expected to cancel to roundoff.

The report must retain the old v1-style independently differentiated divergence value as a descriptive legacy field if convenient, but it is not an acceptance criterion in v2.

## 5. Decision

Only if every inherited M1/M2/M3/M4(non-divergence)/M5 condition and every new M4-D1/D2/D3 condition passes:

```text
R3-W1-MANUFACTURED-V2 = PASS.
```

Otherwise:

```text
R3-W1-MANUFACTURED-V2 = STOP_REPAIR_W1_MANUFACTURED_V2.
```

No failed condition may be rescued by changing `A`, `nu`, box, grid, `dt`, horizon, integrator, diagnostic core, or tolerance after output is inspected.

A v2 PASS permits only the design of a separately preregistered candidate-time pilot. Before any late-time or singularity interpretation, evolved-source whole-space tail control, independent discretization checks, explicit resolution-scale diagnostics, and ultimately rigorous numerical error enclosure remain open.
