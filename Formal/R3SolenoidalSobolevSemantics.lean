import Formal.R3SolenoidalCarrierCompleteness
import Formal.R3SobolevCarrier

namespace MNS2

open MeasureTheory

noncomputable section

/-- Decode a solenoidal Bessel coordinate as the same tempered distribution used by `R3HsVelocity`. -/
def r3HsSolenoidalToTempered (s : ℝ) (u : R3HsSolenoidalVelocity s) :
    SchwartzMap.VectorTemperedDistribution 3 :=
  r3HsToTempered s u.1

/-- Every solenoidal Bessel coordinate represents an `H^s(R³; C³)` tempered distribution. -/
theorem r3HsSolenoidalToTempered_memSobolev (s : ℝ) (u : R3HsSolenoidalVelocity s) :
    (r3HsSolenoidalToTempered s u).MemSobolev s 2 := by
  exact r3HsToTempered_memSobolev s u.1

/-- Integer-order wrapper for the strong `H^m_σ` carrier. -/
theorem r3HmSolenoidalToTempered_memSobolev (m : ℕ) (u : R3HmSolenoidalVelocity m) :
    (r3HsSolenoidalToTempered (m : ℝ) u).MemSobolev (m : ℝ) 2 := by
  exact r3HsSolenoidalToTempered_memSobolev (m : ℝ) u

end

end MNS2
