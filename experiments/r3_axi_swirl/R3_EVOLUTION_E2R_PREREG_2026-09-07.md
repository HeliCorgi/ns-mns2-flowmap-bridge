# R3 axisymmetric-with-swirl evolution E2R preregistration — 2026-09-07

**Classification:** `NUMERICAL CANDIDATE INFRASTRUCTURE / BOUNDED RESOLUTION-DOMAIN RESCUE`.

This document freezes one bounded rescue after the first E2 lattice failed its preregistered
spatial/asymptotic and radial-domain qualification gates. It does **not** alter the failed E2
verdict. It asks whether the same continuum datum and the same numerical method enter a qualified
regime on a larger artificial box and finer mesh.

No E2 threshold, field, norm, physical time, continuum datum, equation, integrator, or common
comparison region is relaxed or deleted.

## Fixed physical/numerical problem

```text
seed          R3S04
nu            0.002
T             0.02
integrator    SSPRK3
space         centered second-order node finite differences
elliptic      factorized second-order -L5 solve
z topology    strictly nonperiodic
outer BC      zero artificial Dirichlet
CFL limit     0.40
viscous limit 0.80
float         float64
```

The rescue changes only the artificial box and mesh ladder. The continuum datum remains the same
explicit `C_c^infty` datum.

## Frozen base box and spatial ladder

Use the larger base artificial box

```text
(Rmax,Zmax) = (1.0,0.9)
```

and the three-grid equal-spacing ladder

```text
name   nr   nz   dr=dz            dt_cap
B160   160  288  0.00625          0.001
B200   200  360  0.005            0.001
B240   240  432  0.004166666667   0.001
```

This is strictly finer than the original E2 base ladder at the fine end, and the base artificial
boundaries are farther from the compact datum and fixed comparison core.

## Frozen highest-grid time refinement

Run

```text
B240H  nr=240 nz=432 Rmax=1.0 Zmax=0.9 dt_cap=0.00015
```

The normal B240 accepted step is determined by the unchanged fail-closed step selector. The time
gate below requires the executed B240H maximum accepted step to be at most `0.51` times B240's
maximum accepted step, regardless of the expected limiter value.

## Frozen one-coordinate domain enlargement

At exactly the B200 physical mesh spacing `dr=dz=0.005`, run

```text
name    Rmax  Zmax  nr   nz
RPLUS2  1.2   0.9   240  360
ZPLUS2  1.0   1.1   200  440
```

No square-box replacement and no further domain enlargement may be selected after seeing E2R.

## Common physical comparison grid

Keep exactly the original E2 comparison core and grid:

\[
0\le r\le0.55,\qquad |z|\le0.45,
\]

with `65 x 97` common physical points and linear interpolation.

Compare exactly the same fields:

```text
u1, omega1,
ur, uz, utheta,
u1_r, u1_z, omega1_r, omega1_z,
ur_r, ur_z, uz_r, uz_z, utheta_r, utheta_z.
```

For every field record the same relative `Linf` and physical `2*pi*r dr dz` weighted-L2 metrics
used by E2.

## Inherited E1 gates

Every E2R run must independently satisfy exactly the original inherited E1 gates:

```text
accepted steps                                  > 0
rejected steps                                  <= 20
minimum dt                                      >= 1e-8
all pre/stage/post CFL                          <= 0.40
all viscous numbers                             <= 0.80
max positive one-step relative energy increase <= 1e-4
relative Gamma sup overshoot                    <= 1e-3
axis regularity defect                          <= 1e-12
relative physical-divergence Linf defect        <= 1e-2
elliptic algebraic residual Linf                <= 1e-8
minimum gradient scale                          >= 1 grid point
outer boundary-shell ratio                      <= 1e-6
curvature-tail diagnostic                       finite
```

## Frozen E2R decision rule

`R3-E2R-SAME-DATUM-CONVERGENCE = PASS` only if all conditions below hold.

### Spatial ladder

For every listed field and both relative norms,

```text
D(B200,B240) < D(B160,B200).
```

Also require

```text
min_gradient_scale_points(B160)
  < min_gradient_scale_points(B200)
  < min_gradient_scale_points(B240),

min_gradient_scale_points(B240) >= 2.0,

max_curvature_tail(B160)
  > max_curvature_tail(B200)
  > max_curvature_tail(B240),

max_curvature_tail(B240) <= 1.0.
```

These are the same qualification thresholds used by E2.

### Time refinement

Require

```text
max_dt(B240H) <= 0.51 * max_dt(B240)
```

and, for every field and both norms,

```text
D(B240,B240H) <= D(B200,B240).
```

### Artificial-domain sensitivity

At the identical B200 mesh spacing require, for every field and both norms,

```text
D(B200,RPLUS2) <= 1e-3,
D(B200,ZPLUS2) <= 1e-3.
```

The `1e-3` threshold is unchanged from E2. This remains a numerical truncation-sensitivity test,
not a rigorous tail enclosure.

### Save/reload provenance

Save all six final `(u1,omega1)` states to one NPZ, reload with exact `np.array_equal`, record
SHA-256, exact configurations, Python/NumPy/SciPy versions through hosted logs, and upload the
summary plus NPZ artifact even on scientific FAIL.

## Bounded stop rule

If any condition fails, report the exact failures and set

```text
R3-E2R-SAME-DATUM-CONVERGENCE = FAIL
R3S04-CENTERED-FD-ZERO-BC-STACK = PARK
```

Do not add a third rescue lattice, loosen the thresholds, delete fields, shorten/extend `T`, or
change the common grid after seeing E2R. A future continuation would require a genuinely new
numerical-method contract or a separately preregistered continuum datum, not another unbounded
resolution escalation.

If E2R passes, it only licenses a separately preregistered bounded multi-seed screen on the same
qualified numerical stack. It is not a blow-up or continuum theorem.

## Nonclaims

Neither PASS nor FAIL establishes finite-time singularity, global regularity, or any Clay A/B/C/D
statement.
