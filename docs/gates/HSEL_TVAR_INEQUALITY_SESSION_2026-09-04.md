# HSEL_TVAR_INEQUALITY_SESSION — 2026-09-04 — T-VAR inequality session (twenty-second session): search for ONE new exact-NS inequality contributing to T-VAR without wall budgets; two new identities derived (both wall-level, FAILCASE); a STRUCTURAL OBSTRUCTION found — the symmetric-sector collapse lemma (SSC): on an NS-invariant sub-ball of the M-ball the Gram matrix is scalar for all time, so T-VAR (and T-DIR / T-DIR-SPK / T-GRAM / T-CONE / T-DET) coincide VERBATIM with full-enstrophy wall statements; VERDICT: ROUTE-KILLED (RECORD-ONLY on the open content; proved yields marked)

**Repo:** `c:/Users/corgi/Downloads/ns-mns2-flowmap-bridge` · **Status:** proof-session record. No Lean; no numerics. Proved items flagged [D] (each re-derived twice, signs/indices/measures re-checked); **no open statement is claimed and no new named sufficient condition is introduced** (per the commission). Lean baseline unchanged (8775-job gate).

**Commissioning provenance.** User instruction, 2026-09-04 (twenty-second session), paraphrased from the Japanese original: *do not create a new named sufficient condition; determine only whether at least one NEW inequality, derived from exact 3-D Navier–Stokes dynamics and actually contributing to T-VAR* — `∃e ∈ S²: ∫₀^{T′}(d/dt‖∂_e u(t)‖²_{L²})₊dt ≤ Q₀(ν,T,M)` — *can be proved to completion. Mere reformulation, replacement by a stronger sufficient condition, restatement into det/trace/eigenvalue language, or assumption of another open head does NOT count. Routes requiring the full-enstrophy / BKM / Serrin wall are rejected. No inequality ⟹ NO-PROGRESS; a structural obstruction to the lane itself ⟹ ROUTE-KILLED; an inequality ⟹ SUBSTANTIVE-PROGRESS, stating which term of T-VAR it improves and by how much. No numerics, no Lean.*

Notation as in the T-DIR/T-VAR records: `G_{ij} = ⟨∂ᵢu,∂ⱼu⟩_{L²}` (PSD; `trG = E := ‖∇u‖²₂`), `X_e = eᵀGe = ‖∂_e u‖²₂`, `D_{ij} = ⟨∇∂ᵢu,∇∂ⱼu⟩` (PSD; `trD = ‖∇²u‖²₂`), `𝒫_{ij} = ∫(∂ᵢu)ᵀS(∂ⱼu)dx` (`tr𝒫 = −∫ωᵀSω`), `G′ = −2νD − 2𝒫`, `R = νD + 𝒫 = −½G′`, `TV₊(f) = ∫₀^{T′}(f′)₊dt`. Free budgets: `∫₀^{T′}E\,dt ≤ M²/(2ν)`, `‖u(t)‖₂ ≤ M`, `X_e(0) ≤ E(0) ≤ M²`, `∫₀^{T′}trR\,dt = ½(E(0)−E(T′))`. Certified solutions are smooth strong solutions from admissible (real, divergence-free, Schwartz) data with `‖u₀‖_{H³} ≤ M`, on every horizon `T′ ≤ T` inside the maximal existence time.

---

## §0 — Result in one paragraph

No admissible new inequality exists to be found, and the reason is structural, not a failure of search: **the tetrahedrally-equivariant sub-ball of the M-ball is invariant under the NS flow, non-empty at every `M > 0`, and on it every Gram-type tensor of the lineage (`G, D, 𝒫, R, R₋, 𝔑`) is a scalar multiple of the identity at every time.** Hence on that sector `X_e(t) = E(t)/3` for **every** `e ∈ S²` and every `t`, so T-VAR reads `TV₊(E) ≤ 3Q₀` — the full-enstrophy rise budget, i.e. exactly the banned wall — and likewise T-DIR ⟺ `∫E²dt ≤ 9Q₀` (the `L⁴_tḢ¹` wall), T-DIR-SPK ⟺ `∫(∫ωᵀSω)₊dt ≤ 3Q₀` (the enstrophy-production wall), T-CONE ⟺ T-DET ⟺ `TV₊(E) ≤ 6Q₀`. The "∃e freedom", the "`λ_min` vs trace" and "`det` vs trace" strict weakenings are therefore strict only OFF this sector; ON it they are equalities. Consequently: any inequality valid for all certified solutions that contributes to T-VAR must, restricted to the sector, contribute to the enstrophy-rise budget (forbidden and unavailable); and any inequality that avoids this is anisotropy-conditional and vacuous on the sector, so no finite collection of such inequalities can close T-VAR. The wall-free T-VAR program (and by the same token the wall-free T-DET/T-CONE/T-DIR programs) is **ROUTE-KILLED**. Two genuinely new identities were derived along the way (the Lamb-vector form of the production tensor and its uniform-in-`e` domination); both have wall-level budgets and are recorded as FAILCASE so they are not re-derived.

## §1 — The commissioned search: candidates tried, and the two new identities [D]

**I-1 (the Lamb-vector representation of the production tensor) [D, new to the record].** Write NS in rotational form, `∂_tu = −ω×u − ∇π + νΔu`, `π = p + |u|²/2`. Then `X_e′ = 2⟨∂_eu, ∂_e∂_tu⟩ = −2⟨∂_e²u, ∂_tu⟩ = 2⟨∂_e²u, ω×u⟩ + 2⟨∂_e²u, ∇π⟩ − 2ν⟨∂_e²u, Δu⟩`. The pressure pairing vanishes (`div∂_e²u = 0`); two integrations by parts give `⟨∂_e²u, Δu⟩ = Σ_j‖∂_j∂_eu‖² = eᵀDe`. Comparing with the channel identity `X_e′ = −2νeᵀDe − 2P_e`:

> **`P_e = −⟨∂_e²u, ω×u⟩_{L²}`, and by polarization (both sides symmetric bilinear, equal on the diagonal) `𝒫_{ij} = −∫ ∂ᵢ∂ⱼu · (ω×u)\,dx` — the production tensor is the Hessian of `u` paired with the Lamb vector.**

Independent re-derivation: `P_e = ∫v·(v·∇)u` with `v = ∂_eu`; integrating by parts with `div v = 0`, `= −∫u·(v·∇)v = −∫u·((∂_eω)×v)` (the `∇|v|²/2` part dies against `div u = 0`) `= ∫∂_eω·(u×v) = −∫ω·∂_e(u×∂_eu) = −∫ω·(u×∂_e²u) = −⟨∂_e²u, ω×u⟩` ✓. Trace check: `tr𝒫 = −⟨Δu, ω×u⟩ = −⟨Δu, u·∇u⟩ = −∫ωᵀSω` ✓ (battery record §2b). The pressure is again absent, and only the Leray-projected Lamb vector `P(ω×u) = νΔu − ∂_tu` pairs.

**I-2 (uniform-in-`e` Lamb domination) [D, new; FAILCASE].** Cauchy–Schwarz on I-1 and `‖∂_e²u‖₂² ≤ eᵀDe` give `X_e′ ≤ −2ν‖∂_e²u‖² + 2‖∂_e²u‖‖P(ω×u)‖`, hence, maximizing over `‖∂_e²u‖`,

> **`(X_e′)₊ ≤ ‖P(ω×u)‖²₂/(2ν)` for every `e ∈ S²`, pointwise in time**, with the exact budget identity `∫₀^{T′}‖P(ω×u)‖²₂dt = ∫₀^{T′}‖∂_tu‖²₂dt + ν(E(T′)−E(0)) + ν²∫₀^{T′}‖Δu‖²₂dt` (from `P(ω×u) = νΔu − ∂_tu` and `⟨∂_tu,Δu⟩ = −E′/2`).

The budget is the `H²`-dissipation / `∂_tu` level (scaling `L^{−1}`, subcritical, equivalent to the banned wall). Rejected on sight per the rule; recorded because it is the sharpest uniform-in-`e` domination available and shows that **the ∃e quantifier is not even engaged by any pointwise domination** — see I-4.

**I-3 (accumulated production is bounded above, free) [D].** Integrating `𝒫 = −½G′ − νD` with `G(T′) ⪰ 0`, `D ⪰ 0`, `G(0) ⪯ M²I`: `∫₀^{T′}𝒫\,dt ⪯ ½G(0) ⪯ (M²/2)I`. So `∫P_e\,dt ≤ M²/2` for every `e` — a one-sided free bound on the *descent-producing* part; it says nothing about `(−P_e)₊` (it is P-c of the T-DIR-SPK record in tensor form). Not progress.

**I-4 (why no uniform-in-`e` domination can be sub-wall) [D].** For any ONB, `Σᵢ(X_{eᵢ}′)₊ ≥ (Σᵢ X_{eᵢ}′)₊ = (E′)₊`, so `avg_{e∈S²}(X_e′)₊ ≥ (E′)₊/3` and any bound `(X_e′)₊ ≤ A(t)` valid for all `e` forces `∫A ≥ TV₊(E)/3`, whose finiteness is the enstrophy bound. Hence every candidate of the form "pointwise domination of the rise" (I-2, Hölder/GN on `P_e`, strain-eigenvalue pointwise bounds `−P_e ≤ ∫(−λ₁(S))|∂_eu|²`, the `∂_tu`-pairing `|X_e′| ≤ 2‖∂_e²u‖‖∂_tu‖`) is wall-level by construction — the only room is in the ∃e, i.e. in anisotropy. §2 shows that room is absent on an invariant sector.

**I-5 (Fourier/transfer form, for the record) [D].** With `μ_t = |û(·,t)|²dξ`, `G = ∫ξξᵀdμ_t`, `D = ∫ξξᵀ|ξ|²dμ_t`, `𝒫 = ∫ξξᵀρ_t(ξ)dξ` where `ρ_t = Re(û*·(ω×u)^) = −½T_t` is minus half the nonlinear energy-transfer density (`∫ρ_t = 0`). T-VAR asks for a direction whose `(e·ξ)²`-weighted transfer has budgeted positive part; the triad identity `T_ξ+T_η+T_ζ = 0` yields no sign for `(e·ξ)²T_ξ+(e·η)²T_η+(e·ζ)²T_ζ = T_ξ b(c−a) + T_η a(c−b)` (`a,b,c = e·ξ, e·η, e·ζ`, `a+b+c=0`). No free structure.

No candidate produced an admissible inequality. The reason is §2.

## §2 — THE STRUCTURAL OBSTRUCTION: the symmetric-sector collapse lemma (SSC) [D]

Let `Γ ⊂ SO(3)` be the tetrahedral rotation group `T ≅ A₄` (order 12), generated by `d₁ = diag(1,−1,−1)`, `d₂ = diag(−1,1,−1)` and the cyclic permutation `C: e₁↦e₂↦e₃↦e₁` (`Cd₁C⁻¹ = d₂`, so `⟨d₁,d₂,C⟩ = V₄ ⋊ C₃ = T`; all determinants `+1`). For `g ∈ O(3)` and a vector field `u` put `(g·u)(x) := g\,u(gᵀx)`. Call `u` **Γ-equivariant** if `g·u = u` for all `g ∈ Γ`.

**SSC-1 (invariance under the NS flow).** If `(u,p)` is a strong solution on `[0,T′]` with admissible datum `u₀`, then `(g·u, p(gᵀ·))` is a strong solution with datum `g·u₀` [D: `∂_t`, `Δ`, `∇p` commute with the action; `(g·u)·∇(g·u) = g[(u·∇)u](gᵀx)` and `div(g·u) = (div u)(gᵀx)` by `gᵀg = I`]. All lineage norms (`H³`, `L²`, the certified lifespan) are `O(3)`-invariant, so `g·u₀` is admissible in the same `M`-ball with the same certified horizons. By **uniqueness** of certified/strong solutions on a common horizon (the Lean-level unrestricted uniqueness; classically the strong-solution uniqueness), `g·u₀ = u₀ ⟹ g·u(t) = u(t)` for all `t ∈ [0,T′]`. **The Γ-equivariant sub-ball `𝔅_Γ(M) := {u₀ admissible, ‖u₀‖_{H³} ≤ M, Γ-equivariant}` is invariant under the certified flow.**

**SSC-2 (non-emptiness at every `M > 0`, infinite-dimensional).** Take a Schwartz vector potential `A(x) = φ(x)a` with `a ∈ ℝ³∖{0}` and `φ(x) = e^{−|x−x₀|²}`, `x₀` generic (its Γ-orbit has 12 distinct, well-separated points). Its Γ-average `Ā = (1/12)Σ_{g∈Γ} g·A` is Γ-equivariant, Schwartz, and non-zero (`Ā ≈ φ\,a/12` near `x₀`). Then `u₀ := ∇×Ā` is Γ-equivariant (curl commutes with rotations), divergence-free, Schwartz, real, generically non-zero; rescaling by a constant places it anywhere in the ball. Varying `x₀, a, φ` gives an infinite-dimensional family. ✓

**SSC-3 (all Gram-type tensors transform by conjugation).** `G[g·u] = g\,G[u]\,gᵀ` [D: `∂ᵢ(g·u)_a(x) = g_{ab}g_{ic}(∂_cu_b)(gᵀx)`, unit Jacobian, `Σ_a g_{ab}g_{ab′} = δ_{bb′}`]. Identically `D[g·u] = gDgᵀ` (inner gradient contracted), `𝒫[g·u] = g𝒫gᵀ` (`S[g·u](x) = gS[u](gᵀx)gᵀ`), hence `R, R₋` (spectral calculus commutes with conjugation) and `𝔑 = ∫R₋dt` likewise. On a Γ-equivariant solution every one of these matrices `Y(t)` satisfies `Y = gYgᵀ` for all `g ∈ Γ`.

**SSC-4 (the commutant is scalar).** `d₁Yd₁ = Y ⟹ Y₁₂ = Y₁₃ = 0`; `d₂Yd₂ = Y ⟹ Y₂₃ = 0`; so `Y = diag(a,b,c)`; `CYCᵀ = Y` permutes the diagonal cyclically ⟹ `a = b = c`. **Hence `Y = (trY/3)\,I`.** (Any finite `Γ ⊂ O(3)` whose action on symmetric matrices has scalar commutant — e.g. the octahedral, icosahedral groups and their reflection extensions — works verbatim.)

**SSC (the collapse).** For every certified solution from `𝔅_Γ(M)`, every `T′ ≤ T`, every `t ∈ [0,T′]` and **every** `e ∈ S²`:

| object | on the Γ-equivariant sector | consequence |
|---|---|---|
| `G(t)` | `(E(t)/3)I` | `X_e(t) = E(t)/3` ∀e — the channel IS one third of the enstrophy |
| `D(t)` | `(‖∇²u‖²₂/3)I` | `eᵀDe = ‖∇²u‖²/3` — the directional `H²`-dissipation IS one third of the full one |
| `𝒫(t)` | `−(1/3)(∫ωᵀSω)I` | `(−eᵀ𝒫e)₊ = (∫ωᵀSω)₊/3` — the directional production IS one third of vortex stretching |
| `R(t)` | `−(E′/6)I`, `R₋ = ((E′)₊/6)I` | `𝔑(T′) = (TV₊(E)/6)I`; `λ_min𝔑 = tr𝔑/3`; `det𝔑 = (tr𝔑/3)³` — **AM–GM is an equality** |

and therefore, **verbatim on the sector** (the ∃e is void — every `e` gives the same number):

- **T-VAR ⟺ `TV₊(E) ≤ 3Q₀`** ⟹ `sup_{t≤T′}‖∇u(t)‖²₂ ≤ M² + 3Q₀` — the full-enstrophy bound (the wall; with the classical `Ḣ¹` blow-up criterion it is quantitative global regularity of the sector);
- **T-DIR ⟺ `∫₀^{T′}‖∇u‖⁴₂dt ≤ 9Q₀`** — the `L⁴_tḢ¹` (Beirão-da-Veiga-type `(4,2)` gradient) wall, the records' "E-2/L_d wall quantity"; the Zhang/CFZ `∂₃u ∈ L⁴_tL²_x` bridge criterion is, on the sector, `∇u ∈ L⁴_tL²_x` — **not sub-wall**;
- **T-DIR-SPK ⟺ `∫₀^{T′}(∫ωᵀSω)₊dt ≤ 3Q₀`** — the full enstrophy-production budget (the T-SPK record's §4 wall, the quantity the averaging no-go called wall-level);
- **T-GRAM**: `∫G = (∫E/3)I` — every direction is a "canonical" direction (this is exactly the probe's R1 Taylor–Green finding: triple-degenerate `E_min`, `R̃ ≡ 1.000` — SSC in action, unrecognized at the time);
- **T-CONE ⟺ `TV₊(E) ≤ 6Q₀`** and **T-DET ⟺ `TV₊(E) ≤ 6Q₀`** — the "strictly weaker than the trace" claims of the twentieth/twenty-first records hold off the sector and are **equalities on it**: `λ_min𝔑 = tr𝔑/3`, `det𝔑 = (tr𝔑/3)³`.

**SSC-5 (what the sector contains).** `𝔅_Γ(M)` has no dimension reduction and no known regularity theorem; discrete-symmetry classes of this kind (Kida–Pelz / Boratav–Pelz high-symmetry flows, octahedral; the Taylor–Green vortex) are the classical *singularity-candidate* classes of the numerical literature. Assuming regularity of the sector would be assuming an open (Clay-level, in-class) statement — ROUTE-SWAP by the standing rule; no such assumption is made or available.

**Battery on SSC itself [D]:** (i) the 2.5-D sanity family (F7, `∂_eu ≡ 0` for some `e`) is the opposite extreme (maximally anisotropic Gram) — consistent; (ii) the kinematic rotating-anisotropy barrier (F2) is off-sector (its Gram is anisotropic) — SSC is the complementary, on-sector obstruction; (iii) small-data/O-1: symmetric small data are regular with bounded `E`, so T-VAR holds there — consistent; (iv) the probe's Taylor–Green run exhibits the collapse numerically (record-only cross-check, not load-bearing).

## §3 — Why the verdict is ROUTE-KILLED and not NO-PROGRESS [D]

The commission's target is an inequality `𝔍` valid for **all** certified solutions of the M-ball that lowers a term of T-VAR without a wall budget. Restrict any such `𝔍` to `𝔅_Γ(M)`: by SSC every T-VAR term becomes the corresponding full-enstrophy term over 3, so `𝔍|_{𝔅_Γ}` is an inequality lowering `TV₊(E) = ∫(2∫ωᵀSω − 2ν‖∇²u‖²)₊dt` — a sub-wall bound on the vortex-stretching / enstrophy-rise budget for a class with no reduction. That is (a) exactly what the rule rejects and (b) unavailable (its existence for the sector would be an in-class regularity theorem). The dichotomy is therefore exhaustive:

1. **Uniform contributions** (valid on the whole ball, non-vacuous on the sector) are wall contributions — rejected/unavailable (I-4 is the pointwise instance; SSC is the general one).
2. **Anisotropy-conditional contributions** (vacuous on the sector, e.g. any "gain" `tr𝔑/3 − λ_min𝔑`, `(tr/3)³ − det`, frame-coherence gains, negative-cone anti-equidistribution) can never *close* T-VAR, because T-VAR must also hold on the sector where they contribute nothing and the whole obligation is the wall. Converting a per-time anisotropy gain into a fixed-`e` gain moreover requires the open frame-coherence input (SP-b), so even this class supplies no *proved* inequality today.

Hence the lane "prove T-VAR from exact NS by wall-free inequalities" cannot succeed **as a matter of structure**: T-VAR *contains* the wall as a verbatim sub-statement on an invariant sector. This is sharper than the standing "Clay-equivalent-or-harder" caveat, which concerned the *consequence* of T-VAR through the CFZ bridge; SSC concerns its *content*: the positional claims that justified the lane — "sub-wall bridge criterion" (channel search C4), "half a criticality unit above free mathematics with the ∃e freedom", "strictly weaker than the banned trace" (T-CONE §3, T-DET §1) — are all void on `𝔅_Γ(M)`. The same holds for every member of the family and for any future "∃-direction / anisotropy-invariant" head: a head whose defining tensor is Gram-type collapses to its trace on the sector. **Standing battery item added (SYM-test): before commissioning any ∃-direction / anisotropy head, evaluate it on the Γ-equivariant sector; if it reduces to a wall statement there, it is not sub-wall.**

## §4 — Cross-checks and consistency [D]

- **No contradiction with the proved arrows.** T-DET ⟹ T-CONE ⟹ T-VAR ⟹ T-DIR remain proved; on the sector they are all the single statement `TV₊(E) ≲ Q₀` (constants 6 : 6 : 3 : 9 in the table of §2) — consistent with the constant-2 and `λ_min ≤ det^{1/3}` arrows.
- **Polarity unchanged.** A blow-up in the sector violates every member (forced through the bridge and now directly: `E → ∞`); a blow-up off the sector is subject to the prior analysis. No counterexample is asserted; no regularity is asserted.
- **The kinematic barrier and SSC are complementary.** Off the sector the open input was priced as anti-equidistribution of the accumulated negative cone (the F2 rotator); on the sector the cone is *always* fully isotropic (`R₋ ∝ I`), so "anti-equidistribution" is *false* there and the obligation is amplitude control = the wall. Thus the T-CONE/T-DET "missing NS input" (3-D anti-equidistribution / codimension-1 confinement) **cannot be an NS theorem** on the whole ball — it fails identically on `𝔅_Γ(M)` — which is a second, independent way to see that the T-DET proof session recommended in HANDOFF cannot succeed wall-free.
- **Probe cross-reference.** The tetrahedral/octahedral collapse is visible in the existing Taylor–Green run (triple-degenerate spectrum of `∫G`); a T-DET-targeted probe would only re-observe SSC on symmetric data and the F2-type anisotropy on generic data; it cannot inform a wall-free proof. Not commissioned; no numerics run.

## §5 — VERDICT

**ROUTE-KILLED.** No new inequality contributing to T-VAR without a wall budget exists to be proved (§1, §3); the obstruction is structural and proved (§2): **on the NS-invariant, non-empty Γ-equivariant sub-ball, T-VAR and its whole family coincide verbatim with full-enstrophy wall statements, so the ∃e / anisotropy / det-vs-trace room that defined the lane is empty on a sector the theorem must cover.** Not NO-PROGRESS (the negative result is a theorem about the lane, not a null search); not SUBSTANTIVE-PROGRESS (I-1/I-2 are new identities but wall-level — FAILCASE; nothing lowers any T-VAR term sub-wall).

**Consequences (recorded recommendations; each execution is a user act):**
1. The general T-DIR lane's *wall-free* program (T-DIR / T-DIR-SPK / T-GRAM / T-VAR / T-CONE / T-DET) is closed as a proof route; the heads remain OPEN statements with their verified bridge, but their positional value ("sub-wall", "strictly weaker than trace") is withdrawn on `𝔅_Γ(M)`. Recommended: **PARK the general lane** (the DEAD-END consequence anticipated in HANDOFF "Next work" item 1 now fires in its strongest form).
2. The pending items "T-DET proof session" and "T-DET-targeted probe" are **moot** for a wall-free proof and are not recommended.
3. **Erratum annotations** (appended, dated, to the affected records — no silent repair): channel search §2 collapse check (passes generically, fails on the sector); quantifier battery §2c/§3 (F-family lacked the symmetric family; the "open content = anisotropy" statement is sector-false); T-VAR §3, T-CONE §1/§3, T-DET §1/§2 ("strictly weaker than trace" ⟹ "strictly weaker off the sector, equal on it").
4. Fallback ordering HR-1 / HR-3′ stays on file; before any commissioning, apply the SYM-test of §3 (pointwise-geometric heads such as CF-type direction coherence do not automatically collapse under a discrete symmetry — the test is cheap and must be run, not assumed).
5. Standing items unchanged: axisym assets parked; SEL-3/SEL-5/EB-1 on hold; M-1 on hold; local Elan gate only.

## §6 — Claim boundary

No open statement is proved or disproved: T-VAR, T-DIR, T-DIR-SPK, T-GRAM, T-CONE, T-DET, H-SEL, N0 remain OPEN as statements; SSC shows they *contain* the enstrophy wall on an invariant sector, nothing more. The [D]-items are: NS `O(3)`-covariance + uniqueness (flow invariance of equivariant data), the conjugation law of Gram-type tensors, an elementary commutant computation, an explicit non-empty equivariant Schwartz family, and two integration-by-parts identities (I-1, I-2). **Nothing here asserts, approaches, or implies a resolution of the Navier–Stokes Millennium problem in either direction** — in particular, no statement about the regularity or singularity of symmetric flows is made. Per the commission no new named sufficient condition is introduced (SSC is an obstruction lemma, not a head). Parking, pivoting, erratum adoption into the kill table, and any probe or proof commissioning are user acts; the appended errata are annotations, not freeze-review rulings.
