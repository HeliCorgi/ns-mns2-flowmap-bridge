# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: 2026-08-21 JST.

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
- The operator-realness slices (`Formal/R3StokesConjugationEquivariance.lean`,
  `Formal/R3LerayConjugationEquivariance.lean`,
  `Formal/R3ConvectionConjugationEquivariance.lean`) and the physically real local mild
  solution (`Formal/R3RealLocalMildSolution.lean`) are committed directly on `main` after
  local verification: full `Formal.+` gate passes (8748 → 8751 jobs), pinned source scans
  clean, axiom audit standard.
- The explicit quantitative lifespan (`Formal/R3QuantitativeLifespan.lean`, plus the
  statement-preserving refactor of `Formal/EndpointSafeTwoSpacePicard.lean` extracting
  `exists_isMildSolutionOn_of_kernelPrimitive_lt`, with ten new `Formal/AxiomAudit.lean`
  prints) is committed directly on `main` after local verification: full `Formal.+` gate
  pass (8752 jobs), pinned source scan clean, axiom audit standard (commit `6d5e541`).
- The mild restart identity and unrestricted uniqueness
  (`Formal/EndpointSafeTwoSpaceRestart.lean`, `Formal/EndpointSafeTwoSpaceUniqueness.lean`,
  with eight new `Formal/AxiomAudit.lean` prints, including the unconditional-realness
  corollary) are committed directly on `main` after local verification: full `Formal.+`
  gate pass (8754 jobs), pinned source scan clean, axiom audit standard (commit `e8b7144`).
- The maximal-continuation layer in blow-up–dichotomy form
  (`Formal/EndpointSafeTwoSpaceConcatenation.lean`, `Formal/R3MildContinuation.lean`, with
  eight new `Formal/AxiomAudit.lean` prints) is committed directly on `main` after local
  verification: full `Formal.+` gate pass (8756 jobs), pinned source scan clean, axiom
  audit standard (commit `77f3832`). This completes the endorsed 3-gate plan.
- The vertical-integration audit (`docs/formal/R3_NS_VERTICAL_INTEGRATION_STATUS.md`,
  README/STATUS frontier synchronization) is commit `7c6c8d8`; the BH reopen pass
  (`docs/gates/BH_QUANTITATIVE_RIGIDITY_K12_AUDIT.md`) follows it. Docs-only commits; no
  Lean source touched; the 8756-job gate remains the verification baseline.
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

Third pass (2026-08-19): adversarial audit + kill table —
`docs/gates/D1_ADVERSARIAL_AUDIT_2026-08-19.md`, `docs/gates/TYPE2_KILL_TABLE_2026-08-19.md`.
Outcomes:

- **[D1] withdrawn** (the `ρ < 1/2` CKN-cylinder kill was unsound: ε-regularity gives no
  uniform scale-invariant bound at the visited scale); replaced by the conditional transport
  cut [D1′] `ρ ≥ min(1−γ, 1/2)`; the on-axis blob window is unaffected; corrections
  propagated to the map document, figure footnote, and the lab registry entry;
- CSTY-II verified verbatim (arXiv:0709.4230): `|v| ≤ C_* r^{−1+ε}|t|^{−ε/2}` ⇒ regular,
  `C_*` arbitrary — inside the blob window its violation is automatic (no new cut); for
  rings it forces `γ > ρ` or a mesoscale violation region;
- conditional swirl razor (K9, unverified family): if `|u_θ| ≤ C r^{−d}` (`d < 1`) implies
  regularity, then the core swirl exponent is pinned to `σ = α` exactly — an
  amplitude-subdominant core carrying `O(1)` circulation `Γ`;
- **dimension answer**: after all currently-verified cuts, `S_survive` = a 2-D open wedge
  (blob) + a 3-D conditional slab (ring, `γ < 1` for core-carried `L³`) + the ≥3-region
  corridor — not a curve, not empty;
- **verification debts** (the next cheap theory items): K4 (KNSS exact `|v| ≤ C/r` form),
  K9 (exact swirl-component criteria), K10 (full-text extraction of Seregin
  arXiv:2402.13229, revised 2026-08 — the area is actively moving).

Fourth pass (2026-08-19): debts settled, map frozen, dominant-balance inversion done —
`docs/gates/DOMINANT_BALANCE_INVERSION_2026-08-19.md` and updated kill table / figure.

- K4 retired (non-load-bearing; verified K3 covers the map's uses); K9 paid
  (Chen–Fang–Zhang weighted swirl criterion; the `σ = α` core razor holds at the `L^∞`
  endpoint); K10 paid — **Seregin's Euler-scaling Type II class maps exactly onto the
  `γ + α = 1` edge, `γ ∈ (1/2, 3/5)`**, with conditional exclusion pressure there.
- New cut **K11: `γ + α ≥ 1`** (term balance and energy-flux derivations agree). Frozen
  window: `{1/2 < γ < 1, max(1−γ, 2γ/3, 2γ−1) ≤ α < γ}`.
- Balance classification: edge = generalized self-similar Euler (contested); interior =
  quasi-static steady-Euler (Bragg–Hawthorne) cores, slowly modulated; heat balance,
  `∂ₜ`-dominant dynamics, and convection–diffusion-balanced `L³`-carrying cores are all
  impossible in the wedge. Every survivor is asymptotically inviscid (`Re_core → ∞`).
- Deferred by plan (do NOT start yet): N-level harness, Stage B modulation/trapping
  formalization, new ansatz generation, non-axisymmetric pivot, further literature
  excavation. The one recorded research question for later: do Bragg–Hawthorne profiles
  compatible with `σ = α`, `O(1)` circulation, and the wedge exponents exist?

Fifth pass (2026-08-19): BH-profile taste pass (one bounded pass, per the external
reviewer's brief) — `docs/gates/BH_PROFILE_TASTE_REPORT.md`,
`experiments/bh_taste_exponents.py`. **Verdict: YELLOW.**

- Gate A: Gavrilov / Constantin–La–Vicol verified (localized steady Euler cores with swirl
  exist at fixed swirl fraction); Jiu–Xin rigidity verified at search level (compactly
  supported axisymmetric no-swirl steady Euler ⇒ 0).
- Gate B: fixed-profile scaling is a double no-go (`σ = γ` and `Γ → ∞`; circulation-tuned
  variant gives `γ = α`).
- Gates C/D: in core variables the swirl enters Grad–Shafranov at `O(ε²)`; a regular
  `ε → 0` family would converge to a nontrivial localized no-swirl flow — dead by
  rigidity. **Any admissible family must be singular**; existence unconstructed.
- Gate E: residual hierarchy formally perturbative in the interior; closed-streamline
  secular (Prandtl–Batchelor-type) argument obstructs `α ≥ 1/2` (homogenized `Γ` ⇒
  `F̂′ → 0` ⇒ swirl decoupling ⇒ no-swirl rigidity again). Proposed conditional K12
  (report-only, NOT applied to the frozen map): quasi-static interior needs `α < 1/2`.
- Smallest missing theorem: **quantitative no-swirl rigidity** (the forced degeneration
  rate of swirl-poor localized families). Deferred; do not start without a fresh decision.

**Resume point: return to the Lean program (next gate below — operator realness
preservation), per the frozen plan. Standing decision (2026-08-19, user-approved): once the
continuation criterion is closed on the Lean side, the BH branch reopens — i.e. the
quantitative no-swirl rigidity question and the K12 decision from
`docs/gates/BH_PROFILE_TASTE_REPORT.md` become the next Stage-A item at that point.**

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
(FORMAL_SCOPE section 6, next gate 1). Slice 1 is **closed** (2026-08-19,
`Formal/R3StokesConjugationEquivariance.lean`, full gate 8748 jobs, axiom audit standard):
the generic theorems `reflect_conj_of_realEven_multiplier` (frequency side) and
`r3L2Conj_of_fourier_realEven` (physical side, via the Plancherel bridge and injectivity)
plus symbol realness/evenness give
`r3L2Conj_r3StokesL2Operator`, `r3L2Conj_r3StokesH3Evolution`,
`r3L2Conj_r3StokesH2ToH3Operator`, and the `IsR3RealVelocity` preservation corollaries.
Reuse `r3L2Conj_of_fourier_realEven` for every further scalar-multiplier operator
(including the Bessel weights / decoders if needed).

**The operator-realness gate is now FULLY closed** (2026-08-19). Slice 2
(`Formal/R3LerayConjugationEquivariance.lean`): fiber-level conjugation equivariance and
evenness of the complex Leray symbol, the matrix-multiplier generalization of the generic
equivariance theorems, `r3L2Conj_r3LerayL2Operator` plus the definitionally-equal order-two/
order-three variants, and the `IsR3RealVelocity` corollaries. Slice 3
(`Formal/R3ConvectionConjugationEquivariance.lean`): carrier antilinearity `r3L2Conj_smul`;
conjugation equivariance of real even Schwartz Fourier multipliers and hence of the Bessel
coordinate map (`r3L2Conj_r3SchwartzToHsCLM`); conjugation equivariance of the Schwartz
convection (via `fderiv` commuting with the real-linear fiber conjugation); the
triple-conjugated bilinear map `r3ConjugatedConvectionH3ToH2` (ℂ-bilinear again by three
conjugations), shown equal to `r3ConvectionH3ToH2` by the dense-core uniqueness theorem;
hence `r3L2Conj_r3ConvectionH3ToH2`, `r3L2Conj_r3ProjectedConvectionH3ToH2`, and
`IsR3RealVelocity.projectedConvection`.

**The real local mild solution is closed** (2026-08-19,
`Formal/R3RealLocalMildSolution.lean`): conjugation equivariance of the endpoint-safe
Duhamel integrand (`r3L2Conj_r3EndpointSafeProjectedDuhamelIntegrand`), the conjugated
trajectory of a mild solution with real datum is again a mild solution
(`IsR3EndpointSafeProjectedMildSolutionOn.r3L2Conj_comp`, using
`ContinuousLinearMap.intervalIntegral_comp_comm` to pass conj through the Bochner
integral), and — by the ball-uniqueness clause, with **no new fixed point** —
`r3EndpointSafeProjected_exists_realLocalMildSolution`: for `ν > 0` and physically real
`u0`, a horizon `0 < T ≤ 1` and a mild solution that is **physically real at every
certified time**, with the ball bound and ball uniqueness.

**The explicit quantitative lifespan is closed** (2026-08-19,
`Formal/R3QuantitativeLifespan.lean` + refactor of `Formal/EndpointSafeTwoSpacePicard.lean`):

- abstract layer: `exists_isMildSolutionOn_of_kernelPrimitive_lt` — existence + ball bound +
  ball uniqueness on **any** given horizon `T > 0` with
  `kernelPrimitive T < δ(‖u₀‖) = min (1/(‖B‖(R)²+1)) (1/(2(‖B‖·2R+1)))`, `R = ‖u₀‖+1`;
  the old existential `exists_pos_time_isMildSolutionOn` is now a corollary (statement
  unchanged);
- closed-form kernel mass: `r3EndpointSafeProjected_kernelPrimitive_eq` —
  `K(T) = T + √T/(π√ν)` for `T ≥ 0` (via `integral_rpow` at exponent `-1/2` and
  `√((2π)²ν) = 2π√ν`);
- explicit lifespan: `r3MildLifespan nu r = (δ(r)/(1 + (π√ν)⁻¹ + δ(r)))²` with
  `r3MildLifespan_pos`, `r3MildLifespan_le_one`, and the key inequality
  `r3EndpointSafeProjected_kernelPrimitive_mildLifespan_lt` (`K(T₀) < δ`, algebra:
  `K(T₀) = √T₀(√T₀ + c)` and `√T₀ = δ/(1+c+δ) ≤ δ < 1+δ`);
- quantitative existence: `r3EndpointSafeProjected_exists_mildSolutionOn_mildLifespan`
  (complex carrier) and `r3EndpointSafeProjected_exists_realMildSolutionOn_mildLifespan`
  (physically real data ⇒ pointwise-real solution), both on the explicit horizon
  `T₀(ν, ‖u₀‖)` depending only on the viscosity and the initial-datum norm.

**The mild restart identity and unrestricted uniqueness are closed** (2026-08-19,
`Formal/EndpointSafeTwoSpaceRestart.lean` + `Formal/EndpointSafeTwoSpaceUniqueness.lean`):

- restart (`IsMildSolutionOn.restart`, concrete
  `IsR3EndpointSafeProjectedMildSolutionOn.restart`): a mild solution restarted at a
  certified time `s` solves the shifted mild equation on `[0, T-s]` with datum `u s` —
  proof splits the Duhamel integral at `s`, pushes the linear evolution out of the head
  piece by `smoothing_coherent` (a.e.; the endpoint `σ = s` is null), and translates the
  tail by `σ ↦ s + σ` (`duhamelIntegrand_comp_add_left`, everywhere, no null set);
- contraction step (`isMildSolutionOn_eq_of_contraction`): two `R`-ball solutions with the
  same datum agree when `‖B‖·2R·K(T) < 1` — max of the difference norm on the compact
  horizon satisfies `M ≤ θM`, no fixed-point machinery;
- **`IsMildSolutionOn.unique` / `r3EndpointSafeProjectedMildSolution_unique`**: two mild
  solutions with the same datum agree on their common horizon, with **no ball
  restriction** (continuity gives a common bound `R`; small-time smallness gives a step
  `T_s` with contraction; restart + induction walk the agreement window; Archimedes ends);
- free corollary (`IsR3EndpointSafeProjectedMildSolutionOn.isR3RealVelocity`):
  **every** mild solution with physically real datum is pointwise physically real
  (the conjugated trajectory is a solution with the same datum; unconditional uniqueness
  pins it) — no ball hypothesis anywhere.

Lean tooling note for these files: rewriting under `ℝ≥0` anonymous-constructor arguments
(`⟨τ, hτ0⟩`) breaks `rw`'s motive check under `instances` transparency; use
`congr 1` + `exact`, `congrArg` on operator equalities, and applied congruence lemmas
(`positiveSmoothing_congr_apply`) instead. Dot notation on contract theorems must pass the
contract explicitly (`hu.restart C hs`), since `C` precedes the self argument.

**The maximal-continuation layer is closed in blow-up–dichotomy form** (2026-08-19,
`Formal/EndpointSafeTwoSpaceConcatenation.lean` + `Formal/R3MildContinuation.lean`),
completing the endorsed 3-gate plan:

- concatenation (`IsMildSolutionOn.concat`, concrete
  `IsR3EndpointSafeProjectedMildSolutionOn.concat`): a mild solution on `[0,s]` followed
  by a mild solution from the reached state glues to a mild solution on `[0, s+T']` — the
  restart computation in reverse (head piece absorbs the evolution by
  `smoothing_coherent` a.e., tail piece is the translated Duhamel integral; glued
  continuity via `ContinuousOn.union_of_isClosed`);
- `r3MildLifespan_antitone`: the explicit lifespan is antitone in the datum norm, so one
  bound `R` yields a uniform positive step `r3MildLifespan ν R`;
- `r3EndpointSafeProjected_exists_extension_of_bounded`: an `R`-bounded mild solution on
  `[0,T]` extends to `[0, T + r3MildLifespan ν R]`;
- `r3MildHorizons` (the set of certified horizons for a datum), nonempty by the explicit
  lifespan; `r3EndpointSafeProjected_horizons_unbounded_of_uniform_bound`: a uniform norm
  bound on all certified solutions forces the horizon set to be unbounded (a horizon
  within one uniform step of the supremum would extend past it);
- **`r3EndpointSafeProjected_blowup_dichotomy`**: either arbitrarily long horizons carry
  mild solutions, or the certified solution norms escape every ball.

Lean tooling note (in addition to the `ℝ≥0`-mk note above): rewriting under an applied
if-lambda trajectory fails because `rw` sees the unreduced application — insert
`show <beta-reduced form>` before rewriting; and `congr 1` can close subgoals via
`assumption` when the needed equality is in context, so prefer explicit `congrArg` when a
following tactic expects remaining goals.

**The 2026-08-19 vertical-integration audit + BH reopen pass is complete** (multi-agent
adversarial pass; deliverables `docs/formal/R3_NS_VERTICAL_INTEGRATION_STATUS.md` and
`docs/gates/BH_QUANTITATIVE_RIGIDITY_K12_AUDIT.md`; README/STATUS synchronized):

- vertical integration verdict: **CHAIN CLOSED TO CONTINUATION** (README was stale, the
  mathematics was closed); 5 required semantic edges remain to the official Clay
  statement (Bucket A of the status doc);
- BH verdict: **YELLOW** (grade unchanged, content replaced). The baseline power-vs-log
  dichotomy is retired as ill-posed; the smallest missing theorem is now the
  **swirl-fraction gap (★)**: for compactly supported axisymmetric steady Euler flows,
  is `inf s(u) > 0`, `s(u) = ∫|u_θ|²/∫|u_pol|²`? (`inf s > 0` ⇒ RED for blob *and*
  ring; a family with `s → 0` ⇒ YELLOW-GREEN.) One new hard result: the exact
  momentum-flux identity `∫u_r² + ∫u_θ² = 2∫u_z²` for localized steady axisymmetric
  Euler [H], equivalent form of (★). K12: **KEEP CONDITIONAL** (route (F) closed for
  `α > 1/2` up to a separatrix-sliver caveat; route (P) narrowed but open; `α = 1/2` is
  a grey line; ring corridor untouched — planar rigidity is false). Report-level
  annotations K12′/K12″ recorded; frozen map unchanged; K9 two-scale verification debt
  logged.

**The (★) P0 probe is complete** (2026-08-19,
`docs/gates/BH_SWIRL_FRACTION_PROBE_2026-08-19.md`; Gavrilov + CLV primary texts read in
full; verdict **YELLOW, content inverted twice**):

- published constructions pinned: `σ(A) = 1/2 − (21/32)A`, `s = 1/2 − (21/16)δ²` [H]
  (core swirl fraction 1/3 forced four ways, incl. CLV (52) [V]);
- but the corrected range is `(0, 1/2]`: continuing the same solution to its Hill-type
  separatrix and cutting a thin shell there gives an explicit candidate family with
  `σ ≃ 0.82√(A_H − A) → 0` [C on one continuation lemma] — **(★) as stated is likely
  answered NO** (`inf s = 0` over the naked A_NS);
- **but the branch does not go GREEN**: the realizing family (`r_min/R ~ s`, sheet
  thickness `~ s²`) is below the viscous cutoff `√(ντ)` on the whole interior blob
  wedge [C] — **(★) is decoupled from the branch verdict**; the decision object is now
  **(★_geo): `s(u) ≥ c·(r_min/r_max)^θ`** on the localizable class (θ = 1/5 proved
  per-streamline; θ ≥ 1/2 would empty the interior blob wedge; the explicit family sits
  at θ = 1);
- A_NS minimally defined (A1–A5; no normalization needed; a priori `q ≤ 2`);
  CLV F → 0 classified: F ≡ 0 dead [H, redundant vs Jiu–Xin]; radially thin pinned at
  `s = 1/2`; wide-aspect corridor = SURVIVING FAMILY (conditional); Scope B
  (non-localizable) open and decisive; stagnant-axis structural fact proved [H].

**The (★_geo) geometry gate is closed — Outcome A, θ = 1, sharp** (2026-08-19,
`docs/gates/BH_GEO_SWIRL_AGGREGATION_2026-08-19.md`; erratum appended to the P0 probe;
verdicts **GEO-RESTRICT / YELLOW-RED / CAP: DO NOT START**):

- **THEOREM [H, Scope A]**: on every regular closed poloidal streamline (`A > 0`) of a
  `p = p(ψ)` steady axisymmetric Euler flow, `s_level ≥ δ(ψ)/157` and
  `α/r_min² ≥ 1/42`; globally `s(u) ≥ (1/157)·δ_geo(u)` with
  `δ_geo = ⟨r_min(ψ)/r_max(ψ)⟩_{E_pol}` (barycentric; aggregation lossless). Convexity
  hypothesis retired; ω-machinery off the critical path (one-parameter elliptic-orbit
  rigidity: `s_level` is *determined* by `δ`); θ = 1 sharp at level scale [H], flow
  scale [C] (shell family sits exactly on the bound);
- frozen substitution: pure-geometry Prop G (`E = 2γ − α > 1/2` on the whole wedge, no
  contradiction from Euler alone) strictly separated from Prop V [C] (under the
  unpromoted V1 viscous premise the interior blob wedge empties; exact threshold θ < 4,
  correcting "θ ≤ 2"); **nobody may cite this as "blob dead"** — Scope A + V1 gates;
- **ring corollary [C, single-sourced, unverified]**: thin ring ⇒ δ(ψ) → 1 uniformly ⇒
  s ≥ c > 0, contradicting `s_ring → 0` — viscosity-free, θ-independent; contradicts
  the recorded "ring corridor has no rigidity kill";
- armed falsifier P6 (A↔σ dictionary, one number, [C-num]); sharp constant at σ*
  uncomputed (cosmetic).

**The ring corollary is verified and the scope freeze is executed** (2026-08-19,
`docs/gates/BH_RING_COROLLARY_ADVERSARIAL_AUDIT_2026-08-19.md`; verdicts
**RING-ONE-SCALE-KILL / YELLOW-RED / NEXT: MULTI-REGION AUDIT**; map annotation
authorized and appended to `TYPE2_KILL_TABLE_2026-08-19.md` with riders R1–R4):

- **certified kill (amplitude/circulation form, cheaper than the energy route)**: Scope-A
  top-speed level has `r_min ≤ √3·Γ₀/‖u‖_∞·(1+o(1))` (thin-endpoint pinning
  `u_θ² = |u|²/3`, three independent derivations) ⟹ contained one-scale ring forces
  `ρ ≥ γ` — contradiction with K3 *and* (via `ρ+2α ≥ 3γ`) K6; doubly sourced,
  viscosity-free, compactness-free, non-vacuous (`(0.6, 0.42, 0.45)` ∈ S_ring killed);
- **exact map wording (nothing broader)**: "one-scale localizable ring branch excluded by
  swirl-geometry pinning";
- **Scope B is a GAP, not an exit** [H, witness-backed]: Hill's spherical vortex is a
  steady axisymmetric Euler flow with `s_level ≡ 0` — the geometry-gate conclusion is
  false outside Scope A; `p = p(ψ)` is added and not removable. Sharp open question:
  must a *localized* steady axisymmetric Euler core with swirl satisfy the eikonal
  overdetermination `|∇ψ|² + F² = 2A(ψ)r²`?
- **"blob dies too" REFUTED**: Scope A relocates the swirl sup to the axis-grazing
  tongue tip (`r_min ≲ τ^γ`), where `Γ = O(1)` saturates; K9's `σ ≤ α` is a
  sup-location premise, not a theorem there — blob unchanged, still V1-conditional; new
  K9 debt (P6) logged in the map annotation;
- errata appended (not silently repaired): geometry-gate §8 global-`s` sentence
  withdrawn (amplitude form replaces it), `k = −P′/2` (P6 falsifier must be re-derived
  before evaluation), `α_g` notation; taste report §3 is the MHD GS form (`P = −B`).

**The multi-region audit is complete** (2026-08-20,
`docs/gates/BH_MULTIREGION_AUDIT_2026-08-20.md`; per-class verdicts **M2 RESTRICTED (no
independent members — "not a ring branch") · M3 OPEN · B2 RESTRICTED**; BH
**YELLOW-RED held**; next branch **FREEZE REVIEW**):

- K3 is a covering condition (concave min; middle-ε gap witness); K9 reduces to
  Γ-saturation and is a **trichotomy** in the saturation scale (`β_v = α` printed /
  `β_v ∈ (α,γ]` intra-core, unanalysed / `β_v < α` separate region); the map's `σ` is
  ill-posed for on-axis cores (`σ_core` vs `σ_sup`; in Scope A `σ_sup = γ` always);
- amplitude gate on multi-region flows: the second scale is **capped** (`ρ_T ≥ γ`),
  not pinned; every Scope-A blob is two-scale in the tongue sense; the tongue's energy
  share `→ 0` so **V1 does not bite it**; the Gate-C sacrifice is selected: uniform
  `C¹` fails at rate `1/ε`;
- **the interlock (highest value)**: amplitude-gate silence ⟺ K3 middle-ε gap ⟺ M3's
  swirl-dominated core — one object, covered exactly by the **retired row K4** (KNSS
  `|v| ≤ C/r`), whose retirement rationale is FALSE (`ρ=σ=γ` violates K3 for every ε
  yet obeys `|u| ≤ C/r`). **M3's blocking question = does KNSS bite the Γ-saturated
  core?** Only a freeze decision can re-arm a retired row;
- **P6 falsifier RESOLVED: PASS** (symbolic; `k` cancels; corrected
  `X = (1/3)(1−7σ²/16)`, test number `21/64 = 21/64`; retired: `23/32`, `0.5391`;
  residual [V?]: the `δ_probe = ℓ/R` reading);
- literature: Jiu–Xin verbatim abstract secured [V] (C¹, finite energy + constant far
  field; **no "no swirl" in the abstract** — body must carry it, debt sharper, not
  paid); **DVEP (arXiv:2005.04380, ARMA 2021) = Scope-B witness at weak regularity**
  (compactly supported, axisym-with-swirl, piecewise smooth, explicitly not
  localizable) — necessity of `p = p(ψ)` is false without a regularity hypothesis;
  the geometry gate's §10 trigger **as worded is met** (freeze review must fire or
  amend to primary-class wording); Peralta-Salas–Slobodeanu 2026: analytic localizable
  ⟹ axisymmetric (overdetermination reading confirmed);
- corrections queued for the freeze review: Prop G/V carry the far-field erratum
  (repair: per-level + Markov inside core energy, `E = 2γ−α` stands in weakened form);
  `S_blob` boundary `α > 2γ−1` strict; [D2] "≥3-regions" over-count (min 2).

**The M3 × KNSS gate is answered** (2026-08-20,
`docs/gates/BH_M3_KNSS_GATE_2026-08-20.md`; the K4 verification debt is PAID first-hand
from arXiv:0709.3599 full text):

- **Answer: NO** — frozen M3 (`γ₂ ≤ γ`) does not imply KNSS's global `|v| ≤ C/r`; the
  defeating member is the **amplitude-tie face `γ₂ = γ`**, whose ancient limit contains
  a non-decaying plateau = KNSS's own `u = b(t)` obstruction (their receding-axis
  branch is Type-I-only [V]);
- **but `M3 ∩ {γ₂ < γ}` DIES** [D, Scope-A-free, viscosity-free, conditional on (E)
  dictionary-exhaustiveness + (P) class transfer]: the L³ carrier's `C/r` violation
  escapes the `τ^γ` zoom, Prop 6.1 is amplitude-normalized and **rate-free (Type II is
  the enabler, not the obstruction)**, Thm 5.3 kills the limit;
- the tie face has `(γ, α₂) ∈ S_blob` by pure exponent arithmetic — **it is a B2 point
  wearing a Γ-saturated sub-core**: M3 moves **OPEN → RESTRICTED (no independent
  members)**; **the Scope-A open set contracts to B2 alone** (blockers: V1 [C] +
  quantitative rigidity rate);
- map queue additions (freeze review): K4 restore [V] with Thm 6.1 + rider
  (`K₄ ∩ M3 = ∅` — K4 never applies to the unzoomed flow); new conditional row K4′
  ("amplitude-normalized ancient limit decays like 1/r ⟹ regular", kills
  `M3 ∩ {γ₂ < γ}` mod (E)+(P)); elongated-filament one-region M3 (P5, cleanest K4′
  target); K5-not-scale-invariant legend (P7); K2 row corrections.

**The constant-exclusion pass is complete** (2026-08-20,
`docs/gates/BH_CONSTANT_EXCLUSION_ROW_2026-08-20.md`; ruling PARTIAL — better than
either hoped-for outcome):

- **branch (a) is RETIRED, not open** [D, row R-A]: KNSS Lemma 6.1 nowhere requires
  `C = 1`; re-centring the zoom on the Γ-saturated level (amplitude corollary,
  `C = √42`) keeps the axis at bounded rescaled distance — the limit is axisymmetric
  with a Γ-saturated core, for **every** Scope-A blob, B2 included. Branch (a) was an
  exact-maximizer artifact. (Boost-the-original refuted, R-NEG1; constants cannot be
  excluded by any scale-invariant estimate at an axisym singularity — Ożański–Palasek
  — but re-centring makes that moot, R-NEG2);
- **everything reduces to ONE literature-named open object (OO)**: nonzero bounded
  ancient mild axisymmetric NS solution with `Γ ∈ L^∞`, `Γ ≢ 0` (the survey's "most
  difficult remaining case");
- **certified primary conditional row R-B1 [V+C]**: Lei–Zhang JFA 2011 Thm 1.2
  (bounded weak ancient + `r|v_θ|` bounded + **stream function BMO** ⟹ `v ≡ 0`).
  Every hypothesis transfers FREE (Γ is exactly scale-invariant under the Prop-6.1
  zoom — new unconditional row K4‴) except **BMO of the boosted limit's stream
  function** — one hypothesis, one logarithm of slack over the (Q)-form. If
  discharged: **the tie face AND B2's Γ-saturated blob die — no Type-I, no viscosity,
  no Scope-A geometry**;
- (E) ⟹ (Q) holds but needs **(E⁺)** (adds C¹-exhaustiveness near the zoom centre);
  escalation: charging (E⁺) kills the tie face at the same strength as `γ₂ < γ`;
- freeze-review queue extended: K4′ amend to (E⁺); new rows K4″ [C] and K4‴ [D]; P7
  legend (`Γ ∈ L^p, p<∞` non-descending); KNSS implicit-(6.16) footnote; negative
  rows; branch wording ("M3 tie face and B2 reduce to one object (OO)").

**The Biot–Savart deviation ledger is complete — R-B2 DISCHARGED on the frozen
dictionary** (2026-08-20, `docs/gates/BH_BIOT_SAVART_LEDGER_2026-08-20.md`, tag [C]):

- `r_y|w_pol| ≤ C` τ-uniform on the receding ball `R₀ ≤ |y| ≤ R_k = ε₀τ^{(β−γ)/2}`
  (β = finest non-local gradient exponent: α for B2, ρ₂ for the tie face) ⟹
  `|w| ≤ C/r` globally on the re-centred ancient limit ⟹ **KNSS Thm 5.3 ⟹ w ≡ 0 ⟹
  Γ ≡ 0 — contradiction with the Γ-saturated core ⟹ M3 tie face AND B2's Γ-saturated
  blob excluded** (no Type-I, no viscosity, no energy, no Scope-A geometry, no V1);
- conditionals: **(E⁺⁺)** [C] (the tongue's `ω_θ` content is the core's — its recorded
  vorticity excess is `∇Γ`-generated `ω_r/ω_z`, invisible to the poloidal kernel) +
  (P) [C] + (N-Γ) [C-dict]. The kill routes through **KNSS 5.3, not Lei–Zhang**;
  R-B1's "one log of slack" REFUTED (BMO-stream ⟺ `w ∈ BMO^{-1}`, zero logarithms);
- **the debt is localized, not erased**: the single remaining substantive conditional
  is one exponent — the named negation witness **(NECK)** (poloidal shear layer of
  amplitude order riding the tongue's sub-saturated stretch; defeats both rows at rate
  R; dictionary-extension, inadmissible as a class member; exactly what (E⁺⁺)
  excludes);
- kernel formula sheet [H] established (monopole absent in far zone; axis-straddling
  2-D window empty; `b_τ` axial by derivation); corrections queued: gate's
  `r|u_pol| ≲ 1` is exterior-tail only (F5); tongue `‖ω‖` not chargeable to the
  poloidal kernel (F6); freeze queue F1–F8 with exact wordings.

**The neck ω_θ-budget is complete** (2026-08-20,
`docs/gates/BH_NECK_OMEGA_BUDGET_2026-08-20.md`; ruling: **outcome (b) in its
general clause — δ_T itself REFUTED**, three independent routes):

- the exact budget identity is established, twice-derived (2-D conservation form +
  Kelvin/winding): stretching = 2-D compressibility defect, cancels identically;
  **viscosity is a pure boundary flux with no sign (T4)** — the claimed bulk sink
  `−ν∫ω_θ/r²` does not exist (R-NEG4); production is oscillation-controlled,
  `|∮(Γ²/r³)dr| ≤ ½ osc_R(Γ²)(r₁^{−2}−r₂^{−2})`, δ-free in both tongue orientations;
- **δ_T is permanently removed from the branch** (F10) — not the missing exponent;
- **the missing exponent is a coherence time (COH)**: (E⁺⁺) ⟺ `θ_coh(ρ) ≥ 2ρ` on
  `ρ ∈ [(γ+α)/2, γ]`; below threshold (NECK) is reachable at damage rate
  `R = τ^{ρ−γ}`. Reference horizons: turnover `ρ+γ` (clears, ν-free), viscous `2ρ`
  (exactly marginal), lifetime `1` (fails everywhere on the neck — K11 `γ+α ≥ 1`
  says precisely that the whole neck is inside `√(ντ)`);
- with the full-lifetime horizon the budget is **vacuous on all of S_blob**
  (R-NEG3): both proposed exponent wedges refuted (`α+3γ<2` empty under K11;
  `γ+3α<2` outer-endpoint-only — W3 truncated sheet at `R* = τ^{(1−2γ)/3}`);
- **tag: (E⁺⁺) stays [C]**; both analyst outcome-(a) verdicts rested on undischarged
  viscous inputs; not ruled (c) — W3 is a negation witness only; (NECK) refined to
  any dyadic-annulus sheet at `R ≤ min(R*, R_k)`;
- freeze queue extended with **F9–F14** ((E⁺⁺) re-worded to the κ-form actually
  consumed, F12; `R₀` constant mismatch, F14).

**The (COH) winding pass is complete** (2026-08-21,
`docs/gates/BH_COH_WINDING_2026-08-21.md`; 3 analysts + 2 independent verifiers +
critic, outcome (ii) **unanimous and provenance-clean**):

- **(COH) not discharged at any radius; the winding form is RETIRED as a discharge
  vehicle** (structural + input starvation — residence, confinement, fold count,
  material preimage — but NOT proved impossible); (E⁺⁺) stays [C]; R-B2′ unchanged;
- **headline [D]: the INCREMENT/LEVEL GAP — the frozen (COH) "iff" is WRONG.**
  Budget and winding routes bound only `|κ̂(t) − κ̂₀|`; (E⁺⁺) needs `|κ̂(t)| ≤ C`;
  on the ancient limit there is no anchor, and the dictionary's only level bound at
  neck radii is the contour form `|κ̂| ≤ CR` — exactly (NECK) level. `θ_coh ≥ 2ρ`
  is **necessary but NOT sufficient**. The debt splits into TWO objects:
  **(COH-Δ)** (coherence, as printed) + **(ANCH)** (level/erasure for `κ̂`, carried
  only by T4 since there is no bulk sink — R-NEG4 re-verified by a fifth route);
- persistence ruled explicitly: "(NECK)-level `κ̂` present initially and
  persisting" is neither excluded nor forced (the adversary's "forced below ρ*"
  refuted); it does not re-open R-B2 (already conditional on (E⁺⁺)) but enlarges
  what a discharge must deliver;
- method facts to [C-dict]: exact winding identity (second viscous term cancels ⟹
  T4-only ledger confirmed); osc hint vacuous (`min(Γ₀, rτ^{−γ}) = Γ₀` identically
  on the neck — zero exponent); exponent equivalence (power-for-power with the
  production budget; R-NEG3 by a second route); **no Lagrangian localization**
  (Eulerian transfer licensed only on the turnover horizon — circular; F18);
- cumulative-free edge real but inert: `TV_s(θ)` is an unassigned Lagrangian
  geometric quantity with no maximum principle — sign-coherence debt converted to
  geometric debt, same size;
- freeze queue extended **F15–F20** (F16 = correction to frozen text: F11
  superseded; R-NEG5/R-NEG6; T4 = named unassigned input, sole carrier of (ANCH);
  witnesses W4/W6, renumber W5).

**The FREEZE REVIEW is EXECUTED** (2026-08-21, user's fork-(β) adjudication
received verbatim and applied; master record
`docs/gates/FREEZE_REVIEW_2026-08-21.md` (31-row adjudication table) + authorized
annotation A1–A20 appended to `docs/gates/TYPE2_KILL_TABLE_2026-08-19.md`; both
audited by a 3-lens Opus workflow — adjudication fidelity / source consistency /
completeness — all blockers and errors fixed before commit):

- **fork (β)**: the frozen dictionary **declines** the neck poloidal level bound,
  `sup(ω_θ/r)`, and `ℓ_neck` — nothing was invented at the review;
- adopted: σ_core/σ_sup split (A1); K9 saturation-scale trichotomy, `β_v ∈ (α,γ]`
  an open debt (A2); K6 [D2] "≥2 regions" under power-law `L³` (A3); Prop G/V
  per-level+Markov repair (A4); P6 `7/16`/`21/64` symbolic PASS + residual [V?]
  (A5); **K4 restored [V]** with the zoom-route-only rider and an explicit
  no-corridor-coverage clause (A6); `S_blob` `α > 2γ−1` strict (A7); §10 trigger
  amended in its Scope-B limb only — `A_NS`-internal witnesses; DVEP no fire (A8);
  K4′ [(E⁺)+(P)] (A9); K4″ ≡ R-B1 demoted to redundant confirmation (A10); K4‴
  (A11); P5 corollary-only (A12); P7 (A13); K2 correction (A14); **R-B2′ primary
  row [C]** with the full chain incl. `v = b·e_z` (A15); **(E⁺⁺) = (COH-Δ) +
  (ANCH)** κ-form + symbol legend (A16); ledger F5–F8 (A17); R-NEG1–R-NEG6
  (A18); winding retirements + `ℓ_neck` ≠ ledger-`β` disambiguation (A19);
  residuals incl. W6→W5 renumber, F15-conflict resolution, `R₀`-as-two-objects
  (A20);
- **post-freeze frontier (frozen)**: M2 RESTRICTED · M3 RESTRICTED · Scope-A
  quasi-static = **B2 alone**, killed by R-B2′ [C] on (COH-Δ)+(ANCH)+(P)
  (+(N-Γ) [C-dict]); (NECK) = standing dictionary-extension request (`θ_coh`,
  `ℓ_neck`); **all three in-house vehicles retired/blocked** (budget/winding;
  level route; T4-with-a-sign). BH **YELLOW-RED maintained**; no CAP trigger.

The next branch is the **user's choice** (no default asserted; freeze-review
record §7):

1. **Scope-B reconnaissance** — the recorded runner-up, strictly cheaper now that
   the §10 trigger wording is fixed (A8): survey what exists outside
   `p = p(ψ)`-localizability at weak regularity (DVEP-adjacent literature), no
   theorem attempts.
2. **Return to the formal (Lean) side** — the 5 Clay semantic-promotion edges
   (Bucket A of `docs/formal/R3_NS_VERTICAL_INTEGRATION_STATUS.md`) and/or the
   glued maximal trajectory `u*` with pointwise `limsup ‖u*‖ = ∞`.
3. Deliberately deferred list unchanged (intra-core `β_v` branch; K8/K10 on
   multi-region tuples; Jiu–Xin body; separatrix lemma; ζ-averaging / K12″).
3. deliberately deferred: intra-core `β_v ∈ (α,γ]` branch; K8/K10 on multi-region
   tuples; coexistence/one-pressure vocabulary limit; Jiu–Xin body (paywalled);
   separatrix continuation lemma; ζ-averaging / K12″; optional formal refinement
   (glued maximal trajectory u*; interface adapters — not blockers).

The closed layers are local statements on the Bessel-coordinate carrier (complex, and real
via the conjugation gate). No pressure reconstruction, no unconditional uniqueness, no
continuation criterion, and no Clay statement is available yet.

## Latest Lean verification

```text
runner: local Windows (Git Bash) process via Elan
revision: working tree of the maximal-continuation commit on main
  (new: Formal/EndpointSafeTwoSpaceConcatenation.lean, Formal/R3MildContinuation.lean;
   extended: Formal/AxiomAudit.lean)
toolchain: leanprover/lean4:v4.32.1
dependency manifest: committed lake-manifest.json; mathlib per lake-manifest.json
target scope: lake build Formal.EndpointSafeTwoSpaceConcatenation /
  Formal.R3MildContinuation — pass, no new warnings
full scope: lake build (Formal.+ default target) — pass (8756 jobs)
source scan: pinned sorry/admit/axiom/opaque scan over changed files — clean
axiom scope: Formal.AxiomAudit — pass; all eight new audited declarations
  (IsMildSolutionOn.concat, IsR3EndpointSafeProjectedMildSolutionOn.concat,
   r3MildSmallnessThreshold_antitone, r3MildLifespan_antitone,
   r3EndpointSafeProjected_exists_extension_of_bounded, r3MildHorizons_nonempty,
   r3EndpointSafeProjected_horizons_unbounded_of_uniform_bound,
   r3EndpointSafeProjected_blowup_dichotomy)
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
- `IsR3RealVelocity` / `IsR3ConjugateSymmetricVelocity` are related through the Plancherel
  `L²` Fourier transform; every concrete operator of the mild theory is
  conjugation-equivariant and realness-preserving; the local mild solution is physically
  real for physically real data — now **unconditionally** (every mild solution with real
  datum is pointwise real, no ball hypothesis). Still missing: the glued maximal
  trajectory with pointwise blow-up (the certified-horizon dichotomy IS formalized),
  pressure reconstruction, and any Clay statement;
- uniqueness is now **unrestricted** on a common horizon
  (`r3EndpointSafeProjectedMildSolution_unique`); the ball-uniqueness clauses of the older
  existence theorems remain valid but are superseded;
- the horizon is explicit (`r3MildLifespan nu ‖u₀‖ = (δ/(1+(π√ν)⁻¹+δ))²`, positive and
  `≤ 1`) and the continuation criterion is available in blow-up–dichotomy form over the
  certified-horizon set; the canonical glued maximal trajectory and its pointwise
  `limsup ‖u* t‖ = ∞` restatement are **not** yet constructed — do not cite the dichotomy
  as a trajectory-level statement, and do not present any of this as global regularity;
- do not spend hosted Actions as an interactive compiler while quota is scarce/exhausted.

## Minimal continuation prompt

`ns-mns2-flowmap-bridge を resume protocol どおり確認して、最新 main/Lean verification と HANDOFF.md を照合して続きから。形式側: 縦連鎖は continuation blow-up dichotomy まで閉鎖済み(残りは Clay semantic promotion 5 edges、Bucket A = docs/formal/R3_NS_VERTICAL_INTEGRATION_STATUS.md)。研究側: **FREEZE REVIEW 実行済み**(2026-08-21、ユーザーの fork-(β) 裁定適用; master record = docs/gates/FREEZE_REVIEW_2026-08-21.md(31行裁定テーブル)+ TYPE2_KILL_TABLE_2026-08-19.md への authorized annotation A1–A20; 3-lens Opus 監査で全 BLOCKER/ERROR 修正済み)。凍結後 frontier: **fork (β) — 辞書は neck の poloidal level bound / sup(ω_θ/r) / ℓ_neck を割り当てない(review で何も発明しない)**。M2 RESTRICTED · M3 RESTRICTED(γ₂<γ は K4′ [(E⁺)+(P)] で死亡; tie face は B2 へ併合)· **Scope-A 準静的 = B2 のみ**、kill は R-B2′ [C](full chain: re-centred zoom + Γ-max + (N-Γ) + axial boost + ledger ⟹ |w|≤C/r ⟹ KNSS 5.3 ⟹ w≡0 ⟹ v=b·e_z ⟹ Γ≡0 矛盾)、条件 **(E⁺⁺) = (COH-Δ)+(ANCH)** + (P) + (N-Γ)[C-dict]。**(NECK) = standing dictionary-extension request**(未割当入力2つ: θ_coh(ρ)、ℓ_neck; δ_T は削除済み)。K4 復活 [V](zoom-route-only rider; corridor は直接カバーしない)、K4″≡R-B1 は冗長確認へ降格、K4‴ 採用、S_blob は α>2γ−1 strict、§10 trigger は Scope-B limb のみ A_NS 内文言に修正(DVEP は fire しない)、in-house 3 vehicle(budget/winding・level route・T4-with-sign)は全て退役/ブロック。BH **YELLOW-RED 維持**、CAP trigger なし。**次はユーザー選択(デフォルト無し)**: (1) Scope-B reconnaissance(記録済み次点; trigger 文言修正済みで安価; p=p(ψ)-localizability 外の文献調査、定理試行なし)、(2) Lean 形式側へ復帰(Clay semantic promotion 5 edges / glued maximal trajectory u*)、(3) 意図的後回しリスト(intra-core β_v 枝、K8/K10 multi-region、Jiu–Xin 本文、separatrix 補題、ζ-averaging/K12″)。数値・新 ansatz(negation witness を除く)・V1/K12 promotion・CAP・in-house Liouville は行わない。GitHub Actions は一切使わない(quota 枯渇)。docs は照合後 main に直接 push。古い会話より実コードを優先して。`
