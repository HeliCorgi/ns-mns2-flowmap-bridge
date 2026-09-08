# R3 W1 short-time manufactured nonlinear gate — result (2026-09-07)

**Status:** `STOP_REPAIR_W1_MANUFACTURED`. The frozen v1 gate failed. This record does not retroactively change any preregistered threshold.

## Execution provenance

```text
revision: c4a69fba0adf253c1c32c5aa4275cc4d1ab4bfdd
workflow: R3 W1 manufactured short-time gate
run: 34111861776
conclusion: failure
artifact: r3-w1-manufactured-short-time
artifact id: 10014663277
sha256:030daaae303071b742c223f895ea9480aed3d0becc1a4c317c75052be478424e
```

Frozen preregistration: `R3_AXISYM_WHOLESPACE_W1_MANUFACTURED_PREREG_2026-09-07.md`.

Machine decision:

```text
R3-W1-MANUFACTURED = STOP_REPAIR_W1_MANUFACTURED
```

## Passed rows

Every frozen check passed except the independently reconstructed physical-divergence threshold.

```text
M1 initial RHS relative errors
h=.04: u1=1.2668778207969671e-2, omega1=1.8570827548033384e-2
h=.02: u1=2.883010626216039e-3,  omega1=4.698892278680329e-3

M2 first-step secant relative errors
h=.04: u1=1.2680807472967607e-2, omega1=1.8588073157835335e-2
h=.02: u1=2.89448267501751e-3,   omega1=4.716761042930718e-3

M5 RK4-vs-SSPRK3 relative state difference
h=.04: 5.359304546183964e-16
h=.02: 5.410332231219124e-16

M5 resolution relative difference
u1:     4.872515088260401e-7
omega1: 1.3923586328098756e-2
```

All four runs completed the frozen eight steps with zero rejected steps. All states and stages were finite. The maximum frozen-symbol amplification was `1.0`; maximum Poisson residual was below `4.4e-14`; maximum odd-z defect was below `1.0e-14`; the physical-energy ratio stayed below one; and the maximum stepwise energy-balance defect was below `0.014`.

## Binding failure

The frozen M4 requirement was

```text
max relative recovered divergence <= 1e-10.
```

Observed maxima were

```text
h=.04 RK4/SSPRK3: about 1.030541016664716e-3
h=.02 RK4/SSPRK3: about 2.5434609153687554e-4
```

The fine/coarse ratio is approximately `0.2468083`, consistent with a second-order defect.

## Discrete diagnosis [DERIVED AFTER THE FAILED RUN]

This derivation explains the failure but does not alter the failed decision.

On a uniform interior radial grid let centered differences be `D_r,D_z`, let `q=D_z psi`, and reconstruct

```text
u_r = -r q,
u_z = 2 psi + r D_r psi.
```

Because `r_i` is linear in the grid index,

```text
D_r(r q)_i = r_i D_r q_i + (q_{i+1}+q_{i-1})/2.
```

Also centered `D_r` and `D_z` commute on the common interior stencil. Hence

```text
D_r u_r + u_r/r + D_z u_z
 = q_i - (q_{i+1}+q_{i-1})/2
 = -(h^2/2) D_rr q_i.
```

Therefore the continuum identity `div u=0` is not expected to cancel to roundoff when velocity is reconstructed and then independently differentiated with this stencil. The natural residual is `O(h^2)` away from boundaries/axis. The original `1e-10` target was an invalid acceptance quantity for this particular diagnostic.

This does **not** imply the nonlinear solver is validated. It identifies a diagnostic-design error that must itself be repaired and checked independently.

## Required repair before any v2 nonlinear gate

A separate preregistered repair gate must, before a new nonlinear production output is inspected:

1. test the algebraic discrete identity above on smooth manufactured streamfunctions;
2. verify second-order convergence of the independently differentiated divergence residual under at least three aligned grids;
3. separately retain a roundoff-level check for a discretely compatible divergence construction, if one is introduced;
4. preserve the distinction between continuum incompressibility, truncation error of an independent diagnostic, and algebraic discrete cancellation;
5. only after that repair passes, define a versioned W1 manufactured-v2 gate with a divergence condition derived from the validated diagnostic rather than by relaxing v1 post hoc.

PR #109 is intentionally closed unmerged as archival evidence of the fail-closed result.

## Nonclaims

No long-time amplification, singularity, regularity, continuum-convergence, or Clay A/B/C/D claim follows from this result.
