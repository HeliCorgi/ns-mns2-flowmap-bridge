# R3 axisymmetric whole-space alpha-kappa family screen — preregistration

Date: 2026-09-09 JST

Status: **preregistered before family-screen output**.

This gate follows merged PR #117, whose frozen `alpha=16, kappa=1` candidate-time pilot passed all numerical-validity checks through `T=.25` but produced no preregistered physical-growth trigger. The purpose here is only to triage a small dimensionless family and identify rows, if any, worth a separately preregistered matched-resolution confirmation.

This is not a singularity test, not a continuum whole-space theorem, and not a Clay A/B/C/D claim.

## 1. Parent boundary

Merged `main` entering this gate is

```text
3aad852ee20dd0e1e72a4634bcf800c0831a390a
```

with

```text
R3-CANDIDATE-TIME-PILOT(alpha=16,kappa=1,T=.25)
  = PASS_NO_GROWTH_TRIGGER_THROUGH_T025
```

No stopped parent result is retroactively changed.

## 2. Frozen datum family

Keep the exact `SPEC.md` whole-space axisymmetric-with-swirl equations, `nu=.01`, `R=1`, `force=0`, and the same compact smooth shape family. Vary only the scale-invariant pair `(alpha,kappa)`:

```text
A = alpha * nu
Z = kappa
u1_0(r,z) = A b(r^2) (z/Z) b(z^2/Z^2)
omega1_0 = 0
psi1_0 = 0
```

The screen grid is exactly

```text
alpha in {16, 32, 64, 128}
kappa in {0.75, 1.00, 1.50}
```

for 12 rows total. There is no adaptive parameter insertion, deletion, or retuning after output.

## 3. Frozen screen discretization

Each row is evolved with classical RK4 to

```text
Tscreen = .25
h = .08
dt = .002
```

on two independent nonperiodic finite boxes:

```text
B22: Rmax=2, Zmax=2
B44: Rmax=4, Zmax=4
```

Thus every row has exactly 125 attempted/accepted steps if it remains safe. The purpose is triage, not continuum confirmation. Any row promoted by this screen must later receive an independent matched-resolution confirmation.

## 4. All-step runtime gate

Both B22 and B44 runs for every row must retain the inherited W1 all-stage/all-step checks:

- finite stage/state/RHS;
- frozen-symbol amplification `<= 1+1e-10`;
- CFL `<= .10`;
- viscous number `<= .05`;
- stage and accepted-step Poisson residual `<= 1e-10`;
- odd-z parity defect `<= 1e-12`;
- physical energy ratio `<= 1+1e-5`;
- stepwise energy-balance defect `<= .20`;
- zero rejected steps;
- exact completion of 125 accepted steps;
- final Poisson residual `<=1e-10`.

A row failing either box is classified invalid and cannot trigger promotion.

## 5. Frozen domain veto

For each `(alpha,kappa)` compare B22 and B44 at the same `h,dt,T`.

On the common core

```text
r <= .8, |z| <= .8
```

let `Sbox` be the relative combined `(u1,omega1)` difference. At the four frozen W1 receivers

```text
(.12, .00), (.24, .20), (.28,-.24), (.20,.32)
```

let `Vbox` be the relative difference of recovered `(u^r,u^z)`.

Also compare the two physical-growth diagnostics used for screening.

Require all of

```text
Sbox <= .01
Vbox <= .05
abs(Emax_B22 - Emax_B44) <= .01
abs(Wfinal_B22 - Wfinal_B44) <= .02
```

where

```text
Emax = max_{0<=t<=.25} physical_enstrophy(t) / physical_enstrophy(0)
Wfinal = final physical-vorticity sup / initial physical-vorticity sup.
```

These are screen-level vetoes only. They are not rigorous `R^3` tail enclosures.

## 6. Frozen growth trigger

A row is sent to high-resolution confirmation only if its runtime and domain vetoes pass and **both boxes independently show the same physical-growth trigger**.

Define

```text
G_E: min(Emax_B22,Emax_B44) >= 1.02
G_W: min(Wfinal_B22,Wfinal_B44) >= 1.05
```

A row is promoted iff `G_E or G_W`.

The thresholds intentionally require growth above the no-growth parent row and above small coarse-grid/domain differences. They are only triage thresholds, not singularity criteria.

## 7. Machine classifications

For each row:

```text
INVALID_RUNTIME
INVALID_DOMAIN
NO_GROWTH_TRIGGER
PROMOTE_HIGH_RES
```

Overall screen decision:

```text
if every row is INVALID_RUNTIME/INVALID_DOMAIN:
    R3-FAMILY-SCREEN = STOP_REPAIR_SCREEN
elif at least one row is PROMOTE_HIGH_RES:
    R3-FAMILY-SCREEN = PASS_WITH_PROMOTIONS
else:
    R3-FAMILY-SCREEN = PASS_NO_PROMOTIONS
```

Rows marked `PROMOTE_HIGH_RES` are the only rows permitted into the next matched-resolution gate. No post-hoc substitution by a nearby parameter is allowed.

## 8. Required output

For every row and box save:

- full streamed runtime summary;
- initial/final/max physical enstrophy and `Emax`;
- initial/final physical-vorticity sup and `Wfinal`;
- final `max|u1|` ratio and final `max|omega1|/A` as descriptive diagnostics;
- final receiver `psi,psi_r,psi_z` and recovered `u^r,u^z`;
- B22/B44 state and velocity differences;
- all domain-veto booleans;
- exact row classification.

The report must list the promotion set explicitly and deterministically.

## 9. Next gate if promotions exist

Each promoted row must be confirmed separately at matched spatial resolutions before any longer-time interpretation. The minimum next design is B22/B44 at `h=.04` plus a B22 `h=.02` refinement row, with `dt/h^2=.3125`, all-step runtime diagnostics, and a domain-vs-resolution comparison analogous to the merged W1 dynamic-resolution/candidate-time gates.

If there are no promotions, this screen does not prove regularity or exclude other datum families; it only says this frozen 12-row grid produced no qualifying amplification through `T=.25`.

## 10. Nonclaims

No row from this screen, even if promoted, is evidence of finite-time blow-up. No power-law fit, singular-time fit, continuation-norm divergence claim, global-regularity claim, or Clay A/B/C/D claim is permitted from this gate.