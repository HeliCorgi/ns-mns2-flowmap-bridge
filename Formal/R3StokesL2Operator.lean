import Mathlib.Analysis.Fourier.LpSpace
import Mathlib.MeasureTheory.Function.Holder
import Formal.R3StokesFrequencySymbol

namespace MNS2

open MeasureTheory FourierTransform Filter
open scoped ENNReal FourierTransform

noncomputable section

/-- Complexified three-component velocity fiber used by the `L²(R³)` Fourier theory. -/
abbrev R3C := EuclideanSpace ℂ (Fin 3)

/--
The first concrete bundled function-space carrier for the physical `R³` formal PDE layer.

It is the complexified velocity space `L²(R³; ℂ³)`.  Complexification is used because mathlib's
Plancherel/Fourier `L²` equivalence is formulated over complex-valued target spaces.  No claim is
made here that this is already the final local-wellposedness carrier for Navier--Stokes.
-/
abbrev R3L2Velocity := Lp (α := R3) R3C 2 (volume : Measure R3)

/-- Complex form of the real scalar Stokes multiplier from `R3StokesFrequencySymbol`. -/
def r3StokesScalarComplex (ν t : ℝ) (ξ : R3) : ℂ :=
  Complex.ofReal (r3StokesScalar ν t ξ)

/-- The complex scalar Stokes multiplier is continuous in the physical frequency. -/
theorem continuous_r3StokesScalarComplex (ν t : ℝ) :
    Continuous (r3StokesScalarComplex ν t) := by
  unfold r3StokesScalarComplex r3StokesScalar r3StokesDecayRate
  fun_prop

/-- For nonnegative viscosity and forward time, the complex Stokes multiplier has norm at most one. -/
theorem norm_r3StokesScalarComplex_le_one
    {ν t : ℝ} (hν : 0 ≤ ν) (ht : 0 ≤ t) (ξ : R3) :
    ‖r3StokesScalarComplex ν t ξ‖ ≤ 1 := by
  rw [r3StokesScalarComplex, Complex.norm_real, Real.norm_eq_abs,
    abs_of_pos (r3StokesScalar_pos ν t ξ)]
  exact r3StokesScalar_le_one hν ht ξ

/--
The scalar Stokes multiplier bundled as an `L∞` function on frequency space.

The proof data `hν`, `ht` certify the uniform forward-time bound by one; they do not alter the
underlying multiplier function.
-/
def r3StokesScalarLpTop
    {ν t : ℝ} (hν : 0 ≤ ν) (ht : 0 ≤ t) :
    Lp ℂ ⊤ (volume : Measure R3) :=
  (memLp_top_of_bound
      (continuous_r3StokesScalarComplex ν t).aestronglyMeasurable
      1
      (ae_of_all _ fun ξ => norm_r3StokesScalarComplex_le_one hν ht ξ)).toLp
    (r3StokesScalarComplex ν t)

/-- The bundled `L∞` multiplier agrees almost everywhere with its pointwise formula. -/
theorem r3StokesScalarLpTop_ae
    {ν t : ℝ} (hν : 0 ≤ ν) (ht : 0 ≤ t) :
    r3StokesScalarLpTop hν ht =ᵐ[volume]
      r3StokesScalarComplex ν t := by
  unfold r3StokesScalarLpTop
  exact MemLp.coeFn_toLp _

/-- Scalar multiplication on the complex three-component velocity fiber as a continuous bilinear map. -/
def complexScalarActionR3C : ℂ →L[ℂ] R3C →L[ℂ] R3C :=
  ContinuousLinearMap.lsmul ℂ ℂ

/--
The Stokes multiplier acting on the bundled Fourier-side space `L²(R³; ℂ³)`.

This is the first step beyond frequency-fiber algebra: the pointwise scalar symbol is now a genuine
bounded continuous linear operator on a complete function space.
-/
def r3StokesL2FrequencyMultiplier
    {ν t : ℝ} (hν : 0 ≤ ν) (ht : 0 ≤ t) :
    R3L2Velocity →L[ℂ] R3L2Velocity := by
  let H :
      Lp ℂ (⊤ : ℝ≥0∞) (volume : Measure R3) →L[ℂ]
        Lp R3C (2 : ℝ≥0∞) (volume : Measure R3) →L[ℂ]
          Lp R3C (2 : ℝ≥0∞) (volume : Measure R3) :=
    complexScalarActionR3C.holderL
      (volume : Measure R3) (⊤ : ℝ≥0∞) (2 : ℝ≥0∞) (2 : ℝ≥0∞)
  exact H (r3StokesScalarLpTop hν ht)

/-- Exact almost-everywhere pointwise realization of the bundled Fourier-side Stokes multiplier. -/
theorem r3StokesL2FrequencyMultiplier_ae
    {ν t : ℝ} (hν : 0 ≤ ν) (ht : 0 ≤ t) (f : R3L2Velocity) :
    r3StokesL2FrequencyMultiplier hν ht f =ᵐ[volume]
      fun ξ => r3StokesScalarComplex ν t ξ • f ξ := by
  change
    complexScalarActionR3C.holder 2 (r3StokesScalarLpTop hν ht) f =ᵐ[volume]
      fun ξ => r3StokesScalarComplex ν t ξ • f ξ
  filter_upwards
    [complexScalarActionR3C.coeFn_holder (r3StokesScalarLpTop hν ht) f,
      r3StokesScalarLpTop_ae hν ht]
    with ξ hholder hscalar
  rw [hholder, hscalar]
  rfl

/--
The physical-space `L²(R³; ℂ³)` Stokes operator, defined by Fourier conjugation of the bounded
frequency multiplier.

Unlike `r3StokesFrequencySymbol`, this is a genuine function-space continuous linear map.
It still does not include the matrix-valued Leray multiplier or the nonlinear convection term.
-/
def r3StokesL2Operator
    {ν t : ℝ} (hν : 0 ≤ ν) (ht : 0 ≤ t) :
    R3L2Velocity →L[ℂ] R3L2Velocity :=
  fourierInvCLM ℂ R3L2Velocity ∘L
    r3StokesL2FrequencyMultiplier hν ht ∘L
      fourierCLM ℂ R3L2Velocity

/-- The function-space Stokes operator has exactly the intended Fourier multiplier realization. -/
theorem fourier_r3StokesL2Operator
    {ν t : ℝ} (hν : 0 ≤ ν) (ht : 0 ≤ t) (f : R3L2Velocity) :
    𝓕 (r3StokesL2Operator hν ht f) =
      r3StokesL2FrequencyMultiplier hν ht (𝓕 f) := by
  simp [r3StokesL2Operator]

/-- At time zero the bundled Fourier-side Stokes multiplier is the identity. -/
theorem r3StokesL2FrequencyMultiplier_zero_time
    {ν : ℝ} (hν : 0 ≤ ν) :
    r3StokesL2FrequencyMultiplier hν (le_refl 0) =
      ContinuousLinearMap.id ℂ R3L2Velocity := by
  ext f
  filter_upwards [r3StokesL2FrequencyMultiplier_ae hν (le_refl 0) f] with ξ hξ
  simpa [r3StokesScalarComplex, r3StokesScalar] using hξ

/-- At time zero the physical-space `L²` Stokes operator is the identity. -/
theorem r3StokesL2Operator_zero_time
    {ν : ℝ} (hν : 0 ≤ ν) :
    r3StokesL2Operator hν (le_refl 0) =
      ContinuousLinearMap.id ℂ R3L2Velocity := by
  ext f
  simp [r3StokesL2Operator, r3StokesL2FrequencyMultiplier_zero_time hν]

end

end MNS2