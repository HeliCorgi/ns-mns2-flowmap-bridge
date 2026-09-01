# Formal scope and theorem boundary

Last synchronized: 2026-09-02 (JST, third session), after the user-commissioned
**T-SEL bridge discharge step** (records
`docs/formal/TSEL_BRIDGE_FORMALIZATION_2026-09-02.md` and
`docs/formal/TSEL_BRIDGE_DISCHARGE_2026-09-02.md`): **SEL-1 and SEL-4 are now proved
theorems** (`r3TSel_classicalSobolevComparability`, `r3TSel_katoPonceCommutator`; new
files `Formal/R3TSelClassicalComparability.lean`, `Formal/R3TSelSchwartzCalculus.lean`,
`Formal/R3TSelLeibnizCommutator.lean`), on top of the session-2 statement layer
(`Formal/GronwallIntegralInequality.lean`, `Formal/R3TSelDecodedGradient.lean`,
`Formal/R3TSelBridge.lean`). Local full `Formal.+` gate pass (8775 jobs), axiom audit
standard (`propext`, `Classical.choice`, `Quot.sound`), pinned source scan clean. The
2026-08-23 stop rule on *uncommissioned* formal plumbing is unchanged; the T-SEL work
is an explicit user commission and its head `N0` is untouched by commission.

This file records what the Lean layer has actually established and what remains outside the proof boundary.

`PROJECT_GOAL.md` is the repository-level acceptance specification. `SPEC.md` is the subordinate normative contract for the current primary physical track (`R^3`, `f = 0`, axisymmetric with swirl, breakdown side). If this file conflicts with either higher-level specification, the higher-level specification controls.

No theorem described here is a Clay A/B/C/D result.

## 1. Exact flow-map bridge

For real normed spaces with complete target, an open admissible set `U`, a map `S`, and affine path

`γ(s) = x + s d`, `s ∈ [0,1]`,

if `S` is `C¹` on `U` and the full path remains in `U`, Lean proves

`∫₀¹ (DS(x + s d))[d] ds = S(x + d) - S(x)`.

The radial specialization is

`∫₀¹ (DS(s d))[d] ds = S(d) - S(0)`.

The tangent is the fixed, unnormalized direction `d`.

Key files:

- `Formal/Bridge.lean`
- `Formal/FlowMapFTC.lean`
- `Formal/FlowMapChainRule.lean`
- `Formal/FlowMapOperatorContinuity.lean`
- `Formal/FlowMapContDiffOne.lean`
- `Formal/FlowMapLocalContDiff.lean`
- `Formal/PDEBridgeAdapter.lean`
- `Formal/NavierStokesTimeBridge.lean`

`PDEBridgeAdapter` and `NavierStokesTimeBridge` package the analytic bridge with externally supplied PDE semantic relations. They do not themselves construct Navier--Stokes evolution.

## 2. Mild-solution and tangent semantics

`Formal/MildSolutionSemantics.lean` defines a Banach-space mild kernel with time-indexed continuous linear evolution `H(t)` and nonlinearity `B`.

A trajectory satisfies the Duhamel equation

`u(t) = H(t)u₀ - ∫₀ᵗ H(t-s) B(u(s)) ds`

with explicit continuity, initial-value, and interval-integrability requirements.

For a continuous bilinear map

`Q : V →L[ℝ] V →L[ℝ] V`,

`Formal/QuadraticMildNonlinearity.lean` defines `B(u) = Q(u,u)` and proves

`DB(u)[v] = Q(u,v) + Q(v,u)`.

The later quadratic stack differentiates parameterized Duhamel terms under explicit domination hypotheses and derives the representative tangent equation

`J(t)h = H(t)h - ∫₀ᵗ H(t-s) (Q(u(s), J(s)h) + Q(J(s)h, u(s))) ds`.

Relevant files include:

- `Formal/MildFlowMapBridge.lean`
- `Formal/MildZeroUniqueness.lean`
- `Formal/QuadraticLinearizedMild.lean`
- `Formal/QuadraticMildTangentAdapter.lean`
- `Formal/QuadraticDuhamelDifferentiation.lean`
- `Formal/QuadraticMildFixedPointDerivative.lean`
- `Formal/QuadraticMildTangentRealization.lean`
- `Formal/QuadraticMildCoherentFamilyAdapter.lean`

These remain abstract Banach-space results until instantiated by a concrete Navier--Stokes PDE layer.

## 3. Leray-projected quadratic operator contract

`Formal/LerayProjectedQuadratic.lean` defines `LerayProjectedQuadraticContract` with a certified solenoidal submodule, a continuous linear Leray map, a raw continuous bilinear convection map, and the corresponding projected bilinear map.

Lean derives Leray idempotence, solenoidal range properties, solenoidality of the quadratic diagonal and derivative, and compatibility with the packaged mild nonlinearity.

This is still an abstract operator contract; it is distinct from the later concrete `R^3` function-space constructions.

## 4. Concrete `R^3` frequency and `L²` operator layer

The repository now goes substantially beyond the old frequency-fiber-only boundary.

### Frequency symbols

`Formal/R3LerayFrequencySymbol.lean` defines the pointwise real Leray projection on the transverse frequency fiber and proves the expected projection, transversality, explicit formula, and norm bounds.

`Formal/R3StokesFrequencySymbol.lean` defines the scalar Stokes factor

`exp(-(2π)^2 ν t |ξ|^2)`

under the pinned mathlib Fourier convention and proves forward-time contraction and semigroup facts at frequency level.

### Bundled `L²(R³; ℂ³)` Stokes operator

`Formal/R3StokesL2Operator.lean` defines

`R3L2Velocity := Lp (α := R3) R3C 2 (volume : Measure R3)`

and constructs:

- a bundled `L∞` scalar Stokes multiplier;
- the corresponding continuous linear map on Fourier-side `L²`;
- the physical-space Stokes operator by Fourier conjugation;
- exact Fourier realization;
- identity at time zero.

This is a genuine bounded function-space Stokes operator. It is not by itself a full Navier--Stokes semigroup/mild-theory instantiation.

### Bundled `L²` Leray operator

The solenoidal carrier stack culminates in `Formal/R3LerayL2Operator.lean`, which defines the physical-space `L²(R³; ℂ³)` Leray projector as orthogonal projection onto the closed solenoidal submodule.

Lean proves:

- every projected output is solenoidal;
- already-solenoidal fields are fixed;
- idempotence;
- exact range identification;
- pointwise operator norm non-expansion;
- operator norm at most one.

The later Fourier bridge files identify the relevant frequency-space realization. This removes the old blocker that the project had only a frequency-fiber Leray symbol.

Relevant files include:

- `Formal/R3SobolevCarrier.lean`
- `Formal/R3SolenoidalSobolevCarrier.lean`
- `Formal/R3ClosedSolenoidalCarrier.lean`
- `Formal/R3SolenoidalCarrierCompleteness.lean`
- `Formal/R3LerayL2Operator.lean`
- `Formal/R3LerayFourierBridge.lean`
- `Formal/R3LerayPointwiseL2.lean`
- `Formal/R3LerayPointwiseProjectionIdentification.lean`
- `Formal/R3StokesL2Operator.lean`
- `Formal/R3StokesSolenoidalPreservation.lean`
- `Formal/R3StokesSolenoidalOperator.lean`

## 5. Current Schwartz convection/Sobolev track

The Schwartz-core estimates

- `R3SchwartzConvectionTermSobolevEstimate 3`, and
- `R3SchwartzConvectionSobolevEstimate 3`

are now proved in `Formal/R3SchwartzConvectionSobolevEstimate.lean`, using a
finite uniform majorant for the three coordinate-derivative constants.

That estimate has now been promoted, by density, to a bounded complex-bilinear
`H³ × H³ → H²` map on the complete Bessel-coordinate carriers.  The result is
an extension of the exact Schwartz formula, with an explicit norm bound and a
uniqueness theorem.  It is not a construction of a separate topological
completion of Schwartz space: `R3HsVelocity s` is the existing complete `L²`
Bessel-coordinate model whose physical meaning is supplied by its
order-dependent decoder.

### Exact Fourier product/convolution bridge

`Formal/R3SchwartzProductConvolution.lean` proves the exact Fourier convolution formula for a Schwartz convection summand. In particular, the transformed term is represented as an ordinary convolution integral of one coordinate field with one coordinate derivative field.

### H² Bessel-weight geometry and pointwise majorant

The following files build the weighted frequency estimate:

- `Formal/R3H2BesselWeightGeometry.lean`
- `Formal/R3H2WeightedConvolutionKernel.lean`
- `Formal/R3H2AdditiveConvolutionWeight.lean`
- `Formal/R3H2YoungWeightedBridge.lean`
- `Formal/R3SchwartzConvectionH2FrequencyMajorant.lean`

They yield a pointwise H²-frequency bound for one convection summand by two scalar integral majorants.

### Named ordinary scalar majorants

`Formal/R3SchwartzConvectionScalarMajorants.lean` defines

- `r3H2LeftScalarMajorant`;
- `r3H2RightScalarMajorant`.

Lean proves their integrands are integrable, both majorants are nonnegative, and each is exactly an ordinary real scalar convolution of the relevant pointwise norm fields. It also rewrites the one-coordinate H² pointwise bound using these two names.

### Real Young `L¹/L²` Bochner bridge

`Formal/R3YoungRealL1L2Bochner.lean` defines a real-valued `L²(R³)` carrier and an `L²`-valued Bochner convolution based on translation. It proves:

- continuity and isometry of translation;
- Bochner integrability for a continuous real `L¹` factor;
- `L¹ * L² → L²` Young bound;
- an argument-order wrapper for the `L² * L¹ → L²` use case with the corresponding norm estimate.

### Norm-field `L²` bundling

`Formal/R3SchwartzNormFieldL2.lean` defines canonical `L²` bundles of the pointwise norm fields of scalar- and velocity-valued Schwartz functions:

- `r3SchwartzScalarNormL2`;
- `r3SchwartzVelocityNormL2`.

It also defines the bundled Young candidates

- `r3H2LeftMajorantYoungL2`;
- `r3H2RightMajorantYoungL2`;

and proves their expected Young norm bounds.

### Representative/Fubini bridge — closed by merged PR #79

The previously explicit gap between ordinary scalar convolution and the bundled Young construction is formalized on green `main`.

Relevant merged files include:

- `Formal/R3YoungRealSetIntegralBridge.lean`;
- `Formal/R3YoungRealConvolutionCommutativity.lean`;
- `Formal/R3SchwartzMajorantYoungRepresentative.lean`;
- `Formal/R3SchwartzScalarMajorantL2.lean`;
- `Formal/R3SchwartzConvectionH2L2Majorant.lean`.

In particular, Lean proves the required a.e. representative identifications for the two concrete majorants, packages the ordinary majorants in `L²`, transfers the Young norm estimates to them, and lifts the pointwise H² frequency majorant to the bundled estimate

`norm_r3H2WeightedVelocitySchwartz_fourier_convectionTerm_toLp_le_YoungFactors`.

Therefore the old invariant warning against silently identifying

- `r3H2LeftScalarMajorant`, `r3H2RightScalarMajorant`

with

- `r3H2LeftMajorantYoungL2`, `r3H2RightMajorantYoungL2`

has been discharged for these concrete objects by explicit theorems. The general proof discipline remains: analogous identifications elsewhere still require explicit representative/Fubini results.

### H³ Fourier-coordinate and convection closure — closed by merged PR #80

Merged PR #80 adds and verifies the coordinate/Fourier bookkeeping and the per-coordinate H³→H² estimate.

`Formal/R3H2CoordinateFourierBounds.lean` proves, among other results:

- `fourier_r3SchwartzCoordinate_eq`;
- `integral_norm_fourier_r3SchwartzCoordinate_le_H3`;
- `norm_r3H2WeightedScalarSchwartz_fourier_coordinate_toLp_le_H3`.

In particular,

`𝓕 (r3SchwartzCoordinate i f) = r3SchwartzCoordinate i (𝓕 f)`

is no longer an open bookkeeping obligation.

`Formal/R3SchwartzConvectionH3Closure.lean` proves:

- `norm_r3H2WeightedVelocitySchwartz_fourier_convectionTerm_toLp_le_H3`;
- `norm_r3SchwartzToHsCLM_two_convectionTerm_le_H3`.

The physical H² estimate for one coordinate has the explicit bound

`‖r3SchwartzToHsCLM 2 (r3SchwartzConvectionTerm i u v)‖`

`≤ 4 * ‖r3H2InverseBesselWeightL2‖ * r3CoordinateDerivativeFrequencyConstant i * ‖r3SchwartzToHsCLM 3 u‖ * ‖r3SchwartzToHsCLM 3 v‖`.

The only coordinate dependence in this bound is the already formalized nonnegative derivative-frequency constant `r3CoordinateDerivativeFrequencyConstant i`.

### Uniform coordinate packaging and full convection estimate — closed

`Formal/R3SchwartzConvectionSobolevEstimate.lean` now defines the explicit finite majorant

`r3UniformCoordinateDerivativeFrequencyConstant`

as the sum of the three nonnegative coordinate constants and proves:

- `r3UniformCoordinateDerivativeFrequencyConstant_nonneg`;
- `r3CoordinateDerivativeFrequencyConstant_le_uniform`;
- `r3SchwartzConvectionH3Constant_nonneg`;
- `r3SchwartzConvectionTermSobolevEstimate_three`;
- `r3SchwartzConvectionSobolevEstimate_three`.

Thus both `R3SchwartzConvectionTermSobolevEstimate 3` and
`R3SchwartzConvectionSobolevEstimate 3` are proved on the Schwartz core. The full estimate carries
the same documented factor-three triangle-inequality loss as `.to_convection`, now through an
exported direct sum bound; no new analytic assumption is introduced by the finite packaging.

### Dense Bessel-coordinate extension — closed

`Formal/R3SchwartzSobolevDensity.lean` proves that the order-`s` Bessel
multiplier on Schwartz fields is onto, using the inverse-order multiplier, and
then combines this with mathlib's density of Schwartz fields in `L²` to prove

`r3SchwartzToHsCLM_denseRange (s : ℝ)`.

This is a dense-range statement into the complete Bessel-coordinate model. It
does not assert that the native Schwartz Fréchet topology is the topology
induced by one `H^s` norm.

`Formal/R3SobolevConvectionExtension.lean` uses the proved core estimate and
`LinearMap.extendOfNorm` in the second and then the first variable. It defines

`r3ConvectionH3ToH2 : R3HsVelocity 3 →L[ℂ] R3HsVelocity 3 →L[ℂ] R3HsVelocity 2`

and proves:

- `r3ConvectionH3ToH2_apply_schwartz`;
- `r3HsToTempered_r3ConvectionH3ToH2_schwartz`;
- `norm_r3ConvectionH3ToH2_le`;
- `norm_r3ConvectionH3ToH2_apply_le`;
- `r3ConvectionH3ToH2_unique`.

Thus the completed coordinate map agrees exactly with physical convection on
canonical Schwartz inputs and is the unique continuous complex-bilinear map
with those dense-core values.  The decoder agreement theorem is intentionally
limited to Schwartz inputs; equality with an independently defined
distributional product for every `H³` pair has not been proved.

The Sobolev-order parameter of `R3HsVelocity` is currently phantom at the Lean
type level: orders two and three share the same underlying `L²` coordinate
type, while their decoders differ.  No physical `H³ → H²` inclusion or
`H² → H³` smoothing estimate may therefore be justified by definitional
equality of these aliases.

### Order-aware H² Leray bridge and projected convection — closed

`Formal/R3H2LerayBridge.lean` defines the bounded physical `L²`
reconstruction

`r3H2ToL2Operator : R3HsVelocity 2 →L[ℂ] R3L2Velocity`

by the genuine inverse Bessel multiplier `J⁻²`. It proves:

- `r3L2ToTempered_r3H2ToL2Operator` for every stored order-two coordinate;
- exact recovery of `f.toLp 2` on canonical Schwartz coordinates;
- `r3H2ToL2Operator_commutes_leray`;
- `r3HsToTempered_r3LerayH2Operator`, identifying the decoded coordinate
  projection with the existing physical `L²` Leray projector.

Thus `r3LerayH2Operator` has order-two physical semantics fixed by proved
decoder and commutation theorems, not by the phantom alias equality.

`Formal/R3ProjectedSobolevConvection.lean` defines

`r3ProjectedConvectionH3ToH2 : R3HsVelocity 3 →L[ℂ] R3HsVelocity 3 →L[ℂ] R3HsVelocity 2`

and proves the inherited operator and pointwise norm bounds, stored-coordinate
and reconstructed physical-`L²` solenoidality, the general decoder formula,
and exact Schwartz decoder agreement with the existing literal
`r3ProjectedSchwartzConvectionL2`. The sign is `+P((u · ∇)v)`; the existing
mild equation supplies its own minus sign.

The new audited theorems depend only on the standard foundations reported by
the rest of this development (`propext`, `Classical.choice`, and `Quot.sound`).

### Positive-time H²-to-H³ Stokes smoothing — closed

`Formal/R3StokesH2H3Smoothing.lean` defines, for strictly positive viscosity `ν` and positive
elapsed time `τ`, the genuine stored-coordinate map

`r3StokesH2ToH3Operator : R3HsVelocity 2 →L[ℂ] R3HsVelocity 3`.

It is Fourier conjugation of multiplication by

`(1 + ‖ξ‖²)^(1/2) * exp(-(2π)² ν τ ‖ξ‖²)`,

rather than a retyping through the phantom Sobolev-order alias. Lean proves
`fourier_r3StokesH2ToH3Operator`, `norm_r3StokesH2ToH3Operator_apply_le`, and
`norm_r3StokesH2ToH3Operator_le`. The explicit bound is

`1 + (sqrt ((2π)² ν τ))⁻¹`,

and `intervalIntegrable_r3StokesH2H3TimeKernel` proves that this scalar majorant is
interval-integrable on `[0,T]` for every `T ≥ 0`.

The same module constructs the genuine inverse-order-three reconstruction

`r3H3ToL2Operator : R3HsVelocity 3 →L[ℂ] R3L2Velocity`

and proves `r3L2ToTempered_r3H3ToL2Operator`. The identities
`r3H3ToL2Operator_r3StokesH2ToH3Operator` and
`r3HsToTempered_r3StokesH2ToH3Operator` identify the reconstructed output exactly with the
existing physical `L²` Stokes operator applied to `r3H2ToL2Operator` of the input.

The module also defines the order-aware `r3LerayH3Operator`, proves its physical `L²` decoder
semantics, proves `r3StokesH2ToH3Operator_commutes_leray`, and proves stored-coordinate and
reconstructed physical-`L²` solenoidal preservation. These statements fix the order-three and
cross-order meanings through explicit multipliers and decoders, not through definitional equality
of the carrier aliases.

The new audited theorems depend only on the standard foundations reported by this development
(`propext`, `Classical.choice`, and `Quot.sound`).

## 6. Exact current analytic gate

The density, bounded-extension, projected-convection, positive-time smoothing, and endpoint-safe
two-space Duhamel layers are closed. PR #82 (`Formal/EndpointSafeTwoSpaceDuhamel.lean`,
`Formal/R3StokesH3Evolution.lean`, `Formal/R3EndpointSafeProjectedDuhamel.lean`) establishes:

- the bundled `EndpointSafeTwoSpaceDuhamelContract 𝕜 X Y` with same-space `linearEvolution`
  (identity at zero, honest nonnegative-time semigroup law, jointly continuous action),
  positive-elapsed-time smoothing `Y → X`, continuous bilinear source `X →L X →L Y`, and a
  locally interval-integrable nonnegative scalar smoothing majorant;
- endpoint totalization by the zero operator at `τ ≤ 0`, with no fictitious bounded `H² → H³`
  operator at `τ = 0`;
- strong measurability and Bochner interval-integrability of the **actual vector-valued**
  Duhamel integrand for every trajectory continuous on the compact forward interval, plus the
  pointwise and integral norm estimates;
- the mild predicates `IsMildAt` / `IsMildSolutionOn`, whose integrability clause excludes the
  totalized-integral loophole;
- the concrete instantiation `r3EndpointSafeProjectedDuhamelContract` on
  `X = R3HsVelocity 3`, `Y = R3HsVelocity 2` with `r3ProjectedConvectionH3ToH2`,
  `r3StokesH2ToH3Operator`, `r3StokesH3Evolution`, and `r3StokesH2H3TimeKernel`, together with
  the concrete predicate `IsR3EndpointSafeProjectedMildSolutionOn`.

The Picard fixed-point layer for exactly this contract is now also closed.
`Formal/EndpointSafeTwoSpacePicard.lean` proves, for an arbitrary contract:

- nonnegativity, monotonicity, continuity, and small-time smallness of the cumulative
  smoothing mass `kernelPrimitive`;
- the exact reversed elapsed-time representation of the endpoint-safe Duhamel integral
  (`integral_duhamelIntegrand_eq_reversed`, via `intervalIntegral.integral_comp_sub_left`);
- quantitative Duhamel bounds: size (`norm_duhamelIntegral_le`), trajectory difference
  (`norm_duhamelIntegral_sub_le`, from the bilinear splitting
  `Q u u - Q v v = Q u (u - v) + Q (u - v) v`), and final-time difference
  (`norm_duhamelIntegral_time_sub_le`);
- time-continuity of the Duhamel integral on the compact horizon
  (`continuousOn_duhamelIntegral`), by uniform continuity of the trajectory — no dominated
  convergence over the moving singular kernel is needed in the reversed variable;
- the Picard map on `C(Icc 0 T, X)` (`picardMap`, trajectories extended by `Set.IccExtend`),
  closed-ball invariance under a contractive linear evolution (`norm_picardMap_le`), and the
  contraction estimate (`dist_picardMap_le`);
- the Banach fixed point on the complete closed ball of radius `‖u₀‖ + 1`:
  `exists_pos_time_isMildSolutionOn` produces `0 < T ≤ 1` and a trajectory `u` with
  `IsMildSolutionOn T u₀ u`, staying in the ball, unique among ball-valued mild solutions.

`Formal/R3EndpointSafeProjectedLocalExistence.lean` instantiates this on the concrete carriers:
`r3EndpointSafeProjected_exists_localMildSolution` gives, for every `ν > 0` and every
order-three Bessel coordinate `u₀`, a horizon `0 < T ≤ 1` and a trajectory satisfying
`IsR3EndpointSafeProjectedMildSolutionOn hnu T u₀ u` with the `‖u₀‖ + 1` ball bound and
ball uniqueness. The required contractivity is `norm_r3StokesH3Evolution_apply_le`.

The first slice of the reality gate is also closed. `Formal/R3ConjugationReflection.lean`
supplies, on the shared `L²` Bessel-coordinate carrier (hence for every `R3HsVelocity s`):

- `r3CConj : R3C ≃ₗᵢ[ℝ] R3C`, coordinatewise fiber conjugation, with
  `r3CConj_eq_self_iff` (fixed points = componentwise-real vectors);
- `r3L2Conj : R3L2Velocity →L[ℝ] R3L2Velocity`, pointwise carrier conjugation — a
  norm-preserving continuous involution;
- `r3L2Reflect : R3L2Velocity →L[ℂ] R3L2Velocity`, composition with `x ↦ -x` — a
  norm-preserving continuous involution commuting with conjugation
  (`r3L2Reflect_r3L2Conj`);
- the predicates `IsR3RealVelocity` (`r3L2Conj g = g`, characterized a.e. by
  `isR3RealVelocity_iff_im_ae`) and `IsR3ConjugateSymmetricVelocity`
  (`r3L2Reflect (r3L2Conj g) = g`, the exact `L²` form of `û (-ξ) = conj (û ξ)`), both closed
  under addition, real scalars, negation, subtraction, and reflection, both cutting out closed
  subsets of the carrier.

The Plancherel reality bridge is closed as well. `Formal/R3FourierConjugationBridge.lean`
proves:

- the Schwartz-level involutions `r3SchwartzConjCLM` (postcomposition with `r3CConjCLM`) and
  `r3SchwartzReflectCLM` (precomposition with `x ↦ -x`);
- the pointwise Fourier–conjugation identity `r3Fourier_conj_eq`:
  `𝓕 (fun x => conj (f x)) ξ = conj (𝓕 f (-ξ))`, obtained by moving the real-linear isometry
  `r3CConj` through the Bochner integral and conjugating the character
  (`Circle.coe_inv_eq_conj`, `AddChar.map_neg_eq_inv`);
- the Schwartz form `fourier_r3SchwartzConjCLM` and the `toLp` compatibility of both carrier
  involutions;
- the exact `L²` intertwining `fourier_r3L2Conj`:
  `𝓕 (r3L2Conj g) = r3L2Reflect (r3L2Conj (𝓕 g))`, by `DenseRange.induction_on` over
  `SchwartzMap.denseRange_toLpCLM`, `SchwartzMap.toLp_fourier_eq`, and closedness of the
  agreement set;
- the predicate equivalence `isR3RealVelocity_iff_fourier_conjugateSymmetric`:
  `IsR3RealVelocity g ↔ IsR3ConjugateSymmetricVelocity (𝓕 g)`, with the reverse direction from
  injectivity of the Plancherel isometry.

The operator-realness gate is closed (2026-08-19):
`Formal/R3StokesConjugationEquivariance.lean` proves the generic statement that a Fourier
multiplier realized a.e. by a real, even scalar symbol commutes with `r3L2Conj` (via the
frequency-side commutation with `r3L2Reflect ∘ r3L2Conj`, the Plancherel bridge, and
injectivity), and applies it to `r3StokesL2Operator`, `r3StokesH3Evolution`, and
`r3StokesH2ToH3Operator`, with `IsR3RealVelocity` preservation corollaries
(`.stokesL2`, `.stokesH3`, `.stokesH2ToH3`). `Formal/R3LerayConjugationEquivariance.lean`
extends this to conjugation-equivariant, even **matrix-valued** symbols and applies it to
the `L²` Leray projector through its a.e. fiber realization
(`r3LerayL2FrequencyOperator_ae`), giving `r3L2Conj_r3LerayL2Operator` and
`IsR3RealVelocity.leray`.

`Formal/R3LerayConjugationEquivariance.lean` further proves the matrix-multiplier
equivariance theorems and `r3L2Conj_r3LerayL2Operator` (with the order-two/order-three
variants), and `Formal/R3ConvectionConjugationEquivariance.lean` closes the gate: carrier
antilinearity, conjugation equivariance of real even Schwartz Fourier multipliers and of the
Bessel coordinate map, conjugation equivariance of the Schwartz convection, the
triple-conjugated bilinear map identified with `r3ConvectionH3ToH2` by dense-core
uniqueness, and the projected-convection equivariance with its `IsR3RealVelocity`
corollary. **Every concrete operator of the mild theory is now conjugation-equivariant.**

The physically real local mild solution is closed (2026-08-19,
`Formal/R3RealLocalMildSolution.lean`): conjugation equivariance of the endpoint-safe Duhamel
integrand, the conjugated trajectory of a mild solution with real datum is again a mild
solution (conjugation passes through the Bochner interval integral by
`ContinuousLinearMap.intervalIntegral_comp_comm`), and ball uniqueness pins it to the
original — `r3EndpointSafeProjected_exists_realLocalMildSolution` gives, for real data, a
mild solution that is pointwise physically real on the certified horizon.

The explicit quantitative lifespan is closed (2026-08-19,
`Formal/R3QuantitativeLifespan.lean`, with the abstract Picard layer refactored so that
`exists_isMildSolutionOn_of_kernelPrimitive_lt` accepts **any** horizon satisfying the
kernel-mass smallness, the old existential theorem now being a corollary):

- closed-form kernel mass `r3EndpointSafeProjected_kernelPrimitive_eq`:
  `K(T) = T + √T/(π√ν)` for `T ≥ 0`;
- the explicit lifespan `r3MildLifespan nu r = (δ(r)/(1 + (π√ν)⁻¹ + δ(r)))²` with
  `δ(r) = r3MildSmallnessThreshold r`, positivity, `≤ 1`, and `K(T₀) < δ`;
- `r3EndpointSafeProjected_exists_mildSolutionOn_mildLifespan` and
  `r3EndpointSafeProjected_exists_realMildSolutionOn_mildLifespan`: existence, ball bound,
  ball uniqueness (and pointwise realness for real data) on the explicit horizon
  `T₀(ν, ‖u₀‖)`.

The mild restart identity and unrestricted uniqueness are closed (2026-08-19,
`Formal/EndpointSafeTwoSpaceRestart.lean`, `Formal/EndpointSafeTwoSpaceUniqueness.lean`):
a mild solution restarted at a certified time solves the shifted mild equation
(`IsMildSolutionOn.restart`, via `smoothing_coherent` and integrand translation); two mild
solutions with the same datum agree on their common horizon with **no ball restriction**
(`IsMildSolutionOn.unique`, contraction step + restart patching + Archimedes); and every
mild solution with physically real datum is pointwise physically real
(`IsR3EndpointSafeProjectedMildSolutionOn.isR3RealVelocity`), with no ball hypothesis.

The maximal-continuation layer is closed in blow-up–dichotomy form (2026-08-19,
`Formal/EndpointSafeTwoSpaceConcatenation.lean`, `Formal/R3MildContinuation.lean`): the
concatenation identity (converse of restart), antitonicity of the explicit lifespan in the
datum norm, the uniform-step extension of norm-bounded mild solutions, and the dichotomy
`r3EndpointSafeProjected_blowup_dichotomy` — either arbitrarily long horizons carry mild
solutions, or the certified solution norms escape every ball.

### T-SEL bridge statement layer and conditional assembly — 2026-09-02

The selected Stage-9 theorem **T-SEL = L_a** (`docs/gates/STAGE9_REVERSE_GAP_AUDIT_2026-09-02.md`,
SS-5/SS-6) now has its ten-lemma paper bridge formalized as a Lean statement layer plus
a fully proved conditional assembly (`docs/formal/TSEL_BRIDGE_FORMALIZATION_2026-09-02.md`
is the complete record; every artifact is listed there with its CLOSED/OPEN status):

- **proved**: the Grönwall–Bellman integral inequality (SEL-6,
  `le_mul_exp_of_le_add_intervalIntegral`, new standalone infrastructure); the
  quantitative decoded embedding (SEL-2, `r3TSel_decoded_embedding`:
  `r3DecodedSup f + r3DecodedGradSup f ≤ C_emb ‖f‖` with explicit Cauchy–Schwarz
  constants, plus everywhere-`C¹` derivative bounds, Schwartz-core pinning, a.e.
  identification with the decoded velocity, and Lipschitz continuity of the
  gradient-sup); the SEL-7 bookkeeping (norm continuity, integrand interval
  integrability, `Q`-monotonicity for `r3TSelGradIntegral`); SEL-8 realness
  instantiation; the SEL-9 exponential carrier bound **conditional on the ladder**
  (`r3TSel_carrierBound_of_ladder`, ν-free); SEL-10 uniqueness transfer and plug
  discharge; and the composed chain `N0 → N1 → N2 → N3`
  (`r3TSel_uniform_carrierBound_of_head`, `r3TSel_horizons_unbounded`,
  `r3TSel_admissibleSchwartz_globalContinuation`,
  `r3TSel_conditional_globalContinuation`).
- **proved in the third session (T-SEL discharge step,
  `docs/formal/TSEL_BRIDGE_DISCHARGE_2026-09-02.md`)**: the SEL-1 comparability
  (`r3TSel_classicalSobolevComparability`, explicit constants `1/81` and `27(2π)⁶`)
  and the SEL-4 BKM derivative-tuple commutator (`r3TSel_katoPonceCommutator`,
  explicit constant `93(2π)³`; the Prop was restated to the audit record's own `D^α`
  form — the sharp fractional `J³` Kato–Ponce is consumed by nothing in the chain and
  is not claimed).  The ladder Prop `R3TSelH3Ladder` now carries the
  `IsR3RealVelocity u0` hypothesis required by the transport cancellation (supplied
  for admissible data by SEL-8).
- **stated only, OPEN, never asserted** (Prop-valued definitions consumed as explicit
  hypotheses): the head `N0` (`R3TSelGradientBound`, `R3TSelHead`) — **no proof search
  performed, per commission**; the integrated `H³` ladder (SEL-5, `R3TSelH3Ladder`);
  and interior Sobolev smoothing (SEL-3 clause, `R3TSelInteriorSobolevSmoothing`).
  The intended discharge route for both (mollified energy method, Friedrichs
  commutator, SEL-4 extension to mollified fields) and the checked dead ends are
  recorded in the discharge record's §4.

Do not cite the conditional theorems as unconditional results: each carries its open
hypotheses in its statement. Do not treat `r3DecodedGradSup` as an intrinsic
distributional `W^{1,∞}` seminorm — it is the gradient-sup of the explicit decoded
representative, a.e.-pinned to the decoded velocity.

The next analytic gates, in intended order:

1. optional refinement of the continuation layer: the canonical glued maximal trajectory
   `u* : [0, T*) → H³` (choice + unrestricted uniqueness) and the pointwise restatement
   `T* < ∞ ⇒ limsup ‖u* t‖ = ∞`, connected to the existing
   `FlowMapNonextendibilityCriterion` / `UniformRestartContinuation` layers;
2. connection of the concrete evolution to the abstract `MildEvolutionKernel` /
   `LerayProjectedQuadraticContract` mild-theory and flow-map interfaces.

The fixed-point layer, the reality gate, the quantitative lifespan, the uniqueness layer,
and the continuation dichotomy are all statements on the Bessel-coordinate carrier.

**Above that layer (2026-08-22/23), the chain continues and is closed** — this section's
positive record stops at the carrier, so the theorem-level record of the upper layers lives
in [`docs/formal/R3_NS_VERTICAL_INTEGRATION_STATUS.md`](docs/formal/R3_NS_VERTICAL_INTEGRATION_STATUS.md)
and the readiness audit
[`docs/formal/STAGE9_READINESS_AUDIT_2026-08-23.md`](docs/formal/STAGE9_READINESS_AUDIT_2026-08-23.md).
The anchors are: decoded-velocity semantics (Laplacian / convection / Helmholtz pressure /
divergence all identified by theorem); the **Navier–Stokes capstone**
`r3EndpointSafeProjectedMild_navierStokes` (`Formal/R3NavierStokesEquation.lean`);
pointwise-in-time finite energy (`Formal/R3FiniteEnergy.lean`); realness transport through
the decoder (`Formal/R3DecodedVelocityRealness.lean`); and the admissible Schwartz
initial-data adapter `r3AdmissibleSchwartzDatum_navierStokes`
(`Formal/R3SchwartzInitialData.lean`, `Formal/R3SchwartzDivergence.lean`).

Pressure **reconstruction** is therefore no longer open (edge 2a, closed and consumed); its
regularity is. The glued maximal trajectory and every Clay-level statement remain open.

## 7. What is still not formalized

The Lean development does **not** currently establish:

- the T-SEL head `N0` (`R3TSelGradientBound` / `R3TSelHead`) in either direction, nor
  the open bridge statements `R3TSelH3Ladder` and `R3TSelInteriorSobolevSmoothing` —
  statement definitions only, and every `r3TSel_*` continuation theorem is conditional
  on the ones it names (`R3TSelClassicalSobolevComparability` and
  `R3TSelKatoPonceCommutator` are proved);
- the sharp fractional (`J³`-form) Kato–Ponce commutator, in either direction;
- Clay statement A, B, C, or D;
- global smoothness or global existence for arbitrary 3D data;
- a blow-up counterexample;
- a closed-form general solution;
- continuation of a `C¹` solution map through a singular time;
- equality, for arbitrary completed `H³` inputs, between the decoded extension
  and a separately constructed distributional convection product;
- a theorem that the Leray symbol maps Schwartz space to itself;
- any regularity, decay, or uniqueness statement for the reconstructed pressure — the
  reconstruction itself is **closed** (edge 2a, `Formal/R3HelmholtzPressure.lean`,
  `r3HelmholtzPressure_gradient`: `∇p = −(I−P)F` componentwise in `𝓢'` for every `L²`
  source; consumed by the Navier–Stokes capstone through
  `postcomp_r3LerayL2Operator_eq`), but the pressure is determined only up to additive
  harmonic terms and no `Lᵖ`/Sobolev regularity is proved;
- a bounded `H² → H³` Stokes map at zero elapsed time or zero viscosity (such a bound is not
  expected);
- a canonical glued maximal trajectory `u* : [0, T*) → H³` with the pointwise blow-up
  statement `T* < ∞ ⇒ limsup ‖u* t‖ = ∞` (the certified-horizon blow-up **dichotomy** is
  formalized; the trajectory-level restatement is not);
- a complete projected Navier--Stokes quadratic map on the final selected Sobolev/mild carrier with all mapping estimates;
- **any implication from the coordinate carrier to smoothness or decay** — in particular
  `H³ ⇒ C^∞` and `H³ ⇒` rapid decay are **not** proved, not claimed, and not used; the
  admissible-data adapter (`Formal/R3SchwartzInitialData.lean`) runs in the opposite
  direction (concrete Schwartz datum ⇒ carrier coordinate, with `decode ∘ encode = id`);
- a characterization of arbitrary `R3HsVelocity 3` elements as smooth rapidly decaying
  fields (Clay semantic edge 3 *proper*; only the concrete admissible-class adapter is
  closed);
- a uniform-in-time energy bound, an energy inequality, or a dissipation identity
  (finite energy is proved **at each time**; `edge 4-uniform: DEFERRED / NON-BLOCKING FOR
  STAGE 9`);
- a classical (pointwise) solution: the certified time derivative is strong `L²`-valued
  and the momentum equation is componentwise in `𝓢'`, at **interior** times of a **local**
  certified horizon;
- a connection of the new concrete local mild solutions to the abstract `MildEvolutionKernel` /
  `LerayProjectedQuadraticContract` mild-theory and flow-map interfaces;
- an open admissible initial-data domain with `C¹` solution-map dependence for that concrete equation;
- a rigorous finite-cylinder Hou to official Clay-domain transfer;
- convergence of the MNS-2 discrete/reduced bridge to a continuum Navier--Stokes bridge.

Unverified feature-branch drafts are not part of this theorem boundary until accepted by the pinned Lean gate and landed on `main`.

## 8. Remaining near-term formal obligations

For the current Schwartz/Sobolev route, the intended order is:

1. ~~formulate the endpoint-safe two-space Duhamel contract and prove actual integrand
   measurability, interval-integrability, and the resulting norm estimate~~ — closed by PR #82;
2. ~~instantiate it with `r3ProjectedConvectionH3ToH2`, `r3StokesH2ToH3Operator`, and an honestly
   interpreted same-space `H³` Stokes evolution~~ — closed by PR #82;
3. ~~prove the fixed-point/local-existence statements for the endpoint-safe two-space contract in
   the complex Bessel-coordinate carrier, with uniqueness at least in the certified ball~~ —
   closed by `Formal/EndpointSafeTwoSpacePicard.lean` and
   `Formal/R3EndpointSafeProjectedLocalExistence.lean`;
4. ~~construct the physical real-valued/conjugate-symmetric carrier restriction~~ — closed by
   the conjugation/reflection, Plancherel-bridge, operator-equivariance, and
   `Formal/R3RealLocalMildSolution.lean` slices;
5. strengthen the local theory: ~~quantitative horizon~~ (closed by
   `Formal/R3QuantitativeLifespan.lean`), ~~unrestricted uniqueness~~ (closed by
   `Formal/EndpointSafeTwoSpaceRestart.lean` + `Formal/EndpointSafeTwoSpaceUniqueness.lean`),
   ~~continuation in blow-up–dichotomy form~~ (closed by
   `Formal/EndpointSafeTwoSpaceConcatenation.lean` + `Formal/R3MildContinuation.lean`),
   then the glued maximal trajectory, and connect the concrete evolution to the
   mild-theory and flow-map interfaces.

**Status 2026-08-23 — the near-term formal queue is CLOSED for Stage 9.** The Clay
semantic-promotion edges 1, 2 and 3-adapter are `THEOREM-CLOSED`, edge 4 is `PARTIAL`
(pointwise-in-time), and the Stage-9 readiness audit
(`docs/formal/STAGE9_READINESS_AUDIT_2026-08-23.md`) returned **`PASS`**. Per the audit's
stop rule, the remaining items in this section — the glued maximal trajectory, the
abstract-interface adapters, uniform-in-time energy, classical regularity, endpoint
derivatives, general pressure regularity, edge-3-proper class semantics, and edge-5 Clay
packaging — are **NOT** to be worked on for completeness. They are revisited only when a
concrete Stage-9 theorem consumes one of them.

A later PDE layer must still supply the exact local-wellposedness carrier and prove that the concrete Stokes, Leray, convection, and projected quadratic objects instantiate the intended mild theory with the required regularity.

## 9. Numerical and domain scope

Finite-dimensional path identities, POD/SVD reductions, modal tangent reconstruction, and synthetic Hou-like data remain numerical/reduction tools only.

A continuum promotion requires explicit convergence of solution maps and pathwise tangent actions on a common time interval. A finite-cylinder Hou computation is not an official `R^3` or periodic Clay-domain computation without a rigorous transfer theorem.

## 10. Audit policy

The formal source gate rejects `sorry`, `admit`, local `axiom`, and source-level `opaque` declarations under `Formal/`.

`Formal/AxiomAudit.lean` prints axiom dependencies of selected strong formal theorems into the Lean build log.

The intended verification policy is documented in `docs/LEAN_CI_OPERATIONS.md`. Green Lean verification remains the merge gate for mathematical PRs. The preferred interactive path is now a ChatGPT-connected external Lean runner that reproduces the pinned repository gate; local/self-hosted or deliberately spent GitHub-hosted checks remain valid reproduction/final-confirmation paths when they check the exact relevant revision and toolchain.
