# R3 whole-space elliptic E0 prototype result — 2026-09-07

**Classification:** `NUMERICAL CANDIDATE INFRASTRUCTURE / E0 PROTOTYPE ONLY`.

This is a development audit of the new strictly nonperiodic `z` prototype for

\[
-\mathcal L_5\psi_1=\omega_1.
\]

It is not yet a validated free-space solver and is not a Navier–Stokes time evolution.

## Execution status

The algorithm and gate logic were reproduced in an isolated Python/NumPy/SciPy development run during construction. This is **not yet a hosted revision-qualified execution of the branch source**, so the values below are development evidence.

## Test 1 — smooth 5D-radial free-space reference with exact boundary values

Use

\[
\omega(r,z)=\exp(-(r^2+z^2)/a^2),\qquad a=0.25,
\]

whose exact decaying radial solution is

\[
\psi(\rho)=\frac13\left[\rho^{-3}\int_0^\rho s^4e^{-s^2/a^2}\,ds
+\int_\rho^\infty s e^{-s^2/a^2}\,ds\right],
\qquad \rho=\sqrt{r^2+z^2}.
\]

On the fixed box `Rmax=1`, `Zmax=1.2`, supplying the exact free-space value on the artificial boundary gave:

```text
nr x nz     Linf error       physical-weighted L2 error
24 x 48     8.915891e-05     1.406497e-05
48 x 96     2.230217e-05     3.509820e-06
96 x 192    5.576249e-06     8.771593e-07
```

Both errors decrease by approximately a factor four under each `h -> h/2` refinement, consistent with the intended second-order prototype. The final algebraic sparse-solve residual was below `9e-13`.

## Test 2 — explicit artificial-boundary sensitivity for a nonzero free-space tail

The same Gaussian source has a `rho^-3` elliptic tail. Replacing the exact outer Dirichlet values by zero and holding the mesh scale near `0.02`, the error on the fixed inner core `r<=0.45`, `|z|<=0.45` was:

```text
Rmax=Zmax   core Linf        core physical-weighted L2
0.60        8.925662e-04     5.793057e-04
0.80        3.634461e-04     2.516174e-04
1.00        1.834061e-04     1.299995e-04
1.50        5.440832e-05     3.841492e-05
```

This monotone decrease is useful because it explicitly separates artificial-boundary error from spatial refinement. It is still only a domain-sensitivity observation; domain enlargement is not a rigorous tail enclosure.

## Test 3 — recovery of preregistered compact seed R3S04

For `R3S04` the exact `psi1` is compactly supported strictly inside `Rmax=0.7`, `Zmax=0.6`, so zero Dirichlet data are the exact manufactured boundary values. Solving from its derived `omega1=-L5 psi1` gave:

```text
nr x nz      Linf error       physical-weighted L2 error
 96 x 192    7.308551e-03     1.765296e-03
128 x 256    1.979607e-03     4.506337e-04
160 x 320    3.449917e-04     7.262881e-05
```

The compact bump is deliberately sharp in `s`, so its asymptotic regime begins much later than the Gaussian test. The errors nevertheless decrease strongly on this first high-resolution ladder. The final algebraic residual was about `6.4e-12`.

## Prototype decision

```text
R3-E0-GAUSSIAN-SPATIAL-REFINEMENT = PASS in isolated development reproduction
R3-E0-ARTIFICIAL-BOUNDARY-SENSITIVITY = PASS as diagnostic monotone sequence
R3-E0-COMPACT-R3S04-RECOVERY = PASS in isolated development reproduction
R3-E0-HOSTED-REVISION-CERT = NOT RUN
R3-E0-RIGOROUS-TAIL-ENCLOSURE = NOT DONE
```

This is enough to keep the nonperiodic elliptic prototype alive and to proceed to independent derivative/boundary tests. It is **not** enough to call the solver a validated free-space inversion.

## Next smallest E0 gate

Before nonlinear evolution:

1. add first-derivative recovery errors for the manufactured tests;
2. add independent one-coordinate-at-a-time `Rmax` and `Zmax` enlargement rather than only square boxes;
3. add a second free-space reference path (Green integral, Hankel transform, or equivalent) so the exact radial formula is not the sole tail reference;
4. then freeze the SSPRK3/RK4 whole-space evolution discretization and all-step acceptance diagnostics.

## Nonclaims

No finite-time singularity, nonextendability, continuum-convergence theorem, global regularity statement, or Clay A/B/C/D result is established.