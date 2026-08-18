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
- The Picard fixed-point / local-existence layer
  (`Formal/EndpointSafeTwoSpacePicard.lean`, `Formal/R3EndpointSafeProjectedLocalExistence.lean`,
  with new `Formal/AxiomAudit.lean` prints) is committed directly on `main` after this
  continuation's local verification: full `Formal.+` gate pass (8745 jobs), pinned source scan
  clean, axiom audit standard for all four new audited theorems.
- The conjugation/reflection reality-predicate layer
  (`Formal/R3ConjugationReflection.lean`, with five new `Formal/AxiomAudit.lean` prints) is
  committed directly on `main` after local verification: full `Formal.+` gate pass
  (8746 jobs), pinned source scan clean, axiom audit standard.
- The Plancherel reality bridge (`Formal/R3FourierConjugationBridge.lean`, with four new
  `Formal/AxiomAudit.lean` prints) is committed directly on `main` after local verification:
  full `Formal.+` gate pass (8747 jobs), pinned source scan clean, axiom audit standard.
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

## Stage-A candidate gate campaign (2026-08-18)

The necessary-condition gate battery was pre-registered and run at literature level against
the fixed-ν Hou NS candidate (arXiv:2107.06509). Outcome: **route killed at candidate
level** — the candidate's own `‖u‖_∞ ~ (T−t)^{−1/2}` one-scale scaling is Type I, excluded
for axisymmetric NS by CSTY 2008/2009 + KNSS 2009. See
`docs/gates/BARKER_GATE_PREREGISTRATION_2026-08-18.md`,
`docs/gates/STAGE_A_LITERATURE_VERDICT_2026-08-18.md`, and the registry entry
`ns-singularity-certificate-lab/docs/candidates/HOU_FIXED_NU_TYPE1_NS_CANDIDATE_KILL_AUDIT_2026-08-18.md`.

Second pass (same date): the two-scale literature gate and the Type II survival map are
done — `docs/gates/TWO_SCALE_LITERATURE_GATE_2026-08-18.md`,
`docs/gates/TYPE2_SURVIVAL_MAP_2026-08-18.md`, figure `docs/gates/type2_survival_map.png`
(generator `experiments/type2_survival_map.py`), registry entry
`ns-singularity-certificate-lab/docs/candidates/HOU_HUANG_TWO_SCALE_NS_ROUTE_STATUS_2026-08-18.md`.
Outcome: the Hou–Huang two-scale scenarios are Clay-inadmissible (Euler / degenerate ν) and
their standard-ν NS transfer died in the authors' own test (max-vorticity growth < 2); the
survival map nevertheless leaves a **nonempty open window** — `γ ∈ (1/2, 1)`,
`α ∈ (max(2γ/3, 2γ−1), γ)` for a core carrying the `L³` divergence, with sub-parabolic ring
collapse dead and swirl-dominated cores forced into ≥3-region structures.

Consequences for planning:

- the Lean program below is candidate-independent and continues unchanged;
- the abstract Chen–Hou-style skeleton (Stage B) remains the right 4/10 → 5/10 target, but
  its concrete instantiation must wait for a candidate **inside the survival window**;
- the admission test for any future (N)-level candidate is now fixed: fitted `(γ, α, ρ)`
  with confidence intervals inside the open window, converged `√(T−t)·‖u‖_{L∞} → ∞`, and
  gates G1–G7 with null/positive controls;
- next theory increment for the map (cheap): tabulate the exact hypotheses of the
  `|u| ≤ C/r` exclusion family and the slightly-supercritical / Type II refinements
  ([V1]/[V2] in the map document) — they can only shrink the window near its `γ = 1/2`
  edge.

## Exact next Lean gate

Do not reopen the completed convolution, bounded-extension, Leray, positive-time smoothing,
endpoint-safe two-space Duhamel, or Picard local-existence work unless current source regresses.

The Picard fixed-point layer demanded by the previous handoff is closed on `main`:

- `Formal/EndpointSafeTwoSpacePicard.lean` — cumulative smoothing mass (`kernelPrimitive`)
  with monotonicity/continuity/small-time smallness; exact reversed elapsed-time
  representation of the Duhamel integral; quantitative size/difference/time-difference bounds;
  `continuousOn_duhamelIntegral`; the Picard map on `C(Icc 0 T, X)` with ball invariance and
  contraction; `exists_pos_time_isMildSolutionOn` (existence on some `0 < T ≤ 1`, trajectory in
  the closed `‖u₀‖ + 1` ball, uniqueness among ball-valued mild solutions).
- `Formal/R3EndpointSafeProjectedLocalExistence.lean` —
  `r3EndpointSafeProjected_exists_localMildSolution`: for every `ν > 0` and order-three Bessel
  coordinate `u₀`, local existence + ball uniqueness for
  `IsR3EndpointSafeProjectedMildSolutionOn hnu T u₀ u`, plus the unfolded mild-equation form
  `r3EndpointSafeProjected_localMildSolution_equation`.

The first slice of the reality gate is closed by `Formal/R3ConjugationReflection.lean`:
fiber conjugation `r3CConj` with its fixed-point characterization, the norm-preserving carrier
involutions `r3L2Conj` (pointwise conjugation, `→L[ℝ]`) and `r3L2Reflect` (composition with
`x ↦ -x`, `→L[ℂ]`), their commutation, and the predicates `IsR3RealVelocity` /
`IsR3ConjugateSymmetricVelocity` with algebraic closure, closedness, and the a.e.
characterization `isR3RealVelocity_iff_im_ae`. Do not redefine these structures.

The Plancherel reality bridge demanded by the previous handoff is closed by
`Formal/R3FourierConjugationBridge.lean`: the Schwartz involutions `r3SchwartzConjCLM` /
`r3SchwartzReflectCLM`, the pointwise identity `r3Fourier_conj_eq`
(`𝓕 (conj ∘ f) ξ = conj (𝓕 f (-ξ))`), the `toLp` compatibility lemmas, the exact `L²`
intertwining `fourier_r3L2Conj` (`𝓕 (r3L2Conj g) = r3L2Reflect (r3L2Conj (𝓕 g))`), and the
equivalence `isR3RealVelocity_iff_fourier_conjugateSymmetric`. Do not re-prove these.

The next smallest mathematical task is **realness preservation of the concrete operators**
(FORMAL_SCOPE section 6, next gate 1). Prove commutation with `r3L2Conj` for, in increasing
order of difficulty:

1. the Stokes evolution: `r3StokesScalarComplex ν t ξ = exp (-(2π)² ν |ξ|² t)` is real-valued
   and even in `ξ`, so the frequency multiplier commutes with `r3L2Reflect ∘ r3L2Conj`; push
   through `fourier_r3StokesL2Operator` and the bridge to get
   `r3L2Conj (r3StokesL2Operator … g) = r3StokesL2Operator … (r3L2Conj g)`, then the same for
   `r3StokesH3Evolution` and `r3StokesH2ToH3Operator` (whose extra factor
   `(1 + ‖ξ‖²)^(1/2)` is likewise real and even);
2. the Leray projector: the fiber symbol `P(ξ) = I - (ξ ⊗ ξ)/|ξ|²` is a real matrix, even in
   `ξ`, so it commutes with fiber conjugation; conclude for `r3LerayL2Operator` and its
   order-two/order-three variants;
3. the projected convection `r3ProjectedConvectionH3ToH2`: conjugation equivariance on the
   Schwartz core (the convection term is a real bilinear expression in the fields), then
   extend by density exactly as the bounded-extension layer does.

After that: realness of the local mild solution for real data — the real ball trajectories
form a closed nonempty Picard-invariant subset of `C(Icc 0 T, X)`, so the fixed point lies in
it, promoting `r3EndpointSafeProjected_exists_localMildSolution` to a physical statement.
Then the quantitative horizon / unrestricted uniqueness / continuation strengthening feeding
the breakdown track.

The closed layers are statements about the complex carrier and the `L²` Fourier transform. No
concrete operator has been proved to preserve realness, and no physical (real-valued)
local-wellposedness, pressure reconstruction, or Clay statement is available.

## Latest Lean verification

```text
runner: local Windows (Git Bash) process via Elan
revision: working tree of the Plancherel reality-bridge proof commit on main
  (new: Formal/R3FourierConjugationBridge.lean; extended Formal/AxiomAudit.lean)
toolchain: leanprover/lean4:v4.32.1
dependency manifest: committed lake-manifest.json; mathlib per lake-manifest.json
target scope: lake env lean Formal/R3FourierConjugationBridge.lean — pass, no warnings
full scope: lake build (Formal.+ default target) — pass (8747 jobs)
source scan: pinned sorry/admit/axiom/opaque scan over Formal/ — clean
axiom scope: Formal.AxiomAudit — pass; the four new audited theorems
  (r3Fourier_conj_eq, fourier_r3SchwartzConjCLM, fourier_r3L2Conj,
   isR3RealVelocity_iff_fourier_conjugateSymmetric)
  depend only on propext, Classical.choice, Quot.sound
GitHub Actions: not invoked (quota exhausted; hosted runs banned)
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
- the projected map does not yet supply a physical real-valued/conjugate-symmetric restriction
  or pressure reconstruction; the two-space Duhamel contract and the ball-local mild existence
  theorem are supplied by the merged Duhamel/Picard layers and must not be re-proved;
- the proved `H² → H³` Stokes operator requires `ν > 0` and positive elapsed time; no bounded
  cross-space operator is supplied at `τ = 0` or `ν = 0`;
- interval integrability of `r3StokesH2H3TimeKernel` is a scalar-majorant theorem, not yet a proof
  that an endpoint-totalized operator-valued Duhamel integrand is strongly measurable or Bochner
  integrable;
- do not claim that the nonsmooth-at-zero Leray symbol maps Schwartz space to itself; the proved
  core comparison is in `L²` and tempered distributions;
- do not use the phantom Sobolev-order alias itself as an inclusion or smoothing theorem; the
  positive-time result is justified by its explicit multiplier and decoder theorems;
- the new local mild solution lives in the complex Bessel-coordinate carrier; do not call it
  physical local well-posedness before the real-valued/conjugate-symmetric restriction exists;
- `IsR3RealVelocity` / `IsR3ConjugateSymmetricVelocity` are now related through the Plancherel
  `L²` Fourier transform, but no concrete Stokes/Leray/convection operator has been proved to
  preserve either predicate, and no mild solution has been proved real;
- its uniqueness clause holds only among trajectories in the certified `‖u₀‖ + 1` ball on the
  produced horizon; do not cite it as unconditional uniqueness;
- the produced horizon is existential with `0 < T ≤ 1`; no quantitative lower bound in `‖u₀‖`
  and no continuation/maximal-interval theorem is available yet;
- do not spend hosted Actions as an interactive compiler while quota is scarce/exhausted.

## Minimal continuation prompt

`ns-mns2-flowmap-bridge を resume protocol どおり確認して、最新 main/Lean verification と HANDOFF.md を照合して続きから。Duhamel contract(PR #82)、Picard fixed-point layer(局所存在+ball 一意性)、conjugation/reflection reality predicates、Plancherel reality bridge(r3Fourier_conj_eq・fourier_r3L2Conj・isR3RealVelocity_iff_fourier_conjugateSymmetric、ローカル 8747 jobs green)まで main に完了済み。次は具体 operator の realness 保存: (1) Stokes(symbol exp(-(2π)²ν|ξ|²t) は実かつ偶 → fourier_r3StokesL2Operator と bridge 経由で r3L2Conj と可換、H3Evolution と H2ToH3 も同様)、(2) Leray(実行列 P(ξ) = I - ξ⊗ξ/|ξ|² は偶)、(3) projected convection(Schwartz core での共役同変性 → 密度で拡張)。その後 real 初期値の mild 解の realness(閉かつ Picard 不変な部分集合に不動点が入る論法)。Lean はローカルで反復し、GitHub Actions は一切使わない(quota 枯渇)。green 後は成果物を main に fast-forward 統合して。古い会話より実コードを優先して。`
