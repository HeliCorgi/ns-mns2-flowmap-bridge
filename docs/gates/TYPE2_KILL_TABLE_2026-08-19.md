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
| K4 | KNSS Acta 2009 (Liouville) | axisym, `|v| ≤ C r^{−1}` ⇒ regular (`ε = 0` endpoint of K3) | candidates with `sup_x u·r < ∞`; blob window: automatic violation (`u·r ~ τ^{α−γ} → ∞`) — no new cut | [V?] (abstract not refetched; consistent with K3) |
| K5 | energy + dissipation (Leray) | `‖u‖₂` bounded, `∫‖∇u‖₂² < ∞` | blob: `α < 2γ/3` or `α ≤ 2γ−1`; ring: `ρ+2α < 2γ` or `ρ ≤ 2γ−1` | [H]+[B] |
| K6 | ESŠ 2003 / Seregin 2012 | `‖u‖_{L³} → ∞` necessary | core-carried-`L³` variants: blob `α ≥ γ`; ring `ρ+2α ≥ 3γ`. Swirl-dominated core (`σ = γ`, at `r ~ R`): **arithmetically incompatible** with core-carried `L³` ([D2], via `Γ` max principle `γ ≤ ρ`) — forces ≥3-region structure | [H]+[B] |
| K7 | Tao 2019 (triple-log lower bound on `‖u‖_{L³}`) | quantitative ESŠ rate | cuts only sub-power-law `L³` growth; **no cut** on power-law ansätze | [H], vacuous here |
| K8 | transport/diffusion displacement | hypothesis (T): structure advected + diffused | ring: `ρ < min(1−γ, 1/2)` excluded; blob: no cut (no translation) | [C] ([D1′]; replaces withdrawn [D1]) |
| K9 | swirl-component criteria family (Lei–Zhang / Wei-type: regularity if `|u_θ| ≤ C r^{−d}` for some `d < 1`) | **to verify** | if the family holds: core swirl must violate every `d < 1` bound: `σ ≥ d·α` for all `d < 1` ⟹ `σ ≥ α`; with `Γ` max principle (`σ ≤ α`) ⟹ **`σ = α` exactly**: the core must carry `Γ ~ O(1)` circulation while remaining amplitude-subdominant (`σ = α < γ`) | [V?][C] |
| K10 | Seregin note arXiv:2402.13229 (Euler-scaling treatment of a Type II scenario; revised 2026-08) | abstract too thin to extract `K_j` | none claimed; full-text extraction is the outstanding [V2] item | [V?] open |

## 2. Resulting survival set

**Blob (on-axis, core carries `L³`):**
`S_blob = {(γ, α) : 1/2 < γ < 1, max(2γ/3, 2γ−1) ≤ α < γ}` — **unchanged by today's
audit** (K3/K4 violations are automatic inside it; K8 does not apply to a non-translating
core). Conditional refinement from K9: the swirl exponent on its fibers is pinned to
`σ = α` — an amplitude-subdominant core carrying `O(1)` swirl circulation.

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

## 4. Verification debts (explicit)

1. K4: refetch KNSS abstract/statement for the exact `|v| ≤ C/r` form and solution class.
2. K9: identify the exact swirl-component criteria (authors, exponent ranges, solution
   class); only then does `σ = α` become load-bearing.
3. K10: full-text extraction of the Seregin note (which Type II scenario, which weighted
   bounds, what is proved) — the note was revised this month; the area is moving.
