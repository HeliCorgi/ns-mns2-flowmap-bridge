# Stage-9 decision-theorem selection — 2026-08-23

**Record-only.** This document *selects and specifies* the next research task. It proves
nothing, discharges no debt, and applies no edit to the frozen map. Any map change arising
from executing the selected theorem must be drafted as a **proposal for the next
user-adjudicated freeze review**, never applied unilaterally.

Trigger: the Stage-9 readiness audit returned `PASS`
(`docs/formal/STAGE9_READINESS_AUDIT_2026-08-23.md`), so formal plumbing stops and the next
item must be Stage-9 mathematics.

**Commissioning authority — read this carefully.** `FREEZE_REVIEW_2_2026-08-21.md` §6
reserves the next branch to the **user's choice, as before**, with *nothing commissioned*,
and prints this limb as "doubly relevant as (SB-ANCH)'s home … theorem-shaped and **needs
explicit commissioning**". That is a requirement addressed to the user, **not** a
delegation to a selecting agent, and this document does not treat it as one. The authority
exercised here is the **user's dated instruction of 2026-08-23** (the Stage-9 readiness
pass specification), which directs: *"Select exactly one decision theorem … The next
research task must be a falsifiable quantitative theorem whose YES/NO outcome materially
affects the blow-up/global-regularity route"*, and *"Run failcase audit before proof
search"*. This document executes that instruction; the freeze-review slot is **where the
choice lands**, not what authorizes it.

If the user did not intend that instruction as the explicit commissioning of this limb,
treat everything below as a **proposal** and do not begin proof search until they say so.

Method: three independent analysts (frozen ledger / lab registry / literature watch), one
selector, two independent failcase auditors (checklist lens and adversarial lens), one
completeness critic. Verdict of the critic: **SELECT-AMENDED** (three repairs applied
below; no reselection ground found).

---

## 1. Lane re-audit — is the tracked lane still the best?

All three analysts return **BEST**, on argued grounds rather than inertia.

- **Ledger.** The lane is a theorem-forced funnel, not a preference: K2 (verified) makes
  Type II mandatory for axisymmetric finite-energy blow-up, and K11 plus the frozen wedge
  push every interior survivor into asymptotically inviscid quasi-static steady-Euler (BH)
  cores. Two years of adversarial kills have compressed the landscape to a two-item
  frontier — Scope A: B2's Γ-saturated realization under R-B2′ [C] with a fully enumerated
  conditional stack; Scope B: **B2 UNKILLED** with exactly one named gap, (SB-ANCH) ⟺
  τ-uniform `β_v = γ` corner attainment. No competing lane in the repository has a frontier
  this sharp.
- **Registry** (`ns-singularity-certificate-lab`). There *is* a competing lane — the
  Monster circulation-gate / conveyor chain (MONSTER-1 killed as written; the MONSTER-2.x
  chain patched to 2.7.3 with V2/V3 execution-stack kills; V3.2 sealed, the pre-registered
  short sign attack returning `NO_SIGN_REVERSAL_SIGNAL` over ~1.5 % of its own macro-cycle
  clock; the 2026-08-10 viability audit ruling **no ARCH-KILL / no PDE-KILL** but
  explicitly "not killed is not established"). Its own viability audit lands it at
  `γ = 5/9` or `2/3` — **inside the frozen Type-II window** — and its decisive literature
  threat is the same Seregin family that pressures the window's `γ + α = 1` edge. So the
  two lanes have converged on one corridor: the Type-II window is the adjudicating frame
  and the Monster lane is a candidate mechanism inside it, not a replacement. No registry
  commit after 2026-08-19 changes the window, K11, or the Seregin edge.
- **Literature (June–August 2026).** The material event is **Seregin, arXiv:2606.29468**
  (28 Jun 2026), "On potential Type II blowups for the Navier–Stokes equations": it
  generalizes the frozen power-law edge to log-corrected scaling families
  `f(λ) = λ^{α−1}/ln^γ(e/λ)` and again reduces exclusion to **Liouville-type theorems for
  ancient Euler solutions in explicit scaled-energy classes — left OPEN**. That is the
  lane's own central reduction, restated more generally by its originator. Also logged, not
  lane-changing: Ionescu–Jia–Palasek arXiv:2606.07501 (numerical unstable self-similar
  axisymmetric swirl-free non-uniqueness profiles — wrong axis, self-similar not
  bounded-ancient) and Peralta-Salas–Slobodeanu arXiv:2606.13462 (analytic *localizable*
  steady 3D Euler ⟹ symmetry — **assumes** localizability, so **trigger (T-c) stays OPEN,
  B5 does not fire**). Explicit null on a `C¹` non-localizable witness and on any discharge
  of (OO) or the KNSS / CSTY / Lei–Zhang / Chen–Fang–Zhang rows.

**Reconciliation with the standing 2026-08-19 decision.** Its reopen clause ("once the
continuation criterion is closed on the Lean side, the BH branch reopens") has fired — the
continuation criterion is Lean-closed and Stage-9 readiness passed — but its *payload
pointer is stale and was consumed*: the quantitative no-swirl rigidity question was retired
as ill-posed (K12 audit) → replaced by (★) → answered `inf s = 0` and decoupled (P0 probe)
→ replaced by (★_geo) → **closed affirmatively** by the geometry gate (Outcome A, θ = 1
sharp), and the reopen pass itself is on record as executed
(`BH_QUANTITATIVE_RIGIDITY_K12_AUDIT.md`). The successor of that payload on the current
frontier is the (SB-ANCH) / `β_v` complex — which is what is selected.

---

## 2. The selected decision theorem (amended statement, operative)

> Fix the frozen Type-II power-law vocabulary (`TYPE2_KILL_TABLE_2026-08-19.md` +
> annotations A1–A20, B1–B14). Let `u` be any axisymmetric finite-energy suitable weak
> solution of standard-`ν` incompressible Navier–Stokes on `R³` with first singular time
> `T* < ∞` and Type-II rate (`√τ·‖u(t)‖_∞ → ∞`, `τ := T* − t`), whose asymptotics fit the
> frozen exponents `‖u(t)‖_∞ ≍ τ^{−γ}`, core scale `≍ τ^{α}`, with
> `(γ, α) ∈ S_blob = {1/2 < γ < 1, max(1−γ, 2γ/3) ≤ α < γ, α > 2γ−1}` (K11 cut included;
> A7 strictness), whose core is an on-axis blob carrying the `L³` divergence (class **B2**)
> with `O(1)` swirl circulation `Γ₀ > 0` (`Γ := r·u_θ`; `‖Γ(t)‖_∞ ≤ Γ₀` by Γ-max;
> **non-evanescent**: `liminf_{t→T*} ‖Γ(t)‖_∞ ≥ c₀Γ₀` for some fixed `c₀ > 0` — the
> circulation-evaporation face, on which `r_sat(t;c′) = ∞` for every fixed `c′` eventually,
> is outside the decided class and if encountered is recorded alongside the
> out-of-vocabulary boundary), and with **no Scope-A hypothesis** (no `p = p(ψ)`
> overdetermination, no localizability, no quasi-static steady-Euler core structure).
>
> For fixed `c′ ∈ (0,1)` let
> `r_sat(t;c′) := inf{ r : sup_{axis-distance ≤ r} |Γ(·,t)| ≥ c′Γ₀ }`; the scope-free
> envelope `Γ(r) ≤ min(Γ₀, r‖u‖_∞)` forces `r_sat ≥ c′Γ₀/‖u‖_∞`, and `β_v ∈ (0,γ]` is the
> B13 saturation-scale exponent `r_sat ≍ τ^{β_v}`, where "`β_v = γ`" means **τ-uniform
> constant-attainment at the envelope corner** `r = Γ₀/‖u‖_∞` (B13: *not* bare exponent
> equality).
>
> **DECISION.** Is the middle limb
> `M := B2 ∩ {sub-core Γ-saturation, corner attainment failing}` — operative definition by
> quantifiers: *there exists a fixed `c′ ∈ (0,1)` with `r_sat(t;c′) = o(τ^α)`, while
> `r_sat(t;c′)·‖u(t)‖_∞/Γ₀ → ∞` as `t → T*` for every fixed `c′ ∈ (0,1)`*; in the power-law
> vocabulary this is exactly `β_v ∈ (α, γ)`, and members whose `r_sat` carries no power-law
> exponent (e.g. sub-polynomially degenerating corner constants at bare exponent `γ`) fall
> under the out-of-vocabulary recording clause below, not under a separately named limb —
> **CONSISTENT** with the conjunction of the frozen rows (scope-free in B1's sense: theorem
> / arithmetic content scope-free, applicability riders as printed here) —
>
> - Γ-max;
> - K3's every-`ε` violation placement;
> - K6 with [D2] as corrected in A3 (≥ 2 regions forced under a power-law `L³` divergence,
>   sup-location premise honored);
> - K9's `L^∞`-endpoint (Chen–Fang–Zhang) arithmetic under the A1 `σ_core`/`σ_sup` split
>   **applied at the correct radius** (the anchor audit's recorded `τ^{α−γ}` misfire mode is
>   a mandatory check);
> - K11 (`γ + α ≥ 1`);
> - **K4‴ [D, unconditional]** (A11: `Γ` exactly scale-invariant under the Prop-6.1
>   rescaling; every amplitude-normalized ancient limit inherits `|v_θ| ≤ Γ₀/r`);
> - **K4′ [C on (E⁺)+(P)]** (A9: axisym + amplitude-normalized ancient limit decays like
>   `1/r` ⟹ regular), carried with the record's own execution rule
>   (`BH_M3_KNSS_GATE_2026-08-20.md` §6: (E)/(P) must be printed with any use of K4′) and
>   B1's rider that **(P)'s Scope-B status is unresolved** — *no NO-side pinning chain may
>   consume K4′'s conclusion without printing [(E⁺)+(P)] in its certificate, and any such
>   chain is conditional [C], not a scope-free pin*
>
> — or does scope-free exponent arithmetic **PIN** `β_v` to the endpoint set
> `{β_v ≤ α} ∪ {β_v = γ, τ-uniform}`?
>
> **YES (consistent)** requires an explicit exponent/region assignment in the frozen
> vocabulary realizing `M`, verified row-by-row against every frozen row above.
> **NO (pinned)** requires a derivation from the frozen rows alone that every Scope-B B2
> solution satisfies `β_v ≤ α` or attains the corner τ-uniformly.
> Marginal / log-divergence faces the power-law vocabulary cannot express (A3) are recorded
> as **out-of-vocabulary boundary**, not adjudicated with invented entries.

### Kill / survive criterion

The mechanism at stake is the **anchorless intermediate-saturation escape channel** — the
only unnamed way a Scope-B B2 core can evade (SB-ANCH).

- **NO (pinned) KILLS it.** A2's trichotomy collapses to its endpoints and the sole
  unkilled class of the whole map splits into exactly two named, attackable structures:
  (i) `β_v = γ` τ-uniform corner attainment — (SB-ANCH)'s attained side, where R-B2′'s
  constant-agnostic scope-free machinery already reaches (any τ-uniform `c` substitutes
  verbatim for `1/√42`), modulo only the labelled-region / exhaustiveness gap (B6 rider);
  (ii) `β_v ≤ α` — sup-swirl unsaturated, or saturation exiled to a separate region, each
  exposed to the K9/K6 arithmetic.
- **YES (consistent) SURVIVES.** A certified, never-enumerated Scope-B survival class — the
  first genuinely new surviving structure since the corridor — enters the map as the named
  target for both the kill program and any later-commissioned negation-witness program, and
  (SB-ANCH) is shown evadable in one specific mode.

Both certificates are finite and checkable; neither outcome is vacuous; both rewrite the
frozen frontier.

### Why it matters

In Scope A the limb is already pinned to `β_v = γ` by the amplitude corollary (B2 (T3)), so
every bit of output is net-new Scope-B content. The decision determines **how (SB-ANCH) can
fail**, which is prerequisite-quality information for any attack on it, and it is the
cheapest live decision object on the ledger: one bounded pass over frozen rows, no new
mathematics imported, no numerics, no literature dependency.

---

## 3. Failcase audit (run before any proof search)

Two independent auditors ran the project battery. Checklist lens: **SURVIVES** (11/11
PASS). Adversarial lens: **AMEND** (14 PASS, 1 FAIL on statement wording fidelity). Critic
adjudicated **for the adversarial lens** on first-hand reading of the frozen rows.

| Check | Result | Note |
|---|---|---|
| dimensional-lift mismatch | PASS | actual axisymmetric NS on `R³`, not a reduced/synthetic model |
| physical 3D divergence structure | PASS | every consumed row is a theorem for divergence-free axisymmetric 3D NS; recon §4 classifies them scope-free |
| reconstruction correctness | N/A | no decode/reconstruction step; arithmetic over frozen rows |
| sparse-index multiplicity | PASS | both recorded multiplicity traps (sup-location premise; `τ^{α−γ}` radius misfire) are **mandatory inputs** of the statement |
| approximation-to-blowup transfer | PASS | no approximate object transferred; statement is conditional on the class and asserts no existence |
| numerical-evidence-to-theorem leap | PASS | zero numerics by construction; both certificates are vocabulary-level |
| finite-energy compatibility | PASS | finite-energy suitable weak solutions; `S_blob` already encodes the K5 energy cuts; K2 forces Type II for the class |
| known self-similar / nonexistence obstructions | PASS | no verified row pre-adjudicates `M`; triple-anchored as open (A2 "unanalysed", FREEZE_REVIEW_2 B1 "unresolved", anchor audit §4 (T3) "live and never claimed in Scope B") |
| viscosity / scaling quantifiers | PASS | standard-`ν` fixed; frozen window quoted with the K11 cut and A7 strictness; `Γ` exactly scale-invariant (K4‴) |
| well-posedness on the frozen dictionary | PASS | only frozen legend entries; the fork-β-declined entries (`θ_coh`, `ℓ_neck`, `sup(ω_θ/r)`, neck poloidal level bound) are **not** used |
| YES/NO falsifiability, both informative | PASS | complementary finite certificates over the power-law vocabulary |
| already answered / vacuous | PASS | open on three independent records |
| freeze / CAP / commissioning compliance | PASS | record-only; no profile discovery, no construction; CAP and (T-c) untouched |
| strict domination by a cheaper runner-up | PASS | verified against the record (see §4) |
| **statement wording fidelity** | **FAIL → repaired** | K4′ was mis-glossed as a Γ-transport fact and its `[C on (E⁺)+(P)]` tags dropped; **substance unaffected**, wording amended above |

Amendments applied to the statement: **[E1]** mandatory K4′/K4‴ printing repair with the
`(E⁺)+(P)` execution rule and B1's unresolved-(P)-in-Scope-B rider; **[E2]** operative
quantifier definition of `M`, with the "degenerate face" struck as a separately named limb
(its polynomial members *are* the `β_v ∈ (α,γ)` case; its sub-polynomial members fall under
the A3 out-of-vocabulary clause); **[E3]** circulation non-evanescence gloss, closing the
only partition edge (`r_sat` is an infimum over a possibly empty set).

**The candidate did not die.** It survives the battery in amended form.

---

## 4. Why not the runners-up

| Rejected | Reason |
|---|---|
| (SB-ANCH) in full | its YES side needs a genuinely new co-location mechanism with no recorded lead ("co-location is the entire gap", recon §4); its NO side *is* this `β_v` pass — the bounded gate buys the decisive content cheaper and makes the later attack well-posed |
| eikonal / localizability necessity | research-level open problem; the forcing direction is **empty in 3D** (all three subject papers assume localizability); unbounded cost; CAP-adjacent on its YES side; B5's default posture is literature watch |
| quantitative no-swirl rigidity rate | **superseded and closed** (ill-posed → (★) → (★_geo) → geometry gate Outcome A, θ = 1 sharp); selecting it re-litigates a closed theorem |
| K12 / K12′ / K12″ | KEEP CONDITIONAL, Scope-A-only half-wedge, partially redundant with R-B2′, zero payoff on the live Scope-B gap; ζ/K12″ is on the deliberately-deferred list |
| (COH-Δ) / (ANCH-κ) via a new vehicle | blocked — all three in-house vehicles retired or declined by fork-β; six failed passes; the residue is a dictionary-extension request pending external input, not a selectable theorem |
| D1 / PLSMC `Ξ₀ ≥ 15` test (registry) | experiment-shaped, not theorem-shaped; barred by the standing no-numerics prohibition absent its own commissioning; convention ambiguity exceeds the level margin by the proposal's own record; prior data adverse |
| Seregin `m`-exponent check (registry) | a literature-verification read, not a theorem — and now stale, since arXiv:2606.29468 supersedes the power-law edge with log-corrected families |
| Seregin-class ancient-Euler Liouville (literature) | maximally decisive but frontier-PDE left open by its own author, with no recorded attack on the scaled-energy class; expensive-decisive loses to cheap-decisive — **the natural successor decision after this one** |
| (OO) `p = ∞` Liouville | unchanged open research problem; explicit June–August null on new purchase |
| IJP ASSF certification | wrong axis (non-uniqueness, not blow-up vs regularity); self-similar NS blow-up already excluded (NRS/Tsai); near-certain duplication |

---

## 5. Standing obligations inherited by the commissioned task

1. Print `[(E⁺)+(P)]` in the certificate of any chain consuming K4′; such a chain is `[C]`,
   never a scope-free pin (`BH_M3_KNSS_GATE_2026-08-20.md` §6 + B1).
2. Carry the **P6 residual [V?]** and the **Chen–Fang–Zhang endpoint-admissibility
   footnote** as stated verification obligations (kill-table §4 residuals) — do not resolve
   them computationally.
3. Perform the **`τ^{α−γ}` misfire check** on every K9 application
   (`BH_RB2_ANCHOR_AUDIT_2026-08-21.md` §8).
4. Record every marginal / log / sub-polynomial / circulation-evanescent face as
   **out-of-vocabulary boundary** (A3), never adjudicated with invented dictionary entries.
5. **Record-only discipline**: any discharge of debt A2, or any new survival row, is drafted
   as a proposal for the next user-adjudicated freeze review; nothing is applied to the
   frozen map in this lane without that adjudication.
6. **Queued independently (not a blocker for this task, must not be silently dropped):** the
   mandatory row-(i) update for **Seregin arXiv:2606.29468** (log-corrected Type-II
   families; the reduction to open ancient-Euler Liouville theorems) at the next freeze
   review.

---

## 6. What this document does *not* do

- It proves no theorem and settles no `YES`/`NO`.
- It changes no frozen verdict: **BH stays YELLOW-RED**, B2 stays **UNKILLED in Scope B**,
  trigger (T-c) stays **OPEN**, no retired row is re-armed, no CAP trigger fires.
- It authorizes no numerics, no new ansatz, no profile discovery, and no in-house Liouville
  manufacturing.
- It makes no Clay claim of any kind.
