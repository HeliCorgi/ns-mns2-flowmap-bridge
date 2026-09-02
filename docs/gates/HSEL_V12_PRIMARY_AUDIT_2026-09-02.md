# HSEL_V12_PRIMARY_AUDIT — 2026-09-02 — V-12 targeted primary-source audit: T-SRC as printed is DEMOTED (dominated by Li–Pan 2022); the head is RE-BASED to the critical-line swirl budget T-SRC′ with a VERIFIED published bridge; the u_r/r arrow S4 as printed is GAP-FOUND and moot (RECORD-ONLY)

**Repo:** `c:/Users/corgi/Downloads/ns-mns2-flowmap-bridge` · **Status: RECORD-ONLY.** No Lean file touched; no numerics; no proof search on T-SRC/T-SRC′/H-SEL/N0; nothing frozen moved. Lean baseline unchanged (8775-job gate).

**Commissioning provenance.** User instruction, 2026-09-02 (eleventh session): discharge V-12 at primary level — (1) does `sup_t‖u_r/r‖_∞ ≤ K` ⟹ norm-uniform `H³` follow as known mathematics? (2) is T-SRC (`q = u_θ/r ∈ L⁴_t(L⁵∩L⁸)`) contained in / equivalent to / dominated by an existing theorem? (3) verify the Hou–Li `(q,η)` equations, signs and coefficients; (4) if needed, reconstruct Arrow S4 as a shortest chain of known lemmas. Verdict ∈ {VERIFIED-BRIDGE / DEMOTED-AS-KNOWN-CRITERION / GAP-FOUND}. No Lean, no numerics, no T-SRC proof search.

**Method.** Two parallel first-hand lanes (`u_r/r`-criteria + S4 quantitativity; Hou–Li system + swirl-criteria + domination check), main-loop adjudication with normalization and logical-direction re-checks. Levels: [V-P] primary full text; [V-adj] faithful secondary; [V-abs] abstract only; [D] derived here.

---

## §1 — Answers to the four commissioned questions

**Q3 (Hou–Li system): VERIFIED [V-P].** arXiv:math/0608295 eqs. (96)–(98) (reformulated 3-D system in `ũ₁ = u_θ/r, ω̃₁ = ω_θ/r, ψ̃₁ = ψ/r` variables): zeroth-order term `+2(ψ̃₁)_z ũ₁ = −2(u_r/r)ũ₁` (via `v^r = −r(ψ̃₁)_z`); source `+(ũ₁²)_z`; viscous operator `∂_r² + (3/r)∂_r + ∂_z²` in all three equations; Biot–Savart `v^r = −r(ψ̃₁)_z, v^z = 2ψ̃₁ + r(ψ̃₁)_r`. Exactly the algebra the route-selection record used; sign conventions fixed (source coefficient +1 on `(q²)_z`). Caveat: the arXiv version's variables carry the cutoff decomposition; the CPAM print (61 (2008) 661–697) is paywalled [V-abs for its numbering].

**Q2 (T-SRC containment): DOMINATED — the decisive find [V-P].** **Li–Pan, DCDS 42 (2022), arXiv:2011.03146, Theorem 1.3 / Condition 1.1** (axisymmetric MHD–Boussinesq with the magnetic/density fields allowed ≡ 0, data `H^m, m ≥ 3`): for **any `s ≥ 0`**, the solution extends past `T*` if

> `∫₀^{T*} ‖u^θ/r^s‖_{L^p}^{q} dt < ∞`, with `3/p + 2/q ≤ 1+s`, `3/(1+s) < p ≤ ∞` — **no smallness; finiteness suffices**.

At `s = 1` this is literally a `q = u_θ/r` criterion with the admissible region `3/p + 2/q ≤ 2`, `p > 3/2`. T-SRC as printed (`L⁴_t(L⁵∩L⁸)`, criticality `2/4+3/5 = 1.1`) sits **strictly inside this region with margin 0.9** — it is not a rephrase of any published criterion (the domination table of the lane report checked CFZ 2017 (`d ∈ [0,1)` only), Fang–Chen–Zhang 1802.08956 (`d = −1` anisotropic, preprint — also dominates), Neustupa–Pokorný 2001, Lei–Zhang FBC (smallness — incomparable), Lei–Zhang/Wei log-caps (incomparable), KPZ/Kubica (incomparable), small-swirl-datum results (different genre)), **but it is strictly stronger than a published no-smallness criterion needs — per the head-reduction discipline it cannot stand as the selected head.**

**Q1 (`sup_t‖u_r/r‖_∞ ⟹ H³` known?): NO — GAP-FOUND [V-P search, thorough].** No published criterion has `A(t) = ‖u_r/r‖_∞` (in `L^∞_t` or `L¹_t`) as hypothesis in any form. Closest relatives, all verified to exclude it: Kubica-II (arXiv:1206.4567 is the solo sequel, **not** KPZ-I) Theorem 1 — weighted Serrin on the **positive part** of `u_r`, near-axis only, with all three endpoints of the `u_r/r ∈ L¹_tL^∞` corner (`d = −1, w = 1, s = ∞`) excluded and an extra swirl-decay hypothesis; Neustupa–Pokorný Theorem 1 — unweighted Prodi–Serrin on `u_r` (negative part suffices, their Remark 2); Renclawowicz–Zajączkowski JMFM 21:51 (2019) — `∫∫ v_r²/r³` (an `L²_{t,x}` weighted version). Also verified: **no paper states an `H³` conclusion with constants `C(ν,T,M,K)`** — published conclusions stop at strong-solution/enstrophy level with unquantified classical bootstrap above (the only fully quantitative axisym regularity theorem found is Ożański–Palasek, hypothesis = weak-`L³`, different object). The published *toolkit* (CFZ Lemmas 2.7–2.8 elliptic transfers; the `(Φ,Γ) = (ω_r/r, ω_θ/r)` exponential Grönwall, recorded explicitly as Renclawowicz–Zajączkowski (2.15); the `−q∫(u_r/r)|u_θ|^q` identities in NP (3.1), Kreml–Pokorný, CFZ (3.19)) is quantitative at the enstrophy level and makes the S4 substitution *plausible new work* — but it is not citable mathematics. **Moot for the chain** (Q4).

**Q4 (shortest reconstruction): SUPERSEDED.** The shortest known-lemma bridge from a swirl budget to regularity is now the **single published theorem** [Li–Pan Thm 1.3, s = 1], replacing Arrows S2–S4 of the route record wholesale. The `u_r/r` route (R-5 fallback and the S4 arrow) is retired from the critical path. The zeroth-order `q`-Grönwall (item 7 of the lane report) is reconstructible from published identities but is no longer needed.

## §2 — VERDICT and the re-based head

**Composite verdict, each value attached to its object:**

- **T-SRC as printed (route record §4): DEMOTED-AS-KNOWN-CRITERION-DOMINATED** — retired; the route record is annotated.
- **Re-based head — T-SRC′ (the critical-line swirl budget), norm-uniform, OPEN:**

> ∀ν>0, ∀T<∞, ∀M<∞: ∃Q₀(ν,T,M) < ∞ such that every certified solution from every admissible **axisymmetric** Schwartz datum with `‖u0‖ ≤ M` satisfies, on every certified horizon T′ ≤ T:
> **`‖u_θ/r‖_{L⁴_t L²_x([0,T′]×ℝ³)} ≤ Q₀`.**
>
> Family note: any member of the critical line `3/p + 2/q_t = 2, p > 3/2` is admissible and scaling-equivalent; `(q_t,p) = (4,2)` is canonical because it upgrades **the exact quantity the energy identity already budgets**: the known free bound is `∫₀^T‖u_θ/r‖²_{L²}dt ≤ M²/(2ν)` (criticality 5/2), and T-SRC′ says the time-profile `h(t) = ‖u_θ/r(t)‖²_{L²}` lies in `L²(0,T)` — not just `L¹` — uniformly on the ball: **a no-temporal-concentration statement for the swirl-dissipation channel, exactly one half criticality unit above known unconditional mathematics** (vs the parent head's full unit).

- **Bridge for T-SRC′: VERIFIED-BRIDGE (qualitative layer)** — `T-SRC′ ⟹` (finiteness alone, per Li–Pan Thm 1.3 at the `≤`-included equality endpoint) no axisym blow-up on `[0,T]` ⟹ `H-SEL^ds|_axisym` (per-datum, by compact-horizon continuity as in EQ-4(a)). **Residue V-13 (named, load-bearing for the nu-layer only):** first-hand verification that (i) the `h ≡ 0, ρ ≡ 0` reduction clause is as read (pure NS included), (ii) the equality case of Condition 1.1 is covered as quoted, (iii) Li–Pan's proof is quantitative (a priori bounds in terms of the budget + data norms) — if (iii) fails, the nu-layer (`H-SEL^nu|_axisym`) needs a quantitative re-run of their chain with the published CFZ/RZ toolkit (bounded new work, not commissioned).

**Dependency chain (updated, replacing the route record's §4 chain):**

```
[T-SRC′]  ‖u_θ/r‖_{L⁴_tL²_x} ≤ Q₀(ν,T,M)      (OPEN — the re-based head; weaker than the retired T-SRC)
   ▼ Arrow L [V-P: Li–Pan DCDS 42 (2022), Thm 1.3, s = 1; residues V-13(i,ii)]
[per-datum axisym regularity on [0,T]] ⟹ H-SEL^ds|_axisym
   ▼ Arrow Q [V-13(iii), else bounded quantitative re-run on the published toolkit]
[norm-uniform H³ on the axisym ball] ⟹ (SEL-2) H-SEL^nu|_axisym — extends the S-7 validation
   ▼ (EB-1 + integration)  N0|_axisym; the GENERAL-class head stays OPEN and unclaimed.
```

## §3 — Battery notes for T-SRC′ ([D]; solutions-only guard throughout)

- **Type-I:** `‖q‖₂² ~ (T−t)^{−1/2}` ⟹ `∫‖q‖₂⁴dt` **log-diverges** — violated at exactly logarithmic rate, consistent with T-SRC′ being exactly scale-critical.
- **Frozen `S_blob` (profile vocabulary):** the declared swirl subcore (`Γ ~ Γ₀(r/τ^β)²` on `r ≲ τ^β`) contributes `‖q‖₂² ~ Γ₀²τ^{−β}`, so the subcore channel diverges the budget **iff `β_v ≥ 1/2`**; the core channel's envelope bound (`q ≤ ‖u‖_∞/r` down to the member's regularity scale) *permits* divergence at all window exponents but does not force it. Violation of T-SRC′ by any actual blow-up is **logically forced** through the verified bridge; the profile arithmetic only shows *where* it can live — **the violation localization ties directly to the frozen middle-limb parameter `β_v`** (a feature: the head connects to the map's open question, not a defect).
- **Proposal P-LP (record-only; adoption = future freeze review; C0-clean):** Li–Pan's `s = 1` criterion is NEW to the frozen corpus (the kill-table's K9/L-AX4 family stops at `d ≥ 0`). At solutions level it ties: *any* frozen-window blow-up solution must carry an infinite critical swirl budget through some channel; on the printed profile vocabulary the subcore channel does so iff `β_v ≥ 1/2`. **No class-wide kill is established** (the core envelope permits budget divergence for all window members — checked [D]); no map object moves; routed as a watch/freeze-review proposal only. Un-park triggers: none fire (no theorem proved, nothing consumed).
- **Watch routing (proposal):** Shahmurov arXiv:2605.01875 / 2605.09797 (May 2026, large-data axisym-with-swirl global-regularity claims; same author as the triaged D-3 = arXiv:2606.07869, load-bearing gaps confirmed there) — route to the standing literature watch register alongside W-1–W-4; correctness not established; consumed by nothing; no CAP fire.

## §4 — Debt ledger update

- **V-12: DISCHARGED** (this record; both lanes primary-level; the Neustupa–Pokorný and Kubica-II texts, CFZ, Hou–Li arXiv, Lei–Zhang, Wei, Li–Pan ×2, Fang–Chen–Zhang, RZ 2019, Q.S. Zhang survey all [V-P]; Chae–Lee via two concordant [V-adj]; KPZ-I proper inaccessible [V-abs] — non-load-bearing).
- **NEW V-13** (Li–Pan reduction clause + equality endpoint + proof quantitativity — load-bearing for the nu-layer Arrow Q; precedes any nu-consumption or proof commissioning).
- Non-load-bearing residues: KPZ-I exact indices; Zujin Zhang CAMWA 76 (2018) and the 2023 JMAA mixed-Lorentz paper (both access-blocked [V-abs]; unlikely to bear on the `(4,2)` member, flagged).

## §5 — Claim boundary

RECORD-ONLY; no Lean edit; no numerics; no proof search on any open head. **Nothing here asserts, approaches, or implies a resolution of the Navier–Stokes Millennium problem, or of axisymmetric-with-swirl global regularity, in either direction.** T-SRC′ is OPEN; the logical-collapse caveat applies (universally proved, it implies axisym-class regularity through the published bridge); its selection value is positional — one half criticality unit above the free energy budget, with a published no-smallness bridge, a single-scalar falsification observable, and a violation-localization tie to the frozen `β_v` question. The §3 P-LP and watch items are proposals; adopting them, discharging V-13, or commissioning anything downstream is a user act. C0 discipline throughout; the demotion of the printed T-SRC follows the same standard applied to every prior head (EH-1 precedent: a re-basing to the weakest closable member, selection-preserving in spirit, statement-improving in fact).
