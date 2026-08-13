import Mathlib
import Mathlib.Analysis.Calculus.ParametricIntegral
import Formal.QuadraticMildFixedPointDerivative

namespace MNS2

open Set MeasureTheory Filter Metric
open scoped Interval Topology

noncomputable section

section QuadraticMildTangentRealization

variable {V : Type*}
variable [NormedAddCommGroup V] [NormedSpace ℝ V] [CompleteSpace V]

/--
The local dominated-differentiation data needed at one endpoint time for the
quadratic Duhamel term.  This packages, without weakening, the analytic hypotheses
used by `quadraticDuhamelIntegral_hasFDerivAt_of_dominated`.

It is deliberately time-local: in a PDE application the neighborhood and majorant
may depend on the endpoint time.
-/
structure QuadraticDuhamelDerivativeCertificateAt
    (H : ℝ → V →L[ℝ] V)
    (Q : V →L[ℝ] V →L[ℝ] V)
    (t : ℝ) (U : V → ℝ → V) (x₀ : V)
    (J : ℝ → V →L[ℝ] V) where
  N : Set V
  hN : N ∈ 𝓝 x₀
  bound : ℝ → ℝ
  hF_meas : ∀ᶠ x in 𝓝 x₀,
    AEStronglyMeasurable
      (fun s : ℝ => quadraticDuhamelIntegrand H Q t U x s)
      (volume.restrict (Ι (0 : ℝ) t))
  hF_int : IntervalIntegrable
    (fun s : ℝ => quadraticDuhamelIntegrand H Q t U x₀ s)
    volume 0 t
  hF'_meas : AEStronglyMeasurable
    (quadraticDuhamelDerivativeIntegrand H Q t U x₀ J)
    (volume.restrict (Ι (0 : ℝ) t))
  h_lip : ∀ᵐ s ∂volume.restrict (Ι (0 : ℝ) t),
    LipschitzOnWith (Real.nnabs (bound s))
      (fun x : V => quadraticDuhamelIntegrand H Q t U x s) N
  hbound : IntervalIntegrable bound volume 0 t
  hUdiff : ∀ᵐ s ∂volume.restrict (Ι (0 : ℝ) t),
    HasFDerivAt (fun x : V => U x s) (J s) x₀

/--
Evaluation of the operator-valued quadratic mild RHS derivative in a direction `h`
is exactly the vector-valued linearized Duhamel RHS.  The only hypothesis needed is
interval integrability of the operator-valued derivative integrand.
-/
theorem quadraticMildRHSDerivativeAtTime_apply_eq_linearized
    (H : ℝ → V →L[ℝ] V)
    (Q : V →L[ℝ] V →L[ℝ] V)
    (t : ℝ) (U : V → ℝ → V) (x₀ : V)
    (J : ℝ → V →L[ℝ] V)
    (hint : IntervalIntegrable
      (quadraticDuhamelDerivativeIntegrand H Q t U x₀ J)
      volume 0 t)
    (h : V) :
    (quadraticMildRHSDerivativeAtTime H Q t U x₀ J) h =
      H t h -
        ∫ s in (0 : ℝ)..t,
          H (t - s) (quadraticDerivative Q (U x₀ s) ((J s) h)) := by
  change
    H t h -
        (∫ s in (0 : ℝ)..t,
          quadraticDuhamelDerivativeIntegrand H Q t U x₀ J s) h =
      H t h -
        ∫ s in (0 : ℝ)..t,
          H (t - s) (quadraticDerivative Q (U x₀ s) ((J s) h))
  rw [ContinuousLinearMap.intervalIntegral_apply hint h]
  rfl

/--
At one endpoint time, the dominated fixed-point derivative theorem from the previous
layer yields the actual directional linearized mild equation, together with the
required interval integrability of its vector-valued integrand.
-/
theorem quadraticMild_fixedPoint_direction_equation_of_certificate
    (H : ℝ → V →L[ℝ] V)
    (Q : V →L[ℝ] V →L[ℝ] V)
    (t : ℝ) (U : V → ℝ → V) (x₀ : V)
    (J : ℝ → V →L[ℝ] V)
    (C : QuadraticDuhamelDerivativeCertificateAt H Q t U x₀ J)
    (hUdiff_t : HasFDerivAt (fun x : V => U x t) (J t) x₀)
    (hfixed : ∀ x : V,
      U x t = quadraticMildRHSAtTime H Q t U x)
    (h : V) :
    IntervalIntegrable
      (fun s : ℝ =>
        H (t - s) (quadraticDerivative Q (U x₀ s) ((J s) h)))
      volume 0 t ∧
    (J t) h =
      H t h -
        ∫ s in (0 : ℝ)..t,
          H (t - s) (quadraticDerivative Q (U x₀ s) ((J s) h)) := by
  have hdiff := quadraticDuhamelIntegral_hasFDerivAt_of_dominated
    H Q t U x₀ J C.N C.hN C.bound
    C.hF_meas C.hF_int C.hF'_meas C.h_lip C.hbound C.hUdiff
  have hint : IntervalIntegrable
      (quadraticDuhamelDerivativeIntegrand H Q t U x₀ J)
      volume 0 t := hdiff.1
  have happ : IntervalIntegrable
      (fun s : ℝ =>
        (quadraticDuhamelDerivativeIntegrand H Q t U x₀ J s) h)
      volume 0 t := by
    constructor
    · exact (ContinuousLinearMap.apply ℝ V h).integrable_comp hint.1
    · exact (ContinuousLinearMap.apply ℝ V h).integrable_comp hint.2
  constructor
  · simpa [quadraticDuhamelDerivativeIntegrand] using happ
  · calc
      (J t) h =
          (quadraticMildRHSDerivativeAtTime H Q t U x₀ J) h :=
        quadraticMild_fixedPoint_fderiv_apply_eq_of_dominated
          H Q t U x₀ J C.N C.hN C.bound
          C.hF_meas C.hF_int C.hF'_meas C.h_lip C.hbound C.hUdiff
          hUdiff_t hfixed h
      _ = H t h -
          ∫ s in (0 : ℝ)..t,
            H (t - s) (quadraticDerivative Q (U x₀ s) ((J s) h)) :=
        quadraticMildRHSDerivativeAtTime_apply_eq_linearized
          H Q t U x₀ J hint h

/--
A differentiable quadratic mild fixed-point family realizes the existential tangent
semantics once the dominated-differentiation certificate is available at every time on
the horizon and the directional derivative trajectory has the expected continuity and
initial value.

This is the missing semantic-witness step: the conclusion is an actual
`QuadraticMildTangentEvolvesAt`, not merely an operator identity at the endpoint.
No uniqueness of the base or tangent trajectory is assumed.
-/
theorem quadraticMildTangentEvolvesAt_of_dominated_fixedPoint_family
    (H : ℝ → V →L[ℝ] V)
    (Q : V →L[ℝ] V →L[ℝ] V)
    (T : ℝ) (U : V → ℝ → V) (x₀ : V)
    (J : ℝ → V →L[ℝ] V) (h : V)
    (hbase :
      (MildEvolutionKernel.ofQuadratic H Q).IsMildSolutionOn T x₀ (U x₀))
    (hcont : ContinuousOn (fun t : ℝ => (J t) h) (Icc (0 : ℝ) T))
    (hinit : (J 0) h = h)
    (hcert : ∀ t ∈ Icc (0 : ℝ) T,
      QuadraticDuhamelDerivativeCertificateAt H Q t U x₀ J)
    (hUdiff : ∀ t ∈ Icc (0 : ℝ) T,
      HasFDerivAt (fun x : V => U x t) (J t) x₀)
    (hfixed : ∀ t ∈ Icc (0 : ℝ) T, ∀ x : V,
      U x t = quadraticMildRHSAtTime H Q t U x) :
    QuadraticMildTangentEvolvesAt H Q T x₀ h ((J T) h) := by
  refine ⟨U x₀, (fun t : ℝ => (J t) h), ?_, rfl⟩
  constructor
  · exact hbase
  · refine ⟨hbase.1, hcont, hinit, ?_⟩
    intro t ht
    exact quadraticMild_fixedPoint_direction_equation_of_certificate
      H Q t U x₀ J (hcert t ht) (hUdiff t ht) (hfixed t ht) h

end QuadraticMildTangentRealization

end

end MNS2
