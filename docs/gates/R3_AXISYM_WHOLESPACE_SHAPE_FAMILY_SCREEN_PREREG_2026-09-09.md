# R3 axisymmetric whole-space shape-family screen — preregistration

Date: 2026-09-09 JST

Status: **preregistered before shape-family numerical output**.

This gate follows merged PR #118, whose fixed centered pure-swirl bump family produced no preregistered physical-growth trigger over `alpha={16,32,64,128}`, `kappa={.75,1,1.5}` through `T=.25`. The purpose here is to change the **datum shape**, not to continue increasing `alpha` in the same profile.

This remains a finite-resolution triage gate. It is not a singularity test, continuum whole-space theorem, regularity result, or Clay A/B/C/D claim.

## 1. Parent and negative-knowledge boundary

Parent merged `main`:

```text
9070b7b998e41882b82dcdaadefc3a99b8db3f41
```

External Fable5 P0-A/B/C/D/E obligations remain binding: RK4 frozen-symbol stability, all-stage/all-step CFL/stability/finite/Poisson/parity/energy diagnostics, nonperiodic `z`, explicit B22/B44 domain sensitivity, and no grid-scale or continuum claim from coarse growth.

The previous family screen is not relabeled. Its exact status remains

```text
R3-FAMILY-SCREEN = PASS_NO_PROMOTIONS
```

## 2. Exact admissible datum family

Keep

```text
nu = .01
R = 1
omega1_0 = psi1_0 = 0
u0(x,y,z)=(-y u1_0, x u1_0, 0)
```

so every row is exactly divergence-free pure swirl. Write

```text
s = r^2
zeta = z/kappa
b(q) = exp(-q/(1-q)) for 0<=q<1, and 0 for q>=1.
```

Every radial factor below is a `C_c^infty` function of `r^2`; every axial factor is odd and `C_c^infty`. Hence the Cartesian field is `C_c^infty(R^3)`, divergence-free, finite-energy, and has nonzero swirl for nonzero amplitude.

Freeze two radial profiles:

```text
C(s) = b(s)
A(s) = b(((s-.45)/.35)^2)
```

`A` is an annular profile supported where `.10 < r^2 < .80`, so it remains smooth at the axis and compactly supported before `r=1`.

Freeze three axial profiles:

```text
Z0(zeta) = zeta * b(zeta^2)
Z1(zeta) = zeta * b(zeta^2)^2
Z2(zeta) = zeta * (1 - 2 zeta^2) * b(zeta^2)
```

`Z1` concentrates the original axial lobe without changing its support. `Z2` inserts a preregistered interior sign change and therefore changes the spatial organization of `partial_z(u1^2)` without changing odd parity or compact support.

The six shape codes are the Cartesian product

```text
C-Z0, C-Z1, C-Z2,
A-Z0, A-Z1, A-Z2.
```

For a row `(alpha,shape)`, freeze

```text
Acoef = alpha * nu
kappa = .75
u1_0(r,z) = Acoef * RadialShape(r^2) * AxialShape(z/.75).
```

No result-dependent renormalization of the shapes is allowed.

## 3. Frozen screen rectangle

Use only

```text
alpha = {64,128}
kappa = .75
shape = {C-Z0,C-Z1,C-Z2,A-Z0,A-Z1,A-Z2}
```

for exactly 12 rows.

The choice `kappa=.75` is hypothesis-generation informed by PR #118, where `(128,.75)` had the largest descriptive generated `max|omega1|/A`; that prior observation is **not** itself a growth result. This new screen is separately preregistered before any new-shape output.

For every row run both

```text
B22: Rmax=2, Zmax=2
B44: Rmax=4, Zmax=4
```

with identical

```text
Tscreen=.25
h=.08
dt=.002
RK4
```

and the same nonperiodic finite-box elliptic solver used by the merged W1 stack.

## 4. Binding runtime gate

Each B22 and B44 evolution must satisfy, over all attempted RK stages and all accepted steps:

- exact completion of `T=.25` (`125` accepted steps);
- zero rejected steps;
- finite state and RHS;
- frozen-symbol amplification `<=1+1e-10`;
- CFL `<=.10`;
- viscous number `<=.05`;
- stage/step Poisson residual `<=1e-10`;
- odd-z defect `<=1e-12`;
- physical energy ratio `<=1+1e-5`;
- stepwise physical energy-balance defect `<=.20`;
- final Poisson residual `<=1e-10`.

A row failing this gate is `INVALID_RUNTIME` and cannot be promoted.

## 5. Binding matched-box domain veto

For each row compare B22 with B44 at identical `h,dt,T`.

Freeze

```text
common-core combined (u1,omega1) relative difference <= .01
receiver meridional-velocity relative difference      <= .05
|max-enstrophy-ratio_B22 - _B44|                      <= .01
|final-vorticity-ratio_B22 - _B44|                    <= .02
```

A runtime-valid row failing any domain condition is `INVALID_DOMAIN` and cannot be promoted.

This is only a numerical finite-box veto, not a rigorous whole-space tail enclosure.

## 6. Physical-growth promotion rule

Only after runtime and domain gates pass, define

```text
G_E: min(B22,B44 max physical enstrophy / initial) >= 1.02
G_W: min(B22,B44 final physical-vorticity sup / initial) >= 1.05
```

Classify each row exactly as

```text
INVALID_RUNTIME
INVALID_DOMAIN
PROMOTE_HIGH_RES     if G_E or G_W
NO_GROWTH_TRIGGER    otherwise
```

The screen decision is

```text
STOP_REPAIR_SHAPE_SCREEN  if no row is numerically valid
PASS_WITH_PROMOTIONS      if at least one row is PROMOTE_HIGH_RES
PASS_NO_PROMOTIONS        otherwise.
```

Only `PROMOTE_HIGH_RES` rows may enter a later high-resolution confirmation gate.

A coarse promotion is only a triage signal. In particular, Fable5 P0-D remains open: no promoted row may be called resolved growth until a separately preregistered matched-resolution gate records physical width/gradient-scale diagnostics and verifies that any amplification persists under refinement.

## 7. Descriptive mechanism diagnostics

For every valid row record, separately for B22/B44:

- final and maximum physical enstrophy ratios;
- final physical-vorticity-sup ratio;
- final `max|u1|` ratio;
- final `max|omega1| / Acoef`;
- final receiver meridional velocity;
- common-core/domain sensitivity.

These descriptive quantities may rank future hypotheses but cannot override the frozen promotion rule.

## 8. Claim boundary

This gate may establish only a finite-resolution numerical observation about a six-shape pure-swirl family through `T=.25`. It does not establish continuum convergence, rigorous R3 tail control, finite-time breakdown, or global regularity.
