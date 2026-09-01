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
*(This frontier block is superseded by the round-2 closing block below —
Annotation 2026-08-21 (round 2), B2/B11.)*

## Annotation 2026-08-21 (round 2; authorized by `FREEZE_REVIEW_2_2026-08-21.md`, user's amended adjudication)

Executes the Scope-B reconnaissance queue F21–F29
(`BH_SCOPEB_RECON_2026-08-21.md`) and the anchor-audit queue F30–F36 + C6
(`BH_RB2_ANCHOR_AUDIT_2026-08-21.md`), with the user's amendments on
F21/F29/F31/F33/C6. Master record: `FREEZE_REVIEW_2_2026-08-21.md`.

**B1 (scope legend — F21 as amended).** The **theorem/arithmetic content** of
every row K1–K11, K4′–K4‴ and of R-NEG1–R-NEG6 is **SCOPE-FREE** (no profile
equation consumed in the statement or its arithmetic; K8 keeps its `[C on (T)]`
tag; K4 scope-free *as a statement*); `S_blob` is unchanged in Scope B. This
does **not** declare every row's *applicability* settled in Scope B: (P),
K8-on-multi-region-tuples, and the intra-core `β_v ∈ (α,γ]` limb remain
**unresolved** (recon §4). Scope-A dependence enters the map only through the
geometry gate's one-parameter elliptic-orbit rigidity and its corollaries, and
through the **exhaustiveness step** (B2 below).

**B2 (R-B2′ scope rider + target partition + frontier narrowing — F33;
supersedes F22 and the "no Scope-A geometry" clause as printed in A15 /
FREEZE_REVIEW §3 **and §5** / constant-exclusion §2 / ledger §1).** In A15 read
"no Scope-A geometry" as "**no Scope-A aggregation machinery**" (`δ_geo`,
`1/157`, θ, convexity), and "the Γ-saturated level (amplitude corollary)" as
"the **amplitude**-saturated level" (the corollary caps `Γ(L)`; it does not
bound it below). The row's target, partitioned by the co-location exponent
`β_v` (B13):
- **(T1)** tie face (`ρ₁ = σ₁ = γ₁ = γ` by class definition): anchor
  definitional; **R-B2′ scope-free there**, modulo (E⁺⁺)/(P); (N-Γ)
  definitionally discharged **[C-dict], per B11**;
- **(T2)** `B2 ∩ {β_v = γ}` ("a B2 point wearing a Γ-saturated sub-core"): in
  Scope A the anchor is derived from the amplitude corollary; **granting
  membership (i.e. `β_v = γ` as a class clause), the row's machinery is
  scope-free** — the basis of the frontier's "[C] target" phrasing; in Scope B
  this sub-class has **no defining clause in the corpus — undefined, not
  merely anchorless**;
- **(T3)** `B2 ∩ {β_v < γ}` (incl. K9's razor limb `β_v = α`): **empty in
  Scope A by the amplitude corollary; live and never claimed in Scope B** —
  R-B2′ has no zoom centre there. *(This narrows A2's `β_v ∈ (α,γ]` open debt
  **in Scope A** to its endpoint `β_v = γ`; the limb stays fully open in Scope
  B — its home as (SB-ANCH), B6/B13.)*
**The Scope-A gate is the exhaustiveness step** — "every Scope-A blob is
two-scale in the tongue sense" (multiregion §2), i.e. every Scope-A B2
candidate *enters* the Γ-saturated realization — **not the zoom**. Frontier
sentences reading "Scope-A quasi-static = B2 alone, killed by R-B2′" are
**replaced** by: "Scope-A quasi-static = B2; **its Γ-saturated realization is
the target of R-B2′ [C]**; Scope A supplies the exhaustiveness theorem that
every Scope-A B2 candidate enters that realization."

**B3 (DVEP recording corrected — F23; supersedes the DVEP clauses of A8's
rationale and multiregion §6.2).** DVEP (arXiv:2005.04380): the **authors
assert** non-localizability (abstract; §1 "not localizable in general");
**no proof is located in the paper** and no failure point is identified. DVEP
is an *asserted*, not a verified, Scope-B witness. A8's rationale clause
"`p = p(ψ)` necessity is false without regularity hypotheses" is replaced by
(recon C10): "**no necessity proof exists at any regularity; the authors
assert non-necessity at weak regularity without proof.**" A8's ruling is
unaffected (it turns on `A_NS` membership: the velocity jump is structurally
forced — Neumann `c > 0`).

**B4 (gate verdict sentence patched — F24; supersedes
BH_GEO_SWIRL_AGGREGATION l.203–204 as printed).** The BH-verdict sentence now
reads: "a single non-localizable localized steady flow **inside the primary
class `A_NS`** would restore YELLOW immediately." Trigger (A8) and verdict now
agree; DVEP meets neither.

**B5 (trigger status — F25).** "Trigger status at the 2026-08-21
reconnaissance — **(T-c)** = the OPEN verdict label (introduced in
`BH_SCOPEB_RECON_2026-08-21.md` §1) for the geometry-gate §10 CAP-revisit
trigger's **Scope-B limb as amended in A8**: **OPEN, no fire.** Its two
sub-limbs (localizability shown non-necessary inside `A_NS` / a
non-localizable witness inside `A_NS`) are both unmet; neither is unreachable.
Reasons: DVEP outside `A_NS` by (A1), and DVEP's non-localizability unproved
in-paper. The forcing direction is empty in 3D (all three papers with
localizability as their subject assume it). No CAP fire. Next mandatory
re-check: whenever a `C¹` compactly-supported non-localizable 3D witness, or
any regularity ⟹ localizability theorem, is published." *(Label hygiene:
(T-c) is unrelated to the target classes (T1)/(T2)/(T3) of B2, to K8's
hypothesis (T), and to the budget term T4.)*

**B6 ((SB-ANCH)-final — F32, cited by F26).** Supersedes recon §4's one-line
form. **(SB-ANCH):** ∃ `c, c′ > 0` τ-uniform and, along `τ_k → 0`, points
`x_k` with **(H1)** `|u_θ(x_k,t_k)| ≥ c‖u(t_k)‖_∞` (sup-swirl saturation) and
**(H2)** `|Γ(x_k,t_k)| ≥ c′Γ₀` at the same point (co-located Γ-saturation).
`(H2) ⟹ (H1)`; `(H1) ⇏ (H2)`. The distance clause
`dist(x, axis) ≤ CΓ₀/‖u‖_∞` is derivable from (H1) + Γ-max [D] and is
**deleted as a hypothesis**. Single equivalent form: the scope-free envelope
`Γ(r) ≤ min(Γ₀, r‖u‖_∞)` is attained within a constant at its corner
`r = Γ₀/‖u‖_∞` — i.e. **`β_v = γ` in the sense of B13**. Scope A supplies (H1)
with `c = 1/√42`, and (H2) only on `ρ_T = γ`. **Rider (load-bearing): granting
(SB-ANCH) does NOT transplant R-B2′ to Scope B** — it supplies a level, not a
labelled region; the ledger's tip/solenoid rows and (E⁺⁺)/(NECK) need a
poloidal-exponent and thickness assignment (the labelled-region /
exhaustiveness side), a separate and independent requirement.
**Standing Scope-B open question (print form, F26's first half, recon §1
verbatim):** *"Does there exist `u ∈ C¹(R³)`, axisymmetric with swirl,
non-trivial, solving steady Euler distributionally with `u ∈ L²`,
`p ∈ L¹_loc` and `liminf_{R→∞} ∫_{R≤|x|≤2R}(|u|²+|p|) = 0`, such that
`u·∇p ≢ 0` (equivalently `u·∇|u|² ≢ 0`)?"*

**B7 (literature ledger — F27).** arXiv:2606.13462 (Peralta-Salas–Slobodeanu
2026: localizable + analytic ⟹ axisymmetric — converse direction; corroborates
Scope-A ring topology) and arXiv:2608.11547 (Sato–Abe 2026: assumes
`p = p(ψ)`) added. Legend: "three papers take localizability as their subject;
all three assume it."

**B8 (debts — F28).** Jiu–Xin CMP 287 (2009) body: **paywalled, never read**;
usable surrogate = CLV's verbatim citation ("must vanish identically if the
swirl F vanishes") + DVEP's citation ("axisymmetric stationary Euler flows of
compact support without swirl do not exist [8]"); the unqualified gloss cannot
be used without the **no-swirl qualifier**. DVEP's (A4)/(L) check: exterior
pressure is a nonzero constant; the repair (`p → p + const` gauge) is
cost-free — discharged [D].

**B9 (Scope-B legends — F29 as amended).** (E⁺⁺)/(COH-Δ)/(ANCH-κ)/(NECK)/
`θ_coh`/`ℓ_neck`/T4/W1–W5 are **undefined, not open, in Scope B**. The
per-level swirl-fraction bound is **FALSE outside Scope A** (Hill) — no
Scope-B analogue can be a weakening. Direction legend: `σ_sup = γ` and the
forced tongue are Scope-A *escape* structures; their loss in Scope B
strengthens K9's `σ ≤ α` half and K6's [D2] **as a loss-of-escape statement
only — this is NOT a proof of any new kill** (user's rider). *(Recon §4's
"K9's `σ = α` razor" is superseded by A2's trichotomy — the strengthened
object is the `σ ≤ α` half.)*

**B10 (A15 transparency — F30).** R-B2′'s printed conditionality list is to be
read as: (E⁺⁺) = (COH-Δ)+(ANCH-κ), (P), (N-Γ)[B11], **plus the imported
layer**: `(E⁺)` = (E) + C¹-exhaustiveness within `τ^{(γ+β)/2}` of the zoom
centre (A16 legend; **not** the ledger ball radius `R₀` — a distinct object,
per A20) and the `frozen dictionary [C-dict]` (the ledger chain's first input,
ledger §1) — previously listed by reference only.

**B11 ((N-Γ) status split — F31 as strengthened by the user).** (N-Γ) is
**not** blanket [C-dict]. Split by the tip exponent:
- on **(T1) / `ρ_T = γ`**: discharged **[C-dict]** (definitional / saturation
  at the anchor scale);
- on **`ρ_T > γ`**: **[C] — discharge unsupplied**, even in Scope A: the
  second scale is capped (`ρ_T ≥ γ`), not pinned (multiregion §2), and Γ's
  exact scale invariance (A11) puts the centre's rescaled
  `Γ ≍ τ^{ρ_T−γ} → 0` there. The constant-exclusion §1 phrase "dischargeable
  from τ-uniform saturation" is superseded on this branch — **as are the
  unqualified `[C-dict]` tags printed on-map in A15's chain line and A16's
  legend entry for (N-Γ), and FREEZE_REVIEW (round 1) §5's "…plus (N-Γ) at
  [C-dict]": all are to be read as (N-Γ)[B11 split].**
This split is printed to prevent conditionality inflation at future audits.

**B12 (naming — F34, user's choice).** The κ̂-level/erasure statement inside
(E⁺⁺) is renamed **(ANCH-κ)** everywhere it is printed on-map: **A15's row
list** (`(E⁺⁺) = (COH-Δ) + (ANCH)`), **A16's decomposition**, **A19's "sole
carrier of (ANCH)"** (the T4 legend, adopting F20), and the round-1 closing
block (already superseded wholesale). R-NEG6's "it is not an anchor" refers to
`κ̂ ≤ τ^{2ρ−γ−α}`, not to (ANCH-κ), and needs no rename. FREEZE_REVIEW
(round 1) §5's "the conditional frontier is now exactly three named objects:
(COH-Δ), (ANCH) … plus (N-Γ) at [C-dict]" is **superseded twice over** (this
rename + B11's split). The Scope-B re-centring-anchor gap keeps the name
**(SB-ANCH)**. The two are unrelated objects.

**B13 (`β_v` legend — F35 as amended).** `β_v` = the co-location /
saturation-scale exponent (joins `σ_core`/`σ_sup`, A1/A2): the exponent of the
radius at which `Γ` attains `≍ Γ₀` relative to the amplitude scale.
**`β_v = γ` means the τ-uniform constant-attainment of the envelope
`Γ(r) ≤ min(Γ₀, r‖u‖_∞)` at its corner `r = Γ₀/‖u‖_∞` — NOT a bare exponent
equality.** (This is what makes B6's "single equivalent form" safe.)

**B14 (internal consistency — F36 + C6 as fixed by the user).** Fork-(c)
operative definition, frozen: **fork (c) fires ⟺ an UNLISTED, INDEPENDENT,
IRREDUCIBLE Scope-A input is discovered.** Multiplicity of anchor
*appearances* does not fire it — downstream usages derived from the same input
are not new conditions (of the audit's four anchor-touch sites, one is
irreducible: the zoom-centre selection — **which is the anchor itself, listed,
not unlisted: fork (c) does not fire**, audit §3). Recon §8's wording
("consumes the anchor more than once") is **superseded**. Doc pointer
corrected: B2/K9/amplitude-gate structural content lives in
`BH_MULTIREGION_AUDIT_2026-08-20.md` §§1–3 + kill-table annotations A1–A3, not
in `BH_SWIRL_FRACTION_PROBE_2026-08-19.md`.

**Post-round-2 frontier (frozen; supersedes the round-1 closing block):**
M2 RESTRICTED (no independent members) · M3 RESTRICTED (`γ₂ < γ` dies by K4′
[(E⁺)+(P)]; tie face merges into B2) · **Scope-A quasi-static = B2; its
Γ-saturated realization is the target of R-B2′ [C]** on
(E⁺⁺) = (COH-Δ)+(ANCH-κ), (P), (N-Γ)[B11 split] (+ imported layer: (E⁺),
frozen dictionary [C-dict] — B10), with the exhaustiveness step as the Scope-A
gate; (NECK) = standing dictionary-extension request (`θ_coh`, `ℓ_neck`);
fork (β) — the dictionary declines the neck level bound, `sup(ω_θ/r)`, and
`ℓ_neck`; all three in-house vehicles retired/blocked (budget/winding by
F15–F18; level route and T4-with-a-sign by the fork-(β) declinations) ·
**Scope B: B2 UNKILLED**; first named gap **(SB-ANCH) ⟺ `β_v = γ` (τ-uniform
corner attainment, B13)**, with the B6 rider that (SB-ANCH) alone does not
transplant R-B2′; one-scale ring and M2 reopen in Scope B; **M3 `γ₂ < γ`: K4′
transports as a scope-free statement, the kill stays conditional on
(E⁺)+(P), and (P)'s Scope-B status is unresolved (B1)**; trigger (T-c) OPEN
(B5) · BH verdict **YELLOW-RED maintained**; no CAP trigger.

*(This frontier block is superseded by the post-round-3 frontier below,
2026-09-01.)*

## Erratum & freeze queue F37–F43 (2026-09-01, synthesis audit — appended, not silently repaired; nothing below edits a row or annotation until user-adjudicated at freeze review round 3)

**F37 (MAJOR — B6/F32, the clause "`(H2) ⟹ (H1)`; `(H1) ⇏ (H2)`").** False as
printed once the distance clause is deleted: (H2) yields `|u_θ| ≥ c′Γ₀/r` and no
upper bound on `r` (the envelope bounds `r_sat` only from below; Γ-max bounds `r`
above only given (H1)). Corpus counterexample: every `β_v < γ` configuration has
(H2) at `r_sat ≍ τ^{β_v}` with `|u_θ|(r_sat) = o(‖u‖_∞)` — (H1) fails (B2 (T3);
`BH_BETAV_ENDPOINT_PINNING_2026-08-23.md` P4(ii)). Proposed replacement, verbatim
from the anchor-audit erratum E1:
> Neither pointwise implication holds after the distance-clause deletion:
> `(H1) ⇏ (H2)` and `(H2) ⇏ (H1)`. What is true:
> `(H1) + Γ-max ⟹ r(x_k) ≤ Γ₀/(c‖u‖_∞)`; `(H2) + envelope ⟹ r(x_k) ≥ c′Γ₀/‖u‖_∞`;
> hence the conjunction `(H1) ∧ (H2)` ⟺ τ-uniform attainment of the envelope at its
> corner — `β_v = γ` in the B13 sense.
B6's single equivalent form, the B6 rider, and the frontier's "(SB-ANCH) ⟺
`β_v = γ`" line consume only the conjunction and stand unchanged.

**F38 (MAJOR — B2 (T3) and its narrowing rider).** "Empty in Scope A by the
amplitude corollary" is unproved as cited on `ρ_T > γ`: the corollary supplies (H1)
and caps `Γ(L)` (B2's own F31 clause, printed in the same annotation); on
`ρ_T > γ` — live in Scope A (multiregion §2 "capped, not pinned"; B11 "even in
Scope A") — the level's `Γ_L ≍ Γ₀τ^{ρ_T−γ} → 0`, and no recorded row locates
Γ-saturation at the corner. T3-emptiness would mean Scope A supplies (H2) on all of
B2, contradicting B6's co-frozen "(H2) only on `ρ_T = γ`". Proposed replacement of
the (T3) bullet:
> **(T3)** `B2 ∩ {β_v < γ}` (incl. K9's razor limb `β_v = α`): **empty in Scope A
> on the `ρ_T = γ` sub-branch by the amplitude corollary; NOT established empty on
> `ρ_T > γ` (the corollary supplies (H1), never (H2) — F31's capping direction);
> live and never claimed in Scope B** — R-B2′ has no zoom centre there. *(This
> narrows A2's `β_v ∈ (α,γ]` open debt in Scope A to its endpoint `β_v = γ` **only
> on `ρ_T = γ`**; on `ρ_T > γ` the limb stays open in Scope A as well, absent a
> (Γ-DEP)-type location theorem; in Scope B it stays fully open — its home as
> (SB-ANCH), B6/B13.)*
Source: anchor-audit erratum E2, which enumerates the superseded downstream print
sites (`FREEZE_REVIEW_2_2026-08-21.md` §3; `BH_BETAV_ENDPOINT_PINNING_2026-08-23.md`
§4/§5/§7.3; `STAGE9_DECISION_SELECTION_2026-08-23.md` §2).

**F39 (minor — §2 S_blob paragraph, the Seregin-edge identification).** Endpoint
overreach, inconsistent with this table's own K10 row and §4 debt item 3, both of
which correctly print `γ ∈ (1/2, 3/5)` **open**: `m₀ ∈ (2/5, 1)` ⟹
`m = 3m₀/(2+m₀) ∈ (1/2, 1)` ⟹ `α_S = 2−m ∈ (1, 3/2)` ⟹
`γ = α_S/(α_S+1) ∈ (1/2, 3/5)`; `γ = 3/5` requires the excluded `m₀ = 2/5`. The
wedge's `γ+α = 1` lower edge itself does extend over `(1/2, 3/5]`, so the corner
`(γ, α) = (3/5, 2/5)` is on the edge but **outside** the K10 class. Proposed
replacement sentence:
> The `γ + α = 1` lower edge is exactly Seregin's Euler-scaling class (K10) for
> `γ ∈ (1/2, 3/5)` and is under conditional exclusion pressure there; the edge's
> endpoint `γ = 3/5` (`m₀ = 2/5`, excluded from K10's range) lies on the edge but
> outside the class, so the conditional exclusion pressure does not reach it.
Same slip propagated in `TYPE2_SURVIVAL_MAP_2026-08-18.md` §7 and
`DOMINANT_BALANCE_INVERSION_2026-08-19.md` §3.1 (errata appended there).
Measure-zero, but the corner is the point Prop G's θ = 4 threshold analysis
isolates, so the identification must not silently include it.

**F40 (minor — §2 S_ring, boundary strictness of the lower envelope).** The single
strict `<` over `max(2γ−1, min(1−γ, 1/2)·[C])` wrongly excludes the face
`ρ = min(1−γ, 1/2)`: K8's row excludes only the **open** set `ρ < min(1−γ, 1/2)`,
and its source [D1′] (`D1_ADVERSARIAL_AUDIT_2026-08-19.md`) states the surviving
condition as the **non-strict** `ρ ≥ min(1−γ, 1/2)`. Strictness is correct only for
the K5 arm (`ρ ≤ 2γ−1` excluded; dissipation log-diverges at equality). For
in-window `γ ∈ (1/2, 2/3)` the binding arm is `1−γ`, so the printed set drops a
face no K-row excludes — violating the table's own format `S_survive = S₀ \ ⋃K_j`;
this is the ring analogue of the S_blob mixed-strictness that A7 repaired for the
blob only. Proposed replacement (joint form with F41):
> `S_ring = {(γ, ρ, α) : 1/2 < γ < 1, γ + α ≥ 1 (K11 — F41), 2γ−1 < ρ (K5, strict),
> min(1−γ, 1/2) ≤ ρ ([C], K8, non-strict), ρ ≤ α, ρ < γ (K3/R4),
> 2γ ≤ ρ + 2α < 3γ}` — closes at `γ = 1` (as before, from K5+K6).

**F41 (minor — S_ring was not updated with K11).** Both K11 derivations apply
verbatim at a ring core: (i) term balance — `∂ₜu ~ τ^{−γ−1}` vs convection
`U²/ℓ = τ^{−2γ−α}` and diffusion `νU/ℓ² = τ^{−γ−2α}` use only the amplitude `γ` and
the finest scale `α`, giving `γ + α ≥ 1`; (ii) energy flux — growth exponent
`−2γ+ρ+2α−1` vs convective supply `τ^{−3γ+ρ+α}` gives `γ + α ≥ 1` again (`ρ`
cancels). Yet the printed S_ring (its unconditional clauses, i.e. ignoring the [C]
K8 arm) contains K11-violating points, e.g. `(γ, ρ, α) = (0.55, 0.30, 0.44)` with
`γ + α = 0.99 < 1` — an internal inconsistency under the table's own format
`S_survive = S₀ \ ⋃K_j` (K11's row states no blob restriction; B1 declares K1–K11
arithmetic scope-free; A16 applies K11 at neck radii). Adjudication requested
between: (a) adopt the `γ + α ≥ 1 (K11)` clause (F40's joint form — shrink-only;
under the K8 arm it is implied, so only the unconditional set changes; moot for the
excluded Scope-A one-scale ring, live for its Scope-B reopening), or (b) print an
explicit blob-core-only scoping rider on the K11 row. The F40 joint form assumes (a).

**F42 (nit — A16 (COH-Δ), "lifetime `1` fails everywhere by K11").** With the
non-strict threshold (`θ_coh(ρ) ≥ 2ρ` delivered; the same sentence calls the
viscous horizon `2ρ` "exactly marginal") and non-strict K11, `θ = 1` fails iff
`ρ > 1/2` **strictly**; on the K11-equality edge `γ+α = 1` — inside the frozen
window exactly for `γ ∈ (1/2, 3/5]` (A7 makes only `α > 2γ−1` strict) — the neck
endpoint `ρ = (γ+α)/2 = 1/2` has `1 = 2ρ`: exactly marginal, not failing
(`BH_COH_WINDING` §2 item 3's own "`O(1)` only on the K10 edge `γ+α = 1`").
Proposed replacement clause:
> viscous `2ρ` exactly marginal; lifetime `1` fails everywhere by K11 **except
> exactly-marginal at the neck endpoint `ρ = 1/2` on the `γ+α = 1` edge** — and K11
> (`γ+α ≥ 1`) places the whole neck at `ρ ≥ 1/2`, i.e. entirely inside `√(ντ)` —
Superseded print sites, not rewritten there: `FREEZE_REVIEW_2026-08-21.md` §3;
origin wordings in `BH_NECK_OMEGA_BUDGET_2026-08-20.md` §1/§4 and
`BH_COH_WINDING_2026-08-21.md` §1/F16 (errata appended at both source docs). No
result moves: the marginal set is a codimension-1 edge at a single neck endpoint,
and the neck-budget MASTER RESULT (no sub-wedge survives; the outer endpoint
`ρ = γ > 1/2` always fails) is untouched.

**F43 (minor — A19's parenthetical winding form).** As a formula it silently drops
the `∫T4` and viscous Γ-defect entries of the identity it abbreviates; the
midrange/oscillation bound controls the winding term alone. Proposed corrected
print (source: `BH_COH_WINDING_2026-08-21.md` erratum E1):
> `|κ_pol(t) − κ₀ − ∫₀ᵗ T4 dt′ − ν∫₀ᵗ∮(Δ−(2/r)∂_r)Γ dθ dt′| ≤ ½ osc_loop(Γ)·TV_s(θ(t))`
A19's retirement ruling (increment vs level; input starvation) never used the false
form and is unaffected.

## Annotation (2026-09-01 freeze review round 3 — C0–C14, EXECUTED; master record `FREEZE_REVIEW_3_2026-09-01.md`; adjudication authority: the user's dated 2026-09-01 instruction)

*Label hygiene: C-numbers continue the A/B annotation series; they are unrelated to
the anchor audit's internal ledger C1–C9 and to region C of `W★`.*

**C0 (standing policy, user-directed).** **(Γ-DEP) is cited as a SUFFICIENT closer
only.** The β_v decision's "single named object" / unqualified "minimal" / "there is
no third route" claims are retired from citation (erratum E1 at source). Recorded
closure shapes for the middle limb: (Γ-DEP) [sufficient]; an outright proof of
(SB-ANCH) (never as a premise); a memberwise dichotomy `(Γ-DEP) ∨ (SB-ANCH)`. No
exclusivity among shapes is claimed.

**C1 (= F37, ADOPTED).** B6's clause "`(H2) ⟹ (H1)`; `(H1) ⇏ (H2)`" is **replaced**
by the F37 blockquote above, which is now the operative text of B6 at that point.
B6's single equivalent form, its rider, and "(SB-ANCH) ⟺ `β_v = γ`" stand.

**C2 (= F38, ADOPTED).** B2's (T3) bullet and its narrowing rider are **replaced**
by the F38 blockquote above (Scope-A emptiness on `ρ_T = γ` only). The
exhaustiveness-gate sentence of B2's closing paragraph carries the same restriction
(see the post-round-3 frontier below).

**C3 (= F39, ADOPTED).** §2's S_blob Seregin-edge sentence is **replaced** by the
F39 blockquote above (`γ ∈ (1/2, 3/5)` open; the endpoint is on the edge, outside
the K10 class).

**C4/C5 (= F40 + F41 option (a), ADOPTED).** §2's `S_ring` is **replaced** by the
F40 joint form above: K8 arm non-strict, K5 arm strict, and the new clause
`γ + α ≥ 1 (K11)` (both K11 derivations are core-shape-agnostic; shrink-only;
implied under the [C] K8 arm; live for the Scope-B ring reopening).

**C6 (= F42, ADOPTED).** A16's lifetime clause is **replaced** by the F42 blockquote
above (exactly-marginal at the neck endpoint `ρ = 1/2` on the `γ+α = 1` edge).

**C7 (= F43, ADOPTED).** A19's parenthetical winding form is **replaced** by the F43
corrected inequality above.

**C8 (= P1, ADOPTED as amended).** A2's middle-limb rider now reads: *"analysed
against the frozen scope-free rows (2026-08-23): the limb `β_v ∈ (α,γ)` is
**row-compliant on all of `S_blob`** — no scope-free pin to `{β_v ≤ α} ∪ {β_v = γ,
τ-uniform}` exists; the debt narrows to (i) the existence question (out of scope for
exponent bookkeeping) and (ii) the closure shapes of C0."* The NO side of the debt
is closed; the debt as a whole is NOT discharged.

**C9 (= P2, ADOPTED as amended).** (T3)'s Scope-B status: *"live in Scope B and, on
the frozen scope-free rows, row-compliant on all of `S_blob`; R-B2′ still has no
zoom centre there (unchanged); its Scope-A emptiness holds on the `ρ_T = γ`
sub-branch only (C2/F38)."* (P2's drafted "untouched" clause conflicted with F38 and
was amended at adjudication.)

**C10 (= P3, ADOPTED as amended).** Frontier sentence, executed in the post-round-3
frontier block: after "first named gap (SB-ANCH) ⟺ `β_v = γ`" — *"; the complement
`{β_v < γ}` is not reachable by scope-free arithmetic — the middle limb
`β_v ∈ (α,γ)` is row-compliant at every point of `S_blob`; (Γ-DEP) is a
**sufficient** closer (C0), an outright (SB-ANCH) proof closes it from the other
endpoint, and a memberwise dichotomy is a third shape; the Scope-A amplitude
corollary remains a class change, effective only on `ρ_T = γ` (C2)."*

**C11 (= P4, ADOPTED).** Two record-only true statements in the frozen vocabulary:
(i) `{β_v = γ, τ-uniform} ⟺ (SB-ANCH)`, hence `M ⟹ ¬(SB-ANCH)` and
**`{β_v < γ} = ¬(SB-ANCH)` exactly** (re-derived from Γ-max alone; consumes the
conjunction, not the C1-withdrawn implication); (ii) on **all** of `{β_v < γ}` the
flow is sup-swirl-poor at the saturation radius:
`|u_θ|(r_sat) ≍ τ^{γ−β_v}‖u‖_∞ = o(‖u‖_∞)` — (H1) is unattained there
(generalizing the anchor audit's (T3) note from `β_v = α` to every `β_v < γ`; the
same arithmetic as C1's counterexample, now a positive record).

**C12 (= P5, ADOPTED).** §2's sentence "Conditional refinement from K9: the swirl
exponent on its fibers is pinned to `σ = α` — an amplitude-subdominant core carrying
`O(1)` swirl circulation" is **struck** (superseded by A1's `σ_core`/`σ_sup` split
and A2's saturation-scale trichotomy; the 2026-08-23 decision turned on exactly that
pinning being unavailable).

**C13 (= P6, ADOPTED).** New record-only row: *"Middle-limb realization
(record-only, [B] bookkeeping): for every `(γ,α) ∈ S_blob` and every
`β_v ∈ (α,γ)`, the two-region tuple `C = (α, α, 3α, γ, 2α−β_v)`,
`S = (β_v, β_v, 3β_v, β_v, β_v)` satisfies every frozen scope-free row. This is
exponent bookkeeping and NOT a survival claim about Navier–Stokes."* (Re-verified at
adjudication: K5a/K5b/K6/K11/Γ-max/envelope pass; S sits on the `v = 3γ_j` marginal
face exactly as `W★` — OOV-1, recorded not decided.)

**C14 (= P7 / Seregin row-(i) update, ADOPTED — pressure-only, [V?]).** Seregin
arXiv:2606.29468 (28 Jun 2026) generalizes the K10 Euler-scaling class to
**log-corrected families**, again reducing exclusion to **open** ancient-Euler
Liouville theorems in scaled-energy classes. The added pressure lives on the map's
out-of-vocabulary faces (OOV-4, where the 08-23 record places exactly these
families): **scope annotation, not a new cut** — no
power-law row moves, and C3's endpoint carve-out is unaffected. **Named verification
debt [V?]: literature-watch-level extraction; full-text verification owed before any
chain consumes this row.**

**Post-round-3 frontier (frozen; the SOLE operative frontier text — supersedes the
round-2 closing block; `FREEZE_REVIEW_3_2026-09-01.md` §4 is a summary of this
block, not a second print):**
**Scope A** — quasi-static = B2; its Γ-saturated realization is the target of R-B2′
[C] on (E⁺⁺) = (COH-Δ)+(ANCH-κ), (P), (N-Γ)[B11 split] (+ imported layer (E⁺),
frozen dictionary [C-dict] — B10); the Scope-A gate is the exhaustiveness step,
**established only on the `ρ_T = γ` sub-branch (C2/F38)** — there, every Scope-A B2
candidate enters the Γ-saturated realization and A2's middle-limb debt narrows to
its endpoint; **on `ρ_T > γ`, (T3)-emptiness is NOT established even in Scope A**
(the corollary supplies (H1) and only caps `Γ(L)` — F31) and the middle limb is open
absent a (Γ-DEP)-type location theorem ·
**Scope B** — **B2 UNKILLED**; first named gap **(SB-ANCH) ⟺ `β_v = γ`** (τ-uniform
corner attainment, B13), a genuine **conjunction** (H1) ∧ (H2), neither clause
implying the other (C1); B6's non-transplant rider stands; the complement
`{β_v < γ}` is not reachable by scope-free arithmetic — the middle limb
`β_v ∈ (α,γ)` is row-compliant at every point of `S_blob`; (Γ-DEP) is a
**sufficient** closer (C0), an outright (SB-ANCH) proof closes it from the other
endpoint, and a memberwise dichotomy is a third shape; the Scope-A amplitude
corollary remains a class change, effective only on `ρ_T = γ` (C2);
`{β_v < γ} = ¬(SB-ANCH)` exactly, with sup-swirl-poverty throughout (C11) ·
**carried** — M2 RESTRICTED (no independent members) · M3 RESTRICTED (`γ₂ < γ` dies
by K4′ [(E⁺)+(P)] — K4′ transports as a scope-free statement, the kill stays
conditional, (P)'s Scope-B status unresolved (B1); tie face merges into B2) ·
one-scale ring and M2 reopen in Scope B (`S_ring` now carries K11 — C5) · (NECK) =
standing dictionary-extension request (`θ_coh`, `ℓ_neck`) · fork (β) — the
dictionary declines the neck level bound, `sup(ω_θ/r)`, and `ℓ_neck` · all three
in-house vehicles retired/blocked (budget/winding by F15–F18; level route and
T4-with-a-sign by the fork-(β) declinations) · trigger (T-c) OPEN (B5) · Seregin
log-corrected pressure on the OOV-4 faces, [V?] (C14) · BH **YELLOW-RED
maintained** · no CAP trigger · **no Clay claim**.
