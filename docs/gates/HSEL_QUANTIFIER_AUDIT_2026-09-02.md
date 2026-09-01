# HSEL_QUANTIFIER_AUDIT — 2026-09-02 — quantifier/falsification audit of the H-SEL head: datum-specific vs norm-uniform fixed explicitly; falsification certificates defined; operative head re-adjudicated to the norm-uniform form (RECORD-ONLY)

**Repo:** `c:/Users/corgi/Downloads/ns-mns2-flowmap-bridge` · **Status: RECORD-ONLY.** No Lean file touched (one read-only verbatim extraction from `Formal/R3TSelBridge.lean`); no proof search; no numerics; no frozen change. Lean verification baseline unchanged (8775-job gate).

**Commissioning provenance.** User instruction, 2026-09-02 (seventh session): fix uniquely, from the theorem statement and the dependency chain, whether the operative H-SEL constant is **datum-specific** `Q₀(u0,T,ν)` or **norm-uniform** `Q₀(T,ν,M)` — the notation `Q₀(T;ν,‖u0‖)` alone does not pin norm-only dependence, so make the quantifiers explicit; for each variant confirm `H-SEL → N0 → global continuation` and define the exact numerical falsification certificate (datum-specific: unbounded `Q₅` toward a bounded horizon along a single certified trajectory; norm-uniform: `sup_t Q₅ → ∞` along a norm-bounded initial-data family at fixed `T,ν,M`); re-adjudicate which variant is the operative research head. No Lean change, no proof search, no numerics.

Notation: `U` = decoded field, `E(t) = ‖∇U(t)‖²_{L²}`, `Q₅(t) = ‖∇U(t)‖_{L∞}/(1+E(t))`, `‖·‖` = the carrier Bessel-`H³` norm (classically measurable through the proved SEL-1 constants `1/81`, `27(2π)⁶`).

---

## §1 — The two variants, quantifiers explicit (EQ-1, EQ-2)

**H-SEL^ds (datum-specific):**

> ∀ν>0 · ∀ admissible Schwartz datum u0 · ∀T<∞ · **∃Q₀ = Q₀(u0,T,ν) < ∞** · ∀ certified solution u on ∀ certified horizon T′ ≤ T · ∀t ∈ [0,T′]: `‖∇U(t)‖_∞ ≤ Q₀(1+E(t))`.

**H-SEL^nu (norm-uniform):**

> ∀ν>0 · ∀T<∞ · ∀M<∞ · **∃Q₀ = Q₀(T,ν,M) < ∞** · ∀ admissible Schwartz datum u0 with `‖u0‖ ≤ M` · ∀ certified solution/horizon T′ ≤ T · ∀t ∈ [0,T′]: `‖∇U(t)‖_∞ ≤ Q₀(1+E(t))`.

The difference is exactly the position of `∃Q₀` relative to `∀u0`. `H-SEL^nu ⟹ H-SEL^ds` (instantiate `M = ‖u0‖`); the converse is **not** known (§2, EQ-3).

**EQ-1 (notation ruling).** Every prior print of "`Q₀(T;ν,‖u0‖)`" (head-reduction audit §5/§9, P-1 record, HANDOFF) is hereby fixed to have asserted only the **ds** reading — the ∃ was always written after ∀u0, and the parenthetical `‖u0‖` was suggestive notation, not a norm-uniformity claim. The same ruling applies to the N0 print "`∃ G(T;ν,‖u0‖)`" of the Stage-9 audit SS-5. No prior verdict changes; this is a clarification, not an erratum — but from this record on, the two forms must be named explicitly.

**EQ-2 (Lean anchor — verbatim, read-only this session).** `Formal/R3TSelBridge.lean`:

```
def R3TSelGradientBound {nu : ℝ} (hnu : 0 < nu) (u0 : R3HsVelocity 3) : Prop :=
  ∀ T : ℝ, ∃ G : ℝ, ∀ T' : ℝ, T' ≤ T → ∀ u, IsR3EndpointSafeProjectedMildSolutionOn hnu T' u0 u →
      r3TSelGradIntegral u T' ≤ G
```

with docstring "a bound `G` (allowed to depend on `T, ν, u0`)", and `R3TSelHead = ∀ν ∀ admissible φ, R3TSelGradientBound …`. **The formal N0 is the datum-specific form**: `∃G` sits inside fixed `(ν, u0, T)`.

## §2 — Chain check for each variant (EQ-3)

- **H-SEL^ds ⟹ N0 (Lean form) ⟹ N1 ⟹ N2 ⟹ N3: HOLDS.** Per fixed `(ν,u0,T)`: Arrow α (EB-1 energy equality, paper) gives `∫₀^{T′}E dt ≤ ‖U(0)‖²_{L²}/(2ν)` with `‖U(0)‖_{L²} ≤ ‖u0‖` (Bessel decoder symbol ≤ 1 — paper-trivial; the Lean-absent decoder-norm bound is part of the B2 debt, as recorded); Arrow β′ (direct integration) gives `G(u0,T,ν) = Q₀(u0,T,ν)·(T + ‖u0‖²/(2ν))` — exactly the `∃G` the Lean Prop demands. Downstream, `r3TSel_uniform_carrierBound_of_head` consumes the head by `obtain ⟨G, hG⟩ := hhead T` **at fixed datum** (verified verbatim this session), and N2/N3 quantify per-datum. **The Lean chain requires nothing more than ds.**
- **H-SEL^nu ⟹ (instantiate `M = ‖u0‖`) H-SEL^ds ⟹ chain: HOLDS a fortiori**, with the norm-uniform surplus `G(T,ν,M)` and hence a norm-uniform N1 (`R(T,ν,M) = M·exp(C·G)` — a uniform-in-ball carrier bound, i.e. *effective* regularity bounds). The surplus is unused by the Lean chain; it is a bonus conclusion, not a requirement.
- **EQ-3 (the gap between the variants is itself open).** `ds ⟹ nu` is a uniform-boundedness/effectivity question over the non-compact `H³` ball, not known to follow: the compactness technology that converts qualitative into quantitative regularity operates at critical-norm granularity (profile decompositions; Tao arXiv:1908.04958's bounds are conditional on the critical `L³` cap) and does not close it, and no theorem in the P-1 record does either. **H-SEL^nu is possibly strictly stronger than H-SEL^ds.**

## §3 — Falsification certificates, exact (EQ-4, EQ-5)

**EQ-4 (ds certificate ⟺ blow-up certificate — H-SEL^ds is NOT independently falsifiable).** Certificate of `¬H-SEL^ds`: one `(ν,u0,T)` and certified times `t_k` inside certified horizons `≤ T` with `Q₅(t_k) → ∞`. Two-sided reduction [D]:
(a) if the trajectory extends smoothly (in the certified sense) to the compact `[0,T]`, then `t ↦ ‖∇U(t)‖_∞` is continuous (trajectory continuity + the proved Lipschitz continuity of the gradient-sup carrier, `Formal/R3TSelDecodedGradient.lean`), so `Q₅` is bounded — no certificate exists;
(b) conversely, if `Q₅` is bounded by some `Q₀` on the maximal certified evolution, the per-datum bridge (Arrow α+β′, then the proved Lean N0→N2 at that datum, modulo the on-hold SEL-5/SEL-3 known-math debts) extends the certified horizons past any bound — so a certificate forces, and is forced by, failure of certified continuation before `T`.
**Hence falsifying H-SEL^ds is exactly the lab's singularity program goal**: a validated finite-time-blow-up certificate. No finite computation on a smooth trajectory can produce it ("Q₅ grew large" is always consistent with a large `Q₀(u0)`). Under the ds reading, `Q₅` retains only its *necessary-signature* role: any candidate singularity must diverge `Q₅` (at rate ≥ `τ^{−(2α−γ)}` in the frozen window, per §9.3 of the head-reduction audit).

**EQ-5 (nu certificate — genuinely independent falsification channel).** Certificate of `¬H-SEL^nu`: fixed `(ν,T,M)` and a sequence of admissible Schwartz data `u0^{(k)}`, `‖u0^{(k)}‖ ≤ M`, with certified times `t_k ≤ T` and `Q₅^{(k)}(t_k) → ∞`. **Every member may be a globally smooth, fully resolvable trajectory — no blow-up is required.** Grades:
- *Theorem-level refutation:* an explicitly constructed family with proven divergence of `sup_{t≤T}Q₅^{(k)}`. This would prove genuine non-uniformity/non-effectivity over subcritical balls — a Palasek-adjacent (C-2) result, publishable in its own right, and it would **not** decide the Clay alternative (H-SEL^ds and N0 survive it untouched — the recorded asymmetry).
- *P-2 numerical-evidence grade (defines the P-2 probe):* a preregistered one-parameter family inside the fixed `M`-ball (seeds: C-1's Lu–Doering-maximizer-shaped and frequency-staircase data, normalized to `‖u0^{(k)}‖ = M`), each member's trajectory resolution-validated on `[0,T]`, the observable `S(k) := sup_{[0,T]}Q₅^{(k)}` measured with error control, and a preregistered acceptance threshold for "growth beyond any datum-uniform fit". Numerics can only ever grade as EVIDENCE-FOR/EVIDENCE-AGAINST/UNDETERMINED — never as a proof of `¬H-SEL^nu`; the fail-closed gate discipline of the lab applies. (Bridging classical numerics to the certified class is P-2 methodology to be fixed at commissioning.)

**EQ-6 (nu is a short-time theorem — non-vacuity check [D]).** For `T ≤ T₀(ν,M)` (the existing Lean explicit lifespan `r3MildLifespan` at radius `M`), the certified trajectory stays in the `M+1` carrier ball, so SEL-2 gives `‖∇U(t)‖_∞ ≤ C_emb(M+1)` and `Q₅ ≤ C_emb(M+1)` uniformly over the ball: **H-SEL^nu holds up to the local lifespan with existing machinery.** The open content is exactly horizon extension past `T₀(ν,M)` — the head is neither vacuous nor instantly false, and the battle line is sharply located.

**Battery note for nu [D].** All recorded violators (frozen-B2, Type-I, the Tao averaged cascade) are single-trajectory objects: they violate ds and a fortiori nu — polarity unchanged. The one attack shape nu is newly exposed to — a smooth-family attack — has no known instance: C-1's kinematic maximizers, used as *data* in the `M`-ball, give `Q₅(0) ≤ C_emb·M` (bounded; their extreme ratio lives at enstrophy levels the ball excludes), and Palasek's family is not `H³`-bounded. **H-SEL^nu also SURVIVES the current battery.**

## §4 — Re-adjudication (EQ-7, EQ-8)

**EQ-7 — THE OPERATIVE RESEARCH HEAD IS FIXED AS `H-SEL^nu`** (C0: a selection, not a uniqueness claim), with `H-SEL^ds` retained as the derived fallback that the Lean chain minimally consumes. Grounds:

1. **Falsifiability was load-bearing in the selection.** The head-reduction audit scored HR-5 partly on its cheap falsification observable; EQ-4 shows that under the ds reading this advantage (for HR-5 and for every head in the roster) collapses — ds-falsification is the program's own terminal goal. Only the nu reading delivers the commissioned "independently falsifiable" property, and only under it is P-2 a well-defined experiment (EQ-5).
2. **The chain is intact:** nu ⟹ ds ⟹ Lean-N0 ⟹ N1→N2→N3 (§2), with the effective-bounds surplus as bonus.
3. **Both outcomes are informative:** proof of nu ⟹ global continuation of the certified class *plus* uniform-in-ball effective bounds; refutation of nu ⟹ a genuine non-uniformity theorem (C-2-adjacent) that leaves the Clay alternative untouched — the correct two-sided polarity, now with an honest statement of what each side does *not* decide.
4. **Constraints C-1/C-2/C-3 carry over unchanged**, and C-2 (Palasek) in fact selects the nu form's shape: `M` must be a subcritical norm — which it is (carrier `H³`).

**EQ-8 (roster-wide quantifier fix).** The same explicit-quantifier discipline applies to every head in the roster (HR-1 coherence, HR-3′ sparseness, …): each is henceforth read in its norm-uniform form for falsifiability purposes, with the datum-specific form as the chain-sufficient fallback. This changes no ranking (the printed falsifiability scores were implicitly nu-read; this record makes it explicit) and no verdict.

**Consequential update to P-2 (statement only; commissioning remains a user act):** P-2 = the *family* probe of EQ-5 at fixed `(ν,T,M)` — not a single-trajectory probe. The single-trajectory `Q₅` measurement survives separately as the necessary-signature diagnostic inside the singularity program (EQ-4).

## §5 — Claim boundary

RECORD-ONLY; the only repository access was a read-only verbatim extraction of the N0 Prop; no Lean edit, no proof search, no numerics; SEL-3/SEL-5, EB-1, M-1 all remain on hold; nothing frozen moved. **Nothing here asserts, approaches, or implies a resolution of the Navier–Stokes Millennium problem in either direction.** Both H-SEL^nu and H-SEL^ds are OPEN; universal H-SEL^ds is Clay-equivalent-or-harder for the certified class, and H-SEL^nu is possibly strictly harder (EQ-3); EQ-6's short-time statement is the only thing here that known machinery proves, and it is claimed only up to the existing explicit local lifespan. C0 discipline throughout: the nu selection is a selection; the ds fallback and the EQ-3 gap are printed, not hidden.
