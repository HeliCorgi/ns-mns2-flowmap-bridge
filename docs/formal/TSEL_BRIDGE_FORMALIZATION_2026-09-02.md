# TSEL_BRIDGE_FORMALIZATION — 2026-09-02 — Lean formalization of the T-SEL ten-lemma bridge (SEL-1…SEL-10); head N0 untouched by commission

**Commission (user, 2026-09-02, second session):** resume at the Stage-9 Reverse-Gap
Audit's SS-5/SS-6 anchor and *formalize SEL-1…SEL-10 in Lean*; **do not start proof
search on the T-SEL head itself.** This record documents exactly that execution. The
head `N0` remains OPEN, unclaimed, and untouched; it enters the formal layer only as a
named hypothesis. Nothing in this pass changes any frozen verdict, the round-4 park, the
literature watches, or the on-hold status of milestone M-1.

Base revision before this pass: `a359354` (local `main` = `origin/main`, clean tree).

---

## 1. What was commissioned vs. what was built

The audit record (`docs/gates/STAGE9_REVERSE_GAP_AUDIT_2026-09-02.md`, SS-6) fixed ten
on-paper lemmas: four resting on existing Lean anchors, six standard-math-to-formalize.
"Formalize" is executed here in the repository's own discipline (no `sorry`, no
`axiom`, assumptions explicit in theorem statements):

- every SEL lemma now has a **Lean artifact** — either a proved theorem, or a
  `Prop`-valued **statement definition** consumed as an explicit hypothesis;
- everything provable at bounded cost **was proved** (SEL-2 fully quantitative, SEL-6
  as new standalone infrastructure, SEL-7's consumed bookkeeping, SEL-8, SEL-9
  conditional on SEL-5, SEL-10, and the composed conditional chain `N0 → N1 → N2 → N3`);
- the genuinely heavy analysis (Kato–Ponce, parabolic smoothing, the `H³` ladder, the
  classical-norm comparability) is **stated, not proved, and not assumed** — each is a
  named open `Prop` that future work discharges one at a time.

No axiom is introduced anywhere: a conditional theorem with hypothesis `H` asserts
`H → …`, which is a theorem of the standard foundations regardless of `H`'s status.

## 2. New files and the SEL ↔ artifact map

New Lean files (all under the pinned gate):

1. `Formal/GronwallIntegralInequality.lean` — Grönwall–Bellman integral inequality
   (closes bridge gap B1: the repository previously had no Grönwall infrastructure).
2. `Formal/R3TSelDecodedGradient.lean` — the decoded sup / gradient-sup functionals,
   the quantitative T-SEL embedding, and the `Q` functional.
3. `Formal/R3TSelBridge.lean` — the SEL statement layer and the conditional assembly.
4. `Formal/AxiomAudit.lean` — 21 new `#print axioms` entries (all standard).

| SEL | Status | Lean artifact |
|---|---|---|
| SEL-1 (norm transport) | consumed part EXISTING; initial-norm identity **proved**; classical `Σ‖D^α·‖²` comparability **OPEN (stated)** | anchors `besselPotential_r3HsToTempered_eq_coordinate`, `r3HsToTempered_memSobolev`, `r3H3ToL2Operator_r3SchwartzToHsCLM`; new `r3TSel_initial_carrierNorm`; open `R3TSelClassicalSobolevComparability` |
| SEL-2 (embedding `H³ ↪ C¹ ∩ W^{1,∞}`) | **PROVED, quantitative** | `r3TSel_decoded_embedding`: `r3DecodedSup f + r3DecodedGradSup f ≤ (‖J⁻³‖_{L²} + 2π‖innerSL ℝ‖‖ξ↦‖ξ‖(1+‖ξ‖²)^{-3/2}‖_{L²})·‖f‖`; ingredients `integral_weighted_norm_r3DecodedFrequency_le`, `norm_fderiv_r3DecodedRepresentative_le`, `hasFDerivAt_r3DecodedRepresentative` |
| SEL-3 (identification + smoothing) | identification EXISTING (capstone); smoothing **OPEN (stated)** | `r3EndpointSafeProjectedMild_navierStokes` (existing); open `R3TSelInteriorSobolevSmoothing` |
| SEL-4 (Kato–Ponce commutator) | **OPEN (stated)** | `R3TSelKatoPonceCommutator C`: Bessel-form `‖J³((φ·∇)φ) − (φ·∇)(J³φ)‖_{L²} ≤ C‖∇φ‖_{L∞}‖J³φ‖_{L²}` on the divergence-free Schwartz core |
| SEL-5 (H³ ladder) | **OPEN (stated, integrated form)** | `R3TSelH3Ladder C`: `‖u t‖² ≤ ‖u0‖² + ∫₀ᵗ 2C·gradSup·‖u s‖²` along certified solenoidal-datum solutions |
| SEL-6 (Grönwall) | **PROVED** | `le_mul_exp_of_le_add_intervalIntegral` (Bellman integral form; no differentiability of `y` consumed) |
| SEL-7 (endpoint bookkeeping) | consumed parts **PROVED**; `t₀ ↓ 0` limit folded into SEL-5's integrated form | `r3TSel_carrierNorm_continuousOn`, `r3TSel_gradIntegrand_intervalIntegrable`, `continuousOn_r3DecodedGradSup_comp`, `r3TSelGradIntegral_mono`, `r3TSelGradIntegral_nonneg` |
| SEL-8 (realness) | **PROVED (instantiation)** | `r3TSel_decodedReal_of_admissible` |
| SEL-9 (bridge assembly) | **PROVED conditional on SEL-5** | `r3TSel_carrierBound_of_ladder`: ladder ⟹ `‖u t‖ ≤ ‖u0‖·exp(C·Q(u,t))`, ν-free |
| SEL-10 (plug discharge) | **PROVED** | `r3TSel_uniform_bound_transfer` (uniqueness transfer); sSup/BddAbove discharge inside `r3TSel_horizons_unbounded` |

The N-chain of the audit's SS-5 dependency diagram is composed as:

- **N0 (OPEN, hypothesis-only):** `R3TSelGradientBound hnu u0` (per-datum) and
  `R3TSelHead` (∀ν, ∀ admissible Schwartz datum) — `∀T ∃G ∀T′ ≤ T`, every certified
  solution on `T′` has `r3TSelGradIntegral u T′ ≤ G`. **Never asserted; no proof
  search performed, per commission.**
- **N0 → N1:** `r3TSel_uniform_carrierBound_of_head` — ladder + head ⟹ per reference
  horizon a single nonnegative `R = ‖u0‖·exp(C·G)` bounding all certified solutions.
- **N1 → N2:** `r3TSel_horizons_unbounded` — via
  `r3EndpointSafeProjected_horizons_unbounded_of_uniform_bound` (existing), the
  certified horizon set is unbounded.
- **N2 → N3:** `r3TSel_admissibleSchwartz_globalContinuation` /
  `r3TSel_conditional_globalContinuation` — for admissible real divergence-free
  Schwartz data, arbitrarily long certified horizons carry mild solutions (the left
  branch of the certified blow-up dichotomy; the repo's formal proxy for global
  continuation).

## 3. Semantic decisions (audit-relevant, all recorded in source docstrings)

1. **The carrier of `‖∇U‖_{L∞}`.** `r3DecodedGradSup f := ⨆ x, ‖fderiv ℝ U_f x‖`,
   where `U_f = r3PhysicalRepresentative (r3DecodedFrequency 3 f)` is the repository's
   existing explicit inverse-Fourier decoded representative — everywhere `C¹`
   (`hasFDerivAt_r3PhysicalRepresentative` with both decoder integrabilities), and
   **a.e. equal to the decoded physical velocity** `r3H3ToL2Operator f` consumed by
   the Navier–Stokes capstone (`r3DecodedRepresentative_ae_r3H3ToL2Operator`, from the
   existing inversion-consistency layer). On the Schwartz core the functional is
   literally the field's own gradient-sup (`r3DecodedGradSup_schwartz`). What is *not*
   claimed: identification with an intrinsic distributional `W^{1,∞}` seminorm — not
   needed by the bridge.
2. **Integrated ladder.** `R3TSelH3Ladder` is SEL-5 *after* time integration on
   `[0,t]`, absorbing SEL-7's `t₀ ↓ 0` limit. Chosen so the assembly consumes only
   trajectory continuity (certified) — no differentiability of `t ↦ ‖u t‖` is ever
   hypothesized. The differential-form derivation (test `D^α`-equation, discard the
   viscous term by sign, kill transport by `div U = 0`, drop the projector) is the
   content of the future SEL-5 proof, alongside SEL-3 and SEL-4.
3. **SEL-4 in `J³` form.** Kato–Ponce (CPAM 41, 1988) is natively a `J^s` commutator
   estimate; the carrier is the Bessel model, so the statement uses
   `r3SchwartzToHsCLM 3` / `SchwartzMap.fourierMultiplierCLM` with the order-3 weight.
   The distance to the literature's `D^α` form is exactly the deferred SEL-1
   comparability (`R3TSelClassicalSobolevComparability`), which the assembly never
   consumes.
4. **Q is scale-honest.** `r3TSelGradIntegral` is defined along arbitrary trajectories;
   nonnegativity and horizon-monotonicity are proved for the certified class. SEL-2's
   quantitative bound witnesses the audit's non-banned check (finiteness per horizon;
   strictly lower-order than the carrier norm).

## 4. Verification evidence (per `docs/LEAN_CI_OPERATIONS.md`)

```text
runner: local Elan-pinned toolchain, bash scripts/lean-ci-local.sh (Git Bash, Windows)
revision: working tree over a359354 (committed immediately after this record;
  the verified tree is exactly the committed one)
toolchain: leanprover/lean4:v4.32.1
dependency manifest: pinned lake-manifest.json (mathlib v4.32.1 tag), unchanged
scope and results:
  - targeted: Formal.GronwallIntegralInequality  PASS (2663 jobs)
  - targeted: Formal.R3TSelDecodedGradient       PASS (8724 jobs)
  - targeted: Formal.R3TSelBridge                PASS (8749/8765 jobs)
  - full pinned gate (source scan + lake build)  PASS (8772 jobs)
result: pass; forbidden-source scan clean (no sorry/admit/axiom/opaque under Formal/)
axiom audit: all 21 new printed theorems depend only on
  [propext, Classical.choice, Quot.sound]
diagnostics: none outstanding (pre-existing style warnings in untouched files only)
```

No GitHub-hosted Action was started; integration is by direct fast-forward push to
`main` without a PR, per the standing CI cost policy.

## 5. Claim boundary

- **The head `N0` is OPEN.** `R3TSelGradientBound` / `R3TSelHead` are definitions.
  Nothing here proves, claims, or begins to prove them — the commission explicitly
  excluded head proof search, and none was performed. Per the audit: proving the head
  for admissible data is Clay-equivalent-or-harder; a certified family with `Q → ∞` on
  a bounded horizon is the falsification signature the singularity program must
  produce. **Both directions remain open.**
- The four open statement definitions (`R3TSelClassicalSobolevComparability`,
  `R3TSelInteriorSobolevSmoothing`, `R3TSelKatoPonceCommutator`, `R3TSelH3Ladder`) are
  never asserted. Conditional theorems consuming them prove implications only.
- No Clay statement, no global regularity, no blow-up, no classical solution is
  claimed. `N3` is the certified-class continuation proxy; classical global smoothness
  would additionally need maximal-trajectory gluing and the parabolic smoothness
  upgrade (outside scope guards, unchanged).
- C0 discipline: `Q` is *a* continuation-controlling quantity, not "the"; T-SEL stays
  a selection, not a uniqueness claim; frozen verdicts (`VIOLATED`, UNDERDETERMINED,
  B2-UNKILLED), the round-4 park, and all watch registers are untouched.
- The `RECORD-ONLY` status of the Stage-9 Reverse-Gap Audit itself is unchanged; this
  pass adds a formal layer commissioned separately and does not adopt any of EP-1…EP-8.

## 6. Remaining proof obligations of the T-SEL bridge (in dependency order)

1. **SEL-6′ (optional strengthening):** none — the Bellman form proved here is what the
   assembly needs.
2. **SEL-1 comparability** (`R3TSelClassicalSobolevComparability`) — bounded standard
   work (Fourier-side `Σ|ξ^α|²` vs `(1+‖ξ‖²)³` weight comparison on the Schwartz
   core); unlocks the literature-verbatim reading of SEL-4.
3. **SEL-4 Kato–Ponce** (`R3TSelKatoPonceCommutator`) — hard; no mathlib analogue.
   Realistic route: order-3 Leibniz + explicit frequency-side commutator majorants in
   the repository's own weighted-convolution style (the `R3H2*`/`R3H3*` weight-geometry
   files are the intended toolbox).
4. **SEL-3 smoothing** (`R3TSelInteriorSobolevSmoothing`) — hard; bootstrap on the
   existing `r3StokesH2ToH3Operator`-style smoothing plus Duhamel iteration.
5. **SEL-5 ladder** (`R3TSelH3Ladder`) — consumes 2–4; the final integration step then
   closes `N1` unconditionally in the ladder slot, leaving the head as T-SEL's single
   open input.
6. **The head `N0`** — awaits its own separate user commission in either direction
   (proof attempt or counterexample program); constrained by FC-086/Tao-averaged
   obstruction to consume exact NS structure.

Item ordering is a recommendation, not a schedule; each item is independently
falsifiable and independently commissionable.
