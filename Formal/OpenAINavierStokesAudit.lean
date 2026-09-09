import Mathlib

namespace MNS2
namespace OpenAINavierStokesAudit

/-!
This file starts an adversarial formal audit of the algebraic spine of the
OpenAI manuscript `Finite Time Blowup for Navier–Stokes` (2026-09-08).

It deliberately proves only identities that are explicitly used in the paper.
No PDE construction, blowup theorem, or Clay claim is imported as an assumption.

First target: the algebra in Lemma 4.5, equations (4.20)–(4.23), because the
admissible stress cone is load-bearing for the later oscillatory realization.
-/

/-- The paper's `t_s = -b_s/a`. -/
def ts (a bs : ℝ) : ℝ := -bs / a

/-- The paper's `v_s = a (1+t_s^2)`. -/
def vs (a bs : ℝ) : ℝ := a * (1 + (ts a bs) ^ 2)

/-- The normalized coefficient `c = 1 - b_s w/a` used in Lemma 4.5. -/
def coneC (a bs w : ℝ) : ℝ := 1 - bs * w / a

/-- The normalized coefficient `j = w + b_s/a` used in Lemma 4.5. -/
def coneJ (a bs w : ℝ) : ℝ := w + bs / a

/-- The equivalent rational form `v = a + b_s^2/a` used in the proof. -/
def coneV (a bs : ℝ) : ℝ := a + bs ^ 2 / a

/-- Equation (4.20): the two displayed formulas for `v_s` agree when `a ≠ 0`. -/
theorem vs_eq_coneV (a bs : ℝ) (ha : a ≠ 0) :
    vs a bs = coneV a bs := by
  field_simp [vs, ts, coneV, ha]
  ring

/--
Under `p_{s,2} = w p_{s,1}`, equation (4.20) gives
`P_c = p_{s,1} (1 - b_s w/a)`.
-/
theorem Pc_substitution (a bs w ps1 : ℝ) (ha : a ≠ 0) :
    ps1 + ts a bs * (w * ps1) = ps1 * coneC a bs w := by
  field_simp [ts, coneC, ha]
  ring

/--
Under `p_{s,2} = w p_{s,1}`, equation (4.20) gives
`J_c = p_{s,1} (w + b_s/a)`.
-/
theorem Jc_substitution (a bs w ps1 : ℝ) (ha : a ≠ 0) :
    w * ps1 - ts a bs * ps1 = ps1 * coneJ a bs w := by
  field_simp [ts, coneJ, ha]
  ring

/--
The factorization displayed in the proof of Lemma 4.5:

`(v-2) j^2 - 2 c^2
 = (1 + b_s^2/a^2) ((a-2)w^2 + 2 b_s w + b_s^2/a - 2)`.

This is a purely algebraic check; the sign hypotheses used later are separate.
-/
theorem lemma45_factorization (a bs w : ℝ) (ha : a ≠ 0) :
    (coneV a bs - 2) * (coneJ a bs w) ^ 2 - 2 * (coneC a bs w) ^ 2
      =
    (1 + bs ^ 2 / a ^ 2) *
      ((a - 2) * w ^ 2 + 2 * bs * w + bs ^ 2 / a - 2) := by
  field_simp [coneV, coneJ, coneC, ha]
  ring

/--
The normalized polynomial expansion used immediately after the compactness
threshold choice in Lemma 4.5. Here `P_c = p c` and `J_c = p j`.
-/
theorem lemma45_threshold_expansion (c j v p : ℝ) (hp : p ≠ 0) :
    (2 * (p * c - v) ^ 2 - (v - 2) * (p * j) ^ 2) / p ^ 2
      =
    (2 * c ^ 2 - (v - 2) * j ^ 2) - 4 * c * v / p + 2 * v ^ 2 / p ^ 2 := by
  field_simp [hp]
  ring

#print axioms vs_eq_coneV
#print axioms Pc_substitution
#print axioms Jc_substitution
#print axioms lemma45_factorization
#print axioms lemma45_threshold_expansion

end OpenAINavierStokesAudit
end MNS2
