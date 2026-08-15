import Mathlib.MeasureTheory.Function.L2Space
import Formal.R3YoungRealL1L2Bochner

namespace MNS2

open MeasureTheory
open scoped InnerProductSpace

noncomputable section

/--
The `L²` translation used by the real Young construction has the expected translated
representative almost everywhere.
-/
theorem coeFn_r3L2RealTranslate
    (y : R3) (g : R3L2RealScalar) :
    (r3L2RealTranslate y g : R3 → ℝ) =ᵐ[(volume : Measure R3)]
      (fun x : R3 => g (x - y)) := by
  simpa [r3L2RealTranslate, r3TranslationMap, Function.comp_def] using
    (Lp.coeFn_compMeasurePreserving g (measurePreserving_r3TranslationMap y))

/--
The bundled real Young integrand represents the literal scalar product
`f(y) * g(x-y)` almost everywhere in the output variable.
-/
theorem coeFn_r3RealYoungL1L2Integrand
    (f : R3 → ℝ) (g : R3L2RealScalar) (y : R3) :
    (r3RealYoungL1L2Integrand f g y : R3 → ℝ) =ᵐ[(volume : Measure R3)]
      (fun x : R3 => f y * g (x - y)) := by
  filter_upwards
    [Lp.coeFn_smul (f y) (r3L2RealTranslate y g),
      coeFn_r3L2RealTranslate y g]
    with x hsmul htranslate
  change (f y • r3L2RealTranslate y g : R3L2RealScalar) x = f y * g (x - y)
  rw [hsmul]
  simp [Pi.smul_apply, htranslate]

/--
Finite-set integrals of the bundled `L¹ * L²` Young convolution can be unfolded into the
corresponding iterated scalar integral.

This deliberately stops before swapping the two scalar integrals.  That Fubini step, together
with a concrete representative for the `L²` factor, is the next bridge needed to identify the
bundled Young convolution with the ordinary pointwise convolution almost everywhere.
-/
theorem setIntegral_r3RealYoungL1L2Convolution_eq_iterated
    {f : R3 → ℝ} (hf : Continuous f) (hfi : Integrable f)
    (g : R3L2RealScalar) {s : Set R3}
    (hs : MeasurableSet s) (hμs : (volume : Measure R3) s ≠ ∞) :
    (∫ x in s, (r3RealYoungL1L2Convolution f g) x) =
      ∫ y : R3, ∫ x in s, f y * g (x - y) := by
  let χ : R3L2RealScalar := indicatorConstLp 2 hs hμs (1 : ℝ)
  have hI : Integrable (fun y : R3 => r3RealYoungL1L2Integrand f g y) :=
    integrable_r3RealYoungL1L2Integrand hf hfi g
  calc
    (∫ x in s, (r3RealYoungL1L2Convolution f g) x) =
        inner ℝ χ (r3RealYoungL1L2Convolution f g) := by
      symm
      simpa [χ] using
        (L2.inner_indicatorConstLp_one hs hμs (r3RealYoungL1L2Convolution f g))
    _ = ∫ y : R3, inner ℝ χ (r3RealYoungL1L2Integrand f g y) := by
      simpa [r3RealYoungL1L2Convolution] using (integral_inner hI χ).symm
    _ = ∫ y : R3, ∫ x in s, (r3RealYoungL1L2Integrand f g y) x := by
      apply integral_congr_ae
      filter_upwards with y
      simpa [χ] using
        (L2.inner_indicatorConstLp_one hs hμs (r3RealYoungL1L2Integrand f g y))
    _ = ∫ y : R3, ∫ x in s, f y * g (x - y) := by
      apply integral_congr_ae
      filter_upwards with y
      exact setIntegral_congr_ae hs
        ((coeFn_r3RealYoungL1L2Integrand f g y).mono fun x hx _ => hx)

end

end MNS2
