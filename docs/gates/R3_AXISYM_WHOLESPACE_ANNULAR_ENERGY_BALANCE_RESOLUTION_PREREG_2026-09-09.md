# R3 annular energy-balance resolution audit — preregistration

Date: 2026-09-09 JST

Status: **preregistered before repair output**.

Merged PR #119 established that every annular row in the coarse `h=.08` shape screen failed only the frozen stepwise physical energy-balance defect `<=.20`, with defects about `.253-.277`, while stability/CFL/Poisson/parity/energy-monotonicity checks passed. Those annular rows remain `INVALID_RUNTIME`; this gate does not relabel them.

The purpose here is to test one narrow hypothesis: **the annular energy-balance failure is a convergent spatial/time-discretization error caused by the sharper radial envelope**, rather than evidence of an unstable evolution or a failure of the continuum physical energy identity.

## 1. Frozen family

Use exactly the annular profiles from PR #119:

```text
A(r^2) = b(((r^2-.45)/.35)^2)
kappa=.75
Z0=zeta*b(zeta^2)
Z1=zeta*b(zeta^2)^2
Z2=zeta*(1-2*zeta^2)*b(zeta^2)
alpha={64,128}
```

with `nu=.01`, `omega1_0=psi1_0=0`, and the unchanged normalized axisymmetric Navier-Stokes equations.

Use only B22 (`Rmax=Zmax=2`) because this is a short-time discretization audit of the already-observed runtime diagnostic, not a domain-promotion gate. The PR #119 B22/B44 agreement remains archival context only.

## 2. Matched parabolic refinement

Freeze

```text
Trepair = .002

dt/h^2 = .3125
h=.08  dt=.002      1 accepted step
h=.04  dt=.0005     4 accepted steps
h=.02  dt=.000125  16 accepted steps
```

Use RK4 only. No step rejection or result-dependent time-step rescue is allowed.

## 3. Runtime obligations

At every level and for all six `(alpha,axial-shape)` rows require:

- exact completion of the frozen horizon;
- zero rejected steps;
- finite stage and step states;
- frozen-symbol amplification `<=1+1e-10`;
- CFL `<=.10`;
- viscous number `<=.05`;
- Poisson residual `<=1e-10`;
- odd-z defect `<=1e-12`;
- physical energy ratio `<=1+1e-5`.

The energy-balance defect itself is the audited quantity and is not part of this precondition.

## 4. R0 — reproduce the coarse failure

At `h=.08`, the new one-step audit must reproduce the PR #119 B22 max energy-balance defect to absolute tolerance `5e-5` for each row. Frozen PR #119 B22 references are:

```text
alpha=64
  A-Z0  .2769415986484736
  A-Z1  .25902774147980734
  A-Z2  .25263199842185224

alpha=128
  A-Z0  .2769509735222076
  A-Z1  .25903329857106117
  A-Z2  .2526358254831897
```

This verifies that the repair audit is measuring the same stopped diagnostic.

## 5. R1 — refinement must reduce the defect

For each of the six rows let

```text
D08 = max energy-balance defect at h=.08
D04 = max energy-balance defect at h=.04
D02 = max energy-balance defect at h=.02.
```

Require

```text
D04 < D08
D02 < D04
D04/D08 <= .40
D02/D04 <= .40.
```

The `.40` ratio allows substantial non-asymptotic error while still demanding clear better-than-first-order-like reduction consistent with the existing second-order spatial stack.

## 6. R2 — repair the original `.20` gate at useful resolutions

Require for every row

```text
D04 <= .12
D02 <= .05.
```

If this passes, the result supports using `h<=.04` in a future annular growth screen while retaining the original `.20` physical energy-balance threshold. It does **not** retroactively validate the `h=.08` annular rows.

## 7. Decision

```text
PASS
```

only if all runtime preconditions and R0-R2 pass for all six rows. Otherwise

```text
STOP_REPAIR_ANNULAR_ENERGY_BALANCE
```

with the exact failed conditions preserved.

## 8. Claim boundary

A PASS establishes only that the previously stopped annular energy-balance diagnostic converges under the frozen refinement experiment and is below the original runtime tolerance at finer resolution. It is not a continuum convergence theorem, not a growth result, not a whole-space tail enclosure, and not a Clay claim.
