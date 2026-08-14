import Formal.R3SchwartzSobolevCore

namespace MNS2

open MeasureTheory FourierTransform

noncomputable section

/-- The explicit frequency-side Bessel coordinate carried by a Schwartz velocity field. -/
def r3SchwartzSobolevFrequencyCoordinate
    (s : ℝ) (f : R3SchwartzVelocity) : R3SchwartzVelocity :=
  SchwartzMap.smulLeftCLM R3C
    (fun ξ : R3 => Complex.ofReal ((1 + ‖ξ‖ ^ 2) ^ (s / 2))) (𝓕 f)

/-- Fourier transform of the physical Bessel coordinate is the explicit weighted frequency field. -/
theorem fourier_r3SchwartzBesselCoordinate
    (s : ℝ) (f : R3SchwartzVelocity) :
    𝓕 (SchwartzMap.fourierMultiplierCLM R3C
      (fun ξ : R3 => Complex.ofReal ((1 + ‖ξ‖ ^ 2) ^ (s / 2))) f) =
      r3SchwartzSobolevFrequencyCoordinate s f := by
  simp [r3SchwartzSobolevFrequencyCoordinate,
    SchwartzMap.fourierMultiplierCLM_apply]

/-- Plancherel identifies the stored `H^s` coordinate norm with the weighted Fourier `L²` norm. -/
theorem norm_r3SchwartzToHsCLM_eq_frequencyCoordinate
    (s : ℝ) (f : R3SchwartzVelocity) :
    ‖r3SchwartzToHsCLM s f‖ =
      ‖(r3SchwartzSobolevFrequencyCoordinate s f).toLp 2 (volume : Measure R3)‖ := by
  rw [r3SchwartzToHsCLM_apply]
  calc
    ‖(SchwartzMap.fourierMultiplierCLM R3C
        (fun ξ : R3 => Complex.ofReal ((1 + ‖ξ‖ ^ 2) ^ (s / 2))) f).toLp 2‖ =
        ‖𝓕 ((SchwartzMap.fourierMultiplierCLM R3C
          (fun ξ : R3 => Complex.ofReal ((1 + ‖ξ‖ ^ 2) ^ (s / 2))) f).toLp 2)‖ := by
      symm
      exact Lp.norm_fourier_eq _
    _ = ‖(𝓕 (SchwartzMap.fourierMultiplierCLM R3C
          (fun ξ : R3 => Complex.ofReal ((1 + ‖ξ‖ ^ 2) ^ (s / 2))) f)).toLp 2‖ := by
      rw [SchwartzMap.toLp_fourier_eq]
    _ = ‖(r3SchwartzSobolevFrequencyCoordinate s f).toLp 2‖ := by
      rw [fourier_r3SchwartzBesselCoordinate]

/-- The order-two Bessel weight is pointwise dominated by the order-three Bessel weight. -/
theorem norm_r3SobolevWeight_two_le_three (ξ : R3) :
    ‖Complex.ofReal ((1 + ‖ξ‖ ^ 2) ^ ((2 : ℝ) / 2))‖ ≤
      ‖Complex.ofReal ((1 + ‖ξ‖ ^ 2) ^ ((3 : ℝ) / 2))‖ := by
  have hbase : 1 ≤ 1 + ‖ξ‖ ^ 2 := by
    nlinarith [sq_nonneg ‖ξ‖]
  have hrpow :
      (1 + ‖ξ‖ ^ 2) ^ ((2 : ℝ) / 2) ≤
        (1 + ‖ξ‖ ^ 2) ^ ((3 : ℝ) / 2) := by
    exact Real.rpow_le_rpow_of_exponent_le hbase (by norm_num)
  simpa [Real.norm_of_nonneg (by positivity)] using hrpow

/-- Pointwise domination of the weighted Fourier representatives at orders two and three. -/
theorem norm_r3SchwartzSobolevFrequencyCoordinate_two_le_three
    (f : R3SchwartzVelocity) (ξ : R3) :
    ‖r3SchwartzSobolevFrequencyCoordinate 2 f ξ‖ ≤
      ‖r3SchwartzSobolevFrequencyCoordinate 3 f ξ‖ := by
  simp only [r3SchwartzSobolevFrequencyCoordinate, SchwartzMap.smulLeftCLM_apply,
    norm_smul]
  exact mul_le_mul_of_nonneg_right (norm_r3SobolevWeight_two_le_three ξ)
    (norm_nonneg (𝓕 f ξ))

/-- On the Schwartz core, the canonical `H²` coordinate norm is dominated by the `H³` norm. -/
theorem norm_r3SchwartzToHsCLM_two_le_three (f : R3SchwartzVelocity) :
    ‖r3SchwartzToHsCLM 2 f‖ ≤ ‖r3SchwartzToHsCLM 3 f‖ := by
  rw [norm_r3SchwartzToHsCLM_eq_frequencyCoordinate,
    norm_r3SchwartzToHsCLM_eq_frequencyCoordinate]
  apply Lp.norm_le_norm_of_ae_le
  filter_upwards [
    (r3SchwartzSobolevFrequencyCoordinate 2 f).coeFn_toLp 2 (volume : Measure R3),
    (r3SchwartzSobolevFrequencyCoordinate 3 f).coeFn_toLp 2 (volume : Measure R3)]
    with ξ h2 h3
  rw [h2, h3]
  exact norm_r3SchwartzSobolevFrequencyCoordinate_two_le_three f ξ

end

end MNS2
