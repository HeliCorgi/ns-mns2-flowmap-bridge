# Scope-B reconnaissance — trigger (T-c) OPEN (no fire, twice over); DVEP is an *asserted* witness; R-B2′ is Scope-A-gated on B2

Date: 2026-08-21 (JST). One bounded literature-reconnaissance pass (3 Opus analysts
(DVEP first-hand / class state-of-the-art / frozen-map scope classification) +
adversarial verifier + critic; web sources fetched first-hand; stop rules clean —
§9). **Record-only: no map edits; every freeze-queue item below is PROPOSED, NOT
EXECUTED.** Baseline: `FREEZE_REVIEW_2026-08-21.md` §7 option 1. Tags: [H] textbook,
[V] verified first-hand (exact location named), [V?] search-level, [D] derived
(flagged compositions/classifications), [C] conditional, [B] bookkeeping.

## 1. RULING: (T-c) OPEN — the amended §10 trigger does not fire, twice over

Trigger (annotation A8, [V]): "Scope B opens — localizability shown non-necessary
inside the primary class `A_NS`, or a non-localizable witness inside `A_NS`
appears." `A_NS` ([V], swirl-probe §3): (A1) `u ∈ C¹(R³)`; (A2) axisymmetric;
(A3) distributional steady Euler; (A4) `u ∈ L²`, `p ∈ L¹_loc`, ring-vanishing (L);
(A5) `u ≢ 0`.

- **Limb (i) not met, and not unreachable**: the forcing direction is **empty in
  3D** — CLV (arXiv:1903.11699 [V], full text), the paper that invented
  localizability, contains no necessity language (grep `necessar` → one hit,
  "unnecessary parameters"); all three papers whose subject is localizability
  (CLV; Peralta-Salas–Slobodeanu arXiv:2606.13462 [V]; Sato–Abe arXiv:2608.11547
  [V, verifier-fetched]) run localizable ⟹ structure, never the converse.
- **Limb (ii) not met**: DVEP (arXiv:2005.04380 [V], full text) fails (A1) —
  the velocity jump across `∂Ω` is forced by the construction's own constants
  (Remark 1.3(iii): Neumann constant `c > 0` with `ψ|_{∂Ω} = 0` ⟹ `|u|² = c` from
  inside vs `u ≡ 0` outside). Structural, not removable.
- **Stronger than expected**: DVEP's non-localizability is **asserted, never
  proved** — full-text grep: exactly four occurrences of `localiz` (abstract; the
  CLV-definition line; "these solutions are not localizable"; §1 "not localizable
  **in general**"), zero of `necessar`; no lemma, computation, or location of
  failure anywhere in the 18 pages. **DVEP is an asserted, not a verified,
  Scope-B witness.** (Critic re-ran the decisive grep independently.)

**Canonical open question (print form):** *Does there exist `u ∈ C¹(R³)`,
axisymmetric with swirl, non-trivial, solving steady Euler distributionally with
`u ∈ L²`, `p ∈ L¹_loc` and `liminf_{R→∞} ∫_{R≤|x|≤2R}(|u|²+|p|) = 0`, such that
`u·∇p ≢ 0` (equivalently `u·∇|u|² ≢ 0`)?* Nearest "no": none in 3D (2D structure:
Elgindi–Huang–Said–Xie arXiv:2408.14662 [V?]). Nearest "yes": DVEP — one
regularity notch below `A_NS` and one proof short of being a witness at all.

**Consequence**: A8 stands; the geometry-gate revisit is NOT mandatory; no CAP
fire. Next mandatory re-check: whenever a `C¹` compactly-supported non-localizable
3D witness, or any regularity ⟹ localizability theorem, is published (F25).

## 2. DVEP — the definitive record [V]

- **Abstract (verbatim)**: "…stationary weak solutions of the 3D Euler equation
  with compact support. The solutions, which are piecewise smooth and
  discontinuous across a surface, are axisymmetric with swirl. The range of
  solutions … is different from, and larger than, the family of smooth stationary
  solutions recently obtained by Gavrilov and Constantin–La–Vicol; in particular,
  these solutions are not localizable. A key step … an overdetermined elliptic
  boundary value problem where one prescribes both Dirichlet and (nonconstant)
  Neumann data."
- **Regularity ledger**: `u ∈ L^∞`, `ω ∈ L^∞`; piecewise `C^s`, `s > 2`
  non-integer (Thm 1.2 — not `C^∞`); `u ∈ C^s(Ω̄)` from inside, `u ≡ 0` outside,
  **not `C⁰(R³)`** — one smooth jump surface, the boundary of a **solid torus**
  (vs the toroidal *shells* of Gavrilov/CLV). Swirl strictly nonzero throughout
  the support (`F∘ψ > 0`, Thm 1.2(iv)).
- **Structure**: Grad–Shafranov pressure (1.5): `p = H(ψ) − (1/2r²)[|∇ψ|² +
  F(ψ)²]`; localizability ⟺ `|∇ψ|² + F(ψ)² = 2r²A(ψ)` — the boundary condition
  (1.8) imposes exactly this overdetermination **on `∂Ω` only** and leaves it free
  in the interior; the free data `(F̃, H)` are nowhere constrained to satisfy it
  [D, flagged composition — the sharpest structural statement of DVEP's Scope-B
  character, one step short of a proof].
- **Jiu–Xin reading confirmed** [V]: DVEP §1 cites "axisymmetric stationary Euler
  flows of compact support **without swirl** do not exist [8 = Jiu–Xin CMP 287
  (2009)]" — first-hand confirmation of the multiregion audit's unprinted-
  hypothesis conjecture. Body remains paywalled (debt, F28); CLV's citation "must
  vanish identically if the swirl F vanishes" is the usable surrogate; the
  unqualified gloss cannot be used without the no-swirl qualifier.
- **Corrections to our frozen recording (F23)**: multiregion §6.2's "explicitly
  'non-localizable'" and A8's rationale "`p = p(ψ)` necessity is **false** without
  regularity hypotheses" both overstate — correct: "the authors assert
  non-localizability (abstract; §1 'in general'); no proof is given." Ruling
  unaffected (A8 turns on `A_NS` membership, not Scope-B status).
- Hill's spherical vortex: retag **[H]** (textbook; the prior [V/H] sourced a
  wiki). It remains the witness that the per-level Scope-A conclusion is FALSE
  outside Scope A (ring corollary §5).

## 3. The class landscape (state of the art, 2026-08-21)

- **CLV (arXiv:1903.11699)** [V]: localizability is an *assumption they exploit*
  (Gavrilov's trick abstracted); Grad–Shafranov-type reduction; "they cannot be
  localized in space" (§2) is a construction remark, not a necessity claim;
  `C^{1/3}` sharpness remark sits in the intro (not Thm 3).
- **Gavrilov (arXiv:1810.08020)** [V abstract]: smooth compactly supported steady
  Euler; localizable (the profile-taste report's reading stands via 2606.13462).
- **NEW — Peralta-Salas–Slobodeanu (arXiv:2606.13462, June 2026)** [V]: "A
  symmetry theorem for localizable steady solutions of the 3D Euler equations" —
  localizable + analytic ⟹ axisymmetric. Converse direction; independently
  corroborates the repo's Scope-A ring-topology structure. Proposed addition F27.
- **NEW — Sato–Abe (arXiv:2608.11547, 2026-08-12)** [V]: also *assumes*
  `p = p(ψ)`. Legend: "three papers take localizability as their subject; all
  three assume it."
- **No forcing theorem, no C¹ witness**, in either direction, at any regularity in
  3D [V? absence-of-evidence; no citation-graph tool].

## 4. Frozen-map scope classification (critic-ruled)

**SCOPE-FREE** (no profile equation consumed): K1, K2, K3, K5, K6, K7, K8 [C on
(T)], K9, K10, K11; K4 (as a statement), K4′, K4″/R-B1, K4‴; **`S_blob` unchanged
in Scope B** (A7 form); the tie-face merge into B2; kernel facts F5–F8; budget
identity F9; winding identity F15, F18; R-NEG1–R-NEG6; Γ-max; KNSS Thm 5.3 as a
statement.

**SCOPE-A-ONLY** (consumes `|u|² = 2A(ψ)` at the one-parameter elliptic-orbit
step): the 2026-08-19 one-scale ring kill; `s_level ≥ δ/157`, θ = 1,
`α_g/r_min² ≥ 1/42`; the **amplitude corollary** `r_min ≤ √42Γ₀/‖u‖_∞`; the
amplitude gate (two-scale, `ρ_T ≥ γ`, `σ_tip = γ`); Prop G/V and `E = 2γ−α`; M2's
dissolution; **R-B2′'s re-centring anchor on B2**; and the objects
(E⁺⁺)=(COH-Δ)+(ANCH), (NECK), `θ_coh`, `ℓ_neck`, T4, W1–W5 — **undefined, not
open, in Scope B**. Direction note: `σ_sup = γ` and the forced tongue are Scope-A
*escape* structures — losing them **strengthens** K9's `σ = α` razor and K6's
[D2] in Scope B.

**MIXED / unresolved this pass**: M3 interlock (K3-limb scope-free; amplitude-gate
limb Scope-A); (N-Γ) (scope-free as a statement; printed discharge route Scope-A
on B2; M3 status unresolved); **(P) unresolved**; K8 on multi-region tuples
unresolved; intra-core `β_v` branch unresolved; R-NEG3 = scope-free arithmetic on
a Scope-A object.

**Scope-B survival landscape**: `S_blob` unchanged; **the one-scale ring REOPENS**
(witness `(γ,ρ,α) = (0.6, 0.42, 0.45)` live again); **M2 reopens**; M3's
`γ₂ < γ` still dies (K4′ scope-free); **B2 survives unkilled in Scope B.**

**Minimal closure requirements (cheapest first)**: (1) **(SB-ANCH)** — a
scope-free re-centring anchor: a point with `|u_θ| ≥ c‖u‖_∞` at distance
`≤ CΓ₀/‖u‖_∞` from the axis, τ-uniform; everything downstream (Γ-max, ledger,
KNSS 5.3, axial boost) is already scope-free; K9 supplies *existence* of a
Γ-saturated region, not *co-location* — co-location is the entire gap; **no
substitute recorded in any repo doc**. (2) A Scope-B pointwise swirl-fraction
bound via Bragg–Hawthorne + (L) — **cannot be a weakening of the Scope-A bound:
the per-level conclusion is FALSE outside Scope A (Hill)**. (3) A scope-free M2
dissolution. (4) A scope-free swirl-poverty ⟹ thinness exchange.

## 5. Defects found in our own frozen text (all proposed repairs, not executed)

1. **F22 — R-B2′'s "no Scope-A geometry" clause is false of its anchor**,
   propagated through three documents (annotation A15 — which names the Scope-A
   amplitude corollary and disclaims "no Scope-A geometry" *in the same
   sentence* — FREEZE_REVIEW §3, BH_CONSTANT_EXCLUSION_ROW §2). Correct reading:
   "no Scope-A *aggregation machinery*"; the re-centring anchor **is** the
   Scope-A amplitude corollary. **On B2, R-B2′ is Scope-A-gated; on M3's
   `γ₂ < γ` limb the anchor is the class definition and the row is scope-free.**
2. **F24 — unpatched consequent (critic's finding)**: A8 amended the §10 trigger
   but the same document's BH-verdict sentence ("a single non-localizable
   localized steady flow would restore YELLOW immediately", geo-gate l.204–205
   [V]) is still regularity-free — as printed it is met by DVEP while the trigger
   is not. Needs the same `A_NS` narrowing. Wording repair, not a verdict change.
3. **F23 — DVEP recording overstated** (§2 above).

## 6. Contradictions adjudicated (critic; 11 rows, compact)

C1 DVEP non-localizability asserted-vs-established → **asserted** (no map
consequence). C2 2606.13462 tag → [V] (Thm 1.1 `b`-clause [V?]). C3 "piecewise
`C^s`" — cosmetic. C4 DVEP vs (A4)/(L): verifier right that exterior pressure is
a nonzero constant, but the repair is **cost-free** (`p → p + const` gauge) [D] —
debt discharged. C5 CLV `C^{1/3}` location → intro. C6 Gavrilov gloss → [D].
C7 Hill → [H] only. C8 KNSS 5.3 presentation → one row + rider. C9 A3's
literature tags → repo-inherited [B]. C10 (new) A8's rationale "necessity false
at weak regularity" **dies** → "no necessity proof exists at any regularity;
authors assert non-necessity without proof". C11 (new) gate verdict sentence
inconsistent with A8 → F24.

## 7. Proposed freeze-queue items F21–F29 (PROPOSED, NOT EXECUTED)

**F21** scope legend (every K-row and R-NEG row scope-free; `S_blob` unchanged;
Scope-A enters only through the geometry gate's elliptic-orbit rigidity).
**F22** R-B2′ scope correction (one row + rider; §5.1). **F23** DVEP recording
correction (§5.3). **F24** patch the gate's verdict sentence with the `A_NS`
narrowing (§5.2). **F25** trigger-status line ((T-c) OPEN at 2026-08-21; both
limbs unmet, neither unreachable; re-check condition). **F26** standing Scope-B
frontier: the canonical open question verbatim + **(SB-ANCH)** as the named gap.
**F27** literature additions (2606.13462, 2608.11547; "three papers take
localizability as their subject; all three assume it"). **F28** debts (Jiu–Xin
paywall + CLV surrogate + no-swirl-qualifier warning; DVEP (L) gauge ruling
discharged [D]). **F29** Scope-B legends (Scope-A objects undefined-not-open in
Scope B; per-level bound FALSE outside Scope A — no weakening possible; Scope-A
escapes lost ⟹ K9/K6 strengthen in Scope B).

## 8. The single next bounded task (critic-designated)

**Audit the R-B2′ chain for anchor-independence** (classification, repo docs
only; no literature, no numerics, no proof attempts): is the map's one remaining
conditional row Scope-A-gated on B2, and can any *already-recorded* scope-free
object substitute for the amplitude corollary as the re-centring anchor?
Outcomes: (a) a recorded scope-free substitute exists ⟹ R-B2′ scope-free on B2,
F22 is wording-only, B2 dies in Scope B too; (b) none exists (expected) ⟹ F22 is
substantive, **(SB-ANCH)** becomes the named primary Scope-B gap, B2 recorded
*unkilled in Scope B*; (c) the chain consumes the anchor more than once ⟹
escalate — the row's conditionality list is incomplete as printed; program
decision for the user. *Not chosen*: paywalled-body fetches (no map
consequence); witness hunts and (L)-normalization work (theorem-shaped,
forbidden).

## 9. Stop-rule audit (whole pass)

CLEAN. No theorem attempted (three compositions flagged [D] as candidate
reductions: DVEP finding 5 & 8, the C4 gauge ruling). No numerics. No map edits —
every proposal carries "proposed, not executed". No new ansatz. No tag
promotions; six demotions executed. Paywalls recorded, bodies never guessed; one
fetch-failure chain recorded and worked around by local extraction; no fabricated
quotes (verifier re-fetched all decisive sources; critic independently re-ran the
decisive grep). A3 performed no web fetches and disclosed it (tags demoted to
[B], not discarded).

Sources fetched first-hand this pass: arXiv:2005.04380v1 (full text),
arXiv:1903.11699 (full text), arXiv:1810.08020 (abstract), arXiv:2606.13462
(abstract + Thm 1.1), arXiv:2608.11547 (abstract); repo docs as cited inline.
