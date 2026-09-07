# R3 axisymmetric-with-swirl evolution E1 preregistration — 2026-09-07

**Classification:** `NUMERICAL CANDIDATE INFRASTRUCTURE / PRE-EXECUTION CONTRACT`.

E1 is the first nonlinear time-integration smoke gate after the static S0 seed audit and the
nonperiodic elliptic E0 prototype. It is not a singularity search result. The purpose is to
verify that the exact `SPEC.md` normalized equations can be advanced on a strictly nonperiodic
truncated box with fail-closed all-step diagnostics before any resolution or blow-up fit is used.

## Frozen E1 smoke case

Before hosted execution, freeze:

```text
seed             R3S04
nu               0.002
T                0.02
Rmax             0.8
Zmax             0.7
nr               96 radial intervals
nz               168 axial intervals
dt_cap           0.001
integrator       SSPRK3
space            centered second-order node finite differences
elliptic         factorized second-order -L5 solve
outer scalar BC  zero artificial Dirichlet
z topology       nonperiodic
CFL limit        0.40
viscous limit    0.80 using nu*dt*max_i sum_j |A_ij|
```

`R3S04` is the already-preregistered middle-radius, narrow-z, zero-shift member of the S0 family.
This selection is for pipeline continuity with the E0 compact manufactured recovery, not because
it was observed to grow. E1 does not rank the 12 seed geometries.

The outer zero Dirichlet condition is explicitly an artificial finite-box approximation. It is
not claimed to equal the free-space elliptic or parabolic boundary condition. Domain enlargement
and free-space truncation control remain E2 obligations.

## Equation and sign freeze

Advance exactly

\[
\partial_tu_1=-u^r u_{1,r}-u^z u_{1,z}+2\psi_{1,z}u_1+\nu\mathcal L_5u_1,
\]

\[
\partial_t\omega_1=-u^r\omega_{1,r}-u^z\omega_{1,z}
+\partial_z(u_1^2)+\nu\mathcal L_5\omega_1,
\]

with

\[
-\mathcal L_5\psi_1=\omega_1,
\qquad u^r=-r\psi_{1,z},
\qquad u^z=2\psi_1+r\psi_{1,r}.
\]

No periodic wrap, Hou no-slip wall-vorticity closure, reduced model, filtering, or tangent/POD
machinery enters this gate.

## Precondition: complete E0 prototype smoke

The E1 workflow must rerun and pass:

1. S0 static seed checks;
2. the existing E0 smooth-Gaussian, Green-reference, independent-domain and compact-seed tests;
3. a new broad-axial manufactured solution
   \(\psi=\exp(-r^2/0.20^2-z^2/0.80^2)\), with characteristic axial wavenumber `O(1)`,
   under `24 -> 48 -> 96` refinement.

The third item closes the still-explicit low-axial-frequency stress obligation in the E0 contract.
It must show clear second-order reduction of field and first-derivative errors and final
`Linf < 2e-3`, with algebraic residual below `1e-10`.

## All-step fail-closed diagnostics

Every accepted SSPRK3 step, not only sparse output times, updates:

- finite state;
- pre, stage-1, stage-2 and post advective CFL;
- conservative explicit-diffusion number `nu*dt*max row-absolute-sum(-L5)`;
- physical kinetic energy and positive single-step relative increase;
- `Gamma=r^2 u1` maximum-principle overshoot;
- axis regularity defect;
- reconstructed physical-divergence relative `Linf` defect;
- elliptic algebraic residual;
- minimum amplitude/gradient scale in grid points over `u1` and `omega1`;
- dimensionless grid-curvature tail diagnostic;
- outer boundary-shell amplitude ratio.

A stage CFL violation, viscous-limit violation or non-finite trial state rejects the full step and
retries with `dt/2`. Acceptance-critical values are never decided from sparse snapshots.

## Frozen E1 PASS gate

E1 passes only if all of the following hold:

```text
sampled SSPRK3 frozen linear stability rectangle   max |R(-a+ib)| <= 1+5e-13
accepted steps                                     > 0
rejected steps                                     <= 20
minimum dt                                         >= 1e-8
all pre/stage/post CFL                             <= 0.40
all viscous numbers                                <= 0.80
max positive one-step relative energy increase    <= 1e-4
relative Gamma sup overshoot                       <= 1e-3
axis regularity defect                             <= 1e-12
relative physical-divergence Linf defect           <= 1e-2
elliptic algebraic residual Linf                   <= 1e-8
minimum gradient scale                             >= 1.0 grid point
outer boundary-shell ratio                         <= 1e-6
curvature-tail diagnostic                          finite; refinement verdict deferred to E2
```

The stability rectangle uses the SSPRK3 polynomial
`R(z)=1+z+z^2/2+z^3/6`, `0<=a<=0.80`, `|b|<=0.40`. This sampled check is not a
nonlinear stability theorem.

If E1 fails, repair or replace the discretization before running a candidate geometry search.
The thresholds are not relaxed post hoc. If E1 passes, the conclusion is only

```text
R3-E1-NONLINEAR-INTEGRATOR-SMOKE = PASS
```

and the next step is E2: a preregistered same-continuum-datum spatial/time/domain convergence
lattice, followed only then by a bounded multi-seed candidate screen.

## Nonclaims

E1 does not establish a resolved whole-space trajectory, a continuum convergence theorem,
free-space truncation control, numerical blow-up, finite-time nonextendability, or Clay A/B/C/D.
