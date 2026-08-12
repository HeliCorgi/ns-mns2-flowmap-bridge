import Mathlib
import Formal.MildZeroUniqueness

namespace MNS2

section QuadraticMildNonlinearity

variable {V : Type*}
variable [NormedAddCommGroup V] [NormedSpace ℝ V] [CompleteSpace V]

/-- The quadratic diagonal associated with a continuous bilinear map. -/
def ContinuousLinearMap.quadraticDiagonal
    (Q : V →L[ℝ] V →L[ℝ] V) (u : V) : V :=
  Q u u

/--
The Fréchet derivative candidate for `u ↦ Q u u`:

  v ↦ Q u v + Q v u.

It is written with mathlib's `precompR` / `precompL` continuous-linear-map
constructors so continuity of the derivative action is part of the object.
-/
def ContinuousLinearMap.quadraticDerivative
    (Q : V →L[ℝ] V →L[ℝ] V) (u : V) : V →L[ℝ] V :=
  Q.precompR V u (ContinuousLinearMap.id ℝ V) +
    Q.precompL V (ContinuousLinearMap.id ℝ V) u

@[simp]
theorem ContinuousLinearMap.quadraticDiagonal_zero
    (Q : V →L[ℝ] V →L[ℝ] V) :
    Q.quadraticDiagonal 0 = 0 := by
  simp [ContinuousLinearMap.quadraticDiagonal]

@[simp]
theorem ContinuousLinearMap.quadraticDerivative_apply
    (Q : V →L[ℝ] V →L[ℝ] V) (u v : V) :
    Q.quadraticDerivative u v = Q u v + Q v u := by
  simp [ContinuousLinearMap.quadraticDerivative]

@[simp]
theorem ContinuousLinearMap.quadraticDerivative_zero
    (Q : V →L[ℝ] V →L[ℝ] V) :
    Q.quadraticDerivative 0 = 0 := by
  ext v
  simp

/-- Exact Fréchet derivative of the diagonal quadratic map. -/
theorem ContinuousLinearMap.hasFDerivAt_quadraticDiagonal
    (Q : V →L[ℝ] V →L[ℝ] V) (u : V) :
    HasFDerivAt Q.quadraticDiagonal (Q.quadraticDerivative u) u := by
  simpa [ContinuousLinearMap.quadraticDiagonal, ContinuousLinearMap.quadraticDerivative] using
    (Q.hasFDerivAt_of_bilinear
      (hasFDerivAt_id (𝕜 := ℝ) u)
      (hasFDerivAt_id (𝕜 := ℝ) u))

/-- Canonical `fderiv` formula for the quadratic nonlinearity. -/
theorem ContinuousLinearMap.fderiv_quadraticDiagonal
    (Q : V →L[ℝ] V →L[ℝ] V) (u : V) :
    fderiv ℝ Q.quadraticDiagonal u = Q.quadraticDerivative u := by
  exact (Q.hasFDerivAt_quadraticDiagonal u).fderiv

/-- The quadratic diagonal is differentiable everywhere. -/
theorem ContinuousLinearMap.differentiable_quadraticDiagonal
    (Q : V →L[ℝ] V →L[ℝ] V) :
    Differentiable ℝ Q.quadraticDiagonal := by
  intro u
  exact (Q.hasFDerivAt_quadraticDiagonal u).differentiableAt

/--
Build a mild-evolution kernel whose nonlinearity has the bilinear quadratic
form expected of the projected Navier--Stokes convection term.

This constructor does not claim that `Q` is a Leray-projected convection
operator; a concrete NS layer must still prove that semantic identification.
-/
def MildEvolutionKernel.ofQuadratic
    (H : ℝ → V →L[ℝ] V) (Q : V →L[ℝ] V →L[ℝ] V) :
    MildEvolutionKernel V where
  linearEvolution := H
  nonlinearity := Q.quadraticDiagonal

@[simp]
theorem MildEvolutionKernel.ofQuadratic_nonlinearity
    (H : ℝ → V →L[ℝ] V) (Q : V →L[ℝ] V →L[ℝ] V) (u : V) :
    (MildEvolutionKernel.ofQuadratic H Q).nonlinearity u = Q u u := by
  rfl

@[simp]
theorem MildEvolutionKernel.ofQuadratic_nonlinearity_zero
    (H : ℝ → V →L[ℝ] V) (Q : V →L[ℝ] V →L[ℝ] V) :
    (MildEvolutionKernel.ofQuadratic H Q).nonlinearity 0 = 0 := by
  simp [MildEvolutionKernel.ofQuadratic]

/--
For a quadratic mild kernel, the abstract `B(0)=0` obligation needed by the
zero-solution theorem is automatic.
-/
theorem MildEvolutionKernel.ofQuadratic_zero_evolvesAt_zero
    (H : ℝ → V →L[ℝ] V) (Q : V →L[ℝ] V →L[ℝ] V)
    {T : ℝ} (hT : 0 ≤ T) :
    (MildEvolutionKernel.ofQuadratic H Q).EvolvesAt T 0 0 := by
  exact (MildEvolutionKernel.ofQuadratic H Q).zero_evolvesAt_zero hT (by simp)

end QuadraticMildNonlinearity

end MNS2
