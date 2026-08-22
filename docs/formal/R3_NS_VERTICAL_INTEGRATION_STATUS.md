# R³ Navier–Stokes vertical integration status

Date: 2026-08-19 (JST). One bounded audit pass over the theorem dependency chain on `main`
(baseline commits: explicit lifespan `6d5e541` → restart/uniqueness `e8b7144` →
continuation/blow-up dichotomy `77f3832`; full local `Formal.+` gate 8756 jobs green;
`Formal/AxiomAudit.lean` standard axioms only: `propext`, `Classical.choice`, `Quot.sound`).

Purpose: the repository must tell the truth about which edges of the chain from the concrete
`R³` operators to the local mild theory are **proved theorems**, which are documentation
artifacts, and which are genuinely open. Progress is measured by remaining disconnected
edges to the final Navier–Stokes statement, not by auxiliary theorem count.

Classification legend (each edge gets exactly one):

- `THEOREM-CLOSED` — proved on `main`, audited, standard axioms.
- `SEMANTICALLY-CLOSED-BUT-DOC-STALE` — proved, but public docs said otherwise (fixed this pass).
- `OPTIONAL-PRESENTATION-EDGE` — provable restatement/packaging; not a mathematical gap.
- `OPEN-REQUIRED-FOR-CLAY` — a genuine remaining implication needed before any Clay-level claim.
- `OPEN-RESEARCH-BRANCH` — open mathematics; the research program itself.
- `DEAD / RETIRED` — intentionally abandoned.

## 1. The closed vertical chain

Every edge below is `THEOREM-CLOSED` on `main` (declaration names are the audit anchors;
all appear in `Formal/AxiomAudit.lean`).

```text
R³ Fourier / Bessel-coordinate carrier
  R3, R3C, R3L2Velocity, R3HsVelocity s   (phantom-order abbrev; Bessel coordinate J^s u)
        ↓
Stokes evolution + positive-time smoothing
  r3StokesL2Operator; r3StokesH3Evolution (+ norm_r3StokesH3Evolution_apply_le, contractive);
  r3StokesH2ToH3Operator (ν>0, τ>0) + majorant r3StokesH2H3TimeKernel
  (+ intervalIntegrable_r3StokesH2H3TimeKernel)
        ↓
Leray projection at every order in play
  r3LerayL2Operator (orthogonal projection, a.e. matrix symbol P(ξ) = I − ξξᵀ/|ξ|² via
  r3LerayL2FrequencyOperator_ae); r3LerayH2Operator; r3LerayH3Operator
        ↓
Projected convection
  r3ProjectedConvectionH3ToH2 : H³ →L H³ →L H² (bounded bilinear;
  norm_r3ProjectedConvectionH3ToH2_apply_le; solenoidal range; Schwartz-core identification
  r3ProjectedConvectionH3ToH2_apply_schwartz; dense-core uniqueness r3ConvectionH3ToH2_unique)
        ↓
Endpoint-safe two-space Duhamel contract
  EndpointSafeTwoSpaceDuhamelContract (X = H³, Y = H²; no fictitious τ = 0 smoothing;
  integrability clause excludes the totalized-integral loophole);
  concrete instance r3EndpointSafeProjectedDuhamelContract;
  predicate IsR3EndpointSafeProjectedMildSolutionOn
        ↓
Picard local existence (ball form + quantitative form)
  exists_pos_time_isMildSolutionOn;
  exists_isMildSolutionOn_of_kernelPrimitive_lt (existence on ANY horizon with K(T) < δ(‖u₀‖))
        ↓
Concrete local existence
  r3EndpointSafeProjected_exists_localMildSolution (0 < T ≤ 1, ball bound, ball uniqueness)
        ↓
Reality gate (full operator equivariance) + real local solution
  r3L2Conj / r3L2Reflect / IsR3RealVelocity; Plancherel bridge fourier_r3L2Conj;
  isR3RealVelocity_iff_fourier_conjugateSymmetric;
  r3L2Conj_r3StokesH3Evolution / _r3StokesH2ToH3Operator / _r3LerayL2Operator /
  _r3ProjectedConvectionH3ToH2;
  r3EndpointSafeProjected_exists_realLocalMildSolution
        ↓
Explicit quantitative lifespan
  r3EndpointSafeProjected_kernelPrimitive_eq  (K(T) = T + √T/(π√ν), closed form);
  r3MildSmallnessThreshold, r3MildLifespan T₀ = (δ/(1+(π√ν)⁻¹+δ))², 0 < T₀ ≤ 1;
  r3EndpointSafeProjected_exists_mildSolutionOn_mildLifespan (+ _realMildSolutionOn_)
        ↓
Mild restart identity
  IsMildSolutionOn.restart; IsR3EndpointSafeProjectedMildSolutionOn.restart
        ↓
Unrestricted uniqueness (+ unconditional realness)
  IsMildSolutionOn.unique; r3EndpointSafeProjectedMildSolution_unique (no ball restriction);
  IsR3EndpointSafeProjectedMildSolutionOn.isR3RealVelocity (every mild solution with real
  datum is pointwise real)
        ↓
Concatenation
  IsMildSolutionOn.concat; IsR3EndpointSafeProjectedMildSolutionOn.concat
        ↓
Continuation / blow-up dichotomy
  r3MildLifespan_antitone; r3EndpointSafeProjected_exists_extension_of_bounded;
  r3MildHorizons (+ _nonempty);
  r3EndpointSafeProjected_horizons_unbounded_of_uniform_bound;
  r3EndpointSafeProjected_blowup_dichotomy
  (either arbitrarily long certified horizons exist, or certified solution norms escape
  every ball)
```

Doc-status note: until this pass, `README.md` still described the complex Leray symbol /
a.e. matrix realization / projected convection as the working frontier. Those edges are
`SEMANTICALLY-CLOSED-BUT-DOC-STALE` → README synchronized in this commit. No mathematical
gap was found in the chain above during this audit; declarations were read, not inferred
from file names.

## 2. Remaining edges

### Bucket A — required before any Clay-level promotion (`OPEN-REQUIRED-FOR-CLAY`)

These are the **5 semantic promotion edges** between the closed chain and the official
Clay/Fefferman statement shape (cross-checked against
`docs/formal/LEAN_MILLENNIUM_ALIGNMENT.md`; the official statement controls):

1. **Coordinate incompressibility semantics** — the Fourier/`L²` solenoidal condition
   (`r3L2SolenoidalSubmodule` membership) implies the physical-coordinate divergence-free
   condition of the endpoint statement, under sufficient regularity.
   **SPLIT (2026-08-21):**
   - **1a (distributional half): `THEOREM-CLOSED`** — `Formal/R3CoordinateIncompressibility.lean`:
     `r3TemperedDivergence` (the physical-coordinate divergence of an `R3C`-valued tempered
     distribution, `∑ᵢ ∂_{eᵢ}` of the components via mathlib's distributional derivative) and
     `r3TemperedDivergence_eq_zero_of_mem_solenoidal` (solenoidal-submodule membership ⟹ the
     `L²`-embedded physical distribution `r3L2ToTemperedCLM u` is divergence-free), audited,
     standard axioms, **hypothesis-free** (no regularity consumed, no phantom Sobolev order
     used as a physical inclusion; proof route: Plancherel
     `Lp.fourier_toTemperedDistribution_eq` + Schwartz derivative↔multiplier exchange + the
     a.e. vanishing of the raw frequency divergence).
   - **1b (classical pointwise half): `THEOREM-CLOSED` in explicit-hypothesis form
     (2026-08-21)** — `Formal/R3ClassicalIncompressibility.lean`: the physical
     representative is exhibited explicitly as the inverse Fourier integral
     `r3PhysicalRepresentative g = 𝓕⁻ g`; under the explicit frequency-side `L¹`
     hypotheses `Integrable g` and `Integrable (fun ξ => ‖ξ‖ * ‖g ξ‖)` it is `C¹`
     (`contDiff_one_r3PhysicalRepresentative`), differentiable at every point with the
     explicit Fourier-integral derivative (`hasFDerivAt_r3PhysicalRepresentative` /
     `r3RepresentativeDeriv` — the `fderiv` in the divergence is genuine, not
     junk-valued), and its classical divergence
     `r3ClassicalDivergence U x = ∑ i, (fderiv ℝ U x (eᵢ)) i` vanishes at every point
     (`r3ClassicalDivergence_r3PhysicalRepresentative`; membership form
     `r3PhysicalRepresentative_incompressible_of_mem_solenoidal`). Hypotheses witnessed
     non-vacuous by Schwartz profiles
     (`r3PhysicalRepresentative_hypotheses_nonvacuous`). Audited, standard axioms; no
     phantom Sobolev order used as a physical inclusion.
   - **Residues, recorded under edge 3 (initial-data class semantics):**
     (i) the **decoder-to-hypothesis bridge** — deriving the two `L¹` frequency
     hypotheses (and the a.e.-representative hypothesis
     `g =ᵐ coeFn (𝓕 u)`) from the Bessel `H³` carrier through the decoder —
     **CLOSED 2026-08-21 as edge 3a, see below**;
     (ii) = **edge 3b**: the **a.e. identification** of the explicit pointwise
     inverse-Fourier *integral* with the `L²` decode — **CLOSED 2026-08-22, see
     below** (the general `L¹ ∩ L²` layer is still absent from mathlib; the closure
     is the instance needed here, via Schwartz pairing, not a general library).
   - **Edge 3b: `THEOREM-CLOSED` (2026-08-22)** —
     `Formal/R3InversionConsistency.lean`:
     `r3PhysicalRepresentative_ae_r3Decoded3PhysicalVelocity` proves
     `r3PhysicalRepresentative (r3DecodedFrequency 3 f) =ᵐ[volume]
     coeFn (r3Decoded3PhysicalVelocity f)` for **every** `L²` Bessel coordinate
     `f` (no solenoidality needed), at order `3`. Scope: the `L¹ ∩ L²`
     inversion-consistency **instance needed here** — no general inversion
     library is built. Route: both sides are paired against smooth compactly
     supported test functions (`L¹` multiplication formula
     `VectorFourier.integral_fourierIntegral_smul_eq_flip` on the pointwise
     side; `Lp.toTemperedDistribution_apply` +
     `Lp.fourierInv_toTemperedDistribution_eq` +
     `TemperedDistribution.fourierInv_apply` on the `L²` side) and the a.e.
     equality follows from `ae_eq_of_integral_contDiff_smul_eq`. Bundled
     consequence `r3DecodedFrequency_incompressible_ae_decoder`: for a
     solenoidal coordinate, the `C¹`, everywhere classically divergence-free
     explicit representative is an a.e. representative of the `L²` decode,
     whose tempered embedding is exactly the carrier's Bessel decoder.
   - **Edge 3a: `THEOREM-CLOSED` (2026-08-21)** —
     `Formal/R3DecoderFrequencyBridge.lean`: the decoded frequency data
     `r3DecodedFrequency 3 f = (1+‖ξ‖²)^(-3/2) • 𝓕 f` of **any** `L²` Bessel
     coordinate satisfies both edge-1b hypotheses
     (`integrable_r3DecodedFrequency`, `integrable_weighted_r3DecodedFrequency`;
     Cauchy–Schwarz + Japanese bracket, `finrank 3 < 6` and `3 < 4` — order `3` is
     the honest threshold, not slack). The word "decoder" is earned by theorem:
     the weight equals the carrier's decoder symbol
     (`r3InverseBesselWeight_eq_sobolevWeight`) and the `L²`-level decode
     `r3Decoded3PhysicalVelocity` agrees with the repository's
     tempered-distribution decoder `r3HsToTemperedCLM 3`
     (`r3L2ToTempered_r3Decoded3PhysicalVelocity`, reusing
     `R3StokesH2H3Smoothing`'s `r3H3ToL2Operator`). Coordinate solenoidality
     transfers to the decode (`r3Decoded3PhysicalVelocity_mem_solenoidal`);
     capstone `r3DecodedFrequency_incompressible` (+ Leray non-vacuity witness)
     delivers edge 1b with every hypothesis discharged from the decoder. No rapid
     decay claimed; the phantom equality never used as an embedding. Edge 3
     proper (the `SmoothRapidDecayInitial`-shaped class semantics) remains
     open; edge 3b is closed separately (2026-08-22, above).
2. **Momentum-equation semantics with a pressure witness** — the projected mild equation
   implies the coordinate momentum equation with an explicit pressure (pressure
   reconstruction).
   **SPLIT (2026-08-22):**
   - **2a (generic Helmholtz pressure reconstruction): `THEOREM-CLOSED`** —
     `Formal/R3HelmholtzPressure.lean`: for **every** `L²` source `F`, the explicit
     pressure tempered distribution `r3HelmholtzPressure F` (inverse Fourier transform
     of the `(-(2πi))⁻¹·(ξ·𝓕F)/‖ξ‖²` profile, split `L¹`-on-ball ⊕ `L²`-exterior)
     satisfies `∇p = -(I-P)F` componentwise in `𝓢'`
     (`r3HelmholtzPressure_gradient`), hypothesis-free, with the Leray complement's
     a.e. frequency realization (`fourier_r3LerayComplementL2_ae`), the supporting
     integrability facts, and a non-vacuity witness
     (`exists_r3LerayComplementL2_ne_zero`: the complement is not identically zero).
     Audited, standard axioms; no phantom Sobolev order; sign matches the NS
     convention (`∇p = -(I-P)((u·∇)u)` shape).
   - **2b-i (general `H³` convection source identification): `THEOREM-CLOSED`
     (2026-08-22)** — `Formal/R3ConvectionSourceIdentification.lean`: for **every** pair
     of order-three Bessel coordinates `u, v`, hypothesis-free, the genuine `J⁻²`
     multiplier decode of the completed coordinate operator equals the literal pointwise
     convection of the decoded physical representatives,
     `r3H2ToL2Operator (r3ConvectionH3ToH2 u v) = r3DecodedConvectionL2 u v`
     (`r3H2ToL2Operator_r3ConvectionH3ToH2`), where
     `r3DecodedConvectionL2 u v = ∑ᵢ (U_u)ᵢ ∂ᵢU_v` is built pointwise from edge-1b's
     explicit derivative of `U_f = 𝓕⁻(r3DecodedFrequency 3 f)` and equals the genuine
     `fderiv` (`r3DecodedConvectionPointwise_eq_fderiv`).  Route: exact Fourier inversion
     on the Schwartz core + continuity in each slot (bounded `2πiξᵢJ⁻³` multiplier
     operators in the derivative slot; quantitative Cauchy–Schwarz decoder `L¹` bound
     `∫‖J⁻³·𝓕f‖ ≤ ‖J⁻³‖_{L²}‖f‖` for the Lipschitz estimate in the velocity slot).
     Projected corollary `r3H2ToL2Operator_r3ProjectedConvectionH3ToH2 =
     r3LerayL2Operator ((U·∇)V)`, the Leray-complement difference identity, and the
     edge-2a pressure gradient instantiated at that source
     (`r3HelmholtzPressure_gradient_decodedConvection`).  **Scope: this fixes the
     semantics of the convection *operator* from which the Duhamel integrand is built;
     it says nothing about the mild solution's time dependence, and it is not an
     identification of the Duhamel integrand along a solution.  No non-vacuity witness
     is shipped for this edge (unlike 2a): nothing yet proves
     `r3DecodedConvectionL2 u v ≠ 0` for any `u, v`.**  No phantom Sobolev order
     consumed; no rapid decay claimed.
   - **2b-ii (momentum-equation semantics proper): still `OPEN-REQUIRED-FOR-CLAY`** —
     time dependence, differentiation of the Duhamel formula, and the mild→strong
     coordinate momentum equation assembling `∂ₜu − νΔu + (u·∇)u + ∇p = 0` with the
     edge-2a pressure witness at the edge-2b-i-identified source (with `v := u` and the
     edge-3a solenoidality). Not attempted.
3. **Initial-data class semantics** — the Bessel-coordinate `H³` carrier is a phantom-order
   `L²` abbrev; a Clay-grade statement needs the decoder-level implication from the
   coordinate class to actual smoothness/decay (`SmoothRapidDecayInitial`-shaped), and the
   converse embedding for the intended data. The general decoder equality for arbitrary
   `H³` inputs against a separately defined distributional product is also still open
   (`FORMAL_SCOPE.md` §7).
4. **Energy semantics** — the carrier norms/estimates imply the finite-energy predicate of
   the endpoint statement.
5. **Breakdown-statement transfer** — a verified breakdown theorem on the concrete solution
   class implies the official whole-space breakdown proposition, including the quantifier
   structure over viscosity (the official statement quantifies over `ν`; a single-`ν`
   candidate needs a rigorous viscosity-scaling bridge) and the `f = 0` specialization.

These must be **semantic promotion theorems**, not definitional adapters
(`LEAN_MILLENNIUM_ALIGNMENT.md` rule).

### Bucket B — useful presentation/integration, not current bottleneck (`OPTIONAL-PRESENTATION-EDGE`)

1. One canonical theorem chaining the whole local theory (existence + realness + explicit
   horizon + uniqueness + extension in a single statement).
2. The canonical glued maximal trajectory `u* : [0, T*) → H³` (choice + unrestricted
   uniqueness make the certified family coherent) and the pointwise restatement
   `T* < ∞ ⇒ limsup_{t→T*} ‖u* t‖ = ∞` of the proved horizon dichotomy. Becomes Bucket A
   only if the final chosen breakdown statement is phrased through a maximal solution.
3. Adapter to the legacy abstract `MildEvolutionKernel` / `LerayProjectedQuadraticContract`
   flow-map interfaces (`FlowMapNonextendibilityCriterion`, `UniformRestartContinuation`).
   Nothing downstream currently consumes it.
4. README dependency graph upkeep.

None of these may preempt the research bottleneck.

### Bucket C — research bottleneck (`OPEN-RESEARCH-BRANCH`)

**BH / small-swirl localized steady-Euler degeneration** (Type-II window, interior
quasi-static branch): quantitative no-swirl rigidity rate and the K12 decision. See
`docs/gates/BH_PROFILE_TASTE_REPORT.md` (YELLOW baseline) and this turn's
`docs/gates/BH_QUANTITATIVE_RIGIDITY_K12_AUDIT.md`.

### Retired within this lane (`DEAD / RETIRED`)

- Hosted GitHub Actions as a verification path (quota; local Elan-pinned gate is the
  evidence contract).
- K4 as a load-bearing kill (superseded by K3); [D1] (withdrawn, replaced by conditional
  [D1′]); fixed-profile BH rescaling (double no-go, taste report §4).

## 3. Verdict

**`CHAIN CLOSED TO CONTINUATION`** — additionally, the audit found the public docs stale
rather than the mathematics open (`DOCUMENTATION WAS STALE, MATHEMATICS CLOSED` applies to
the README frontier; fixed in this commit).

Exact missing-edge count to the official Clay statement class: **5 required semantic
edges** (Bucket A above), plus the open research branch (Bucket C). Bucket B contains no
mathematical gaps.

Update 2026-08-21: edge 1 is split; its distributional half (1a) is `THEOREM-CLOSED`
(`Formal/R3CoordinateIncompressibility.lean`, full gate 8757 jobs, standard axioms). The
required-edge count stays 5, with edge 1 narrowed to its classical-pointwise half (1b).

Update 2026-08-21 (second pass): **edge 1 is now fully closed in explicit-hypothesis
form** — 1b `THEOREM-CLOSED` (`Formal/R3ClassicalIncompressibility.lean`, full gate 8758
jobs, standard axioms). The remaining required edges are **2, 3, 4, 5**, with edge 3
enlarged by two named residues from 1b: the decoder-to-hypothesis bridge and the
`L¹ ∩ L²` a.e. identification of the explicit representative with the `L²` element.

Update 2026-08-21 (third pass): **edge 3a (the decoder-to-hypothesis bridge) is
`THEOREM-CLOSED`** (`Formal/R3DecoderFrequencyBridge.lean`, full gate 8759 jobs, all
seven audited declarations standard axioms, incl. the tempered-decoder identification
`r3L2ToTempered_r3Decoded3PhysicalVelocity`). The remaining required edges are **2,
3 (proper: `SmoothRapidDecayInitial`-shaped class semantics + edge 3b), 4, 5**.

Update 2026-08-22: **edge 3b is `THEOREM-CLOSED`**
(`Formal/R3InversionConsistency.lean`, full gate 8760 jobs, all four audited
declarations standard axioms). The remaining required edges are **2, 3 (proper:
`SmoothRapidDecayInitial`-shaped class semantics), 4, 5**.

Update 2026-08-22 (second pass): **edge 2a (generic Helmholtz pressure reconstruction)
is `THEOREM-CLOSED`** (`Formal/R3HelmholtzPressure.lean`, full gate 8761 jobs, all five
audited declarations standard axioms, incl. the non-vacuity witness). The remaining
required edges are **2b (momentum-equation semantics proper), 3 (proper), 4, 5**.

Update 2026-08-22 (third pass): **edge 2b-i (general `H³` convection source
identification) is `THEOREM-CLOSED`** (`Formal/R3ConvectionSourceIdentification.lean`,
full gate 8762 jobs, all seven audited declarations standard axioms; **no non-vacuity
witness shipped for this edge** — to be added). The required-edge count stays 4, with
edge 2b narrowed to 2b-ii. The remaining required edges are **2b-ii, 3 (proper:
`SmoothRapidDecayInitial`-shaped class semantics), 4, 5**.
