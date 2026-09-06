# M-1 resolution rescue — E3c128 result (2026-09-06)

**Classification:** `NUMERICAL OBSERVATION / EVIDENCE-GRADE ONLY`.

This record preserves the preregistered `E3c128` whole-run resolution screen. It is a periodic `T^3` numerical result. It is not an `R^3` candidate, not a blow-up claim, and not a Clay A/B/C/D result.

## Revision-qualified execution

- PR: #100, `Numerics: screen fixed-continuum E3c128 refinement`;
- numerical PR head checked: `44c119292bd9c0ef0f37a8d97fd8a42487b8a267`;
- workflow: `M-1 E3c128 resolution screen`;
- run id: `34015004075`;
- job: `e3c128-screen`, id `101437192765`;
- runner: GitHub-hosted Ubuntu 24.04;
- Python: 3.12.14;
- NumPy: 2.5.2;
- SciPy: 1.18.1.

The fixed-continuum seed self-check passed before the production run.

## E3c128 result

Preregistered configuration:

```text
run = E3c128
N = 128
nu = 0.02
T = 3.5
dt = 1/160
whole-run spectral-tail tolerance = 1e-5
```

Observed summary:

```text
max_tail = 2.845872144398e-09
tail_tolerance = 1.000000000000e-05
tail_pass = True
finite_pass = True
max_relative_single_step_energy_growth = 0.000000000000e+00
walltime_s = 777.279
```

Therefore

```text
E3c128 WHOLE-RUN RESOLUTION SCREEN = PASS
```

at the preregistered fail-closed spectral-tail gate.

Artifact provenance:

- artifact name: `m1-E3c128-resolution-screen`;
- artifact id: `9983774115`;
- size: 2507 bytes;
- ZIP digest: `sha256:9f8dd8f4cb79f3d84cab81701b98d85189c3ae74f3b01d56b51788f44455fc8e`;
- created: `2026-09-06T06:04:55Z`.

## Consequence within the preregistered M-1 program

Together with the already qualified `E3c96`, this gives the first E3c same-continuum-datum pair for which both retained resolutions satisfy the whole-run tail gate:

```text
E3c96  PASS  max_tail = 3.274744131023e-07
E3c128 PASS  max_tail = 2.845872144398e-09
```

`E3c64` remains excluded (`max_tail = 5.956860730357e-05`).

This establishes **R0 eligibility of the 96/128 pair**, not yet refinement stability of the mechanism diagnostics. The next permitted work is the preregistered common-time comparison / `nearfar_rescue.py` execution on the two qualified E3c grids. No near/far result may use E3c64.

The broader M-1 GO rule is still unmet because it requires at least two genuinely different continuum data with tail-qualified, refinement-stable growth events and the same residual class carrying the positive surplus after near-field absorption. E1 currently has only `E1R96` qualified, and E4c/E2 rescue screens remain outstanding.

## Nonclaims

This result does **not** prove spatial convergence of the Navier--Stokes solution, universality of FAR/COMM/LOC residual dominance, a continuum theorem, an `R^3` transfer, finite-time singularity, global regularity, or any Clay statement.
