# HSEL_TSPK_MECHANISM_AUDIT — 2026-09-02 — T-SRC′ temporal-spike mechanism audit: exact h-evolution identity derived; a quadratic-damping interpolation CLOSES the reduction machinery; T-SRC′ compresses to ONE spike-exclusion lemma (T-SPK, the inflow spin-up work budget); STOP RULE FIRES — the transferable abstraction lands on the Serrin wall, the lane stops and control returns to the general N0/H-SEL side (RECORD-ONLY)

**Repo:** `c:/Users/corgi/Downloads/ns-mns2-flowmap-bridge` · **Status: RECORD-ONLY.** No Lean file touched; no numerics; no proof search on T-SRC′ (the audit derives a *sufficient reduction*, commissioned explicitly; T-SRC′ and the new lemma both remain OPEN); nothing frozen moved. Lean baseline unchanged (8775-job gate).

**Commissioning provenance.** User instruction, 2026-09-02 (thirteenth session): with `q = u_θ/r`, `h(t) = ‖q(t)‖²_{L²}`, fixed `(ν,T,M,M′)` on the axisymmetric-with-swirl class — derive the exact evolution identity/differential inequality for `h` from the Hou–Li `q`-equation; combine with the known `∫₀^T h dt ≤ C(ν,M)` and `‖Γ(t)‖_∞ ≤ M′`; enumerate ALL temporal anti-concentration mechanisms that could give `h ∈ L¹_t ⟹ h ∈ L²_t` (one-sided `h′` bounds; spike height vs minimum lifetime; Γ-max weighted interpolation; viscous suppression of high `h`; `u_r/r` stretching cancellation/sign/localization); test each counterexample-first vs scaling and frozen profiles; classify CLOSES / SURVIVES / DEAD-END; decide whether T-SRC′ compresses to ONE spike-exclusion lemma. **Additional stop rule:** for each surviving mechanism decide axisymmetric-specific vs transferable-to-general-3D; if all are axisym-specific, STOP this lane and return to the general N0/H-SEL side; if ≥1 is transferable, select exactly that one as the next research-theorem candidate. No numerics, no Lean, no T-SRC′ proof search.

**Method.** Main-loop mathematical derivation ([D], standard-level, each step re-checked for signs, measures, and scaling); the counterexample battery uses the frozen profile vocabulary; the stop-rule adjudication applies the head-reduction audit's fence discipline (§2 of `TSEL_HEAD_REDUCTION_AUDIT_2026-09-02.md`).

---

## §1 — The exact evolution identity [D]

From the verified Hou–Li `q`-equation `∂_t q + u_pol·∇q = νΔ̃q − 2(u_r/r)q` (`Δ̃ = ∂_r² + (3/r)∂_r + ∂_z²`), pairing with `q` in `L²(ℝ³)` (measure `r dr dz dθ`; the transport term vanishes by 3-D incompressibility; the 5-D viscous operator integrates by parts in the 3-D measure leaving a good-signed axis trace):

> **`h′(t) = −2ν D(t) − 4 S(t)`**, with `D = ‖∇q‖²_{L²(ℝ³)} + c_ax∫ q(0,z)² dz ≥ 0` and `S(t) = ∫ (u_r/r)\,q²\,dx` (unsigned; `u_r < 0` = inflow makes `−4S > 0` — the classical spin-up: at fixed `Γ`, inflow amplifies `q = Γ/r²`).

Known inputs: **(K-a)** `∫₀^T h dt ≤ ‖u₀‖²_{L²}/(2ν)` (energy dissipation contains `∫u_θ²/r² = ∫q²`); **(K-b)** `|q| ≤ M′/r²` (Γ-max); **(K-c)** `sup_t‖u(t)‖_{L²} ≤ ‖u₀‖_{L²} ≤ M`; **(K-d)** `h(0) ≤ CM²` ball-uniformly (weighted 1-D Hardy at weight `a = −1 < p−1 = 1` — the `q`-weight is on the good side of the Hardy threshold, unlike `η`'s).

## §2 — Mechanism table (counterexample-first)

| ID | Mechanism | Finding | Class |
|---|---|---|---|
| **M-A** | exact `h`-identity | derived above; the ONLY growth channel is inflow stretching | **CLOSES** (component) |
| **M-B** | one-sided `h′` upper bound from known quantities alone | dimensionally forced to the cubic-supercritical level (`h′ ~ λ³ ~ h³`-class); every route to a closed `h′ ≤ F(h, known)` needs an uncontrolled norm; an Osgood-closable coefficient would prove T-SRC′ outright | **DEAD-END** standalone (subsumed by M-D + the budget) |
| **M-C** | spike height ↔ minimum lifetime | Chebyshev on (K-a) caps width-at-height (`τ_H ≤ 2C/H`) but `∫h²` still needs a height cap; the *decay* side is settled by M-D's universal envelope `h(t) ≤ 1/(κ(t−t₀) + 1/h(t₀))` — every spike decays below `λ` within `1/(κλ)`; the *rise* side funnels entirely into the stretching budget | partially **CLOSES** (decay), rise subsumed |
| **M-D** | **viscous suppression: the quadratic-damping interpolation** — outer split `∫_{r>R}q² = ∫_{r>R}u_θ²/r² ≤ M²/R²` (uses `u_θ = rq`; not even `M′`) + per-`z`-slice 2-D Gagliardo–Nirenberg on `q(·,z) ∈ H¹(ℝ²)` (radial; **no axis log** — 2-D GN does not see the origin) + Hölder in `z` gives, absorbing at `R² ~ M²/h`: **`D(t) ≥ c\,h(t)²/M²`** — scale-consistent (both sides `λ³`). Hence `h′ ≤ −κh² + 4S₋`, `κ := 2νc/M²`, `S₋ := ∫(u_r/r)_-\,q²dx` | **CLOSES** — the engine of the reduction |
| M-E | Γ-max weighted interpolation | `M′` gives `\|q\| ≤ M′/r²` but every attempted insertion worsens the axis weight (`r^{−3}`, `r^{−5}` integrands); **the reduction below needs `M′` nowhere** (it enters only downstream, in Li–Pan's J-step) | SURVIVES as unused auxiliary |
| M-F | stretching cancellation / sign / localization | dual form [D]: `S = ⟨ψ₁, ∂_z(q²)⟩`-pairing — the *same object* as the η-equation source; the **unweighted** analogue `∫∫(u_r/r)u_θ²` is the swirl→poloidal energy-exchange term, **budgeted for free by the energy identity**; the open content is exactly the `r^{−4}` concentration weight (from `u_θ²` to `u_θ²/r⁴`), and only the **inflow sign** `(u_r/r)_-` matters — the unsigned time-integral is nearly free (`∫₀^T S dt = (h(0)−h(T))/4 − (ν/2)∫D`, two-sidedly tied to the identity); the §5.3(iii) unsigned-`u_r` unknown reappears as the precise obstruction | **SURVIVES** — where any proof of the reduced lemma would live |

Battery: scaling of `∫h²dt` is exactly invariant (T-SRC′ is critical — consistent); frozen `S_blob` members violate the reduced budget below at ALL window exponents (`𝔖₋`-rate `~ Γ₀²τ^{−γ−α−β}`, divergent since `γ+α ≥ 1` — cleaner polarity than T-SRC′'s own `β_v`-conditional profile arithmetic, consistent with the reduction being sufficient-not-equivalent); Type-I violates; snapshots guarded; every polarity is also logically forced through the verified Li–Pan bridge.

## §3 — THE REDUCTION: one spike-exclusion lemma

Integrating M-D's inequality over `[0,T′]`:

> **`κ ∫₀^{T′} h(t)² dt ≤ h(0) + 4\,𝔖₋`**, `κ = 2νc/M²`, `𝔖₋ := ∫₀^{T′}∫ (u_r/r)_-\,q²\,dx\,dt`.

With (K-d), **T-SRC′ compresses to exactly one open lemma**:

> **T-SPK (spike-exclusion / inflow spin-up work budget; norm-uniform; OPEN):** ∀ν,T,M,M′ ∃Q₀(ν,T,M,M′): every certified solution from the admissible axisym `(M,M′)`-ball satisfies, on every certified horizon, `𝔖₋ ≤ Q₀`.
>
> **T-SPK ⟹ T-SRC′** is PROVED at [D]-standard level by §1–§3 (and thence, by the verified quantitative bridge, `⟹ H-SEL|_axisym ⟹ N0|_axisym`). The converse is not claimed: T-SPK is sufficient-shaped, possibly strictly stronger — its selection value is **structure**, not weakness: it is a single, monotone-in-time, sign-localized scalar (the cumulative work done by axis-directed inflow against the swirl concentration `q²`), maximally falsifiable, and it isolates the open content of the whole axisym lane in one physical quantity. The unweighted version of the same quantity is free (M-F); the entire difficulty is the `r^{−4}` weight and the unsigned `u_r`.

**Commissioned judgment: YES — T-SRC′ reduces to one spike-exclusion lemma**, with the reduction machinery (identity + quadratic damping + decay envelope) fully closed as known-standard mathematics, `M′`-free.

## §4 — STOP-RULE ADJUDICATION: the lane stops here

**Transferability of the surviving mechanism.** The architecture of §3 transfers verbatim to general 3-D NS [D]: with `E(t) = ‖∇u(t)‖²_{L²}`, the trivial interpolation `E = −⟨u,Δu⟩ ≤ ‖u‖₂‖Δu‖₂` gives `‖Δu‖² ≥ E²/M²`, the enstrophy identity gives `E′ ≤ −(2ν/M²)E² + N(t)` (`N` = the positive part of the nonlinear enstrophy production), and a budget on `∫N₊dt` yields `E ∈ L²_t`, i.e. `u ∈ L⁴_tḢ¹ ↪ L⁴_tL⁶` — **the Serrin-critical pair `(4,6)`, whence regularity by known theory.** So a transferable "temporal anti-concentration lemma" is *writable* — but it IS the statement "enstrophy: `L¹_t ⟹ L²_t` uniformly", which is a member of the **Serrin-critical L_d family = the E-2 fence of the head-reduction audit (EQUIVALENT-TO-KNOWN-HARD-PROBLEM)** — inadmissible as a new head by the standing discipline.

**Structural finding (recorded — this is the audit's deepest output):** the *same* free architecture (quadratic damping from interpolation + a production budget) exists in both settings; what differs is where the resulting lemma lands. In general 3-D, the `L¹→L²` upgrade of the (full) enstrophy channel **is** the wall. In axisym-with-swirl, the same upgrade applied to the *swirl channel* `h = ‖u_θ/r‖₂²` lands **strictly inside** the wall (Li–Pan) and compresses to T-SPK. This is a precise mechanism-level explanation of why the axisym subclass sits at half-unit distance while the general class sits on the wall — and it says that any general-class breakthrough via this architecture would need a *partial* channel of the general enstrophy with its own free `L¹_t` budget and sub-wall criterion, which no known structure supplies (consistent with C-3 and the S-7 mechanism note).

**Ruling per the stop rule:** the only *admissible* surviving candidate (T-SPK) is **axisymmetric-specific** (it consumes `q = u_θ/r`, the `r = 0` geometry, the axisym Biot–Savart dual pairing, and the swirl-channel energy budget essentially); the transferable abstraction is fence-classified and hence not selectable. **All admissible survivors are axisym-specific ⟹ THE LANE STOPS HERE.** T-SPK is parked as the axisym lane's compressed proof target (with its proved reduction), available on any future re-commission (P-2's observable set extends naturally: `𝔖₋(t)` is a cheap monotone scalar). **Control returns to the general N0 / H-SEL side.**

## §5 — Claim boundary

RECORD-ONLY; no Lean edit; no numerics; no proof search on T-SRC′ or T-SPK (the §1–§3 derivations are the commissioned mechanism analysis and reduce one open statement to another — T-SPK remains OPEN, and nothing open was proved: the closed steps are kinematic interpolation and energy identities at standard level, flagged [D] throughout; a targeted prior-art check on the M-D interpolation (Hardy–GN family, likely known-adjacent) is a non-load-bearing residue). **Nothing here asserts, approaches, or implies a resolution of the Navier–Stokes Millennium problem, or of axisymmetric-with-swirl global regularity, in either direction.** The logical-collapse caveat applies to T-SPK as to every head. The stop-rule ruling is an application of the commissioned rule plus the standing fence discipline; re-opening the axisym lane, commissioning general-side work, or adopting anything downstream is a user act. C0 discipline throughout.
