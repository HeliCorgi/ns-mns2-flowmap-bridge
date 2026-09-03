# HSEL_CHANNEL_SEARCH — 2026-09-03 — general N0 channel-search audit: the T-SPK design conditions applied to general 3-D NS; VERDICT: ONE-CHANNEL-SELECTED — the directional-derivative channel `X_e = ‖∂_e u‖²_{L²}`, with a pressure-free identity, an explicit quadratic-damping reduction, and TWO published smallness-free bridges at the native (4,2) member; the T-SPK record's closing conjecture is corrected (EC-1) (RECORD-ONLY)

**Repo:** `c:/Users/corgi/Downloads/ns-mns2-flowmap-bridge` · **Status: RECORD-ONLY.** No Lean file touched; no numerics; no direct proof search; nothing frozen moved. Lean baseline unchanged (8775-job gate).

**Commissioning provenance.** User instruction, 2026-09-03 (fourteenth session): apply the T-SPK design conditions to general 3-D incompressible NS and search for scalar/partial-enstrophy channels `X(t)` other than full enstrophy, requiring (C1) an unconditional `L¹_t`/energy-level budget, (C2) coercive dissipation in the evolution identity, (C3) sign/localization-decomposable nonlinear production, (C4) an `X ∈ L²_t`-type upgrade that does NOT collapse onto the Serrin/BKM wall, (C5) no axisymmetry/swirl/`r = 0` geometry. Mandatory candidates: strain/vorticity decomposition, strain-eigenvalue channels, one-component derivative channels, helicity-type quantities, localized/frequency partial enstrophy. Evaluate each on FREE-BUDGET / COERCIVITY / SUB-WALL-BRIDGE / EXACT-NS-SPECIFIC / FAILCASE; apply the equivalence-collapse check (div-free identities, elliptic estimates, Riesz transforms) with immediate rejection; counterexample-first (frozen failcases / Tao averaged / scaling). Verdict binary: ONE-CHANNEL-SELECTED (exactly one, with precise theorem candidate, quantifiers, exponents, downstream N0 bridge) / NO-ELIGIBLE-CHANNEL (then stop this route; next = HR-1, runner-up HR-3′; no further norm-channel enumeration).

**Method.** Main-loop structural analysis ([D], signs/measures/scaling re-checked) + one first-hand literature lane for the single decision point the structure could not settle (the published coverage of the native `(q_t,p_x) = (4,2)` member of the one-component-derivative criterion families). Levels: [V-P]/[V-adj]/[V-abs]/[D] as before.

---

## §1 — Design conditions, formalized from the T-SPK architecture [D]

For a channel `X(t) = ‖x(t)‖²_{L²}` with `x` a `∇u`-order quantity: (C1) `x` pointwise dominated by the dissipation density ⟹ `∫X dt ≤ M²/(2ν)` free; (C2) an evolution identity `X′ = −2νD_X − 2P_X` with `D_X ≥ 0` coercive, plus the **antiderivative-pairing interpolation** (`X = ⟨x,x⟩ = −⟨(antiderivative), ∇·x-pairing⟩ ≤ M‖∇x‖` whenever `x`'s antiderivative is energy-bounded) giving `D_X ≥ X²/M²` and hence the quadratic damping `X′ ≤ −κX² + 2(P_X)₋`, `κ = 2ν/M²`; (C3) `P_X` decomposable; (C4) the upgrade `X ∈ L²_t` must feed a **published, smallness-free, sub-wall** criterion at the native member `(q_t,p_x) = (4,2)` (the only member the free budget + damping natively deliver); (C5) no axisym input. The equivalence-collapse check precedes everything.

## §2 — Channel table

| Ch | Channel | FREE-BUDGET | COERCIVITY | SUB-WALL-BRIDGE | EXACT-NS-SPECIFIC | FAILCASE / verdict |
|---|---|---|---|---|---|---|
| 1 | strain / vorticity split (`‖S‖₂²`, `‖ω‖₂²`) | — | — | — | — | **REJECTED at the collapse check**: for div-free fields `‖S‖₂² = ½‖∇u‖₂² = ½‖ω‖₂²` — constant multiples of full enstrophy (div-free identity) |
| 2 | strain-eigenvalue channels (`‖λ₂⁺‖₂²` etc.) | ✓ (`λ₂⁺ ≤ \|S\|`) | **✗ — fatal**: eigenvalues are non-smooth functionals at crossings; no evolution identity, no dissipation structure, `‖∇λ₂⁺‖` undefined/uncontrolled | plausibly ✓ (Miller's critical line contains (4,2); V-2 undischarged) | ✓ | REJECTED at COERCIVITY — recorded as the nearest structural miss |
| **3a** | **directional-derivative channel `X_e = ‖∂_e u‖²_{L²}`, `e ∈ S²`** | ✓ (`\|∂_e u\| ≤ \|∇u\|`) | **✓✓ — the identity is pressure-free** [D]: differentiating NS in `e` and pairing with `∂_e u`, transport vanishes (div-free) and `⟨∇∂_e p, ∂_e u⟩ = −⟨∂_e p, div ∂_e u⟩ = 0`; `X′_e = −2ν‖∇∂_e u‖² − 2P_e`, `P_e = ∫(∂_e u)ᵀ S (∂_e u)\,dx` (only the strain survives the quadratic form); damping via `X_e = −⟨u, ∂_e²u⟩ ≤ M‖∇∂_e u‖` ⟹ `X′_e ≤ −κX_e² + 2(−P_e)₊`, `κ = 2ν/M²` **with constant exactly 1 in the interpolation — cleaner than the axisym case (no GN needed)** | **✓ VERIFIED [V-P]**: `∂₃u ∈ L⁴_tL²_x` (criticality `2/4+3/2 = 2`, exact) is a published smallness-free criterion TWICE over — **Zhang, Bull. Math. Sci. 7 (2017), Thm 2** (window `q ∈ [(3√37)/4−3, 3] ≈ [1.562,3] ∋ 2`, Leray–Hopf class) and **Chen–Fang–Zhang, MMAS 44 (2021), Thm 1.1** (window `q ∈ (3/2,6]`, extended to Leray–Hopf by their Remark 2); Lorentz-refined Chen–Le–Qian JDE 2021 (`q₀ ∈ (3/2,∞)`, `L^{p₀,1}_t`) as backup; `q = 2` is interior to both windows (robustness margin); the pre-2015 Kukavica–Ziane windows do not reach `q = 2` — the post-2015 literature closes the point | ✓ (component/direction structure not averaging-preserved; the criterion proofs consume anisotropic div-free + pressure representation) | **SELECTED** (battery §3) |
| 3b | one-component gradient `‖∇u₃‖₂²` | ✓ | ✓ but the identity retains the pressure term `⟨Δu₃, ∂₃p⟩` | ✓ VERIFIED: **Wolf, Analysis 35 (2015)** — exactly `∇u³ ∈ L⁴(0,T;L²)` ⟹ regular, weak Leray class [V-adj verbatim abstract]; O JMAA 2023, Wang–Wei–Wu–Zhou JDE 2025 extensions [V-abs] | ✓ | eligible; ranked below 3a (pressure survives in the identity) |
| 3c | two-component vorticity `‖ω̃‖₂²`, `ω̃ = (ω₁,ω₂)` | ✓ | ✓ (vorticity equation is pressure-free; antiderivative pairing via `u`) | ✓ VERIFIED: **Chae–Choe, EJDE 1999 No. 05, Thm 1** — `ω̃ ∈ L^{α}_tL^{γ}_x`, `2/α+3/γ ≤ 2`, `γ ∈ (3/2,∞)` ∋ (4,2), no smallness [V-P] | ✓ | eligible; ranked below 3a (production `(ω·∇u)_h·ω̃` carries the out-of-channel factor `ω₃∂₃u_h` — worse localization) |
| 4 | helicity `∫u·ω` | signless; only `\|H\| ≤ ME^{1/2}` | **✗**: `dH/dt = −2ν∫ω·∇×ω` — unsigned dissipation | ✗ — no helicity-based criterion exists | — | REJECTED |
| 5 | frequency-shell partial enstrophy `‖Δ_j∇u‖₂²` | ✓ | ✓ per shell (`ν2^{2j}`) | **✗ collapse**: any `j`-uniform upgrade is the Besov-endpoint form of the `L⁴_tḢ¹` wall (log-refinements only) | **✗ — doubly fatal**: shell energetics are exactly what Tao's averaging PRESERVES (C-3 violation; his cascade lives here) | REJECTED |
| 5′ | spatially localized enstrophy `∫φ\|∇u\|²` | ✓ | local | ✗ collapse onto the CKN/local-regularity family (E-3 fence adjacency) | ✗ — the local pressure flux is the FC-086-surviving obstruction (SS-4 L_d R2) | REJECTED |
| 6 | single vorticity component `‖ω₃‖₂²` | ✓ | ✓ (pressure-free, pairing works) | **✗ — OPEN**: no published `ω₃`-only criterion for general data in ANY `(q,p)`; Neustupa–Penel call it verbatim "a challenging open problem" [V-adj]; their positive result needs a spectral projection, not `ω₃` | ✓ | REJECTED at SUB-WALL-BRIDGE (a two-open-link chain) |

**Collapse checks passed for the 3-family:** `∂_e u` / `∇u₃` / `ω̃` are genuinely partial — no div-free identity, elliptic estimate, or Riesz transform recovers the full gradient from any of them (this is precisely why the anisotropic criterion literature is nontrivial); none of the three criteria is a Serrin/BKM restatement.

## §3 — The selected channel: battery and reduction

**Battery [D]:** scaling — `∫X_e²dt` exactly invariant (same criticality geometry as T-SRC′: the head sits at the critical line, one half unit above the free `L¹_t` budget). Frozen `S_blob`: all gradient directions are active and comparable in the printed core ⟹ every direction's channel is violated ⟹ the ∃-direction head is violated ✓ polarity (also logically forced through the verified bridge). Type-I: `X_e ~ (T−t)^{−1/2}` ⟹ `∫X_e²` log-diverges ✓ (exactly critical, as expected). Tao averaged: no distinguished-direction structure survives averaging — the proof bar (C-3) is respected by construction; snapshots guarded. FAILCASE: none.

**THE SELECTED THEOREM CANDIDATE (norm-uniform; OPEN — never asserted):**

> **T-DIR:** ∀ν>0, ∀T<∞, ∀M<∞: ∃Q₀(ν,T,M) < ∞ such that for every admissible Schwartz datum with `‖u0‖ ≤ M` and every certified solution on every certified horizon `T′ ≤ T` there exists a unit vector `e ∈ S²` (fixed over the horizon) with
> **`∫₀^{T′} ‖∂_e u(t)‖⁴_{L²(ℝ³)} dt ≤ Q₀`.**
>
> (∃-direction form = weakest member; the fixed-`e₃` ∀-datum variant is the stronger family member. Exponents: time 4, space 2 — the architecture's native, published-bridged member.)

**Proved reduction [D] (the general T-SPK analogue, cleaner):** `κ∫₀^{T′}X_e²dt ≤ X_e(0) + 2𝔓₋` with `κ = 2ν/M²` exactly, `X_e(0) ≤ M²` trivially ball-uniform, and

> **T-DIR-SPK (the compressed form; OPEN):** `𝔓₋ := ∫₀^{T′}\big(−∫(∂_e u)ᵀ S (∂_e u)\,dx\big)_+ dt ≤ Q₀(ν,T,M)` — the budget on compressive-strain amplification work along one direction, **with the pressure exactly cancelled from the channel** and the production a pointwise strain quadratic form (direct kinship with the vortex-stretching/λ₂ literature).

**Downstream N0 bridge (the prize — this chain ends at the GENERAL class):**

```
[T-DIR]  (or T-DIR-SPK ⟹ T-DIR by the proved reduction)
   ▼ rotate e ↦ e₃; Arrow B1 [V-P: Zhang BMS 2017 Thm 2 AND Chen–Fang–Zhang MMAS 2021
     Thm 1.1 — two independent smallness-free criteria at (4,2), Leray–Hopf class;
     class-match bookkeeping: certified solutions are smooth strong solutions ⊂ that class]
[regularity on [0,T′]] ⟹ per-datum: N0^ds for the GENERAL certified class (EQ-4(a) compactness)
   ▼ Arrow B2 [debt V-15: quantitativity of the Zhang/CFZ proofs — needed only for the
     norm-uniform layer, exactly as V-13 was for the axisym lane]
[norm-uniform H³] ⟹ (SEL-2) H-SEL^nu ⟹ (EB-1 + integration) N0 ⟹ Lean N1→N2→N3.
```

**EC-1 (correction to a prior record).** The T-SPK record's §4 closing remark — "a general-class breakthrough via this route needs a partial enstrophy channel with its own free `L¹_t` budget and a sub-wall criterion, **which no known structure supplies**" — is **overturned by this audit's verification**: the directional-derivative channel supplies exactly that (free budget trivially; published bridges 2015–2021). The remark was conjecture-level and is corrected, not the stop ruling itself (which correctly applied its rule to what was then verified); the T-SPK record is annotated. The stop rule of THIS audit does **not** fire; HR-1/HR-3′ remain the recorded fallback ordering should T-DIR die downstream.

## §4 — VERDICT

**ONE-CHANNEL-SELECTED: Ch-3a, the directional-derivative channel**, with T-DIR as the theorem candidate and T-DIR-SPK as its compressed production-budget form. Selection over the two other eligible family members (C0 — a selection, not uniqueness): 3b retains the pressure term in its identity; 3c's production carries an out-of-channel factor; 3a has the pressure-free identity, the exact-constant damping, a self-contained strain-form production, two independent published bridges with `q = 2` interior to both windows, and the ∃-direction weakening. Relation to the original roster: T-DIR upgrades the HR-7 (one-component) family — which scored low for "no mechanism" — by equipping it with the full T-SPK architecture (free budget + quadratic damping + pressure cancellation) and verified bridges; the general lane now has the same single-open-link shape the axisym lane achieved: **only the head (a budget statement half a criticality unit above free mathematics) is open, for the GENERAL certified class.**

Debts: **V-15** (Zhang 2017 / CFZ 2021 proof quantitativity + class-match bookkeeping — load-bearing for the nu-layer only; the ds-layer needs only the qualitative criteria, which are [V-P]); V-2 (Miller) remains open and non-load-bearing; the Wolf/Chae–Choe/CLQ alternates are recorded as bridge redundancy.

## §5 — Claim boundary

RECORD-ONLY; no Lean edit; no numerics; no proof search on T-DIR/T-DIR-SPK/H-SEL/N0 (the §3 identity and reduction are the commissioned mechanism analysis — kinematic pairings and energy identities at [D]-standard level; both new statements remain OPEN). **Nothing here asserts, approaches, or implies a resolution of the Navier–Stokes Millennium problem in either direction.** The logical-collapse caveat applies to T-DIR as to every head (universally proved, it implies general-class continuation through the published criteria); its selection value is positional — a free `L¹_t` budget, an explicit `κ = 2ν/M²` damping, a pressure-cancelled production, published bridges, and a single scalar falsification observable. Commissioning anything downstream (V-15 discharge, a P-2-style probe on `X_e(t)`/`𝔓₋(t)`, or proof work) is a user act. C0 discipline throughout.

---

**Erratum / annotation (2026-09-04, twenty-second session; see `docs/gates/HSEL_TVAR_INEQUALITY_SESSION_2026-09-04.md`, the symmetric-sector collapse lemma SSC).** The §2 collapse check ("no div-free identity, elliptic estimate, or Riesz transform recovers the full gradient from `∂_e u`") is correct for general fields but the channel DOES collapse on an NS-invariant sub-ball: for tetrahedrally-equivariant certified solutions `‖∂_e u‖²₂ = ‖∇u‖²₂/3` for every `e` and every `t`, so on that sector T-DIR is the `L⁴_tḢ¹` wall and the (4,2) bridge criterion is the full-gradient criterion — design condition C4 ("does NOT collapse onto the wall") fails there. The sector is non-empty at every `M`. Add the SYM-test to the collapse check.

---

**PARK annotation (2026-09-04, twenty-fifth session; user ruling).** The general T-DIR / T-DIR-SPK / T-GRAM / T-VAR / T-CONE / T-DET lane that this record opened is **PARKED** with `docs/gates/HSEL_TVAR_INEQUALITY_SESSION_2026-09-04.md` (SSC) as closing evidence; see `docs/gates/HSEL_HR3_BATTERY_GAP_2026-09-04.md` §0 for the parked state and the registered un-park trigger. Nothing in this record is retracted beyond the errata already appended.
