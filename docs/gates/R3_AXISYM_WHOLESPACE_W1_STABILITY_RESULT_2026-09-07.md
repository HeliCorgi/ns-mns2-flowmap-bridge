# R3 W1 stability preflight result — 2026-09-07

**Decision:** `R3-W1-STABILITY-PREFLIGHT = PASS` on the frozen detector gate.

**Scope:** frozen-coefficient stability-detector audit only. No nonlinear evolution, amplification, singularity, regularity, continuum-convergence, or Clay A/B/C/D claim.

## Provenance

Frozen preregistration:

`docs/gates/R3_AXISYM_WHOLESPACE_W1_STABILITY_PREREG_2026-09-07.md`.

Production revision:

```text
c138fb957af98f68007b532e01cc502599f6bdea
```

Workflow:

```text
R3 W1 stability preflight
run 34108056875
conclusion: success
```

Artifact:

```text
r3-w1-stability-preflight
artifact id 10013168914
sha256:f3dea6a4cf51945026ad73ef45c89bb138aa6e153a2743db3e695123bd594acf
```

The machine-readable report gives `decision = PASS` and all seven preregistered checks true.

## S1 — pure centered advection negative control: PASS

Frozen row:

```text
c_r=1, c_z=0, nu=0,
dr=dz=0.05, dt=0.02.
```

Maximum amplification over the `1025 x 1025` wavenumber scan:

```text
Heun    1.003194896318756
SSPRK3  1.0
RK4     1.0
```

Thus the detector explicitly catches the known Heun/centered-advection instability while the frozen RK4 and SSPRK3 controls stay at or below the fail-closed `1+1e-10` threshold. The value `1.0` is attained by the zero mode and is permitted by the preregistration.

## S2 — stable advection-diffusion row: PASS

Frozen row:

```text
|u^r|=0.5, |u^z|=0.75,
nu=0.01,
dr=dz=0.025,
r_min=dr,
dt=0.001,
```

with the conservative interior `L5` radial stress `3 nu / r_min` included in `c_r_eff`.

Maximum amplification:

```text
Heun    1.0
SSPRK3  1.0
RK4     1.0
```

The preregistered acceptance required RK4 and SSPRK3 only; both pass.

## S3 — intentionally oversized step: PASS as rejection test

Using the S2 coefficients with `dt=0.03` gives

```text
Heun    5.016571810627325
SSPRK3  5.615746020181708
RK4     4.810988282315105
```

Both production/comparison integrators exceed the rejection threshold by a wide margin. The detector therefore fails closed on the intentionally unsafe explicit step.

## Decision

```text
S1 Heun instability detected         PASS
S1 RK4 stable                        PASS
S1 SSPRK3 stable                     PASS
S2 RK4 stable                        PASS
S2 SSPRK3 stable                     PASS
S3 RK4 unsafe-step rejection         PASS
S3 SSPRK3 unsafe-step rejection      PASS
R3-W1-STABILITY-PREFLIGHT            PASS
```

## What this does and does not discharge

This discharges only the P0-A **detector preflight**. It does not prove nonlinear solver stability and does not discharge P0-B/C. A real W1 step must recompute the accepted stability/CFL quantities from the pre-state and every RK stage, reject unsafe proposals, and stream acceptance-critical diagnostics over every accepted step.

The next gate is therefore a short-time manufactured nonlinear evolution using the exact W0 initial identities

```text
partial_t omega1|_0 = partial_z(u1_0^2),
partial_t u1|_0 = nu L5 u1_0,
```

plus fail-closed per-stage/per-step diagnostics and an RK4-versus-SSPRK3 comparison. No long-time growth or singularity scan is opened by this PASS.
