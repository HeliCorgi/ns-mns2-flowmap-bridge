import Formal.R3NormalizedDivergenceFrequency
import Formal.R3SobolevCarrier

namespace MNS2

open MeasureTheory FourierTransform
open scoped FourierTransform

noncomputable section

def r3NormalizedDivergenceL2OperatorAux :
    R3L2Velocity →L[ℂ] R3L2ScalarAux :=
  r3NormalizedDivergenceFrequencyAux ∘L fourierCLM ℂ R3L2Velocity

theorem r3NormalizedDivergenceL2OperatorAux_ae (f : R3L2Velocity) :
    r3NormalizedDivergenceL2OperatorAux f =ᵐ[volume]
      fun ξ => r3NormalizedDivergencePointwise ξ ((𝓕 f) ξ) := by
  change r3NormalizedDivergenceFrequencyAux (𝓕 f) =ᵐ[volume]
    fun ξ => r3NormalizedDivergencePointwise ξ ((𝓕 f) ξ)
  exact r3NormalizedDivergenceFrequencyAux_ae (𝓕 f)

def r3L2SolenoidalSubmodule : Submodule ℂ R3L2Velocity :=
  r3NormalizedDivergenceL2OperatorAux.ker

abbrev R3HsSolenoidalVelocity (_s : ℝ) := ↥r3L2SolenoidalSubmodule
abbrev R3HmSolenoidalVelocity (m : ℕ) := R3HsSolenoidalVelocity (m : ℝ)

theorem r3HsSolenoidalVelocity_complete (s : ℝ) :
    CompleteSpace (R3HsSolenoidalVelocity s) := by
  change CompleteSpace r3NormalizedDivergenceL2OperatorAux.ker
  infer_instance

@[simp]
theorem mem_r3L2SolenoidalSubmodule_iff (f : R3L2Velocity) :
    f ∈ r3L2SolenoidalSubmodule ↔ r3NormalizedDivergenceL2OperatorAux f = 0 := by
  simp [r3L2SolenoidalSubmodule]

end

end MNS2
