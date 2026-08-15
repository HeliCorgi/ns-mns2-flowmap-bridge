# Formal scope and theorem boundary

Last synchronized: 2026-08-15 (JST), after merged PR #76. PR #77 is CI infrastructure only and does not change the theorem boundary.

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

The current active formal target is the one-coordinate `H³ → H²` convection estimate needed by

`R3SchwartzConvectionTermSobolevEstimate 3`

in `Formal/R3SchwartzConvectionSobolevReduction.lean`.

Once that one-coordinate estimate is proved, the existing reduction gives the full summed convection estimate with the finite-dimensional coordinate factor.

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

These are bundled `L²` estimates. They do not by themselves identify the bundled convolution with the ordinary pointwise scalar convolution used in the majorants.

### Norm-field `L²` bundling

`Formal/R3SchwartzNormFieldL2.lean` defines canonical `L²` bundles of the pointwise norm fields of scalar- and velocity-valued Schwartz functions:

- `r3SchwartzScalarNormL2`;
- `r3SchwartzVelocityNormL2`.

Lean proves:

- their representatives agree a.e. with the literal pointwise norm fields;
- taking pointwise norm preserves the corresponding `L²` norm;
- the left and right H² majorants have canonical bundled Young candidates
  - `r3H2LeftMajorantYoungL2`;
  - `r3H2RightMajorantYoungL2`;
- those candidates satisfy the expected `L² * L¹ → L²` and `L¹ * L² → L²` bounds.

### Existing H³ Fourier bounds

The repository also contains the Fourier `L¹`/`L²` control and derivative-weight infrastructure needed after the convolution identification closes, including:

- `Formal/R3H2FourierL1Bound.lean`
- `Formal/R3H2VelocityFourierL1Bound.lean`
- `Formal/R3H2CoordinateFourierBounds.lean`
- `Formal/R3H3DerivativeWeightGeometry.lean`
- `Formal/R3SchwartzDerivativeFrequencyBound.lean`
- `Formal/R3SchwartzDerivativeH3LpBounds.lean`

These supply the H³-side factors that are intended to feed the final one-coordinate H² convection estimate.

## 6. Exact current analytic gate

The following identification is **not yet formalized**:

`ordinary scalar convolution majorant = bundled Bochner Young convolution representative`

more concretely, the ordinary pointwise fields represented by

- `r3H2LeftScalarMajorant a b`;
- `r3H2RightScalarMajorant a b`

have not yet been proved a.e. equal to the representatives of

- `r3H2LeftMajorantYoungL2 a b`;
- `r3H2RightMajorantYoungL2 a b`.

This requires a representative/Fubini identification theorem (or an equivalent direct `L²` proof). Do **not** close this gap with `rfl`, `simpa`, or an informal appeal to the two formulas looking the same.

Until this gate is discharged, the repository does not prove `R3SchwartzConvectionTermSobolevEstimate 3`.

## 7. What is still not formalized

The Lean development does **not** currently establish:

- Clay statement A, B, C, or D;
- global smoothness or global existence for arbitrary 3D data;
- a blow-up counterexample;
- a closed-form general solution;
- continuation of a `C¹` solution map through a singular time;
- `R3SchwartzConvectionTermSobolevEstimate 3`;
- the full concrete `H³ → H²` convection estimate until the scalar-convolution identification is closed;
- a complete projected Navier--Stokes quadratic map on the final selected Sobolev/mild carrier with all mapping estimates;
- local existence and uniqueness for the fully concrete `R^3` mild equation used by the flow-map program;
- an open admissible initial-data domain with `C¹` solution-map dependence for that concrete equation;
- a rigorous finite-cylinder Hou to official Clay-domain transfer;
- convergence of the MNS-2 discrete/reduced bridge to a continuum Navier--Stokes bridge.

## 8. Remaining near-term formal obligations

For the current Schwartz/Sobolev route, the intended order is:

1. prove the a.e. representative identification between the ordinary scalar convolution majorants and the bundled real Young convolutions;
2. use the bundled Young estimates to obtain `L²` bounds for both majorants;
3. insert the existing H³ Fourier `L¹`/`L²` bounds;
4. prove `R3SchwartzConvectionTermSobolevEstimate 3`;
5. use the existing reduction to obtain the full `R3SchwartzConvectionSobolevEstimate 3`;
6. only then connect the estimate to the projected quadratic/mild operator layer.

A later PDE layer must still supply the exact local-wellposedness carrier and prove that the concrete Stokes, Leray, convection, and projected quadratic objects instantiate the intended mild theory with the required regularity.

## 9. Numerical and domain scope

Finite-dimensional path identities, POD/SVD reductions, modal tangent reconstruction, and synthetic Hou-like data remain numerical/reduction tools only.

A continuum promotion requires explicit convergence of solution maps and pathwise tangent actions on a common time interval. A finite-cylinder Hou computation is not an official `R^3` or periodic Clay-domain computation without a rigorous transfer theorem.

## 10. Audit policy

The formal source gate rejects `sorry`, `admit`, local `axiom`, and source-level `opaque` declarations under `Formal/`.

`Formal/AxiomAudit.lean` prints axiom dependencies of selected strong formal theorems into the Lean build log.

The intended verification policy is documented in `docs/LEAN_CI_OPERATIONS.md`. Green Lean verification remains the merge gate for mathematical PRs, whether the computation is GitHub-hosted, self-hosted, or locally reproduced according to the repository policy.
