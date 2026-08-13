import Mathlib
import Mathlib.Analysis.Fourier.LpSpace
import Mathlib.MeasureTheory.Function.Holder
import Formal.R3SobolevCarrier

namespace MNS2

open MeasureTheory FourierTransform Filter
open scoped ENNReal FourierTransform

noncomputable section

abbrev R3L2Scalar := Lp (α := R3) ℂ 2 (volume : Measure R3)

def r3FrequencyL1Scale (ξ : R3) : ℝ :=
  1 + ∑ i : Fin 3, |ξ i|

theorem r3FrequencyL1Scale_pos (ξ : R3) : 0 < r3FrequencyL1Scale ξ := by
  unfold r3FrequencyL1Scale
  have hsum : 0 ≤ ∑ i : Fin 3, |ξ i| := by positivity
  linarith

theorem continuous_r3FrequencyL1Scale : Continuous r3FrequencyL1Scale := by
  unfold r3FrequencyL1Scale
  fun_prop

end

end MNS2
