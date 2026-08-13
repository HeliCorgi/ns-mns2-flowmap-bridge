import Formal.R3L2ScalarAux

namespace MNS2

open MeasureTheory

noncomputable section

def r3L2CoordinateAux (i : Fin 3) :
    R3L2Velocity →L[ℂ] R3L2ScalarAux :=
  (ContinuousLinearMap.proj i : R3C →L[ℂ] ℂ).compLpL 2 (volume : Measure R3)

theorem r3L2CoordinateAux_ae (i : Fin 3) (f : R3L2Velocity) :
    r3L2CoordinateAux i f =ᵐ[volume] fun ξ => f ξ i := by
  exact (ContinuousLinearMap.proj i : R3C →L[ℂ] ℂ).coeFn_compLpL f

end

end MNS2
