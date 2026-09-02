# HSEL_PROOF_ROUTE_SELECTION — 2026-09-02 — proof-route selection audit for H-SEL^nu: the no-swirl mechanism decomposed into four components; the with-swirl break isolated to one divergence-form source budget; THE SELECTED MINIMAL SOURCE-CONTROL THEOREM: T-SRC (RECORD-ONLY)

**Repo:** `c:/Users/corgi/Downloads/ns-mns2-flowmap-bridge` · **Status: RECORD-ONLY.** No Lean file touched; no numerics; no direct proof search on H-SEL^nu; nothing frozen moved. Lean baseline unchanged (8775-job gate).

**Commissioning provenance.** User instruction, 2026-09-02 (tenth session): decompose the S-7 no-swirl uniform-bound mechanism (`HSEL_S7_UNIFORMITY_DECISION_2026-09-02.md` §3) into minimal logical components (ball-controlled Hardy/Lorentz quantity; its time propagation; static Biot–Savart control of the stretching coefficient; closure to the `H³` ladder / H-SEL); for the with-swirl class, where the source `∂_z(Γ²/r⁴)` enters, candidate what must replace the lost monotonicity; derive the **weakest** function-space estimate on the source that closes (Lorentz / negative-Sobolev / divergence-form / time-integrated budgets — no premature `L∞` demand); run each candidate counterexample-first against the four filters (ball-known? energy/enstrophy-known? broken by frozen failcases / Tao averaged / concentration profiles? a rephrase of axisym-with-swirl global regularity?); select **one** minimal source-control theorem and print the dependency chain `new source estimate ⟹ no-swirl mechanism survives ⟹ H-SEL^nu` (on the axisymmetric sub-ball — quantifiers per the EQ-7/EQ-8 discipline).

Notation: `q := u_θ/r = Γ/r²`, `η := ω_θ/r`, `A := ‖u_r/r‖_{L∞}`, `Δ̃ := Δ + (2/r)∂_r` (the 5-D Laplacian on axisymmetric functions); norms 3-D Lebesgue; all statements per-datum/per-horizon in the norm-uniform `∃Q₀(ν,T,M)` form.

---

## §1 — The no-swirl mechanism, decomposed (with-swirl survival per component)

The system in the good variables (Hou–Li form [H]; the source `∂_z(Γ²)/r⁴ = ∂_z(q²)` since `r` is `z`-independent — the commission's source **is exactly a `z`-divergence of `q²`**):

> `∂_t q + u_pol·∇q = νΔ̃q − 2(u_r/r)q` · `∂_t η + u_pol·∇η = νΔ̃η + ∂_z(q²)` (sign conventions vary; magnitudes only are used).

| Component | Content (no-swirl proof) | With swirl |
|---|---|---|
| **C-P1 (ball-controlled datum quantity)** | weighted 1-D Hardy (`a = 1 < p−1`, `p > 2`) + `∇ω ∈ H¹ ↪ L^p` ⟹ `‖η₀‖_{L^{p₀}∩L^{p₁}} ≤ CM`, `2 < p₀ < 3 < p₁`, `↪ L^{3,1}` | **SURVIVES verbatim** (a datum statement). Bonus [D]: `q` is a `∇u`-order quantity (`u_θ` vanishes on the axis ⟹ `\|q\| ≤ ‖∇u‖_∞` pointwise), so `‖q₀‖_{L^p} ≤ C_pM` for **all** `p ∈ (2,∞]` — `q` does **not** live in the C²-escape window |
| **C-P2 (time propagation)** | all `L^p(ℝ³)` norms of `η` non-increasing (transport kills by 3-D incompressibility; axis viscous term good-signed) | **THE ONLY BROKEN COMPONENT.** The inhomogeneous estimate [D]: pairing `∂_z(q²)` with `\|η\|^{p−2}η`, integrating by parts in `z`, and absorbing into the dissipation (`Cauchy–Schwarz` against `ν∫\|η\|^{p−2}\|∇η\|²`) gives `d/dt‖η‖²_{L^p} ≤ C_p ν^{−1}‖q(t)‖⁴_{L^{2p}}` — **the divergence structure converts the source requirement into a single time-integrated quartic budget `𝔅_p := ∫₀^T‖q‖⁴_{L^{2p}}dt`; no `L∞` of the source is ever needed** |
| **C-P3 (static drift estimate)** | (L*): `‖u_r/r‖_∞ ≤ C‖η‖_{L^{3,1}}` (AHK Prop 4.1(i) [V-P]) | **SURVIVES verbatim** (kinematic Biot–Savart, involves `ω_θ` only) |
| **C-P4 (closure to `H³`/H-SEL)** | stretching Grönwall + subcritical bootstrap | **conditional-known-class**: given `sup_t A ≤ K` (from restored C-P2/C-P3), `‖q(t)‖_{L^p} ≤ ‖q₀‖_{L^p}e^{2Kt}` (zeroth-order coefficient `−2u_r/r`), and the remaining bookkeeping to uniform `H³` is `u_r/r`-criterion-type known mathematics (KPZ-adjacent; **debt V-12**, §4) or [D]-standard assembly |

**Why no unconditional closure exists [D] (honesty check).** Feeding C-P3 back into the `q`-growth and the `𝔅`-budget yields the self-closing inequality `Z(t)² ≲ M² + ν^{−1}M⁴∫₀^t e^{C∫₀^s Z}` (`Z` = the `η`-norm sum) — Osgood-type, closing only on a horizon `~ ν/M⁴`: exactly the local theory. The loop is genuinely supercritical; breaking it *is* the open content — no candidate below secretly proves itself.

## §2 — The weakest function-space requirement (derivation, not choice)

- The Grönwall route of C-P2 needs precisely `𝔅_{p₀}, 𝔅_{p₁}` for one pair `2 < p₀ < 3 < p₁` (the `p₀ > 2` floor is forced by the Hardy datum entry — the `p = 2` endpoint fails logarithmically; the `p₁ > 3` floor by the `L^{3,1}` interpolation feeding (L*)). The quartic power and `L¹_t` structure are forced by the dissipation absorption (`q²` in `L²_t L^{p}` ⟺ `q ∈ L⁴_t L^{2p}`).
- Duhamel/heat-smoothing variants (negative-Sobolev source classes, trading time- against space-integrability) shuffle norms **along the same scaling line** — for the `∇u`-order quantity `q`, every closable budget sits at supercriticality gap `2 − (2/q_t + 3/p_x) ≈ 1`, the parent head's own class — and buy no scaling weakening [D]. The scale-critical line (`= 2`) is unreachable by this mechanism.
- **Known unconditional input** [D]: the energy identity gives `∫₀^T‖q‖²_{L²}dt ≤ M²/(2ν)` for free (`\|∇(u_θe_θ)\|² ≥ u_θ²/r² = q²`) — this covers part of the low-exponent side by interpolation but cannot reach any `𝔅_p` alone.

## §3 — Candidate heads, counterexample-first (filters: (i) ball-known? (ii) energy-known? (iii) battery polarity (frozen `S_blob`/Type-I/Tao/snapshots)? (iv) rephrase of axisym-with-swirl regularity?)

| ID | Head (norm-uniform `∃Q₀(ν,T,M)` form) | (i) | (ii) | (iii) | (iv) | Verdict |
|---|---|---|---|---|---|---|
| R-1 | `sup_t‖q‖_{L∞} ≤ Q₀` | at `t=0` yes (`C_emb M`); trajectory: NO (content) | no | `S_blob`: `q ~ Γ₀τ^{−2β}` at the swirl radius ⟹ violated ✓; Type-I ✓; snapshots guard ✓ | near-known adjacency (the CFZ `r^d u_θ` family sits at `0 ≤ d < 1`; `d = −1` is outside it, but sup-form `q`-criteria may exist — V-12) | admissible, **not minimal** (strongest of the roster; `L∞` demanded where §2 shows a budget suffices) |
| R-2 | `sup_t‖q‖_{L^s} ≤ Q₀`, one fixed `s > 6` | yes at `t=0` (`C_sM`) | no | violated by `S_blob` (`‖q‖_s ~ Γ₀τ^{−2β+3β/s}`) ✓ | same V-12 note | admissible, not minimal (sup-in-time stronger than the budget) |
| **R-3** | **the budget head: `‖q‖_{L⁴_t(L^{s₀}∩L^{s₁})} ≤ Q₀`, fixed `4 < s₀ < 6 < s₁` (canonical `(s₀,s₁) = (5,8)`)** — supplies `𝔅_{p₀}` (`2p₀ = s₀`) and `𝔅_{p₁}` (`2p₁ = s₁ ⟹ p₁ = 4 ∈ (3,6]`) directly | yes at `t=0` per member; per-horizon finiteness automatic for smooth solutions — content = uniformity (parent-head profile) | no (energy gives only `L²_tL²`; the gap **is** the head) | `S_blob`: `∫‖q‖⁴_{s}dt ~ Γ₀⁴∫τ^{4β(3/s−2)}dτ` diverges for all `β > 3/(4(2s−3)/s)`… numerically: violated class-wide on the window `β ∈ (α,γ) ⊂ (1/3,1)` for both components ✓; Type-I at rate `(T−t)^{−13/4}`-type ✓; Tao averaged: no axisym `q`-structure — the C-3 bar transfers at method level (the closure consumes exact axisym divergence structure + (L*), none averaging-stable) ✓; `u_τ`/`𝒱`: solutions-only guard ✓ | logical collapse acknowledged (§5); attack surface distinct: one scalar component-quantity (swirl per axis distance) in a mixed norm, outside the known CFZ `d`-range, strictly above the energy-given `L²_tL²`, at gap-1 supercriticality — not a norm restatement of regularity; V-12 targeted prior-art check named | **SELECTED** (weakest through the mechanism) |
| R-4 | negative-Sobolev/Duhamel variants (`q² ∈ L²_tH^{−1}`-type and smoothing-shifted cousins) | — | — | same line | — | folded into R-3 by §2 (same scaling line; the `p₀ > 2` datum floor blocks the pure-`L²` member); recorded as norm-shuffles, not weakenings |
| R-5 | drift head `∫₀^T A dt ≤ Q₀` (i.e. `u_r/r ∈ L¹_tL∞`) | at `t=0` n/a (time-integrated) | no | violated by `S_blob` (forced `A ~ ν^{−1}τ^{α−γ}` — the frozen forced-amplitude lemma) ✓ | **HIGH rephrase risk**: this is the loop's *output* assumed, and `u_r/r`-criteria of this shape are plausibly published (KPZ-adjacent; V-12) | admissible fallback, ranked below R-3 (less source-local; consumes the conclusion of C-P3 rather than restoring C-P2) |

## §4 — THE SELECTED MINIMAL SOURCE-CONTROL THEOREM

**[SUPERSEDED (eleventh session, `HSEL_V12_PRIMARY_AUDIT_2026-09-02.md`): the V-12 audit found T-SRC as printed below to be strictly DOMINATED by a published no-smallness criterion (Li–Pan, DCDS 42 (2022), Cond. 1.1 at s = 1: `3/p + 2/q ≤ 2`, `p > 3/2`, finiteness suffices). The operative head is the re-based critical-line budget T-SRC′ = `‖u_θ/r‖_{L⁴_tL²_x} ≤ Q₀(ν,T,M)`, whose bridge to regularity is the published theorem (Arrows S2–S4 below are replaced wholesale; the u_r/r arrow S4 as printed is also a literature GAP — retired). Read this section through the V-12 record.]**

**T-SRC (norm-uniform form; OPEN — never asserted):**

> ∀ν>0, ∀T<∞, ∀M<∞: ∃Q₀(ν,T,M) < ∞ such that every certified solution from every admissible **axisymmetric** Schwartz datum with `‖u0‖ ≤ M` satisfies, on every certified horizon `T′ ≤ T`:
> **`‖u_θ/r‖_{L⁴_t(L⁵_x ∩ L⁸_x)([0,T′]×ℝ³)} ≤ Q₀`.**
>
> (Family note: any fixed pair `4 < s₀ < 6 < s₁` works; the family weakens as `s₁ ↓ 6⁺`; `(5,8)` is the canonical falsification target. `q = Γ/r²`: this is a time-integrated Γ-depletion-flavored statement — Γ must deplete faster than `r²` near the axis in the `L⁴_tL^s` sense.)

**Dependency chain (every arrow's status named):**

```
[T-SRC]  q ∈ L⁴_t(L⁵∩L⁸) with Q₀(ν,T,M)          (OPEN — the new research head)
   │   + energy budget ∫‖q‖²_{L²}dt ≤ M²/(2ν)      [KNOWN: dissipation ≥ ∫ u_θ²/r²; paper]
   ▼ Arrow S1 [D]: 𝔅_{p₀}, 𝔅_{p₁} for (p₀,p₁) = (5/2, 4) — directly from the head's two components
   ▼ Arrow S2 [D, §1 C-P2]: inhomogeneous η-estimate (divergence-form source + dissipation absorption)
       ⟹ sup_{t≤T′} ‖η(t)‖_{L^{p₀}∩L^{p₁}} ≤ C(ν,T,M,Q₀)      [C-P2 RESTORED; C-P1 unchanged]
   ▼ Arrow S3 [V-P: AHK Prop 4.1(i)]: sup_t ‖u_r/r‖_∞ ≤ C′(ν,T,M,Q₀)   [C-P3 unchanged]
   ▼ Arrow S4 [KNOWN-class with debt V-12, else D-standard assembly]:
       A-bounded ⟹ q-norms exp-bounded ⟹ swirl/vorticity bookkeeping ⟹ sup_t‖u‖_{H³} ≤ C(ν,T,M,Q₀)
   ▼ SEL-2 (proved in Lean)
[H-SEL^nu restricted to the axisymmetric sub-ball]   — extends the S-7 no-swirl validation to full
       axisymmetry; thence (EB-1 + integration) N0|_axisym and axisym-class continuation.
       The GENERAL-class head H-SEL^nu remains OPEN and is NOT claimed.
```

**Falsification semantics (EQ-4/EQ-5 analogues [D]).** Norm-uniform T-SRC is falsified by a fixed-`(ν,T,M)` axisym family with the budget diverging — every member possibly smooth; such a refutation would be a Clay- and axisym-regularity-neutral non-uniformity theorem. A *single-trajectory* budget divergence toward a bounded horizon is (via the chain, modulo S4) an axisym blow-up signature: any frozen-window candidate singularity **must** diverge the budget at the §3 rates — correct two-sided polarity, and a cheap scalar observable for the numerical lane.

**Cross-links (recorded, C0-clean).** (a) The zeroth-order coefficient of the `q`-equation is `−2u_r/r`, and S3's output bounds exactly the quantity the Γ-OSC record §5.3(iii) named as the structural unknown ("no frozen row signs `u_r`") — this route *bounds* it rather than signing it. (b) `q = Γ/r²` makes T-SRC a sufficient-condition cousin of (Γ-DEP)-type depletion statements — **proposal-level adjacency only**: nothing here consumes D5-structure or asserts any parked-branch object; no un-park trigger fires (no theorem is proved). (c) FC-086/C-3: the closure consumes exact axisym divergence structure + the kinematic (L*) — none of it averaging-stable; the method bar is respected by construction.

**Debts.** **V-12 (load-bearing for Arrow S4 and for the rephrase filter; discharge before any consumption or proof commissioning):** targeted first-hand check of (a) published `u_θ/r`-integrability and `u_r/r ∈ L¹_tL∞`-type criteria for axisym-with-swirl NS (candidates: Chen–Fang–Zhang DCDS 37 (2017) — partially in-corpus; Kubica–Pokorný–Zajączkowski arXiv:1206.4567 — in-corpus at [V?]; Hou–Li CPAM 61 (2008); P. Zhang–T. Zhang; Wei; Lei–Zhang), fixing whether Arrow S4 is verbatim-known and whether any published criterion already coincides with or dominates T-SRC (which would demote it per the head-reduction discipline); (b) the sign convention of the `η`-source (cosmetic). The `(q,η)` reformulation itself is Hou–Li-standard [H].

## §5 — Claim boundary

RECORD-ONLY; no Lean edit; no numerics; no proof search on H-SEL^nu, on T-SRC, or on N0 — §1–§2's derivations are mechanism-decomposition and weakest-requirement identification (the commissioned analysis), with the Osgood non-closure check confirming nothing open was accidentally proved. **Nothing here asserts, approaches, or implies a resolution of the Navier–Stokes Millennium problem, or of axisymmetric-with-swirl global regularity, in either direction.** The logical-collapse caveat applies to T-SRC as to every admissible head: universally proved, it would imply axisym-class regularity through the chain — its selection is justified on attack-surface grounds (one scalar component-quantity, a time-integrated budget, outside the known criterion families, with a cheap falsification observable), not on any claim of easiness. C0: a selection, not a uniqueness claim — R-5 is the recorded fallback, and the `(s₀,s₁)` family is printed. Commissioning anything downstream (V-12 discharge, P-2 retargeted probe now aimable at the budget observable, or any proof work) is a user act.
