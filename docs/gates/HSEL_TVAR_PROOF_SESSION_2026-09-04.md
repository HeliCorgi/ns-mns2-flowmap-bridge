# HSEL_TVAR_PROOF_SESSION — 2026-09-04 — T-VAR proof session: the commissioned frame decomposition derived; the gap-weighted rotation identified as R's eigenframe off-diagonal; the entrywise sweep shown to overcharge and refined spectrally; VERDICT: ONE-SUBLEMMA — T-CONE, the negative-cone-sweep lemma λ_min(∫R₋dt) ≤ Q₀ (RECORD-ONLY on the open content; proved yields marked)

**Repo:** `c:/Users/corgi/Downloads/ns-mns2-flowmap-bridge` · **Status:** proof-session record. No Lean; no numerics. Proved items flagged [D] (each re-checked for signs, symmetry, and logical direction); **no open statement is claimed** — verdict ONE-SUBLEMMA. Lean baseline unchanged (8775-job gate).

**Commissioning provenance.** User instruction, 2026-09-04 (twentieth session): sole target T-VAR. Derive `QᵀG′Q = Λ′ + [Ω,Λ]` (`G = QΛQᵀ`, `Ω = QᵀQ′`); decompose T-VAR's total rise into eigenvalue-amplitude variation + frame-rotation contribution, with the correct rotation observable being the **gap-weighted** `|λᵢ−λⱼ||Ω_ij|`, not raw `|Ω|`; test via `G′ = −2R = −2(νD+𝒫)` whether this (or something weaker) admits a `(ν,T,M)`-uniform budget; check: (1) near-isotropic ⟹ rotation harmless; (2) strong anisotropy ⟹ possible direction stability; (3) the wide-cone vs thin-fast-cone dichotomy; (4) what `D ⪰ 0` does to the cone's rotation. Any route needing full-enstrophy/BKM/Serrin budgets is rejected on sight. Verdict ∈ {PROVED / ONE-SUBLEMMA / ROUTE-SWAP / DEAD-END}; if ONE-SUBLEMMA, print the weakest weighted-rotation / negative-cone-sweep statement that actually dominates T-VAR (not a raw frame-frequency bound).

---

## §1 — The frame identity and the correct observable [D]

Along a.e.-differentiable eigenpaths (`G` smooth in `t`; Rellich-type care at crossings — ultimately not needed, see §3): differentiating `G = QΛQᵀ` and multiplying by `Qᵀ·,·Q` gives, with `Ω := QᵀQ′` antisymmetric,

> `QᵀG′Q = Λ′ + [Ω,Λ]`, i.e. componentwise `λᵢ′ = (QᵀG′Q)_{ii}` and `(λⱼ−λᵢ)Ω_{ij} = (QᵀG′Q)_{ij}` (i ≠ j).

Substituting the exact NS identity `G′ = −2R` and writing `R̃ := QᵀRQ`:

> **`λᵢ′ = −2R̃_{ii}` and `|λᵢ−λⱼ|\,|Ω_{ij}| = 2|R̃_{ij}|`** — the commissioned gap-weighted rotation IS (twice) the off-diagonal of the rise tensor in the Gram eigenframe. No perturbation-theoretic division by the gap ever occurs: the observable is an entry of `R`, finite through degeneracies — a structural proof that the gap-weighting is the correct normalization.

## §2 — Rise decomposition, the overcharge, and the spectral refinement [D]

For fixed `e` with moving-frame coordinates `c(t) = Qᵀe` (`c′ = −Ωc`): `X_e′ = −2cᵀR̃c = Σᵢ λᵢ′cᵢ² + Σ_{i≠j}(λⱼ−λᵢ)Ω_{ij}c_ic_j` — the amplitude part and the rotation part, recombining exactly (consistency check passed). The naive entrywise dominator ("T-SWEEP": budget `Σᵢ(−R̃_{ii})₊ + 2Σ_{i<j}|R̃_{ij}|`) does imply T-VAR for every `e` [D], **but overcharges**: in a purely dissipative epoch `R = νD ⪰ 0` every channel is monotone (`(X_e′)₊ ≡ 0`) while the off-diagonal charge is positive and wall-level — rejected as a route on sight per the rule. The correct refinement is spectral: with `R = R₊ − R₋` (`R₋ ⪰ 0` the negative spectral part, globally defined, continuous in `t`, frame-free),

> `(X_e′)₊ = 2(−eᵀRe)₊ ≤ 2\,eᵀR₋(t)e` pointwise, for every fixed `e`.

## §3 — THE SUBLEMMA (the weakest frame-free dominator)

Integrating §2 and optimizing `e` — which is now a **linear-spectral** problem, so the ∃-quantifier collapses onto one accumulated PSD matrix:

> **T-CONE (the negative-cone-sweep lemma; norm-uniform; OPEN — never asserted):** ∀ν>0, ∀T<∞, ∀M<∞: ∃Q₀(ν,T,M) < ∞ such that every certified solution from the `M`-ball satisfies, on every certified horizon `T′ ≤ T`:
> **`λ_min\big(𝔑(T′)\big) ≤ Q₀`, where `𝔑(T′) := ∫₀^{T′} R₋(t)\,dt` and `R = νD + 𝒫 = −½G′`.**
>
> *"The time-accumulated negative spectral part of the rise tensor does not become uniformly positive-definite at wall level — some fixed direction escapes the accumulated negative cone."*

**Proved arrow [D]:** T-CONE ⟹ T-VAR with constant 2 (take `e` = a `λ_min`-eigenvector of `𝔑(T′)`; then `∫(X_e′)₊dt ≤ 2∫eᵀR₋e\,dt = 2λ_min(𝔑) ≤ 2Q₀`; per-horizon `e` handled by DQ-1 verbatim) ⟹ T-DIR ⟹ the verified chain (`sup_t‖u‖_{H³} ≤ F(ν,T,M,·)` ⟹ H-SEL^nu ⟹ N0 ⟹ Lean). **Weakest-dominator justification:** among statements of the form "∃e: the accumulated negative part along `e` is budgeted", T-CONE is exactly the optimal-`e` version (`λ_min` of the integral); the only slack left below it is the `R₊`-shielding inside `(−eᵀRe)₊ ≤ eᵀR₋e` (crediting times when `e` lies in the negative cone but positive production still shields the form) — exploiting that requires joint spectral information and returns to T-VAR itself, which remains the weakest chain-closing statement. **Structural virtues:** frame-free (no eigenvector-regularity technicalities — `R₋` is globally defined and measurable; the §1 frame analysis is motivational, not load-bearing); ∃-collapsed (the direction is computable from one matrix); strictly weaker than every trace-level statement (`λ_min(𝔑) ≤ ⅓tr𝔑` — T-CONE is implied by, but does not require, the wall-level budget `∫trR₋dt`).

## §4 — The four commissioned checks [D]

1. **Near-isotropic regime: rotation harmless — CONFIRMED structurally.** `|R̃_{ij}| = ½|λᵢ−λⱼ||Ω_{ij}|`: degenerate gaps null the rotation cost regardless of `|Ω|`; in T-CONE's language, a near-isotropic `G` rotating fast contributes to `R₋` only through actual spectral negativity, not through frame motion.
2. **Strong anisotropy: direction stability — CONDITIONAL STRUCTURE CONFIRMED.** With a large gap, a budget on `|R̃_{ij}|` forces `|Ω_{ij}| = 2|R̃_{ij}|/|λᵢ−λⱼ|` small — bounded off-diagonals + big gaps ⟹ slow frames. (This is the mechanism a T-CONE proof would exploit in the anisotropic branch.)
3. **Dichotomy priced.** Wide negative cone (isotropic negative `R`): `𝔑` grows isotropically at rate `~trR₋/3` — the branch is the production-anisotropy (SP-a-type) question. Thin fast-rotating cone: per-time negativity concentrated in one sweeping direction — `𝔑` isotropizes iff the sweep equidistributes. **T-CONE ⟺ the accumulated negative production cannot be simultaneously wall-large and directionally equidistributed** — the precise sweep formulation; the required NS input is an anti-equidistribution mechanism, which none of the free identities supplies (checked: `tr𝔑 = ∫trR₋` is wall-level; `∫trR\,dt = ½(E(0)−E(T′))` is signed-only; both rejected as closing routes per the rule).
4. **`D ⪰ 0` and the cone's rotation.** Weyl: `ρᵢ(R) ≥ μᵢ(𝒫)` — dissipation narrows and (in dissipative epochs `νλ_min(D) ≥ (−λ_min𝒫)₊`) closes the cone entirely; it does **not** constrain the cone's angular velocity while open. Recorded: `D` is a cone-width resource, not a cone-rotation resource.

**Barrier consistency check [D]:** the kinematic rotating-anisotropy path has `Λ′ = 0`, so `R̃` is purely off-diagonal with eigenvalues `±½|gap||Ω|` — `trR₋ ~ (g−ε)f` and the sweep equidistributes ⟹ `λ_min(𝔑) ~ fTg/3 → ∞`: the kinematic violator defeats T-CONE too, exactly as it must (T-CONE ⟹ T-VAR, and T-VAR is kinematically false). The barrier survives, now priced as **gap × frequency × equidistribution**.

## §5 — VERDICT

**ONE-SUBLEMMA: T-CONE** (printed in §3 with its proved arrow and weakest-dominator justification, as the commission prescribes — a negative-cone-sweep statement, not a raw frame-frequency bound). Not PROVED: the free identities cannot budget `λ_min(𝔑)` (the anti-equidistribution input is missing — §4.3); not ROUTE-SWAP (no open head assumed); not DEAD-END (the sublemma is strictly weaker than all trace-level/entrywise dominators, ∃-collapsed, frame-free, and inherits the full verified chain). Chain now: **T-CONE ⟹ T-VAR ⟹ T-DIR ⟹ [DQ-1 + Zhang/CFZ, V-15, M-only] H-SEL^nu ⟹ N0 ⟹ Lean.** Battery: kinematic rotators violate T-CONE (barrier, not counterexample); frozen profiles violate (forced); the small-data/O-1 subclass satisfies it (uniform bounds ⟹ `tr𝔑` bounded); the wall implies it but it does not imply the wall (strict weakening — non-collapsed target).

## §6 — Claim boundary

No open statement is proved: T-CONE, T-VAR, T-DIR, H-SEL, N0 all remain OPEN; the session's [D]-items are linear algebra along the commissioned identity set (the frame identity, the rise decomposition and its recombination check, the overcharge counter-observation, the spectral-part domination, the T-CONE ⟹ T-VAR arrow, the barrier repricing). **Nothing here asserts, approaches, or implies a resolution of the Navier–Stokes Millennium problem in either direction.** Wall-requiring routes were rejected on sight per the commissioned rule; the logical-collapse caveat applies to T-CONE as to every head; C0 — a selection, not uniqueness. Commissioning proof work on T-CONE, a T-CONE-targeted probe (`spec 𝔑(T′)` is a computable observable on the existing probe infrastructure), or anything else downstream is a user act.
