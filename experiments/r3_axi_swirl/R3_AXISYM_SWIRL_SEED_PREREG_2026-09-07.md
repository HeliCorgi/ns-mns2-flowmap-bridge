# R3 axisymmetric-with-swirl seed-family preregistration — 2026-09-07

**Classification:** `NUMERICAL CANDIDATE INFRASTRUCTURE / R^3 TRACK`.

This document starts a new candidate-construction lane under `PROJECT_GOAL.md` and `SPEC.md` after the periodic M-1 filtered near/far promotion gate stopped. It does **not** claim a Navier–Stokes singularity, nonextendability, global regularity, or Clay A/B/C/D.

## 1. Physical target and variables

The target is the unforced whole-space axisymmetric-with-swirl system on `R^3` from `SPEC.md`, with

\[
u_1=u^\theta/r,\qquad \omega_1=\omega^\theta/r,\qquad \psi_1=\psi^\theta/r,
\]

and

\[
-\mathcal L_5\psi_1=\omega_1,\qquad
\mathcal L_5=\partial_r^2+\frac3r\partial_r+\partial_z^2.
\]

The seed constructor works in

\[
s=r^2
\]

so every primitive seed is a smooth function of `(s,z)`. This makes the Cartesian reconstruction smooth at the axis by construction rather than by imposing only a first-order Neumann condition.

## 2. Compact bump primitive

Use the fixed normalized bump

\[
B(q)=\begin{cases}
\exp\!\left(1-\frac1{1-q^2}\right),&|q|<1,\\
0,&|q|\ge1.
\end{cases}
\]

Thus `B(0)=1` and `B` is `C^infty` with compact support.

For a seed parameter tuple

```text
SeedParams(
  s0,
  ws,
  wz,
  zu,
  Au,
  Apsi
)
```

define

\[
q_s=(s-s_0)/w_s,\qquad q_u=(z-z_u)/w_z,\qquad q_\psi=z/w_z.
\]

The fixed family is

\[
u_1(s,z)=A_u B(q_s)B(q_u),
\]

\[
\psi_1(s,z)=A_\psi B(q_s)\,q_\psi B(q_\psi).
\]

The odd axial factor in `psi1` creates an inward radial velocity near `z=0` when `Apsi>0`, while the swirl profile remains a compact smooth packet. This is a generic finite-energy seed family, not a self-similar/DSS profile ansatz.

Set

\[
\omega_1:=-(4s\,\partial_s^2\psi_1+8\,\partial_s\psi_1+\partial_z^2\psi_1),
\]

which is exactly `-L5 psi1` because for `f=f(s,z)`,

\[
\partial_r^2f+\frac3r\partial_rf=4s f_{ss}+8f_s.
\]

The physical velocity is reconstructed by

\[
u^r=-r\psi_{1,z},\qquad
u^z=2\psi_1+2s\psi_{1,s},\qquad
u^\theta=ru_1.
\]

The Cartesian form used for independent checks is

\[
u_x=-x\psi_{1,z}-yu_1,\quad
u_y=-y\psi_{1,z}+xu_1,\quad
u_z=2\psi_1+2s\psi_{1,s}.
\]

## 3. First frozen geometry lattice

The first geometry-only scan is frozen before time evolution. No result-dependent seed insertion is allowed inside this first lattice.

```text
s0 in {0.04, 0.09, 0.16}
ws = 0.05
wz in {0.18, 0.28}
zu in {0.00, 0.08}
Au = 1.0
Apsi = 0.10
```

This gives 12 continuum seeds. The purpose of this first lattice is to test the whole-space candidate pipeline, not to optimize blow-up growth. Amplitude/Reynolds-number scans, if commissioned, must be preregistered separately rather than chosen after inspecting these runs.

## 4. Seed-level fail-closed gate S0

A seed enters any time-evolution experiment only if all of the following hold:

1. `u1`, `psi1`, and the derived `omega1` are finite on all audit samples;
2. `u_theta` is nonzero somewhere;
3. support is compact in both `r` and `z` with the analytic support bounds recorded;
4. axis conditions `u^r=u^theta=omega^theta=psi^theta=0` at `r=0` hold by reconstruction;
5. the analytic cylindrical divergence identity cancels to roundoff;
6. an independent Cartesian finite-difference divergence check decreases at second-order rate on interior audit points;
7. an independent finite-difference check of `-L5 psi1 = omega1` decreases at second-order rate away from support edges and the axis stencil singularity;
8. physical kinetic energy computed with `2*pi*r dr dz` is finite and positive;
9. the same continuum seed evaluated at common physical coordinates is independent of the numerical resolution.

Failure of S0 excludes the seed until the construction or audit is corrected. S0 is not a PDE evolution or singularity gate.

## 5. Whole-space evolution gate S1 — required before candidate promotion

The existing finite-cylinder/periodic-z pilot is not the production solver for this lane. Before any seed is called an `R^3 numerical candidate`, the evolution stack must satisfy the whole-space transition obligations carried from the read-only Fable5 audit:

- nonperiodic `z` finite-box approximation to `R^3`;
- compact support in `z` and smooth radial dependence through `r^2`;
- free-space treatment of `-L5 psi1=omega1` (Green/Hankel/multipole/artificial-boundary method with independently audited error);
- independent enlargement of `Rmax` and `Zmax`;
- explicit periodic-image exclusion (no periodic-z evidence promoted as whole-space evidence);
- all-step streaming acceptance diagnostics, not diagnostic-stride-only maxima;
- SSPRK3/RK4/validated alternative rather than relying on the previously audited Heun+centered-advection route;
- separate spatial, time-step, domain-truncation, floating-point, and elliptic-solver error records;
- physical `R^3` finite-energy checks using the Cartesian/`2*pi*r dr dz` measure.

The first S1 implementation should be a conservative, auditable solver and convergence harness. It should not inherit a wall condition from the Hou finite-cylinder pilot and relabel it as free space.

## 6. Negative-knowledge preflight

Read-only registry checked before opening this lane:

- `ns-singularity-certificate-lab@fable5-mainline/docs/research_notes/verification_sprint_v1/VERDICTS.md`;
- `ns-singularity-certificate-lab@fable5-mainline/FABLE5_NEXT_TASK_AUDIT.md`.

This seed family does **not** reopen the killed continuous self-similar steady-front profile, does not assume a DSS orbit, and does not use the killed continuum-to-lattice shadowing route. Any future observation resembling a self-similar/DSS profile must be checked against those binding no-go results before promotion.

## 7. Decision boundary

A successful S0 run establishes only:

```text
EXPLICIT C_c^infty-LIKE AXISYMMETRIC SWIRL SEED CONSTRUCTION
+ NUMERICAL RECONSTRUCTION/AUDIT PASS
```

where `C_c^infty-like` means the implementation samples an analytically specified `C_c^infty` formula; the floating arrays themselves are finite-resolution samples, not a formal proof object.

A later S1 growth event remains a `NUMERICAL OBSERVATION` until spatial/time/domain/precision convergence and reconstruction residuals are demonstrated. Finite-time nonextendability requires a separate rigorous continuation-controlling norm argument or equivalent exact failure mode.