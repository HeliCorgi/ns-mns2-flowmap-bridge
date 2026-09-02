# HSEL_S7_UNIFORMITY_DECISION — 2026-09-02 — the S-7 axisymmetric-no-swirl uniformity decision: V-11 discharged at primary level; the D₀-dependence is a PROOF ARTIFACT; VERDICT: UNIFORM-BOUND — sup_{t≤T} Q₅ ≤ C(ν,T,M) on the no-swirl sub-ball; the S-7 seed is CLOSED (RECORD-ONLY)

**Repo:** `c:/Users/corgi/Downloads/ns-mns2-flowmap-bridge` · **Status: RECORD-ONLY.** No Lean file touched; no numerics; nothing frozen moved. Lean baseline unchanged (8775-job gate).

**Commissioning provenance.** User instruction, 2026-09-02 (ninth session): execute the S-7 uniformity decision — (i) discharge **V-11** first-hand, tracking the quantitative constant dependence in the Ladyzhenskaya / Ukhovskii–Yudovich-type global regularity proofs; (ii) decide whether, at fixed `(ν,T,M)` for axisymmetric no-swirl Schwartz data with `‖u0‖_{H³} ≤ M`, the bound `sup_{t≤T} ‖∇u(t)‖_∞/(1+‖∇u(t)‖₂²) ≤ C(ν,T,M)` is actually derivable from existing proofs; (iii) distinguish whether dependence on ball-non-uniform auxiliary quantities like `D₀ = ‖ω₀/r‖_∞` is a proof artifact or essential; (iv) check whether `D₀^{(k)} → ∞` can be made to force `Q₅` growth by an analytic lower bound. Verdict ∈ {UNIFORM-BOUND / COUNTERFAMILY / UNDERDETERMINED}. No numerics, no Lean change.

**Method.** Two parallel first-hand literature lanes (classical originals + the key-lemma / measure-data modern theory) + main-loop mathematical adjudication; every load-bearing logical direction re-checked; new derivation steps marked [D] and kept at the standard-known-math level. Verification levels: [V-P] primary full text; [V-adj] faithful full-text secondary (original inaccessible, so noted); [V-abs] abstract; [D] derived in this record. Extracted source texts (including the full 23-page Ladyzhenskaya 1968 scan) are preserved in the session scratchpad, paths in the lane reports.

Notation: `η = ω_θ/r`; `D₀ = ‖η₀‖_{L∞}`; `Q₅(t) = ‖∇u(t)‖_∞/(1+‖∇u(t)‖₂²)`; norms 3D-Lebesgue unless flagged.

---

## §1 — V-11 discharge: what the classical proofs actually consume

| Source | Level | Constant-dependence finding |
|---|---|---|
| **Ladyzhenskaya, Zap. Nauchn. Sem. LOMI 7 (1968) 155–177** (Russian original, all 23 pages read) | **[V-P]** | **`‖ω₀/r‖_{L∞}` appears NOWHERE in the paper.** Data hypotheses (45)–(46): finite energy + finite enstrophy + `ω₀/r ∈ L²` (+ force integrals incl. `f/r ∈ L²_tL²`). The general-`Φ` relation (17) is the earliest citable source of the whole `L^p(η)` family; the single point where an `η`-norm feeds the nonlinearity is the stretching estimate (33), consuming the **propagated `L²` norm** of `η` (from (23)/(25)); enstrophy bound (38); Теорема 2 (p. 175) closes global solvability on exactly this data class |
| **Leonardi–Málek–Nečas–Pokorný, Z. Anal. Anwendungen 18 (1999) 639–649** | **[V-P]** | Theorem 1: global regularity for **axisym `v₀ ∈ W^{2,2}`, no `ω₀/r` hypothesis at all**; key bounds (6)–(7) with "`C(v₀,f)` … depending on `‖v₀‖_{2,2}` and `∫‖f‖_{1,2}`" — `‖ω₀/r‖₂` absorbed into `‖v₀‖_{H²}` by Hardy (their Lemmas 3–5); closing Remark: the `p → ∞` endpoint is invoked only for the **Euler** variant |
| Ukhovskii–Yudovich, PMM 32 (1968) (original paywalled/undigitized) | [V-adj ×4] | data class includes `η₀ ∈ L²∩L∞`; per Hmidi–Rousset (Ann. IHP 27 (2010), p. 1228 [V-P]) the U–Y result is "**uniform with respect to vanishing viscosity**" — the `L∞` endpoint serves the ν-uniform/Euler conclusion; no secondary claims the viscous case needs it (and the two [V-P] proofs above close without it). Internal U–Y bookkeeping remains unverified — flagged, non-load-bearing |
| Abidi, Bull. Sci. Math. 132 (2008) (via the author's HDR) | [V-adj] | global regularity for axisym `u0 ∈ H^{1/2}` — a class where `D₀ = ∞` generically: no bound in it can depend on `D₀` |
| **Abidi–Hmidi–Keraani, Math. Ann. 347 (2010), Prop 4.1(i)** | **[V-P]** | the lemma **(L*)**: `‖u^r/r‖_{L∞} ≲ ‖ω/r‖_{L^{3,1}(ℝ³)}` — static Biot–Savart estimate (Shirota–Yanagisawa pointwise kernel [V-adj via AHK] + O'Neil `L^{3/2,∞} ⋆ L^{3,1} → L^∞`), 3D Lebesgue convention, scale-consistent (`λ²` both sides). Restated with the same citation in Gallay–Šverák, Confluentes Math. 7 (2015), Rem. 2.7 (33) [V-P] |
| Hmidi–Rousset (2010), p. 1228 | [V-P] | verbatim: `∂_tΠ + v·∇Π − (Δ+(2/r)∂_r)Π = 0` "from which we get that for all `p ∈ [1,∞]`, `‖Π(t)‖_{L^p} ≤ ‖Π₀‖_{L^p}`" — the citable `L^p` monotonicity |
| Chen–Fang–Zhang, DCDS 37 (2017), Lem. 2.8 | [V-P] | CZ family `‖∇̃(u^r/r)‖_q ≤ C(q)‖ω^θ/r‖_q`, `1<q<∞` (3D representation (2.2)) |
| **Feng–Šverák, ARMA 215 (2015)** (vortex-ring data `ω₀ = κδ_γ`) and **Gallay–Šverák (2015; Ann. Sci. ÉNS 2019)** (filament data) | [V-P] | the entire global theory runs on **measure-level** norms (`‖ω_θ‖_{L¹(drdz)}`, `Γ/ν`), with `‖η(t)‖_∞` **regenerated** at positive times by viscous Nash-type smoothing (`≤ C₄M/(t√(νt))`, GŠ 2019 Lem. 2.2); `D₀` of the data is infinite and enters nowhere |

**§2 — Artifact ruling (commissioned question (iii)).** **The `D₀`-dependence is a PROOF ARTIFACT of one classical presentation (the U–Y data class), not essential to viscous global regularity.** Verified at primary level twice over: Ladyzhenskaya's own 1968 proof and LMNP's 1999 reproof close the full viscous chain from `‖v₀‖_{H²}`-controlled quantities only; the measure-data theory (FS/GŠ) shows the `L∞` level is not even needed as data information — viscosity regenerates it. Where `D₀` genuinely lives: the ν-uniform / Euler endpoint (`p = ∞` of the `L^p` family), irrelevant at fixed `ν > 0`.

---

## §3 — The uniform bound is derivable (commissioned question (ii))

**Route A (primary route — rests only on [V-P] sources + standard steps).**
1. `‖u0‖_{H³} ≤ M ⟹ ‖u0‖_{H²} ≤ M`; LMNP Theorem 1 chain [V-P] gives `sup_{t≤T}‖u(t)‖_{H²} ≤ K₁(ν,T,M)` and `∫₀^T‖u‖²_{H³}dt ≤ K₂(ν,T,M)` (their (6)–(7) constants are explicitly `‖v₀‖_{2,2}`-only; the `H²`-level continuation is the same chain [D-standard]).
2. One ladder rung [D-standard]: Agmon `‖∇u‖_∞ ≤ C‖u‖_{H²}^{1/2}‖u‖_{H³}^{1/2}` ⟹ `∫₀^T‖∇u‖_∞dt ≤ CK₁^{1/2}T^{3/4}K₂^{1/4}`; the `H³` energy ladder `d/dt‖u‖²_{H³} ≤ C‖∇u‖_∞‖u‖²_{H³}` (Kato–Ponce commutator — the same known-math family as the on-hold SEL-5, used on paper only) + Grönwall ⟹ `sup_{t≤T}‖u(t)‖_{H³} ≤ M·exp(CK₁^{1/2}T^{3/4}K₂^{1/4}) =: C₃(ν,T,M)`.
3. `Q₅(t) ≤ ‖∇u(t)‖_∞ ≤ C·C₃(ν,T,M)`. ∎

**Route B (corroborating route — sharper structure; one [V-adj] ingredient).**
1. **[D — the new step, resolving the artifact]:** Hardy data bound. For smooth axisym no-swirl `u` (so `ω_θ(0,z) = 0`), the weighted 1-D Hardy inequality (weight `r^a`, valid for `a < p−1`, here `a = 1`, `p > 2`) gives, sectionally in `r` and integrating in `z`: `‖ω/r‖_{L^p(ℝ³)} ≤ C_p‖∇ω‖_{L^p(ℝ³)}` for every `p ∈ (2,6]`; with `∇ω ∈ H¹(ℝ³) ↪ L^p`: **`‖ω₀/r‖_{L^{p₀}∩L^{p₁}} ≤ C M`** for fixed `2 < p₀ < 3 < p₁ ≤ 6`, and `L^{p₀}∩L^{p₁} ↪ L^{3,1}` (distribution-function split) ⟹ `‖η₀‖_{L^{3,1}} ≤ CM` — **the `H³` ball uniformly controls exactly the norm the modern theory propagates**.
2. `L^p` monotonicity [V-P: Hmidi–Rousset; earliest primary: Ladyzhenskaya (17)] at `p₀,p₁` ⟹ `‖η(t)‖_{L^{3,1}} ≤ CM` for all `t`.
3. (L*) [V-P: AHK Prop 4.1(i), static form] ⟹ `sup_{t≤T}‖u_r/r‖_∞ ≤ C₁M`.
4. Stretching Grönwall: `d/dt‖ω‖₂² + 2ν∫(|∇ω|²+ω²/r²) ≤ 2‖u_r/r‖_∞‖ω‖₂²` ⟹ `sup_t‖ω(t)‖₂² ≤ M²e^{2C₁MT}`, `∫‖∇ω‖² ≤ K/2ν` [D-classical].
5. Subcritical bootstrap to `H³` [KNOWN, Tail-A class] ⟹ the same conclusion, with the bonus uniform drift bound `‖u_r/r‖_{L^∞_{t,x}} ≤ C₁M`.

**Answer: YES — `sup_{t≤T} Q₅ ≤ C(ν,T,M)` on the axisymmetric no-swirl `M`-ball is derivable from existing proofs**, in Route A with nothing beyond the two [V-P] primaries and standard ladder steps, and in Route B modulo one [V-adj] kernel ingredient (Shirota–Yanagisawa Lemma 1, quoted verbatim inside AHK's [V-P] proof). The derivation was the commissioned determination; it incidentally constitutes a **norm-uniform validation of H-SEL^nu on the axisymmetric no-swirl sub-ball — the first large-data (no-smallness) subclass where the head provably holds.**

## §4 — The lower-bound half (commissioned question (iv))

**Closed, negatively.** No analytic lower bound forcing `Q₅` growth along the S-7 family can exist: it would contradict §3's uniform upper bound. `D₀^{(k)} → ∞` forces nothing — the degradation of the *classical U–Y presentation's* bounds under `D₀ → ∞` was precisely the artifact of §2; the flow contracts the right norm (`η` in `L^{3,1}`, ball-controlled by [D]-Hardy), and viscosity regenerates the `L∞` level (FS/GŠ [V-P]) rather than consuming it.

## §5 — VERDICT and consequences

**VERDICT: UNIFORM-BOUND.**

- **S-7 is CLOSED as a falsification seed** (supersedes the corresponding live-territory line of `HSEL_P3_FALSIFICATION_SEARCH_2026-09-02.md` §4: the C²-escape window is **shut in the axisymmetric no-swirl class**). V-11 is DISCHARGED (residues: U–Y internal bookkeeping [V-adj, non-load-bearing]; Shirota–Yanagisawa original [V-adj via AHK, load-bearing only for Route B]).
- **Mechanism note [D], recorded for the map:** the closure runs through a *monotone, scale-appropriate quantity* (`η` in `L^p`) that the `H³` ball controls via Hardy. This is exact-NS/geometric structure of precisely the kind C-3 demands (it does not survive Tao averaging), and it is exactly what the **with-swirl** class lacks (the swirl source `∂_z(Γ²/r⁴)` breaks `η`-monotonicity — consistent with the frozen research map's own Γ-lane findings). The general (non-axisym) class has no known analogue.
- **Falsification frontier after this decision:** (i) **axisymmetric WITH swirl** C²-escape-type families — not covered by this closure, still cheap to probe (axisymmetric reduction), and continuous with the lab's frozen research specialization; (ii) the generic non-axisym S-5 core. **P-2 retarget proposal:** priority family = axisym-with-swirl ball families driving swirl-weighted second-derivative quantities; secondary = S-3 reconnection geometry.
- **Ranking note (proposal only, no re-ranking commissioned):** the first large-data subclass validation is a genuine plausibility upgrade for H-SEL^nu (a future ranking pass may justify Plaus 3 → 4); it also demonstrates that the EQ-3 effectivity gap *can* close where a ball-controlled monotone quantity exists — a shape hint for any future proof-route selection.

## §6 — Claim boundary

RECORD-ONLY; no Lean edit, no numerics. **Nothing here asserts, approaches, or implies a resolution of the Navier–Stokes Millennium problem in either direction.** The uniform bound of §3 is a statement about the **axisymmetric no-swirl subclass only**, assembled from primary-verified known mathematics plus the [D]-steps printed above (the Hardy data bound and one ladder rung — both standard-level); the open head H-SEL^nu concerns the full certified class and is untouched in either direction. The §3 derivation was performed under this decision's explicit commission ("既存 proof から実際に導けるかを判定する"); no proof search on the open (general-class) head was started. C0: "first subclass where the head provably holds" is a description of the fetched-and-derived record, not an exclusivity or progress claim beyond it; the §5 retargeting items are proposals, commissioning them is a user act.
