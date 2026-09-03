# HSEL_TDIRSPK_PROOF_SESSION — 2026-09-04 — first proof session on T-DIR-SPK(∃e): the five commissioned mechanisms adjudicated; the head is found to OVER-DEMAND a directional dissipation budget and is re-based; VERDICT: ONE-SUBLEMMA — T-VAR, the total-rise budget (RECORD-ONLY on the open content; proved yields marked)

**Repo:** `c:/Users/corgi/Downloads/ns-mns2-flowmap-bridge` · **Status:** proof-session record. No Lean file touched; no numerics. The proved items below ([D], each re-checked for signs and logical direction) are elementary consequences of the commissioned identity set; **no open statement is claimed** — the verdict is ONE-SUBLEMMA, not PROVED. Lean baseline unchanged (8775-job gate).

**Commissioning provenance.** User instruction, 2026-09-04 (nineteenth session): commission proof work on the sole target `∃e ∈ S²: K_{T′}(e) := ∫₀^{T′}(−eᵀ𝒫(t)e)₊dt ≤ Q₀(ν,T,M)` (no canonical direction assumed), using the exact identities `G′ = −2νD − 2𝒫` (D ⪰ 0), `trG = ‖∇u‖₂²`, `tr𝒫 = −∫ωᵀSω`, incompressibility/pressure cancellation/energy equality. Counterexample-first checks: (1) what sphere minimization of `e ↦ K_T(e)` gets from exact-NS constraints; (2) persistence/rotation of `𝒫(t)`'s negative eigenspace; (3) whether `G′` and `D ⪰ 0` limit the total variation of the production's negative part; (4) whether coherence/strain geometry can generate ∃e directly; (5) transfer from Miller's existential-direction `v×ω` structure. Rules: sphere-averaging-to-wall = immediate rejection; assuming another open head = ROUTE-SWAP; kinematic rotating-anisotropy = known barrier, not a counterexample. Verdict ∈ {PROVED / ONE-SUBLEMMA / ROUTE-SWAP / DEAD-END} with prescribed consequences.

Notation as in the T-GRAM records; additionally `R(t) := νD(t) + 𝒫(t)` (the "rise tensor": `X_e′ = −2eᵀRe`), `TV₊(X_e) := ∫₀^{T′}(X_e′)₊dt` (total positive variation).

---

## §1 — Proved yields of the session [D]

- **P-a (exact reformulation of the head).** From `−eᵀ𝒫e = ½X_e′ + ν eᵀDe` (the channel identity rearranged), pointwise `(½X′)₊ ≤ (−eᵀ𝒫e)₊ ≤ (½X′)₊ + νeᵀDe`, hence
  > `½·TV₊(X_e) ≤ K_{T′}(e) ≤ ½·TV₊(X_e) + ν∫₀^{T′}eᵀDe\,dt`, and also `K_{T′}(e) ≥ ν∫eᵀDe\,dt − M²/2`.
  **Consequence — the head over-demands:** T-DIR-SPK(∃e) forces `ν∫‖∇∂_e u‖²dt ≤ Q₀ + M²/2` — a *directional `H²`-dissipation budget* that the downstream chain never needs (T-DIR requires only `∫X_e²dt`). Per the EH-1 re-basing precedent, the commissioned head carries a strictly-stronger-than-needed component and is **re-based**.
- **P-b (the weakened sublemma and both arrows).** Define
  > **T-VAR (∃e total-rise budget; OPEN):** ∀ν,T,M ∃Q₀(ν,T,M): every certified solution from the `M`-ball admits, per certified horizon `T′ ≤ T`, a unit `e ∈ S²` with `TV₊(X_e) = ∫₀^{T′}\big(\tfrac{d}{dt}‖∂_e u(t)‖²_{L²}\big)_+dt ≤ Q₀`.
  Then **(i)** `T-DIR-SPK ⟹ T-VAR` (pointwise `(X′)₊ = 2(−eᵀRe)₊ ≤ 2(−eᵀ𝒫e)₊` since `νeᵀDe ≥ 0`); **(ii)** `T-VAR ⟹ T-DIR` (proved): `sup_t X_e ≤ X_e(0) + TV₊ ≤ M² + Q₀`, hence `∫₀^{T′}X_e²dt ≤ T(M²+Q₀)²` — T-DIR with `Q₀′ = T(M²+Q₀)²`, and thence the V-15-verified quantitative M-only bridge to `H-SEL^nu`, `N0`, and the Lean assembly. DQ-1 handles the per-horizon `e` as before. **T-VAR is the weakest member of this family that still closes the chain** (it is exactly the sup-bound input; the dissipation demand is dropped).
- **P-c (equivalent rise-tensor form and a new free identity).** `T-VAR ⟺ ∃e: ∫(−eᵀR(t)e)₊dt ≤ Q₀/2` with `R = νD + 𝒫 = −½G′`. Free integral identity: `∫₀^{T′}tr R\,dt = ½(E(0) − E(T′)) ≤ M²/2` — the signed ONB-sum of the rise-form is globally budgeted by the enstrophy CHANGE; only the per-direction positive parts (oscillation) are unbudgeted.
- **P-d (the free structure is provably insufficient — barrier localized).** The candidate matrix-path lemma "`G ⪰ 0`, `∫trG dt ≤ B`, `G(0) ⪯ M²I` ⟹ ∃e: `TV₊(eᵀGe) ≤ f(B,M,T)`" is **FALSE**: the rotating-anisotropy path `G(t) = R_f(t)\,\mathrm{diag}(g,ε,ε)\,R_f(t)ᵀ` (realizable by the F2 kinematic velocity family) has all free budgets fixed while `TV₊ ~ fTg → ∞` for every fixed `e` as the rotation frequency `f → ∞`. **The unbounded resource is the Gram frame's oscillation frequency**; any proof of T-VAR must extract an NS-dynamical bound on it (R4 of the decomposition record showed the naive route costs wall budgets) — the F2 barrier now localized to exactly this quantity.

## §2 — The five commissioned checks

| # | Check | Finding |
|---|---|---|
| 1 | sphere minimization of `K_T` under exact-NS constraints | the constraint set reaches the minimization only through trace/averaging functionals — sphere averaging gives `avg_e K ≳` wall quantities (rejected on sight per the rule); the relaxed density-matrix version `min_ρ ∫(⟨−𝒫,ρ⟩)₊` at fixed `ρ` is the same problem (`ρ = I/3` = wall; time-varying `ρ` = the insufficient per-time statement). Minimization content = frame coherence, unchanged |
| 2 | persistence/rotation of `𝒫`'s negative eigenspace | no exact-NS obstruction to `𝒫(t) ≺ 0` (all-directions-bad) was found — isotropic positive-stretching states realize it kinematically; persistence under NS is open; after P-b the relevant object is `R`'s negative cone (smaller — dissipation helps), and its **rotation** is the residual resource (P-d) |
| 3 | do `G′`, `D ⪰ 0` limit the negative-production total variation? | they give exactly the one-sided structure of P-a (all channel rise comes from production; `K ≍ ½TV₊ + `dissipation) and the free identity P-c — but **no free TV bound exists** (P-d counterexample). Answer: reformulation yes, control no |
| 4 | coherence/strain geometry generating ∃e | YES conditionally: `∂_e u = Se + Ae` with `Ae = ½ω×e`; for `e ∥` a globally coherent vorticity direction the transverse part is small and `P_e ≈ ∫eᵀS³e`, which is `≳ 0` under the DNS-generic `ω`–`λ₂` alignment with `λ₂ ≥ 0` — i.e. **coherence + alignment would generate the good direction**. But both inputs are open heads (HR-1-type + a `λ₂`-sign statement) ⟹ **ROUTE-SWAP** per the rule; recorded as the route's map, not taken |
| 5 | Miller `v×ω` transfer | the antisymmetric half of the channel vector IS Miller's object at constant direction (`ω×e = 2Ae`); his variable-`v(x,t)` freedom has no bridge on our side (the CFZ criterion needs constant `e`); kinship recorded, no usable transfer |

## §3 — VERDICT and consequences

**VERDICT: ONE-SUBLEMMA — T-VAR** (P-b), with the commissioned head **T-DIR-SPK re-based** (P-a: it over-demands the directional dissipation budget; archived as the stronger family member, everything it implies flows through T-VAR). Per the commission's prescription, **T-VAR is the single next target**:

> `∃e ∈ S²: ∫₀^{T′}\big(\tfrac{d}{dt}‖∂_e u(t)‖²_{L²}\big)_+dt ≤ Q₀(ν,T,M)` — "some directional-derivative channel has budgeted total energy rise"

equivalently the rise-tensor form `∃e: ∫(−eᵀR e)₊dt ≤ Q₀/2`, `R = −½G′`. Chain (all downstream proved/verified): `T-VAR ⟹ [P-b(ii)] T-DIR ⟹ [DQ-1 + Zhang/CFZ, V-15] sup_t‖u‖_{H³} ≤ F(ν,T,M,·) ⟹ H-SEL^nu ⟹ N0 ⟹ Lean N1→N2→N3.` **The open content is now: NS dynamics must bound, for one fixed direction, the oscillation (total rise) of the channel energy — with the free identities provably insufficient (P-d) and the unbounded kinematic resource identified as the Gram frame's rotation frequency.**

Battery for T-VAR [D]: kinematic rotating families violate it for every `e` — the standing barrier, not a counterexample; frozen `S_blob`/Type-I violate (polarity forced through the proved arrows); small-data/O-1 subclass satisfies it (uniform bounds ⟹ `TV₊ ≤ ∫\|X′\| ≤ 2ν∫eᵀDe + 2∫\|eᵀ𝒫e\|`, all bounded there); the averaging no-go carries over verbatim (`Σᵢ TV₊(X_{eᵢ}) ≥ ∫(−trR)... ` per-direction positive parts unbudgeted).

## §4 — Claim boundary

No open statement is proved: T-VAR, T-DIR, H-SEL, N0 all remain OPEN; the session's proved items (P-a–P-d) are elementary consequences of the commissioned identity set plus one explicit counterexample path, each flagged [D]. **Nothing here asserts, approaches, or implies a resolution of the Navier–Stokes Millennium problem in either direction.** The logical-collapse caveat applies to T-VAR as to every head. The re-basing of T-DIR-SPK follows the EH-1 precedent (weakest chain-closing member); C0 — a selection, not uniqueness; the ROUTE-SWAP map of check 4 (coherence + λ₂-alignment ⟹ good direction) is recorded for a future comparison against HR-1/HR-3′ but not taken. Commissioning proof work on T-VAR, or anything else downstream, is a user act.
