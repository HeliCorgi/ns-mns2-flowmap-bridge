import Mathlib.MeasureTheory.Function.L2Space
import Mathlib.MeasureTheory.Integral.Prod
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

/--
The same finite-set identity with an explicitly supplied pointwise representative of the `L²`
factor.  Translation preserves null sets, so an a.e. representative identity for `g` may be
transported through every physical translate `x ↦ x-y`.
-/
theorem setIntegral_r3RealYoungL1L2Convolution_eq_iterated_of_ae
    {f : R3 → ℝ} (hf : Continuous f) (hfi : Integrable f)
    (g : R3L2RealScalar) {g₀ : R3 → ℝ}
    (hg : (g : R3 → ℝ) =ᵐ[(volume : Measure R3)] g₀)
    {s : Set R3} (hs : MeasurableSet s)
    (hμs : (volume : Measure R3) s ≠ ∞) :
    (∫ x in s, (r3RealYoungL1L2Convolution f g) x) =
      ∫ y : R3, ∫ x in s, f y * g₀ (x - y) := by
  rw [setIntegral_r3RealYoungL1L2Convolution_eq_iterated hf hfi g hs hμs]
  apply integral_congr_ae
  filter_upwards with y
  have hshift :
      (fun x : R3 => g (x - y)) =ᵐ[(volume : Measure R3)]
        (fun x : R3 => g₀ (x - y)) := by
    simpa [r3TranslationMap, Function.comp_def] using
      (measurePreserving_r3TranslationMap y).quasiMeasurePreserving.ae_eq hg
  exact setIntegral_congr_ae hs
    (hshift.mono fun x hx _ => by rw [hx])

/--
On a finite-measure output set, an integrable scalar factor times a continuous uniformly bounded
translated kernel is integrable on the product space.  This is the exact Fubini hypothesis needed
for the concrete Schwartz norm fields used later.
-/
theorem integrable_r3RealYoungKernel_restrict_prod
    {f : R3 → ℝ} (hfi : Integrable f)
    {g₀ : R3 → ℝ} (hg₀ : Continuous g₀)
    (C : ℝ) (hC : ∀ x : R3, ‖g₀ x‖ ≤ C)
    {s : Set R3} (hs : MeasurableSet s)
    (hμs : (volume : Measure R3) s ≠ ∞) :
    Integrable
      (fun z : R3 × R3 => f z.2 * g₀ (z.1 - z.2))
      (((volume : Measure R3).restrict s).prod (volume : Measure R3)) := by
  have hμ_restrict_univ :
      ((volume : Measure R3).restrict s) Set.univ < ∞ := by
    simpa only [Set.univ_inter, MeasurableSet.univ, Measure.restrict_apply,
      lt_top_iff_ne_top] using hμs
  letI : IsFiniteMeasure ((volume : Measure R3).restrict s) :=
    ⟨hμ_restrict_univ⟩
  have hbase :
      Integrable (fun z : R3 × R3 => f z.2)
        (((volume : Measure R3).restrict s).prod (volume : Measure R3)) :=
    hfi.comp_snd ((volume : Measure R3).restrict s)
  have hkernelMeas :
      AEStronglyMeasurable (fun z : R3 × R3 => g₀ (z.1 - z.2))
        (((volume : Measure R3).restrict s).prod (volume : Measure R3)) :=
    (hg₀.comp (continuous_fst.sub continuous_snd)).aestronglyMeasurable
  have hkernelBound :
      ∀ᵐ z : R3 × R3 ∂(((volume : Measure R3).restrict s).prod (volume : Measure R3)),
        ‖g₀ (z.1 - z.2)‖ ≤ C :=
    Filter.Eventually.of_forall fun z => hC (z.1 - z.2)
  exact hbase.mul_bdd hkernelMeas hkernelBound

/--
Fubini swap for the bounded concrete representative used in the real Young bridge.
-/
theorem integral_setIntegral_swap_r3RealYoungKernel
    {f : R3 → ℝ} (hfi : Integrable f)
    {g₀ : R3 → ℝ} (hg₀ : Continuous g₀)
    (C : ℝ) (hC : ∀ x : R3, ‖g₀ x‖ ≤ C)
    {s : Set R3} (hs : MeasurableSet s)
    (hμs : (volume : Measure R3) s ≠ ∞) :
    (∫ y : R3, ∫ x in s, f y * g₀ (x - y)) =
      ∫ x in s, ∫ y : R3, f y * g₀ (x - y) := by
  have hprod :=
    integrable_r3RealYoungKernel_restrict_prod hfi hg₀ C hC hs hμs
  simpa [Function.uncurry] using
    (integral_integral_swap hprod).symm

/--
Finite-set integrals of the bundled Young convolution equal finite-set integrals of the literal
pointwise convolution whenever the chosen `L²` representative is continuous and uniformly bounded.
This is the form needed by the later a.e.-uniqueness step.
-/
theorem setIntegral_r3RealYoungL1L2Convolution_eq_pointwise_of_ae_of_bound
    {f : R3 → ℝ} (hf : Continuous f) (hfi : Integrable f)
    (g : R3L2RealScalar) {g₀ : R3 → ℝ}
    (hg : (g : R3 → ℝ) =ᵐ[(volume : Measure R3)] g₀)
    (hg₀ : Continuous g₀) (C : ℝ) (hC : ∀ x : R3, ‖g₀ x‖ ≤ C)
    {s : Set R3} (hs : MeasurableSet s)
    (hμs : (volume : Measure R3) s ≠ ∞) :
    (∫ x in s, (r3RealYoungL1L2Convolution f g) x) =
      ∫ x in s, ∫ y : R3, f y * g₀ (x - y) := by
  calc
    (∫ x in s, (r3RealYoungL1L2Convolution f g) x) =
        ∫ y : R3, ∫ x in s, f y * g₀ (x - y) :=
      setIntegral_r3RealYoungL1L2Convolution_eq_iterated_of_ae
        hf hfi g hg hs hμs
    _ = ∫ x in s, ∫ y : R3, f y * g₀ (x - y) :=
      integral_setIntegral_swap_r3RealYoungKernel hfi hg₀ C hC hs hμs

end

end MNS2
