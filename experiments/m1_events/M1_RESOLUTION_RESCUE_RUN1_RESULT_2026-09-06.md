# M-1 resolution rescue — run 1 result (2026-09-06)

**Classification:** `NUMERICAL OBSERVATION / EVIDENCE-GRADE ONLY`.

This record preserves the first executed result from the preregistered resolution-rescue ladder in `M1_RESOLUTION_RESCUE_PREREG_2026-09-06.md`. It is a periodic `T^3` numerical screen. It is not an `R^3` candidate, not a blow-up claim, and not a Clay A/B/C/D result.

## Revision-qualified execution

- PR: #98, `Numerics: run first M1 resolution rescue screen`;
- PR head: `99541d2202c9394926b46a82dda991a892f0f4e5`;
- workflow: `M-1 resolution rescue`;
- run id: `34005553913`;
- runner: GitHub-hosted Ubuntu 24.04;
- Python: 3.12.14;
- NumPy: 2.5.2;
- SciPy: 1.18.1.

The exact repository seed self-check completed successfully:

```text
PASS shared=0.000e+00 coeff_norm_delta=4.441e-16
```

The `E1R96` screen then completed successfully as a computation. The scientific resolution gate was evaluated separately from CI success.

## E1R96 result

Preregistered configuration:

- datum: analytic Taylor--Green;
- `N = 96`;
- `nu = 0.01`;
- `T = 8`;
- `dt = 1/150`;
- RK4 accepted steps: 1200;
- whole-run spectral-tail tolerance: `1e-5`.

Observed run summary:

```text
max_tail = 6.086987397920e-07
tail_tolerance = 1.000000000000e-05
tail_pass = True
finite_pass = True
max_relative_single_step_energy_growth = 0.000000000000e+00
walltime_s = 519.108
```

Therefore

```text
E1R96 WHOLE-RUN RESOLUTION SCREEN = PASS
```

at the preregistered `1e-5` spectral-tail gate.

Artifact provenance:

- artifact name: `m1-e1r96-resolution-screen`;
- artifact id: `9980926946`;
- size: 4986 bytes;
- artifact ZIP digest: `sha256:d15de290da07776781a36a2337723899d0703b7ee01873d0a370bd559dd03c53`;
- created: `2026-09-06T02:14:38Z`.

## Consequence within the preregistered M-1 program

`E1R96` is now eligible for `nearfar_rescue.py`, because both `tail_pass` and `finite_pass` are true. This only establishes eligibility of one periodic fixed datum. It does not establish cross-datum reproducibility or refinement stability.

The next preregistered R0 step is the fixed-continuum `E3c` pair:

1. `E3c64`;
2. `E3c96`.

Only after a run passes its whole-run screen may the expensive Yu-structured near/far diagnostic be run on that run. Mechanism promotion still requires at least two genuinely different continuum data with tail-qualified, refinement-stable growth events and the same residual class after near-field absorption.

## Nonclaims

This result does **not** prove numerical convergence of the PDE solution, a continuum theorem, universality of the historical FAR residual pattern, finite-time singularity, global regularity, or any Clay statement. The periodic computation remains diagnostic-only until the later preregistered spatial/time refinement and mechanism-comparison gates are satisfied.
