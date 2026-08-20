# Type II kill table — every regularity theorem as an excluded subset of exponent space

Date: 2026-08-19 (JST). Companions:
[`TYPE2_SURVIVAL_MAP_2026-08-18.md`](TYPE2_SURVIVAL_MAP_2026-08-18.md) (base map),
[`D1_ADVERSARIAL_AUDIT_2026-08-19.md`](D1_ADVERSARIAL_AUDIT_2026-08-19.md) ([D1] withdrawn).

Format target: `S_survive = S₀ \ ⋃_j K_j`, with each theorem translated into the subset
`K_j` of exponent space it excludes. Exponents: amplitude `γ` (`‖u‖_∞ ~ τ^{−γ}`), core
scale `α` (`ℓ ~ τ^α`), ring radius `ρ` (`R ~ τ^ρ`; blob = `ρ = α`), core swirl amplitude
`σ` (`sup_core |u_θ| ~ τ^{−σ}`). Status tags: [H] hard (statement verified),
[V✓] verified from the source abstract today, [V?] believed/unverified, [C] conditional on
a stated hypothesis, [B] ansatz bookkeeping.

## 1. The table

| # | Source | Exact hypothesis (as verified) | Excluded subset `K_j` | Status |
|---|---|---|---|---|
| K1 | Leray 1934 | local existence lower bounds | `γ < 1/2`; enstrophy exponent `β < 1/4` | [H] |
| K2 | CSTY-II (arXiv:0709.4230), CSTY-I; KNSS Acta 2009 | axisym, nontrivial swirl, `|v| ≤ C_*|t|^{−1/2}`, `C_*` arbitrary ⇒ regular | `{γ = 1/2` with bounded prefactor`}` — Type II required | [V✓] |
| K3 | CSTY-II (arXiv:0709.4230) | axisym, `|v| ≤ C_* r^{−1+ε}|t|^{−ε/2}` for some `ε>0`, `C_*` arbitrary ⇒ regular | candidates whose *global* profile obeys such a bound for some `ε`. Core placement: the violation `sup |u|·r^{1−ε}τ^{ε/2} = ∞` must occur somewhere for **every** `ε ∈ (0, 1]`. Blob core: automatic in the window (`γ > α` and `γ > 1/2` suffice — no new cut). Ring core: forces **`γ > ρ`** or the violation moves to a separate mesoscale region | [V✓] |
| K4 | KNSS Acta 2009 (Liouville) | abstract only says "partial results … axi-symmetric" — exact `|v| ≤ C r^{−1}` form not confirmable from the abstract | **declared non-load-bearing** (2026-08-19): every cut the map uses is already covered by the verified K3 (`r^{−1+ε}` family); the `ε = 0` endpoint would add nothing to the map | [V?], retired |
| K5 | energy + dissipation (Leray) | `‖u‖₂` bounded, `∫‖∇u‖₂² < ∞` | blob: `α < 2γ/3` or `α ≤ 2γ−1`; ring: `ρ+2α < 2γ` or `ρ ≤ 2γ−1` | [H]+[B] |
| K6 | ESŠ 2003 / Seregin 2012 | `‖u‖_{L³} → ∞` necessary | core-carried-`L³` variants: blob `α ≥ γ`; ring `ρ+2α ≥ 3γ`. Swirl-dominated core (`σ = γ`, at `r ~ R`): **arithmetically incompatible** with core-carried `L³` ([D2], via `Γ` max principle `γ ≤ ρ`) — forces ≥3-region structure | [H]+[B] |
| K7 | Tao 2019 (triple-log lower bound on `‖u‖_{L³}`) | quantitative ESŠ rate | cuts only sub-power-law `L³` growth; **no cut** on power-law ansätze | [H], vacuous here |
| K8 | transport/diffusion displacement | hypothesis (T): structure advected + diffused | ring: `ρ < min(1−γ, 1/2)` excluded; blob: no cut (no translation) | [C] ([D1′]; replaces withdrawn [D1]) |
| K9 | Chen–Fang–Zhang swirl criterion: regular if `r^d u_θ ∈ L^q(0,T; L^p)`, `2/q + 3/p ≤ 1 − d`, `0 ≤ d < 1` (as quoted in the axisymmetric criteria literature, 2026 survey-level source) | at the `(p, q) = (∞, ∞)` endpoint: `|u_θ| ≤ C r^{−d}` for some `d < 1` ⇒ regular | the core swirl must violate every `d < 1` bound **or** a separate swirl-critical region exists. Core case: `σ > dα` for all `d < 1` ⟹ `σ ≥ α`; with `Γ` max principle (`σ ≤ α`) ⟹ **`σ = α` exactly** — the core carries `Γ ~ O(1)` circulation while remaining amplitude-subdominant | [V✓ endpoint, search-level; full-text endpoint-admissibility check noted][C] |
| K10 | Seregin note arXiv:2402.13229 (full text, as extracted 2026-08-19) | Type II class with scaled-`L³` lower bound at rates `r_k`, parameter `m₀ ∈ (2/5, 1)`; "Euler scaling" `v → λ^{α_S} v(λx, λ^{α_S+1}t)`, `α_S = 2 − m`, `m = 3m₀/(2+m₀) ∈ (1/2, 1)`; under boundedness of the stated scaled norms, self-similar/discretely-self-similar limit profiles vanish and the limit equations carry **no swirl** | in our coordinates: `γ = α_S/(α_S+1) ∈ (1/2, 3/5)`, `α = 1/(α_S+1) = 1 − γ` — **exactly the `γ + α = 1` Euler-balance edge** of the wedge for `γ ∈ (1/2, 3/5)`. Conditional exclusion pressure on that edge (exclusion holds unless one of Seregin's scaled-norm conditions fails); the wedge interior (`γ + α > 1`) is untouched | [V✓ full-text, second-hand extraction][C] |

| K11 | dominant-balance / energy-flux (two independent derivations, see `DOMINANT_BALANCE_INVERSION_2026-08-19.md`) | `∂ₜu ≳ U/τ` at an amplitude-growing core; some NS term must respond | **`γ + α ≥ 1`** — for `γ + α < 1` inside the wedge, convection, diffusion, and pressure gradient are all `≪ ∂ₜu` and the equation cannot balance | [B]+[D], double-derived |

## 2. Resulting survival set

**Blob (on-axis, core carries `L³`):**
`S_blob = {(γ, α) : 1/2 < γ < 1, max(1−γ, 2γ/3, 2γ−1) ≤ α < γ}` (K11 added 2026-08-19;
lower envelope `1−γ` on `(1/2, 3/5]`, `2γ/3` on `[3/5, 3/4]`, `2γ−1` on `[3/4, 1)`;
nonempty for every `γ ∈ (1/2, 1)`). K3/K4 violations are automatic inside it; K8 does not
apply to a non-translating core. Conditional refinement from K9: the swirl exponent on its
fibers is pinned to `σ = α` — an amplitude-subdominant core carrying `O(1)` swirl
circulation. The `γ + α = 1` lower edge (`γ ∈ (1/2, 3/5]`) is exactly Seregin's
Euler-scaling class (K10) and is under conditional exclusion pressure there.

**Ring (core carries `L³`, meridionally dominated):**
`S_ring = {(γ, ρ, α) : 1/2 < γ < 1, max(2γ−1, min(1−γ, 1/2)·[C]) < ρ ≤ α, ρ < γ (K3),
2γ ≤ ρ + 2α < 3γ}` — closes at `γ = 1` (as before, from K5+K6).

**Swirl-dominated ≥3-region corridor:** survives power counting at any `γ`, with the K3
violation and the `L³` divergence both exiled to a mesoscale, and (under K9) the core pinned
to `σ = α`. Every added requirement is structural, none yet lethal.

## 3. Answer to the dimension question

After subtracting every currently-verified `K_j`: the admissible set is a **2-dimensional
open wedge** (blob) plus a **3-dimensional conditional slab** (ring) plus the baroque
corridor. It is *not* down to a curve, and it is *not* empty. The conditional rows (K8, K9)
do not reduce the dimension of `(γ, α)`; they pin auxiliary structure (`ρ` range, `σ = α`).
Collapse to a curve or to ∅ would require: verified K9 with `d` pushed to a specific rate,
the K10 full-text content, or genuinely new theorems at the `γ → 1/2⁺` edge.

Operational reading: numerical search remains a legitimate objective —
`find a standard-ν trajectory with fitted (γ, ρ, α) ∈ S_survive and √τ‖u‖_∞ → ∞ converged`
— and the most informative theory work is whatever shrinks `S_blob` from its `γ → 1/2⁺`
edge (K10 extraction, K9 verification) or hardens K8.

## 4. Verification debts — settled 2026-08-19

1. K4: **retired** (non-load-bearing; verified K3 covers everything the map uses).
2. K9: **paid** (Chen–Fang–Zhang weighted swirl criterion identified with its exact
   inequality; `σ = α` razor holds at the `L^∞` endpoint, with the endpoint-admissibility
   check in the original paper left as a footnote-level residue).
3. K10: **paid** (Seregin's class mapped exactly onto the `γ + α = 1` edge,
   `γ ∈ (1/2, 3/5)`; conditional exclusion pressure on that edge; interior untouched).

Residual small debts (footnote level, not blocking the freeze): CFZ endpoint
admissibility; independent first-hand read of Seregin's conditions (1.3)/(2.3)/(2.4).
**The map is now frozen** except for these footnotes; see
`DOMINANT_BALANCE_INVERSION_2026-08-19.md` for the balance-level refinement (K11) and the
dominant-balance classification of the frozen wedge.

## Annotation 2026-08-19 (authorized by `BH_RING_COROLLARY_ADVERSARIAL_AUDIT_2026-08-19.md`)

> **one-scale localizable ring branch excluded by swirl-geometry pinning**

Riders (required by the authorization, all in this edit):

- **R1 (one-scale definition, previously implicit in the ring rows):** the one-scale ring
  branch means: the top-speed / energy-carrying poloidal levels are contained in a tube of
  minor scale `ℓ ~ τ^α` at radius `R ~ τ^ρ` (`ρ < α`), with a τ-independent constant, and
  the energy fill `∫|u|² ≍ ‖u‖_∞² · Rℓ²` holds. K5/K6's printed cuts are exactly these
  two bounds; without them `S_ring` is undefined. An inward energy-carrying tongue exits
  this class (→ mesoscale / ≥3-region corridor).
- **R4 (provenance relabel, survival set unchanged):** the `S_ring` constraint printed as
  "`ρ < γ (K3)`" is sourced as **`ρ ≤ γ` [K3] + `ρ ≠ γ` [K6 ∧ `ρ ≤ α`]** (K3's exponent
  arithmetic alone gives strictness only for `ρ ≤ 1/2`).
- Scope of the exclusion (exact): Scope-A (CLV-localizable, `p = p(ψ)`) one-scale ring
  only; viscosity-free, compactness-free, doubly sourced (K6 and K3). **Not covered:**
  the blob (`ρ = α`, unchanged, V1-conditional), the mesoscale / ≥3-region corridor
  (burden transferred: the mesoscale must carry asymptotically all poloidal energy and be
  axis-grazing), Scope-B rings (`p` not a streamline function — a GAP inside the frozen
  class, witness Hill's spherical vortex for the scope statement), the `γ+α = 1` edge.
- New footnote-level debt (P6): K9's blob-row `σ ≤ α` half uses a swirl-sup-*location*
  premise (`r ≍ ℓ`); Scope-A structure can relocate the swirl sup to an axis-grazing
  tongue tip `r_min ≲ τ^γ`. Feeds the multi-region audit; blob row unchanged.

## Annotation 2026-08-21 (authorized by `FREEZE_REVIEW_2026-08-21.md`, user fork-(β) adjudication)

The accumulated agenda of six passes is executed here. Master record with the full
adjudication table: `FREEZE_REVIEW_2026-08-21.md`. Section labels A1–A20 are referenced
from that record.

**A1 (legend: `σ_core` vs `σ_sup`).** The single exponent `σ` is ill-posed on an
on-axis core: separate `σ_core` (the core's own swirl amplitude) from `σ_sup` (the
global swirl sup, which Scope-A structure can relocate to an axis-grazing tongue tip).
In Scope A, `σ_sup = γ` identically; K9-type rows must state which `σ` they cut.

**A2 (K9 corrected to the saturation-scale trichotomy).** The printed pinning
"`σ = α` exactly" is replaced: on a Γ-saturated core the **saturation-scale**
exponent `β_v ∈ (0, γ]` trichotomizes — `β_v = α` (the printed razor) /
`β_v ∈ (α, γ]` (intra-core sub-core — the original two-scale debt, **unanalysed,
carried as an open debt**) / `β_v < α` (**the saturation sits in a separate
region**, not the core — an alternative structure carried on the map, not an
exclusion). K9's row cuts only the first case; the map must not cite `σ = α` as
unconditional.

**A3 (K6 [D2] correction).** [D2] carries a swirl-sup-*location* premise (the
violation placed at `r ≍ R`); and its conclusion is corrected from "forces ≥3-region
structure" to **"forces ≥2 regions (minimum two)"** — the arithmetic only forces the
`L³`-carrier and the swirl-sup carrier apart, **under a power-law `L³` divergence**
(the marginal face `ρ=σ=γ=α` needs log divergence and sits outside the map's
power-law vocabulary). [D2] does **not** fire at the tongue tip (same location
premise as K9). §2's "≥3-region corridor" heading is retained as a name only — the
forced minimum is 2.

**A4 (Prop G/V repaired).** The global-`s` (global swirl-fraction) step is withdrawn
(far-field dominated — the ring-audit erratum appended to the geometry gate); Prop
G/V survive in the **per-level + intra-core Markov** form only: per-level
`δ(ψ) ≤ 157·s_level(ψ)` + Markov inside the core energy gives `r_min ≲ τ^{2γ−α}`
**for a positive `E_pol`-fraction of core levels**. `E = 2γ−α` persists in weak
form.

**A5 (P6 falsifier settled).** The recorded X-expansion `23/32` and falsifier number
`0.5391` are **retired**; correct values: `X = (1/3)(1 − 7σ²/16)` → `7/16`, giving
`s_level = 1/2 − (21/64)(1−δ)²`, while the published shell side is
`1/2 − (21/16)δ_probe² = 1/2 − (21/64)(1−δ)²` under `1−δ = 2δ_probe` — **exact
rational agreement, symbolic PASS; the P6 trigger does not fire**. Residual [V?]:
the reading `δ_probe = ℓ/R` (forced by two internal consistency checks; a `1−δ`
reading would fail by exactly 4) is unverified against the probe source —
footnote-level, non-blocking. K9's blob row stands with A2's trichotomy rider.

**A6 (K4 RESTORED [V], with mandatory rider).** K4's 2026-08-19 retirement is
reversed; the retirement rationale is recorded as **false** (K3's `r^{−1+ε}` family
does not cover the `ε = 0` endpoint). K4 = KNSS Thm 6.1 [V first-hand: rate-free,
Type-II-valid]. **Rider (mandatory): K4 acts only through the route
amplitude-normalized zoom → ancient limit → KNSS rigidity; it never applies directly
to the unzoomed flow (`K₄ ∩ M3 = ∅` at the unzoomed level).** K4 does **not** cover
the swirl-dominated corridor by itself: through the zoom route only
`M3 ∩ {γ₂ < γ}` is cut, and only conditionally, via **K4′ [C] on (E⁺)+(P)** (A9);
the tie face `γ₂ = γ` defeats the `C/r` hypothesis (non-decaying plateau in the
ancient limit — KNSS gate §1 ruling NO) and merges into B2, where it is excluded
only conditionally by **R-B2′ [C]** (A15). This supersedes the K4 row's
"`[V?]`, retired" status tag (§1) and §4 debt item 1.

**A7 (`S_blob` boundary strictness).** The `α ≥ 2γ−1` clause is **strict**:
`α > 2γ−1`. `S_blob = {(γ,α) : 1/2 < γ < 1, max(1−γ, 2γ/3) ≤ α < γ, α > 2γ−1}`.

**A8 (geometry-gate §10 CAP-revisit trigger amended in its Scope-B limb only, not
fired).** The gate's trigger has three limbs; only the first is amended: "Scope B
opens — **localizability shown non-necessary inside the primary class `A_NS`**, or
a **non-localizable witness inside `A_NS`** appears." The other two limbs stand
unchanged (the ring corollary fails verification; the P6 dictionary test falsifies
the one-parameter reduction — now settled PASS, A5). DVEP (arXiv:2005.04380) is
recorded as the Scope-B witness (piecewise smooth, outside the primary C¹ class):
`p = p(ψ)` necessity is false without regularity hypotheses — outside `A_NS`,
hence **no fire, and no CAP trigger**.

**A9 (new row K4′ [C]).** "Axisym + the amplitude-normalized ancient limit decays
like `1/r` ⟹ regular" — excludes `M3 ∩ {γ₂ < γ}`, conditional on **(E⁺) + (P)**
(amended from (E)+(P)).

**A10 (row K4″ [C] — redundant confirmation only).** Lei–Zhang JFA 2011 Thm 1.2
(bounded weak ancient + `r|v_θ|` bounded + stream function BMO ⟹ `v ≡ 0`): kept on
the map as **redundant confirmation**, not a primary kill; its "one logarithm of
slack" sizing is withdrawn (BMO-stream ⟺ `w_pol ∈ BMO^{−1}`, zero logarithms).
(This row is the constant-exclusion pass's **R-B1**; `K4″` is its map label — two
names, one row.)

**A11 (new row K4‴ [D, unconditional]).** `Γ` is exactly scale-invariant under the
Prop-6.1 rescaling: every amplitude-normalized ancient limit inherits
`|v_θ| ≤ Γ₀/r` globally; every Thm-5.3-type application reduces to a poloidal
statement.

**A12 (P5 recorded as auxiliary corollary).** The elongated axis filament
(thickness `τ^γ`, length `τ^{l_T}`, `l_T ∈ (2γ−1, γ)`) is the cleanest K4′ target —
kept as a corollary, **not** a main map row.

**A13 (P7 legend).** Energy is not scale-invariant under the zoom
(`∫|v_k|² = λ_k^{−1}∫|u|² → ∞`): K5 constrains the original flow, never a rescaled
ancient limit. `Γ ∈ L^p` (`p < ∞`) does **not** descend to the limit; `Γ ∈ L^∞`
descends.

**A14 (K2 attribution corrected).** The KNSS citation requires (6.5) **and** (6.6);
"nontrivial swirl" is not a KNSS hypothesis. CSTY-I/II citations downgraded to
unverified-this-pass, not deleted.

**A15 (primary row R-B2′ [C]; R-B1 demoted).** New primary conditional row:

> **R-B2′ [C]:** re-centred Prop-6.1/Lemma-6.1 zoom on the Γ-saturated level
> (amplitude corollary, `C = √42`) + Γ-max + (N-Γ) [C-dict] + axial boost (derived)
> + the Biot–Savart deviation ledger under (E⁺⁺) ⟹ `|w| ≤ C/r` globally on the
> ancient limit ⟹ KNSS Thm 5.3 [V] ⟹ `w ≡ 0` ⟹ `v = b·e_z` ⟹ `Γ ≡ 0`,
> contradicting the Γ-saturated core ⟹ **M3's tie face AND B2's Γ-saturated blob
> excluded** — no Type-I rate, no viscosity, no energy, no Scope-A geometry, no V1.
> Conditional on **(E⁺⁺) = (COH-Δ) + (ANCH)** (see A16), **(P)**, **(N-Γ)**.

R-B1 (Lei–Zhang route) is demoted to redundant confirmation (A10).

**A16 (the (E⁺⁺)/(NECK) block — final frozen forms; supersedes the ledger's F3/F4
wordings and the neck-budget "iff"/F11).**

- **(E⁺⁺) [C], κ-form:** within the ledger ball, the neck's poloidal circulation
  over any dyadic meridional annulus obeys `λ_y ≤ C/R` (`κ̂ ≤ C`), τ- and
  R-uniformly. **Decomposition — both parts required (increment/level gap [D]):**
  **(COH-Δ)** — increment: coherence exponent `θ_coh(ρ)`, threshold
  `θ_coh(ρ) ≥ 2ρ` throughout `ρ ∈ [(γ+α)/2, γ]` (turnover `ρ+γ` clears ν-free;
  viscous `2ρ` exactly marginal; lifetime `1` fails everywhere by K11 — and K11
  (`γ+α ≥ 1`) places the whole neck at `ρ ≥ 1/2`, i.e. entirely inside `√(ντ)` —
  *necessary but NOT sufficient*); **(ANCH)** — level: an anchor/erasure statement
  for `κ̂` at neck radii; by R-NEG4 its only known carrier is T4, whose sizing
  consumes the unassigned `ℓ_neck`. **Either part failing re-opens R-B2 at rate
  `R = τ^{ρ−γ}`.**
- **(NECK), final:** poloidal shear structure of full amplitude order
  (`λ_y = O(1)`) on any dyadic meridional annulus at `R → ∞`, `R ≤ min(R*, R_k)`.
  **Standing dictionary-extension request; two named unassigned inputs:
  `θ_coh(ρ)`, `ℓ_neck`. `δ_T` deleted** (refuted by three independent routes).
  Negation witness only; inadmissible as a class member.
- *Legend for the frozen wordings:* `R* = (Γ₀²T̂)^{1/3}` with `T̂ = τ^{1−2γ}`;
  `R_k = ε₀τ^{(β−γ)/2}`, `β` = the finest **non-local** gradient-scale exponent
  (`α` for B2, `ρ₂` for the M3 tie face); **(E⁺)** = (E) + C¹-exhaustiveness
  within `τ^{(γ+β)/2}` of the zoom centre; **(P)** = class transfer (the
  re-centred limit lands in KNSS's bounded-weak class); **(N-Γ)** =
  interior-time lower bound on the rescaled `Γ` at a fixed point [C-dict].

**A17 (ledger facts F5–F8 adopted).** F5: `r|u_pol| ≲ 1` is exterior-tail only —
false inside the core; the whole neck is inside the core. F6: the poloidal kernel
sees `ω_θ` only; `∫ω dV ≡ 0` in axisymmetry; near-axis sources carry the `r′²`
weight; the axis-straddling 2-D window is empty. F7: `b_τ` is axial **by
derivation**. F8: ledger ball radius = (E⁺)'s printed C¹ radius exactly;
time-uniformity rests on `2γ−1 > 0` alone.

**A18 (neck-budget facts F9–F10, F13 + winding F19 adopted; F14 executed in
A19/A20; negative rows collected).** Budget identity: `dκ_R/dt = −∮ω_θ(u_pol·n)dl + ∮(Γ²/r³)dr +
ν∮[∂_nω_θ + (ω_θ/r)n_r]dl`; advective flux vanishes identically on material
regions; stretching = 2-D compressibility defect; production oscillation-controlled
`|∮(Γ²/r³)dr| ≤ ½ osc_R(Γ²)(r₁^{−2}−r₂^{−2})`, δ-free in both tongue orientations.
`δ_T` retired from the (E⁺⁺) discussion. Negative rows (frozen): **R-NEG1**
boost-the-original refuted (wind `M_k·b → ∞`); **R-NEG2** constants unexcludable by
scale-invariant estimates at an axisym singularity (Ożański–Palasek), moot under
re-centring; **R-NEG3** the neck production budget with an ancient/full-lifetime
horizon is vacuous on all of `S_blob` (both wedges `α+3γ<2`, `γ+3α<2` refuted);
**R-NEG4** no viscous bulk sink in the meridional κ-budget; **R-NEG5** the winding
identity has no viscous validity window (`νκ/ℓ²` sizings consume unassigned `ℓ`);
**R-NEG6** a region's gradient scale is a region descriptor, not a pointwise `ω_θ`
bound — `κ̂ ≤ τ^{2ρ−γ−α}` defines the neck's **outer (largest-`R`) endpoint**
`ρ = (γ+α)/2`, i.e. `R_k` (`ρ` increases inward: `ρ = γ` ⟺ `R = O(Γ₀)`); it is not
an anchor.

**A19 (winding facts F15, F17–F18, F20 adopted).** The winding form
(`|κ_pol(t)−κ₀| ≤ ½osc_loop(Γ)·TV_s(θ)`) reproduces the production budget
power-for-power and is **retired as a discharge vehicle for (E⁺⁺)** (structural:
increment vs level; starvation: residence, confinement, fold count, material
preimage — not proved impossible). `osc_loop(Γ)` hint vacuous: on the neck
`min(Γ₀, rτ^{−γ}) = Γ₀` identically. No Lagrangian localization: material↔Eulerian
transfer licensed only for `t ≲ τ^{ρ+γ}` (circular). **T4** = unsigned viscous
boundary flux, unestimated after six passes, sole carrier of (ANCH); `ℓ_neck` (the
neck's **own** gradient scale — **not** the ledger's non-local `β`, which is a
different, assigned object) printed as a **named unassigned input**, not a free
parameter.

**A20 (residual recordings).** KNSS receding-axis branch implicitly uses (6.16)
(rescaled Type-I) alongside Thm 5.1 + Rem 6.1. Legend: "no Liouville theorem can
exclude a nonzero constant — constants are genuine members; post-KNSS refinements
are constant-producing." Branch wording: **M3's tie face and B2 reduce to one
object (OO)** — nonzero bounded ancient mild axisym solution with `Γ ∈ L^∞`,
`Γ ≢ 0` (the survey arXiv:2101.04905's "most difficult remaining case" [V?
search-level]); **branch (a) retired as an exact-maximizer artifact**. Witness
renumbering: W1 stacked-slab, W2 outward evacuation, W3 truncated neck sheet at
`R*`, W4 fold count, **W5 initial-loading (formerly W6)**. **F-numbering:** two
competing F15 drafts were submitted in the winding pass; the winding report's §7
queue is the numbering of record — its F15 supersedes both drafts. `R₀`/C10:
resolved as **two distinct objects, both kept** — a reasoned departure from
F14/F20's "pick one": ledger §1 defines the ball radius `R₀ = 10√42Γ₀` while
ledger §4 defines the neck span `r_y ∈ [√42Γ₀, R_k]`; the automatic zone
`|w| ≤ 2√42` inside `R₀` covers the gap `[√42Γ₀, 10√42Γ₀]`, so no inconsistency.
[B]

**Post-freeze frontier (frozen):** M2 RESTRICTED (no independent members) · M3
RESTRICTED (`γ₂ < γ` dies by K4′ [(E⁺)+(P)]; the tie face merges into B2) ·
Scope-A quasi-static = **B2 alone**, killed by R-B2′ [C] conditional on
(COH-Δ) + (ANCH) + (P) (+ (N-Γ) [C-dict]); (NECK) = standing extension request
(`θ_coh`, `ℓ_neck`); fork (β) — the dictionary declines the neck level bound,
`sup(ω_θ/r)`, and `ℓ_neck`; all three in-house vehicles are retired or blocked
(budget/winding by F15–F18; the level route and T4-with-a-sign by the fork-(β)
declinations). BH verdict **YELLOW-RED maintained**; no CAP trigger.
