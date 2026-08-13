import Mathlib
import Formal.R3StokesL2Operator

namespace MNS2

noncomputable section

def r3CoordinateLinearAux (i : Fin 3) : R3C →ₗ[ℂ] ℂ where
  toFun v := v i
  map_add' x y := rfl
  map_smul' c x := rfl

end

end MNS2
