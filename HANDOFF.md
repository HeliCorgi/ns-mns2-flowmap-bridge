# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: 2026-08-18 JST.

This is the short-form continuation point for future GPT sessions. The repository is expected to be developed primarily through repeated GPT sessions; do not rely on chat history as durable state.

## Resume protocol

Follow `docs/GPT_WORKFLOW.md`. Read, in order:

1. `PROJECT_GOAL.md`;
2. `SPEC.md`;
3. `AGENTS.md`;
4. `FORMAL_SCOPE.md`;
5. this file;
6. `docs/LEAN_CI_OPERATIONS.md`;
7. current GitHub `main`, relevant `Formal/` files, open PRs, and latest Lean verification evidence.

Current code and theorem statements override stale prose.

## Repository / verification state

- PR #77 (`Cut hosted Lean CI usage and add cache`) is merged.
- PR #78 (`Gpt handoff protocol`) is merged.
- PR #79 (`R3 young real set integral bridge`) is merged.
- PR #80 (`Close R3 Schwartz H3-to-H2 convection factors`) is merged.
- PR #81 (`Agent/chatgpt external lean workflow`) is merged as
  `710709c34b8ee564b071e71fd27313be4cc383a6`.
- PR #81 head `18c64b80b6eebb95a4344dec5811fc024b963377` passed hosted Lean run #257
  (`31924077773`). Its Git tree is identical to merge commit `710709c...`; the merge SHA itself has
  no separately attached run.
- Before this continuation, local and GitHub `main` were
  `f6bb133cf10f5a9b96594f10c742a1aa5c6cfe68`, with no open PRs.
- Proof commit `6ecfcda51d74b456b538def2577c52a403a0ff88` passed targeted builds of
  `Formal.R3SchwartzConvectionSobolevEstimate` and `Formal.AxiomAudit`.
- Commit `213495284f14c08d60936fa12a5260688124aa3f`, which adds only synchronized documentation on
  top of that proof, passed the local pinned source scan and full `Formal.+` gate (8735 jobs).
- Proof commit `5eb29848eea0529bf557c68a599e78317090f522` closes the weighted-density and
  bounded-extension gate. It passed targeted density/extension/AxiomAudit builds and the local
  pinned source scan plus full `Formal.+` gate (8737 jobs).
- Proof commit `2127757807768709d1ac19a0ec6f760c48a973cc` closes the order-aware `H²` Leray and
  projected-convection gate. It passed targeted bridge/projected/AxiomAudit builds and the local
  pinned source scan plus full `Formal.+` gate (8739 jobs).
- Proof commit `7ab4091eefeaf2d25b73824b9ec2941088876844` closes the positive-time `H² → H³`
  Stokes-smoothing gate. It passed targeted builds of `Formal.R3StokesH2H3Smoothing` and
  `Formal.AxiomAudit`, followed by the local pinned source scan and full `Formal.+` gate
  (8740 jobs).
- PR #82 (`Formalize endpoint-safe projected Duhamel on R^3`, proof commit
  `4f8ae0d66c65cd5458bc49b13c4e6b015e318b4d`) is merged as `03ea967`. Its hosted Lean run
  `32112489718` failed after 6 seconds because the GitHub Actions quota is exhausted; the hosted
  run is **not** the verification evidence for this merge.
- The verification evidence for `main = 03ea967` is local: the merge tree is identical to
  `4f8ae0d` (`git rev-parse <sha>^{tree}` both `d6c5424...`), and the full `Formal.+` gate
  (`lake exe cache get && lake build`) passed locally on that exact tree with 8743 jobs,
  including `Formal.AxiomAudit` (standard axioms only: `propext`, `Classical.choice`,
  `Quot.sound`).
- GitHub Actions quota is exhausted; hosted runs must not be used at all for the foreseeable
  future. All verification is local (Elan-pinned toolchain), and integration to `main` is by
  direct fast-forward push without opening a PR.
- This continuation's proof and synchronized documentation were integrated by direct fast-forward
  to `main`, without opening a PR; the verified `Formal/` tree is exactly the proof commit above.
- No GitHub Action was started or rerun for the new mathematical proof.
- Automatic full Lean builds on pushes to `main` remain disabled.
- Opening a PR to `main` currently starts the hosted Lean workflow, so a no-Actions integration must
  not use a PR merely as a merge vehicle.
- The preferred interactive path is now **ChatGPT -> external Lean runner -> exact diagnostics -> ChatGPT iteration** under the contract in `docs/LEAN_CI_OPERATIONS.md`.
- Local/self-hosted execution remains a valid reproduction/fallback path.
- GitHub-hosted Actions should be used only for deliberately spent status/final-confirmation checks or when repository integration policy explicitly requires one.

## Local Lean status in this workspace

The VS Code Lean extension, Elan shims, and pinned Lean 4.32.1 toolchain are installed locally. The
only environment issue found was an unset `ELAN_HOME`. The tested PowerShell setup is:

```powershell
$env:ELAN_HOME = Join-Path $env:USERPROFILE '.elan'
```

With that process-local setting, `lean --version`, `lake --version`, targeted builds, the axiom
audit, and the full gate all run locally. The extension provides the IDE/LSP integration; the actual
verification is performed by the local Elan-selected Lean compiler and kernel.

## Project claim boundary

Ultimate target: an exact official Clay/Fefferman Navier–Stokes A/B/C/D statement.

Current physical research specialization remains the `R^3`, preferably unforced `f = 0`, axisymmetric-with-swirl breakdown track governed by `SPEC.md`.

No current Lean theorem is a Clay result. Do not claim global regularity, blow-up, local well-posedness of the full concrete `R^3` problem, finite-cylinder transfer, or discrete-to-continuum promotion unless separately proved.

## Completed formal target

The previous near-term target

`R3SchwartzConvectionTermSobolevEstimate 3`

is now proved as `r3SchwartzConvectionTermSobolevEstimate_three` in
`Formal/R3SchwartzConvectionSobolevEstimate.lean`.

The same file proves `r3SchwartzConvectionSobolevEstimate_three`, obtaining the full
`R3SchwartzConvectionSobolevEstimate 3` through an exported direct sum estimate with the same
documented factor-three triangle-inequality loss as the existing `.to_convection` reduction.

That density/bounded-extension target is now also closed. The completed object is the complex
Bessel-coordinate map

`r3ConvectionH3ToH2 : R3HsVelocity 3 →L[ℂ] R3HsVelocity 3 →L[ℂ] R3HsVelocity 2`.

Here “completed” means that the codomain and domains are the existing complete `L²`
Bessel-coordinate models. It does not mean that Lean constructed a separate topological
`Completion` of Schwartz space.

The order-aware Leray/projected-convection target is now closed as well. The new bounded
reconstruction

`r3H2ToL2Operator : R3HsVelocity 2 →L[ℂ] R3L2Velocity`

implements the actual `J⁻²` Fourier multiplier. Lean proves that it represents exactly the
order-two tempered decoder and that it intertwines `r3LerayH2Operator` with the existing physical
`r3LerayL2Operator`. The resulting complex bilinear map is

`r3ProjectedConvectionH3ToH2 : R3HsVelocity 3 →L[ℂ] R3HsVelocity 3 →L[ℂ] R3HsVelocity 2`.

It has the inherited operator and pointwise bounds, stored-coordinate and reconstructed-`L²`
solenoidality, and exact Schwartz decoder agreement with the existing literal
`r3ProjectedSchwartzConvectionL2`.

The positive-elapsed-time, positive-viscosity smoothing target is now closed as well.
`Formal/R3StokesH2H3Smoothing.lean` constructs the nontrivial complex Bessel-coordinate map

`r3StokesH2ToH3Operator : R3HsVelocity 2 →L[ℂ] R3HsVelocity 3`

for `ν > 0` and `τ > 0`. Its Fourier multiplier is exactly

`(1 + ‖ξ‖²)^(1/2) * exp(-(2π)² ν τ ‖ξ‖²)`.

Lean proves the application and operator-norm bounds with the explicit majorant

`r3StokesH2H3TimeKernel ν τ = 1 + (sqrt ((2π)² ν τ))⁻¹`,

and proves that this scalar majorant is interval-integrable on `[0,T]` for every `T ≥ 0`.
The new genuine reconstruction

`r3H3ToL2Operator : R3HsVelocity 3 →L[ℂ] R3L2Velocity`

implements `J⁻³`. Reconstruction of the smoothed coordinate is exactly the existing physical
`L²` Stokes evolution of the reconstructed order-two input, both in `L²` and after embedding in
tempered distributions. The file also supplies order-three Leray decoder semantics, exact
order-two/order-three Leray intertwining, and stored-coordinate and reconstructed-`L²`
solenoidal preservation.

## Merged infrastructure through PR #80

### Representative/Fubini bridge — PR #79

The old ordinary-scalar-convolution versus bundled-Bochner representative blocker is closed for the two concrete H² majorants.

Relevant merged files/theorems include:

- `Formal/R3YoungRealSetIntegralBridge.lean`;
- `Formal/R3YoungRealConvolutionCommutativity.lean`;
- `Formal/R3SchwartzMajorantYoungRepresentative.lean`:
  - `coeFn_r3H2RightMajorantYoungL2_eq_scalarMajorant`;
  - `coeFn_r3H2LeftMajorantYoungL2_eq_scalarMajorant`;
- `Formal/R3SchwartzScalarMajorantL2.lean`;
- `Formal/R3SchwartzConvectionH2L2Majorant.lean`:
  - `norm_r3H2WeightedVelocitySchwartz_fourier_convectionTerm_toLp_le_scalarMajorants`;
  - `norm_r3H2WeightedVelocitySchwartz_fourier_convectionTerm_toLp_le_YoungFactors`.

Do not generalize that representative/Fubini identification to unrelated convolution objects without another explicit theorem.

### Fourier-coordinate and H³ closure — PR #80

`Formal/R3H2CoordinateFourierBounds.lean` now proves:

- `fourier_r3SchwartzCoordinate_eq`;
- `integral_norm_fourier_r3SchwartzCoordinate_le_H3`;
- `norm_r3H2WeightedScalarSchwartz_fourier_coordinate_toLp_le_H3`.

The exact coordinate/Fourier identity

`𝓕 (r3SchwartzCoordinate i f) = r3SchwartzCoordinate i (𝓕 f)`

is therefore green and no longer an open bridge.

`Formal/R3SchwartzConvectionH3Closure.lean` now proves:

- `norm_r3H2WeightedVelocitySchwartz_fourier_convectionTerm_toLp_le_H3`;
- `norm_r3SchwartzToHsCLM_two_convectionTerm_le_H3`.

The proved physical per-coordinate estimate is

`‖r3SchwartzToHsCLM 2 (r3SchwartzConvectionTerm i u v)‖`

`≤ 4 * ‖r3H2InverseBesselWeightL2‖ * r3CoordinateDerivativeFrequencyConstant i * ‖r3SchwartzToHsCLM 3 u‖ * ‖r3SchwartzToHsCLM 3 v‖`.

Also already available:

`r3CoordinateDerivativeFrequencyConstant_nonneg (i : Fin 3)`.

### Uniform finite-coordinate closure — locally verified commit `6ecfcda...`

`Formal/R3SchwartzConvectionSobolevEstimate.lean` adds:

- `r3UniformCoordinateDerivativeFrequencyConstant`;
- `r3UniformCoordinateDerivativeFrequencyConstant_nonneg`;
- `r3CoordinateDerivativeFrequencyConstant_le_uniform`;
- `r3SchwartzConvectionH3Constant`;
- `r3SchwartzConvectionH3Constant_nonneg`;
- `r3SchwartzConvectionTermSobolevEstimate_three`;
- `r3SchwartzConvectionSobolevEstimate_three`.

The uniform derivative constant is the finite sum over `Fin 3`. Each coordinate constant is
nonnegative, so every summand is bounded by that sum. The common per-term witness is

`4 * ‖r3H2InverseBesselWeightL2‖ * r3UniformCoordinateDerivativeFrequencyConstant`.

`Formal/AxiomAudit.lean` now prints the axiom dependencies of both final estimate theorems. They
use only the standard mathlib foundations reported by the rest of this development (`propext`,
`Classical.choice`, and `Quot.sound`).

### Weighted density and completed convection — locally verified commit `5eb2984...`

`Formal/R3SchwartzSobolevDensity.lean` proves:

- `r3SobolevWeightComplex_mul_neg`;
- `r3SchwartzBesselMultiplier_inverse_apply`;
- `r3SchwartzBesselMultiplier_surjective`;
- `r3SchwartzToHsCLM_denseRange`.

The proof uses the inverse-order Bessel multiplier on Schwartz fields and mathlib's dense range of
the canonical Schwartz-to-`L²` map. Do not strengthen this to an inducing/dense-embedding claim for
the native Schwartz Fréchet topology.

`Formal/R3SobolevConvectionExtension.lean` applies `LinearMap.extendOfNorm` first in the second
input and then in the first input. It proves:

- `r3ConvectionH3ToH2_apply_schwartz`;
- `r3HsToTempered_r3ConvectionH3ToH2_schwartz`;
- `norm_r3ConvectionH3ToH2_le`;
- `norm_r3ConvectionH3ToH2_apply_le`;
- `r3ConvectionH3ToH2_unique`.

The bounds force both dense-core maps to vanish on the appropriate kernels, so the extensions are
well-defined and do not choose Schwartz representatives or approximating sequences. The axiom
audit reports only `propext`, `Classical.choice`, and `Quot.sound` for the new audited theorems.

`R3HsVelocity s` currently has a phantom order parameter and is definitionally the same `L²`
coordinate type for every `s`. Its physical meaning is fixed by `r3HsToTemperedCLM s`. Never use
the alias equality as a physical `H³ → H²` inclusion or as a smoothing theorem.

## Exact next Lean gate

Do not reopen the completed convolution, bounded-extension, Leray, positive-time smoothing, or
endpoint-safe two-space Duhamel work unless current source regresses.

The two-space Duhamel interface demanded by the previous handoff is closed by PR #82:
`EndpointSafeTwoSpaceDuhamelContract`, actual-integrand strong measurability and Bochner
interval-integrability, the quantitative bounds, the `IsMildAt` / `IsMildSolutionOn` predicates,
the same-space `r3StokesH3Evolution`, and the concrete
`r3EndpointSafeProjectedDuhamelContract` with `IsR3EndpointSafeProjectedMildSolutionOn` are all
on `main` and locally verified.

The next smallest mathematical task is the **Picard fixed-point layer** for exactly that
contract, in the complex Bessel-coordinate carrier:

1. time-continuity of `t ↦ ∫ s in 0..t, duhamelIntegrand t u s` for a trajectory continuous on
   `[0, T]`, via the reversed representation `∫ τ in 0..t, endpointSafeSmoothing τ (Q (u (t-τ)) (u (t-τ)))`
   (`intervalIntegral.integral_comp_sub_left`), uniform continuity of the trajectory, and
   continuity of the primitive `K(t) = ∫₀ᵗ k̃`;
2. the Picard map on `C(Icc 0 T, X)` (extend trajectories by `Set.IccExtend`), closed-ball
   invariance `‖u₀‖-controlled`, and the contraction estimate from
   `Q u u - Q v v = Q u (u-v) + Q (u-v) v`;
3. Banach fixed point (`ContractingWith`) on the complete closed ball, giving for small `T > 0`
   a mild solution in the sense of `IsMildSolutionOn` and uniqueness among ball trajectories;
4. concrete instantiation: local existence + ball uniqueness for
   `IsR3EndpointSafeProjectedMildSolutionOn hnu T u0 u`, with `M = 1` from
   `norm_r3StokesH3Evolution_le_one`.

This layer stays in the complex carrier. It does not by itself give physical (real-valued)
local well-posedness, pressure reconstruction, or any Clay statement; the
real-valued/conjugate-symmetric restriction remains a separate later gate.

## Latest Lean verification

```text
runner: local Windows (Git Bash) process via Elan
revision: main merge 03ea967 (tree identical to proof commit 4f8ae0d6)
toolchain: leanprover/lean4:v4.32.1
dependency manifest: committed lake-manifest.json; mathlib per lake-manifest.json
full scope: lake exe cache get && lake build — pass (8743 jobs)
axiom scope: Formal.AxiomAudit — pass (propext, Classical.choice, Quot.sound only)
GitHub Actions: PR #82 hosted run 32112489718 failed in 6s on exhausted quota; not evidence
```

## Runner protocol for the next proof

Use a conforming ChatGPT-accessible Lean runner when connected; otherwise use the tested local
Elan path above. In either case, preserve the same pinned-revision evidence contract.

For each candidate change, record:

```text
runner: <tool/provider>
revision: <commit SHA or exact candidate patch>
toolchain: <value from lean-toolchain>
scope: <target module or full gate>
result: <pass/fail>
diagnostics: <exact Lean error when failing>
```

Preferred iteration:

```text
smallest target
-> exact Lean diagnostic
-> minimal proof edit
-> same target again
-> full pinned gate after target is green
```

Do not use GitHub-hosted PR runs as the diagnostic loop.

## Nonclaims / guardrails

- no `sorry`;
- no `admit`;
- no new local `axiom`;
- no source-level `opaque` proof hiding;
- do not report candidate code as proved before a conforming pinned Lean verification accepts it;
- do not merge an ungreen mathematical PR;
- do not auto-merge unless the user explicitly asks;
- the completed map is a complex Bessel-coordinate extension; arbitrary-`H³` decoder equality with
  a separately defined distributional product is not yet proved;
- the projected map does not yet supply a physical real-valued/conjugate-symmetric restriction,
  a two-space Duhamel contract, pressure reconstruction, or concrete local well-posedness;
- the proved `H² → H³` Stokes operator requires `ν > 0` and positive elapsed time; no bounded
  cross-space operator is supplied at `τ = 0` or `ν = 0`;
- interval integrability of `r3StokesH2H3TimeKernel` is a scalar-majorant theorem, not yet a proof
  that an endpoint-totalized operator-valued Duhamel integrand is strongly measurable or Bochner
  integrable;
- do not claim that the nonsmooth-at-zero Leray symbol maps Schwartz space to itself; the proved
  core comparison is in `L²` and tempered distributions;
- do not use the phantom Sobolev-order alias itself as an inclusion or smoothing theorem; the
  positive-time result is justified by its explicit multiplier and decoder theorems;
- do not spend hosted Actions as an interactive compiler while quota is scarce/exhausted.

## Minimal continuation prompt

`ns-mns2-flowmap-bridge を resume protocol どおり確認して、最新 main/Lean verification と HANDOFF.md を照合して続きから。endpoint-safe two-space Duhamel contract・actual integrand の Bochner integrability・same-space H³ evolution・具体 R³ mild 述語は PR #82 で完了済み(main、ローカル 8743 jobs green)。次は同 contract の Picard fixed-point layer: Duhamel 積分の時間連続性 → C(Icc 0 T, X) 上の Picard 写像と縮小評価 → 小さい T>0 での mild 解の存在と ball 一意性 → 具体 R³ instantiation。complex carrier のままで良い(実数値制限は別ゲート)。Lean はローカルで反復し、GitHub Actions は一切使わない(quota 枯渇)。green 後は成果物を main に fast-forward 統合して。古い会話より実コードを優先して。`
