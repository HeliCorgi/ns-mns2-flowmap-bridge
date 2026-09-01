# TSEL_HEAD_REDUCTION_AUDIT — 2026-09-02 — sufficient-estimate reduction of the T-SEL head N0: 13 adjudicated objects, counterexample-first, one selected head (RECORD-ONLY)

**Repo:** `c:/Users/corgi/Downloads/ns-mns2-flowmap-bridge` · **Status: RECORD-ONLY.** No Lean file is touched; no frozen verdict, frontier, or park changes; every map consequence is a proposal. The Lean verification baseline remains the full pinned gate PASS at 8775 jobs (commits `0565237`/`bb1c473`/`b839af0`).

> **CORRECTION NOTICE (2026-09-02, fifth session, commissioned one-shot — §9).**
> The H-SEL statement correction audit found and repaired two defects in this
> record: **EH-1** — the closable-exponent print was wrong: `p = 2`, not
> `p = 4/3`, is the exact endpoint of the power family closable by the energy
> equality alone; the selected head is restated with `‖∇U‖₂²` on the right
> (a strictly weaker, hence better, head; the old `4/3` form implies it).
> **EH-2** — the "reverse Gagliardo–Nirenberg" reading (a claimed bound on
> `‖∇³U‖₂`) inverted an inequality and is **retracted**. Read §3 (HR-5 row),
> §5, and §8 through §9; battery and ranking are re-run there (all verdicts
> and the selection survive; several printed rates and one superlative are
> superseded). Original text below is annotated, not silently rewritten.

**Commissioning provenance.** Executed under the user's 2026-09-02 (fourth-session) instruction, which does three things at once:

1. **SEL-3/SEL-5 Lean implementation is put ON HOLD** — carried as *formalization debt on known mathematics*; the Prop `R3TSelH3Ladder` (and the SEL-3 clause `R3TSelInteriorSobolevSmoothing`) is **not** to be treated as a research-unknown. Its mathematical content is the standard 1984 energy ladder (audit SS-6 items 3/5); the fixed mollified-energy discharge route and checked dead ends of `docs/formal/TSEL_BRIDGE_DISCHARGE_2026-09-02.md` §4 stand unchanged for whenever the debt is paid. No Lean edit is made by this session.
2. **No direct proof search on the head N0** (`R3TSelGradientBound` / `R3TSelHead`) — unchanged from the standing commission boundary.
3. **Execute the T-SEL head reduction audit**: generate several sufficient estimates `R` with `R ⟹ ∫₀^{T′}‖∇U‖_{L∞}dt < ∞` (per-datum, per-horizon, in N0's own ∃-constant form) that are more local, more quantitative, and independently falsifiable relative to N0; ban restatements of "H³ bounded", "no blow-up", "∫‖∇U‖_∞ < ∞", and the bare Serrin/BKM criteria; for each candidate state the known-theorem basis, the scaling, and the derivation chain to N0; run counterexample search **before** any proof search; classify **COUNTEREXAMPLE / SURVIVES / EQUIVALENT-TO-KNOWN-HARD-PROBLEM**; rank survivors by leverage × plausibility × distance-from-known-theory × Lean-connectability and select exactly one as the next research theorem.

**Method.** Single-session sequential offices with an explicit adversarial re-check (§5): admission/ban fixing → fence-row sweep of the norm axis (§2) → candidate generation in three structural lanes (§3) → the standing counterexample battery (§4: scaling; frozen-B2/`S_blob` arithmetic with the forced-amplitude vocabulary of `GAMMA_OSC_FEASIBILITY_2026-09-02.md`; Type-I profiles; multi-scale/stacked-cell families; the standing snapshots `u_τ`/`𝒱` under the solutions-only guard; FC-086 Tao-averaged bearing; known-smooth-flow stress) → ranking and selection (§5). C0 language discipline throughout (every selection is a selection, never a uniqueness claim). Claims tagged [H] (from-memory literature, verification debt named), [V] (verified in-corpus this pass), [D] (derived in this record), [C] (conditional). The numerical failcase registry (`failcases/mns2-v2.11–14.md`) was checked: those entries concern the MNS2 numerical bridge and bear on nothing here; the load-bearing registry items are FC-086 (Tao averaged-NS obstruction) and FC-087 (supercriticality gap), both already consumed by the Stage-9 audit.

---

## §1 — The target, and what "reduction" means

**N0, verbatim from `STAGE9_REVERSE_GAP_AUDIT_2026-09-02.md` SS-5** [V]:

> ∀ν>0, ∀ admissible Schwartz datum u0, ∀ finite T: ∃ G(T;ν,‖u0‖) < ∞ such that every certified solution on every certified horizon T′ ≤ T satisfies ∫₀^{T′} ‖∇U(s)‖_{L∞(ℝ³)} ds ≤ G(T), U = J⁻³∘u (decoded field).

**Admission criteria for a candidate head `R`** (fixed before generation):

- (A1) `R` is stated in N0's own per-datum ∃-constant form (constants may depend on `T, ν, ‖u0‖`; quantified over all certified solutions/horizons).
- (A2) `R ⟹ N0` by a derivation chain that is KNOWN mathematics, with every non-formalized step named as a debt. A candidate whose chain to N0 is itself OPEN is **inadmissible** (recorded in §2 where instructive).
- (A3) `R` is not a banned restatement (ban list above), and offers a genuinely different attack surface: more local in space/structure, and falsifiable by an observable that is not simply a norm of `∇U` again.

**The logical-collapse clarification [D], fixed before classification.** For any admissible `R`, the universal statement "`R` holds for the whole certified class" is *logically* inter-derivable with universal N0 modulo known mathematics: `R ⟹ N0 ⟹` global continuation `⟹` smoothness on compact horizons `⟹` (for every candidate below) `R` back again, with per-datum constants. So logical strength cannot be the discriminator — every admissible universal head is Clay-equivalent-or-harder for the certified class, exactly as N0 itself is. The commissioned classification therefore reads:

- **EQUIVALENT-TO-KNOWN-HARD-PROBLEM**: the statement is a reformulation of a *named* hard open problem (the ESS/critical-norm wall, the classical enstrophy problem, "no singular point") with no new locality, structure, or falsification observable.
- **SURVIVES**: no constructed certified violator; the statement's attack surface (proof structure consumed, refutation observable) is genuinely distinct from N0's and from every named wall.
- **COUNTEREXAMPLE**: a certified-class violator exists (none was found this pass; the fence rows of §2 fail on admission or equivalence, not on constructed violators).

---

## §2 — Fence rows: the norm axis collapses (recorded to bound the search space)

| ID | Object | Classification | Reason (condensed) |
|---|---|---|---|
| E-1 | `sup_t ‖U(t)‖_{H^s}`, any subcritical `s > 1/2` (representative: enstrophy `s = 1`) | **EQUIVALENT** | any subcritical sup-norm bound ⟹ regularity by the known Serrin-subcritical bootstrap ⟹ every other one; `s = 1` **is** the classical formulation of the regularity problem; `s = 3` is N1 restated (banned shape; cf. the banned L_e) |
| E-2 | critical-norm family: `sup_t‖U‖_{L³}` (= L_c), Serrin pairs (= L_d), pressure criteria (Berselli–Galdi [H]), critical Besov | **EQUIVALENT-TO-KNOWN-HARD-PROBLEM** | the recorded L_c/L_d walls; pressure reduces to the velocity walls by Calderón–Zygmund (`p ~ RᵢRⱼ(uᵢuⱼ)`) [D]; no locality gained |
| E-3 | uniform-scale CKN local smallness: ∃r₀ uniform with `r₀⁻¹∬_{Q_{r₀}}\|∇U\|² ≤ ε_{CKN}` everywhere | **EQUIVALENT** | CKN necessity: at a singular point the scaled quantity exceeds ε at **every** scale, so the statement is "no singular point" verbatim — the banned "no blow-up" restatement in local coordinates [D] |
| E-4 | log-relaxed N0: `∫₀^{T′}‖∇U‖_∞/(1+ln⁺(e+‖U‖_{H³}))dt ≤ G` | **EQUIVALENT** (to N0's own family) | strictly weaker integrand, but identical attack surface; known log-Grönwall crosses the gap (double-exponential `G`); zero locality gain — kept only as the calibration endpoint: any candidate offering less than this gains nothing |
| E-5 | whole-space Type-I cap `‖U(t)‖_∞ ≤ Q₀(T+1−t)^{−1/2}`, `Q₀` arbitrary | **INADMISSIBLE (A2)** | the bridge to N0 is OPEN in the general class — Type-I exclusion is a theorem only under axisymmetry (CSTY/KNSS; = L-AX3's lane); the small-`Q₀` version is admissible but collapses into E-3 (ε-regularity) |
| E-6 | `sup_t‖U(t)‖_{Ḃ^{−1}_{∞,∞}} ≤ Q₀`; Constantin–Iyer expected-stretching caps | **INADMISSIBLE (A2)** | bounded (non-small) `Ḃ^{−1}_{∞,∞}` has no known bridge to regularity (and norm-inflation ill-posedness lives there [H]); Constantin–Iyer is circular in the target quantity (recorded, SS-4 L_a R4) |

**Consequence [D].** Genuinely new heads cannot be norms of `U` or `∇U` at all: the subcritical axis is one equivalence class, the critical axis is the named walls, the supercritical axis has no bridge. The candidate lanes of §3 are therefore *structural*: geometric (direction, level-set shape), spectral (strain eigenvalue), and distributional (interpolation/intermittency shape) — each with a falsification observable that is not a norm of the field.

---

## §3 — Candidate table

All candidates are stated per-datum/per-horizon (A1): "∃ constants(T;ν,‖u0‖) s.t. every certified solution on every certified horizon T′ ≤ T satisfies …". `S_blob = {1/2 < γ < 1, max(1−γ, 2γ/3) ≤ α < γ, α > 2γ−1}` and the profile vocabulary are the frozen ones. Common chain tails (each step known mathematics; formalization status in brackets):

- **Tail-A (enstrophy tail):** `sup_t‖U‖_{H¹} ≤ C` ⟹ Serrin-subcritical pair `(∞,6)` via Sobolev ⟹ quantitative regularity + parabolic smoothing to `sup_t‖U‖_{H³}` [KNOWN; same debt class as the on-hold SEL-3] ⟹ SEL-2 (proved in Lean) ⟹ `Q ≤ T·C_emb·sup‖U‖_{H³}` ⟹ N0.
- **Tail-B (vorticity-sup tail):** `sup_t‖ω‖_{L∞} ≤ C` ⟹ `∫‖ω‖_∞ < ∞` ⟹ BKM log-inequality + log-Grönwall ⟹ `sup_t‖U‖_{H³}` double-exponential [KNOWN] ⟹ SEL-2 ⟹ N0.
- **Tail-C (direct energy tail):** energy equality for certified solutions `∫₀^{T′}‖∇U‖²_{L²}dt ≤ ‖U(0)‖²_{L²}/(2ν)` [KNOWN on paper; **Lean-absent — named debt EB-1**] + Hölder in time ⟹ N0 directly.

| ID | Head `R` (falsifiable form) | Known-theorem basis (`R ⟹ …`) | Scaling | Chain to N0 | Verdict |
|---|---|---|---|---|---|
| **HR-1** | **coherence head**: ∃ρ, M: `\|sin∠(ω(x,t),ω(y,t))\| ≤ ρ⁻¹\|x−y\|^{1/2}` whenever `\|ω(x,t)\|,\|ω(y,t)\| ≥ M` | Constantin–Fefferman, Indiana Univ. Math. J. 42 (1993) (Lipschitz form); Beirão da Veiga–Berselli, Diff. Int. Eq. 15 (2002) (β = 1/2 form) [H, debt V-1] ⟹ enstrophy control (geometric depletion of stretching, consumes ν) | `sin∠` scale-invariant; the modulus transforms `ρ⁻¹ ↦ ρ⁻¹λ^{1/2}` under `u_λ` — supercritical as a bare hypothesis, traded against Biot–Savart + dissipation inside the theorem | CF/BdVB ⟹ `sup‖ω‖_{L²}` ⟹ Tail-A | **SURVIVES** |
| **HR-2** | **middle-eigenvalue head**: `‖λ₂⁺(t)‖_{L^q_tL^p_x} ≤ Q₀` for one fixed pair `2/q+3/p = 2, p > 3/2` (`λ₂` = intermediate eigenvalue of `S = sym∇U`) | Neustupa–Penel (2001); Miller, ARMA 235 (2020) 99–139 [H, debt V-2] ⟹ enstrophy control | exactly critical for a `∇U`-order scalar | Miller ⟹ `sup‖ω‖_{L²}` ⟹ Tail-A | **SURVIVES** |
| **HR-3** | **sparseness head**: at every `t` with `‖ω(t)‖_∞` above a datum threshold, the super-level set `{\|ω(t)\| > c‖ω(t)‖_∞}` is 1-D δ-sparse at scale `κ‖ω(t)‖_∞^{−1/2}` (fixed `c, δ, κ`) | Grujić geometric-depletion framework; Bradshaw–Farhat–Grujić, ARMA 231 (2019) ("algebraic reduction of the scaling gap") [H, debt V-3] ⟹ `‖ω‖_∞` control | the sparseness scale `‖ω‖_∞^{−1/2}` is the parabolic self-similar scale — scale-invariant formulation | BFG ⟹ `sup‖ω‖_∞` ⟹ Tail-B | **SURVIVES** |
| **HR-4** | **vortex-line geometry head**: through every near-max vorticity point runs a line segment with controlled length, direction variation, and velocity divergence (Deng–Hou–Yu parameters) | Deng–Hou–Yu, CPDE 30 (2005) — stated for **Euler**; the NS transfer is an additional debt [H, debt V-4] | mixed (length parameters supercritical) | DHY(+NS transfer) ⟹ `‖ω‖_∞`-type control ⟹ Tail-B | **SURVIVES** (marginality + transfer debt; see §4) |
| **HR-5** | **reverse-interpolation (anti-intermittency) head**: `‖∇U(t)‖_{L∞} ≤ Q₀·(1 + ‖∇U(t)‖_{L²}^{4/3})` for all certified `t` | none needed beyond the energy equality: the head + the `L²_t` enstrophy budget close N0 by Hölder alone [D]; relation to known theory: a *reverse* Gagliardo–Nirenberg (by GN `‖∇U‖_∞ ≲ ‖∇U‖₂^{1/4}‖∇³U‖₂^{3/4}`, the head reads `‖∇³U‖₂ ≲ Q₀^{4/3}‖∇U‖₂^{13/9}` — a spectral-non-spreading/bounded-intermittency statement); Tao's averaged-NS blow-up (arXiv:1402.0290) is the template violator (§4); prior conditional-regularity literature on intermittency dimensions to be swept [H, debt V-5] | LHS scales `λ²`, RHS scales `λ^{2/3}`: deeply supercritical as a hypothesis — a strong structural restriction, which is exactly its content; the exponent 4/3 is the largest closable against the `L²`-in-time budget (any θ ≤ 4/3 admissible; 4/3 = weakest member) | **Tail-C** (2 arrows: EB-1 energy equality + Hölder; then the existing Lean N0→N3 assembly) | **SURVIVES** — **row corrected by §9**: endpoint `p = 2` (EH-1); the reverse-GN sentence in this row is RETRACTED (EH-2) |
| **HR-6** | **strain-integral head**: `∫₀^{T′}‖S(t)‖_{L∞}dt ≤ Q₀` | max principle on `D\|ω\|/Dt ≤ \|Sω\| + ν(…)`: `‖ω(t)‖_∞ ≤ ‖ω₀‖_∞ e^{∫‖S‖_∞}` [D, elementary]; strictly weaker hypothesis than N0 (symmetric part only; the antisymmetric-part analogue is L_b/BKM — banned as a candidate, so HR-6 is kept distinct only by its S-form) | exactly critical (same as N0) | max principle ⟹ `sup‖ω‖_∞` ⟹ Tail-B | **SURVIVES** (low novelty; ban-adjacent) |
| **HR-7** | **one-component head**: ∃ unit vector `e` (per solution): `‖U·e‖_{L^q_tL^p_x} ≤ Q₀` at a Cao–Titi/Chemin–Zhang-admissible index pair | Cao–Titi, Indiana Univ. Math. J. 57 (2008); Chemin–Zhang(-Zhang) critical-space refinements [H, debt V-6] | critical-to-subcritical per pair | one-component theorem ⟹ Tail-A | **SURVIVES** (no mechanism selects `e`; wall-class for the component) |

---

## §4 — Counterexample battery (run before any proof search)

Standing guard applied everywhere: `u_τ`/`𝒱` are snapshots/kinematic scans that solve no PDE — solutions-only heads are stressed, never rejected, by them; frozen-B2 members are hypothesized, none constructed; a candidate head **must** be violated by any blow-up-compatible scenario (else A2 would fail) — this is the *polarity check*, not a defect. FC-086 binds proof routes, not statements.

**HR-1 (coherence).**
- *Polarity vs `S_blob`* [D]: a coherent core of scale `τ^α` with O(1) direction swing (toroidal ω-geometry) forces `ρ⁻¹ ≥ c·τ^{−α/2}` → any B2-type member violates the head. Type-I self-similar profiles violate at rate `(T−t)^{−1/4}`. Correct polarity.
- *Smooth-flow stress*: antiparallel reconnection is `sin`-coherent (`sin π = 0` — the CF form treats antiparallel as aligned [D]); the genuine stress is orthogonal collision geometry, where the modulus grows but no certified violator is known; DNS robustly shows core alignment [H].
- *Multi-scale*: braided/interlocked filament tangles could grow `ρ⁻¹` without bound — no theorem either way; this is the open content ("no a priori coherence modulus exists", already recorded at SS-4 L_a R2 [V]).
- *FC-086*: geometric depletion does **not** survive Tao averaging — a proof of HR-1 must consume exact Biot–Savart structure; the statement is unbarred and the constraint is favorable (it points at exactly the structure class FC-086 demands). **SURVIVES.**

**HR-2 (λ₂⁺).**
- *Polarity*: by Miller's contrapositive, any blow-up diverges the critical `λ₂⁺` norm; in `S_blob` arithmetic, stretching-dominated cores carry `λ₂ ~ τ^{−(γ+α)}` on the core volume → divergence at a positive rate [D]. Correct polarity. Axisymmetric note [D]: `e_θ` is a strain eigendirection with eigenvalue `u_r/r`; for ω_θ-dominant cores the head's controlling object is the sign/size of `u_r/r` — precisely structure candidate (iii) of `GAMMA_OSC_FEASIBILITY_2026-09-02.md` §5.3 ("no frozen row signs `u_r`"). The cross-link is recorded: an HR-2 proof would have to control the exact quantity the Γ-lane audit named as unknown.
- *Smooth-flow stress*: DNS turbulence has positively-skewed `λ₂` (alignment of ω with the intermediate eigenvector) [H] — the head's critical norm is generically active, not small; plausibility of horizon-uniform bounds is the open content. **SURVIVES.**

**HR-3 (sparseness).**
- *Polarity vs `S_blob`* [D]: the sparseness scale is `‖ω‖_∞^{−1/2} ~ τ^{(γ+α)/2}`; the core scale is `τ^α`; since `α < γ` on all of `S_blob`, `τ^α ≫ τ^{(γ+α)/2}` — a solid blob core is maximally non-sparse at the sparseness scale. **HR-3 is the only head in the roster that kills B2-type scenarios by geometry rather than amplitude.** Type-I: core scale `(T−t)^{1/2}` **equals** the sparseness scale — exactly marginal, matching BFG's own "scaling gap" language.
- *Multi-scale near-miss* [D]: the stacked counter-rotating cell family (EP-7 vocabulary) is locally sheet-like; thin shells of thickness below the sparseness scale are 1-D sparse in the normal direction — a sheet-organized concentration could *satisfy* HR-3 while concentrating. Since the family solves no PDE this rejects nothing, but it maps HR-3's blind spot precisely: sheet-like blow-up scenarios are the surviving falsification territory.
- *FC-086*: level-set geometry does not survive averaging — same favorable constraint as HR-1. **SURVIVES.**

**HR-4 (DHY geometry).**
- The recorded weakness stands [V, SS-4 L_b R1]: the hypothesis parameters are what Hou-type candidates *marginally* satisfy — polarity is muddy by construction; and the theorem basis is Euler-form, so the NS chain carries a transfer debt on top. No certified violator; survives, weakly. **SURVIVES** (lowest confidence in the roster).

**HR-5 (reverse interpolation).** **[Rates in this block are for the original `4/3` form; the corrected `p = 2` rates are in §9.3 — verdicts unchanged.]**
- *Polarity vs `S_blob`* [D, adversarially re-checked §5]: core arithmetic gives `‖∇U‖_∞ ~ τ^{−(γ+α)}`, `‖∇U‖²_{L²} ~ τ^{α−2γ}` (core-dominated: `α − 2γ < 0`, so any O(1) background enstrophy is subdominant), hence the head demands `γ ≥ 5α`; the frozen window has `α ≥ 2γ/3 > γ/5` — **every `S_blob` member violates HR-5, class-wide, at rate `τ^{−(5α−γ)/3}`**. Type-I profiles violate at rate `(T−t)^{−2/3}`. Correct polarity, the sharpest margin in the roster.
- *Frequency-concentration transient* [D]: a single-shell datum at frequency `N` has ratio `~ N^{7/6}`, but `‖u0‖_{H³} ~ N³` absorbs it — the per-datum constant survives kinematic shell data; the open content is growth *along* the flow beyond every function of the datum.
- *FC-086, sharpened to a feature* [D]: Tao's averaged-NS blow-up is frequency-shell-concentrated and violates the head-analogue at rate `N^{7/6}` — so (i) no averaging paradox arises, and (ii) since the averaged model satisfies the full energy structure yet violates the head, **any proof of HR-5 must consume exact-NS structure beyond the energy identity** — the FC-086 bar is automatically respected and precisely located.
- *Smooth-flow stress* [D, heuristic — recorded as such]: at fixed ν, Kolmogorov power counting gives `‖∇U‖_∞/‖∇U‖₂^{4/3} ~ (ε/ν)^{−1/6}·(intermittency corrections)` — the leading power is *favorable* (more intense dissipation helps the head); the corrections are of unknown sign. No certified violator known; the head is also the cheapest object in the roster to measure in any dataset (one scalar ratio per time slice). **SURVIVES.**

**HR-6 (strain integral).** Same battery profile as N0/L_b (rate `τ^{−(γ+α)}`, divergence iff `γ+α ≥ 1` = K11 — every frozen member diverges it ✓); no locality gain; kept as the S-form boundary marker of the ban region. **SURVIVES** (low novelty).

**HR-7 (one component).** Polarity: in `S_blob` every velocity component of the poloidal core carries the critical divergence (forced-amplitude lemma [V]) — for axisymmetric-type concentration no direction `e` is good, so violation is forced ✓; for general scenarios the rotation freedom has no known selection mechanism, and for the chosen component the head is wall-class (E-2 family). **SURVIVES** (weakly; wall-adjacent).

---

## §5 — Ranking and the selected head

Axes per the commission, each 1–5: **leverage** (payoff if proved, incl. standalone mathematical value and program synergy) × **plausibility** (of the universal per-datum statement, given numerics/known theory) × **distance** (nearness-to-attackable from known theory, in either direction — proof or refutation) × **Lean-connectability** (economy of the `R ⟹ N0` bridge onto the existing proved SEL chain). C0: the product ranks attack surfaces of independently falsifiable open targets; it asserts neither provability nor exclusivity.

| # | Head | Lev | Plaus | Dist | Lean | Π | Notes |
|---|---|---|---|---|---|---|---|
| 1 | **HR-5** reverse interpolation | 5 | 3 | 2 | 4 | **120** | shortest bridge in the audit (Tail-C: EB-1 + Hölder — 2 arrows onto the proved Lean assembly); sharpest B2 polarity margin; cheapest falsification observable (one scalar ratio); proved-or-refuted, both outcomes informative |
| 2 | **HR-1** coherence | 5 | 3 | 2 | 2 | 60 | strongest literature/DNS support among geometric heads; 30-year-old open modulus; bridge = CF/BdVB formalization + Tail-A (heavy) |
| 3 | HR-3 sparseness | 5 | 3 | 3 | 1 | 45 | only head killing B2 by geometry; sheet-scenario blind spot mapped; bridge needs harmonic-measure machinery (far from repo assets) |
| 4 | HR-2 middle eigenvalue | 4 | 2 | 2 | 2 | 32 | clean modern theorem basis; DNS positive-λ₂ bias lowers plausibility; cross-links to the unsigned `u_r/r` unknown |
| 5 | HR-6 strain integral | 3 | 2 | 2 | 2 | 24 | tie broken over HR-7: single canonical statement, elementary route | 
| 5 | HR-7 one component | 3 | 2 | 2 | 2 | 24 | no selection mechanism for `e`; wall-adjacent |
| 7 | HR-4 DHY geometry | 3 | 2 | 1 | 1 | 6 | Euler-transfer debt + recorded marginality |
| — | E-1…E-6 | — | — | — | — | — | fence rows; unranked by design |

### THE SINGLE SELECTED HEAD

**[Superseded by §9 (EH-1): the operative statement is the `p = 2` form printed there; the `4/3` form below implies it and is retained as the original print.]**

**H-SEL := HR-5 — the reverse-interpolation (anti-intermittency) head:**

> ∀ν>0, ∀ admissible Schwartz datum u0, ∀ finite T: ∃ Q₀(T;ν,‖u0‖) < ∞ such that every certified solution on every certified horizon T′ ≤ T satisfies, for all t ∈ [0,T′]:
> **‖∇U(t)‖_{L∞} ≤ Q₀ · (1 + ‖∇U(t)‖_{L²}^{4/3}).**

**Derivation chain to N0 (both arrows known mathematics):**

```
[H-SEL]  ‖∇U(t)‖_∞ ≤ Q₀(1 + ‖∇U(t)‖₂^{4/3})            (OPEN — the new research head)
   │
   ▼  Arrow α — energy equality for certified solutions [KNOWN, paper; Lean debt EB-1]:
      ∫₀^{T′} ‖∇U‖²_{L²} dt ≤ ‖U(0)‖²_{L²}/(2ν)
   ▼  Arrow β — Hölder in time (q = 3/2 on the 4/3-power) [KNOWN, trivial]:
      ∫₀^{T′} ‖∇U‖_∞ dt ≤ Q₀T + Q₀T^{1/3}(‖u0‖²_{L²,dec}/(2ν))^{2/3} =: G(T;ν,‖u0‖)
[N0]  — verbatim; thence the existing Lean assembly N0 → N1 → N2 → N3
      (currently conditional also on the on-hold known-math debts SEL-3/SEL-5).
```

**Adjudicator spot-verification (performed independently, this pass [D]):** (i) scaling recomputed — LHS `λ²` vs RHS `λ^{2/3}` under `u_λ`, so zoom families move the datum and manufacture no violator (the head is a structural restriction, not a norm bound); (ii) ban check — the head bounds no norm of `U`; it constrains the *shape* (spectral concentration/flatness) of `∇U`, and its falsification observable `Q₅(t) := ‖∇U‖_∞/(1+‖∇U‖₂^{4/3})` is not a norm of the field; per-horizon finiteness is automatic, content = horizon-uniformity — same non-triviality profile as N0; (iii) polarity re-walk — `S_blob` violation margin `τ^{−(5α−γ)/3}` recomputed from the frozen exponents including the background-enstrophy check; Type-I rate `(T−t)^{−2/3}` recomputed; (iv) the Tao-averaged violator recomputed (`N^{7/6}`), confirming both the absence of an averaging paradox and the exact-structure constraint on any future proof; (v) battery re-walk — B2 members hypothesized/none constructed; `u_τ`/`𝒱` solve no PDE; no smooth finite-energy certified violator is known in the literature consulted [H]. **Confirmed: SURVIVES; selected.**

**Runner-up (recorded, C0):** HR-1, the coherence head — selected instead if the V-5 literature sweep uncovers a prior refutation of HR-5-type reverse interpolation along solutions, or if the numerical ratio probe (below) shows super-datum growth of `Q₅` in certified-class-matching data.

**Counterexample-first obligations on H-SEL (precede any proof search, per standing discipline):**

1. **P-1 (literature sweep, debt V-5):** first-hand search for prior art on reverse-GN/intermittency-conditional regularity (Grujić-school "scaling-gap" and effective-dimension criteria; Constantin–Doering–Titi-adjacent bounds) — both to import any known partial theorem and to check H-SEL is not already refuted or known-equivalent to a named wall.
2. **P-2 (numerical ratio probe):** measure `Q₅(t)` on available near-singular datasets (Hou-type reproductions when the numerical lane resumes; published DNS where accessible). A validated super-datum divergence of `Q₅` on a bounded horizon is exactly the falsification event — and is simultaneously the signature the lab's singularity program must produce anyway (a candidate singularity must diverge `Q₅` at rate ≥ `τ^{−(5α−γ)/3}` in the frozen window).
3. **P-3 (analytic refutation attempt):** attempt certified-class constructions with spectral spreading (frequency-staircase data evolved on short horizons) driving `Q₅` beyond any fixed function of the datum — the honest first attack, before any proof attempt.

---

## §6 — SEL-3/SEL-5 reclassification (per the same user instruction)

- SEL-3 (`R3TSelInteriorSobolevSmoothing`) and SEL-5 (`R3TSelH3Ladder`) are **ON HOLD as Lean implementation targets** — carried as **formalization debt on known mathematics** (the 1984 energy ladder + standard parabolic smoothing; audit SS-6 items 3/5). They are **not** research-unknowns and must not be ranked, audited, or treated alongside open heads; this audit's candidate space deliberately excludes them.
- The fixed discharge route (mollified energy method + Friedrichs commutator + SEL-4-for-mollified-fields) and the checked dead ends of `TSEL_BRIDGE_DISCHARGE_2026-09-02.md` §4 remain the binding plan for whenever the debt is paid; nothing here reopens or modifies it. The `IsR3RealVelocity u0` hypothesis on the ladder stays (do not drop it).
- Chain bookkeeping [D]: the Lean theorem `r3TSel_conditional_globalContinuation` presently consumes N0, SEL-5, and SEL-3 as hypotheses. Under this audit's reduction the *research* frontier is H-SEL alone; the *formalization* frontier is {EB-1 (new, energy equality), SEL-5, SEL-3} — all known-math debts. No Lean file was touched this session.

---

## §7 — Claim boundary and debts

- **RECORD-ONLY.** No frozen verdict, frontier, park, watch, or hold changes. The BH branch stays PARKED; M-1 stays ON HOLD; N0 proof search stays uncommissioned and unstarted; **no Lean code was written or modified.**
- **Nothing here asserts, approaches, or implies a resolution of the Navier–Stokes Millennium problem in either direction.** Every head in §3 is OPEN; H-SEL is OPEN; universal H-SEL is Clay-equivalent-or-harder for the certified class, exactly as N0 is (§1 logical-collapse note). No proof obligation of `FABLE5_HANDOFF.md` is closed or claimed closed.
- **C0 discipline:** H-SEL is *a* selected head, not "the" route; the ranking asserts no exclusivity; runner-up and revision triggers are printed.
- **Verification debts (named, none consumed):** V-1 CF/BdVB exact hypotheses (norm on the ω-region, constant arbitrariness, solution class); V-2 Miller index range and solution class; V-3 BFG sparseness constants and time-continuity requirement; V-4 DHY Euler-form parameters + NS-transfer status; V-5 the H-SEL prior-art sweep (obligation P-1); V-6 Cao–Titi/Chemin–Zhang exact indices. Every literature citation in this record is [H] (from memory) unless marked [V]; **none is consumed by any frozen object** — first-hand fetch is mandatory before any of them is load-bearing.
- **New Lean-absent debt named:** EB-1, the energy equality for certified solutions (Arrow α). Formalizing it is a bounded known-math task but is **not commissioned**; the Stage-9 stop rule on uncommissioned formal plumbing stands.

---

## §8 — Bottom line

The norm axis collapses (§2): below criticality every sup-norm head is the classical problem restated; at criticality the heads are the named walls; above it no bridge exists. Seven structural heads were generated in three lanes (geometric, spectral, distributional) and run through the standing counterexample battery before any proof search: **all seven survive, none is rejected by a constructed certified violator, and each is violated by every frozen-window blow-up-compatible scenario — the correct two-sided polarity.** The ranking selects **H-SEL = HR-5, the reverse-interpolation head** — operative corrected form (§9): **`‖∇U(t)‖_∞ ≤ Q₀(1+‖∇U(t)‖₂²)`** — as the single next research theorem: its bridge to N0 is two known arrows (energy budget + direct integration) landing on the already-proved Lean assembly, every frozen blow-up-compatible scenario violates it class-wide (`τ^{−(2α−γ)}`; the original "sharpest margin" superlative is withdrawn in §9), Tao's averaged blow-up violates its analogue (so any proof must consume exact-NS structure — the FC-086 constraint located, not evaded), and its falsification observable is a single scalar ratio measurable in any dataset. The coherence head HR-1 is the recorded runner-up. Counterexample-first obligations P-1/P-2/P-3 precede any proof search on H-SEL; commissioning any of them is a user act. SEL-3/SEL-5 are reclassified as on-hold formalization debt on known mathematics — not research-unknowns. Nothing frozen has moved; no Lean file changed; no Clay claim of any kind is made or implied.

---

## §9 — H-SEL statement correction audit (2026-09-02, fifth session; commissioned one-shot; RECORD-ONLY)

**Commission.** User instruction, fifth session: for the power family `‖∇U(t)‖_∞ ≤ Q₀(1+‖∇U(t)‖₂^p)`, recompute the exact endpoint closable to N0 by the energy equality alone; verify whether `p = 2` is the maximal energy-closable exponent and re-adjudicate the `p = 4/3` selection; re-audit the logical direction of the printed reverse-GN reading and retract it if unjustifiable; re-run the frozen-`S_blob`, Type-I, multi-scale, and Tao-averaged counterexample tests on the corrected head; recompute the ranking including HR-1/HR-3. No Lean change, no proof search, no bulk literature search (V-debts stay undischarged).

### 9.1 EH-1 — the closable endpoint is `p = 2`, not `p = 4/3` (printed-statement defect, corrected)

The only budget the energy equality supplies is `∫₀^{T′}‖∇U‖²_{L²}dt ≤ B := ‖U(0)‖²_{L²}/(2ν)` (plus `sup_t‖U(t)‖₂ ≤ ‖U(0)‖₂`, which only feeds the constant). The head closes N0 iff `∫₀^{T′}(1+‖∇U‖₂^p)dt` is bounded by datum quantities, and from the `L²_t` budget alone [D]:

- **`p ≤ 2` closes.** `p = 2`: directly, `∫‖∇U‖₂² ≤ B` — no Hölder needed, giving `G(T;ν,‖u0‖) = Q₀·(T + B)`. `p < 2`: Hölder, `∫‖∇U‖₂^p ≤ T^{1−p/2}B^{p/2}`.
- **`p > 2` does not close on this budget.** Time-spike model: enstrophy `‖∇U‖₂² = H` on a window of length `B/H`, else 0 — the budget `∫‖∇U‖₂² = B` is fixed while `∫‖∇U‖₂^p = B·H^{(p−2)/2} → ∞` as `H → ∞`. The energy equality alone cannot exclude such spikes, so no `G` exists for `p > 2` by this route.

**Hence `p = 2` is the exact endpoint — verified as commissioned.** The original print ("4/3 is the largest closable against the `L²`-in-time budget") arose from an unnecessary Hölder split (`q = 3/2` applied to the `4/3` power) and is a **false superlative**; §3's parenthetical "(any θ ≤ 4/3 admissible; 4/3 = weakest member)" is superseded by "(any `p ≤ 2` closable; `p = 2` = weakest, hence primary, member)".

**Re-adjudication of the selection object [D].** Since `1 + x^{4/3} ≤ 2(1 + x²)`, the old `4/3` head **implies** the `p = 2` head (with `Q₀ ↦ 2Q₀`): the correction moves H-SEL to the *weakest* member of the family that still closes N0 — a strictly weaker hypothesis at identical bridge cost (Arrow β even simplifies: direct integration replaces Hölder). The correction is therefore selection-preserving and statement-improving. **Operative statement (H-SEL, corrected):**

> ∀ν>0, ∀ admissible Schwartz datum u0, ∀ finite T: ∃ Q₀(T;ν,‖u0‖) < ∞ such that every certified solution on every certified horizon T′ ≤ T satisfies, for all t ∈ [0,T′]:
> **‖∇U(t)‖_{L∞} ≤ Q₀ · (1 + ‖∇U(t)‖_{L²}²).**

Corrected chain: Arrow α (EB-1, unchanged) ⟹ Arrow β′ (direct integration [KNOWN, trivial]): `∫₀^{T′}‖∇U‖_∞ dt ≤ Q₀(T + ‖u0‖²_{L²,dec}/(2ν)) =: G(T;ν,‖u0‖)` ⟹ N0 verbatim. Corrected scaling: LHS `λ²` vs RHS `λ¹` under `u_λ` — still supercritical as a hypothesis (the scale-invariant exponent is `p = 4`), but one power weaker than the `4/3` print (`λ^{2/3}`); the head is now the closest energy-closable member to scale invariance.

### 9.2 EH-2 — the reverse-GN reading is RETRACTED (logical-direction error)

The §3 HR-5 row printed: "by GN `‖∇U‖_∞ ≲ ‖∇U‖₂^{1/4}‖∇³U‖₂^{3/4}`, the head reads `‖∇³U‖₂ ≲ Q₀^{4/3}‖∇U‖₂^{13/9}`". This inverts an inequality: GN and the head are **both upper bounds on `‖∇U‖_∞`**; combining two upper bounds on the same quantity yields nothing about `‖∇³U‖₂`. The derivation would need a *lower* bound on `‖∇U‖_∞` in terms of `‖∇³U‖₂` — i.e. GN saturation — which is false in general. Explicit countermodel [D]: `f_N = N^{−1}\sin(Nx₁)φ(x)` (fixed bump `φ`) has `‖∇f_N‖_∞ = O(1)`, `‖∇f_N‖₂ = O(1)`, `‖∇³f_N‖₂ ≍ N² → ∞` — it satisfies every head in the family with a fixed constant while violating the claimed consequence unboundedly. **The sentence is retracted.** What survives: the "anti-intermittency / spectral-concentration" description is **demoted from an equivalent formulation to heuristic motivation** (accurate only for GN-saturating, single-scale-concentrated fields). Verdict impact: none on admission, battery, or polarity — no battery computation consumed the retracted reading; the interpretive strength of HR-5 is reduced, and this is priced into the re-ranking below rather than hidden.

### 9.3 Battery re-run on the corrected head (`p = 2`)

| Test | Arithmetic [D] | Verdict |
|---|---|---|
| frozen `S_blob` | `‖∇U‖_∞ ~ τ^{−(γ+α)}` vs `Q₀‖∇U‖₂² ~ Q₀τ^{α−2γ}` (core-dominated: `α−2γ < 0`, O(1) background subdominant — unchanged check): head holds iff `α ≤ γ/2`; window forces `α ≥ 2γ/3 > γ/2` ⟹ **violated class-wide at rate `τ^{−(2α−γ)}`, with `2α−γ ≥ γ/3 > 1/6`** | polarity PASS |
| margin comparison | the original "sharpest margin in the roster" superlative is **withdrawn**: `2α−γ ≥ α/2` (HR-1's coherence margin) throughout the window with equality only on the `α = 2γ/3` edge — "≥ the coherence head's margin, non-strict at the edge" is the correct print | corrected |
| Type-I | `‖∇U‖_∞ ~ (T−t)^{−1}` vs `‖∇U‖₂² ~ (T−t)^{−1/2}` ⟹ violated at rate `(T−t)^{−1/2}` (was `(T−t)^{−2/3}` for the `4/3` form) | polarity PASS |
| single-shell datum (kinematic) | shell at frequency `N`, `‖u‖₂ = 1`: ratio `~ N^{5/2}/N² = N^{1/2}`, absorbed by `Q₀(‖u0‖_{H³})` with `‖u0‖_{H³} ~ N³` — per-datum survival unchanged (was `N^{7/6}`) | no violator |
| Tao averaged-NS (FC-086) | the frequency-concentrated averaged blow-up violates the head-analogue at rate `N(t)^{1/2} → ∞` beyond any function of the datum; the averaged model satisfies the full energy structure yet violates the head ⟹ **any proof of H-SEL must consume exact-NS structure beyond the energy identity — conclusion unchanged**, rate print corrected | polarity PASS |
| multi-scale / stacked-cell | spatial/frequency spreading raises `‖∇U‖₂²` relative to `‖∇U‖_∞` — the head only gets easier on spread configurations; blow-up-compatible members must still concentrate and hence violate; unchanged | polarity PASS |
| fixed-ν phenomenology (heuristic, recorded as such) | Kolmogorov counting: `‖∇U‖_∞/‖∇U‖₂² ~ (ε/ν)^{−1/2}·(intermittency corrections)` — leading power *more* favorable than the `4/3` form's `(ε/ν)^{−1/6}` | favorable |

All polarity checks pass on the corrected head; every rate specific to the `4/3` form (`τ^{−(5α−γ)/3}`, `(T−t)^{−2/3}`, `N^{7/6}`) is superseded by the row above.

### 9.4 Re-ranking (same axes; HR-1/HR-3 re-examined)

No new facts arose about HR-1, HR-3, or any other roster member (no literature fetched, per commission); their rows are re-affirmed as printed. For HR-5 the correction cuts both ways and the offsets are priced explicitly: **(+)** strictly weaker statement at identical (slightly simpler) bridge cost; **(+)** scaling moved one power toward invariance; **(+)** more favorable fixed-ν counting; **(−)** EH-2 removes the structural "reverse-GN" reading (the head's content is thinner than advertised — a ratio bound, with the spectral reading only heuristic); **(−)** the margin superlative is withdrawn (non-strict at the window edge vs HR-1).

| # | Head | Lev | Plaus | Dist | Lean | Π | Change |
|---|---|---|---|---|---|---|---|
| 1 | **HR-5 (corrected, `p = 2`)** | 5 | 3 | 2 | 4 | **120** | scores unchanged: the (+) items would justify Plaus 4 in isolation, the EH-2 demotion cancels the bump — held at 3, both directions recorded |
| 2 | HR-1 coherence | 5 | 3 | 2 | 2 | 60 | unchanged; margin comparison now non-strict at the `α = 2γ/3` edge (cosmetic) |
| 3 | HR-3 sparseness | 5 | 3 | 3 | 1 | 45 | unchanged |
| 4– | HR-2 / HR-6 / HR-7 / HR-4 | — | — | — | — | 32/24/24/6 | unchanged |

**Selection re-affirmed (C0: a selection, not a uniqueness claim): H-SEL = HR-5 in the corrected `p = 2` form; runner-up HR-1 unchanged**, with the same revision triggers (a V-5 prior-art refutation, or a P-2 probe showing super-datum growth of the corrected ratio `Q₅(t) := ‖∇U(t)‖_∞/(1+‖∇U(t)‖₂²)`). Obligations P-1/P-2/P-3 stand, now aimed at the `p = 2` form (P-1's sweep must cover the whole family `p ∈ (0,4]`, since prior art on any member bears on the endpoint choice).

### 9.5 Claim boundary of this correction pass

RECORD-ONLY; no Lean file touched; no proof search on H-SEL or N0; no literature fetched (debts V-1…V-6 remain undischarged and unconsumed). EH-1/EH-2 are recorded as errata with the original text annotated in place, not silently rewritten. The corrected H-SEL remains OPEN; universal H-SEL remains Clay-equivalent-or-harder for the certified class; nothing frozen has moved; no Clay claim of any kind is made or implied.
