# MNS-2 v2.12 — predictive path-correction POD bridge report

Date: 2026-08-13 JST

## Verdict

**`PREDICTIVE-PATH-POD-BRIDGE-AUDIT-COMPLETE`** on the short-time synthetic 12x24 frozen discrete map.

v2.12 fixes the main scope defect of v2.11: at each held-out certification node, the reduced tangent is now formed from a coefficient model **before** the true JVP at that node is evaluated. The true JVP is then used only to audit the prediction residual.

With a low-amplitude-resolved training mesh and global rank 4, the 12-panel composite Gauss-4 audit gives approximately:

- predictive endpoint relative error vs direct: **`9.10e-9`**;
- full tangent bridge relative error vs direct: **`4.32e-9`**;
- predictive-vs-full tangent integral relative error: **`8.07e-9`** (absolute metric error `7.22e-9`);
- quadrature residual-integral estimate relative to the direct endpoint norm: **`1.60e-8`**;
- numerical triangle ratio: **`0.505`**.

This remains a finite-discrete synthetic audit. The residual integral is a floating-point quadrature estimate, not a rigorous interval enclosure. No continuum or Clay promotion is made.

## Predictive construction

As in v2.11,

\[
g(\lambda)=J_T(\lambda y_0)[y_0],\qquad
c(\lambda)=g(\lambda)-g(0).
\]

But v2.12 splits training from certification.

### Training

True correction snapshots are evaluated only at

`0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 0.75, 1.0`.

A physical-energy POD basis is learned from those snapshots. For each retained mode `phi_j`, the training coefficient

\[
a_j(\lambda_k)=\langle \phi_j,c(\lambda_k)\rangle_E
\]

is computed. The exact anchor `c(0)=0` is added, and each scalar coefficient is interpolated by PCHIP.

### Certification

At a held-out quadrature node `lambda`, the predictor is first formed as

\[
q_{\rm pred}(\lambda)=g(0)+\sum_{j=1}^r \widehat a_j(\lambda)\phi_j.
\]

Only after this value is fixed does the audit evaluate the true JVP `g(lambda)` and residual

\[
r(\lambda)=g(\lambda)-q_{\rm pred}(\lambda).
\]

This ordering is a code-level invariant and certification nodes are required to be disjoint from training amplitudes.

## Why the training mesh changed

A coarse training mesh `0.25,0.5,0.75,1.0` looked strongly rank two in v2.11, but a predictive PCHIP model trained only there gave a roughly `2.27e-7` endpoint error.

Direct amplitude probes showed the reason: the correction is exactly zero at `lambda=0` and then rises sharply around `lambda ~ 1e-3 ... 1e-2` before reaching its short-time plateau. For example the correction norm was observed at the rough scales

- `lambda=1e-4`: `~2e-8`;
- `lambda=1e-3`: `~1.15e-6`;
- `lambda=5e-3`: `~2.43e-6`;
- `lambda=1e-2`: `~2.30e-6`;
- `lambda>=2.5e-2`: close to the `~2.2e-6` plateau.

The fixed WENO epsilon makes such a low-amplitude crossover plausible in the frozen discrete map. This is a numerical/discretization feature to be resolved, not a physical singularity claim.

Adding the low-amplitude training points reduces the predictive error dramatically, but it also exposes more resolved POD directions. This is why v2.12 defaults to a rank ladder interpretation rather than preserving the coarse-training rank-2 label.

## Rank audit with richer training

At the 12-panel level, representative results were:

| rank | predictive endpoint rel. error | predictive-vs-full abs. error | residual estimate rel. | triangle ratio |
|---:|---:|---:|---:|---:|
| 2 | `1.657e-8` | `1.373e-8` | `4.344e-8` | `0.353` |
| 3 | `1.222e-8` | `1.004e-8` | `2.022e-8` | `0.555` |
| 4 | `9.103e-9` | `7.220e-9` | `1.597e-8` | `0.505` |

The richer-training POD eigenvalues relative to the first were approximately

`1, 6.257e-3, 1.565e-3, 2.138e-4, 6.150e-5, 9.716e-6, ...`.

So the correct statement is not “the path correction is universally rank two.” The rank required by a predictive model depends on the resolved training distribution and must be re-audited when that distribution changes.

## Two-chart experiment not promoted

A separate local experiment used low/high-amplitude POD charts with a smooth blend over `[0.025,0.1]`. Local rank 3 produced a 12-panel endpoint error around `6.31e-9`, but its combined span can be as large as six dimensions and the extra model complexity was not justified by this tiny short-time synthetic case. Hard switching was rejected because it introduced a model jump.

Therefore v2.12 keeps the simpler global rank-4 predictor as the reproducible baseline. Local/basis-adaptive models remain an experimental option for longer or more nonlinear windows.

## Relation to the formal residual theorem

PR #18 proves the exact functional-analytic inequality

\[
\left\|(S(d)-S(0))-\int_0^1q(s)\,ds\right\|
\le
\int_0^1\|DS(sd)[d]-q(s)\|\,ds.
\]

v2.12 supplies a genuinely predictive finite-rank candidate `q_pred`. The numerical audit checks the corresponding residual at held-out nodes and applies composite quadrature to the right-hand side.

The analytic theorem is rigorous; the numerical quadrature value is not yet a rigorous enclosure. That distinction remains mandatory.

## What v2.12 establishes

For this single synthetic short-time frozen discrete map:

1. a coefficient predictor can be formed independently of held-out true JVP values;
2. resolving the low-amplitude coefficient crossover reduces the coarse predictor error by more than an order of magnitude;
3. rank 4 gives a predictive endpoint error around `9e-9`, comparable to the underlying full-tangent quadrature scale;
4. the observed predictive-vs-full integral error is below the quadrature estimate of the integrated pointwise residual;
5. the rank label is sensitive to the training distribution and must not be frozen across retraining.

## What v2.12 does not establish

It does **not** establish:

- a universal low-dimensional Navier--Stokes solution map;
- a rank-4 continuum tangent family;
- a rigorous numerical upper enclosure for the residual integral;
- convergence across grid, timestep, physical time, or domain;
- transfer from the finite cylindrical MNS/Hou discretization to Clay `R^3` or `T^3`;
- Hou late-state singular behavior;
- a blow-up or Clay A/B/C/D result.

## New fail-closed rules

- **FC-079:** coarse amplitude training plus stable quadrature is not coefficient-model convergence;
- **FC-080:** POD rank must be re-audited when the training distribution changes;
- **FC-081:** certification truth must not leak into predictor construction or tuning.

## Next step

The next meaningful numerical promotion is no longer “make the short synthetic endpoint error smaller.” It is to test whether the predictive structure survives a **grid / timestep / physical-time ladder**, with training and certification splits frozen in physical amplitude coordinates and all WENO/LF schedule provenance held fixed.

Only after that should longer resolved windows or more nonlinear states be considered. A continuum/Clay promotion remains a separate theorem-level obligation.
