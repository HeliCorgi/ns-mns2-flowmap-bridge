# R3 axisymmetric-with-swirl seed S0 audit — 2026-09-07

**Classification:** `NUMERICAL CANDIDATE INFRASTRUCTURE / S0 ONLY`.

This result concerns only the explicit compact seed formulas and reconstruction checks in `compact_family.py`. There is no Navier–Stokes time evolution in S0.

## Execution status

An isolated Python/NumPy reproduction of the branch formulas and the preregistered S0 gate logic was run during construction. It is **not yet a hosted revision-qualified repository execution**; therefore the numbers below are development evidence, not a CI certificate.

All 12 preregistered continuum seeds passed the static gate in that reproduction:

```text
n_pass = 12 / 12
```

Representative final-step independent finite-difference errors (`h=2.5e-4`) were:

```text
seed   Cartesian divergence    -L5 psi1 vs omega1
R3S00  1.6149e-06              1.5088e-05
R3S02  2.1553e-06              6.9771e-06
R3S04  6.6967e-06              3.1933e-05
R3S06  5.6025e-06              1.7991e-05
R3S08  1.3811e-05              7.7286e-05
R3S10  1.0429e-05              4.7645e-05
```

The `zu=0.08` partners have the same poloidal/elliptic errors because `psi1` is unchanged by `zu`; their swirl packet is axially shifted.

For every seed in the isolated reproduction:

- analytic cylindrical divergence cancellation was at floating roundoff (`<=1.78e-15`);
- axis odd physical components audited here were exactly zero in floating arithmetic;
- support-leak probes were exactly zero;
- nested-grid shared-coordinate differences for `u1`, `psi1`, and `omega1` were zero in floating arithmetic;
- kinetic energy with physical `2*pi*r dr dz` quadrature was finite and positive;
- the swirl probe was nonzero.

The physical-energy values range from approximately

```text
9.980956e-04  to  7.235429e-03
```

for the first fixed amplitudes `Au=1`, `Apsi=0.1`. These unequal energies are intentional at S0: this first lattice is a geometry/pipeline audit, not a fair amplitude-controlled competition between seeds.

## Mathematical construction boundary

The continuum formulas are analytically `C_c^infty` because the primitive bump is `C_c^infty` and the radial dependence is through `s=r^2`. The reconstructed Cartesian field is compactly supported and smooth at the axis. The saved finite arrays used by future solvers are only samples of those formulas and require their own discretization audits.

`omega1` is not chosen independently: it is defined from the explicit `psi1` by

\[
\omega_1=-(4s\psi_{1,ss}+8\psi_{1,s}+\psi_{1,zz})=-\mathcal L_5\psi_1.
\]

Thus this family supplies a manufactured exact pair for the next free-space elliptic inversion gate.

## Decision

```text
R3-SEED-S0-FORMULA-AUDIT = PASS in isolated development reproduction
R3-SEED-S0-HOSTED-REVISION-CERT = NOT RUN
R3-WHOLE-SPACE-EVOLUTION = NOT STARTED
```

The next technical target is E0 in `R3_WHOLE_SPACE_SOLVER_CONTRACT_2026-09-07.md`: a genuinely nonperiodic/free-space approximation to `-L5 psi1=omega1` that recovers these manufactured pairs under spatial and domain refinement.

## Nonclaims

This does not establish a numerical blow-up candidate, finite-time singularity, nonextendability, global regularity, or Clay A/B/C/D.