# M-1 resolution rescue — run 2 result (2026-09-06)

**Classification:** `NUMERICAL OBSERVATION / EVIDENCE-GRADE ONLY`.

This record preserves the fixed-continuum `E3c` pair from the preregistered resolution-rescue ladder in `M1_RESOLUTION_RESCUE_PREREG_2026-09-06.md`. It is a periodic `T^3` numerical screen. It is not an `R^3` candidate, not a blow-up claim, and not a Clay A/B/C/D result.

## Revision-qualified execution

- PR: #99, `Numerics: screen fixed-continuum E3c resolution pair`;
- PR head: `795797d4d889702788867069e0eccddb55c5b948`;
- workflow: `M-1 E3c resolution pair`;
- run id: `34013942287`;
- runner: GitHub-hosted Ubuntu 24.04;
- Python: 3.12.14;
- NumPy: 2.5.2;
- SciPy: 1.18.1.

The exact fixed-continuum seed self-check passed before either production run. The workflow completed successfully as execution infrastructure. Scientific tail-gate results were reported separately from CI success.

## E3c64 result

Preregistered configuration:

- datum: resolution-invariant `ic_r4_continuum`;
- `N = 64`;
- `nu = 0.02`;
- `T = 3.5`;
- `dt = 1/80`;
- whole-run spectral-tail tolerance: `1e-5`.

Observed summary:

```text
max_tail = 5.956860730357e-05
tail_tolerance = 1.000000000000e-05
tail_pass = False
finite_pass = True
max_relative_single_step_energy_growth = 0.000000000000e+00
walltime_s = 43.010
```

Therefore

```text
E3c64 WHOLE-RUN RESOLUTION SCREEN = FAIL
```

at the preregistered spectral-tail gate.

Artifact provenance:

- artifact name: `m1-E3c64-resolution-screen`;
- artifact id: `9983329156`;
- ZIP digest: `sha256:1ed22f6775fbb347e367b665769e8bce1b83e5675da9575478183deee285758b`.

## E3c96 result

Preregistered configuration:

- datum: the same resolution-invariant `ic_r4_continuum` continuum field;
- `N = 96`;
- `nu = 0.02`;
- `T = 3.5`;
- `dt = 1/120`;
- whole-run spectral-tail tolerance: `1e-5`.

Observed summary:

```text
max_tail = 3.274744131023e-07
tail_tolerance = 1.000000000000e-05
tail_pass = True
finite_pass = True
max_relative_single_step_energy_growth = 0.000000000000e+00
walltime_s = 256.388
```

Therefore

```text
E3c96 WHOLE-RUN RESOLUTION SCREEN = PASS
```

at the preregistered spectral-tail gate.

Artifact provenance:

- artifact name: `m1-E3c96-resolution-screen`;
- artifact id: `9983371155`;
- ZIP digest: `sha256:c8775148c3a9d00614fd474561e14f592711efe799e09934382c8f495000815b`.

## Consequence within the preregistered M-1 program

The E3c pair does **not** yet establish a two-resolution qualified sequence because `E3c64` fails while `E3c96` passes. The preregistered ladder therefore advances to `E3c128` if E3c is to obtain two whole-run tail-qualified spatial resolutions.

`E3c96` is individually eligible for `nearfar_rescue.py`. `E3c64` is not and must not be used for the expensive near/far mechanism verdict. No E3c refinement-stability claim is available until `E3c128` is screened and, if qualified, compared with `E3c96` on common physical times.

The next focused numerical gate is therefore:

```text
E3c128 WHOLE-RUN RESOLUTION SCREEN
```

with the same fixed continuum datum and the preregistered `N = 128`, `dt = 1/160` configuration. The `1e-5` tail threshold is not changed.

## Nonclaims

These results do **not** prove spatial convergence of the Navier--Stokes solution, universality of FAR/COMM/LOC residual dominance, a continuum theorem, an `R^3` transfer, finite-time singularity, global regularity, or any Clay statement.
