# R3 W1 recovered-divergence diagnostic repair — result (2026-09-07)

**Status:** `R3-W1-DIVERGENCE-DIAGNOSTIC-REPAIR = PASS`.

This result validates the repaired diagnostic interpretation only. It does **not** retroactively change the stopped manufactured-v1 decision, and it makes no long-time amplification, singularity, regularity, continuum-convergence, or Clay A/B/C/D claim.

## Execution provenance

```text
revision: 21f994d779a401895fc2f3a8c37da90e82effcc7
workflow: R3 W1 divergence diagnostic repair
run: 34112298964
conclusion: success
artifact: r3-w1-divergence-diagnostic-repair
artifact id: 10014824733
sha256:cc44cb205dedc664d356d651d2aa57edd087f8ea6f78dd355b82ca65aa6474a0
```

Frozen preregistration:

`R3_AXISYM_WHOLESPACE_W1_DIVERGENCE_REPAIR_PREREG_2026-09-07.md`.

Exact decision:

```text
R3-W1-DIVERGENCE-DIAGNOSTIC-REPAIR = PASS
```

All D1–D4 checks passed for both manufactured profiles and all three frozen grids.

## D1 — exact centered defect identity

For the independently differentiated reconstruction

```text
q   = D_z psi
u_r = -r q
u_z = 2 psi + r D_r psi

div_ind = D_r u_r + u_r/r + D_z u_z
```

the preregistered predicted defect was

```text
div_pred = q_i - (q_{i+1}+q_{i-1})/2.
```

Worst relative `L∞` mismatch over all six manufactured rows:

```text
6.197347369817331e-12
```

below the frozen `1e-10` threshold.

## D2 — independent-divergence refinement

Relative independent divergence:

```text
even profile
h=.08  4.152511223945919e-3
h=.04  8.940481354390355e-4
h=.02  2.139589936967900e-4

odd profile
h=.08  4.152511223945876e-3
h=.04  8.940481354391210e-4
h=.02  2.139589936966544e-4
```

Ratios are approximately

```text
h=.04 / .08 : 0.2153
h=.02 / .04 : 0.2393
```

for both profiles, passing the preregistered `<=0.35` half-grid reduction rule.

## D3 — leading `h^2` truncation structure

The predicted continuum leading term was

```text
div_ind/h^2 -> -(1/2) f_rr g_z.
```

Relative grid-`L2` errors:

```text
even
h=.08  9.945016562029046e-2
h=.04  2.526958015828759e-2
h=.02  6.113386559346512e-3

odd
h=.08  1.023708632883646e-1
h=.04  2.601779071223724e-2
h=.02  6.299423824762443e-3
```

Each refinement is strict and satisfies the frozen `<=0.40` ratio rule.

## D4 — compatible commutator

The separately defined compatible residual

```text
div_compat = r (D_z D_r psi - D_r D_z psi)
```

cancels to roundoff. Worst normalized value:

```text
1.0667838413545287e-15
```

below the frozen `1e-12` threshold.

## Interpretation

The repair confirms three distinct facts that must not be conflated:

1. continuum incompressibility is exact for the streamfunction reconstruction;
2. independently reconstructing velocity and then applying centered cylindrical divergence creates a deterministic `O(h^2)` product-rule truncation term;
3. a discretely compatible commutator construction cancels algebraically to roundoff.

The manufactured-v1 requirement `relative recovered divergence <= 1e-10` incorrectly demanded fact (3) from diagnostic (2). The repair establishes the correct discrete behavior; it does not erase the v1 failure.

Standing result:

```text
R3-W1-MANUFACTURED-v1 = STOP_REPAIR_W1_MANUFACTURED
```

## Next permitted gate

A separately versioned manufactured-v2 preregistration may preserve all v1 M1/M2/stability/Poisson/parity/energy/integrator/resolution conditions while replacing the invalid divergence row by two independently audited conditions:

- exact centered defect-identity agreement plus second-order refinement for the independently differentiated divergence;
- roundoff-level compatible commutator residual.

Only a new v2 execution can decide whether the short-time nonlinear manufactured gate passes under the repaired diagnostic.
