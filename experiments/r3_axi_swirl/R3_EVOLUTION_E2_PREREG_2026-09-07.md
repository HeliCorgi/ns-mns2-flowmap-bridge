# R3 axisymmetric-with-swirl evolution E2 preregistration — 2026-09-07

**Classification:** `NUMERICAL CANDIDATE INFRASTRUCTURE / PRE-EXECUTION CONTRACT`.

E2 tests whether the short E1 trajectory for the **same continuum datum** stabilizes under
spatial, temporal, and artificial-domain refinement. It is frozen before any E2 trajectory is
executed. E2 does not search the 12-seed family and does not fit a blow-up time or exponent.

## Fixed physical problem for E2

All runs use the same explicit continuum datum and physical parameters:

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
```

The zero outer boundary remains an artificial truncation. E2 only measures sensitivity to it;
no rigorous free-space tail enclosure is claimed.

## Frozen run lattice

Base spatial ladder on `(Rmax,Zmax)=(0.8,0.7)`:

```text
name   nr   nz   dr=dz          dt_cap
S96     96  168  0.0083333333   0.001
S128   128  224  0.00625        0.001
S160   160  280  0.005          0.001
```

Highest-grid time-refinement run:

```text
S160H  160  280  0.005          0.000225
```

The normal S160 run is expected from the already-frozen explicit diffusion limiter to take steps
near `0.00045`; the `0.000225` cap is therefore fixed in advance to force an actual approximately
factor-two time refinement. The executed step sizes, not this expectation, decide the time-ratio
gate below.

One-coordinate-at-a-time artificial-domain enlargement at the **same grid spacing as S128**:

```text
name    Rmax  Zmax  nr   nz   dr=dz
RPLUS   1.0   0.7   160  224  0.00625
ZPLUS   0.8   0.9   128  288  0.00625
```

No square-box enlargement may replace these two tests post hoc.

## Common physical comparison grid

All final-state comparisons are interpolated with linear interpolation onto the fixed interior
rectangle

\[
0\le r\le0.55,\qquad |z|\le0.45,
\]

using a `65 x 97` common physical grid. This lies strictly inside every E2 box.

Compare all of the following fields:

```text
u1, omega1,
ur, uz, utheta,
u1_r, u1_z, omega1_r, omega1_z,
ur_r, ur_z, uz_r, uz_z, utheta_r, utheta_z.
```

For every field `f`, record both

```text
relative Linf = ||fa-fb||_inf / max(||fa||_inf,||fb||_inf,1e-14)
relative L2   = ||fa-fb||_(2*pi*r dr dz) / max(||fa||_weightedL2,||fb||_weightedL2,1e-14)
```

on the common grid. These are numerical comparison diagnostics, not rigorous error bounds.

## All-run E1 inheritance

Every E2 run must independently satisfy the already-preregistered E1 streaming gates:

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

No E2 comparison may rescue a run that fails its inherited E1 gate.

## Preregistered E2 decision rule

`R3-E2-SAME-DATUM-CONVERGENCE = PASS` only if **all** conditions below hold.

### Spatial ladder

For every listed comparison field and for both relative norms,

```text
D(S128,S160) < D(S96,S128).
```

Additionally the all-step resolution diagnostics must satisfy

```text
min_gradient_scale_points(S96)
  < min_gradient_scale_points(S128)
  < min_gradient_scale_points(S160),

min_gradient_scale_points(S160) >= 2.0,

max_curvature_tail(S96)
  > max_curvature_tail(S128)
  > max_curvature_tail(S160),

max_curvature_tail(S160) <= 1.0.
```

The `2.0`-point and `1.0` curvature-tail thresholds are qualification thresholds for this short
E2 lattice only. They do not certify a production singularity computation as resolved.

### Time refinement

The executed S160H maximum accepted time step must obey

```text
max_dt(S160H) <= 0.51 * max_dt(S160).
```

For every listed field and both relative norms,

```text
D(S160,S160H) <= D(S128,S160).
```

Thus the highest-grid time-discretization change must be no larger than the remaining fine spatial
change on the same comparison metric.

### Artificial-domain refinement

Because S128, RPLUS, and ZPLUS have identical grid spacing, require for every listed field and
both relative norms

```text
D(S128,RPLUS) <= 1e-3,
D(S128,ZPLUS) <= 1e-3.
```

This is a short-time numerical truncation-sensitivity threshold only; it is not a whole-space tail
proof.

### Save/reload provenance

The driver must save all six final `(u1,omega1)` states to one NPZ artifact, reload it in the same
job, and require exact `np.array_equal` reproduction of every stored array. It must record SHA-256
of that NPZ and the exact run configuration. The arithmetic precision for this E2 gate is
`float64`; no higher-precision equivalence is claimed.

## Stop rule

If any condition above fails, report the exact failing field/norm/run and stop at

```text
R3-E2-SAME-DATUM-CONVERGENCE = FAIL
```

without relaxing a threshold, deleting a comparison field, changing the common grid, extending
`T`, or selecting a different seed after seeing the output. Repairing a demonstrable code defect
is permitted only with a new revision and explicit rerun provenance.

If E2 passes, the next stage is **not** a blow-up claim. It only licenses a separately
preregistered bounded multi-seed screen on the same numerical stack.

## Nonclaims

Passing E2 does not establish continuum convergence, rigorous free-space truncation control,
finite-time singularity, nonextendability, global regularity, or Clay A/B/C/D.
