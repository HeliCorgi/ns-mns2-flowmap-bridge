# R3 W1 recovered-divergence diagnostic repair — preregistration (2026-09-07)

**Status:** frozen before repair-gate production output. This is a diagnostic repair after the stopped W1 manufactured-v1 gate. It does not change the v1 decision and makes no amplification, singularity, regularity, continuum-convergence, or Clay A/B/C/D claim.

## 1. Why this gate exists

W1 manufactured-v1 failed only the preregistered requirement

```text
max relative recovered divergence <= 1e-10.
```

The failed run showed approximately second-order reduction rather than roundoff cancellation. Post-run algebra identified the reason: with independently differentiated centered differences, the continuum streamfunction identity is not an exact discrete product-rule identity.

For an interior uniform radial grid, centered `D_r,D_z`, `q=D_z psi`, and

```text
u_r = -r q,
u_z = 2 psi + r D_r psi,
```

one has exactly on the common centered interior stencil

```text
D_r(r q)_i = r_i D_r q_i + (q_{i+1}+q_{i-1})/2,
```

and, because centered `D_r` and `D_z` commute there,

```text
D_r u_r + u_r/r + D_z u_z
  = q_i - (q_{i+1}+q_{i-1})/2
  = -(h^2/2) D_rr q_i.
```

Thus an independently reconstructed divergence residual is generically `O(h^2)`, while a streamfunction-compatible commutator check may still cancel to roundoff. This repair gate validates those two facts separately before any manufactured-v2 nonlinear gate is designed.

## 2. Frozen manufactured streamfunctions

Use the compact bump

```text
b(s)=exp(-s/(1-s)), 0<=s<1; 0 otherwise.
```

On the fixed box

```text
0 <= r <= 2,
-2 <= z <= 2,
```

use two smooth compact streamfunctions:

```text
P-even: psi(r,z) = b(r^2) b(z^2)
P-odd:  psi(r,z) = b(r^2) z b(z^2).
```

Both are even in signed `r` and compactly supported in `r<1, |z|<1`.

Freeze aligned grids

```text
h = 0.08, 0.04, 0.02.
```

All acceptance comparisons use the common diagnostic core

```text
0.16 <= r <= 0.80,
|z| <= 0.80.
```

The axis itself is intentionally excluded because the failed v1 quantity was the ordinary cylindrical divergence formula containing `u_r/r`; the axis has a separate regular limit.

## 3. Frozen discrete operators

Use the same centered interior operators as W1 manufactured-v1:

```text
D_r f_i,j = (f_{i+1,j}-f_{i-1,j})/(2h)
D_z f_i,j = (f_{i,j+1}-f_{i,j-1})/(2h).
```

Reconstruct

```text
q   = D_z psi
u_r = -r q
u_z = 2 psi + r D_r psi.
```

Define the independently differentiated divergence

```text
div_ind = D_r u_r + u_r/r + D_z u_z.
```

Define the predicted centered-product-rule defect

```text
div_pred = q_i - (q_{i+1}+q_{i-1})/2.
```

Define the streamfunction-compatible commutator residual

```text
div_compat = r*(D_z D_r psi - D_r D_z psi).
```

No quantity is silently substituted for another: `div_ind` is the independent physical reconstruction diagnostic; `div_pred` is its exact discrete identity; `div_compat` tests commutation/algebraic compatibility.

## 4. D1 — exact discrete-defect identity

On the frozen core, for each profile and each grid, require

```text
||div_ind-div_pred||_inf / max(||div_ind||_inf, ||div_pred||_inf, 1e-30)
  <= 1e-10.
```

This is an algebraic implementation check. Failure means the diagnosis of manufactured-v1 was incomplete or the diagnostic code is not reproducing the same stencil.

## 5. D2 — second-order independent-divergence refinement

Normalize the independent divergence by the size of the three cylindrical-divergence terms:

```text
rel_div = ||div_ind||_inf /
          max(||D_r u_r||_inf + ||u_r/r||_inf + ||D_z u_z||_inf, 1e-30)
```

with every norm taken on the frozen core.

For each profile require strict decrease and

```text
rel_div(h=.04) <= 0.35 * rel_div(h=.08)
rel_div(h=.02) <= 0.35 * rel_div(h=.04).
```

The factor `0.35` is frozen before output and is deliberately looser than the ideal second-order factor `0.25`.

## 6. D3 — leading truncation term

For `psi=f(r)g(z)` with `f(r)=b(r^2)`,

```text
f_rr = 2 b'(r^2) + 4 r^2 b''(r^2).
```

Since `q=psi_z=f g_z`, the continuum leading term predicted by the exact discrete identity is

```text
div_ind / h^2 -> -(1/2) * f_rr * g_z.
```

Use analytic `b'` and `b''` and the exact analytic `g_z` for each profile. Define the grid-Euclidean relative L2 error on the core between `div_ind/h^2` and this leading term.

Require strict decrease and

```text
lead_err(h=.04) <= 0.40 * lead_err(h=.08)
lead_err(h=.02) <= 0.40 * lead_err(h=.04).
```

No absolute tolerance is used here; the gate tests the predicted asymptotic structure rather than tuning to the failed v1 magnitude.

## 7. D4 — compatible roundoff check

For each profile and each grid define

```text
compat_rel = ||div_compat||_inf /
             max(||r D_z D_r psi||_inf + ||r D_r D_z psi||_inf, 1e-30).
```

Require

```text
compat_rel <= 1e-12.
```

This is the quantity expected to cancel to roundoff. It is not labeled an independent physical-divergence error.

## 8. Decision

Only if D1–D4 all pass for both manufactured profiles on all three grids:

```text
R3-W1-DIVERGENCE-DIAGNOSTIC-REPAIR = PASS.
```

Otherwise:

```text
R3-W1-DIVERGENCE-DIAGNOSTIC-REPAIR = STOP_REPAIR_DIAGNOSTIC.
```

A PASS does not retroactively change

```text
R3-W1-MANUFACTURED-v1 = STOP_REPAIR_W1_MANUFACTURED.
```

It only permits a separately versioned manufactured-v2 preregistration whose incompressibility acceptance distinguishes (a) independently differentiated `O(h^2)` truncation behavior from (b) roundoff-level compatible algebraic checks.
