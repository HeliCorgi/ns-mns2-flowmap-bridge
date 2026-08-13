# MNS-2 v2.13 — predictive grid/dt/physical-time lattice report

Date: 2026-08-13 JST

## Verdict

**`PREDICTIVE-CONVERGENCE-LATTICE-AUDIT-COMPLETE`** for the registered seven-case short-time synthetic finite-discrete lattice.

All fail-closed screening gates passed in GitHub Actions numerical run #16 on Python 3.12 / NumPy 2.5.2 / SciPy 1.18.0.

This result is deliberately weaker than a convergence theorem.  The grid axis records scalar diagnostics in changing discrete spaces; no common-space operator, tangent-subspace, or continuum convergence metric is supplied.  Therefore the allowed claim is:

> the v2.12 predictive tangent model survives the registered short-time grid/dt/time scalar robustness lattice under its finite-discrete scope.

The disallowed claim is:

> the predictive tangent operator or POD space has converged to a continuum Navier--Stokes object.

## Common configuration

Unless the axis explicitly changes it:

- synthetic analytic v2.2 regression seed; not Hou late-state evidence;
- viscosity `nu=5e-3`;
- fixed amplitude-training mesh
  `0.005,0.01,0.025,0.05,0.1,0.25,0.5,0.75,1.0`;
- rank-4 predictive POD coefficient model;
- 8 composite Gauss--4 panels for the lattice CI;
- one frozen LF/WENO schedule across all amplitudes in each case;
- fixed unnormalized radial path direction;
- certification nodes held out from coefficient training;
- residual integral reported both relative to the full endpoint and relative to the nonlinear correction.

## Grid axis

Fixed `dt=2e-8`, 2 SSPRK3 steps, physical time `T=4e-8`.

| grid | predictive endpoint rel. error | full tangent bridge rel. error | residual / endpoint | residual / nonlinear correction | direct endpoint norm |
|---|---:|---:|---:|---:|---:|
| `8x16` | `1.964622e-08` | `1.557930e-08` | `2.729097e-08` | `2.899339e-03` | `8.938270223555e-01` |
| `12x24` | `8.967550e-09` | `4.524034e-09` | `1.553865e-08` | `6.368027e-03` | `8.948215172977e-01` |
| `16x32` | `3.315717e-09` | `1.979491e-09` | `6.085717e-09` | `7.905978e-03` | `8.951087181225e-01` |

### Interpretation

The full-endpoint-normalized errors improve over these three grids.  However the metric that isolates the nonlinear correction moves in the opposite direction:

- `0.2899%` on `8x16`;
- `0.6368%` on `12x24`;
- `0.7906%` on `16x32`.

This is exactly why v2.13 carries FC-085.  The full endpoint is dominated by the zero-reference identity/Stokes-like tangent, so a decreasing endpoint-relative error does not by itself certify convergence of the nonlinear correction model.

The correct conclusion is therefore **mixed scalar evidence**, not predictor convergence.  A future cross-grid promotion must compare the actual represented tangent/correction object in a common embedding or restriction framework.

## Timestep axis

Fixed grid `12x24` and exact physical time `T=4e-8`.

| dt | steps | predictive endpoint rel. error | full tangent bridge rel. error | residual / endpoint | residual / nonlinear correction |
|---:|---:|---:|---:|---:|---:|
| `4e-8` | 1 | `8.967550e-09` | `4.524034e-09` | `1.553865e-08` | `6.368027e-03` |
| `2e-8` | 2 | `8.967550e-09` | `4.524034e-09` | `1.553865e-08` | `6.368027e-03` |
| `1e-8` | 4 | `8.967550e-09` | `4.524034e-09` | `1.553865e-08` | `6.368027e-03` |

All displayed diagnostics are identical at the printed precision.  This must **not** be described as exact timestep independence.  The physical window is only `4e-8`; the SSPRK3 timestep effect is unresolved at the current observable/error scale.  The allowed statement is simply that no dt dependence was resolved by this registered micro-window test.

The lattice checks `dt * steps = T` without silent step rounding.

## Physical-time robustness axis

Fixed grid `12x24`, fixed `dt=2e-8`.

| T | steps | predictive endpoint rel. error | full tangent bridge rel. error | residual / endpoint | residual / nonlinear correction | direct endpoint norm |
|---:|---:|---:|---:|---:|---:|---:|
| `2e-8` | 1 | `4.483834e-09` | `2.262029e-09` | `7.769437e-09` | `6.368087e-03` | `8.948217237535e-01` |
| `4e-8` | 2 | `8.967550e-09` | `4.524034e-09` | `1.553865e-08` | `6.368027e-03` | `8.948215172977e-01` |
| `8e-8` | 4 | `1.793463e-08` | `9.047967e-09` | `3.107641e-08` | `6.367907e-03` | `8.948211044099e-01` |

Over this extremely short window, endpoint/residual errors scale approximately linearly with physical time, while the residual relative to the nonlinear-correction norm stays essentially fixed near `0.6368%`.

This is consistent with a stable local predictive error fraction on the micro-window.  It is not evidence that the same structure persists into a strongly nonlinear or near-singular regime.

## What passed

Every registered case satisfied the screening gates:

- predictive endpoint relative error `< 2e-6`;
- integrated residual estimate / integrated true-correction norm `< 0.15`;
- numerical triangle ratio `<= 1.05`;
- certification nodes held out from training;
- common frozen schedule across amplitude comparisons;
- no silent timestep-to-physical-time rounding.

These thresholds are regression/promotion screens, not rigorous continuum error tolerances.

## Fail-closed interpretation

### FC-082 — scalar grid stability is not operator/subspace convergence

The grid table alone cannot compare POD vectors or tangent operators because their discrete spaces change with resolution.

### FC-083 — timestep and physical-time axes are distinct

The dt axis fixes `T`; the physical-time axis fixes `dt`.  Mixing these would make the observed change uninterpretable.

### FC-084 — no silent step rounding

Only exactly represented registered time triples are admitted.

### FC-085 — endpoint normalization can hide nonlinear-correction error

The correction-relative residual is mandatory and reveals a different grid trend from the full-endpoint error.

## What v2.13 does not establish

It does **not** establish:

- convergence of the Fréchet derivative as an operator across grids;
- convergence of the POD/projector subspace across grids;
- convergence of the discrete state map to a continuum Navier--Stokes flow map;
- a rigorous enclosure of the residual integral;
- robustness at Hou-like late times or amplitudes;
- fidelity to Hou's production wall-vorticity closure;
- finite-cylinder to Clay `R^3` / `T^3` transfer;
- a blow-up or Clay A/B/C/D result.

## Next numerical promotion gate

Do **not** extend the current short synthetic lattice merely to obtain more tiny endpoint-error digits.  The next meaningful numerical tasks are:

1. provide a common-space restriction/prolongation framework and compare correction/tangent subspaces or represented tangent fields across grids;
2. separately resolve the production wall-vorticity closure before any Hou-production / late-state study;
3. only then move to longer, more nonlinear windows with the same predictor/truth separation and residual accounting.

The continuum/Clay step remains theorem-level work and is not discharged by this lattice.
