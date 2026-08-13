# MNS-2 v2.11 — path-correction POD reduced bridge report

Date: 2026-08-13 JST

## Verdict

**`PATH-CORRECTION-POD-BRIDGE-AUDIT-COMPLETE`** on the synthetic 12x24 frozen discrete map.

The rank-2 physical-energy POD approximation of the **path-specific nonlinear tangent correction** produces a reduced radial bridge whose final 12-panel composite Gauss-4 endpoint error is about

- **`7.00e-9` relative to the direct frozen-map endpoint difference**,

while the fully evaluated tangent bridge at the same quadrature has relative endpoint error

- **`4.32e-9`**.

The reduced-vs-full-tangent integral difference is `5.89e-9` relative to the direct endpoint norm, while the quadrature estimate of the integrated pointwise residual is `1.25e-8`. Their ratio is about `0.472`, consistent with the triangle-inequality residual certificate formalized separately in Lean.

This is a **finite-discrete path-specific audit**, not a continuum Navier--Stokes theorem, not a universal rank-2 solution map, and not Hou late-state evidence.

## Object being compressed

The full short-time derivative is known from the earlier derivative audit to contain a datum-independent identity/Stokes-like component and is not low rank. The target is therefore exactly the nonlinear correction needed by the radial bridge:

\[
 c(\lambda)=\bigl(J_T(\lambda y_0)-J_T(0)\bigr)[y_0].
\]

For a POD projector `P_r` learned from coarse amplitude snapshots, v2.11 evaluates

\[
 q_r(\lambda)=J_T(0)[y_0]+P_r c(\lambda).
\]

The exact discrete radial tangent is

\[
 g(\lambda)=J_T(\lambda y_0)[y_0].
\]

The reduced endpoint is obtained from `∫ q_r(λ)dλ`. The pointwise residual

\[
 r_r(\lambda)=g(\lambda)-q_r(\lambda)
\]

is retained explicitly rather than discarded.

## Configuration

- synthetic two-component v2.2 bridge seed; explicitly **not** Hou late-state evidence
- grid: `12x24`
- viscosity: `nu=5e-3`
- `dt=2e-8`
- SSPRK3 steps: `2`
- physical time: `T=4e-8`
- common frozen schedule: `alpha_r=alpha_z=100`, `eps_g=eps_o=1e-6`
- fixed unnormalized path direction: `y0`
- physical-energy metric for POD, projection, and residual norms
- POD training amplitudes: `0.25, 0.5, 0.75, 1.0`
- quadrature: composite Gauss--Legendre order 4 per panel
- panel ladder: `2,4,6,8,12`

Direct endpoint-difference metric norm: `0.8948215172977055`.

Zero-base tangent norm `||J_T(0)[y0]||_E`: `0.8948218204818902`.

The nonlinear correction is tiny at this short time. Across the four training amplitudes,

- `||c(lambda)||_E ≈ 2.16e-6 ... 2.22e-6`,
- `||c(lambda)||_E / ||g(lambda)||_E ≈ 2.42e-6 ... 2.48e-6`.

Therefore this test is structural validation of the reduced formula, not evidence of a strong nonlinear or near-singular regime.

## POD audit

The correction snapshot singular values normalized by the leading value are approximately

`1, 6.14955e-2, 9.62573e-4, 2.10612e-4`.

The metric Gram error of the first three reconstructed POD vectors is `8.79e-13`.

This basis is tied to the single radial path and tangent `y0`. It is not a universal initial-data basis.

## Quadrature ladder

### Full tangent bridge

| panels | nodes | rel. endpoint error vs direct | drift from previous |
|---:|---:|---:|---:|
| 2 | 8 | `4.84e-9` | — |
| 4 | 16 | `4.01e-9` | `4.09e-9` |
| 6 | 24 | `4.32e-9` | `2.45e-9` |
| 8 | 32 | `4.52e-9` | `1.41e-9` |
| 12 | 48 | `4.32e-9` | `1.67e-9` |

The sequence is not strictly monotone. The panel ladder is retained as a convergence diagnostic rather than selecting one formal order and declaring it exact.

### Rank-2 reduced bridge

| panels | endpoint error vs direct | reduced-vs-full integral | integrated residual estimate | triangle ratio | drift |
|---:|---:|---:|---:|---:|---:|
| 2 | `5.75e-9` | `7.68e-9` | `1.05e-8` | `0.731` | — |
| 4 | `6.10e-9` | `6.60e-9` | `9.92e-9` | `0.665` | `1.53e-9` |
| 6 | `6.59e-9` | `6.29e-9` | `1.09e-8` | `0.575` | `1.16e-9` |
| 8 | `6.90e-9` | `6.08e-9` | `1.18e-8` | `0.516` | `5.82e-10` |
| 12 | `7.00e-9` | `5.89e-9` | `1.25e-8` | `0.472` | `1.86e-10` |

Here “integrated residual estimate” means the **same composite quadrature** applied to

\[
\int_0^1\|g(\lambda)-q_2(\lambda)\|_E\,d\lambda.
\]

It is numerical evidence compatible with the analytic inequality; it is not itself a rigorous interval bound.

### Rank comparison at 12 panels

| rank | endpoint error vs direct | reduced-vs-full integral | integrated residual estimate |
|---:|---:|---:|---:|
| 1 | `6.86e-8` | `6.91e-8` | `1.45e-7` |
| 2 | `7.00e-9` | `5.89e-9` | `1.25e-8` |
| 3 | `6.10e-9` | `4.76e-9` | `1.07e-8` |

Rank 2 captures essentially all of the useful improvement available at this short synthetic window; rank 3 improves the reduced-vs-full integral modestly but the total endpoint error is already comparable to the underlying tangent-quadrature error.

## Reduced coefficient formula

At 12 panels the integrated rank-2 POD coefficients are approximately

\[
\int_0^1 a_1(\lambda)d\lambda=-2.17810418\times10^{-6},
\]

\[
\int_0^1 a_2(\lambda)d\lambda=-6.15884092\times10^{-8}.
\]

Thus the tested discrete reduced bridge has the explicit form

\[
S_T(y_0)-S_T(0)
\approx
J_T(0)[y_0]
+\phi_1\!\int_0^1 a_1(\lambda)d\lambda
+\phi_2\!\int_0^1 a_2(\lambda)d\lambda,
\]

with the tangent residual kept as a separate error budget.

The corresponding Lean theorem now proves, for an exact local `C¹` bridge and any interval-integrable approximation `q`,

\[
\left\|(S(d)-S(0))-\int_0^1 q(s)ds\right\|
\le
\int_0^1\|DS(sd)[d]-q(s)\|ds.
\]

## What v2.11 establishes

For this one frozen discrete map and one synthetic radial path:

1. separating the zero-base linear reference from the nonlinear correction is numerically coherent;
2. the path-specific correction family has a strongly dominant two-dimensional POD subspace;
3. integrating the rank-2 projected tangent gives an endpoint reconstruction at roughly `7e-9` relative error;
4. the observed reduced-vs-full integral error stays below the quadrature estimate of the integrated pointwise residual on every tested panel level;
5. the reduced integral itself is quadrature-stable at the `~2e-10` level between 8 and 12 panels.

## What v2.11 does not establish

It does **not** establish:

- a rank-2 full Fréchet derivative;
- a rank-2 universal solution map;
- a predictor that avoids evaluating the true JVP at certification nodes;
- a rigorous numerical upper bound on the residual integral;
- a continuum limit;
- a transfer from the finite cylindrical MNS/Hou setting to Clay `R^3` or `T^3`;
- a singularity, blow-up, or Clay A/B/C/D result.

## New fail-closed rules

- **FC-077:** a quadrature estimate of `∫||r||` is called a rigorous residual certificate without a quadrature/interval error bound;
- **FC-078:** projection using true JVP values at every quadrature node is called a predictive low-cost reduced model.

## Next step

The useful next split is now clear:

1. **Lean:** specialize the general integrated-residual theorem to a linear reference plus a finite-rank correction basis;
2. **numerics:** build a predictive coefficient model `a_j(lambda)` from training amplitudes, then evaluate it on held-out quadrature nodes without using the true correction to form `q_r`;
3. certify that predictive model against independently evaluated JVP residuals and a quadrature refinement ladder;
4. repeat on grid/dt/time lattices and longer resolved windows;
5. only after a separate continuum/domain-transfer theorem could any part of this be promoted toward the Clay C/D target.
