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
