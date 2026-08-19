# BH geometry gate — (★_geo) aggregation: the swirl–geometry theorem

Date: 2026-08-19 (JST). Task: BH geometry-gate brief (one bounded pass; stop rules
observed: no simulation, no new ansatz, no K12 promotion, no map edits, no Lean, no
separatrix-continuation attempt, no Scope-B attack). Baseline:
`BH_SWIRL_FRACTION_PROBE_2026-08-19.md` (P0 probe). Process: four analysts + two
adversarial verifications + completeness critic (parallel agents); every load-bearing
derivation was re-derived independently at least twice. Tags: [H] hard (twice-derived),
[V] verified from a source read, [C] conditional, [C-num] truncated-series arithmetic,
[B] bookkeeping.

**Scope stamp (P3, applies to every statement in this file):** all results are on
**Scope A** — the CLV-localizable class `p = p(ψ)` (⟺ `|u|² = 2A(ψ)`, speed constant on
streamlines). Localizability is sufficient-only; its necessity for compact support is the
decisive open question and is untouched here. Scope B (non-localizable localized flows)
remains open.

## 1. Geometry definition (ruled)

Rejected [H]: the support ratio `δ_supp = r_min(supp)/r_max(supp)` and its active-set
variant — both are **identically zero on the frozen blob branch** (the support touches
the axis; localizable + compact ⇒ `u ≡ 0` on the whole axis), making any bound vacuous
exactly where it must bite; neither is covariant with the ω-cutoff reweighting. Rejected:
radial-band energy quantiles (conflate intra-streamline aspect with inter-component
separation).

**Definition of record.** For a level ψ with closed poloidal streamline, the
per-streamline aspect `δ(ψ) := r_min(ψ)/r_max(ψ) ∈ (0,1)`. The flow-level geometry is the
**poloidal-energy barycentre**

> `δ_geo(u) := ⟨δ(ψ)⟩_{E_pol}` (arithmetic mean, weight `dE_pol`).

Properties [H]: scale/amplitude invariant; ω-covariant (the cutoff moves neither
streamlines nor `δ(ψ)`, only the weight); anti-mediant under disjoint coaxial unions
(stays between the members); nondegenerate on axis-touching blobs. The energy-median is
kept only as a reporting corollary (Markov, constant halves). Conversion: `δ_supp ≤
inf_ψ δ(ψ) ≤ δ_geo`, so any `δ_geo`-theorem implies the `δ_supp`-theorem; the reverse has
no bound.

## 2. Streamline-level input — the one-parameter rigidity

On a regular closed poloidal streamline of a `p = p(ψ)` flow, normalize `|u|² = 2A = 1`.
Then [H] (all re-derived independently by the verifier, and the constant chain re-checked
a third time by the critic):

- first integral: `u_z = k(r² − M)`, `k = A′/2`, `M = ⟨r²⟩` (time average);
- the orbit's time measure is the explicit elliptic measure
  `dν_σ ∝ dy/√((1−y²)(1+σy))` on `y ∈ [−1,1]`, with a **single parameter** `σ ∈ (0,σ*)`;
  `σ → 0` is the radially-thin end (`δ → 1`), `σ → σ*` the axis-grazing end (`δ → 0`);
- exact identity `3⟨y²⟩_σ + (2/σ)⟨y⟩_σ = 1`, equivalently **`⟨u_z²⟩ ≡ ⟨|u|²⟩/3` per
  connected component** — the level identity `R + Θ = 2Z` holds component-wise, with no
  ω-machinery, no (S-ID), no localization: pure coarea + the first integral;
- `u_r² = 1 − α/r² − k²(r² − M)²` is a function of `r` alone ⇒ exactly two turning
  points ⇒ **the old per-streamline convexity hypothesis is retired**, not weakened;
- the level state is a one-parameter family: `(δ, s_level)` traces a graph
  `s_level = S(δ)` (monotonicity proved via Chebyshev association) — the level swirl
  fraction is **determined** by the level aspect ratio.

New structural corollaries [H]: `|u| = 0` at every elliptic centre of a localizable flow
(this *is* the CLV (52) pinning); the pointwise swirl fraction at the inner turning point
is universally bounded: `α/r_min² ≥ 1/42`; interior separatrices with `r_min > 0` cannot
occur on `A > 0` levels; the `A = 0` levels carry zero energy weight.

## 3–4. The aggregation and the global inequality (Outcome A)

Aggregation is **linear and lossless** at θ = 1: `s(u)` is the `(R+Z)`-weighted average of
`s_level(ψ)`, and `δ_geo` is the same-weighted average of `δ(ψ)`, so the per-level bound
integrates with no Jensen/Markov loss. The feared level-weight adversary (ω
concentration) *is* the single-level problem, which is solved exactly. The five danger
regions (separatrix, axis, thin-shell weighting, stagnation, `A → 0` levels) are each
neutralized ([H]; the fifth was found by the verification and closed by scale invariance
+ zero weight).

> **THEOREM (Scope A) [H].** Let `u` be a steady axisymmetric Euler flow on `R³` with
> `p = p(ψ)`. On every regular closed poloidal streamline with `A(ψ) > 0`:
>
> `s_level(ψ) = ⟨u_θ²⟩/⟨|u_pol|²⟩ ≥ δ(ψ)/157`, and `α/r_min² ≥ 1/42`.
>
> Consequently, for (L)-localized members with finite poloidal energy:
>
> **`s(u) ≥ (1/157) · δ_geo(u)`**, `δ_geo = ⟨r_min(ψ)/r_max(ψ)⟩_{E_pol}`.
>
> Hypotheses (P2, frozen): `p = p(ψ)`; regular closed poloidal streamlines; no `r² = α`
> pure-swirl stratum; no positive-measure stagnation set. Localization and compact
> support are NOT needed for the per-level statement. The constant `1/157` is a crude
> series-free surrogate; the sharp constant is an elliptic-integral evaluation at `σ*`
> (open, cosmetic).

**Mechanism.** The `δ² → δ` enhancement over the naive Jensen bound comes from the
elliptic time measure's `1/√(1+σy)`-singularity at the axis-side turning point: the orbit
*lingers* near `r_min`, where the pointwise swirl fraction is `Θ(1)` (≥ 1/42), for a time
fraction `≍ δ`. The earlier `σ ≥ α/r_max²`-route ceiling ("θ < 2 unreachable") was
correct about that route and is bypassed by integrating instead of minimizing.

## 5. Exponent convention

Single convention throughout: `δ_geo ∈ [0,1]`, target `s ≥ c·δ_geo^θ`, smaller θ =
stronger. **Proved: θ = 1** (the best possible: the conditional shell family realizes
`s ≍ δ_geo`, so θ < 1 is impossible). The previous chain "θ = 5 proved / θ ≤ 2 needed"
is superseded at both links (the per-streamline input and the aggregation were each lossy
by design, and the convexity crutch is gone).

**Erratum against the P0 probe (P4):** probe §5 mixed the reciprocal convention: its
"θ = 1/5 (all that is proved)" and "θ ≥ 1/2 empties the wedge" are `ρ_a`-convention
statements; in the mandated convention they read θ = 5 and θ ≤ 2 respectively, and both
are now superseded by θ = 1. Probe §4's classification-row rate
"`ρ_a ≳ ε_loc^{−2/3}` [H under convexity]" is vacuous (`ε_loc² ≥ 1/42` always) and is
replaced by the linear, hypothesis-free `ρ_a ≥ 1/(157·s)`. An erratum block is appended
to the probe document; nothing there is silently rewritten.

## 6. Sharpness / counterexample analysis

- θ = 1 is **sharp at the level scale** [H]: `s_level ≍ δ` two-sidedly as `δ → 0`
  (upper-bound side asserted with endpoint checks; full uniform upper bound recorded as
  a non-load-bearing debt).
- At the flow scale, sharpness is **[C]**: the shell family (P0 §2.3) realizes
  `s ≍ δ_geo` conditional on the unproved separatrix-continuation lemma; it sits exactly
  *on* the proved bound — a coherence signal, not an escape.
- Counterexample search with the full permitted freedom (multiband ω-cutoffs, disjoint
  coaxial unions with the mediant envelope recomputed exactly, nested cells) returned
  **negative**: nothing beats θ = 1. Corrections recorded: nested cells do *not* carry
  disjoint ψ-ranges (the complement of the support is connected); ω cannot separate the
  components of one level; "exactly conv(Γ)" weakened to "⊆"; none of these touch the
  theorem, whose proof no longer uses ω-freedom at all.
- Cheap falsifier left armed (P6): the `A ↔ σ` dictionary test
  `s_level = 1/2 − 0.5391(1−δ)² + O((1−δ)³)` vs the probe's `s = 1/2 − (21/16)δ_probe²`
  — one number decides; [C-num] both sides; nothing rests on it.

## 7. Frozen-scaling substitution — pure geometry first (Prop G)

With `R ~ τ^α`, `s ~ τ^{2(γ−α)}` and the theorem at exponent θ:
`δ_geo ≲ s^{1/θ}`, so the innermost energy-carrying radius obeys
`r_min ≲ τ^E`, `E(θ; γ, α) = α + 2(γ−α)/θ`.

**Proposition G (pure geometry, no viscous input) [H given the theorem].** On the open
interior blob wedge, any θ > 0 forces `ρ_a → ∞` and `r_min/R → 0` at strictly positive
power rates; at θ = 1: `E = 2γ − α > γ > 1/2` on the entire wedge (all vertices
re-checked), with sheet thickness exponent `2E − α = 4γ − 3α` if the shell structure is
additionally assumed. **Euler alone excludes nothing** — these are descriptions, not
contradictions.

Threshold bookkeeping (re-derived exactly; corrects one recorded claim): exclusion of the
whole wedge under the `E > 1/2` criterion holds iff **θ < 4** (not "θ ≤ 2" — true but
not sharp); θ = 4 leaves exactly the measure-zero `γ+α = 1` edge (already under K10/K11
contest, and there the leading-order-Euler premise itself fails — that corner must never
be read as survival or death); θ = 5 would leave the sliver `3α + 2γ < 5/2` (1/36 of the
wedge, best margin `τ^{−1/50}`); under the sheet structure the threshold moves to θ* = 8.
**All moot at the proved θ = 1.**

## 8. Conditional viscous interpretation (kept separate, [C])

**Proposition V [C].** *Premise (V1-level, explicitly unpromoted; its derivation is
recorded as truncated and without adversarial review):* at fixed ν no energy-carrying
structure persists below `√(ντ) ~ τ^{1/2}`. *Then* exclusion of a wedge point ⟺
`E > 1/2` strictly; at θ = 1 this holds on the **entire open interior blob wedge**
(`E = 2γ − α > 1/2` with no marginal corner). The swirl-poor localizable core is a
structure fixed-ν NS erases faster than the ansatz builds it.

This is the pre-registered decision rule firing — **conditionally**. Nobody may cite this
as "the blob branch is dead": the exclusion is Scope-A + V1-conditional, and the V1
premise remains [C].

**Ring corollary (new, decision-relevant, needs NO viscous input) [C — single-sourced,
verification required before any map use].** On the frozen ring branch (`R ~ τ^ρ`,
minor scale `~ τ^α`, `ρ < α`), every streamline is radially thin: `δ(ψ) → 1` uniformly,
so by the uniform pinning (now backed by the one-parameter graph rigidity, closing the
earlier "pinning is only a limit statement" objection) `s ≥ c > 0` — contradicting the
branch requirement `s_ring ~ τ^{2(γ−ρ)} → 0` (K3 forces `γ > ρ`). θ-independent; only
`c > 0` is used. This **contradicts the recorded reading that the ring corridor "has no
rigidity kill at all"** (that reading concerned the planar no-swirl rigidity, which is
indeed false; the swirl-fraction pinning is a different, Scope-A mechanism). Escapes:
exactly K3's own mesoscale/≥3-region corridor, and Scope B.

## 9. Physical interpretation

A localized quasi-steady Euler core buys small swirl with geometry at the now-proved
exchange rate θ = 1: to make the swirl energy fraction `s` small, the energy-carrying
core must send a radially thin, axis-grazing tongue to `r_min ~ R·s`, becoming a
near-critically oblate sheet (`∫u_r²/∫u_z² → 2`). Euler is scale-free and tolerates
this; fixed-ν viscosity (under the unpromoted V1 premise) does not — the forced inner
scale falls below `√(ντ)` everywhere in the frozen wedge.

**One sentence:** on the localizable class, a localized quasi-steady Euler core cannot be
made swirl-poor while remaining geometrically thick enough to be a plausible
fixed-viscosity Navier–Stokes core — swirl-poverty and viscous thickness are
incompatible at the proved linear exchange rate; this is a statement about the geometric
plausibility of a candidate NS core, not a claim that Euler existence implies NS
survival, and it says nothing yet about non-localizable flows.

## 10. Final verdict

- **Geometry verdict: `GEO-RESTRICT`.** The (★_geo) inequality exists, is sharp
  (θ = 1), is hypothesis-light (convexity retired, ω-machinery off the critical path),
  and bites on the whole wedge. Not GEO-KILL: GEO-KILL requires the accepted NS-side
  assumptions, and the V1 premise is explicitly unaccepted; the whole gate is Scope-A.
  Far past GEO-OPEN; the opposite of GEO-SURVIVOR (the only known realizing family sits
  *on* the bound, not under it).
- **BH verdict: `YELLOW-RED`.** The pass's machinery survived adversarial verification
  and strengthened (θ = 5 → 1, [C] → [H], convexity retired); (★_geo) came back
  affirmative at the best possible exponent, and by the pre-registered table the
  interior blob wedge empties under the [C] viscous premise; the Scope-A ring corollary
  adds viscosity-free pressure on the ring corridor. Not RED: every kill is gated on
  Scope A, the blob kill additionally on the unpromoted V1 premise; a single
  non-localizable localized steady flow would restore YELLOW immediately.
- **CAP trigger: `CAP: DO NOT START`.** Profile discovery would target exactly the
  axis-grazing sheet the gate says fixed-ν NS cannot sustain in-window, whose only Euler
  realization is [C] on an unproved continuation. Revisit triggers: Scope B opens
  (localizability shown non-necessary, or a non-localizable witness appears); or the
  ring corollary fails verification; or the P6 dictionary test falsifies the
  one-parameter reduction. No CAP note is created (per the brief, it exists only for an
  NS-resolvable survivor).

## Next bounded task

**Adversarially verify and scope-freeze the ring corollary** (§8): uniformity of
`δ(ψ) → 1` on a thin-ring core; uniform pinning via the graph rigidity rather than a
per-family limit; the exact hypothesis list it consumes (Scope A, leading-order Euler,
K3's `γ > ρ`, single-valued `A`). Algebraic; needs no continuation lemma, no literature,
no viscous premise — and it is the only object on the table that could move a map-level
scope statement without invoking [C] NS assumptions. Runner-up (bundled literature
errand, not a pass): Jiu–Xin's primary hypothesis class + whether necessity of
`u·∇p = 0` is known.

## Debts and failures (recorded, unrepaired)

Sharp constant at `σ*` uncomputed (cosmetic); `s_level ≤ Cδ` upper bound not fully
proved (non-load-bearing); flow-scale sharpness [C] on the continuation lemma; the V1
premise remains [C] with a truncated derivation; ring corollary single-sourced; P6
dictionary test unevaluated; Scope B untouched by construction. Superseded and
withdrawn during the pass: the θ = 5 chain (both links), "no route to θ < 2" (route-
specific), "c = 1/2 sharp", "exactly conv(Γ)", "disjoint nested ψ-ranges", "median
maximally broken". No files modified by agents; no numerics beyond [C-num]-tagged series
arithmetic; frozen map untouched.
