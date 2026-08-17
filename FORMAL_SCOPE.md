# Formal scope and theorem boundary

Last synchronized: 2026-08-17 (JST), after local full verification of commit
`2127757807768709d1ac19a0ec6f760c48a973cc`.

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

## 6. Exact current analytic gate

The density, bounded-extension, and order-aware projected-convection bridges
are closed. The next analytic gate is the smoothing layer:

1. for strictly positive viscosity `ν` and positive elapsed time `τ`, construct
   the genuine `H² → H³` Stokes coordinate multiplier
   `(1 + ‖ξ‖²)^(1/2) * exp(-(2π)² ν τ ‖ξ‖²)`;
2. prove its Fourier realization, compatibility with the existing physical
   `L²` Stokes operator under the order-two/order-three decoders, an explicit
   `O(1 + (ν τ)^(-1/2))` (or sharper) norm bound, and local time-integrability
   near `τ = 0`;
3. prove the required Leray/solenoidal compatibility;
4. introduce a two-space mild/Duhamel contract, or prove a genuinely
   same-space estimate, before connecting the result to the existing abstract
   flow-map layer.

The same-order `r3StokesL2Operator` cannot be retyped through the phantom
Sobolev alias to manufacture `H² → H³` smoothing. Such smoothing is unavailable
at elapsed time zero and at zero viscosity.

## 7. What is still not formalized

The Lean development does **not** currently establish:

- Clay statement A, B, C, or D;
- global smoothness or global existence for arbitrary 3D data;
- a blow-up counterexample;
- a closed-form general solution;
- continuation of a `C¹` solution map through a singular time;
- equality, for arbitrary completed `H³` inputs, between the decoded extension
  and a separately constructed distributional convection product;
- a physical real-valued restriction of the completed projected convection map
  (in particular, Fourier conjugate symmetry has not been proved);
- a theorem that the Leray symbol maps Schwartz space to itself;
- pressure reconstruction for the completed projected map;
- a positive-time `H² → H³` Stokes smoothing estimate and locally integrable
  Duhamel kernel bound;
- a complete projected Navier--Stokes quadratic map on the final selected Sobolev/mild carrier with all mapping estimates;
- local existence and uniqueness for the fully concrete `R^3` mild equation used by the flow-map program;
- an open admissible initial-data domain with `C¹` solution-map dependence for that concrete equation;
- a rigorous finite-cylinder Hou to official Clay-domain transfer;
- convergence of the MNS-2 discrete/reduced bridge to a continuum Navier--Stokes bridge.

Unverified feature-branch drafts are not part of this theorem boundary until accepted by the pinned Lean gate and landed on `main`.

## 8. Remaining near-term formal obligations

For the current Schwartz/Sobolev route, the intended order is:

1. construct positive-elapsed-time, positive-viscosity `H² → H³` Stokes smoothing and
   prove its time-singular bound is locally integrable;
2. prove its exact decoder and Leray/solenoidal compatibility;
3. formulate the required two-space Duhamel contract, while separately
   constructing the physical real-valued carrier restriction;
4. only then connect the concrete projected operator to the mild-theory and
   flow-map interfaces.

A later PDE layer must still supply the exact local-wellposedness carrier and prove that the concrete Stokes, Leray, convection, and projected quadratic objects instantiate the intended mild theory with the required regularity.

## 9. Numerical and domain scope

Finite-dimensional path identities, POD/SVD reductions, modal tangent reconstruction, and synthetic Hou-like data remain numerical/reduction tools only.

A continuum promotion requires explicit convergence of solution maps and pathwise tangent actions on a common time interval. A finite-cylinder Hou computation is not an official `R^3` or periodic Clay-domain computation without a rigorous transfer theorem.

## 10. Audit policy

The formal source gate rejects `sorry`, `admit`, local `axiom`, and source-level `opaque` declarations under `Formal/`.

`Formal/AxiomAudit.lean` prints axiom dependencies of selected strong formal theorems into the Lean build log.

The intended verification policy is documented in `docs/LEAN_CI_OPERATIONS.md`. Green Lean verification remains the merge gate for mathematical PRs. The preferred interactive path is now a ChatGPT-connected external Lean runner that reproduces the pinned repository gate; local/self-hosted or deliberately spent GitHub-hosted checks remain valid reproduction/final-confirmation paths when they check the exact relevant revision and toolchain.
