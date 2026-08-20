# Multi-region audit — M2 dissolves, M3 open on one retired row, B2 restructured

Date: 2026-08-20 (JST). One bounded pass (4 Opus analysts + 2 adversarial verifications +
completeness critic; stop rules observed: no simulation — one [C-num] quadrature
cross-check whose load was removed by a third, symbolic derivation; no new ansatz — two
close calls policed, both admissible; no V1/K12 promotion; **no map edits** — this pass
was report-level only, the freeze review holds the pen). Baselines:
`BH_RING_COROLLARY_ADVERSARIAL_AUDIT_2026-08-19.md`, `TYPE2_KILL_TABLE_2026-08-19.md`
(+ ring annotation), `BH_GEO_SWIRL_AGGREGATION_2026-08-19.md`. Tags: [H] hard, [D]
derived this pass (twice-checked), [V] verified from a fetched source, [V?] search-level,
[C] conditional, [C-num] series/quadrature, [B] bookkeeping.

## 1. Per-region dictionary and the K3 covering lemma

A uniform per-region dictionary (region j: radius `τ^{ρ_j}`, gradient scale `τ^{λ_j}`,
volume `τ^{v_j}`, amplitude `τ^{−γ_j}`, swirl `τ^{−σ_j}`) reproduces every printed
blob/ring row exactly [D]. Two structural facts:

- **K3 is a covering condition and `min_j E_j` is concave** [D]: each region covers an
  *interval* of the CFZ parameter ε; a two-region flow can leave a middle-ε gap and be
  regular (explicit gap witness). A single region covers everything iff
  `ρ_j ≤ γ_j ∧ γ_j > 1/2`. Multi-region candidates must exhibit the cover — endpoint
  checks are insufficient.
- **K9 reduces to Γ-saturation** [D]: given the Γ maximum principle, K9 ⟺ some region
  has `σ_j = ρ_j > 0`. It cuts nothing in `(γ,α)`; it is a location/structure
  requirement. Corrected shape: **a trichotomy** in the saturation scale
  `β_v ∈ (0,γ]` — `β_v = α` (the printed razor), `β_v ∈ (α,γ]` (intra-core sub-core —
  the original two-scale debt, **still unanalysed**), `β_v < α` (separate region). Both
  halves of the printed razor substitute `β_v = α`; P6 charged only one. Additionally
  the map's `σ` is **ill-posed for on-axis cores**: `σ_core` (at `r ≍ ℓ`) and
  `σ_sup` (whole core) differ — in Scope A, `σ_sup = γ` always, while Scope A
  *restores* `σ_core = α` when the tongue reaches `ρ_T = γ` (ruling 4).

## 2. The amplitude gate on multi-region flows — capping, not pinning

The containment-free amplitude corollary places the top-speed level's inner radius at
`r_min ≍ Γ(L)/‖u‖_∞ ≤ √42·Γ₀/‖u‖_∞`. Corrected reading (verification ruling): the
second scale is **capped** (`ρ_T ≥ γ`), not pinned to `τ^γ` — `Γ(L) ≤ Γ₀` is an
inequality, and a level may carry small circulation. Consequences:

- **every Scope-A blob is two-scale in the tongue sense** (a level with
  `|u_θ| ≥ ‖u‖_∞/√42` exists at `r_min ≤ √42 Γ₀/‖u‖_∞`), with `σ_tip = γ` at depth
  `ρ_T ≥ γ`; the tongue's energy share is `O(τ^{2(γ−α)}) → 0`, so **V1 does not bite
  it** (V1 constrains energy-carrying structure — the tempting "tongue < √(ντ) + V1 ⟹
  blob dead" shortcut fails; the energy weighting is load-bearing);
- Scope A **selects** the Gate-C sacrifice: uniform `C¹` in core variables fails at rate
  `1/ε` (`|∇u|_tip/|∇u|_core ~ τ^{α−γ}`) — the taste report's five-way sacrifice list
  narrows to **one named sacrifice at a named rate** [D];
- the gate is **silent** wherever the amplitude-dominant region has `γ_reg ≤ ρ_reg`
  (i.e. `|u| ≲ Γ₀/r`) — and that silence zone is exactly the swirl-dominated corridor
  (see the interlock, §4).

## 3. Per-class results

**M2 (ring + mesoscale): RESTRICTED — no independent members** [D, triple-derived].
Every sub-case relabels: a contained Scope-A core that carries `‖u‖_∞` and its own K9 is
*forced* to `ρ = σ = γ` (amplitude gate + Γ-max + K9), i.e. it **is** the M3 swirl core —
a theorem, not a taxonomy choice; a tongued core is B2; a mesoscale amplitude-carrier
makes the "ring" an inert decoration around a blob. `S_ring ∩ Scope-A ∩ {contained,
amplitude+L³ carrier} = ∅` (re-derived three times). **M2 is not a ring branch.**

**M3 (swirl-dominated corridor): OPEN — on exactly one retired row** (§4). Untouched by
every frozen row: the swirl core `ρ₁ = σ₁ = γ₁ = γ` covers K3 alone, satisfies
K5/K9/K11 automatically, and exiles `L³` to a carrier region. Region-count correction:
under a power-law `L³` divergence the forced minimum is **2**, not "≥3" (the printed
[D2] over-counts; the marginal face `ρ=σ=γ=α` needs log divergence and sits outside the
map's power-law vocabulary). If the `L³` carrier is itself Scope-A with `γ₂ > 1/2`, it
has its own forced tongue — that is the honest source of a third region.

**B2 (two-scale blob): RESTRICTED — structure added, exponents unchanged.** Surviving
set: `(γ,α) ∈ S_blob` (with the boundary correction: K5 excludes `α ≤ 2γ−1`, so the
printed face `α = 2γ−1`, `γ > 3/4` is actually excluded) **plus** the forced tongue
(`ρ_T ≥ γ`, `σ_tip = γ`, `Γ_L ≍ τ^{ρ_T−γ}`); the vorticity sup relocates off the core
(`‖ω‖_∞ ≳ τ^{−γ−ρ_T} ≫ τ^{−(γ+α)}` — every row built on `‖ω‖_∞ ~ U/ℓ` must be re-read);
K6's [D2] does **not** fire at the tip (same location premise as K9), so core-carried
`L³` survives. **The frozen rows cut nothing beyond `S_blob`** — recorded as a failure
of the table, not repaired. Blocking: V1 (unpromoted) and the quantitative rigidity rate.

## 4. The interlock — one object, one retired row (highest-value finding)

Three "open" objects coincide [D, found twice independently]:
**amplitude-gate silence** (`|u| ≲ Γ₀/r`) ⟺ **the K3 middle-ε gap region** ⟺ **M3's
swirl-dominated core** — and the retired row **K4 (KNSS Liouville: axisymmetric,
`|v| ≤ C/r` ⟹ regular) covers exactly this object.** The K4-retirement rationale ("every
cut it would give is covered by K3") is **false**: the tuple `ρ = σ = γ` violates K3 for
every ε ∈ (0,1] while obeying `|u| ≤ C/r` — K3 does not cover it; K4 would kill it.
**The exact blocking question for M3:** does KNSS's criterion hold with the hypotheses
the map needs (structure localized near the axis, constant uniform in τ)? If yes, the
swirl-dominated corridor collapses — Scope-A-free and viscosity-free. If no, M3 is the
survivor. Only a freeze decision can re-arm a retired row.

## 5. P6 falsifier — RESOLVED: PASS (symbolic)

The armed A↔σ dictionary test is settled [V symbolic + C-num cross-check]:
`k` **cancels identically** from the level expansion (it enters only via `k²b²`, pinned
by `⟨u_z²⟩ = ⟨|u|²⟩/3`), so the ring-audit erratum's worry was right for the wrong
constant: the recorded `X = (1/3)(1 − 23σ²/32)` is **wrong**; correct (three independent
derivations, one fully symbolic) is `X = (1/3)(1 − 7σ²/16)`, giving
`s_level = 1/2 − (21/64)(1−δ)²`. The published shell side gives, in the same
dictionary-free aspect variable, `1/2 − (21/16)δ_probe² = 1/2 − (21/64)(1−δ)²`
(`1−δ = 2δ_probe`). **Exact rational agreement 21/64 = 21/64 — the one-parameter
reduction is confirmed against the published construction.** The geometry gate's revisit
trigger "P6 falsifies the reduction" is **not** met. Residual [V?]: the reading
`δ_probe = ℓ/R` (forced by two internal consistency checks; a `1−δ` reading would fail
by exactly 4) — check against the probe source before citing the PASS. Retired numbers:
`23/32`, `0.5391`.

## 6. Literature results

1. **Jiu–Xin CMP 287, verbatim abstract secured [V]:** C¹ class; hypotheses *finite
   energy + uniform constant far-field state*; conclusion: no nontrivial exact
   solutions + approximate-solution compactness. **Neither "no swirl" nor "compact
   support" appears in the abstract**; since Gavrilov's flow satisfies the printed
   hypotheses, the body must carry an unprinted hypothesis (almost certainly no-swirl)
   [H]. The Gate-C citation debt is **not paid** and is now sharper. Upside if
   no-swirl: the class is *weaker* than compact support — finite energy + far-field
   control suffices — which would shorten Gate C's sacrifice list.
2. **Scope-B witness exists at weak regularity [V]:** Domínguez-Vázquez–Enciso–
   Peralta-Salas (arXiv:2005.04380, ARMA 239 (2021)): compactly supported stationary
   weak Euler flows, **axisymmetric with swirl, piecewise smooth, discontinuous across
   a surface, explicitly "not localizable"**. Necessity of `p = p(ψ)` is **false at
   weak regularity**; any necessity proof must consume a regularity hypothesis. DVEP is
   outside the primary class `A_NS` (not C¹), so it does not restore YELLOW — but the
   geometry gate's §10 revisit trigger, **as worded (regularity-free), is met**: the
   freeze review must either fire it or amend the wording to "…a non-localizable
   witness **in the primary class `A_NS`**".
3. **Rigidity inside Scope A [V]:** Peralta-Salas–Slobodeanu (arXiv:2606.13462, 2026):
   analytic localizable 3-D Euler in a bounded domain ⟹ axisymmetric — the specialists'
   own reading of localizability as an overdetermination; not a necessity result.
4. **Hill's vortex usage certified [V/H]:** swirl-free, embedded in a uniform stream
   (not localized) — legitimate as the per-level scope witness (the per-level theorem
   needs no localization), exactly as the ring audit used it.

## 7. Corrections to previous passes (recorded; execution belongs to the freeze review)

- **Prop G / Prop V (blob) carry the ring erratum's defect** [D, found by both
  verifications]: as printed they substitute the *global* `δ_geo`/`s`, which is
  far-field-dominated on `S_blob` (core energy share `τ^{3α−2γ} → 0` where K5a is
  strict). **Repair (safe, direction-checked):** per-level `δ(ψ) ≤ 157·s_level(ψ)` +
  Markov *inside core energy* gives `r_min ≲ τ^{2γ−α}` for a positive `E_pol`-fraction
  of core levels — `E = 2γ−α` and Prop V stand in this weakened per-level form.
- Gate C/D of the taste report survive Scope-A tongues (the `ε²F̂F̂′` structure is a BH
  identity; the tongue contributes `O(ε³)` to `ψ̂`); what fails is Gate C hypothesis
  (ii), uniform `C¹`, at rate `1/ε` — a refinement, not a new channel.
- (A1) of the ring corollary fails **as printed** at the tongue tip (relative error
  `Θ(ν/Γ₀)`, non-decaying); the corollary's contained-level application is unaffected.

## 8. Verdicts

- **Per class: M2 RESTRICTED (no independent members) · M3 OPEN (blocking question =
  K4/KNSS on the Γ-saturated core) · B2 RESTRICTED (tongue structure forced; frozen
  rows cut nothing beyond `S_blob`).**
- **BH verdict: `YELLOW-RED`, HELD.** Not YELLOW: DVEP is outside `A_NS` and the ring
  kill stands unrefuted. Not RED-ward: this pass produced zero kills and exposed that
  the frozen table does not touch M3.
- **Next branch: `NEXT: FREEZE REVIEW`.** The pass's three most consequential results
  are corrections to frozen text (ill-posed `σ`; the unpropagated Prop-G/V erratum; the
  wrong armed-falsifier number — now resolved); the map is printed-inconsistent
  (`S_blob` boundary, "≥3" count); and the single biggest lever — **K4** — is a retired
  row that only a freeze decision can re-arm. Runner-up (recorded, not scheduled):
  Scope-B reconnaissance — strictly cheaper after the freeze fixes the trigger wording.

## 9. Proposed freeze-review agenda (annotation wordings drafted; NONE executed)

(1) define `σ_core` vs `σ_sup` in the kill-table legend; (2) K9 → trichotomy wording;
(3) K6 [D2] location premise + region-count correction; (4) propagate the far-field
erratum to Prop G/V with the per-level repair; (5) replace the P6 numbers
(`7/16`, `21/64`; trigger does not fire); (6) **K4: restore as [V?] with a first-hand
verification debt, or print that the swirl-dominated corridor survives *because* K4 is
retired**; (7) `S_blob` boundary `α > 2γ−1` strict; (8) gate §10 trigger: fire or amend
to primary-class wording (DVEP). Plus debts carried: the intra-core `β_v ∈ (α,γ]`
branch unanalysed; K8/K10 never applied to multi-region tuples; single-time power
counting (coexistence/one-pressure unchecked); Jiu–Xin body unread.
