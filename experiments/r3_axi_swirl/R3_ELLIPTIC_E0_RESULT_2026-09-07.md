# R3 whole-space elliptic E0 prototype result — 2026-09-07

**Classification:** `NUMERICAL CANDIDATE INFRASTRUCTURE / E0 PROTOTYPE ONLY`.

This is a revision-qualified numerical audit of the strictly nonperiodic `z` prototype for

\[
-\mathcal L_5\psi_1=\omega_1,
\qquad
\mathcal L_5=\partial_r^2+\frac3r\partial_r+\partial_z^2.
\]

It is not a validated free-space solver and is not a Navier--Stokes time evolution.

## Hosted execution provenance

The original S0/E0 subset passed on branch revision
`763dbc36812b5a2592f3784bda31c6db65b3ba31`, workflow run `34066171548`, job
`101575195688`. Its S0/E0 JSON bundle is artifact `9998999218`, digest
`sha256:8f84c3175537118f07112e3d67756fe7c043f964d42fada79daf2d28c6a29582`.

The completed E0 suite was rerun as a fail-closed precondition of the nonlinear E1 workflow at
exact revision

```text
dd8b06af0837b40eb221b7a54bb22b5211d76f1a
```

in workflow `R3 axisymmetric swirl nonlinear E1`, run `34075898846`, job
`101601815270`, on Ubuntu 24.04 / CPython 3.12.14 / NumPy 2.5.3 / SciPy 1.18.1.
The S0 check, the full E0 manufactured check, and the new low-axial-frequency E0 stress all
completed successfully before E1 was allowed to run.

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

On the fixed box `Rmax=1`, `Zmax=1.2`, supplying the exact free-space value on the artificial
boundary gave:

```text
nr x nz     Linf error       physical-L2 error   grad-r Linf      grad-z Linf
24 x 48     8.915891e-05     1.406497e-05        1.060627e-04     2.287388e-04
48 x 96     2.230217e-05     3.509820e-06        2.630415e-05     5.797777e-05
96 x 192    5.576249e-06     8.771593e-07        6.563718e-06     1.464473e-05
```

All field and first-derivative errors fall by approximately a factor four under each
`h -> h/2` refinement. The final sparse-solve algebraic residual is below `1e-10` by the
preregistered gate.

## Test 2 — independent 5D Green-reference cross-check

The code independently evaluates the axis value with

\[
G_5(X)=\frac1{8\pi^2|X|^3}
\]

and adaptive quadrature, without using the incomplete-gamma radial closed form. At the four
predeclared axis points the maximum absolute difference from the closed radial formula was

```text
1.734723e-18
```

in the hosted run. This is a floating-point reference cross-check, not an interval enclosure of
the free-space tail.

## Test 3 — artificial-boundary sensitivity with independent R/Z enlargement

For the same Gaussian source, replace the exact outer values by zero and hold mesh scale near
`0.02`. Errors are measured only on the fixed inner core `r<=0.45`, `|z|<=0.45`.

Square enlargement:

```text
Rmax=Zmax   core Linf        core physical-L2
0.60        8.925662e-04     5.793057e-04
0.80        3.634461e-04     2.516174e-04
1.00        1.834061e-04     1.299995e-04
1.50        5.440832e-05     3.841492e-05
```

Radial-only enlargement with `Zmax=1.5`:

```text
Rmax        core Linf        core physical-L2
0.60        8.861399e-04     5.511049e-04
0.80        3.583905e-04     2.414275e-04
1.00        1.801834e-04     1.253874e-04
1.50        5.440832e-05     3.841492e-05
```

Axial-only enlargement with `Rmax=1.5`:

```text
Zmax        core Linf        core physical-L2
0.60        5.090204e-04     2.094855e-04
0.80        1.579707e-04     8.757776e-05
1.00        8.079205e-05     5.385571e-05
1.50        5.440832e-05     3.841492e-05
```

Every sequence is strictly decreasing. This separates radial and axial artificial-boundary
sensitivity at the diagnostic level. It still does not constitute a rigorous truncation bound.

## Test 4 — low-axial-frequency nonperiodic stress

To close the explicit E0 contract item that forbids a periodic Fourier gap from masquerading as
whole-space decay, use the broad-axial manufactured function

\[
\psi(r,z)=\exp(-r^2/0.20^2-z^2/0.80^2),
\]

with characteristic axial wavenumber about `1.25`, strictly nonperiodic `z`, `Rmax=1`,
`Zmax=1.5`, and `dr=dz`.

Hosted results:

```text
nr x nz     Linf error       physical-L2 error   grad-r Linf      grad-z Linf
24 x 72     1.863085e-02     3.924640e-03        3.440596e-02     1.731839e-02
48 x 144    4.674823e-03     9.715771e-04        8.475638e-03     4.520622e-03
96 x 288    1.169752e-03     2.423991e-04        2.120715e-03     1.142561e-03
```

The field and first derivatives again show clear second-order reduction, and the final `Linf`
passes the preregistered `2e-3` prototype threshold.

## Test 5 — recovery of preregistered compact seed R3S04

For `R3S04`, the exact `psi1` is compactly supported strictly inside `Rmax=0.7`, `Zmax=0.6`, so
zero Dirichlet data are the exact manufactured boundary values. Solving from its derived
`omega1=-L5 psi1` gave:

```text
nr x nz      Linf error       physical-L2 error   grad-r Linf      grad-z Linf
 96 x 192    7.308551e-03     1.765296e-03        1.904902e-01     1.144527e-01
128 x 256    1.979607e-03     4.506337e-04        5.943835e-02     3.089505e-02
160 x 320    3.449917e-04     7.262881e-05        3.950929e-02     9.721878e-03
```

All audited field and first-derivative errors decrease monotonically. The sharp compact bump is
not yet being treated as asymptotically resolved merely because this first ladder passes.

## Prototype decision

```text
R3-E0-GAUSSIAN-SPATIAL-REFINEMENT = PASS
R3-E0-FIRST-DERIVATIVE-RECOVERY = PASS
R3-E0-GREEN-REFERENCE-CROSSCHECK = PASS (floating-point, not interval)
R3-E0-INDEPENDENT-R/Z-DOMAIN-SENSITIVITY = PASS as diagnostic
R3-E0-LOW-AXIAL-FREQUENCY-STRESS = PASS
R3-E0-COMPACT-R3S04-RECOVERY = PASS
R3-E0-HOSTED-REVISION-CERT = PASS on dd8b06af0837b40eb221b7a54bb22b5211d76f1a
R3-E0-RIGOROUS-FREE-SPACE-TAIL-ENCLOSURE = NOT DONE
```

The E0 prototype gate is therefore complete enough to permit the short E1 nonlinear integrator
smoke. It is not enough to call the elliptic solver a validated free-space inversion.

## Nonclaims

No finite-time singularity, nonextendability, continuum-convergence theorem, global regularity
statement, rigorous free-space tail enclosure, or Clay A/B/C/D result is established.
