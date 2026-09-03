# HSEL_V15_DISCHARGE — 2026-09-04 — V-15 discharged at primary level: the (4,2) directional-derivative criteria verified smallness-free and non-degenerate at q = 2; the class-match is CLEAN (CFZ's theorem is stated for the strong solution itself); the proof is quantitative end to end; rotation invariance and DQ-1 integration confirmed; the Gram/coherence form is NOT demoted by prior art; VERDICT: QUANTITATIVE-BRIDGE (RECORD-ONLY)

**Repo:** `c:/Users/corgi/Downloads/ns-mns2-flowmap-bridge` · **Status: RECORD-ONLY.** No Lean file touched; no numerics; no proof search on T-DIR/T-DIR-SPK; nothing frozen moved. Lean baseline unchanged (8775-job gate).

**Commissioning provenance.** User instruction, 2026-09-04 (sixteenth session): discharge V-15 — verify at primary level (1) that `∂₃u ∈ L⁴_tL²_x` is genuinely covered smallness-free as the equality/native member; (2) the class-match `certified strong solution → Leray–Hopf → criterion → continuation`; (3) whether the proofs are quantitative — `‖∂₃u‖_{L⁴_tL²_x} ≤ Q` and `‖u0‖_{H³} ≤ M` ⟹ `sup_{t≤T}‖u(t)‖_{H³} ≤ F(ν,T,M,Q)` by constant tracking alone; (4) rotation `e ↦ e₃` constant invariance; (5) that DQ-1 folds into maximal-horizon continuation without extra hypotheses; plus a targeted prior-art check on the Gram/coherence form `inf_{e∈S²}∫₀^T(eᵀG(t)e)²dt`. Verdict ∈ {QUANTITATIVE-BRIDGE / QUALITATIVE-ONLY / DEMOTED-BY-PRIOR-ART / CLASS-GAP}.

**Method.** Two lanes: (A) full primary deep-read of both bridge papers; (B) targeted prior-art check on the Gram form. Main-loop adjudication; [D] items re-derived. Levels [V-P]/[V-adj]/[V-abs]/[D] as before.

---

## §1 — The five commissioned determinations

**(1) Membership / smallness / native equality: VERIFIED [V-P].** P1 = Zhang, Bull. Math. Sci. (2017; pagination 8 (2018) 33–47), Thm 2 verbatim: window `q ∈ [(3√37)/4−3, 3]` **closed at both ends**, no smallness anywhere; `q = 2` strictly interior, and the proof's interpolation exponents evaluated at `q = 2` (`ϑ₁..ϑ₄ ≈ 0.506/0.507/0.334/0.692`) are all strictly interior — no degeneration (edges only). P2 = **Hui** Chen–Fang–Zhang (arXiv:2007.10888 v1; MMAS 44 (2021), DOI 10.1002/mma.7097 — author-name correction recorded; published text unverified vs v1, statement match confirmed), Thm 1.1 verbatim: window `q ∈ (3/2, 6]`, no smallness (the `q = 3/2, p = ∞` smallness is a separate Remark-1 endpoint statement); `q = 2` sits in the non-degenerate middle branch `2 ≤ q < 3` (the dangerous exponent `4q/(5q−9)` blows up only at `q = 9/5`, served by the other branch). Both papers normalize `ν = 1`; general-ν recovery by the exact recipe `F(ν,T,M,Q) =` unscaling of `F(1, νT, ν⁻¹M, ν^{−3/4}Q)` [D].

**(2) Class-match: CLEAN — better than commissioned (no Leray–Hopf passage needed): NOT CLASS-GAP [V-P].** P2's Theorem 1.1 is stated **directly for the unique `H¹` strong solution** and its whole proof is an a priori estimate on that object up to its maximal time — the certified solution (`u0 ∈ H³ ⊂ H¹`) IS the theorem's object with `T = T*`; no weak-solution class enters the load-bearing line at all. (P1's weak-class Definition 1 carries an energy-inequality-from-0-only convention and a tacit weak–strong-uniqueness step — irrelevant for the bridge since our object is the strong solution; P1 is corroboration only.)

**(3) Quantitativity: YES — P2 self-contained [V-P].** The full skeleton was mapped (anisotropic Biot–Savart Lemma 2.1; the `(ω³, ∂₃u, u³)` estimate chain (3.2)–(4.10); closing (5.5)–(5.6); the final self-contained `H¹` display `‖∇u(t)‖₂² ≤ ‖∇u(T₁)‖₂² exp(C∫E⁴)`): **every step is explicit energy/interpolation/CZ/Grönwall; no compactness, no contradiction-without-quantities, no delegation to any external criterion.** The qualitative tail-smallness becomes quantitative by interval partition `N ≤ ⌈(2C₁Q)⁴⌉+1`, giving `E₂ ≤ 4^N E₂(0)` (`E₂(0) ≤ c(M²+M³)`), then `sup_t‖u‖²_{H¹} ≤ cM²·exp(CT(4^N E₂(0))⁴)`; with `u0 ∈ H³` the standard quantitative subcritical bootstrap tops out at `H³`. **Result: `sup_{t≤T}‖u(t)‖_{H³} ≤ F(ν,T,M,Q)` with `F` explicit (double-exponential-type in `Q⁴`).** Notably — unlike the axisym lane's `M′` carry — **no extra datum input appears anywhere: the general-lane constant is `M`-only.** P1 alone would carry a flag (its terminal step delegates to Zhang–Yao–Lu–Ni JMP 52 (2011) Prop 1.1, paywalled/unverified) — recorded as corroboration, not load-bearing.

**(4) Rotation invariance: VERIFIED [V-P + D].** Both papers' constants are absolute inequality constants (Hölder/GN/Cao-type/CZ at fixed exponents) plus solution norms — no frame-dependent input (P1's Lemma 3 is even stated permutation-generally). NS rotation-equivariance + rotation-invariance of `L^p_tL^q_x` norms give the `∂_e u` criterion for every `e ∈ S²` with **identical constants**.

**(5) DQ-1 integration: NO EXTRA HYPOTHESES [D].** With P2's strong-solution framing, the plug is: horizons bounded with `T* = sSup` ⟹ DQ-1 extracts a fixed `e*` with the budget `≤ Q₀` on `[0,T*)` ⟹ rotate `e* ↦ e₃` ⟹ Thm 1.1 at `T = T*` forbids blow-up at `T*` (the a priori `H¹`/`H³` bound holds up to `T*`) ⟹ local theory restarts ⟹ contradiction with maximality — the SEL-10 pattern verbatim, consuming nothing beyond what DQ-1 and the theorem already state (the weak-limit extension contemplated at DQ-1 §1(b) is not even needed on this route).

## §2 — Prior-art check on the Gram/coherence form: NOT DEMOTED

Targeted verification (lane B): **no published theorem is equivalent to, or dominates, `inf_{e∈S²}∫₀^T(eᵀG(t)e)²dt ≤ Q₀`** — no Gram-matrix formulation, no direction-infimum, and no unconditional bound on any such object exists anywhere in the searched record (Miller's survey confirms the unconditional inventory is essentially the energy equality — which gives exactly our free `∫‖∂_e u‖₂²dt ≤ E₀/ν` for every `e`, the wrong power: the half-unit gap as framed). Nearest relatives, all recorded: (i) CFZ/Zhang fixed-direction criteria — **consumers/pairing theorems**, not prior art (rotation covariance makes fixed-`e₃` ⟺ ∃-`e` at criterion level; no one has exploited direction optimization); (ii) **Miller arXiv:2002.02152 Thm 1.6** — the only published genuinely existential-direction `L⁴_tL²_x` budget statement, for the in-plane vorticity `v×ω` with even `(x,t)`-dependent direction fields, conditional, with an explicit exponential `Ḣ¹` bound — the closest structural neighbor (a candidate variant channel, recorded, no action); (iii) Neustupa–Penel/Miller strain-eigenvalue criteria — pointwise spectral, incomparable; (iv) the small-`∂₃u`/almost-2D global results (Liu–Zhang; Liu–Paicu–Zhang; Chemin–Gallagher(–Paicu); Iftimie) — **validating smallness relatives** at the head's small end, none unconditional, none quantified over `e`; (v) Constantin–Fefferman — a different object (pointwise vorticity-direction field). 

## §3 — VERDICT and the completed chain

**VERDICT: QUANTITATIVE-BRIDGE** (and NOT-DEMOTED-BY-PRIOR-ART; NOT CLASS-GAP; NOT QUALITATIVE-ONLY). **V-15 is DISCHARGED.** The general-lane chain is now verified end to end:

```
[T-DIR]  ∃e ∈ S²: ∫₀^{T′}‖∂_e u‖⁴_{L²}dt ≤ Q₀(ν,T,M)      (OPEN — the only open link)
   ▼ DQ-1 [D, closed, zero loss] + rotation invariance [V-P/D]
   ▼ CFZ Thm 1.1 at (p,q) = (4,2) [V-P, smallness-free, strong-solution-framed,
     quantitative; P1 corroborates the window]
[sup_{t≤T}‖u‖_{H³} ≤ F(ν,T,M,Q₀)]  — explicit F, M-only (no M′-analogue)
   ▼ SEL-2 ⟹ H-SEL^nu (GENERAL class, M-ball) ⟹ (EB-1 + integration) N0 ⟹ Lean N1→N2→N3.
```

**Position note (recorded):** with V-15 discharged, the GENERAL lane matches and surpasses the axisym lane's end state — the entire downstream bridge is verified quantitative published mathematics, with **no extra ball parameter** (the axisym lane needed `M′ = ‖ru₀^θ‖_∞`), and the only open object is T-DIR itself (equivalently its compressed production-budget form T-DIR-SPK, or the Gram form `inf_e∫(eᵀGe)²dt ≤ Q₀`). This is the strongest verified state the head lineage has reached.

Residual flags (none load-bearing): P1's [33] delegation unverified (P1 is corroboration); MMAS published text vs arXiv v1 unverified (statement match confirmed); author correction (Hui Chen); Kukavica–Ziane/Chae–Choe originals quoted via Miller's survey; Namlyeyeva–Skalák ZAMM blocked (subsumed by CFZ's window).

## §4 — Claim boundary

RECORD-ONLY; no Lean edit; no numerics; no proof search on T-DIR/T-DIR-SPK/H-SEL/N0 — this record verifies the bridge and its constants, nothing about the open head. **Nothing here asserts, approaches, or implies a resolution of the Navier–Stokes Millennium problem in either direction.** The lane-B consequence is restated with C0 care: a proved T-DIR would yield regularity on the given horizons through the published criteria — i.e., universal T-DIR is Clay-equivalent-or-harder, exactly as every head in this lineage; its value remains positional (free budget, exact damping, pressure-cancelled production, published quantitative bridge, single scalar observable). Commissioning the probe or any proof work on T-DIR is a user act. C0 discipline throughout.
