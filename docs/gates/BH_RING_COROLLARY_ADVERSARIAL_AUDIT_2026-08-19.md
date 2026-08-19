# Ring pinning corollary — adversarial audit and scope freeze

Date: 2026-08-19 (JST). Task: ring-corollary verification brief (one bounded pass; stop
rules observed: no numerics beyond [C-num]-tagged load-nothing checks, no new ansatz, no
V1/K12 promotion, no Lean, no separatrix lemma, no Scope-B theorem; the map edit below is
executed only under the explicit authorization of this audit, with all four mandated
riders). Baseline: `BH_GEO_SWIRL_AGGREGATION_2026-08-19.md` (the Scope-A swirl–geometry
theorem). Process: four analysts + two adversarial verifications + completeness critic;
every load-bearing arrow independently re-derived at least twice. Tags: [H] hard, [V]
verified today, [V?] search-level, [C] conditional, [B] bookkeeping.

## 1. Exact one-scale ring geometry assumptions

`R ~ τ^ρ` (ring radius), minor scale `ℓ ~ τ^α`, `ρ < α` (so `ℓ/R = τ^{α−ρ} → 0`);
amplitude `‖u_pol‖_∞ ≍ τ^{−γ}`; swirl `σ = ρ` (circulation pinning `Γ = r·u_θ = O(1)` at
`r ≍ R`).

**Containment is definitional, not an added hypothesis** [B]/[V?] (reconstruction —
sound and near-forced, but the tube volume `Rℓ²` is nowhere printed in the frozen table;
this documentation debt is paid by rider R1): the frozen ring rows K5
(`ρ+2α ≥ 2γ`) and K6 (`ρ+2α < 3γ`) are literally the substitutions
`∫|u|² ≍ τ^{−2γ}Rℓ²` and `∫|u|³ ≍ τ^{−3γ}Rℓ²` — the lower (fill) and upper
(containment) bounds respectively. Without containment+fill, `Rℓ²` measures nothing and
`S_ring` as printed is undefined. K3's ring cut and `σ = ρ` likewise evaluate at
`r ≍ R`. **An inward tongue is therefore an exit from the one-scale class** (into the
mesoscale/≥3-region corridor), not a counterexample — exactly as the brief mandates.

## 2. δ_geo → 1 — proof, and its correct scope

Given containment, every poloidal streamline in the tube has
`δ(ψ) ≥ (R−Cℓ)/(R+Cℓ) ≥ 1 − 2C·τ^{α−ρ}` — uniform in ψ, in `z₀`, in component count
[H]; the barycentre step is monotone integration (no Jensen, no Markov). Exceptional-set
tolerance: a fraction η of `E_pol` outside the tube degrades the bound to
`s ≥ (1−η)(1−2Cτ^{α−ρ})/157`; the kill survives iff `limsup η < 1`.

**Statement-level defect found and corrected (P1/E12/C9, confirmed twice):** on `S_ring`
the *core* energy share is `τ^{ρ+2α−2γ} → 0` wherever `2γ < ρ+2α` is strict, so the
**global** `δ_geo(u)` of the full flow is far-field-dominated and does *not* tend to 1.
The geometry-gate report's §8 sentence "`s ≥ c > 0`" for the global flow is **withdrawn**
(erratum appended there); the certified kill is the **amplitude/circulation form** of §7
below, which never forms an energy ratio and is immune to this defect.

## 3. Ring swirl-fraction dictionary

Certified [H]/[B]: `σ = ρ` from `Γ = O(1)` at `r ≍ R` (K9's razor reproduces it:
`σ ≥ ρ` from the CFZ-endpoint violation, `σ ≤ ρ` from the Γ maximum principle);
`s = ∫u_θ²/∫u_pol² ~ τ^{2(γ−ρ)} → 0` with both energies in the same tube (containment).
Toroidal/poloidal co-location holds in the one-scale class by definition; a flow whose
poloidal energy lives elsewhere is a multi-region flow (case 2/3) and outside the
corollary's scope by construction.

## 4. Derivation of γ > ρ — provenance corrected (rider R4)

Re-derived [V]: K3's exponent arithmetic (`E(ε) = (ρ−γ) + ε(1/2−ρ)`) alone gives
`γ ≥ ρ`, strict only for `ρ ≤ 1/2`; the boundary `γ = ρ` is closed by K6 ∧ `ρ ≤ α`.
The kill table's printed label "`ρ < γ (K3)`" is mis-sourced; corrected annotation:
**`ρ ≤ γ` [K3] + `ρ ≠ γ` [K6 ∧ `ρ ≤ α`]**. The survival set is unchanged. Moreover the
certified chain does not even need K3: `ρ ≥ γ` ⟹ `ρ+2α ≥ 3γ` exits `S_ring` by K6
directly — the kill is **doubly sourced** (K6 and K3).

Case separation (mandated): (1) one-scale ring — killed below; (2) ring + mesoscale
K3-violation region — outside the class, survives with the burden transferred (the
mesoscale must carry asymptotically all `E_pol` *and* be axis-grazing, i.e. exactly
Prop G/V's object); (3) ≥3-region corridor — untouched.

## 5. Scope-A hypothesis audit — the decisive scope facts

1. **`p = p(ψ)` is ADDED, and NOT removable [H, witness-backed].** Steady axisymmetric
   Euler always gives exactly two streamline invariants — `Γ = F(ψ)` and Bernoulli
   `B = B(ψ)` — whose entire joint content is the Bragg–Hawthorne equation
   `Δ*ψ = r²B′(ψ) − FF′(ψ)` (a Scope-B object). Scope A is the *additional* eikonal
   overdetermination `|∇ψ|² + F² = 2A(ψ)r²`. **Witness: Hill's spherical vortex** —
   an exact steady axisymmetric Euler flow with regular closed poloidal streamlines,
   `δ(ψ) ∈ (0,1)` bounded away from the endpoints, and `s_level ≡ 0`: the geometry-gate
   per-level conclusion is **false outside Scope A**. Hill is not a localized Scope-B
   ring, so the Scope-B existence question stays open — but Scope B is thereby settled
   **as a scope statement**: it is a **GAP inside the frozen ring class** (which asserts
   only leading-order steady Euler), not an exit from it. This ruling forces the word
   "localizable" into the map wording.
2. Closed nested tori are automatic at regular values (planar Hamiltonian); the real
   hypothesis is containment (A3 below).
3. Elliptic-centre `|u| = 0` (gate corollary) is consistent with the amplitude
   normalization (attained on `A > 0` levels).
4. The pure-swirl stratum `r² = α_g` is the swirl-**rich** endpoint (`s_level → 1`);
   a swirl-poor branch cannot hide there.
5. **Defects recorded in the upstream documents** (errata appended, not silently
   repaired): (P2) the gate's first-integral constant is `k = −P′/2 = (A′−B′)/2`, not
   `A′/2` (harmless per level; **the armed P6 falsifier is built on `k` and must be
   re-derived before evaluation — it could fire spuriously**); (P3) the taste report §3
   writes the *MHD* Grad–Shafranov form — its `P(ψ)` is `−B` (Bernoulli head), not
   pressure; read as pressure it would covertly make the frozen branch Scope A and the
   kill unconditional — it does not; Gates C/D are unaffected; (P12) the gate's `α`
   (per-streamline swirl constant) collides with the map's `α` (core-scale exponent) —
   written `α_g` here.

## 6. Escape tests R1–R5

| test | ruling |
|---|---|
| R1 energy-weighted bad streamlines | **VOID** in-class (uniform pointwise δ-bound; no weighting adversary); reduces to R2 |
| R2 inward tongue | **CLASS-EXIT** (violates containment ⟹ mesoscale/multi-region). Containment-free constraint [H]: `Γ` constant on streamlines + `α_g/r_min² ≥ 1/42` force `r_min ≲ Γ₀/‖u‖_∞ ~ τ^γ` — a tongue may reach from `τ^ρ` to `τ^γ`, no further |
| R3 multi-region energy split | **CLASS-EXIT** (a flow with poloidal energy elsewhere is not a one-scale ring; the corollary claims nothing about it) |
| R4 foliation degeneration | **VOID**: multiple O-centres in a ring tube are excluded outright by the gate's "no interior separatrix with `r_min > 0` on `A>0` levels" (every ring level has `r_min ≥ R−Cℓ > 0`); `A = 0` levels carry zero energy; the pure-swirl stratum is the wrong pole |
| R5 Scope B | **GAP** (not class-exit): decided by the Hill witness + the twice-derived `B = B(ψ) ⇏ p = p(ψ)`. The sharp open question: *must a localized steady axisymmetric Euler core with swirl satisfy the eikonal overdetermination, or does a BH solution exist with `p` non-constant on a poloidal streamline?* |

Additional [C] residue added to the escape list (P7): approximate-Euler/stability — the
thin-ring pinning is a curvature effect (invisible to the leading-order 2-D core
description), tolerant of `o(1)` relative Scope-A violation but not the `O(1)` violation
that "leading-order steady Euler" alone permits.

Refuted during the pass (recorded): the analysts' proposed strengthening "`σ ≥ γ`
containment-free ⟹ the blob dies too, viscosity-free" — **REFUTED**: for a blob, Scope A
relocates the swirl sup to the axis-grazing tongue tip `r_min ≲ τ^γ ≪ ℓ`, where
`Γ = O(1)` is exactly saturated; K9's `σ ≤ α` half is a swirl-sup-*location* premise
(`r ≍ ℓ`), not a theorem, and does not apply there. **The blob is unchanged and remains
V1-conditional.** New debt logged against K9's blob row (P6) for the multi-region audit.

## 7. The certified corollary (amplitude/circulation form)

> **RING PINNING COROLLARY (Scope A, one-scale) [H on (A2)–(A5), C on (A1)].**
> Let the core solve steady axisymmetric Euler with `p = p(ψ)` and `‖Γ‖_∞ ≤ Γ₀`, and
> let `L` be a regular closed poloidal streamline with `A > 0` carrying
> `|u| ≥ (1−o(1))‖u‖_∞` (a.e.-regularity supplies one, since `|u|² = 2A(ψ)`). Then
> `r_min(L) ≤ √42·Γ₀/‖u‖_∞`, sharpening to `√3·Γ₀/‖u‖_∞·(1+o(1))` when `L` is radially
> thin (endpoint pinning `u_θ² = |u|²/3 + O(ℓ/R)`, derived three independent ways).
> If `L` lies in the tube `{|(r,z)−(R,z₀)| ≤ Cℓ}` with τ-independent `C` and
> `ℓ/R → 0`, then `R ≲ Γ₀/‖u‖_∞`, i.e. `ρ ≥ γ` — contradicting K3's `ρ < γ`, and
> forcing `ρ+2α ≥ 3γ`, which exits `S_ring` by K6. **The one-scale localizable ring
> branch is inconsistent.**

Hypotheses: (A1) leading-order steady axisymmetric Euler with `o(1)` relative `C¹` error
[C — fails on the `γ+α=1` edge]; (A2) `p = p(ψ)` — added, not removable; (A3) top-speed
level regular, closed, `A > 0`, contained at radius `≍ R` [B, definitional]; (A4)
`‖Γ‖_∞ = O(1)` [H for an NS candidate via the maximum principle; B for an abstract
profile]; (A5) K6 ∧ `ρ ≤ α`, or K3. **Not consumed:** `δ_geo`, energy weighting, the
aggregation theorem, `1/157`, `1/42` (thin case — the endpoint pinning retires them for
the ring), θ, convexity, V1/K12, compactness, the separatrix lemma. Non-vacuity [V]:
`(γ,ρ,α) = (0.6, 0.42, 0.45)` satisfies every printed row of `S_ring` with `ρ < α` — the
killed set is nonempty and open. Consistency [V]: the thin Scope-A level has
`u_θ² = |u|²/3` ⟹ `σ = γ`, which is verbatim K6's [D2] swirl-dominated row — the kill is
internal to the frozen table (the gate adds exactly one new fact; K6 then fires).

## 8. Scope freeze

- **Class A — blob (`ρ = α`): UNCHANGED.** The corollary degenerates continuously to
  vacuity at `ρ = α`; the axis-grazing tongue is available; still V1-conditional.
- **Class B — one-scale localizable ring (`ρ < α`): DEAD.** Scope-A, viscosity-free,
  compactness-free, non-vacuous, doubly sourced (K6 and K3).
- **Class C — open:** Scope-B ring (GAP inside Class B — the decisive residue);
  mesoscale/≥3-region corridor (burden transferred: the mesoscale must carry
  asymptotically all `E_pol` and be axis-grazing); the `γ+α = 1` unsteady edge ((A1)
  fails; neither death nor survival); the `ρ = α` face (= Class A).

A Class-B kill is **not** propagated into Class C.

## 9. Final verdict

- **Ring verdict: `RING-ONE-SCALE-KILL`.** Not RING-KILL: the corollary as originally
  printed had a statement-level defect (global-`s` sentence, withdrawn) and its kill
  covers only the localizable part of the one-scale class — Scope B is a GAP inside the
  frozen class.
- **BH verdict: `YELLOW-RED`** (unchanged). A viscosity-free Scope-A kill of a nonempty
  open sub-branch strengthens the pass; every kill remains Scope-A-gated, and a single
  non-localizable localized steady witness would restore YELLOW.
- **Next branch: `NEXT: MULTI-REGION AUDIT`.** The burden transfer is now quantified,
  and the new K9 swirl-sup-location debt (P6) lives exactly there. Runner-up, recorded
  not scheduled: Scope-B reconnaissance (already the gate's revisit trigger).

Map edit authorized and executed with this audit (riders R1–R4): the kill table's ring
row carries the annotation **"one-scale localizable ring branch excluded by
swirl-geometry pinning"** with the one-scale definition and the provenance relabel;
nothing broader (no blob, no mesoscale, no Scope-B, no dimension-collapse claim).
