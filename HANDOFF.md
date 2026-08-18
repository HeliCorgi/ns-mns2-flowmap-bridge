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
  pass (8752 jobs), pinned source scan clean, axiom audit standard.
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

The next smallest mathematical tasks, in order (per the endorsed 3-gate plan):

1. **unrestricted uniqueness** on a common horizon (remove the ball restriction):
   Gronwall-type or stepwise-smallness patching; the enabling lemma is a **mild restart
   identity** (a mild solution restarted at time `s` is a mild solution of the shifted
   equation with datum `u s`), which is shared with task 2 — build it first;
2. **maximal continuation**: unique maximal mild solution on `[0, T*)` with
   `T* < ∞ ⇒ ‖u t‖_{H³} → ∞` (restart argument seeded by the explicit lifespan
   `r3MildLifespan`, which is bounded below on bounded-norm data), stated against
   `FlowMapNonextendibilityCriterion` / `UniformRestartContinuation` where they fit;
3. on continuation close, the **BH branch reopens** (standing decision; quantitative
   no-swirl rigidity + K12, see `docs/gates/BH_PROFILE_TASTE_REPORT.md`).

The closed layers are local statements on the Bessel-coordinate carrier (complex, and real
via the conjugation gate). No pressure reconstruction, no unconditional uniqueness, no
continuation criterion, and no Clay statement is available yet.

## Latest Lean verification

```text
runner: local Windows (Git Bash) process via Elan
revision: working tree of the quantitative-lifespan commit on main
  (new: Formal/R3QuantitativeLifespan.lean; refactored: Formal/EndpointSafeTwoSpacePicard.lean
   — exists_isMildSolutionOn_of_kernelPrimitive_lt extracted, old theorem statement unchanged;
   extended: Formal/AxiomAudit.lean)
toolchain: leanprover/lean4:v4.32.1
dependency manifest: committed lake-manifest.json; mathlib per lake-manifest.json
target scope: lake build Formal.R3QuantitativeLifespan — pass
full scope: lake build (Formal.+ default target) — pass (8752 jobs)
source scan: pinned sorry/admit/axiom/opaque scan over changed files — clean
axiom scope: Formal.AxiomAudit — pass; all ten new audited declarations
  (exists_isMildSolutionOn_of_kernelPrimitive_lt, r3MildSmallnessThreshold_pos/_le_one,
   r3MildLifespan_pos/_le_one, r3EndpointSafeProjected_kernelPrimitive_eq,
   endpointSafe_lifespan_sq_add_lt, r3EndpointSafeProjected_kernelPrimitive_mildLifespan_lt,
   r3EndpointSafeProjected_exists_mildSolutionOn_mildLifespan,
   r3EndpointSafeProjected_exists_realMildSolutionOn_mildLifespan)
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
  conjugation-equivariant and realness-preserving; and the local mild solution is proved
  physically real for physically real data on its certified horizon and ball. Still
  missing: unconditional uniqueness, any continuation / maximal-interval theorem, pressure
  reconstruction, and any Clay statement;
- its uniqueness clause holds only among trajectories in the certified `‖u₀‖ + 1` ball on the
  produced horizon; do not cite it as unconditional uniqueness;
- the horizon is now explicit (`r3MildLifespan nu ‖u₀‖ = (δ/(1+(π√ν)⁻¹+δ))²`, positive and
  `≤ 1`), but no continuation/maximal-interval theorem is available yet; do not present the
  explicit lifespan as a global or maximal statement;
- do not spend hosted Actions as an interactive compiler while quota is scarce/exhausted.

## Minimal continuation prompt

`ns-mns2-flowmap-bridge を resume protocol どおり確認して、最新 main/Lean verification と HANDOFF.md を照合して続きから。Duhamel contract、Picard fixed-point layer、reality gate 一式(conjugation/reflection、Plancherel bridge、全 operator の共役同変性)、real local mild solution(R3RealLocalMildSolution)、そして explicit quantitative lifespan(R3QuantitativeLifespan: K(T)=T+√T/(π√ν) の閉形式、T₀=(δ/(1+(π√ν)⁻¹+δ))²、複素+実データの定量的存在定理;抽象側は exists_isMildSolutionOn_of_kernelPrimitive_lt に分離済み)まで main に完了済み。次は 3 連ゲートの残り 2 つ: (1) mild restart identity(時刻 s で再スタートした mild 解が shifted mild 方程式を満たす補題 — uniqueness と continuation の共有基盤なので最初に作る)、(2) unrestricted uniqueness(ball 制限の除去; Gronwall 型または stepwise smallness patching)、(3) maximal continuation(一意極大解、T*<∞ ⇒ ‖u t‖→∞; r3MildLifespan が norm 有界データで下に有界なことを restart に使う; FlowMapNonextendibilityCriterion / UniformRestartContinuation に接続)。continuation クローズ後は BH branch(定量的 no-swirl 剛性、docs/gates/BH_PROFILE_TASTE_REPORT.md)を再開する standing decision あり。Lean はローカルで反復し、GitHub Actions は一切使わない(quota 枯渇)。green 後は成果物を main に fast-forward 統合して。古い会話より実コードを優先して。`
