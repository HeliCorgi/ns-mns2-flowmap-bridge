import Formal.NavierStokesTimeBridge
import Formal.R3CoordinateIncompressibility
import Formal.R3ClassicalIncompressibility
import Formal.R3DecoderFrequencyBridge
import Formal.R3InversionConsistency
import Formal.R3HelmholtzPressure
import Formal.FlowMapNonextendibilityCriterion
import Formal.UniformRestartContinuation
import Formal.TerminalFlowMapAmplification
import Formal.TerminalFlowMapOperatorNorm
import Formal.MildSolutionSemantics
import Formal.MildFlowMapBridge
import Formal.MildZeroUniqueness
import Formal.QuadraticMildNonlinearity
import Formal.QuadraticLinearizedMild
import Formal.QuadraticMildTangentAdapter
import Formal.QuadraticMildFixedPointDerivative
import Formal.QuadraticMildTangentRealization
import Formal.QuadraticMildCoherentFamilyAdapter
import Formal.LerayProjectedQuadratic
import Formal.R3LerayFrequencySymbol
import Formal.R3StokesFrequencySymbol
import Formal.R3StokesL2Operator
import Formal.R3LerayL2Operator
import Formal.R3LerayFourierBridge
import Formal.R3LerayComplexFiberSymbol
import Formal.R3SobolevCarrier
import Formal.R3SchwartzConvectionSobolevEstimate
import Formal.R3SobolevConvectionExtension
import Formal.R3ProjectedSobolevConvection
import Formal.R3StokesH2H3Smoothing
import Formal.EndpointSafeTwoSpaceDuhamel
import Formal.R3StokesH3Evolution
import Formal.R3EndpointSafeProjectedDuhamel
import Formal.EndpointSafeTwoSpacePicard
import Formal.R3EndpointSafeProjectedLocalExistence
import Formal.R3ConjugationReflection
import Formal.R3FourierConjugationBridge
import Formal.R3StokesConjugationEquivariance
import Formal.R3LerayConjugationEquivariance
import Formal.R3ConvectionConjugationEquivariance
import Formal.R3RealLocalMildSolution
import Formal.R3QuantitativeLifespan
import Formal.EndpointSafeTwoSpaceRestart
import Formal.EndpointSafeTwoSpaceUniqueness
import Formal.EndpointSafeTwoSpaceConcatenation
import Formal.R3ConvectionSourceIdentification
import Formal.R3MildContinuation
import Formal.ReducedBridgeResidual
import Formal.FiniteRankReducedBridge

/-
CI-visible axiom audit for the strongest currently formalized bridge theorems.

These commands do not add assumptions. They print the axiom dependencies of the declarations
into the Lean build log so that unexpected dependencies are visible during review.
-/
#print axioms MNS2.affine_flowmap_bridge_of_contDiffOn_open
#print axioms MNS2.radial_flowmap_bridge_of_contDiffOn_open
#print axioms MNS2.FixedTimePDEBridgeAdapter.affine_bridge
#print axioms MNS2.FixedTimePDEBridgeAdapter.radial_bridge
#print axioms MNS2.FixedTimePDEBridgeAdapter.radial_bridge_of_zero_fixed
#print axioms MNS2.NavierStokesTimeBridgeAdapter.affine_bridge_at_time
#print axioms MNS2.NavierStokesTimeBridgeAdapter.radial_bridge_at_time
#print axioms MNS2.NavierStokesTimeBridgeAdapter.radial_bridge_at_time_of_zero_fixed
#print axioms MNS2.FlowMapContinuationPackage.endpoint_norm_le_of_radial_directional_bound
#print axioms MNS2.FlowMapContinuationPackage.directional_fderiv_unbounded_of_nonextendible
#print axioms MNS2.FlowMapUniformRestartPackage.continuation_of_uniform_endpoint_bound
#print axioms MNS2.FlowMapUniformRestartPackage.directional_fderiv_unbounded_of_nonextendible
#print axioms MNS2.FlowMapUniformRestartPackage.terminal_directional_fderiv_unbounded_of_nonextendible
#print axioms MNS2.FlowMapUniformRestartPackage.eventually_arbitrarily_large_directional_fderiv
#print axioms MNS2.FlowMapUniformRestartPackage.terminal_fderiv_opNorm_unbounded_of_nonextendible
#print axioms MNS2.FlowMapUniformRestartPackage.exists_terminal_fderiv_opNorm_above
#print axioms MNS2.MildEvolutionKernel.evolvesAt_nonnegative
#print axioms MNS2.MildEvolutionKernel.evolvesAt_zero_eq_initial
#print axioms MNS2.MildEvolutionKernel.evolvesAt_endpoint_equation
#print axioms MNS2.NavierStokesTimeBridgeAdapter.mild_endpoint_equation
#print axioms MNS2.NavierStokesTimeBridgeAdapter.radial_path_has_mild_witness
#print axioms MNS2.NavierStokesTimeBridgeAdapter.radial_bridge_eq_mild_duhamel
#print axioms MNS2.MildEvolutionKernel.trajectoryUniqueOn_endpointUniqueAt
#print axioms MNS2.MildEvolutionKernel.zero_isMildSolutionOn
#print axioms MNS2.MildEvolutionKernel.zero_evolvesAt_zero
#print axioms MNS2.NavierStokesTimeBridgeAdapter.stateMap_zero_of_mild_endpointUnique
#print axioms MNS2.NavierStokesTimeBridgeAdapter.stateMap_zero_of_mild_trajectoryUnique
#print axioms MNS2.NavierStokesTimeBridgeAdapter.radial_bridge_eq_mild_duhamel_of_endpointUnique
#print axioms MNS2.hasFDerivAt_quadraticDiagonal
#print axioms MNS2.fderiv_quadraticDiagonal
#print axioms MNS2.MildEvolutionKernel.ofQuadratic_zero_evolvesAt_zero
#print axioms MNS2.quadraticLinearizedMild_equation_at_time_expanded
#print axioms MNS2.quadraticMildTangentEvolvesAt_nonnegative
#print axioms MNS2.quadraticMildTangentEvolvesAt_zero_eq_initial
#print axioms MNS2.quadraticMildTangent_zero_evolvesAt_zero
#print axioms MNS2.QuadraticMildC1TangentAdapter.fderiv_realizes_linearized_mild
#print axioms MNS2.QuadraticMildC1TangentAdapter.radial_bridge_with_linearized_mild_semantics
#print axioms MNS2.QuadraticMildC1TangentAdapter.radial_endpoint_bridge_with_linearized_mild_semantics
#print axioms MNS2.quadraticMild_fixedPoint_fderiv_eq_of_dominated
#print axioms MNS2.quadraticMild_fixedPoint_fderiv_apply_eq_of_dominated
#print axioms MNS2.quadraticMild_fixedPoint_fderiv_eq_of_dominated_on_nhds
#print axioms MNS2.quadraticMild_fixedPoint_fderiv_apply_eq_of_dominated_on_nhds
#print axioms MNS2.quadraticMildRHSDerivativeAtTime_apply_eq_linearized
#print axioms MNS2.quadraticMild_fixedPoint_direction_equation_of_certificate
#print axioms MNS2.quadraticMild_fixedPoint_direction_equation_of_local_certificate
#print axioms MNS2.quadraticMildTangentEvolvesAt_of_dominated_fixedPoint_family
#print axioms MNS2.quadraticMildTangentEvolvesAt_of_local_fixedPoint_family
#print axioms MNS2.QuadraticMildC1CoherentFamilyAdapter.fderiv_realizes_linearized_mild
#print axioms MNS2.QuadraticMildC1CoherentFamilyAdapter.radial_bridge_with_derived_tangent_semantics
#print axioms MNS2.LerayProjectedQuadraticContract.leray_idempotent_apply
#print axioms MNS2.LerayProjectedQuadraticContract.projectedConvection_mem
#print axioms MNS2.LerayProjectedQuadraticContract.quadraticDerivative_mem
#print axioms MNS2.LerayProjectedQuadraticContract.fderiv_mildKernel_nonlinearity_mem
#print axioms MNS2.mem_r3SolenoidalFiber_iff_inner
#print axioms MNS2.r3LeraySymbol_mem
#print axioms MNS2.inner_r3LeraySymbol_eq_zero
#print axioms MNS2.r3LeraySymbol_idempotent
#print axioms MNS2.norm_r3LeraySymbol_le
#print axioms MNS2.r3LeraySymbol_zero
#print axioms MNS2.r3LeraySymbol_self
#print axioms MNS2.r3LeraySymbol_apply
#print axioms MNS2.r3StokesDecayRate_nonneg
#print axioms MNS2.r3StokesScalar_le_one
#print axioms MNS2.r3StokesFrequencySymbol_zero_time
#print axioms MNS2.r3StokesFrequencySymbol_add_time
#print axioms MNS2.r3StokesFrequencySymbol_mem
#print axioms MNS2.r3StokesFrequencySymbol_commutes_leray
#print axioms MNS2.norm_r3StokesFrequencySymbol_le
#print axioms MNS2.r3StokesLerayFrequencySymbol_mem
#print axioms MNS2.continuous_r3StokesScalarComplex
#print axioms MNS2.norm_r3StokesScalarComplex_le_one
#print axioms MNS2.r3StokesL2FrequencyMultiplier_ae
#print axioms MNS2.fourier_r3StokesL2Operator
#print axioms MNS2.r3StokesL2FrequencyMultiplier_zero_time
#print axioms MNS2.r3StokesL2Operator_zero_time
#print axioms MNS2.r3LerayL2Operator_mem_solenoidal
#print axioms MNS2.r3NormalizedDivergenceL2OperatorAux_r3LerayL2Operator
#print axioms MNS2.r3LerayL2Operator_fixed_of_mem
#print axioms MNS2.r3LerayL2Operator_idempotent
#print axioms MNS2.norm_r3LerayL2Operator_apply_le
#print axioms MNS2.norm_r3LerayL2Operator_le_one
#print axioms MNS2.fourier_mem_r3L2FrequencySolenoidalSubmodule_iff
#print axioms MNS2.map_r3L2SolenoidalSubmodule_fourier
#print axioms MNS2.r3LerayL2FrequencyOperator_mem_solenoidal
#print axioms MNS2.fourier_r3LerayL2Operator
#print axioms MNS2.mem_r3ComplexSolenoidalFiber_iff_inner
#print axioms MNS2.r3LeraySymbolComplex_mem
#print axioms MNS2.inner_r3LeraySymbolComplex_eq_zero
#print axioms MNS2.r3LeraySymbolComplex_fixed_of_mem
#print axioms MNS2.r3LeraySymbolComplex_idempotent
#print axioms MNS2.norm_r3LeraySymbolComplex_le
#print axioms MNS2.r3LeraySymbolComplex_zero
#print axioms MNS2.r3LeraySymbolComplex_self
#print axioms MNS2.r3LeraySymbolComplex_apply
#print axioms MNS2.besselPotential_r3HsToTempered_eq_coordinate
#print axioms MNS2.r3HsToTempered_memSobolev
#print axioms MNS2.r3HmToTempered_memSobolev
#print axioms MNS2.r3StrongSobolevOrder_three
#print axioms MNS2.r3SchwartzConvectionTermSobolevEstimate_three
#print axioms MNS2.r3SchwartzConvectionSobolevEstimate_three
#print axioms MNS2.r3SchwartzToHsCLM_denseRange
#print axioms MNS2.r3ConvectionH3ToH2_apply_schwartz
#print axioms MNS2.r3HsToTempered_r3ConvectionH3ToH2_schwartz
#print axioms MNS2.norm_r3ConvectionH3ToH2_apply_le
#print axioms MNS2.r3ConvectionH3ToH2_unique
#print axioms MNS2.r3L2ToTempered_r3H2ToL2Operator
#print axioms MNS2.r3H2ToL2Operator_commutes_leray
#print axioms MNS2.r3HsToTempered_r3LerayH2Operator
#print axioms MNS2.norm_r3ProjectedConvectionH3ToH2_le
#print axioms MNS2.norm_r3ProjectedConvectionH3ToH2_apply_le
#print axioms MNS2.r3H2ToL2Operator_r3ProjectedConvectionH3ToH2_mem_solenoidal
#print axioms MNS2.r3HsToTempered_r3ProjectedConvectionH3ToH2
#print axioms MNS2.r3HsToTempered_r3ProjectedConvectionH3ToH2_schwartz
#print axioms MNS2.norm_r3StokesH2ToH3Operator_le
#print axioms MNS2.intervalIntegrable_r3StokesH2H3TimeKernel
#print axioms MNS2.r3L2ToTempered_r3H3ToL2Operator
#print axioms MNS2.r3H3ToL2Operator_r3StokesH2ToH3Operator
#print axioms MNS2.r3HsToTempered_r3StokesH2ToH3Operator
#print axioms MNS2.r3HsToTempered_r3LerayH3Operator
#print axioms MNS2.r3StokesH2ToH3Operator_commutes_leray
#print axioms MNS2.r3StokesH2ToH3Operator_mem_solenoidal
#print axioms MNS2.r3StokesL2Operator_r3H2ToL2Operator_mem_solenoidal
#print axioms MNS2.EndpointSafeTwoSpaceDuhamelContract.intervalIntegrable_duhamelIntegrand_of_continuousOn
#print axioms MNS2.EndpointSafeTwoSpaceDuhamelContract.isMildAt_zero_iff
#print axioms MNS2.r3StokesH3Evolution_add
#print axioms MNS2.continuous_r3StokesH3Evolution_action
#print axioms MNS2.r3H3ToL2Operator_r3StokesH3Evolution
#print axioms MNS2.r3StokesH2ToH3Operator_add_nnreal
#print axioms MNS2.aestronglyMeasurable_r3EndpointSafeProjectedDuhamelIntegrand
#print axioms MNS2.intervalIntegrable_r3EndpointSafeProjectedDuhamelIntegrand
#print axioms MNS2.norm_integral_r3EndpointSafeProjectedDuhamelIntegrand_le
#print axioms MNS2.r3EndpointSafeProjectedMild_equation_at_time
#print axioms MNS2.EndpointSafeTwoSpaceDuhamelContract.continuousOn_duhamelIntegral
#print axioms MNS2.EndpointSafeTwoSpaceDuhamelContract.exists_pos_time_isMildSolutionOn
#print axioms MNS2.r3EndpointSafeProjected_exists_localMildSolution
#print axioms MNS2.r3EndpointSafeProjected_localMildSolution_equation
#print axioms MNS2.r3L2Reflect_r3L2Conj
#print axioms MNS2.isR3RealVelocity_iff_im_ae
#print axioms MNS2.isR3ConjugateSymmetricVelocity_iff_reflect_eq_conj
#print axioms MNS2.isClosed_setOf_isR3RealVelocity
#print axioms MNS2.isClosed_setOf_isR3ConjugateSymmetricVelocity
#print axioms MNS2.r3Fourier_conj_eq
#print axioms MNS2.fourier_r3SchwartzConjCLM
#print axioms MNS2.fourier_r3L2Conj
#print axioms MNS2.isR3RealVelocity_iff_fourier_conjugateSymmetric
#print axioms MNS2.r3L2Conj_of_fourier_realEven
#print axioms MNS2.r3L2Conj_r3StokesL2Operator
#print axioms MNS2.r3L2Conj_r3StokesH3Evolution
#print axioms MNS2.r3L2Conj_r3StokesH2ToH3Operator
#print axioms MNS2.r3L2Conj_of_fourier_conjEquivariant_even
#print axioms MNS2.r3CConj_r3LeraySymbolComplex
#print axioms MNS2.r3L2Conj_r3LerayL2Operator
#print axioms MNS2.IsR3RealVelocity.leray
#print axioms MNS2.IsR3RealVelocity.stokesH3
#print axioms MNS2.r3L2Conj_r3LerayH2Operator
#print axioms MNS2.r3L2Conj_r3LerayH3Operator
#print axioms MNS2.r3L2Conj_r3SchwartzToHsCLM
#print axioms MNS2.r3SchwartzConvection_conj
#print axioms MNS2.r3ConjugatedConvectionH3ToH2_eq
#print axioms MNS2.r3L2Conj_r3ConvectionH3ToH2
#print axioms MNS2.r3L2Conj_r3ProjectedConvectionH3ToH2
#print axioms MNS2.IsR3RealVelocity.projectedConvection
#print axioms MNS2.IsR3EndpointSafeProjectedMildSolutionOn.r3L2Conj_comp
#print axioms MNS2.r3EndpointSafeProjected_exists_realLocalMildSolution

-- Explicit quantitative lifespan: given-horizon Picard, closed-form kernel mass
-- `K(T) = T + √T/(π√ν)`, the explicit lifespan `T₀ = (δ/(1+(π√ν)⁻¹+δ))²`, and the
-- quantitative existence theorems on the explicit horizon (complex + real data).
#print axioms MNS2.EndpointSafeTwoSpaceDuhamelContract.exists_isMildSolutionOn_of_kernelPrimitive_lt
#print axioms MNS2.r3MildSmallnessThreshold_pos
#print axioms MNS2.r3MildSmallnessThreshold_le_one
#print axioms MNS2.r3MildLifespan_pos
#print axioms MNS2.r3MildLifespan_le_one
#print axioms MNS2.r3EndpointSafeProjected_kernelPrimitive_eq
#print axioms MNS2.endpointSafe_lifespan_sq_add_lt
#print axioms MNS2.r3EndpointSafeProjected_kernelPrimitive_mildLifespan_lt
#print axioms MNS2.r3EndpointSafeProjected_exists_mildSolutionOn_mildLifespan
#print axioms MNS2.r3EndpointSafeProjected_exists_realMildSolutionOn_mildLifespan

-- Mild restart identity and unrestricted uniqueness: a mild solution restarted at a
-- certified time solves the shifted problem; two mild solutions with the same datum agree
-- on their common horizon (no ball restriction); consequently every mild solution with
-- physically real datum is pointwise physically real.
#print axioms MNS2.EndpointSafeTwoSpaceDuhamelContract.duhamelIntegrand_comp_add_left
#print axioms MNS2.EndpointSafeTwoSpaceDuhamelContract.IsMildSolutionOn.restart
#print axioms MNS2.IsR3EndpointSafeProjectedMildSolutionOn.restart
#print axioms MNS2.EndpointSafeTwoSpaceDuhamelContract.IsMildSolutionOn.mono
#print axioms MNS2.EndpointSafeTwoSpaceDuhamelContract.isMildSolutionOn_eq_of_contraction
#print axioms MNS2.EndpointSafeTwoSpaceDuhamelContract.IsMildSolutionOn.unique
#print axioms MNS2.r3EndpointSafeProjectedMildSolution_unique
#print axioms MNS2.IsR3EndpointSafeProjectedMildSolutionOn.isR3RealVelocity

-- Maximal continuation layer: the concatenation identity (converse of restart), the
-- antitone explicit lifespan, the uniform-step extension of norm-bounded solutions, and
-- the blow-up dichotomy for the certified-horizon set.
#print axioms MNS2.EndpointSafeTwoSpaceDuhamelContract.IsMildSolutionOn.concat
#print axioms MNS2.IsR3EndpointSafeProjectedMildSolutionOn.concat
#print axioms MNS2.r3MildSmallnessThreshold_antitone
#print axioms MNS2.r3MildLifespan_antitone
#print axioms MNS2.r3EndpointSafeProjected_exists_extension_of_bounded
#print axioms MNS2.r3MildHorizons_nonempty
#print axioms MNS2.r3EndpointSafeProjected_horizons_unbounded_of_uniform_bound
#print axioms MNS2.r3EndpointSafeProjected_blowup_dichotomy
#print axioms MNS2.interval_integral_approximation_error_bound
#print axioms MNS2.radial_reduced_bridge_error_bound
#print axioms MNS2.radial_reduced_endpoint_error_bound_of_zero_fixed
#print axioms MNS2.intervalIntegral_finiteRankPath
#print axioms MNS2.radial_finiteRank_bridge_error_bound
#print axioms MNS2.radial_finiteRank_endpoint_error_bound_of_zero_fixed

-- Coordinate incompressibility semantics (Clay semantic-promotion edge 1, distributional
-- half): a Fourier-side solenoidal L² velocity represents a physical tempered distribution
-- whose physical-coordinate divergence (the sum of the distributional coordinate partial
-- derivatives of its components) vanishes; no phantom Sobolev order consumed.
#print axioms MNS2.r3TemperedDivergence_apply
#print axioms MNS2.r3TemperedDivergence_eq_zero_of_mem_solenoidal

-- Coordinate incompressibility semantics, classical half (Clay semantic-promotion edge 1b):
-- the explicit inverse-Fourier-integral physical representative is C^1 under explicit
-- frequency-side L^1 hypotheses, differentiable everywhere with an explicit derivative,
-- and its classical divergence vanishes at every point for solenoidal data; hypotheses
-- witnessed non-vacuous by Schwartz profiles.
#print axioms MNS2.contDiff_one_r3PhysicalRepresentative
#print axioms MNS2.hasFDerivAt_r3PhysicalRepresentative
#print axioms MNS2.r3RepresentativeDeriv_div_eq_zero
#print axioms MNS2.r3ClassicalDivergence_r3PhysicalRepresentative
#print axioms MNS2.r3PhysicalRepresentative_incompressible_of_mem_solenoidal
#print axioms MNS2.r3PhysicalRepresentative_hypotheses_nonvacuous

-- Bessel decoder -> edge-1b frequency hypotheses (Clay semantic edge 3a): the decoded
-- frequency data of an H^3 Bessel coordinate satisfies both explicit L^1 hypotheses of
-- edge 1b (Cauchy-Schwarz against the order-three inverse Bessel weight in dimension
-- three), is a.e. the Fourier transform of the L^2-level physical decode, coordinate
-- solenoidality transfers to the decode, and the capstone discharges every edge-1b
-- hypothesis from the decoder.
#print axioms MNS2.integrable_r3DecodedFrequency
#print axioms MNS2.integrable_weighted_r3DecodedFrequency
#print axioms MNS2.r3DecodedFrequency_ae_coeFn_fourier
#print axioms MNS2.r3Decoded3PhysicalVelocity_mem_solenoidal
#print axioms MNS2.r3DecodedFrequency_incompressible
#print axioms MNS2.r3L2ToTempered_r3Decoded3PhysicalVelocity
#print axioms MNS2.r3DecodedFrequency_incompressible_leray

-- Inversion consistency (Clay semantic edge 3b): the pointwise inverse-Fourier-integral
-- representative of the decoded frequency data agrees a.e. with the L^2-level decode
-- (Schwartz pairing on both sides + a.e. uniqueness against smooth compactly supported
-- test functions; no general L^1-cap-L^2 inversion library).
#print axioms MNS2.integral_smul_r3PhysicalRepresentative
#print axioms MNS2.integral_smul_r3Decoded3PhysicalVelocity
#print axioms MNS2.r3PhysicalRepresentative_ae_r3Decoded3PhysicalVelocity
#print axioms MNS2.r3DecodedFrequency_incompressible_ae_decoder

-- Generic Helmholtz pressure reconstruction (Clay semantic edge 2a): for every L^2
-- source, the explicit pressure tempered distribution (inverse Fourier transform of the
-- low/high split of the divergence-over-|xi|^2 profile) satisfies grad p = -(I-P)F
-- componentwise in Schwartz'; supporting integrability and frequency-realization facts.
#print axioms MNS2.integrable_r3PressureFrequencyLow
#print axioms MNS2.memLp_two_r3PressureFrequencyHigh
#print axioms MNS2.fourier_r3LerayComplementL2_ae
#print axioms MNS2.r3HelmholtzPressure_gradient
#print axioms MNS2.exists_r3LerayComplementL2_ne_zero

-- General H^3 convection source identification (Clay semantic edge 2b-i): the genuine
-- J^-2 decode of the completed coordinate convection operator equals, for all order-three
-- coordinates, the pointwise convection (U.grad)V of the decoded physical representatives
-- built from the explicit derivative; projected corollary P((U.grad)V); quantitative
-- Cauchy-Schwarz decoder L^1 bound; generic L^1-cap-L^2 inversion consistency; and the
-- edge-2a pressure gradient instantiated at the identified convection source.
#print axioms MNS2.integral_norm_r3DecodedFrequency_le
#print axioms MNS2.r3PhysicalRepresentative_ae_fourierInv
#print axioms MNS2.r3DecodedDerivativeL2Operator_ae_deriv
#print axioms MNS2.r3DecodedConvectionL2_schwartz
#print axioms MNS2.r3H2ToL2Operator_r3ConvectionH3ToH2
#print axioms MNS2.r3H2ToL2Operator_r3ProjectedConvectionH3ToH2
#print axioms MNS2.r3HelmholtzPressure_gradient_decodedConvection
#print axioms MNS2.exists_r3DecodedConvectionL2_ne_zero
#print axioms MNS2.exists_r3ConvectionH3ToH2_ne_zero
