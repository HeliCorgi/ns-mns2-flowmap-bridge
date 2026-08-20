# Constant-exclusion pass — branch (a) retired, one open object (OO), one certified conditional row

Date: 2026-08-20 (JST). One bounded fetch-and-verify pass (3 Opus analysts + adversarial
verification + critic; KNSS full text + Lei–Zhang 1011.5066 read first-hand; stop rules
clean: no numerics, no new ansatz, no promotions, no map edits, no in-house Liouville
proof — both reductions are verbatim compositions of quoted theorems, flagged as
candidates). Baseline: `BH_M3_KNSS_GATE_2026-08-20.md`. Tags: [H] hard, [D] derived
(composition of quoted results), [V] verified first-hand, [V?] search-level, [C]
conditional, [C-dict] dischargeable inside the frozen dictionary, [B] bookkeeping.

## 1. RULING: PARTIAL — better than either hoped-for outcome

**Branch (a) — the pure-constant limit — is ELIMINATED, not open** [D, row R-A]:

- KNSS **Lemma 6.1 nowhere requires `C = 1`** ([V] verbatim, l.857–861). Re-centre the
  zoom on the Γ-saturated level supplied by the geometry gate's containment-free
  amplitude corollary (`|u_θ| ≥ H(t_k)/√42` at `|x̃′_k| ≤ √42·Γ₀/H(t_k)`): then
  `M̃_k ∈ [H/√42, H]`, `|ṽ^{(k)}| ≤ √42`, `M̃_k|x̃′_k| ≤ √42·Γ₀` — the axis stays at
  bounded rescaled distance and the limit **is axisymmetric with a Γ-saturated core**.
  Branch (a) was an artifact of insisting on KNSS's exact maximizer; the re-centred
  extraction is available **for every Scope-A blob, B2 included**. The only new content
  is three lines of arithmetic; residue **(N-Γ)** [C-dict] (interior-time lower bound on
  the rescaled Γ at a fixed point; dischargeable from τ-uniform saturation).
- The previously seeded route "boost the *original* flow" is **refuted and recorded**
  (R-NEG1): the wind has size `M_k·b → ∞` in original units. Re-centring, not boosting.
- Deflationary corollary (R-NEG2, [V]): Ożański–Palasek (arXiv:2210.10030 — axisym +
  `L^{3,∞}` bounded ⟹ regular) makes KNSS's own constant-exclusion doctrine
  ("exclude constants by a scale-invariant estimate") **unreachable at an axisymmetric
  singularity by theorem** — but with re-centring we never need to exclude a constant.

**The surviving object is therefore ONE, and the literature itself names it open**:

> **(OO)** Does there exist a non-zero bounded ancient mild axisymmetric solution of
> NS on `R³×(−∞,0)` with `Γ = r·v_θ ∈ L^∞`, `Γ ≢ 0`?
> (Survey arXiv:2101.04905, [V?]: *"the remaining case for the Liouville property,
> which is also the most difficult one, is when Γ does not decay near infinity."*)

M3's tie face and B2's blob both produce exactly this object under the re-centred zoom.

## 2. The certified conditional kill — R-B1 (primary row)

> **Lei–Zhang, JFA 261 (2011), arXiv:1011.5066, Thm 1.2 [V first-hand]:** *"Let v be a
> bounded, weak ancient solution to (1.1). Suppose also r|v^θ| is bounded and the
> stream function is a BMO function. Then v ≡ 0."*

Hypothesis transfer to the re-centred, axially-boosted limit `w`:
bounded ✓; weak ancient ✓ (mild ⟹ weak; the weak class *explicitly admits* the
parasitic `b(t)` — KNSS l.66–67 [V] — so the boost's time-dependence question is
**void**); axisymmetric ✓ (axial boost; axiality of the constant is forced by KNSS's
own definition of axisymmetry, l.585–596 [V/H]); `r|v_θ|` bounded ✓ **free** — the
exact scale-invariance `Γ_{v^{(k)}} = Γ_u` [D] means every amplitude-normalized ancient
limit inherits `|v_θ| ≤ Γ₀/r` globally; **the stream function `B_w ∈ BMO` — the ONE
open hypothesis.** Sizing [D]: `r|w_pol| ≤ C` (the (Q)-form) ⟹ `B_θ = ψ/r` bounded ⟹
BMO, and BMO additionally tolerates `ψ/r ~ log r` — one logarithm plus oscillation of
slack over (Q); the swirl side is comfortable (`B_z ~ Γ₀ log r ∈ BMO`).

**If discharged: `w ≡ 0` ⟹ `v = b·e_z` ⟹ `Γ ≡ 0` — contradicting the Γ-saturated core
⟹ the tie face AND B2's Γ-saturated blob die, consuming no Type-I bound, no viscosity,
no Scope-A geometry.** Fallback row R-B2 (KNSS Thm 5.3 + boost, debt (Q) in ball form)
is subsumed by R-B1. Rejected rows: R-B3 (LZZ `Γ ∈ L^p`, `p < ∞` — hypothesis does not
descend, `M_k³`-blow-up, and expected false on a saturated core); R-B4 (Lei–Ren–Zhang
1902.11229 Thm 1.2 carries a smallness constant `ε₀`, not a mere `1/r` rate — a `1/r`
tail with `O(1)` coefficient does not discharge it; its sibling needs z-periodicity).

## 3. Corrections and escalation

- **"Constant background at spatial infinity" is not a descended fact** [D]: locally
  uniform convergence says nothing at `|y| → ∞`; `b` is *defined* by the far-field
  hypothesis. 100% of the content sits in the far-field poloidal debt — the Galilean
  boost is bookkeeping.
- **(E) ⟹ (Q) holds** (re-checked: the failure radius recedes, `R_k ≍ τ^{(ρ₂−γ)/2}`)
  **but requires (E⁺)** = (E) + C¹-exhaustiveness within `τ^{(γ+ρ₂)/2}` of the zoom
  centre (excludes R2's own forced tongue). **Escalation**: if (E⁺) is charged, the
  tie face dies at the same hypothesis strength that killed `γ₂ < γ` — the KNSS gate's
  literal NO-ruling stands, but its consequence "the face survives, merging into B2"
  does not survive (E⁺).
- KNSS mechanics now cited, not inferred [V, l.1088–1100]: their receding-axis branch
  gets `w = 0` from Thm 5.1 + Rem 6.1 **plus (6.16)** (rescaled Type-I) — the last
  step is implicit in the paper.
- `b`-constancy: the Rem-6.1-based derivation is refuted (its hypothesis is "of the
  form b(t)"); the dictionary-freezing derivation survives as [C-dict]; and the
  question is void anyway (weak class admits `b(t)`).

## 4. Queue for the freeze review (exact wordings drafted by the critic)

(1) K4′ amend: "(E)+(P)" → "(E⁺)+(P)". (2) New row **K4″ [C]**: re-centred Lemma-6.1
limit + Γ-max + (N-Γ) + axial boost + **BMO stream function** (Lei–Zhang Thm 1.2 [V])
⟹ excludes the whole tie face and B2's Γ-saturated sub-core. (3) New row **K4‴ [D,
unconditional]**: `Γ` is exactly scale-invariant under Prop-6.1 rescaling — every
amplitude-normalized ancient limit satisfies `|v_θ| ≤ Γ₀/r`; every Thm-5.3-type
application reduces to a poloidal statement. (4) P7 legend: `Γ ∈ L^p (p<∞)` joins the
non-descending list; `Γ ∈ L^∞` descends. (5) KNSS footnote (implicit (6.16) step).
(6) Negative rows R-NEG1/R-NEG2 + "no Liouville theorem can exclude a non-zero
constant — constants are genuine members; post-KNSS refinements are
constant-producing". (7) Branch wording: "M3's tie face and B2 reduce to **one**
object (OO); branch (a) retired as an exact-maximizer artifact."

## 5. Next bounded task (critic-designated)

**Discharge or refute the far-field poloidal debt IN-HOUSE, by Biot–Savart** — an
estimate on our own flow, not a rigidity theorem (does not trip the
no-in-house-Liouville rule): extend the geometry gate's poloidal ledger
(`r|u_pol| ≲ 1` for `r ≥ τ^γ`, already established for the core dipole tail) to the
**deviation field** `u_pol − b_τ` on `R₀τ^γ ≤ |x − x̃_k| ≤ R_kτ^γ` with τ-uniform `C`,
under (E⁺); then read off which of `r|w_pol| ≤ C` (⟹ R-B2), `ψ_w/r ∈ BMO` (⟹ R-B1,
the cheaper target — one logarithm of slack), or neither, is delivered. **Do not stand
down to B2's V1 — V1 is unpromoted and is now the more expensive route.**
