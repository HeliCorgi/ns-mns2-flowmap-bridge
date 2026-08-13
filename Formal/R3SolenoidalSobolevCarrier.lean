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

theorem abs_r3_coordinate_le_scale (i : Fin 3) (ξ : R3) :
    |ξ i| ≤ r3FrequencyL1Scale ξ := by
  have hi : |ξ i| ≤ ∑ j : Fin 3, |ξ j| := by
    exact Finset.single_le_sum (fun j _ => abs_nonneg (ξ j)) (Finset.mem_univ i)
  unfold r3FrequencyL1Scale
  linarith

def r3NormalizedFrequencyCoordinate (i : Fin 3) (ξ : R3) : ℂ :=
  Complex.ofReal (ξ i / r3FrequencyL1Scale ξ)

theorem continuous_r3NormalizedFrequencyCoordinate (i : Fin 3) :
    Continuous (r3NormalizedFrequencyCoordinate i) := by
  unfold r3NormalizedFrequencyCoordinate
  apply Complex.continuous_ofReal.comp
  exact (continuous_apply i).div continuous_r3FrequencyL1Scale
    (fun ξ => ne_of_gt (r3FrequencyL1Scale_pos ξ))

theorem norm_r3NormalizedFrequencyCoordinate_le_one (i : Fin 3) (ξ : R3) :
    ‖r3NormalizedFrequencyCoordinate i ξ‖ ≤ 1 := by
  rw [r3NormalizedFrequencyCoordinate, Complex.norm_real, Real.norm_eq_abs,
    abs_div, abs_of_pos (r3FrequencyL1Scale_pos ξ)]
  exact (div_le_one (r3FrequencyL1Scale_pos ξ)).2 (abs_r3_coordinate_le_scale i ξ)

def r3NormalizedFrequencyCoordinateLpTop (i : Fin 3) :
    Lp ℂ ⊤ (volume : Measure R3) :=
  (memLp_top_of_bound
      (continuous_r3NormalizedFrequencyCoordinate i).aestronglyMeasurable
      1
      (ae_of_all _ fun ξ => norm_r3NormalizedFrequencyCoordinate_le_one i ξ)).toLp
    (r3NormalizedFrequencyCoordinate i)

theorem r3NormalizedFrequencyCoordinateLpTop_ae (i : Fin 3) :
    r3NormalizedFrequencyCoordinateLpTop i =ᵐ[volume]
      r3NormalizedFrequencyCoordinate i := by
  unfold r3NormalizedFrequencyCoordinateLpTop
  exact MemLp.coeFn_toLp _

end

end MNS2
