# Swirl-fraction gap (★) — P0 probe: s(u) on the known families, A_NS, CLV F → 0 limit

Date: 2026-08-19 (JST). Task: BH/NS task table (math-physics view), P0 rows. One bounded
pass; stop rules: no simulation, no new ansatz, no K12 promotion, no map edits — observed
(one soft note in §6). Baseline: `BH_QUANTITATIVE_RIGIDITY_K12_AUDIT.md` (YELLOW, (★)
designated). Process: four analysts + two adversarial verifications + completeness critic
(parallel agents); primary texts **read in full this pass**: Gavrilov arXiv:1810.08020
(7 pp.), Constantin–La–Vicol arXiv:1903.11699 (15 pp.). Tags: [H] hard, [V] verified from
the primary text today, [C] conditional, [C-num] conditional on truncated-series
arithmetic, [B] bookkeeping.

## 1. Verdict — YELLOW (grade unchanged; the content inverts twice)

- **Against the gap:** (★) as literally stated is likely answered **NO**: inside the
  Gavrilov/CLV construction itself there is an explicit candidate family with
  `s → 0` (§2.3), conditional on one unproved continuation lemma [C].
- **Against the branch:** the realizing family is geometrically a thin sheet wrapping a
  separatrix with `r_min/R ~ s` and thickness `~ s²`; in frozen variables both scales fall
  below the viscous cutoff `√(ντ)` on the **entire interior blob wedge** (`γ > 1/2`), by
  two independent power counts [C]. So a NO answer to (★) does **not** produce a seed.
- **Consequence: (★) has decoupled from the branch verdict.** Its naive decision rule
  ("`s → 0` family ⇒ YELLOW-GREEN") is **retired as stated**; the geometry-weighted
  replacement (★_geo) is defined in §5 and is the next decision-relevant object.

Not YELLOW-GREEN: the `s → 0` family is [C] (continuation unproved, constants [C-num])
and viscously unrealizable in-window. Not YELLOW-RED: no surviving evidence for a naked
gap `inf s > 0`.

## 2. P0(i) — s(u) on the known families

**There is no single "value of s" — s is a functional of the localization cutoff `ω(p)`**;
what is computable is the level-shell profile `σ(A)` and the range of its `ω²`-weighted
averages. Results (every headline number independently re-derived by the verifier from
both primary texts; the two papers agree through the exact dictionary `φ = α_G/2`,
`a(φ) = H(α)/(12α)`):

1. **Core pinning [V]+[H], four independent routes.** At every CLV/Gavrilov localization
   point the swirl fraction is forced: `α(0) = r₀²/3`, i.e. pointwise
   `u_θ²/|u_pol|² = 1/2` and `u_θ² = |u|²/3`. Routes: CLV's own (52) [V]; positivity of
   `|∇ψ|²` forcing `w = β − 3α → 0` for **every** admissible free function `M` [H]; the
   closure identity for thin tori (`c = 1/3`) [H]; the exact first-integral inversion
   [H]. The "3" descends from Gavrilov's `p = p(ψ)` trick. Full cylindrical
   equipartition follows: `∫u_r² = ∫u_θ² = ∫u_z² = E/3`.
2. **Published (small-shell) constructions:** `σ(A) = 1/2 − (21/32)A + O(A²)` [H],
   hence `s = 1/2 − (21/16)δ² + O(δ⁴)` at aspect `δ` — the `O(δ)` term **vanishes**;
   thinner tori push `s ↑ 1/2`. The Gavrilov cutoff and CLV Thm 3's multiscale freedom
   (amplitude/scale/translation/rotation) are exactly the `s`-null directions: regularity
   is traded (their `C^{1/3}` families), `s` is not. Seeded prediction `s ≈ 1/2`
   CONFIRMED — mechanism: the ODE compatibility ratio 1/3 (the near-planar-isotropy
   heuristic gives the same number; the verifiers warn the coincidence must not be
   over-read).
3. **The corrected range is `(0, 1/2]`, not a neighbourhood of 1/2 [C].** The two
   analysts' escape-blocking argument was **refuted structurally** (series-free): if a
   poloidal level curve touches the axis, `C¹` regularity forces `Γ = F(ψ) = 0` on it —
   "level reaches the axis" and "swirl vanishes on that level" are the *same* event, not
   sequentially ordered ones. Continuing the local solution outward it is a Hill-type
   cell whose outermost streamline touches the axis with `F = 0` there; cutting `ω` in a
   thin shell against that separatrix yields smooth compactly supported axisymmetric
   steady Euler flows with
   **`σ(A) ≃ 0.82·√(A_H − A) → 0`** [C-num for the constants; qualitative mechanism
   series-free]. The single load-bearing gap: neither paper proves the local solution
   continues to the separatrix (`ε` never quantified); no interior obstruction exists
   (no critical values between core and axis level) [H], but that is not an existence
   proof. **First (conditional) answer to the audit's §8.2 probe:
   `inf_{A_NS} s = 0` [C].**
4. Consistency [H]: the family satisfies (S-ID) exactly in the limit —
   `∫u_θ² → 0 ⟺ ∫u_r² → 2∫u_z²` (critical oblateness `q → 2`), realized by
   radially-tangent axis-touching tips; and it sits inside the F→0 classification's one
   open corridor with `ρ_a = r_max/r_min ~ 1/s`, satisfying the proved per-streamline
   rate `ρ_a ≳ ε_loc^{−2/3}`. The `s ↔ F→0 ↔ (S-ID)` triangle is consistent everywhere.

## 3. P0(ii) — the admissible class A_NS

**Definition (primary).** `u ∈ A_NS` iff (A1) `u ∈ C¹(R³)` — no norm bounds; (A2)
axisymmetric; (A3) ∃p: `div u = 0`, `div(u⊗u + pI) = 0` in `D′`; (A4) `u ∈ L²`,
`p ∈ L¹_loc`, and the ring-vanishing condition (L):
`liminf_{R→∞} ∫_{R≤|x|≤2R}(|u|²+|p|) = 0`; (A5) `u ≢ 0`. Then `s(u)` is well-defined and
(S-ID) holds [H]. Notes: (L) — not `o(|x|^{−3})` — is the sharp localization for the
momentum-flux identity; **no normalization is needed** (`u_pol ≡ 0 ⇒ u ≡ 0` via (S-ID));
(S-ID) does not even need axisymmetry. A priori `q = ∫u_r²/∫u_z² ≤ 2` on the whole
class: **no localized steady flow is oblate beyond the critical value**, and `s → 0` is
exactly the approach to critical oblateness.

Optional strengthenings (each only weakens a kill): compact support; `C^{1,β}`/`C^∞`;
support geometry (blob/ring); single-valued GS data; CLV localizability; nondegenerate
foliation. NS-side items (fixed-ν realizability, frozen exponents, K9) belong to the
**interpretation step**, packaged as the δ-stable operational form
`(★_δ)`: flows with NS-residual `≤ δ·∫|u|²` in weighted-`L¹` have `s ≥ c` — whose error
term is exactly the Gate-E residual table.

Population [V]/[C]: Gavrilov is the **only known witness of the primary class**
(`C^∞`, compactly supported, off-axis torus); CLV Thm 2/3 are Hölder-only, hence members
of the weak variant `A_NS^weak` (`L²_loc`, distributional) only; mollification does not
repair this. The fluid-sense on-axis blob subclass has **no known member** — sharpened
this pass by the verified structural fact: *a CLV-localizable compactly supported flow
has `u ≡ 0` on the entire axis* (stagnant axis; vortex-ring topology — not a kill, a
constraint) [H]. **Required amendment after §2.3:** (★) over the naked A_NS admits the
sheet-degenerate `s → 0` family, so any future use of (★) as a kill criterion must carry
a uniform-nondegeneracy (support-geometry) qualifier — see (★_geo), §5.

## 4. P0(iii) — the CLV localizability constraint as F → 0: classification

Status of the identity [V]: `|∇ψ|² + F² = 2r²A(ψ)` is CLV's **definition** of
localizable (⟺ `p = p(ψ)` ⟺ `|u|² = 2A(ψ)`, speed a streamline function); sufficiency
only — **necessity for compact support is never claimed and remains the decisive open
scope question.** All theorems below are Scope A (localizable); Scope B is untouched.

Machinery proved and verified [H]: the curvature identity
`κ = r²p′/(√(2A)W) − α sinθ/(rW²)` (at `F = 0`: `κ = λ(ψ)r`); the closure identities
`∮κ dr = ∮κ dz = 0`; the exact first integral `sinθ = (r/W)(λr²/2 + K)`; the CLOSURE
relation linking `λ|Ω|` to the swirl boundary term. Standing hypotheses (flagged by the
verification): regular closed streamlines, no `r² = α` stratum (pure-swirl stagnation),
no positive-measure stagnation set.

**Classification (corrected per the verifications and the critic):**

| sector | outcome |
|---|---|
| `F ≡ 0`, localizable | no nontrivial solution [H] — a clean 5-line reproof, but **redundant** (strictly inside Jiu–Xin's class); value = machine-check |
| `F ≠ 0`, radially thin (`r_max/r_min → 1`) | **value pinning, not contradiction**: `α/r² → 1/3`, `s → 1/2`; contains all published constructions |
| `F ≠ 0`, wide aspect (`ρ_a → ∞`) | **SURVIVING FAMILY (conditional)** — the corridor where §2.3's family lives; rate-constrained: per-streamline `ρ_a ≳ ε_loc^{−2/3}` [H under convexity], globally `ρ_a ≳ s^{−1/5}` [C] |
| non-localizable compactly supported (Scope B) | open — decisive |

So the P0(iii) answer is **(3) SURVIVING FAMILY**, conditional on the continuation lemma —
not (1) contradiction, not (2) unavoidable degeneration alone. (The degeneration content
survives inside it: the family *must* degenerate in radial aspect, quantitatively.)

## 5. The decision-relevant synthesis — (★) decoupled, (★_geo) armed

In frozen blob variables (`R ~ τ^α`, `s = ε² = τ^{2(γ−α)}`), the candidate `s → 0`
family has inner radius `r_min ~ s·R ~ τ^{2γ−α}` and sheet thickness `~ s²·R ~ τ^{4γ−3α}`.
Both are below the viscous cutoff `√(ντ) ~ τ^{1/2}` precisely when `γ > 1/2` — i.e. on
the **whole frozen interior window**, by two independent power counts [C, inheriting the
audit's V1-level realizability premise]. Hence:

- a NO answer to (★) (which this pass makes likely) does **not** open a YELLOW-GREEN
  seed: the only realization known is not NS-realizable in-window;
- the branch-deciding object is the geometry-weighted gap
  **(★_geo): prove or refute `s(u) ≥ c · r_min/r_max` (exponent θ = 1) on the
  localizable class** — the global upgrade of the proved per-streamline aspect bound.
  Decision table [C]: `θ ≥ 1/2` empties the interior blob wedge under the viscous
  cutoff; `θ = 1/5` (all that is proved today) leaves only the sliver
  `3α + 2γ < 5/2`; the explicit family sits at `θ = 1`.

**Next single bounded task:** settle the aggregation gap — upgrade the per-streamline
bound to global `s ≥ c·(r_min/r_max)^{1/θ...}`-form and fix θ. Algebraic, bounded, uses
machinery already in hand (CLOSURE, first integral, level densities `M ≡ π/2`,
`R(A)+Θ(A) = 2Z(A)`), needs no continuation lemma and no literature access. Runners-up
(deliberately not next): the continuation lemma (settles (★), not the branch);
necessity of localizability (decisive but open-ended); Jiu–Xin's primary hypothesis
class (bundle as a literature errand).

## 6. Debts, corrections, and process notes

- **Withdrawn within the pass** (verifier/critic rulings): the two s-analysts'
  "family pinned near 1/2 / cannot reach s → 0" [refuted — the escape-blocking root
  comparison was structurally impossible]; clv-f0's headline "no surviving family [H]"
  [scope error — its own §6/§7 said otherwise]; "on-axis blob dies" [proved: stagnant
  axis only]; the verifier's proposed level-by-level tensor identity `P(A) = 4A·M(A)`
  [inconsistent — withdrawn; the salvageable level-by-level fact is
  `R(A) + Θ(A) = 2Z(A)`].
- **Soft stop-rule note:** several root-orderings/constants were decided by truncated
  symbolic series arithmetic ([C-num]); one such decision (the refuted root comparison)
  was wrong. No solver/simulation was run. Rule adopted: no verdict rests on a [C-num]
  number — §1's verdict rests only on the series-free structural argument and integer
  power counting.
- **Open items carried:** the continuation lemma (§2.3); necessity of `u·∇p = 0`
  (Scope B); Jiu–Xin primary hypothesis class (still second-hand); whether `σ(A) → 0`
  survives CLV's general free function `M` (only `A` linear checked); (L) for rescaled
  Leray profiles; θ-aggregation (the designated next task).
- No map edits, no K12 change, no new ansatz, no Lean changes. The audit's §6 decision
  rule ("`s → 0` ⇒ YELLOW-GREEN") is superseded by §5 of this report at report level;
  the frozen survival map is unchanged.

## Erratum (2026-08-19, geometry-gate pass — see `BH_GEO_SWIRL_AGGREGATION_2026-08-19.md`)

Appended, not silently repaired:

1. §5's "θ = 1/5 (all that is proved today)" and "θ ≥ 1/2 would empty the interior blob
   wedge" were written in the **reciprocal** (`ρ_a`) exponent convention; in the mandated
   convention (`s ≥ c·δ_geo^θ`, `δ_geo = r_min/r_max`) they read θ = 5 and θ ≤ 2
   respectively. Both are **superseded**: the geometry-gate pass proved θ = 1 (sharp),
   and the exact wedge-emptying threshold under the [C] viscous premise is θ < 4.
2. §4's classification-row rate "`ρ_a ≳ ε_loc^{−2/3}` [H under convexity]" is vacuous
   (the geometry-gate theorem gives `ε_loc² = α/r_min² ≥ 1/42` universally) and is
   replaced by the linear, hypothesis-free `ρ_a ≥ 1/(157·s)` on Scope A.
3. §1/§5's "(★) is decoupled..." framing stands, but the decision object (★_geo) is now
   **answered** (Outcome A, θ = 1) rather than open.
