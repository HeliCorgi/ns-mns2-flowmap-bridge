# R3 alternate-datum R3S02 qualification preregistration — 2026-09-07

**Classification:** `NUMERICAL CANDIDATE INFRASTRUCTURE / SINGLE ALTERNATE DATUM QUALIFICATION`.

The bounded `R3S04` E2R rescue failed its frozen narrow-scale/curvature qualification and therefore
parks `R3S04 + centered-FD + zero-Dirichlet`. This document opens exactly one allowed
alternate-continuum-datum qualification under the unchanged numerical method.

This is **not** a multi-seed screen. The datum is selected before any `R3S02` Navier--Stokes
evolution is executed.

## Fixed datum and selection rationale

Use frozen lattice datum

```text
name  R3S02
index 2
s0    0.04
ws    0.05
wz    0.28
zu    0.00
Au    1.0
Apsi  0.10
```

The choice is based only on the already-published continuum geometry in `compact_family.py`, not
on an unseen evolution result: among the unshifted frozen seeds, `R3S02` combines the smallest
radial center `s0=0.04` with the widest axial support `wz=0.28`, making it the least steep radial/
axial geometry in the current lattice while keeping the exact same bump formulas and amplitudes.

No other seed may replace R3S02 after execution.

## Unchanged physical/numerical problem

```text
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

The finite boxes remain artificial truncations of the `R^3` target.

## Datum-specific elliptic preflight A0

Before any R3S02 evolution, recover the exact compact `psi1` from its analytically derived
`omega1=-L5 psi1` on the frozen base-box spatial ladder below. Zero outer Dirichlet data are exact
for the manufactured compact `psi1` because its support lies strictly inside every box.

For `B160/B200/B240`, record field `Linf`, physical weighted-L2, first-derivative errors, and
algebraic residual. Require every field/derivative error metric to decrease strictly across the
three grids and require on B240

```text
psi Linf                 < 1e-3
psi physical weighted L2 < 1e-4
algebraic residual Linf  < 1e-9
```

These are the same prototype absolute field thresholds already used for compact E0 recovery; they
are not selected from R3S02 output.

If A0 fails, no evolution result can rescue the datum.

## Frozen evolution lattice

Reuse exactly the already-preregistered E2R base box and mesh family, changing only
`seed_index: 4 -> 2`:

```text
base box (Rmax,Zmax)=(1.0,0.9)

B160   160 x 288   h=0.00625          dt_cap=0.001
B200   200 x 360   h=0.005            dt_cap=0.001
B240   240 x 432   h=0.004166666667   dt_cap=0.001
B240H  240 x 432                       dt_cap=0.00015

RPLUS2 (Rmax,Zmax)=(1.2,0.9)  240 x 360  h=0.005
ZPLUS2 (Rmax,Zmax)=(1.0,1.1)  200 x 440  h=0.005
```

## Common comparison and fields

Keep exactly

\[
0\le r\le0.55,\qquad |z|\le0.45
\]

on the same `65 x 97` common physical grid, with the same 15 fields and relative `Linf` / physical
weighted-L2 definitions used by E2/E2R:

```text
u1, omega1,
ur, uz, utheta,
u1_r, u1_z, omega1_r, omega1_z,
ur_r, ur_z, uz_r, uz_z, utheta_r, utheta_z.
```

## Evolution decision rule

Every run must pass all inherited E1 gates. In addition require, unchanged from E2R:

### Spatial

For every field and both norms,

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

### Time

Require

```text
max_dt(B240H) <= 0.51 * max_dt(B240)
```

and every B240/B240H field discrepancy must be no larger than the corresponding B200/B240
spatial discrepancy.

### Domain

At equal B200 spacing require for every field and both norms

```text
D(B200,RPLUS2) <= 1e-3,
D(B200,ZPLUS2) <= 1e-3.
```

### Save/reload

Save all six final `(u1,omega1)` states, require exact `np.array_equal` reload, record NPZ SHA-256,
and upload summary plus NPZ even on scientific FAIL.

## Bounded decision / no seed shopping

PASS requires A0 and every evolution condition:

```text
R3S02-ALT-DATUM-QUALIFICATION = PASS
```

A PASS only licenses a separately preregistered bounded family screen; each eventual surviving
candidate still needs its own refinement evidence before any growth claim.

If R3S02 fails, set

```text
R3S02-ALT-DATUM-QUALIFICATION = FAIL
CURRENT-12-SEED-CENTERED-FD-QUALIFICATION-PATH = PARK
```

and do **not** try R3S00/R3S06/etc. one by one. The next continuation must change the numerical
method under a new manufactured-test contract, rather than shop the existing seed lattice for a
passing datum.

## Nonclaims

This qualification concerns finite-resolution numerical behavior only. It proves neither
continuum convergence, finite-time singularity, global regularity, nor any Clay A/B/C/D statement.
