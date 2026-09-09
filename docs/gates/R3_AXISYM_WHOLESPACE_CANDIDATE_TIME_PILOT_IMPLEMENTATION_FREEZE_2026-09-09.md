# R3 candidate-time pilot — implementation freeze

Date: 2026-09-09 JST

This note is committed **before any candidate-time production output** and only fixes implementation details left implicit in the main pilot preregistration.

## Receiver evaluation

The pilot retains the four physical receiver coordinates frozen in the preregistration, including on the `h=.08` level where those coordinates are not all grid nodes.

For every run, after the final finite-box solve `-L5 psi1 = omega1`, construct the same exact interpolant class on that run's native `(r,z)` grid:

```text
RectBivariateSpline(r, z, psi1, kx=3, ky=3, s=0)
```

and evaluate at each receiver

```text
psi1      = spline.ev(rp,zp)
partial_r = spline.ev(rp,zp,dx=1,dy=0)
partial_z = spline.ev(rp,zp,dx=0,dy=1)

u^r = -rp partial_z
u^z = 2 psi1 + rp partial_r.
```

Thus C2/C3/C4 compare the same physical receiver coordinates across all grids; no nearest-node substitution is allowed.

## State restriction

Three-level state comparisons use exact nested-grid restriction on the common core. For `h=.08 -> .04 -> .02`, the grids are nested by integer stride two.

## Global constants in the inherited RK4 driver

The inherited W1 RK4 driver reads `T_FINAL` and `DT` as module globals. The pilot executes runs sequentially and sets those globals to the preregistered `(T,dt)` pair immediately before each run. The PDE, spatial stencil, stability scanner, stage logic, rejection rule, and diagnostics are otherwise unchanged.

This technical mechanism is not permission to alter `Tpilot`, `dt`, thresholds, boxes, or the candidate datum after output inspection.
