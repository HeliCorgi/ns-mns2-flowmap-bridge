# R3 axisymmetric whole-space alpha-kappa family screen — result

Date: 2026-09-09 JST

## Production execution

```text
revision: ba8ccc63016ac97a4bfc43157707bbfafd3d1147
workflow: R3 alpha-kappa family screen
run: 34330169892
conclusion: success
artifact: r3-alpha-kappa-family-screen
artifact id: 10095803752
sha256:76692b74bbecca915d75efdf1d256237a211bfda7ed6b05ba952a85d8c1d055b
```

Exact machine decision:

```text
R3-FAMILY-SCREEN = PASS_NO_PROMOTIONS
```

All 12 preregistered rows were numerically valid and passed the B22/B44 domain veto. No row met either physical-growth promotion threshold, so the promotion set is empty and no high-resolution confirmation is opened from this screen.

## Frozen grid

```text
alpha = {16,32,64,128}
kappa = {.75,1.00,1.50}
T=.25, h=.08, dt=.002, RK4
B22 and B44 for every row
```

Promotion required both boxes independently to satisfy at least one of

```text
max physical enstrophy / initial >= 1.02
final physical-vorticity sup / initial >= 1.05
```

after all runtime and domain vetoes passed.

## Row summary

The B44 final diagnostics are:

| alpha | kappa | max enstrophy / initial | final enstrophy / initial | final vorticity sup / initial | classification |
|---:|---:|---:|---:|---:|---|
| 16 | .75 | 1.000000 | 0.7645711245 | 0.9215404383 | NO_GROWTH_TRIGGER |
| 16 | 1.00 | 1.000000 | 0.8053968488 | 0.9510482519 | NO_GROWTH_TRIGGER |
| 16 | 1.50 | 1.000000 | 0.8359278785 | 0.9647494496 | NO_GROWTH_TRIGGER |
| 32 | .75 | 1.000000 | 0.7646145515 | 0.9213279701 | NO_GROWTH_TRIGGER |
| 32 | 1.00 | 1.000000 | 0.8054315669 | 0.9508564016 | NO_GROWTH_TRIGGER |
| 32 | 1.50 | 1.000000 | 0.8359442884 | 0.9645918838 | NO_GROWTH_TRIGGER |
| 64 | .75 | 1.000000 | 0.7647882279 | 0.9204787960 | NO_GROWTH_TRIGGER |
| 64 | 1.00 | 1.000000 | 0.8055704277 | 0.9500895440 | NO_GROWTH_TRIGGER |
| 64 | 1.50 | 1.000000 | 0.8360099361 | 0.9639619675 | NO_GROWTH_TRIGGER |
| 128 | .75 | 1.000000 | 0.7654824286 | 0.9170932422 | NO_GROWTH_TRIGGER |
| 128 | 1.00 | 1.000000 | 0.8061256891 | 0.9470307889 | NO_GROWTH_TRIGGER |
| 128 | 1.50 | 1.000000 | 0.8362726584 | 0.9614478436 | NO_GROWTH_TRIGGER |

`max enstrophy / initial = 1` for every row means the maximum over the closed interval occurred at the initial time; none exhibited physical-enstrophy amplification above its initial value on this horizon.

## Domain and runtime audit

All 24 individual box runs completed 125 accepted steps with zero rejects and passed the frozen all-stage/all-step finite, stability, CFL, viscous, Poisson, parity, physical-energy, and energy-balance checks.

Worst domain-veto metrics across the 12 rows were

```text
max Sbox                         = 7.597116483473903e-6
max Vbox                         = 3.2365476928470954e-3
max |Emax_B22-Emax_B44|          = 0
max |Wfinal_B22-Wfinal_B44|      = 9.389977746243616e-6
```

against frozen limits `.01`, `.05`, `.01`, and `.02` respectively. Thus the absence of a trigger is not caused by a row being discarded for the screen's finite-box veto.

For context, the largest generated normalized toroidal-vorticity diagnostic was

```text
final max|omega1|/A = 0.15074196234560067
```

at `(alpha,kappa)=(128,.75)`. This is generated vorticity, not amplification of the physical-vorticity supremum; that row still ended at `0.9170932422` of its initial physical-vorticity supremum.

## Interpretation

Within this frozen 12-row grid, increasing `alpha` from 16 to 128 does not produce a preregistered physical-enstrophy or final physical-vorticity growth trigger through `T=.25`. The widest axial profile `kappa=1.5` is the least dissipative by the final ratios, but it still remains below the initial physical enstrophy and vorticity levels.

Therefore the preregistered rule sends **no row** to high-resolution confirmation. Running high-resolution confirmation anyway would violate the screen design.

This result does not prove regularity, does not exclude later-time growth, and does not exclude other compact datum shapes or parameter ranges. It only closes this particular frozen coarse family screen.

## Nonclaims

This is finite-resolution numerical evidence only. It is not a continuum whole-space theorem, not a rigorous tail enclosure, not evidence of finite-time blow-up or global regularity, and not a Clay A/B/C/D result.