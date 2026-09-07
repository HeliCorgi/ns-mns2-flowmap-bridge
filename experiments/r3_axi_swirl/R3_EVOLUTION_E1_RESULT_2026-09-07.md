# R3 axisymmetric-with-swirl evolution E1 result — 2026-09-07

**Classification:** `NUMERICAL CANDIDATE INFRASTRUCTURE / E1 PROTOTYPE ONLY`.

This result is the first short nonlinear time-integration smoke for the `SPEC.md` whole-space
axisymmetric-with-swirl track. It is a truncated-box finite-difference computation, not a
resolved `R^3` trajectory and not a singularity search result.

## Exact execution provenance

Preregistration: `R3_EVOLUTION_E1_PREREG_2026-09-07.md`.

Hosted workflow:

```text
name       R3 axisymmetric swirl nonlinear E1
run        34075898846
job        101601815270
head       dd8b06af0837b40eb221b7a54bb22b5211d76f1a
conclusion SUCCESS
runner     Ubuntu 24.04
Python     3.12.14
NumPy      2.5.3
SciPy      1.18.1
```

Result artifact:

```text
id      10002018444
name    r3-axisym-swirl-e1-results
digest  sha256:9de007fd3ecbc15c385fb47d33e40462bda548986de087dc9d9e1072a03db0a2
```

The workflow reran S0, the completed nonperiodic E0 suite, and the low-axial-frequency E0 stress
as fail-closed prerequisites. All passed before E1 executed.

## Frozen smoke case

```text
seed       R3S04
nu         0.002
T          0.02
Rmax       0.8
Zmax       0.7
nr         96
nz         168
dt_cap     0.001
integrator SSPRK3
z          strictly nonperiodic
outer BC   zero artificial Dirichlet
```

The discrete equations are exactly the normalized `SPEC.md` signs used in the preregistration.
The outer boundary is only a finite-box approximation and is not certified as a free-space
boundary condition.

## Fail-closed result

The preregistered sampled SSPRK3 frozen linear stability rectangle had

```text
max |R(-a+ib)| = 1.000000000000e+00
PASS
```

for `0<=a<=0.80`, `|b|<=0.40` on the declared `401 x 401` sample. This is only a sampled linear
cross-check, not a nonlinear stability theorem.

The nonlinear hosted run produced:

```text
accepted_steps                                      20
rejected_steps                                       0
min_dt                           9.999999999999905e-04
max_cfl_pre                      7.843699181762567e-02
max_cfl_stage1                   7.724334938692544e-02
max_cfl_stage2                   7.785285150158727e-02
max_cfl_post                     7.726816554143712e-02
max_viscous_number               5.760000000000001e-01
max positive one-step dE/E        0.0
Gamma max-principle overshoot     0.0
max axis regularity defect        0.0
max relative divergence Linf      2.404239402803843e-03
max elliptic residual Linf        1.104893954106956e-12
min gradient scale [grid points]  1.428770392265728
max curvature-tail diagnostic     1.930980036004977
max outer-shell ratio             2.020216560605260e-77
```

Every declared E1 acceptance condition therefore passed.

The kinetic energy decreased from

```text
2.486614120691731e-03
```

to

```text
2.193939492385651e-03
```

on this short run. The circulation supremum also decreased from about
`9.594997287183739e-02` to `9.375192631499503e-02`. These are descriptive observations; they
are not promotion criteria and do not imply regularity.

The maximum normalized swirl scalar increased only slightly from `1.0` to
`1.0023402964745545`, while the sampled maximum `omega1` decreased from about `155.25` to
`60.41`. Thus this smoke interval is not itself a growth event.

## Resolution warning carried forward

Two diagnostics deliberately prevent overpromotion:

```text
minimum gradient scale = 1.43 grid points
maximum curvature-tail diagnostic = 1.93
```

The E1 gate only required the former to exceed one grid point and the latter to remain finite.
Those are intentionally weak smoke conditions. They are **not** evidence that the state is
spatially resolved. In particular, `1.43` points is too close to grid scale for any candidate
claim. The exact purpose of E2 is to determine whether the same continuum datum stabilizes under
spatial, temporal, and domain refinement.

## Decision

```text
R3-E1-S0-PREFLIGHT = PASS
R3-E1-E0-PREFLIGHT = PASS
R3-E1-LOW-AXIAL-FREQUENCY-PREFLIGHT = PASS
R3-E1-NONLINEAR-INTEGRATOR-SMOKE = PASS
R3-E1-RESOLVED-R3-TRAJECTORY = NOT ESTABLISHED
R3-E1-GROWTH-CANDIDATE = NO CLAIM
R3-FREE-SPACE-TRUNCATION-CERTIFICATE = NOT DONE
```

The next gate is the preregistered E2 same-continuum-datum convergence lattice, including three
spatial resolutions, highest-grid `dt/2`, one-coordinate-at-a-time domain enlargement, and common
physical-coordinate comparisons of `u1`, `omega1`, velocity, and first derivatives.

## Nonclaims

This result does not prove a continuum-converged Navier--Stokes trajectory, finite-time
singularity, nonextendability, global regularity, or Clay A/B/C/D.
