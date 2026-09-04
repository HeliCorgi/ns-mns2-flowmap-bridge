# M-1 independent probe — 2026-09-04

Status: **EVIDENCE-GRADE ONLY**. Periodic `T^3`, `64^3`, existing repo pseudo-spectral solver architecture (rotational form, Leray projection, 2/3 dealias, RK4). This is an independent scratch run for later comparison; nothing here is a Clay claim and nothing was committed to the repo.

## 1. Question

Use enstrophy-growth events as the conditioning object, decompose exact NS terms, and look for a dimensionless cancellation/geometry observable that is not merely the already-priced `L_t^4 H^1` / `lambda_2^+` wall.

Runs used:

- R1 Taylor–Green, `nu=0.02`; max finite-difference enstrophy growth at `t=1.70`, tail `1.73e-10`.
- R2 anisotropic random low-band, `nu=0.035`; positive-growth diagnostic at `t=0.25`, tail `1.62e-6`.
- R4 mixed two-mode + 10% random perturbation, `nu=0.02`; max finite-difference enstrophy growth at `t=1.05`, tail `3.31e-6`.

All three quoted snapshots are below the old `1e-5` tail smoke threshold. R4's later enstrophy maximum at `t=1.8` is above it (`1.56e-5`) and is not used as primary evidence.

## 2. Pressure / middle-strain decomposition

For `S e_i=lambda_i e_i`, the exact projected strain equation is sampled as

`D_t lambda_i = -lambda_i^2 + 1/4 (|omega|^2-(omega.e_i)^2) - p_ii + nu e_i^T Delta S e_i`.

For `X=∫(lambda_2^+)^2`, the four contributions to `(1/2)X'` at max enstrophy growth were:

| run | self `-∫lambda2^3` | vorticity source | pressure `-∫lambda2 p22` | projected viscosity | sum |
|---|---:|---:|---:|---:|---:|
| R1 t=1.70 | -1.591 | +2.224 | **+2.027** | -1.026 | +1.634 |
| R4 t=1.05 | -69.366 | +68.361 | **+10.726** | -13.755 | -4.033 |

So the pressure-Hessian term is not a universal regularizer in the `lambda_2^+` channel; in both active snapshots its *global* contribution is destabilizing. Moreover R4 has very strong enstrophy growth while `X` is already decreasing. This independently supports parking a simple HR-2 pressure-rescue route.

Conditioning on the top 1% of positive enstrophy-production density `q=omega^T S omega` reveals opposite geometric branches:

- R1 (`t=1.70`): `omega` is almost orthogonal to `e_2` (`mean cos^2(omega,e2)=0.00258`); `mean p22=+0.376`, so pressure regularizes `lambda_2` there.
- R4 (`t=1.05`): `omega` is strongly aligned with `e_2` (`mean cos^2=0.946`); `mean p22=-0.721`, so pressure destabilizes `lambda_2` there.

Thus neither the sign of `p22` nor a fixed middle-eigenvalue pressure cancellation survives conditioning across the two nonlinear regimes.

For the coordinate-free stretching rate `alpha=(omega/|omega|)^T S (omega/|omega|)`, the Euler part of the exact material derivative contains

`|P_{xi^perp} S xi|^2 - alpha^2 - p_{xi xi}`.

At top-1% production, the combined self/pressure contribution `-alpha^2-p_xixi` is mildly **positive** in R1 (`q`-weighted `+0.0539`) but strongly **negative** in R4 (`-0.8347`). A simple sign law for `p_xixi+alpha^2` is therefore also not supported.

## 3. Exact local Betchov decomposition [derived]

Let `A_ij=partial_i u_j`. For incompressible flow,

`tr(A^3) = div B`,

where

`B_i = u_j A_jk A_ki - (1/2) u_i tr(A^2)`.

Since `A=S+Omega`, `tr S=0`, `tr(S^3)=3 det S`, and `tr(S Omega^2)=1/4 omega^T S omega`,

`q + 4 det S = (4/3) tr(A^3) = div J_B`,

with

`J_B = (4/3) B`.

Hence the local enstrophy equation can be rewritten exactly as

`partial_t (|omega|^2/2) + div( u |omega|^2/2 - nu grad(|omega|^2/2) - J_B )`

`= -4 det S - nu |grad omega|^2`.

The algebraic identity `q+4detS=(4/3)tr(A^3)` was satisfied to `~1e-15` relative at the sampled states. Computing `div J_B` pseudo-spectrally gave relative L2 errors `1.0e-5` (R1), `1.4e-3` (R2), `6.1e-4` (R4), consistent with product/dealias discretization.

This gives a natural dimensionless **source-versus-flux observable** on any conditional region `Omega`:

`beta_B(Omega) := (-4 ∫_Omega det S) / (∫_Omega q)`

and `1-beta_B` is the signed Betchov-flux-divergence fraction.

For `Omega =` top 1% of positive `q`:

| run | `beta_B` determinant/source fraction | Betchov flux fraction `1-beta_B` | `∫|q+4detS| / ∫q` | fraction `lambda2>0` |
|---|---:|---:|---:|---:|
| R1 t=1.70 | **0.0763** | **0.9237** | 0.9237 | 0.8049 |
| R2 t=0.25 | **0.6361** | **0.3639** | 0.5086 | 0.9439 |
| R4 t=1.05 | **0.9080** | **0.0920** | 0.2351 | 1.0000 |

At the top 0.5% the split becomes R1 `0.0455 / 0.9545`, R2 `0.6490 / 0.3510`, R4 `0.8899 / 0.1101`.

So equally genuine enstrophy-growth events separate into very different local mechanisms:

- **flux-dominated branch (R1):** intense local stretching is ~95% the divergence part of the Betchov identity and only ~5% the local strain-determinant source;
- **source-dominated branch (R4):** ~90% is the determinant source, i.e. the branch already naturally priced by `lambda_2^+`;
- **mixed branch (R2):** both contribute at order one.

This split is invisible to the global Betchov/Miller identity because `∫ div J_B=0` on the torus.

## 4. Candidate observable / route seed

The most interesting output of this scratch session is therefore not a pressure sign, but the conditional Betchov ratio

`beta_theta(t) = -4 ∫_{Omega_theta(t)} det S / ∫_{Omega_theta(t)} (omega^T S omega)`

for production superlevel sets `Omega_theta(t)={q_+ >= quantile_theta(q_+)}` (or a scale-localized analogue).

It is dimensionless and distinguishes whether a growth event is generated locally by the strain determinant or by convergence of an exact cubic flux. The corresponding exact localized identity is

`∫_Omega q = -4∫_Omega det S + ∫_{∂Omega} J_B.n`.

A possible analytic dichotomy is:

1. source-dominated events: reduce to the already-known middle-eigenvalue/strain channel;
2. flux-dominated events: try to control repeated concentration through the boundary flux `J_B`, rather than by a pointwise/critical norm of `lambda_2^+`.

No closure is claimed. In particular `J_B ~ u (grad u)^2` is cubic and has no free global critical bound on file. The next useful test, if this observable survives comparison with the other independent run, is whether the flux-dominated branch exhibits a stable *outward / shell-transfer geometry* on nested neighborhoods of the production maximum, rather than merely a large signed divergence at grid points.

## 5. Current verdict

- Simple `p22` sign mechanism: **negative**.
- Simple `p_xixi + alpha^2` sign mechanism: **negative**.
- `lambda_2^+` as universal event carrier: **negative** (R4 enstrophy grows strongly while `X` decreases).
- Conditional local Betchov source/flux split: **candidate observable found; worth one targeted follow-up**, not a theorem and not yet a regularity head.

