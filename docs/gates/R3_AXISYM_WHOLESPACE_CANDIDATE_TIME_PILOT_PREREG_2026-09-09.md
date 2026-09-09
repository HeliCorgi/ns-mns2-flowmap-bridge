# R3 axisymmetric whole-space candidate-time pilot — preregistration

Date: 2026-09-09 JST

Status: **preregistered before candidate-time output**.

This gate is the first later-time diagnostic opened after the merged short-time R3 W1 stack through PR #116. It is not a singularity test, not a continuum whole-space theorem, and not a Clay A/B/C/D claim.

## 1. Parent boundary

Merged `main` entering this gate is

```text
7d2847ccff9433713515bd34ee8a41a96452b726
```

with the accepted numerical status

```text
R3-W0                              = PASS
R3-W1-STABILITY-PREFLIGHT          = PASS
R3-W1-DIVERGENCE-DIAGNOSTIC-REPAIR= PASS
R3-W1-MANUFACTURED-V2              = PASS
R3-W1-GREEN-QUADRATURE-REPAIR      = PASS
R3-W1-ELLIPTIC-DECOMPOSITION       = PASS
R3-W1-DYNAMIC-RESOLUTION           = PASS
```

The archival STOPs remain unchanged:

```text
PR #109 manufactured-v1 = STOP_REPAIR_W1_MANUFACTURED
PR #112 dynamic-domain-v1 = STOP_REPAIR_GREEN_QUADRATURE
PR #114 dynamic-domain-v2 = STOP_REPAIR_DYNAMIC_DOMAIN
```

No later result may relabel those runs.

## 2. Frozen datum and equations

Use the same `SPEC.md` whole-space axisymmetric-with-swirl system and the same datum family already audited in W0/W1:

```text
nu = 0.01
A  = 0.16
R  = 1
Z  = 1
alpha = A R^2 / nu = 16
kappa = Z/R = 1

u1_0(r,z) = A b(r^2) z b(z^2)
omega1_0 = 0
psi1_0 = 0
```

No parameter search is performed in this pilot.

## 3. Pilot horizon and time-step hierarchy

Freeze

```text
Tpilot = 0.25
```

which is `A*Tpilot = 0.04` in the elementary nonlinear-time bookkeeping used by the W0 scaling note. This is only a moderate later-time diagnostic, not an approach to a candidate singular time.

The primary B22 spatial hierarchy uses a constant parabolic time-step ratio

```text
dt / h^2 = 0.3125
```

so that the frozen viscous scanner number is identical across levels:

```text
B22 h=.08  dt=.002
B22 h=.04  dt=.0005
B22 h=.02  dt=.000125
```

All three end exactly at `Tpilot=0.25`.

An independent time-step shadow is frozen on B22 at `h=.04`:

```text
B22 h=.04  dt=.00025
```

The later-time domain veto uses the same spatial/time discretization as the middle B22 run:

```text
B44 h=.04  dt=.0005
```

No result-dependent extension of `Tpilot`, change of `dt`, or change of box is allowed inside this gate.

## 4. Streaming runtime obligations

Every accepted RK4 step and every RK stage inherits the W1 runtime checks:

- finite state/RHS;
- frozen-symbol amplification `<= 1 + 1e-10`;
- CFL `<= .10`;
- viscous number `<= .05`;
- stage and accepted-step Poisson residual `<= 1e-10`;
- odd-z parity defect `<= 1e-12`;
- physical energy ratio `<= 1 + 1e-5`;
- stepwise energy-balance defect `<= .20`;
- zero rejected steps and exact completion of the frozen horizon.

Acceptance-critical diagnostics remain all-step streaming diagnostics; diagnostic-stride snapshots do not replace them.

## 5. Frozen numerical-validity gates

The candidate-growth classification is forbidden unless all of C0-C4 pass.

### C0 — runtime / final Poisson

All five runs must satisfy §4. The final receiver Poisson residual must also be `<=1e-10`.

### C1 — three-level nonlinear state refinement

On the common core

```text
r <= .8, |z| <= .8
```

let

```text
S84 = rel(B22 h=.08, B22 h=.04)
S42 = rel(B22 h=.04, B22 h=.02)
```

for the combined final `(u1,omega1)` state after restriction to the common grid.

Require

```text
S42 <= .45 S84.
```

The `.45` tolerance is intentionally looser than the ideal second-order `.25` because this is the first substantially longer nonlinear horizon, but it still requires clear refinement.

### C2 — recovered meridional-velocity refinement

At the four already frozen W1 receivers

```text
(.12,  .00)
(.24,  .20)
(.28, -.24)
(.20,  .32)
```

recover `(psi1, psi1_r, psi1_z)` from each run's own final `omega1`, then `(u^r,u^z)`.

With

```text
V84 = rel(V_h08, V_h04)
V42 = rel(V_h04, V_h02)
```

require

```text
V42 <= .45 V84.
```

### C3 — independent time-step shadow

Compare B22 `h=.04,dt=.0005` against B22 `h=.04,dt=.00025` at `Tpilot`.

Let `Stime` be the common-core state relative difference and `Vtime` the receiver-velocity difference. Require

```text
Stime <= .10 * S42   OR max(Stime,S42) <= 1e-10
Vtime <= .10 * V42.
```

This is a pilot-level test that RK4 time error is subordinate to the measured fine spatial correction.

### C4 — later-time domain veto

Compare B22 and B44 at exactly `h=.04, dt=.0005, T=.25`.

Let `Sbox` be the common-core state difference and `Vbox` the recovered receiver-velocity difference. Require

```text
Sbox <= .50 * S42   OR max(Sbox,S42) <= 1e-10
Vbox <= .50 * V42.
```

This is only a numerical later-time finite-box veto. It is not a rigorous `R^3` tail enclosure. If C4 fails, no growth observable from this pilot is scientifically promoted.

## 6. Frozen diagnostic checkpoints

For each run retain streamed physical enstrophy at

```text
t = .05, .10, .25
```

and the maximum physical enstrophy over all accepted steps.

On the finest B22 run additionally record at `Tpilot`:

- physical enstrophy ratio to initial;
- physical vorticity supremum ratio to initial, reconstructed from
  `omega^r=-r d_z u1`, `omega^theta=r omega1`, `omega^z=2u1+r d_r u1`;
- `max |u1|` ratio to initial;
- `max |omega1| / A` as a descriptive generated-toroidal-vorticity scale.

No power-law fit, candidate singular time, or blow-up exponent is computed in this pilot.

## 7. Growth-followup trigger

Only after C0-C4 pass, define a **follow-up trigger**, not a singularity criterion.

Trigger if any of the following holds on the finest B22 run:

```text
G1: max_t physical_enstrophy / initial_enstrophy >= 1.01
G2: final physical_vorticity_sup / initial_physical_vorticity_sup >= 1.05
G3: final max|u1| / initial max|u1| >= 1.02
```

Exact machine classification:

```text
if any C0-C4 fail:
    R3-CANDIDATE-TIME-PILOT = STOP_REPAIR_PILOT_NUMERICS
elif G1 or G2 or G3:
    R3-CANDIDATE-TIME-PILOT = PASS_TRIGGER_FOLLOWUP
else:
    R3-CANDIDATE-TIME-PILOT = PASS_NO_GROWTH_TRIGGER_THROUGH_T025
```

`PASS_TRIGGER_FOLLOWUP` means only that a separately preregistered longer/higher-confidence candidate study is worth opening. `PASS_NO_GROWTH_TRIGGER_THROUGH_T025` does not prove regularity and does not kill the datum family beyond this horizon.

## 8. Claim boundary

This pilot may establish only a reproducible finite-resolution numerical observation through `T=.25` under the frozen convergence/time/domain checks above.

Even a positive trigger is **not** evidence of finite-time breakdown by itself. A later candidate must still close independent domain/tail control, resolution/time/precision variation, Cartesian reconstruction/PDE residuals, and ultimately a rigorous continuation/nonextendability bridge before any Clay-level claim is possible.
