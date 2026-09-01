# The Scope-B `β_v` endpoint-pinning decision — EXECUTED

**Ruling: `YES (CONSISTENT)`. Scope-free exponent/region arithmetic does NOT pin `β_v`.**

Date: 2026-08-23 (JST). Commissioned by the user's explicit instruction of the same day
("β_v endpoint-pinning decision theorem の proof search を開始せよ。YES/NO どちらの決着も
成果とする"), under the standing constraints *frozen assumptions unchanged*, *no new formal
infrastructure*, *research-side frozen scope not to be strengthened or altered*. Selection
record: [`STAGE9_DECISION_SELECTION_2026-08-23.md`](STAGE9_DECISION_SELECTION_2026-08-23.md).

**RECORD-ONLY.** No map edit, no promotion, no demotion, no re-armed row, no CAP trigger.
Every map consequence in §6 is a **proposal for the next user-adjudicated freeze review**.
Verdicts unchanged: **BH stays YELLOW-RED; B2 stays UNKILLED in Scope B; trigger (T-c) stays
OPEN.**

Method: 1 statement fixer → 4 independent pin provers (distinct angles: Γ-saturation
structure / energy-dissipation-`L³` budgets / ancient-limit zoom / K3-covering-and-region
combinatorics) → 3 independent witness builders → 3 cross-examiners (witness breaker, pin
breaker, location-premise auditor) → 1 adjudicator, all reading the frozen sources
first-hand. Every pin attempt returned `PIN_FAILED`; the pin breaker confirmed none was
abandoned prematurely; the witness breaker eliminated two of three witness families; the
adjudicator substituted a sharper elimination reason and a repaired primary witness, which
is re-verified below.

---

## 1. The decision, as fixed

**Class.** `u` an axisymmetric finite-energy suitable weak solution of standard-`ν`
incompressible Navier–Stokes on `R³`, first singular time `T* < ∞`, Type-II rate
(`√τ·‖u(t)‖_∞ → ∞`, `τ := T*−t`), asymptotics fitting the frozen power-law exponents
`‖u(t)‖_∞ ≍ τ^{−γ}`, core scale `≍ τ^{α}`, with

```text
(γ, α) ∈ S_blob = {1/2 < γ < 1,  max(1−γ, 2γ/3) ≤ α < γ,  α > 2γ−1}      (K11 cut; A7 strict)
```

core = an on-axis blob carrying the `L³` divergence (**class B2**), `Γ := r·u_θ` with
`‖Γ(t)‖_∞ ≤ Γ₀` (Γ-max) and **non-evanescent** `liminf_{t→T*}‖Γ(t)‖_∞ ≥ c₀Γ₀`,
and **no Scope-A hypothesis**.

**Saturation scale.** `r_sat(t;c′) := inf{ r : sup_{dist ≤ r}|Γ(·,t)| ≥ c′Γ₀ }`; the
scope-free envelope `Γ(r) ≤ min(Γ₀, r‖u‖_∞)` forces `r_sat ≥ c′Γ₀/‖u‖_∞`, so
`β_v ∈ (0,γ]` where `r_sat ≍ τ^{β_v}`. `β_v = γ` means **τ-uniform constant-attainment at
the envelope corner** `r = Γ₀/‖u‖_∞` (B13 — not a bare exponent equality).

**Middle limb `M`** (operative quantifier form): ∃ fixed `c′ ∈ (0,1)` with
`r_sat(t;c′) = o(τ^{α})`, while `r_sat(t;c′)·‖u(t)‖_∞/Γ₀ → ∞` for **every** fixed `c′`.
In the power-law vocabulary: `β_v ∈ (α, γ)`.

**Question.** Is `M` consistent with the conjunction of the frozen scope-free rows — Γ-max;
K3 with its covering placement; K5 (energy **and** dissipation); K6 with [D2] as corrected in
A3; K9's `L^∞` endpoint under the A1 `σ_core`/`σ_sup` split **at the correct radius** (the
`τ^{α−γ}` misfire check mandatory); K11; K4‴ [D, unconditional]; K4′ [C on (E⁺)+(P)] with its
printing rule — or does scope-free arithmetic **pin** `β_v` to
`{β_v ≤ α} ∪ {β_v = γ, τ-uniform}`?

---

## 2. Ruling

**`YES (CONSISTENT)`.** The middle limb is **row-compliant**, and not at an isolated point:
the witness family projects onto **all of `S_blob`**, so the pin fails at every surviving
exponent pair, not merely somewhere.

**Certificate conditionality: NONE.** K4′ is not consumed anywhere in the certificate, so no
`[(E⁺)+(P)]` print is owed and no step carries `[C]` on that account. (Rule restated for the
record: any chain consuming K4′ must print `[(E⁺)+(P)]`, is `[C]`, and can never be a
scope-free pin — `BH_M3_KNSS_GATE_2026-08-20.md` §6 + B1, with (P)'s Scope-B status
unresolved.)

---

## 3. The certificate — witness `W★`

```text
γ = 3/5,   α = 9/20,   β_v = 1/2                    (exact rationals; /20 units below)

Region C  ("core"; amplitude carrier AND designated L³ carrier)
    (ρ, λ, v, γ_j, σ) = (9/20, 9/20, 27/20, 12/20, 8/20)
    ⇒ |u|_C ≍ τ^{−3/5},  |u_θ|_C ≍ τ^{−2/5} at r ≍ τ^{9/20},  V_C ≍ τ^{27/20}
    ⇒ Γ_C ≍ τ^{ρ−σ} = τ^{1/20} → 0        — C is NOT Γ-saturated

Region S  ("Γ-saturated intra-core sub-core" — A2's own name for the limb)
    (ρ, λ, v, γ_j, σ) = (10/20, 10/20, 30/20, 10/20, 10/20)
    ⇒ |u|_S ≍ |u_θ|_S ≍ τ^{−1/2} at r ≍ τ^{1/2},  V_S ≍ τ^{3/2}
    ⇒ Γ_S ≍ τ^{ρ−σ} = τ⁰ ≍ Γ₀            — GENUINELY Γ-saturated (σ = ρ exactly)
```

Both regions use **only the printed blob shape** `v_j = 3λ_j`, `ρ_j = λ_j`
(`TYPE2_SURVIVAL_MAP` §1). No unprinted shape is used anywhere.

**One circulation field realizing `β_v`, consistent across both regions:**

```text
Γ(r,t) = Γ₀ · min( (r/τ^{1/2})^k , τ^{1/2}/r ),      any fixed k > 1, τ-uniform constants
```

- `r_sat(t;c′) = c′^{1/k}·τ^{1/2}` for **every** `c′ ∈ (0,1)` ⇒ `β_v = 1/2`, τ-uniformly;
- at `r ≍ τ^{9/20}` the outer branch gives `Γ = Γ₀τ^{1/20}`, hence `|u_θ| = Γ₀τ^{−2/5}`,
  i.e. `σ_C = 2α − β_v = 2/5` — the two regions are read off **one** field, not posited
  independently;
- `‖Γ(t)‖_∞ = Γ₀` (attained at `r ≍ τ^{1/2}`) and `liminf‖Γ(t)‖_∞ = Γ₀`: Γ-max **and**
  non-evanescence hold with `c₀ = 1`;
- the outer branch decays like `1/r`, so the swirl energy is `Γ₀²·(axial extent)` —
  **log-free** (no `Γ ≡ Γ₀` plateau over a polynomial range of radii; see OOV-3).

**Middle-limb quantifiers, checked:** `r_sat = c′^{1/k}τ^{1/2} = o(τ^{9/20})` ✔ (existential
clause); `r_sat·‖u‖_∞/Γ₀ ≍ τ^{1/2−3/5} = τ^{−1/10} → ∞` for **every** `c′` ✔ (corner
attainment fails, universal clause). So `W★` genuinely realizes `M` and is **not**
relabellable onto either endpoint (see §7 D-1).

### Row-by-row (each row at its own evaluation radius)

| Row | Evaluated at | Arithmetic | Verdict |
|---|---|---|---|
| `S_blob` (A7) | printed `(γ,α)` | `max(1−γ, 2γ/3) = 8/20 ≤ 9/20`; `9/20 < 12/20`; `9/20 > 2γ−1 = 4/20` **strict** | PASS |
| K1 | global | `γ = 3/5 > 1/2`; enstrophy exponent `(2γ−α)/2 = 3/8 ≥ 1/4` | PASS |
| K2 | global | `√τ‖u‖_∞ ≍ τ^{−1/10} → ∞` (Type II) | PASS |
| Γ-max | **pointwise, each region's own radius** | C: `σ = 8/20 ≤ ρ = 9/20`; S: `σ = ρ = 10/20` (equality **is** saturation; [H7] is non-strict) | PASS |
| envelope | attainment radius `τ^{1/2}` | `r‖u‖_∞ ≍ τ^{−1/10} ≫ Γ₀`: the flat branch binds; attainment is a **diverging** factor `τ^{−1/10}` from the corner | PASS |
| K5a energy | each region's own volume | C: `27/20 ≥ 24/20`; S: `30/20 ≥ 20/20`; shares `τ^{3/20}`, `τ^{1/2}` → 0 | PASS |
| K5b dissipation | each region's own `λ` **and** `v` | C: `2γ+2λ−v = 3/4 < 1`; S: `1/2 < 1`; enstrophy `τ^{−3/4}+τ^{−1/2}`, `dτ`-integrable | PASS |
| K5 non-descent (A13) | original flow only | no energy/`Γ∈L^p` statement transported to any rescaled limit (none taken) | HONOURED |
| K6 | designated carrier C | `v = 27/20 < 3γ = 36/20` ⟺ `α < γ`; `‖u‖³_{L³}|_C ≍ τ^{−9/20} → ∞`, **power-law** (so A3's premise holds) | PASS |
| K6 at S | S's own volume | `v = 30/20 = 3γ_j` exactly ⇒ `L³` mass `Θ(1)`: S neither carries nor obstructs the ESŠ divergence; not the designated carrier | PASS (face recorded, OOV-1) |
| K6/[D2] (A3) | swirl-sup **location** premise at `r ≍ ρ_j` | at C: `σ ≠ γ_j` ⇒ premise false ⇒ silent. At S: `σ = γ_j` at `r ≍ τ^{1/2}` ⇒ **fires**, and its printed arithmetic forbids S from carrying `L³` ⇒ carriers forced apart, `N = 2` realized **constructively** | PASS |
| K3 | violation placed at C; **every** `ε ∈ (0,1]` | `E_C(ε) = −3/20 + ε/20 ≤ −2/20 < 0` on all of `(0,1]`; single-region criterion `ρ ≤ γ_j ∧ γ_j > 1/2` holds ⇒ C covers alone; adding S can only lower `min_j E_j` | PASS |
| K9 (CFZ `L^∞`) | **at S's own radius** `τ^{1/2}` | `|u_θ|_S r^d ≍ τ^{−(1−d)/2} → ∞` for every `d < 1` ⇒ criterion inapplicable. Dictionary form "∃j: `σ_j = ρ_j > 0`" supplied by S | PASS |
| K9 under A1 split | which `σ` is cut | `σ_core = 2/5` at `r ≍ ℓ`; `σ_sup = 1/2` at `r ≍ τ^{1/2}`; they differ. The `σ ≤ α` half is **true** here — what fails is the **pinning** | PASS |
| K9 **mandatory `τ^{α−γ}` misfire check** | performed | Γ-max cap at `ℓ` is `τ^{−9/20}`; at the true violation radius it is `τ^{−1/2}`; ratio `τ^{α−β_v} = τ^{−1/20} → ∞`. Not committed: every row above is read at its own radius | CHECK PASSED |
| K11 | amplitude-growing core, printed `(γ,α)` only | `γ+α = 21/20 ≥ 1`; `∂ₜu ≍ τ^{−8/5}`, convection/pressure `≍ τ^{−33/20}` dominate by `τ^{−1/20}` — a term responds. **No per-region `K11` asserted** (licence limit honoured) | PASS |
| K7 | global | no cut on power-law ansätze; divergence is `τ^{−9/20}` | VACUOUS |
| K8 [C on (T)] | blob row | no cut (both regions on-axis, non-translating); conservative ring-clause check `ρ_j ≥ min(1−γ,1/2) = 2/5` also holds | N/A, PASS |
| K10 | edge `γ+α = 1`, `γ ∈ (1/2,3/5)` | `γ+α = 21/20 ≠ 1` **and** `γ = 3/5 ∉ (1/2,3/5)`: off the edge on both counts | N/A |
| K4 (A6 rider) | zoom route only | at the unzoomed level `sup r|u| ≍ τ^{α−γ} = τ^{−3/20} → ∞`, so the `C/r` hypothesis fails on the original flow; **no ancient-limit step is taken** | does not fire |
| K4‴ [D] | the ancient limit, all rescaled radii | `‖Γ‖_∞ ≤ Γ₀` globally ⇒ any limit inherits `|v_θ| ≤ Γ₀/r`. Transfer row, `K = ∅` in `(γ,α)` — nothing to violate | CARRIED |
| K4′ [C on (E⁺)+(P)] | excluded subset `M3 ∩ {γ₂ < γ}` | `W★ ∉ M3` (no region has `ρ = σ = γ_j = γ`) ⇒ **not consumed**, no `[(E⁺)+(P)]` owed | not consumed |

---

## 4. Why the pin fails — the structural reason

All four independent angles failed, and they failed for **one** reason, which the pin
breaker and the location auditor confirmed independently:

> **The frozen scope-free rows contain no statement that LOCATES Γ-saturation.**

Every consumed row is, on `β_v`, either **neutral** or **one-sided in the wrong direction**:

- **Γ-max** is an upper bound on `Γ`, hence (given (H1)) an upper bound on `r` — *never* a
  lower bound on the saturation radius (`BH_RB2_ANCHOR_AUDIT` §2, verbatim: "Γ-max bounds `r`
  above, never below"). It is satisfied *with equality* by saturation.
- **the envelope** bounds `r_sat` only from **below** (`β_v ≤ γ`).
- **K9** is *existential in the region* — "some region has `σ_j = ρ_j > 0`"
  (`BH_MULTIREGION_AUDIT` §1) — so it supplies only a **floor**; it selects no radius, and
  `β_v = max{ρ_j : region j Γ-saturated}` is unconstrained above. It "cuts nothing in
  `(γ,α)`" by the corpus's own statement.
- **K5**'s two clauses, applied to the innermost Γ-saturated structure, reproduce `S_blob`'s
  own floor with `α → β_v`; both are **monotone-relaxed** by shrinking that structure. A
  swirl-dominated region (`γ_j = σ_j = ρ_j`) satisfies K5a and K5b *identically for every*
  `ρ_j ∈ (0,1)` — K5 cannot cut a Γ-saturated region anywhere.
- **K6** acts on the *designated* carrier only; **[D2]/A3** imposes a region-count **floor**
  that `M` meets constructively.
- **K3**'s cover is discharged by the core alone and is **monotone under adding regions**.
- **K11** mentions only `(γ,α)` and is already implied by `S_blob`.
- **K4‴** is a transfer row with empty excluded set; **K4/K4′** do not reach the class.

A conjunction of constraints each neutral or one-sided-monotone in `β_v` **cannot carve out
the open middle interval `(α,γ)` while admitting both of its endpoints.** Structurally: a
`Γ₀`-saturated structure of radius `a` has swirl energy `≍ Γ₀²·(axial extent)` (subcritical,
`a`-independent), `L³` content `≍ Γ₀³` (exactly critical, scale-invariant), and enstrophy
`≍ Γ₀²/a`, `dτ`-integrable for every `β_v < 1`. **The critical-norm budgets are blind to it
at every scale**, so they cannot separate A2's three limbs.

The pin has exactly two horns, and each is exactly one of the two inputs the corpus has
removed from Scope B:

1. **K9's razor location premise** `r ≍ ℓ` — demoted by P6/A1/A2. Using it is the recorded
   `τ^{α−γ}` misfire, so the mandatory check **fires against the pin**. And even *granting*
   it in full, `β_v` is still not pinned: a `Γ` plateau on `[τ^{β_v}, τ^{α}]` satisfies
   `σ_core = α` while `r_sat = τ^{β_v}`, `β_v > α` — and such a plateau is enstrophy-free
   (`ω_z = r^{−1}∂_rΓ = 0` on it), so no frozen row charges it.
2. **the Scope-A amplitude corollary** — which is precisely what makes `(T3)` **empty in
   Scope A**, i.e. why the pin is *trivially true there* and unreachable here. Granting it
   **changes the class** (the decision stipulates "no Scope-A hypothesis"), so the correct
   verdict is `YES`, not `PIN_CONDITIONAL`.

Its only Scope-B-shaped surrogate in the corpus, K12″'s homogenization-driven Γ-depletion, is
report-level, never promoted, `[C]` on a Prandtl–Batchelor/Bragg–Hawthorne profile premise
(hence not scope-free), and **inactive on `{α < 1/2}` by its own audit** — precisely where
`W★` lives (`α = 9/20`).

---

## 5. The minimal logical gap

The single named object that would pin `β_v`, stated in the frozen vocabulary:

> **(Γ-DEP)** — *intra-core circulation depletion* — **genuinely new, named here.**
> ∃ `c′ ∈ (0,1)` and `δ > 0`, both **τ-uniform**, such that for all `t` near `T*`
> ```text
> sup_{ dist(x, axis) ≤ δ·τ^{α} } |Γ(x,t)|  <  c′·Γ₀ .
> ```
> In words: **`Γ` cannot saturate strictly between the envelope corner `τ^γ` and the core
> scale `τ^α`.**

**Sufficient, and minimal.** (Γ-DEP) gives `r_sat(t;c′) ≥ δτ^{α}` at that fixed `c′`, hence
`β_v ≤ α` — the pin's first horn, hence the pin. It must be τ-uniform **and** hold at a
**fixed** `c′`; a version with `c′ = c′(τ) → 0` is sub-polynomial and out of vocabulary (A3).
Nothing weaker in that direction suffices: every frozen row is neutral or one-sided-monotone
in `β_v`, and the rows bound `r_sat` only from below, so a pin requires exactly a **new upper
bound on `Γ` inside the core, of constant-factor strength**.

**Why every candidate input is unavailable at frozen scope:**

| candidate | status |
|---|---|
| Scope-A amplitude corollary `r_min ≤ √42 Γ₀/‖u‖_∞` | **Scope-A-only**; granting it is a **class change**, not a condition. Also caps `Γ(L)` and does **not** bound it below (B2/F31) |
| per-level swirl-fraction bound | **FALSE outside Scope A** (B9; Hill witness) — no Scope-B analogue can even be a weakening |
| neck poloidal level bound, `sup(ω_θ/r)`, `ℓ_neck`, `θ_coh` | **declined by fork (β)** |
| (E⁺⁺)/(COH-Δ)/(ANCH-κ)/(NECK)/T4/W1–W5 | **undefined, not open, in Scope B** (B9) |
| K12″ (axis-Dirichlet homogenization) | closest in **shape**; report-level, never proposed for the map, `[C]` on a profile-level premise, and **inactive on `α < 1/2`** by its own audit. Corroborates the naming of the gap; does not fill it |
| "swirl-poverty ⟹ thinness exchange" | the nearest **recorded** request (recon §4 item 4) — a different statement, recorded **unmet/absent** |
| **V1** | **unpromoted**, and — checked at source — the frozen [V1] is the `C/r` KNSS-type Liouville family, **not** a viscous cutoff. Its hypothesis **fails** on `W★` (`sup r|u| ≍ τ^{−3/20} → ∞` at the core), so even if promoted it would be **inert** |
| unprinted per-region K11 (`γ_j + λ_j ≥ 1`) | **not printed** anywhere (licence limit); its energy-flux premise is broken for a region embedded in a faster ambient flow. Would give only `β_v ≥ 1/2` — `W★` satisfies it (`γ_2+λ_2 = 1`) |
| a viscous-cutoff premise (not V1, unpromoted) | would give only `β_v ≤ 1/2` — does not pin |
| **both of the last two, granted together** | yields `β_v = 1/2` **exactly**, still strictly inside the middle limb whenever `α < 1/2 < γ` — `W★` is precisely such a member. **Even the two strongest unavailable inputs, granted simultaneously, do not reach the endpoint set** |
| R-B2′ / R-B1 / K4″ | Scope-A-gated on B2; B6's load-bearing rider: even a granted (SB-ANCH) does **not** transplant R-B2′ to Scope B |
| K4′ | `[C]` on (E⁺)+(P) with (P) unresolved in Scope B; never a scope-free pin, and does not reach this class |

**New or already named?** **(Γ-DEP) is genuinely new** — it exists nowhere in the corpus at
any scope. The named ledger objects behave as follows:

- **(SB-ANCH)** would close the pin's *second* horn — but it **is** that horn: B6's single
  equivalent form plus B13 give `(SB-ANCH) ⟺ {β_v = γ, τ-uniform}`. A pin conditional on its
  own conclusion is not a pin. (Re-derived independently this pass: `M ⟹ ¬(SB-ANCH)`, and
  more generally **`{β_v < γ} = ¬(SB-ANCH)` exactly**, because (H1) is false at any radius
  `≫ Γ₀/‖u‖_∞` — it would force `|Γ| ≍ τ^{β_v−γ} → ∞`, contradicting Γ-max.)
- **the amplitude corollary** would suffice but only by changing the class.
- **V1** is unpromoted **and** inert.

**There is no third route.** Either (Γ-DEP) is proved, or the class is changed to Scope A.

---

## 6. Consequences for the frozen map — PROPOSALS ONLY

**Nothing below is applied.** Drafted for the next user-adjudicated freeze review.

- **P1. A2's trichotomy debt — partially discharged, in one direction only.** Proposed
  amendment of A2's middle-limb rider, from "unanalysed, carried as an open debt" to:
  *"analysed against the frozen scope-free rows (2026-08-23): the limb `β_v ∈ (α,γ)` is
  **row-compliant on all of `S_blob`** — no scope-free pin to `{β_v ≤ α} ∪ {β_v = γ,
  τ-uniform}` exists; the debt narrows to (i) the existence question (out of scope for
  exponent bookkeeping) and (ii) (SB-ANCH)."* **The NO side of the debt is closed; the debt
  as a whole is NOT discharged.**
- **P2. (T3)'s Scope-B status — strengthened, not changed in kind.** From "live and never
  claimed in Scope B" to *"live in Scope B and, on the frozen scope-free rows, row-compliant
  on all of `S_blob`; R-B2′ still has no zoom centre there (unchanged); its Scope-A emptiness
  by the amplitude corollary is untouched."*
- **P3. Frontier sentence — proposed addition** after "first named gap (SB-ANCH) ⟺ `β_v = γ`":
  *"; the complement `{β_v < γ}` is not reachable by scope-free arithmetic — the middle limb
  `β_v ∈ (α,γ)` is row-compliant at every point of `S_blob`, and closing it needs the new
  object (Γ-DEP), absent at every scope (the Scope-A corollary excepted, which is a class
  change)."*
- **P4. Two new record-only true statements** in the frozen vocabulary:
  (i) `{β_v = γ, τ-uniform} ⟺ (SB-ANCH)`, hence `M ⟹ ¬(SB-ANCH)` and
  `{β_v < γ} = ¬(SB-ANCH)` exactly — re-derived from Γ-max alone, independently of B6's
  route;
  (ii) on **all** of `{β_v < γ}` the flow is sup-swirl-poor at the saturation radius:
  `|u_θ|(r_sat) ≍ τ^{γ−β_v}‖u‖_∞ = o(‖u‖_∞)`, so (H1) is unattained there — **generalizing**
  the anchor audit's (T3) note from the single value `β_v = α` to every `β_v < γ`.
- **P5. K9 §2 hygiene.** §2's blob paragraph still prints "the swirl exponent on its fibers
  is pinned to `σ = α`", already superseded by A2. Proposal: strike it in place, since this
  decision turned on that exact pinning.
- **P6. New survival row, drafted and NOT asserted:** *"Middle-limb realization (record-only,
  [B] bookkeeping): for every `(γ,α) ∈ S_blob` and every `β_v ∈ (α,γ)`, the two-region tuple
  `C = (α, α, 3α, γ, 2α−β_v)`, `S = (β_v, β_v, 3β_v, β_v, β_v)` satisfies every frozen
  scope-free row. This is exponent bookkeeping and NOT a survival claim about
  Navier–Stokes."*
- **P7. Queued independently, not dropped:** the mandatory row-(i) update for **Seregin
  arXiv:2606.29468** (log-corrected Type-II families; reduction to open ancient-Euler
  Liouville theorems). It touches this decision's out-of-vocabulary boundary directly
  (OOV-4).

---

## 7. Scope of the ruling — what is NOT decided

1. **Consistency of exponent arithmetic is NOT existence of a Navier–Stokes solution.**
   `W★` is an exponent/region assignment plus one circulation profile, **not a flow**.
   Nothing here constructs, exhibits, or implies a blow-up. **No Clay claim of any kind is
   made or implied.** The certificate says only: the frozen rows do not exclude this
   bookkeeping, therefore they do not pin `β_v`.
2. **Not decided: realizability.** The corpus's own single-time **coexistence / one-pressure**
   debt for multi-region tuples is inherited by `W★` exactly as by every other multi-region
   tuple on the map, and is **not** discharged here.
3. **Not decided in Scope A.** `(T3) = B2 ∩ {β_v < γ}` remains **empty in Scope A** by the
   amplitude corollary. This ruling is **Scope-B only**, exactly as the class stipulates.
4. **Not decided: (SB-ANCH).** `W★` is a model of its negation *at the bookkeeping level*;
   that confirms (SB-ANCH) is not a consequence of the frozen rows, and closes **nothing**
   about whether it holds for actual solutions.
5. **Not decided: any marginal / logarithmic / sub-polynomial face** (OOV below).
6. **No frozen assumption was changed, strengthened, weakened or reinterpreted.** No Scope-A
   machinery; no fork-(β)-declined entry; none of the Scope-B-undefined objects; no use of V1
   as a premise; no per-region extension of K11; no unprinted shape; no numerics beyond exact
   rational evaluation of the frozen inequalities — which **is** the certificate; no new
   formal (Lean) infrastructure.

### Residual debts — carried, not resolved

- **R-1.** Chen–Fang–Zhang endpoint-admissibility footnote. The K9 limb of this ruling rides
  on it. **Direction-checked: a weaker K9 makes the YES side easier, never harder** — the
  residue cannot flip this ruling toward NO.
- **R-2.** P6's residual [V?]: the reading `δ_probe = ℓ/R`, unverified against the probe
  source.
- **R-3.** (P)'s Scope-B status unresolved — not load-bearing (K4′ not consumed, no class
  transfer performed).
- **R-4.** K8-on-multi-region-tuples unresolved — not relied on in either direction; the
  conservative check was run and passes.
- **R-5.** Single-time coexistence / one-pressure debt (see §7.2).
- **R-6.** Prop 6.1 nondegeneracy residue — not consumed (no zoom taken).

### Out-of-vocabulary faces — recorded, never adjudicated

- **OOV-1.** `W★`'s region S sits exactly on `v = 3γ_j` (`L³` mass `Θ(1)`), i.e. on A3's
  marginal face in its own variables. S is never asked to carry `L³`, so no adjudication
  arises; the face is **touched and recorded, not decided**.
- **OOV-2.** Members whose `r_sat` carries no power-law exponent (e.g. `τ^α|log τ|^{−1}`,
  `τ^γ|log τ|`) — they sit exactly on the limb's two boundaries, which is where a would-be
  pin would have to be fought.
- **OOV-3.** *A log face found this pass:* a `Γ ≡ Γ₀` plateau extended over a **polynomial**
  range of radii with fixed axial extent carries swirl energy `≍ Γ₀²·L·log(1/τ)` — a
  logarithm the power-law vocabulary cannot express. `W★` avoids it by construction (its
  outer branch decays like `1/r`). Recorded, not adjudicated, not load-bearing here.
- **OOV-4.** The gap between **bare** exponent equality `β_v = γ` and B13's **τ-uniform**
  corner attainment — a sub-polynomial face the rows cannot separate, which is exactly what
  B13 was written to keep distinct. Also sub-polynomially degenerating corner constants
  `c′(τ) → 0`. Both are where the queued Seregin arXiv:2606.29468 log-corrected families
  would land.
- **OOV-5.** Circulation-evanescent members — excluded by the class's non-evanescence
  hypothesis, hence not adjudicated.

### Disagreements resolved during the pass

- **D-1 (witness breaker vs builders 2/3).** The breaker ruled two witness families "fatally
  defective" because two labelled regions tie at `γ_j = γ` with different gradient scales,
  forcing a relabelling `α := β_v`. Checked at source, that reasoning is **over-stated**: the
  corpus's own Scope-A B2 has exactly that configuration (the forced tongue at `ρ_T ≥ γ > α`
  with `σ_tip = γ` and full amplitude, nested inside the core) and the corpus explicitly
  **keeps** `α` as the core scale. **Resolution:** the breaker's *selection* is nonetheless
  correct for a sharper reason, substituted here — those tuples are **relabellable onto the
  endpoint** (their sub-core is an on-axis blob carrying the full amplitude *and* a diverging
  `L³`, with `(γ, β_v) ∈ S_blob` satisfying K11 in every printed instance), so they do not
  **discriminate** `M` from `{β_v = α}`. `W★` makes the sub-core amplitude-subdominant
  (`γ_2 = β_v < γ`) and `L³`-non-carrying, so **no relabelling exists**. Verdict: those
  families are *non-discriminating*, not row-violating.
- **D-2 (breaker's repair, declined in one respect).** Its repaired representative used an
  **oblate** on-axis pancake (`v = 2ρ + λ`, `λ > ρ`), a shape printed nowhere in the corpus.
  `W★` uses only the printed blob shape, so the certificate consumes no unprinted dictionary
  entry.

---

## 8. Bottom line

The middle limb of A2's trichotomy — the anchorless intermediate-saturation channel — is
**not excluded by the frozen map**, and cannot be, because the frozen rows never locate
Γ-saturation. Closing it requires **one new theorem, (Γ-DEP)**, or a change of class to
Scope A. **(SB-ANCH) cannot do it: it is logically the other endpoint.**

Frontier status after this pass (unchanged pending freeze review): **BH YELLOW-RED · B2
UNKILLED in Scope B · (T-c) OPEN · no CAP trigger · no Clay claim.**

---

## Erratum (2026-09-01, synthesis audit — appended, not silently repaired; the `YES (CONSISTENT)` ruling, the witness `W★`, and the sufficiency of (Γ-DEP) are all unaffected)

**E1 (§5 "Sufficient, and minimal" / "a pin requires exactly a new upper bound on `Γ`
inside the core" / "There is no third route"; §8 "(SB-ANCH) cannot do it").** The
**sufficiency** of (Γ-DEP) stands as proved. The **necessity/exclusivity** claims
overstate what this pass established: an outright **proof of (SB-ANCH)** for the
class — a τ-uniform constant-factor lower bound on `Γ` at the corner radius
`Γ₀/‖u‖_∞` — would equally exclude the middle limb, since
`(SB-ANCH) ⟺ {β_v = γ, τ-uniform}` (B6+B13, re-derived in this document's own P4(i):
`M ⟹ ¬(SB-ANCH)`), and `β_v = γ` lies in the endpoint set; in that scenario (Γ-DEP)
is false ((Γ-DEP) forces `β_v ≤ α < γ`), so (Γ-DEP) is sufficient but **not
necessary**. §8's dismissal ("logically the other endpoint") bars (SB-ANCH) only as a
**premise** in a conditional pin derivation (circularity); it does not bar proving it
outright — a route this record itself keeps open (P1's "(ii) (SB-ANCH)"; §7.4). A
per-member dichotomy theorem (`(Γ-DEP) ∨ (SB-ANCH)` memberwise) would be a further
admissible closure shape. **Replacement statement:**

> (Γ-DEP) is the minimal new object that closes the middle limb **from below**
> (`β_v ≤ α`); the only other closure shape is the second horn itself — a proof of
> (SB-ANCH), i.e. a τ-uniform constant-factor lower bound on `Γ` at the corner —
> which is the standing open gap and cannot be consumed as a premise without
> circularity; a per-member dichotomy `(Γ-DEP) ∨ (SB-ANCH)` is a third admissible
> shape. No closure shape avoids new mathematics; none is derivable from the frozen
> rows (both (Γ-DEP) and (SB-ANCH) fail on the bookkeeping witness `W★`).

"The single named object", "minimal" (in the unqualified sense), and "There is no
third route" are withdrawn as universal claims; §8's "(SB-ANCH) cannot do it" is to
be read "(SB-ANCH) cannot be consumed as a premise; proved outright, it closes the
limb from the other side".

**E2 (§5 (Γ-DEP) "In words" gloss).** The gloss understates the displayed formula:
since `γ > α`, for every fixed `δ > 0` the ball `dist ≤ δτ^α` **contains** the
envelope corner `τ^γ` near `T*` (`τ^γ/(δτ^α) = δ^{−1}τ^{γ−α} → 0`), so the formula
forbids `c′`-level saturation at the corner and below it as well — pinning to the
**first horn only** (`β_v ≤ α`), exactly as the derivation two lines later uses
("`r_sat ≥ δτ^α` … hence `β_v ≤ α` — the pin's first horn"). The printed words
describe a strictly weaker statement (which would pin only to the union of both
endpoints). Corrected gloss:

> In words: within any fixed fraction of the core scale `τ^α` — a region that
> includes the envelope corner `τ^γ` — `Γ` stays a fixed factor below `Γ₀`; in
> particular it cannot saturate at any radius `≲ τ^α`, forcing `β_v ≤ α` (the pin's
> first horn).

The sufficiency claim is unaffected (the first horn is a subset of the pin's
endpoint set).

**E3 (§5 candidate table, row 3 — provenance).** `θ_coh` is **not** among fork (β)'s
declined objects: the frozen declination (FREEZE_REVIEW round 1 §1; kill-table
frontier blocks, both rounds) covers exactly three — the neck poloidal level bound,
`sup(ω_θ/r)`, and `ℓ_neck`. `θ_coh` is one of (NECK)'s two named unassigned
dictionary-extension inputs (A16) and is Scope-B-undefined per B9. Row split,
corrected:

> | neck poloidal level bound, `sup(ω_θ/r)`, `ℓ_neck` | **declined by fork (β)** |
> | `θ_coh` | **standing unassigned dictionary-extension input (A16); undefined, not open, in Scope B (B9)** |

The row's operative conclusion — unavailable at frozen scope — is unchanged (it
holds via B9, not via the fork-(β) citation).

**E4 (cross-reference — §4 horn 2, §5 candidate-table row 1, §7.3: "(T3) empty in
Scope A by the amplitude corollary").** Superseded by the 2026-09-01 erratum to
`BH_RB2_ANCHOR_AUDIT_2026-08-21.md` (E2, queued F38): the emptiness is established
only on the `ρ_T = γ` sub-branch; §4 horn 2's "why the pin is trivially true there"
and §7.3's "remains empty in Scope A" are to be read with that restriction (on
`ρ_T > γ` the corollary supplies (H1), never (H2), and the pin is not established
even in Scope A absent a (Γ-DEP)-type theorem). The Scope-B `YES (CONSISTENT)`
ruling is unaffected.
