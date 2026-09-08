# R3 W1 short-time manufactured nonlinear gate v2 — result (2026-09-07)

**Status:** `R3-W1-MANUFACTURED-V2 = PASS`.

This is a short-time finite-box implementation preflight. The archived v1 result remains failed and unchanged. No long-time amplification, singularity, regularity, continuum-convergence, or Clay A/B/C/D claim follows.

## Execution provenance

The first workflow attempt, run `34112802643`, terminated before producing a scientific report because the v2 summary wrapper removed a descriptive legacy key before calling the unchanged v1 summary helper. No frozen scientific parameter or threshold was changed. Commit `bd8ee744803b0765608854a6c8e952bd86882b42` restored that key only.

Production execution:

```text
revision: bd8ee744803b0765608854a6c8e952bd86882b42
workflow: R3 W1 manufactured short-time gate v2
run: 34112974469
conclusion: success
artifact: r3-w1-manufactured-short-time-v2
artifact id: 10015094692
sha256:253345aa64bf10a36ab15bae57513bba4305be05f2003c79604571213c02c5b6
```

Frozen preregistration:

`R3_AXISYM_WHOLESPACE_W1_MANUFACTURED_V2_PREREG_2026-09-07.md`.

Exact decision:

```text
R3-W1-MANUFACTURED-V2 = PASS
```

Permanent v1 status:

```text
R3-W1-MANUFACTURED-v1 = STOP_REPAIR_W1_MANUFACTURED
```

## Inherited M1/M2 consistency

```text
M1 initial RHS relative errors
h=.04: u1=1.2668778207969671e-2, omega1=1.8570827548033405e-2
h=.02: u1=2.883010626216072e-3,  omega1=4.698892278680341e-3

M2 first-step RK4 secant relative errors
h=.04: u1=1.2680807472967607e-2, omega1=1.858807315783536e-2
h=.02: u1=2.894482675017511e-3,  omega1=4.716761042930728e-3
```

All inherited thresholds and reduction/decrease conditions passed.

## M3 / inherited non-divergence M4

All four `(h,integrator)` runs completed exactly eight accepted steps with zero rejected steps.

Selected streamed extrema:

```text
max frozen-symbol amplification = 1.0
max CFL = 2.1321988723283098e-10
max viscous number = 7.5e-3
max Poisson residual < 4.3e-14
max odd-z defect < 8.5e-15
max energy ratio < 1
max energy-balance defect:
  h=.04 about 1.31258945266e-2
  h=.02 about 3.48726071e-3
```

All inherited M3 and non-divergence M4 conditions passed.

## Repaired divergence rows

### Exact centered defect identity

Worst accepted-step relative mismatch between

```text
div_ind = D_r u_r + u_r/r + D_z u_z
```

and

```text
div_pred = q_i - (q_{i+1}+q_{i-1})/2,
q=D_z psi,
```

was

```text
2.799446840033473e-12
```

below the frozen v2 `1e-9` threshold.

### Independent-diagnostic refinement

Maximum core-relative independent divergence:

```text
h=.04 RK4     1.1301103801072167e-3
h=.02 RK4     2.8519330514493156e-4
h=.04 SSPRK3  1.1301103801072171e-3
h=.02 SSPRK3  2.851933051447390e-4
```

At every one of the eight matched accepted times, both integrators satisfied the preregistered fine/coarse ratio `<=0.35`. The worst observed ratio was

```text
0.2523588050911226.
```

### Compatible commutator

Worst normalized

```text
r(D_z D_r psi - D_r D_z psi)
```

residual was

```text
1.1298500016833566e-15,
```

below the frozen `1e-12` threshold.

## M5 cross-checks

```text
RK4 vs SSPRK3 combined-state relative difference
h=.04  5.362774111905446e-16
h=.02  5.40883926829345e-16

RK4 resolution relative difference
u1     4.872515088255439e-7
omega1 1.392358632809876e-2
```

All inherited M5 thresholds passed.

## Interpretation

The versioned short-time nonlinear implementation passes the frozen manufactured test after the recovered-divergence diagnostic was separately derived and independently audited. This establishes only that the current finite-box code reproduces the exact first-time identities and the stated finite-discrete diagnostics over `T=2e-4` for the frozen datum.

It does not establish that the finite-box evolution is a validated approximation to whole-space Navier--Stokes at candidate times. Viscous evolution immediately destroys compact support, so the compact-source W0 far-field enclosure cannot simply be reused.

## Next required numerical gate

Before any longer candidate-time growth interpretation, preregister and execute a **dynamic-domain / elliptic-boundary audit** at matched early-time snapshots. It should independently vary radial and axial box extent and compare the finite-box Poisson inversion against a free-space Green reference for the evolved numerical `omega1`, while keeping physical datum, core receiver region, grid spacing, timestep, and integrator fixed.

That next gate is still numerical evidence, not a rigorous evolved-tail theorem; an analytic or validated tail enclosure remains a later obligation.
