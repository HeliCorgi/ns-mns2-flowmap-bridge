# R3 axisymmetric swirl whole-space solver contract — 2026-09-07

**Classification:** `NUMERICAL CANDIDATE INFRASTRUCTURE / PRE-EXECUTION CONTRACT`.

This is the next gate after the static seed-family S0 audit. It is deliberately separated from the old periodic-z / radial-wall pilot. Nothing in this document certifies a Navier–Stokes singularity or a Clay statement.

## A. Governing evolution

Use exactly the `SPEC.md` normalized system

\[
\partial_tu_1+u^r u_{1,r}+u^z u_{1,z}
=2\psi_{1,z}u_1+\nu\mathcal L_5u_1,
\]

\[
\partial_t\omega_1+u^r\omega_{1,r}+u^z\omega_{1,z}
=\partial_z(u_1^2)+\nu\mathcal L_5\omega_1,
\]

\[
-\mathcal L_5\psi_1=\omega_1,
\qquad
u^r=-r\psi_{1,z},\quad
u^z=2\psi_1+r\psi_{1,r}.
\]

No finite-cylinder no-slip wall-vorticity closure is imported into this lane.

## B. Domain approximation

The production approximation is a nonperiodic rectangle

\[
0\le r\le R_{\max},\qquad -Z_{\max}\le z\le Z_{\max},
\]

used only as an approximation to whole space. `Rmax` and `Zmax` must be independently enlarged. Periodic wrapping in `z` is forbidden in the whole-space verdict path.

Candidate data are compactly supported strictly inside the box at `t=0`. Numerical box boundaries are artificial boundaries and their effect must be measured or bounded separately from spatial discretization error.

## C. Elliptic inversion gate E0

The first implementation task is the free-space inversion

\[
-\mathcal L_5\psi_1=\omega_1,\qquad \psi_1\to0\text{ at spatial infinity}.
\]

The seed family provides a manufactured exact pair because `psi1` is explicit and

\[
\omega_1=-(4s\psi_{1,ss}+8\psi_{1,s}+\psi_{1,zz}).
\]

Any candidate elliptic solver must therefore pass, before nonlinear evolution:

1. recover the manufactured `psi1` from its derived `omega1`;
2. show convergence under spatial refinement;
3. show independent improvement as `Rmax` and `Zmax` are enlarged;
4. report interior `Linf`, physical weighted `L2`, and first-derivative errors;
5. report the discrete elliptic residual separately;
6. include a low-axial-frequency stress test so a periodic Fourier gap cannot masquerade as whole-space decay;
7. use either a free-space Green/Hankel method or an artificial/multipole boundary with an explicit truncation-error audit.

Domain doubling alone is diagnostic evidence, not a rigorous tail bound.

### Free-space reference identity

Interpreting `r` as the radial coordinate in four transverse dimensions gives the 5D scalar fundamental solution

\[
G_5(X)=\frac1{8\pi^2|X|^3}
\]

for `-Delta_5`. This identity may be used to build an independent reference evaluator. It is only an elliptic scalar representation; the physical velocity and incompressibility remain three-dimensional.

## D. Evolution integrator gate E1

The first nonlinear prototype uses SSPRK3 or classical RK4. Do not use the previously audited Heun+centered-advection combination as the sole production evidence.

Every accepted step must update streaming maxima/minima for at least:

- finite-value state;
- pre/stage/post advective CFL;
- viscous stability number when explicit diffusion is used;
- physical kinetic energy and positive single-step relative energy change;
- circulation maximum-principle defect for `Gamma=r^2 u1` where applicable;
- axis parity/regularity defect;
- physical divergence reconstruction defect;
- elliptic algebraic residual;
- narrowest resolved scale in both `r` and `z`;
- high-frequency / discretization-tail diagnostic appropriate to the chosen nonperiodic basis.

Diagnostic output may be sparse, but acceptance-critical extrema may not be sampled sparsely.

## E. First convergence lattice E2

Before looking for a singularity fit, every surviving seed must have at least:

- three spatial resolutions with the same continuum datum;
- highest accepted spatial resolution rerun at `dt/2`;
- at least two independently enlarged `(Rmax,Zmax)` choices with one-coordinate-at-a-time enlargement;
- a precision/reload reproducibility record;
- common-physical-coordinate comparisons of `u1`, `omega1`, velocity, and first derivatives.

No exponent fit or blow-up-time fit is used to decide whether the run is resolved. Resolution gates are defined before such fits.

## F. Promotion vocabulary

Passing E0 means only `WHOLE-SPACE ELLIPTIC APPROXIMATION TEST PASSED` for the tested manufactured family.

Passing E1/E2 with growing norms means `R^3 NUMERICAL GROWTH CANDIDATE` at most. Promotion toward a breakdown claim still requires a rigorous connection to a continuation-controlling norm or another exact nonextendability criterion, plus validated error bounds.

## G. Explicit exclusions inherited from negative knowledge

This contract does not search for a steady self-similar front, does not assume a DSS profile, and does not use continuum-to-lattice shadowing. If a later trajectory appears asymptotically self-similar, the Tsai / Chae–Wolf exclusions and the external DSS registry must be rechecked before any profile claim is made.