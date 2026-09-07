# R3 W1 early-time dynamic-domain / elliptic-boundary audit — preregistration (2026-09-07)

**Status:** frozen before production output. This gate follows `R3-W1-MANUFACTURED-V2 = PASS` and tests only early-time finite-box/domain sensitivity. It does not open a long-time growth scan and makes no singularity, regularity, continuum-convergence, or Clay A/B/C/D claim.

The reason for this gate is structural: W0 certified the static free-space elliptic path on compact manufactured sources, but viscous evolution immediately removes exact continuum compact support. Before interpreting any longer finite-box trajectory, separate the dynamic core sensitivity from the elliptic boundary error at a matched early time.

## 1. Frozen PDE, datum, integrator, grid, and horizon

Use exactly the manufactured-v2 physical/numerical datum and primary integrator:

```text
nu = 0.01
A = 0.16
R = Z = 1
alpha = 16
kappa = 1
integrator = classical RK4
h = 0.04
T = 2.0e-4
dt = 2.5e-5
```

Thus every dynamic row must complete exactly eight accepted steps.

Use the same centered finite-box normalized equations and axis treatment as manufactured-v2. No periodic-z/Fourier machinery is permitted.

The common physical comparison core is

```text
0 <= r <= 0.80
|z| <= 0.80.
```

## 2. Frozen independent domain set

Run the same physical datum on exactly these six nonperiodic boxes:

```text
B22 = (Rmax,Zmax) = (2,2)
B32 = (3,2)
B42 = (4,2)
B23 = (2,3)
B24 = (2,4)
B44 = (4,4)
```

The radial sequence `B22 -> B32 -> B42` varies only `Rmax`.
The axial sequence `B22 -> B23 -> B24` varies only `Zmax`.
`B44` is the full large-box reference row.

All grids are aligned at `h=.04`; no interpolation is needed for common-core state comparisons or restriction of the B44 source to smaller boxes.

## 3. A0 — inherited per-stage / all-step sanity checks

For every dynamic box run require the same manufactured-v2 runtime conditions:

```text
completed steps = 8
rejected steps = 0
all stage/state values finite
max frozen-symbol amplification <= 1 + 1e-10
max CFL <= 0.10
max viscous number <= 0.05
max relative Poisson residual <= 1e-10
max odd-z defect <= 1e-12
max_t E(t)/E(0) <= 1 + 1e-5
max stepwise energy-balance defect <= 0.20.
```

The repaired divergence diagnostic remains recorded but is not the load-bearing quantity in this domain gate; manufactured-v2 already certified its finite-discrete behavior.

## 4. A1 — dynamic common-core domain sensitivity

At `T=2e-4`, compare the combined grid-Euclidean `(u1,omega1)` state on the common core. For two aligned boxes `X,Y`, define

```text
D_state(X,Y) = ||state_X-state_Y||_2 / max(||state_Y||_2,1e-30).
```

Freeze the following radial increments:

```text
dR_23 = D_state(B22,B32)
dR_34 = D_state(B32,B42)
```

and axial increments:

```text
dZ_23 = D_state(B22,B23)
dZ_34 = D_state(B23,B24).
```

Acceptance is fail-closed but allows a predeclared numerical-negligibility floor:

```text
radial:
  either max(dR_23,dR_34) <= 1e-10
  or dR_34 <= 0.50*dR_23

axial:
  either max(dZ_23,dZ_34) <= 1e-10
  or dZ_34 <= 0.50*dZ_23.
```

The `1e-10` floor is frozen before output because a local explicit stencil can make early-time state sensitivity smaller than floating/discrete diagnostic scales; it is not a continuum error bound.

Also record, descriptively only,

```text
D_state(B42,B44)
D_state(B24,B44).
```

These diagnose the still-unexpanded orthogonal direction.

## 5. A2 — common evolved source for the elliptic audit

Use **only** the final B44 RK4 `omega1(T)` as the common source for the elliptic-boundary test. Restrict that same aligned array to B22/B32/B42/B23/B24. Do not use each box's separately evolved `omega1` in A3/A4; this isolates the Poisson boundary effect from dynamic state differences.

Before accepting this common-source construction, measure the lifted weighted source outside the smallest B22 box:

```text
M_out/M_total =
  integral_{(r>2) or (|z|>2)} r^3 |omega1_B44| dr dz
  / integral r^3 |omega1_B44| dr dz.
```

Require

```text
M_out/M_total <= 1e-12.
```

Also require the normalized lifted odd monopole

```text
|integral r^3 omega1_B44 dr dz| /
 integral r^3 |omega1_B44| dr dz <= 1e-12.
```

These are numerical source-containment/symmetry checks, not evolved continuum tail theorems.

## 6. Frozen free-space Green receiver set

Use the same four receiver locations as W0, all aligned to `h=.04` and lying in the common core:

```text
(0.12,  0.00)
(0.24,  0.20)
(0.28, -0.24)
(0.20,  0.32).
```

For the common B44 source, evaluate the free-space reduced five-dimensional Green integral

```text
psi(r,z) = (1/(2*pi)) integral rho^3 omega1(rho,zeta)
           [ integral_0^pi sin(theta)^2 / D^(3/2) dtheta ] drho dzeta,

D = r^2 + rho^2 - 2 r rho cos(theta) + (z-zeta)^2,
```

and the differentiated kernels

```text
partial_r D^(-3/2) = -3 (r-rho cos(theta)) D^(-5/2)
partial_z D^(-3/2) = -3 (z-zeta) D^(-5/2).
```

This is an independent elliptic inversion of the evolved numerical source; it is not a second time integrator.

## 7. A3 — Green quadrature self-check

Interpolate the common B44 grid source with a cubic tensor spline in `(rho,zeta)` and integrate over the full B44 source box.

Freeze two quadrature levels:

```text
Qlow:
  source midpoint spacing = 0.04
  theta Gauss-Legendre order = 48

Qhigh:
  source midpoint spacing = 0.02
  theta Gauss-Legendre order = 80.
```

At the four receivers compare the combined 12-component vector

```text
(psi, partial_r psi, partial_z psi).
```

Require

```text
||Qhigh-Qlow||_2 / max(||Qhigh||_2,1e-30) <= 2e-3.
```

If this fails, the gate stops at `REPAIR_GREEN_QUADRATURE`; no finite-box/Green conclusion may be promoted.

## 8. A4 — same-source finite-box elliptic boundary sensitivity

For each box B22/B32/B42/B23/B24/B44, solve

```text
-L5 psi = restricted common B44 omega1(T)
```

with the same homogeneous finite-box boundary closure used by the dynamic solver. At the fixed receivers extract

```text
(psi, centered partial_r psi, centered partial_z psi)
```

and compute relative receiver error against Qhigh:

```text
E_box(B) = ||receiver_B-Qhigh||_2 / max(||Qhigh||_2,1e-30).
```

Require strict independent improvement:

```text
radial sequence:
  E_box(B32) < E_box(B22)
  E_box(B42) < E_box(B32)

axial sequence:
  E_box(B23) < E_box(B22)
  E_box(B24) < E_box(B23)

full large box:
  E_box(B44) <= min(E_box(B42), E_box(B24)).
```

No absolute Green-error threshold is imposed in this gate. The purpose is to test the direction and separability of domain sensitivity before a later accuracy-enclosure gate; adding an absolute threshold after output is forbidden.

Also record adjacent receiver changes `||receiver_mid-receiver_small||` and `||receiver_large-receiver_mid||` descriptively.

## 9. Decision

Only if A0–A4 all pass under the frozen rules:

```text
R3-W1-DYNAMIC-DOMAIN-AUDIT = PASS.
```

If the Green self-check fails:

```text
R3-W1-DYNAMIC-DOMAIN-AUDIT = STOP_REPAIR_GREEN_QUADRATURE.
```

Any other failure gives

```text
R3-W1-DYNAMIC-DOMAIN-AUDIT = STOP_REPAIR_DYNAMIC_DOMAIN.
```

A PASS allows preregistering a longer candidate-time pilot. It does **not** certify a whole-space continuum trajectory: the common source is still a finite-discrete early-time source, and no analytic/interval enclosure of the true evolved tail has been supplied.

## 10. Nonclaims / forbidden rescue

Do not after output:

- change the six boxes or compare only a favorable direction;
- switch receiver locations;
- change `h`, `dt`, `T`, `A`, `nu`, or the integrator;
- replace the common B44 source with a favorable per-box source in A4;
- loosen the Green self-check or the dynamic refinement rules;
- treat a PASS as continuum `R^3` convergence, blow-up evidence, or a Clay result.
