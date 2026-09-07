# R3 alternate-datum R3S02 qualification result — 2026-09-07

**Classification:** `NUMERICAL CANDIDATE INFRASTRUCTURE / SINGLE ALTERNATE DATUM QUALIFICATION`.

This record reports the single alternate-datum qualification that was preregistered after the
bounded R3S04 E2R rescue failed. The datum `R3S02` was selected before any R3S02 Navier--Stokes
evolution from the already-frozen continuum geometry, not from evolution output.

The qualification keeps the same equations, viscosity, physical time, SSPRK3 integrator,
centered second-order finite differences, strictly nonperiodic `z`, zero artificial outer
Dirichlet condition, common comparison region, 15 comparison fields, norms, and numerical
thresholds used by the bounded E2R contract.

## Frozen datum

```text
name  R3S02
index 2
s0    0.04
ws    0.05
wz    0.28
zu    0.00
Au    1.0
Apsi  0.10
nu    0.002
T     0.02
```

## Hosted provenance

```text
workflow  R3 axisymmetric swirl R3S02 qualification
run       34081115069
job       101616428611
head      b2eaa219e69bc6ed0905334a61ccbfe757ca139d
runner    Ubuntu 24.04
python    CPython 3.12.14
numpy     2.5.3
scipy     1.18.1
artifact  10003744205
digest    sha256:d70b9951b74478b28a363f7ec1b0f40a671ea92df5731918099dd3a6090d52b4
NPZ sha   a2619b491089d3c27a6056ceaefc6fcb24d82f47f8c10aa7265c2ce2c718868f
```

The workflow conclusion is `failure` because the preregistered scientific qualification exits
nonzero on any failed gate. The result artifact uploaded successfully; exact NPZ reload passed.

## Datum-specific elliptic A0 preflight — FAIL

Before evolution, the exact compact R3S02 `psi1` was recovered from its analytically derived
`omega1=-L5 psi1` on the frozen B160/B200/B240 ladder:

```text
nr x nz      psi Linf        physical-L2      grad-r Linf     grad-z Linf
160 x 288    2.262678e-03    5.879217e-04     9.641115e-02    2.310976e-02
200 x 360    5.539511e-04    1.551987e-04     6.983862e-02    5.599508e-03
240 x 432    6.695558e-04    1.959785e-04     3.382518e-02    6.821861e-03
```

The field `Linf`, physical-L2, and axial-gradient error improve from B160 to B200 and then worsen
at B240. The preregistration required strict decrease of every field/derivative error metric
through the full ladder, so

```text
R3S02-DATUM-SPECIFIC-ELLIPTIC-A0 = FAIL
```

No evolution behavior may override this fail-closed preflight.

## Evolution diagnostics

All six evolution runs independently passed the inherited E1 smoke gates. Resolution diagnostics
on the base spatial ladder were

```text
run    min gradient scale (grid points)    max curvature-tail
B160           1.527155                        1.051174
B200           1.792440                        0.958943
B240           2.000000                        0.941021
```

Thus the narrow-scale and curvature diagnostics satisfy the frozen B240 endpoint thresholds and
move monotonically in the required directions for this datum.

The common-grid comparison extrema were

```text
pair             max relative Linf      max relative physical-L2
B160 -> B200      8.082699e-02           8.860458e-02
B200 -> B240      5.454146e-02           4.797364e-02
B240 -> B240H     1.039099e-06           1.028117e-06
B200 -> RPLUS2    9.372675e-06           2.970646e-05
B200 -> ZPLUS2    9.437620e-06           2.665646e-05
```

Time discretization and one-coordinate domain sensitivities are comfortably subdominant on this
short trajectory. Most field/norm spatial comparisons improve on the fine pair, but two frozen
relative-Linf comparisons do not:

```text
omega1_z:  fine=5.100540601958e-02 >= coarse=4.053091238257e-02
utheta_r:  fine=1.107671625969e-02 >= coarse=9.480117437666e-03
```

No field is deleted and no inequality is weakened after observing the result.

## Exact decision

The complete preregistered failure set is therefore:

```text
1. R3S02 datum-specific elliptic preflight A0 FAIL
2. spatial omega1_z relative_linf fine >= coarse
3. spatial utheta_r relative_linf fine >= coarse
```

so the bounded decision is

```text
R3S02-ALT-DATUM-QUALIFICATION = FAIL
CURRENT-12-SEED-CENTERED-FD-QUALIFICATION-PATH = PARK
R3-MULTI-SEED-SCREEN = NOT LICENSED
```

The no-seed-shopping rule now applies: do not test R3S00/R3S06/etc one by one under the same
centered-second-order / zero-Dirichlet stack in search of a passing datum.

## What the failure says and does not say

The failure is informative about the numerical method: although the nonlinear short-time field
comparisons, time refinement, domain enlargement, and narrow-scale diagnostics are substantially
better for R3S02 than for the original R3S04 lattice, the datum-specific manufactured elliptic
recovery is not monotonically convergent on the frozen ladder and two first-derivative comparison
metrics also fail. The current finite-difference qualification path therefore stops before any
candidate-growth screen.

This does **not** refute R3S02 as a continuum Navier--Stokes datum, prove regularity, or rule out
singular behavior. It is a numerical qualification failure of the tested finite-resolution stack.
No Clay A/B/C/D conclusion follows.

## Next allowed direction

The next allowed numerical direction is a **genuinely new numerical-method contract**, starting
again from manufactured elliptic/derivative tests before any nonlinear candidate evolution. A
new method must not inherit qualification merely from the current centered-FD results.
