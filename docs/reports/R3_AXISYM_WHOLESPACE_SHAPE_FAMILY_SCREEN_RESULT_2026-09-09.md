# R3 axisymmetric whole-space shape-family screen — result

Date: 2026-09-09 JST

## Production execution

```text
scientific revision: 9aad511ff4390f76fe2ab2d559d7b017acb432c3
workflow: R3 shape-family screen
run: 34337398611
conclusion: success
artifact: r3-shape-family-screen
artifact id: 10098663473
sha256:3893ad27df1494e2817f2304ff963826e366d2fc6e07f069828abbf719e55c61
```

Exact machine decision:

```text
R3-SHAPE-FAMILY-SCREEN = PASS_NO_PROMOTIONS
promotion_set = []
```

This is a finite-resolution triage result only.

## Frozen rows

The gate tested

```text
alpha={64,128}
kappa=.75
radial={C centered, A annular}
axial={Z0 base, Z1 concentrated, Z2 signed/shouldered}
T=.25, h=.08, dt=.002, RK4
B22 and B44 for every row
```

for 12 shape/amplitude rows and 24 box evolutions.

## Valid centered-profile rows

All six centered radial rows (`C-Z0`, `C-Z1`, `C-Z2` at both alphas) passed the complete runtime gate and matched B22/B44 domain veto.

For all six,

```text
max physical enstrophy / initial = 1.0
```

in both boxes. Their final physical-vorticity-sup ratios were below one:

```text
alpha=64
  C-Z0  B22 .9204795247254955   B44 .9204787960153245
  C-Z1  B22 .9107040140228462   B44 .9107036718927858
  C-Z2  B22 .8871256578427587   B44 .8871255069926691

alpha=128
  C-Z0  B22 .9170961464556694   B44 .9170932422343306
  C-Z1  B22 .9088111899041987   B44 .9088098242307857
  C-Z2  B22 .8869697382165086   B44 .8869699444310135
```

Thus none of the two new **axial** shape variants produced the preregistered physical-growth trigger on the centered radial profile.

The centered-row domain sensitivities remained small. The worst centered values were approximately

```text
state B22/B44 relative difference    5.8912e-6
velocity B22/B44 relative difference 1.9209e-3
```

well inside the frozen `.01` and `.05` vetoes.

## Annular rows — INVALID_RUNTIME, not negative growth evidence

All six annular rows (`A-Z0`, `A-Z1`, `A-Z2` at both alphas) completed 125 accepted steps with zero rejects. Frozen-symbol amplification, CFL, viscous number, finiteness, Poisson residual, odd parity, physical-energy monotonicity, and final Poisson checks passed.

However, every annular row failed the **preregistered stepwise physical energy-balance defect `<=.20`**. The worst defects were nearly amplitude- and box-independent:

```text
A-Z0  ~.27694 to .27695
A-Z1  ~.25903
A-Z2  ~.25263
```

while physical energy itself remained decreasing (`max E/E0 < 1`). Therefore these rows are classified exactly as

```text
INVALID_RUNTIME
```

and are **not** evidence that annular shapes have no growth. Their descriptive growth ratios are not promoted or used to kill the annular family.

This pattern is consistent with a coarse-grid energy-balance discretization issue for the sharper annular radial envelope, but that interpretation is only a hypothesis until a separately preregistered resolution audit verifies it.

## Descriptive generated omega1

Among valid centered rows, the largest generated normalized toroidal-vorticity scale remained the base axial profile at `alpha=128`:

```text
C-Z0, alpha=128:
final max|omega1| / Acoef = 0.15074271278478357
```

The new centered axial profiles generated less normalized `omega1` and also had smaller final physical-vorticity ratios. This is descriptive mechanism evidence only.

## Scientific interpretation

The screen resolves two different questions:

1. **Centered radial profile:** changing the axial profile to the preregistered concentrated or signed/shouldered variants does not produce a physical enstrophy/vorticity growth trigger through `T=.25` at `alpha=64,128`, `kappa=.75`.
2. **Annular radial profile:** the coarse `h=.08` screen is inconclusive because all annular rows fail the frozen energy-balance diagnostic before growth classification.

Accordingly, there are no high-resolution growth promotions from this screen. The next smallest gate is not a post-hoc annular growth run; it is a preregistered **annular energy-balance resolution audit** that asks whether the `.20` runtime failure converges away under spatial/time refinement while leaving the physical equations and diagnostic formula unchanged.

Fable5 P0-D remains open for any future positive growth row: no grid-scale or resolved-growth language is permitted without explicit scale diagnostics and matched refinement.

## Nonclaims

This result is not a continuum theorem, not rigorous whole-space tail control, not evidence of finite-time breakdown, not evidence of global regularity, and not a Clay A/B/C/D result.
