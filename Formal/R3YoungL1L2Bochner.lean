import Mathlib.MeasureTheory.Function.LpSpace.DomAct.Continuous
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Formal.R3H2WeightedConvolutionKernel

namespace MNS2

open MeasureTheory

noncomputable section

/-- Translation of an `R³` `L²` velocity field by `y`, represented inside the domain-action API.
The sign is chosen so that the underlying representative is `x ↦ g (x - y)`. -/
def r3L2Translate (y : R3) (g : R3L2Velocity) : R3L2Velocity :=
  DomAddAct.mk (-y) +ᵥ g

@[simp]
theorem norm_r3L2Translate (y : R3) (g : R3L2Velocity) :
    ‖r3L2Translate y g‖ = ‖g‖ := by
  simp [r3L2Translate]

/-- The `L²` translation orbit is continuous in the translation parameter. -/
theorem continuous_r3L2Translate (g : R3L2Velocity) :
    Continuous (fun y : R3 => r3L2Translate y g) := by
  unfold r3L2Translate
  have hneg : Continuous (fun y : R3 => -y) := continuous_neg
  have hmk : Continuous (fun y : R3 => DomAddAct.mk (-y)) :=
    DomAddAct.continuous_mk.comp hneg
  exact hmk.vadd continuous_const

/--
The `L²`-valued Young integrand `f(y) τ_y g`, with `τ_y g(x) = g(x-y)`.

For the current Navier--Stokes application the scalar factor will be one weighted Fourier
coordinate and the vector factor one weighted Fourier velocity field.
-/
def r3YoungL2Integrand
    (f : R3SchwartzScalar) (g : R3L2Velocity) (y : R3) : R3L2Velocity :=
  f y • r3L2Translate y g

@[simp]
theorem norm_r3YoungL2Integrand
    (f : R3SchwartzScalar) (g : R3L2Velocity) (y : R3) :
    ‖r3YoungL2Integrand f g y‖ = ‖f y‖ * ‖g‖ := by
  simp [r3YoungL2Integrand, norm_smul]

/-- The `L²`-valued Young integrand is continuous, hence strongly measurable. -/
theorem continuous_r3YoungL2Integrand
    (f : R3SchwartzScalar) (g : R3L2Velocity) :
    Continuous (fun y : R3 => r3YoungL2Integrand f g y) := by
  unfold r3YoungL2Integrand
  have hf : Continuous (fun y : R3 => f y) := f.continuous
  have hg : Continuous (fun y : R3 => r3L2Translate y g) :=
    continuous_r3L2Translate g
  exact hf.smul hg

/-- The `L²`-valued Young integrand is Bochner integrable for a Schwartz scalar input. -/
theorem integrable_r3YoungL2Integrand
    (f : R3SchwartzScalar) (g : R3L2Velocity) :
    Integrable (fun y : R3 => r3YoungL2Integrand f g y) := by
  have hmajor : Integrable (fun y : R3 => ‖f y‖ * ‖g‖) :=
    (Integrable.norm f.integrable).mul_const ‖g‖
  exact hmajor.mono'
    (continuous_r3YoungL2Integrand f g).aestronglyMeasurable
    (Filter.Eventually.of_forall fun y => by
      rw [norm_r3YoungL2Integrand])

/--
The `L²`-valued convolution obtained as a Bochner integral of translated `L²` fields.

This construction avoids choosing pointwise representatives of the `L²` input.  A later bridge can
identify it with the ordinary convolution when the second input is also Schwartz.
-/
def r3YoungConvolutionL2
    (f : R3SchwartzScalar) (g : R3L2Velocity) : R3L2Velocity :=
  ∫ y : R3, r3YoungL2Integrand f g y

/--
Young's `L¹ * L² → L²` estimate for the Bochner convolution with a Schwartz scalar factor.
The first factor on the right is exactly the physical `L¹` norm of the scalar Schwartz function.
-/
theorem norm_r3YoungConvolutionL2_le
    (f : R3SchwartzScalar) (g : R3L2Velocity) :
    ‖r3YoungConvolutionL2 f g‖ ≤ (∫ y : R3, ‖f y‖) * ‖g‖ := by
  calc
    ‖r3YoungConvolutionL2 f g‖ =
        ‖∫ y : R3, r3YoungL2Integrand f g y‖ := by
      rfl
    _ ≤ ∫ y : R3, ‖r3YoungL2Integrand f g y‖ :=
      norm_integral_le_integral_norm _
    _ = ∫ y : R3, ‖f y‖ * ‖g‖ := by
      apply integral_congr_ae
      exact Filter.Eventually.of_forall fun y =>
        norm_r3YoungL2Integrand f g y
    _ = (∫ y : R3, ‖f y‖) * ‖g‖ := by
      rw [integral_mul_const]

end

end MNS2
