# R3 axisymmetric-with-swirl seed S0 audit — 2026-09-07

**Classification:** `NUMERICAL CANDIDATE INFRASTRUCTURE / S0 ONLY`.

This result concerns only the explicit compact seed formulas and reconstruction checks in `compact_family.py`. There is no Navier–Stokes time evolution in S0.

## Revision-qualified execution

Workflow:

```text
R3 axisymmetric swirl seed and E0 prototype
run 34066171548
job 101575195688
execution head 763dbc36812b5a2592f3784bda31c6db65b3ba31
conclusion SUCCESS
Python 3.12.14
NumPy 2.5.3
SciPy 1.18.1
```

Result artifact:

```text
name   r3-axisym-swirl-seed-e0-results
id     9998999218
digest sha256:8f84c3175537118f07112e3d67756fe7c043f964d42fada79daf2d28c6a29582
```

The artifact contains the exact generated S0 and E0 `summary.json` files for this revision.

All 12 preregistered continuum seeds passed the static S0 gate:

```text
n_pass = 12 / 12
```

Representative final-step independent finite-difference errors (`h=2.5e-4`) are:

```text
seed   Cartesian divergence    -L5 psi1 vs omega1
R3S00  1.614911e-06            1.508803e-05
R3S02  2.155263e-06            6.977115e-06
R3S04  6.696674e-06            3.193329e-05
R3S06  5.602529e-06            1.799140e-05
R3S08  1.381117e-05            7.728578e-05
R3S10  1.042872e-05            4.764523e-05
```

The `zu=0.08` partners have the same poloidal/elliptic errors because `psi1` is unchanged by `zu`; their swirl packet is axially shifted.

For every seed in the hosted execution:

- analytic cylindrical divergence cancellation was at floating roundoff (`<=1.7764e-15`);
- axis odd physical components audited here were exactly zero in floating arithmetic;
- support-leak probes were exactly zero;
- nested-grid shared-coordinate differences for `u1`, `psi1`, and `omega1` were zero in floating arithmetic;
- kinetic energy with physical `2*pi*r dr dz` quadrature was finite and positive;
- the swirl probe was nonzero.

The physical-energy values range from

```text
9.980956e-04  to  7.235429e-03
```

for the frozen first amplitudes `Au=1`, `Apsi=0.1`. These unequal energies are intentional at S0: this lattice is a geometry/pipeline audit, not an amplitude-controlled competition between seeds.

## Mathematical construction boundary

The continuum formulas are analytically `C_c^infty` because the primitive bump is `C_c^infty` and the radial dependence is through `s=r^2`. The reconstructed Cartesian field is compactly supported and smooth at the axis. The floating arrays produced in S0 are samples of those formulas and are not themselves formal proof objects.

`omega1` is not chosen independently: it is defined from the explicit `psi1` by

\[
\omega_1=-(4s\psi_{1,ss}+8\psi_{1,s}+\psi_{1,zz})=-\mathcal L_5\psi_1.
\]

Thus this family supplies a manufactured exact pair for the nonperiodic elliptic inversion gate.

## Decision

```text
R3-SEED-S0-FORMULA-AUDIT = PASS
R3-SEED-S0-HOSTED-REVISION-CERT = PASS at 763dbc36812b5a2592f3784bda31c6db65b3ba31
R3-WHOLE-SPACE-EVOLUTION = NOT STARTED
```

S0 establishes only explicit smooth compact axisymmetric-with-swirl seed construction plus numerical reconstruction/audit success. It does not identify a singular trajectory.

## Nonclaims

This does not establish a numerical blow-up candidate, finite-time singularity, nonextendability, global regularity, or Clay A/B/C/D.