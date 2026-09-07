# R3 W1 dynamic preflight — stability preregistration (2026-09-07)

**Status:** frozen preflight before any W1 growth output. **No amplification, singularity, regularity, or Clay claim.**

W0 has passed on its frozen static gate. W1 therefore opens only at the numerical-stability layer required by the standing Fable5 P0-A/B/C audit. This document freezes the first W1 task before any dynamic candidate run is inspected.

## 1. Integrator choice

The W1 primary explicit integrator is **classical RK4**. The required comparison integrator is **SSPRK3**. Heun/RK2 is retained only as a negative-control stability test and is not accepted as a sole production integrator for centered advection.

The stability polynomials are

```text
Heun:    R2(z)=1+z+z^2/2
SSPRK3:  R3(z)=1+z+z^2/2+z^3/6
RK4:     R4(z)=1+z+z^2/2+z^3/6+z^4/24.
```

## 2. Frozen-coefficient symbol

For centered first differences and centered second differences, the local frozen symbol is

```text
lambda(theta_r,theta_z)
 = -nu*[4 sin^2(theta_r/2)/dr^2 + 4 sin^2(theta_z/2)/dz^2]
   - i*[c_r_eff sin(theta_r)/dr + c_z sin(theta_z)/dz].
```

For interior `L5 = d_rr + (3/r)d_r + d_zz`, the frozen radial first-derivative contribution is included conservatively in

```text
c_r_eff = |u^r| + 3*nu/r_min,
r_min = dr.
```

The axis row itself uses the even-axis `4 d_rr + d_zz` stencil and is not represented by the interior Fourier symbol; the `3 nu / r_min` term is deliberately a conservative interior stress, not an exact axis spectral theorem.

The scan uses `theta_r,theta_z` on a uniform `1025 x 1025` grid over `[-pi,pi]^2`. For a proposed `dt`, a row is symbol-stable only if

```text
max |R(dt*lambda)| <= 1 + 1e-10.
```

The zero mode is allowed to attain exactly one.

## 3. Frozen manufactured stability rows

### S1 — negative control: pure centered advection

```text
c_r=1, c_z=0, nu=0,
dr=dz=0.05, dt=0.02.
```

Acceptance:

```text
Heun max amplification >= 1 + 1e-4
RK4  max amplification <= 1 + 1e-10
SSPRK3 max amplification <= 1 + 1e-10.
```

This must explicitly detect the known Heun instability rather than hiding it under viscosity.

### S2 — stable advection-diffusion row including radial L5 stress

```text
|u^r|=0.5, |u^z|=0.75,
nu=0.01,
dr=dz=0.025,
r_min=dr,
dt=0.001.
```

Acceptance: RK4 and SSPRK3 both satisfy the symbol-stability threshold.

### S3 — intentionally oversized step

Use the S2 coefficients with

```text
dt=0.03.
```

Acceptance: RK4 and SSPRK3 both violate the stability threshold by at least `1e-2`. This verifies that the detector fails closed on an unsafe explicit step.

## 4. Runtime contract for the later W1 evolution

No candidate growth is interpreted until the dynamic implementation records, for **every attempted step**:

- `dt_proposed`, `dt_accepted`, and whether target-time clipping occurred;
- `max|u^r|`, `max|u^z|` at the pre-state and every RK stage;
- advection CFL at the pre-state and every stage;
- explicit viscous stability number at the pre-state and every stage;
- frozen-symbol maximum amplification for the primary integrator at the pre-state and every stage;
- rejected-step count and rejection reason;
- finite-value checks;
- Poisson algebraic residual;
- physical energy and energy-balance defect;
- odd-z / axis-parity defects;
- reconstructed physical divergence;
- acceptance-critical streaming maxima/minima over all accepted steps, not only saved snapshots.

A proposed step whose RK4 symbol factor exceeds `1+1e-10` at the pre-state or any recomputed stage is rejected and retried with smaller `dt`. The comparison SSPRK3 run is required on the same physical datum and output targets; differences are reported rather than tuned away.

## 5. Claim boundary and next gate

Passing S1/S2/S3 only certifies that the stability detector behaves as preregistered. It does not validate the nonlinear PDE solver.

After this preflight passes, the next W1 subgate is a **short-time manufactured evolution** using the exact W0 identities

```text
partial_t omega1|_0 = partial_z(u1_0^2),
partial_t u1|_0 = nu L5 u1_0,
```

plus per-step P0-B/C diagnostics. No long-time amplification scan is opened before that manufactured short-time gate passes.
