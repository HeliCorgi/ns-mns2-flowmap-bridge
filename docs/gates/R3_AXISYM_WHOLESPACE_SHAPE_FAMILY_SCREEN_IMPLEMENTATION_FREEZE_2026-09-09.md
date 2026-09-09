# R3 shape-family screen — implementation freeze

Date: 2026-09-09 JST

This file freezes implementation details before production output. Scientific thresholds and shapes are controlled by `R3_AXISYM_WHOLESPACE_SHAPE_FAMILY_SCREEN_PREREG_2026-09-09.md`.

## Reuse boundary

Reuse the merged W1 numerical kernels without changing their PDE signs or physical diagnostics:

- `manufactured_short_time.py` for centered spatial RHS, RK4, streaming stage/step diagnostics, physical energy/enstrophy;
- `green_quadrature_repair.py::DomainGridSolver` for arbitrary B22/B44 nonperiodic boxes;
- `dynamic_resolution_audit.py::state_rel_same_resolution` for common-core state comparison;
- `candidate_time_pilot.py` for physical-vorticity supremum and spline receiver recovery.

No Lean source changes are part of this gate.

## Parameter injection

Implement a `ShapeGridSolver(DomainGridSolver)` that overrides only `initial_state()` and stores frozen `(alpha,shape)` metadata. It must not change the evolution equations, Poisson operator, boundary closure, derivatives, RK4 stages, or runtime scanner.

Radial and axial profiles must be implemented literally from the preregistration. The annular factor is evaluated as a smooth function of `s=r^2`; do not replace it by a function of `r`.

## Run order

Run rows in deterministic order

```text
alpha 64, then 128;
within each alpha:
C-Z0, C-Z1, C-Z2, A-Z0, A-Z1, A-Z2;
within each row: B22 then B44.
```

Each box solver may be factorized once and reused sequentially across rows because only the initial datum changes.

## Output

Write one JSON artifact containing:

- frozen parameters and exact shape formulas;
- compact B22/B44 runtime summaries;
- physical diagnostics;
- domain metrics/checks;
- per-row classification;
- exact `promotion_set`;
- exact gate decision.

Default artifact path:

`experiments/r3_wholespace_w1/results/SHAPE_FAMILY_SCREEN.json`.

Exit code is zero for `PASS_WITH_PROMOTIONS` or `PASS_NO_PROMOTIONS`, nonzero for `STOP_REPAIR_SHAPE_SCREEN`.

## Fail-closed rule

Do not alter any parameter, formula, threshold, horizon, or grid after production output. If implementation plumbing fails before scientific output, repair only the plumbing while retaining this frozen scientific contract and document the failed attempt. If the scientific gate fails, record the STOP rather than loosening tolerances.
