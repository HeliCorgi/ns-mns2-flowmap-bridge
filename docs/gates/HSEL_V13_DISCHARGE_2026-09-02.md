# HSEL_V13_DISCHARGE — 2026-09-02 — V-13 discharged at primary level: Li–Pan Thm 1.3 / Cond. 1.1 verified for pure NS at the (s,q,p) = (1,4,2) equality endpoint with a fully quantitative proof; VERDICT: QUANTITATIVE-BRIDGE, with one tracked extra datum input `‖ru₀^θ‖_∞` (RECORD-ONLY)

**Repo:** `c:/Users/corgi/Downloads/ns-mns2-flowmap-bridge` · **Status: RECORD-ONLY.** No Lean file touched; no numerics; no proof search on T-SRC′/H-SEL/N0; nothing frozen moved. Lean baseline unchanged (8775-job gate).

**Commissioning provenance.** User instruction, 2026-09-02 (twelfth session): discharge V-13 — re-verify Li–Pan, DCDS 42 (2022) 2333–2353, arXiv:2011.03146, Thm 1.3 / Cond. 1.1 at primary level for (i) the pure-NS reduction, (ii) the `s = 1, (q,p) = (4,2)` equality endpoint, (iii) the proof's quantitative dependence — specifically whether `‖u_θ/r‖_{L⁴_tL²_x} ≤ Q` and `‖u0‖_{H³} ≤ M` yield `sup_{t≤T}‖u(t)‖_{H³} ≤ F(ν,T,M,Q)` by constant-tracking of the existing proof alone. Verdict ∈ {QUANTITATIVE-BRIDGE / QUALITATIVE-ONLY / ENDPOINT-FAIL}. No Lean, no numerics, no T-SRC′ proof search.

**Method.** One dedicated primary deep-read lane (full ar5iv body, Sections 1–3, all lemmas) + main-loop adjudication; the endpoint arithmetic and the ball-uniformity of the extra datum input were independently re-derived at the main loop. Levels: [V-P] primary full text; [D] derived here.

---

## §1 — The three determinations

**(i) Pure NS reduction: CLEAN [V-P].** System (1.1) = axisymmetric MHD–Boussinesq without resistivity/diffusivity; the only structural hypothesis is `h₀^r = h₀^z = 0`; data `(u₀,h₀,ρ₀) ∈ H^m, m ≥ 3`, `∇·u₀ = 0`. Setting `h₀ ≡ 0, ρ₀ ≡ 0` satisfies every hypothesis; `H = h^θ/r` and `ρ` obey pure transport, so both vanish for all time and `u` solves pure axisymmetric NS with swirl. A full scan found **no** estimate that zero fields violate (no normalization, no non-vanishing condition, no division by field magnitudes); all `(h₀,ρ₀)`-constants degrade gracefully to the NS case (`L := Ω − 𝓛ρ` becomes `Ω = ω_θ/r`; the `I₁–I₃` and §3.4–3.5 blocks drop out). **Viscosity is normalized (`μ = 1` "without loss of generality")** — general-`ν` constants are recovered by the standard rescaling `ũ(x,τ) = ν^{−1}u(x,τ/ν)` (which maps `(T,M,M′,Q) ↦ (νT, ν^{−1}M, ν^{−1}M′, ν^{−3}Q)` — explicit, recorded [D]).

**(ii) Equality endpoint `s = 1, (q,p) = (4,2)`: GENUINELY COVERED [V-P].** Condition 1.1 (eq. (1.3)) is printed with **non-strict** `3/p + 2/q ≤ 1+s` and the single exclusion `p = 3/(1+s)` (handled by the smallness Condition 1.2 instead); at `s = 1` our member has `3/2 + 1/2 = 2` (equality) and `p = 2 > 3/2` (strictly inside — Condition-1.1 branch, no smallness). Proof level: the only place Cond. 1.1 is consumed is Lemma 3.2's estimates (3.15)/(3.16)/(3.22); the Young-produced Grönwall exponent is `2p/((1+s)p−3)`, whose reciprocal-pair identity reads `3/p + 2/q̃ = 1+s` **with equality — the equality member is the proof's native case**, not a limit: at `(s,p) = (1,2)` the exponent is exactly `4` (hand-checked at the main loop: `I₄₁ ≤ ‖u^θ/r‖₂‖L‖₄² ≤ C‖u^θ/r‖₂‖L‖^{1/2}‖∇L‖^{3/2} ≤ ¼‖∇L‖² + C‖u^θ/r‖₂⁴‖L‖²`). Closure is a **plain linear Grönwall** with coefficient `∈ L¹(0,T*)` supplied by (1.3) — no interval-splitting, no absolute-continuity device, no smallness. Sobolev–Hardy interpolation (Lemma 2.6) degenerates admissibly to plain Gagliardo–Nirenberg at `s = 1` (`θ = 0` allowed).

**(iii) Quantitative dependence: FULLY QUANTITATIVE [V-P].** The complete skeleton (steps 1–10 mapped in the lane report with equation numbers): maximum-principle/energy (Lemma 3.1) → the `(L,J) = (ω_θ/r − 𝓛ρ, ω_r/r)` Grönwall (Lemma 3.2, exponential in the Cond.-1.1 budget) → `sup_t‖Ω‖₂` (Cor. 3.4) → `ω_θ ∈ L^∞_TL²∩L²_TH¹` (3.26) → poloidal vorticity (3.29)–(3.30) → `sup_t‖∇u‖₂² + ∫‖∇²u‖²` (Lemma 3.5) → `∇u ∈ L¹_TL^∞` (§3.3, heat maximal regularity, explicit `T*`-powers) → (h/ρ blocks, vacuous here) → the **proved** `H^m` bound (§3.6, Kato–Ponce + Kozono–Taniuchi, "Gronwall twice"): `e + E_m(t) ≤ C(e+‖∇^m u₀‖₂²)^{exp(C∫(1+‖∇×u‖_∞))}`. **Every step is an explicit energy/interpolation/Grönwall estimate; every cited lemma is a quantitative inequality with absolute constants; there is no compactness, no contradiction argument, no profile decomposition, and no delegation to a qualitative criterion (no BKM citation — the `H^m` bound is proved, not assumed).** The only soft sentence is the terminal continuation restart, which sits *above* the proved a priori bound and is standard-quantitative local theory. Net shape: `F` = an explicit double-exponential tower in `(Q, T, data)`.

**Tracked extra datum input (the one substantive carry) [V-P + D].** Lemma 3.1(i) and the `s = 1` `J`-estimate (3.22) consume **`‖Γ₀‖_{L∞} = ‖ru₀^θ‖_{L∞}` — a tacit datum assumption, nowhere derived from `H³`**. Main-loop check [D]: it is genuinely NOT ball-uniform on the axisym `H³` `M`-ball (a swirl torus of major radius `R`, amplitude `a`, unit core has `‖u₀‖_{H³} ≳ aR^{1/2}` but `Γ₀ ~ aR`, so `Γ₀ ≲ MR^{1/2} → ∞` inside the ball) — a far-field-weight escape window, cousin of the C²-window. It is finite for every Schwartz member and is a standing class datum of the frozen corpus (`Γ₀` is B2's own parameter), so the correct handling is to carry it as an explicit second ball parameter.

## §2 — VERDICT and chain update

**VERDICT: QUANTITATIVE-BRIDGE.** For pure axisymmetric NS with swirl, `u₀ ∈ H³` divergence-free with `M′ := ‖ru₀^θ‖_{L∞} < ∞`:

> `‖u_θ/r‖_{L⁴_tL²_x([0,T′]×ℝ³)} ≤ Q` ⟹ `sup_{t≤T′}‖u(t)‖_{H³} ≤ F(ν, T, M, M′, Q)`,

with `F` explicit (double-exponential tower) by constant-tracking of the published proof alone — no new mathematics. **V-13 is DISCHARGED**: (i) clean, (ii) native equality coverage, (iii) quantitative with the single named carry `M′`.

**EV-1 (quantifier refinement, superseding the V-12 record's chain print).** The nu-layer conclusion is norm-uniform on the **two-parameter ball** `{axisym admissible, ‖u₀‖ ≤ M, ‖ru₀^θ‖_∞ ≤ M′}`, and T-SRC′'s own constant is correspondingly `Q₀(ν,T,M,M′)`:

```
[T-SRC′]  ‖u_θ/r‖_{L⁴_tL²_x} ≤ Q₀(ν,T,M,M′)      (OPEN — the head; quantifiers now exact)
   ▼ Arrow L+Q [V-P, THIS RECORD: Li–Pan Thm 1.3, s = 1, (4,2), pure-NS reduction,
                quantitative constant-tracking; ν by scaling]
[sup_t‖u‖_{H³} ≤ F(ν,T,M,M′,Q₀)] ⟹ (SEL-2) H-SEL^nu on the (M,M′)-ball;
   per-datum: T-SRC′(ds) ⟹ H-SEL^ds|_axisym unrestricted (M′ finite per member).
   ▼ (EB-1 + integration)  N0|_axisym; the GENERAL-class head stays OPEN and unclaimed.
```

The bridge from the head to `H-SEL|_axisym` is now **published-and-quantitative end to end** — the first head in this program's lineage whose entire downstream chain to the (subclass) target is verified known mathematics with tracked constants. What remains open is exactly the head itself.

## §3 — Consequences and residues

- **Refinement opportunity (recorded, not commissioned):** the `M′`-consumption sits only in the `J = ω_r/r` step at `s = 1` ((3.21)→(3.22)); a proof variant avoiding `J` (or estimating it without `Γ₀^{2s/(1+s)}`) would upgrade the nu-layer to `M`-only uniformity — bounded new work, flagged for any future proof/route session.
- **P-2 unchanged in shape** (budget + temporal-profile observable `h(t) = ‖u_θ/r‖₂²`), with the family design now also reporting `M′` per member (free to normalize: fix `M′` alongside `M`).
- **Residues (named, none load-bearing for the verdict):** the cited standard lemmas (GN, Hmidi–Rousset `𝓛`-boundedness, Lei/Miao–Zheng (2.5), CFZ Sobolev–Hardy, Biot–Savart CZ, heat maximal regularity, Kozono–Taniuchi) were verified as quantitative statements, not re-proved from their sources; a harmless exponent typo in §3.3's last display (`14/9` vs `9/14`) is noted; journal pagination taken from the AIMS listing.

## §4 — Claim boundary

RECORD-ONLY; no Lean edit; no numerics; no proof search on any open head. **Nothing here asserts, approaches, or implies a resolution of the Navier–Stokes Millennium problem, or of axisymmetric-with-swirl global regularity, in either direction.** T-SRC′ remains OPEN; this record verifies only that its downstream bridge is published, endpoint-valid, and quantitative, and fixes the exact quantifiers (EV-1). The logical-collapse caveat stands. Commissioning anything downstream (P-2, the `J`-refinement, or any proof work on T-SRC′) is a user act. C0 discipline throughout.
