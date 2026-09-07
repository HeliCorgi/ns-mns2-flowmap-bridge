# R3 W1 short-time manufactured nonlinear gate — preregistration (2026-09-07)

**Status:** frozen before production output. **No long-time amplification, singularity, regularity, continuum-convergence, or Clay A/B/C/D claim.**

The static W0 gate and the W1 frozen-coefficient stability-detector preflight have passed. This gate is the next deliberately small step: evolve the full normalized axisymmetric-with-swirl equations only for a very short physical time and verify that the implementation reproduces the exact first-time identities while satisfying the standing Fable5 P0-B/C per-stage/per-step diagnostics.

No parameter in this document may be relaxed after production output is inspected. A failure gives `STOP_REPAIR_W1_MANUFACTURED`; it does not authorize a different amplitude, time step, box, tolerance, or integrator as a post-hoc rescue.

## 1. Frozen PDE and numerical scope

Use exactly the `SPEC.md` normalized system

```text
u1_t + ur u1_r + uz u1_z = 2 psi_z u1 + nu L5 u1
omega1_t + ur omega1_r + uz omega1_z = d_z(u1^2) + nu L5 omega1
-L5 psi = omega1
ur = -r psi_z
uz = 2 psi + r psi_r
L5 = d_rr + (3/r)d_r + d_zz.
```

This is a finite-box, centered-difference **manufactured preflight**, not the eventual promoted production discretization. Outer values of `u1`, `omega1`, and `psi1` are set to zero on `r=Rmax` and `z=+-Zmax`. The axis uses evenness and the exact regular limit

```text
L5 f(0,z) = 4 f_rr(0,z) + f_zz(0,z).
```

The finite box is not identified with `R^3`; W0 supplies the independent static free-space audit, while an evolved-source tail enclosure remains a later obligation.

## 2. Frozen datum and short horizon

Use the W0 family normalized to

```text
nu = 0.01
R = 1
Z = 1
A = 0.16
alpha = A R^2 / nu = 16
kappa = Z/R = 1
```

with

```text
u1_0 = A b(r^2) z b(z^2)
omega1_0 = 0
psi1_0 = 0.
```

Freeze

```text
Rmax = 2
Zmax = 2
h = 0.04 and 0.02
T = 2.0e-4
dt = 2.5e-5
```

so each run has exactly eight accepted steps unless a fail-closed stability rejection occurs. A rejection in this manufactured row is itself a gate failure; it is not retried with a post-hoc smaller production `dt`.

Primary integrator: classical RK4. Comparison integrator: SSPRK3. Both use the same spatial operators, box, datum, target time, and output times.

## 3. Exact analytic first-time identities

For `0 <= s < 1`,

```text
b'(s)  = -b(s)/(1-s)^2
b''(s) =  b(s)*(2s-1)/(1-s)^4,
```

and both derivatives are zero outside the bump support.

Write

```text
f(r)=b(r^2),
g(z)=z b(z^2),
u1_0=A f g.
```

Then

```text
g_z  = b(z^2) + 2 z^2 b'(z^2)
g_zz = 6 z b'(z^2) + 4 z^3 b''(z^2)
L5 u1_0
 = A * [(8 b'(r^2) + 4 r^2 b''(r^2))*g(z) + f(r)*g_zz(z)]
partial_z(u1_0^2) = 2 A^2 f(r)^2 g(z) g_z(z).
```

Therefore the exact continuum initial derivatives are

```text
D_u_exact = nu L5 u1_0
D_w_exact = partial_z(u1_0^2).
```

All derivative comparisons below use the frozen core

```text
0 <= r <= 0.8
|z| <= 0.8
```

and the grid-Euclidean relative L2 norm. This norm is an implementation diagnostic and is not labeled a physical energy norm.

## 4. M1 — initial spatial RHS gate

Before taking a time step, evaluate the discrete nonlinear RHS at the exact initial state. Since `omega1_0=psi1_0=0`, the velocity is zero and the comparison directly tests the discrete `L5` and `d_z(u1^2)` operators.

Acceptance:

```text
h=.04:
  relerr(D_u_disc,D_u_exact) <= 0.020
  relerr(D_w_disc,D_w_exact) <= 0.025
h=.02:
  relerr(D_u_disc,D_u_exact) <= 0.006
  relerr(D_w_disc,D_w_exact) <= 0.006
```

and each fine-grid error must be at most `0.35` times its corresponding coarse-grid error.

## 5. M2 — first accepted-step secant gate

For RK4 on each grid, after the first accepted step define

```text
D_u_sec = (u1(dt)-u1_0)/dt
D_w_sec = (omega1(dt)-omega1_0)/dt.
```

Acceptance on the same core:

```text
h=.04:
  relerr(D_u_sec,D_u_exact) <= 0.025
  relerr(D_w_sec,D_w_exact) <= 0.030
h=.02:
  relerr(D_u_sec,D_u_exact) <= 0.008
  relerr(D_w_sec,D_w_exact) <= 0.008
```

and the fine error must be strictly smaller than the coarse error for both fields.

This is a first-time consistency test, not a proof of temporal order for finite `T`.

## 6. M3 — P0-B per-stage stability/CFL gate

At the pre-state and at every RK stage of every attempted step, record

```text
max_abs_ur
max_abs_uz
cfl = dt*(max_abs_ur/h + max_abs_uz/h)
viscous_number = nu*dt*(8/h^2 + 4/h^2)
frozen_symbol_max_amplification
```

where the symbol scan is the same fail-closed detector frozen in the W1 stability preflight, using the conservative interior radial stress

```text
c_r_eff = max_abs_ur + 3 nu/h.
```

Acceptance for both RK4 and SSPRK3 and both grids:

```text
all states finite
max frozen_symbol_max_amplification <= 1 + 1e-10
max cfl <= 0.10
max viscous_number <= 0.05
rejected_steps = 0.
```

The zero Fourier mode may attain amplification exactly one.

## 7. M4 — P0-C all-step streamed diagnostics

For every accepted step, not merely stored output snapshots, record and stream maxima/minima of:

- finite-state check;
- relative Poisson algebraic residual;
- odd-z parity defects of `u1`, `omega1`, and `psi1`;
- recovered physical divergence on the two-cell interior away from the axis and outer boundary;
- physical kinetic energy using `2 pi r dr dz`;
- physical enstrophy reconstructed from

```text
omega^r = -r d_z u1
omega^theta = r omega1
omega^z = 2 u1 + r d_r u1;
```

- stepwise energy-balance diagnostic

```text
B_E = |(E_{n+1}-E_n)/dt + 2 nu*(Omega_n+Omega_{n+1})/2|
      / max(2 nu*(Omega_n+Omega_{n+1})/2, 1e-30).
```

Acceptance:

```text
max relative Poisson residual <= 1e-10
max odd-z defect <= 1e-12
max relative recovered divergence <= 1e-10
max_t E(t)/E(0) <= 1 + 1e-5
max stepwise B_E <= 0.20.
```

The energy-balance row is explicitly a finite-box/numerical sanity check; passing it is not a continuum energy theorem.

## 8. M5 — integrator and resolution cross-check

At `T=2e-4`, compare RK4 and SSPRK3 on the same grid using the combined grid-Euclidean state norm of `(u1,omega1)` over the frozen core.

Acceptance:

```text
RK4 vs SSPRK3 relative state difference:
  h=.04 <= 2e-6
  h=.02 <= 2e-6.
```

For the two RK4 resolutions, inject the fine solution onto the aligned coarse grid and compare fields separately on the coarse core:

```text
relerr(u1_h04, restrict(u1_h02)) <= 2e-4
relerr(omega1_h04, restrict(omega1_h02)) <= 0.030.
```

These are short-time implementation cross-checks, not continuum convergence rates.

## 9. Decision

The machine-readable report must contain M1–M5 and all per-step/per-stage streamed extrema.

Only if every frozen condition passes:

```text
R3-W1-MANUFACTURED = PASS
```

Otherwise:

```text
R3-W1-MANUFACTURED = STOP_REPAIR_W1_MANUFACTURED.
```

A PASS permits designing the next candidate-time pilot, but it does not permit a blow-up fit or singularity claim. Before any late-time interpretation, the project still owes evolved-source whole-space tail control, independent spatial/integrator comparisons, explicit resolution-scale diagnostics, and eventually rigorous numerical error enclosure.
