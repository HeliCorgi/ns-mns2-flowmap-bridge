# R3 W1 resolution-aware early-time nonlinear dynamic audit — result

Date: 2026-09-07 JST

## Production execution

```text
revision: 4dc9280a3acd3ffbea0385227b300f9f1e6b625c
workflow: R3 W1 resolution-aware early-time dynamic audit
run: 34118648031
conclusion: success
artifact: r3-w1-dynamic-resolution
artifact id: 10017290874
sha256:4733aadc720f678bf4bf59b91c05ebca8741ea1769b87e848f076987a8b96cec
```

Exact machine decision:

```text
R3-W1-DYNAMIC-RESOLUTION = PASS
```

## R0 — runtime / Poisson

All five frozen RK4 runs passed the all-step runtime gate:

```text
B22 h=.04
B22 h=.02
B22 h=.01
B44 h=.04
B44 h=.02
```

Each completed exactly eight accepted steps with zero rejects and passed finite, frozen-symbol, CFL, viscous, Poisson, parity, energy, and energy-balance checks.

Final receiver Poisson residuals remained

```text
B22 h=.04  1.0444829747582494e-14
B22 h=.02  4.0416859510370340e-14
B22 h=.01  1.5496507767856469e-13
B44 h=.04  1.1055557802966425e-14
B44 h=.02  4.0554838117759250e-14
```

well below the frozen `1e-10` threshold.

## R1 — nonlinear state refinement

On the common core `r<=.8, |z|<=.8`, the combined final `(u1,omega1)` differences on B22 were

```text
S42 = rel(h=.04,h=.02) = 7.057219708372904e-7
S21 = rel(h=.02,h=.01) = 1.7021651156185794e-7
fine/coarse             = 0.24119485944288768
```

against the preregistered `<=.35` requirement.

## R2 — recovered meridional velocity refinement

For the four frozen receivers, using each run's own final `omega1 -> psi1 -> (u^r,u^z)` recovery,

```text
V42 = rel(h=.04,h=.02) = 6.551584604593220e-3
V21 = rel(h=.02,h=.01) = 1.6396232023826447e-3
fine/coarse             = 0.2502636081709345
```

again essentially the expected second-order `.25` reduction.

## R3 — box sensitivity subordinate to discretization

Measured `.04/.02` resolution corrections were

```text
state B22 = 7.057219708372904e-7
state B44 = 7.057219712535564e-7
state max = 7.057219712535564e-7

velocity B22 = 6.551584604593220e-3
velocity B44 = 6.562378355421767e-3
velocity max = 6.562378355421767e-3
```

At `h=.02`, B22-vs-B44 sensitivity was

```text
state    = 7.473374277931369e-14
state / resolution    = 1.0589686282058924e-7

velocity = 2.067786468770045e-3
velocity / resolution = 0.31509711217148306
```

so both frozen subordinate-to-resolution tests passed, including the binding velocity requirement `<=.50`.

For context only, the recovered-velocity box difference is stable rather than vanishing with refinement:

```text
h=.04 B22-vs-B44 velocity = 2.0780619015523475e-3
h=.02 B22-vs-B44 velocity = 2.0677864687700450e-3
```

which is consistent with a genuine finite-box effect that is nevertheless smaller than the measured spatial discretization correction over this early-time hierarchy.

## Interpretation / next gate

This PASS closes the short-time **implementation / resolution / early-boundary preflight stack** for the frozen `alpha=16, kappa=1` datum at `T=2e-4`.

It does not prove continuum convergence or a whole-space evolution theorem, and it does not erase the stopped PR #114 fixed-grid A4 result. What it establishes is narrower: the nonlinear state and the elliptically recovered meridional velocity both exhibit the preregistered second-order refinement behavior, while the residual B22-vs-B44 early-time boundary effect is subordinate to the measured discretization correction.

A separately preregistered **candidate-time pilot** may now be designed. That pilot must remain diagnostic, use matched resolutions, retain streaming stability/finite/Poisson/parity/energy diagnostics, and re-audit domain sensitivity at its later checkpoint before interpreting any growth.

## Parent statuses

```text
PR #112 dynamic-domain v1      = STOP_REPAIR_GREEN_QUADRATURE
PR #113 Green repair           = PASS
PR #114 dynamic-domain v2      = STOP_REPAIR_DYNAMIC_DOMAIN
PR #115 elliptic decomposition = PASS
PR #116 dynamic resolution     = PASS
```

## Nonclaims

This result is not a continuum theorem, not a rigorous whole-space truncation enclosure, not a long-time production evolution, not evidence of finite-time blow-up or global regularity, and not a Clay A/B/C/D result.
