# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: 2026-09-02 JST (second session).

> **Where the project is (2026-08-23).** The formal side has finished preparation:
> **Stage-9 readiness = `PASS`** (`docs/formal/STAGE9_READINESS_AUDIT_2026-08-23.md`), so
> **formal plumbing is STOPPED** by rule. The first Stage-9 decision theorem was
> commissioned by the user and **has been executed and decided**:
> **`YES (CONSISTENT)` — scope-free exponent arithmetic does NOT pin `β_v`**
> (`docs/gates/BH_BETAV_ENDPOINT_PINNING_2026-08-23.md`). The remaining logical gap
> was there named **(Γ-DEP)** — re-scoped at round 3 (C0): **sufficient-only**,
> three recorded closure shapes. The research-side freeze (round 2, 2026-08-21)
> is **unchanged**: BH YELLOW-RED, B2 UNKILLED in Scope B, trigger (T-c) OPEN; all map
> consequences of the decision are **proposals** for the next freeze review, applied to
> nothing.
>
> **2026-09-01: a corpus-wide mathematical audit pass** (multi-agent, adversarially
> verified) found and recorded 15 defects (2 major) in the frozen research prose — none
> touching a ruling, a Lean theorem, or the frontier verdicts. Frozen gate documents
> carry appended errata; kill-table corrections were queued as F37–F43; live documents
> are repaired in place. See "2026-09-01 mathematical audit pass" below.
>
> **2026-09-01 (same day): FREEZE REVIEW ROUND 3 is EXECUTED** on the user's dated
> instruction (`docs/gates/FREEZE_REVIEW_3_2026-09-01.md`; kill-table annotations
> **C0–C14**). All of F37–F43 ADOPTED (F41 in option (a): `S_ring` gains K11);
> P1–P7 ADOPTED (P1/P2/P3 amended — P1 for the new standing policy
> **C0: (Γ-DEP) is a sufficient closer only** ("unique closer"/"no third route"
> retired from citation), P2/P3 for F38-consistency and C0); the Seregin arXiv:2606.29468 row-(i) update ADOPTED as
> pressure-only with a named [V?] full-text debt (C14). The **frontier is re-fixed
> uniquely** (post-round-3 block): Scope-A exhaustiveness holds only on `ρ_T = γ`;
> on `ρ_T > γ` (T3)-emptiness is NOT established even in Scope A; Scope B unchanged
> (B2 UNKILLED, (SB-ANCH) a genuine conjunction). The external ChatGPT-side record
> **(EXT-ΓDEP-1)** (`Γ-DEP = UNDERDETERMINED`; smooth divergence-free snapshot
> counterprofile; the (Γ-DEP)_fld re-fix; (Γ-OSC)) was supplied verbatim by the
> user the same day and is **IMPORTED with an in-repo audit — PASS at snapshot
> level** (`docs/gates/EXT_GAMMADEP_DECISION_2026-09-01.md`; debts D-1/D-2/D-3
> named, consumed by nothing). Headline no-go: **(Γ-DEP) is not derivable from
> single-time NS-compatible smooth geometry — any proof must consume the time
> evolution.** **Final next-decision verdict (round-3 §8): the Γ-OSC feasibility
> decision** (weakest drift condition for the τ-uniform contraction at `R = τ^α`;
> both directions vs frozen B2; `IMPLIED / VIOLATED / UNDERDETERMINED`) **is
> commissioning-ready** — commissioning is a user act. Registered termination
> rule: continue only on IMPLIED (or a partial IMPLIED naming the consumed NS
> structure); VIOLATED ⟹ end/pivot justified; a second consecutive
> UNDERDETERMINED ⟹ the BH branch ends.
>
> **2026-09-02: the Γ-OSC feasibility decision is EXECUTED and DECIDED —
> `VIOLATED`** (`docs/gates/GAMMA_OSC_FEASIBILITY_2026-09-02.md`): frozen B2
> implies **no** known-sufficient drift condition for the τ-uniform oscillation
> contraction (the implied sub-region of `S_blob` is **exactly empty**; sup /
> `L^∞_tL³` / local-energy caps are **forced-divergent** class-wide at
> `ν^{−1}τ^{−(γ−α)}`, the local-energy cap at the squared rate
> `ν^{−2}τ^{−2(γ−α)}`, by the forced-amplitude lemma), and an explicit
> frozen-compatible smooth divergence-free family defeats **every** minimal
> known-sufficient rung of both ladders τ-uniformly (power vs at most double-log
> caps; the known ladder provably terminates at scale invariance — SSŠZ/SVZ/Wu;
> multi-scale escape closed at the `(ln N)^{−p}, p ≤ 1` threshold). Debts D-1
> and D-2 DISCHARGED. C0-clean: `VIOLATED ⇏ ¬(Γ-OSC)` and `⇏ ¬(Γ-DEP)` — the
> named non-rung NS structures (§5.3 of the record) remain live for genuinely
> new mathematics. **The registered termination rule fires on its VIOLATED
> clause: the Γ-depletion lane's expected value collapses — END/PIVOT of the BH
> branch is JUSTIFIED. Execution of the end/pivot is a user act** (recorded
> options: the `SPEC.md` numerical candidate program; the literature-level
> Seregin watch; D-3 family watch continues regardless).
>
> **Same day: D-3 identified and triaged** — arXiv:2606.07869v1
> (axisymmetric-with-swirl global-regularity claim): first-hand read +
> adversarial adjudication CONFIRMED load-bearing gaps (variational core G1a/G1b;
> exhaustion layer G2); correctness NOT ESTABLISHED; consumed by nothing; **no
> CAP fire**. Companion identified as arXiv:2606.07875; author-cluster red flag
> (both-directions claims) recorded. `docs/gates/D3_TRIAGE_2606_07869_2026-09-02.md`.
>
> **2026-09-02 (same day): FREEZE REVIEW ROUND 4 is EXECUTED** on the user's
> dated instruction (`docs/gates/FREEZE_REVIEW_4_2026-09-02.md`; kill-table
> annotations **D0–D7** + Post-round-4 frontier). P1–P6 all ADOPTED (P6 as
> executed by the instruction itself); the Γ-OSC `VIOLATED` row is on the map at
> exact machinery-closure scope (D1, C0-clean). **The BH / Γ-depletion branch is
> TERMINATED AS THE ACTIVE LANE and PARKED (D0)** — operative distinction:
> **UNRESOLVED ≠ EXHAUSTED-MACHINERY** (B2 stays UNKILLED, the middle limb and
> (Γ-OSC)/(Γ-DEP) stay open; what is exhausted is the in-house known-mechanism
> inventory, in three adjudicated layers); BH verdict frozen YELLOW-RED at park;
> un-park triggers registered. D-3/Seregin **separated to the standing passive
> watch register** (`docs/gates/LITERATURE_WATCH_REGISTER_2026-09-02.md`, as
> W-1–W-3; W-4 = un-park-relevant theory, created alongside). **Active research lane switched to the `SPEC.md` verified nonlinear
> finite-cylinder numerical candidate program; first bounded milestone
> selected: M-1 = implement and verify the Hou 2022 no-slip wall-vorticity
> boundary closure** (clearing the recorded blocker of
> `docs/reports/HOU_WALL_VORTICITY_BOUNDARY_AUDIT_2026-08-13.md`; acceptance
> gates + fail-closed stencil rule in the round-4 record §5). M-1 is selected,
> not yet started.
>
> **2026-09-02 (later): M-1 is ON HOLD by user instruction** (numerical lane
> retained, not discarded, not started), and the **Stage-9 Reverse-Gap Audit is
> EXECUTED** as a one-shot sanctioned bounded analysis
> (`docs/gates/STAGE9_REVERSE_GAP_AUDIT_2026-09-02.md`, RECORD-ONLY — no frozen
> verdict, frontier, or park change). Results: the exact Lean continuation
> **plug spec** extracted from source (carrier norm = Bessel-H³ of the decoded
> field; the extension/dichotomy interface; the L_bridge template with absent
> bridge layers B1–B5); **19 reverse-gap candidates** adjudicated across three
> lanes (whole-space ladder / axisymmetric / K12 complex) with
> counterexample-first discipline — 18 SURVIVE, 1 BANNED (the carrier-norm
> restatement, pinned as degenerate endpoint); the **K12-complex re-verified**
> without assuming past records (two genuine printed-statement defects found:
> EP-1 KC-3b vacuous middle link, EP-3 KC-7 width-floor vacuity; plus EP-4/EP-6
> and carried items — all as record-only erratum PROPOSALS EP-1–EP-8 for a
> future freeze review). **THE SINGLE SELECTED THEOREM: T-SEL = L_a — the
> time-integrated velocity-gradient bound**
> `∫₀^{T′} ‖∇U(s)‖_{L∞} ds ≤ G(T; ν, ‖u₀‖)` over certified horizons — with the
> complete dependency chain N0→N1→N2→N3 (bridge = 1984-known mathematics:
> Kato–Ponce commutator + Grönwall, **ten on-paper lemmas SEL-1…SEL-10**, four
> resting on existing Lean anchors, six standard-math-to-formalize; the head N0
> is OPEN and Clay-equivalent-or-harder, unclaimed). Runner-up: L_b (BKM
> vorticity form). Formalization/proof exploration of T-SEL awaits a separate
> user commission — **the intended resume anchor for the next session is that
> record's SS-5/SS-6 plus this paragraph.**
>
> **2026-09-02 (second session): the T-SEL bridge formalization is COMMISSIONED
> and EXECUTED** (user instruction: formalize SEL-1…SEL-10 in Lean; do **not**
> start proof search on the head). Record:
> `docs/formal/TSEL_BRIDGE_FORMALIZATION_2026-09-02.md`. New Lean files
> `Formal/GronwallIntegralInequality.lean` (SEL-6 **proved** — Grönwall–Bellman
> integral form, new standalone infrastructure),
> `Formal/R3TSelDecodedGradient.lean` (SEL-2 **proved quantitatively** —
> `r3DecodedSup f + r3DecodedGradSup f ≤ C_emb·‖f‖` with explicit Cauchy–Schwarz
> constants; the `‖∇U‖_{L∞}` carrier `r3DecodedGradSup` is everywhere-defined,
> Schwartz-core-pinned, a.e.-identified with the decoded velocity, Lipschitz on
> the carrier; the `Q` functional `r3TSelGradIntegral` with monotonicity), and
> `Formal/R3TSelBridge.lean` (the SEL-1…SEL-10 statement layer + the **proved
> conditional assembly** `N0 → N1 → N2 → N3`:
> `r3TSel_carrierBound_of_ladder` (SEL-9),
> `r3TSel_uniform_carrierBound_of_head` (N1), `r3TSel_horizons_unbounded` (N2),
> `r3TSel_admissibleSchwartz_globalContinuation` /
> `r3TSel_conditional_globalContinuation` (N3), SEL-7/8/10 support theorems).
> **OPEN, stated-only, never asserted** (Prop definitions used as explicit
> hypotheses; no axioms): the head `N0` (`R3TSelGradientBound` / `R3TSelHead` —
> **no proof search performed, per commission**), SEL-4
> (`R3TSelKatoPonceCommutator`), SEL-5 (`R3TSelH3Ladder`), SEL-3 smoothing
> clause (`R3TSelInteriorSobolevSmoothing`), SEL-1 comparability clause
> (`R3TSelClassicalSobolevComparability`). Full pinned local gate PASS
> (8772 jobs), 21 new axiom-audit prints all standard. Frozen research map,
> round-4 park, watches, and the M-1 hold are all untouched. **The intended
> resume anchor for the next session is the "Next work" subsection of the
> handoff update contract below plus the formalization record's §6.**

This is the short-form continuation point for future GPT sessions. The repository is expected to be developed primarily through repeated GPT sessions; do not rely on chat history as durable state.

## Resume protocol

Follow `docs/GPT_WORKFLOW.md`. Read, in order:

1. `PROJECT_GOAL.md`;
2. `SPEC.md`;
3. `AGENTS.md`;
4. `FORMAL_SCOPE.md`;
5. this file;
6. `docs/LEAN_CI_OPERATIONS.md`;
7. current GitHub `main`, relevant `Formal/` files, open PRs, and latest Lean verification evidence.

Current code and theorem statements override stale prose.

## Handoff update contract (standing specification)

**Specification (user directive, 2026-09-02): every session that does substantive work
MUST, before ending, write into this file what the next work is, in a form a fresh
session can execute without this session's chat history.** Concretely, at end of
session:

1. update the dated block at the top of this file with what was executed, what was
   verified (exact gate evidence: runner, toolchain, scope, job count), and what was
   deliberately **not** done;
2. rewrite the **"Next work"** subsection below — it must name: the next task(s) in
   recommended order, the exact files/records a fresh session must read first, any
   commission boundary (what requires a new explicit user instruction vs. what is
   already sanctioned), and any tempting-but-forbidden shortcut;
3. keep `STATUS.md` and `FORMAL_SCOPE.md` synchronized when the formal frontier moved
   (per `AGENTS.md`);
4. never leave the next-work description only in a commit message, chat reply, or
   ephemeral plan — this file is the durable continuation point.

### Next work (written 2026-09-02, second session)

Read first: this file's top block; `docs/formal/TSEL_BRIDGE_FORMALIZATION_2026-09-02.md`
(esp. §6); `docs/gates/STAGE9_REVERSE_GAP_AUDIT_2026-09-02.md` SS-5/SS-6;
`FORMAL_SCOPE.md` (T-SEL subsection); `Formal/R3TSelBridge.lean` docstring.

- **Already sanctioned lane (T-SEL bridge discharge, needs no new commission):** prove
  the open bridge statements in the recommended order of the formalization record §6 —
  (a) `R3TSelClassicalSobolevComparability` (SEL-1 clause; bounded Fourier-side weight
  comparison on the Schwartz core — the natural first target for the next session),
  then (b) `R3TSelKatoPonceCommutator` (SEL-4; hard, no mathlib analogue; intended
  toolbox = the repository's `R3H2*`/`R3H3*` weighted-convolution files), then
  (c) `R3TSelInteriorSobolevSmoothing` (SEL-3 clause), then (d) `R3TSelH3Ladder`
  (SEL-5; consumes a–c and closes the ladder slot of the conditional chain). Each is
  independently commissionable and independently falsifiable; do them as separate
  verified commits.
- **Requires a separate explicit user commission:** any proof search on the head `N0`
  (`R3TSelGradientBound` / `R3TSelHead`), in either direction (proof attempt or the
  counterexample program `Q → ∞` on a bounded horizon). The 2026-09-02 commission
  explicitly excluded it; do not start it implicitly.
- **On hold (user instruction, unchanged):** numerical milestone M-1 (Hou 2022
  no-slip wall-vorticity closure) — retained, not discarded, not started.
- **Forbidden shortcuts:** do not assert any open `R3TSel*` Prop as an axiom or
  instance; do not cite the `r3TSel_*` conditional theorems without their hypotheses;
  do not use the phantom carrier alias as a Sobolev embedding (use the decoded
  representative machinery); do not re-enable hosted CI (local Elan-pinned gate only,
  direct fast-forward push to `main`, no PR).

## Repository / verification state

- PR #77 (`Cut hosted Lean CI usage and add cache`) is merged.
- PR #78 (`Gpt handoff protocol`) is merged.
- PR #79 (`R3 young real set integral bridge`) is merged.
- PR #80 (`Close R3 Schwartz H3-to-H2 convection factors`) is merged.
- PR #81 (`Agent/chatgpt external lean workflow`) is merged as
  `710709c34b8ee564b071e71fd27313be4cc383a6`.
- PR #81 head `18c64b80b6eebb95a4344dec5811fc024b963377` passed hosted Lean run #257
  (`31924077773`). Its Git tree is identical to merge commit `710709c...`; the merge SHA itself has
  no separately attached run.
- Before this continuation, local and GitHub `main` were
  `f6bb133cf10f5a9b96594f10c742a1aa5c6cfe68`, with no open PRs.
- Proof commit `6ecfcda51d74b456b538def2577c52a403a0ff88` passed targeted builds of
  `Formal.R3SchwartzConvectionSobolevEstimate` and `Formal.AxiomAudit`.
- Commit `213495284f14c08d60936fa12a5260688124aa3f`, which adds only synchronized documentation on
  top of that proof, passed the local pinned source scan and full `Formal.+` gate (8735 jobs).
- Proof commit `5eb29848eea0529bf557c68a599e78317090f522` closes the weighted-density and
  bounded-extension gate. It passed targeted density/extension/AxiomAudit builds and the local
  pinned source scan plus full `Formal.+` gate (8737 jobs).
- Proof commit `2127757807768709d1ac19a0ec6f760c48a973cc` closes the order-aware `H²` Leray and
  projected-convection gate. It passed targeted bridge/projected/AxiomAudit builds and the local
  pinned source scan plus full `Formal.+` gate (8739 jobs).
- Proof commit `7ab4091eefeaf2d25b73824b9ec2941088876844` closes the positive-time `H² → H³`
  Stokes-smoothing gate. It passed targeted builds of `Formal.R3StokesH2H3Smoothing` and
  `Formal.AxiomAudit`, followed by the local pinned source scan and full `Formal.+` gate
  (8740 jobs).
- PR #82 (`Formalize endpoint-safe projected Duhamel on R^3`, proof commit
  `4f8ae0d66c65cd5458bc49b13c4e6b015e318b4d`) is merged as `03ea967`. Its hosted Lean run
  `32112489718` failed after 6 seconds because the GitHub Actions quota is exhausted; the hosted
  run is **not** the verification evidence for this merge.
- The verification evidence for `main = 03ea967` is local: the merge tree is identical to
  `4f8ae0d` (`git rev-parse <sha>^{tree}` both `d6c5424...`), and the full `Formal.+` gate
  (`lake exe cache get && lake build`) passed locally on that exact tree with 8743 jobs,
  including `Formal.AxiomAudit` (standard axioms only: `propext`, `Classical.choice`,
  `Quot.sound`).
- GitHub Actions quota is exhausted; hosted runs must not be used at all for the foreseeable
  future. All verification is local (Elan-pinned toolchain), and integration to `main` is by
  direct fast-forward push without opening a PR.
- The Picard fixed-point / local-existence layer
  (`Formal/EndpointSafeTwoSpacePicard.lean`, `Formal/R3EndpointSafeProjectedLocalExistence.lean`,
  with new `Formal/AxiomAudit.lean` prints) is committed directly on `main` after this
  continuation's local verification: full `Formal.+` gate pass (8745 jobs), pinned source scan
  clean, axiom audit standard for all four new audited theorems.
- The conjugation/reflection reality-predicate layer
  (`Formal/R3ConjugationReflection.lean`, with five new `Formal/AxiomAudit.lean` prints) is
  committed directly on `main` after local verification: full `Formal.+` gate pass
  (8746 jobs), pinned source scan clean, axiom audit standard.
- The Plancherel reality bridge (`Formal/R3FourierConjugationBridge.lean`, with four new
  `Formal/AxiomAudit.lean` prints) is committed directly on `main` after local verification:
  full `Formal.+` gate pass (8747 jobs), pinned source scan clean, axiom audit standard.
- The operator-realness slices (`Formal/R3StokesConjugationEquivariance.lean`,
  `Formal/R3LerayConjugationEquivariance.lean`,
  `Formal/R3ConvectionConjugationEquivariance.lean`) and the physically real local mild
  solution (`Formal/R3RealLocalMildSolution.lean`) are committed directly on `main` after
  local verification: full `Formal.+` gate passes (8748 → 8751 jobs), pinned source scans
  clean, axiom audit standard.
- The explicit quantitative lifespan (`Formal/R3QuantitativeLifespan.lean`, plus the
  statement-preserving refactor of `Formal/EndpointSafeTwoSpacePicard.lean` extracting
  `exists_isMildSolutionOn_of_kernelPrimitive_lt`, with ten new `Formal/AxiomAudit.lean`
  prints) is committed directly on `main` after local verification: full `Formal.+` gate
  pass (8752 jobs), pinned source scan clean, axiom audit standard (commit `6d5e541`).
- The mild restart identity and unrestricted uniqueness
  (`Formal/EndpointSafeTwoSpaceRestart.lean`, `Formal/EndpointSafeTwoSpaceUniqueness.lean`,
  with eight new `Formal/AxiomAudit.lean` prints, including the unconditional-realness
  corollary) are committed directly on `main` after local verification: full `Formal.+`
  gate pass (8754 jobs), pinned source scan clean, axiom audit standard (commit `e8b7144`).
- The maximal-continuation layer in blow-up–dichotomy form
  (`Formal/EndpointSafeTwoSpaceConcatenation.lean`, `Formal/R3MildContinuation.lean`, with
  eight new `Formal/AxiomAudit.lean` prints) is committed directly on `main` after local
  verification: full `Formal.+` gate pass (8756 jobs), pinned source scan clean, axiom
  audit standard (commit `77f3832`). This completes the endorsed 3-gate plan.
- The vertical-integration audit (`docs/formal/R3_NS_VERTICAL_INTEGRATION_STATUS.md`,
  README/STATUS frontier synchronization) is commit `7c6c8d8`; the BH reopen pass
  (`docs/gates/BH_QUANTITATIVE_RIGIDITY_K12_AUDIT.md`) follows it. Docs-only commits; no
  Lean source touched; the 8756-job gate remains the verification baseline.
- This continuation's proof and synchronized documentation were integrated by direct fast-forward
  to `main`, without opening a PR; the verified `Formal/` tree is exactly the proof commit above.
- No GitHub Action was started or rerun for the new mathematical proof.
- Automatic full Lean builds on pushes to `main` remain disabled.
- Opening a PR to `main` currently starts the hosted Lean workflow, so a no-Actions integration must
  not use a PR merely as a merge vehicle.
- The preferred interactive path is now **ChatGPT -> external Lean runner -> exact diagnostics -> ChatGPT iteration** under the contract in `docs/LEAN_CI_OPERATIONS.md`.
- Local/self-hosted execution remains a valid reproduction/fallback path.
- GitHub-hosted Actions should be used only for deliberately spent status/final-confirmation checks or when repository integration policy explicitly requires one.
- The T-SEL bridge formalization layer (`Formal/GronwallIntegralInequality.lean`,
  `Formal/R3TSelDecodedGradient.lean`, `Formal/R3TSelBridge.lean`, with 21 new
  `Formal/AxiomAudit.lean` prints) is committed directly on `main` on top of
  `a359354` after local verification: targeted builds of all three new modules and
  `Formal.AxiomAudit`, then the pinned source scan plus full `Formal.+` gate
  (**8772 jobs**, `bash scripts/lean-ci-local.sh`, toolchain
  `leanprover/lean4:v4.32.1`), axiom audit standard for every new audited theorem.
  No hosted Action was started; no PR was opened.

## Local Lean status in this workspace

The VS Code Lean extension, Elan shims, and pinned Lean 4.32.1 toolchain are installed locally. The
only environment issue found was an unset `ELAN_HOME`. The tested PowerShell setup is:

```powershell
$env:ELAN_HOME = Join-Path $env:USERPROFILE '.elan'
```

With that process-local setting, `lean --version`, `lake --version`, targeted builds, the axiom
audit, and the full gate all run locally. The extension provides the IDE/LSP integration; the actual
verification is performed by the local Elan-selected Lean compiler and kernel.

## Project claim boundary

Ultimate target: an exact official Clay/Fefferman Navier–Stokes A/B/C/D statement.

Current physical research specialization remains the `R^3`, preferably unforced `f = 0`, axisymmetric-with-swirl breakdown track governed by `SPEC.md`.

No current Lean theorem is a Clay result. Do not claim global regularity, blow-up, local well-posedness of the full concrete `R^3` problem, finite-cylinder transfer, or discrete-to-continuum promotion unless separately proved.

## Completed formal target

The previous near-term target

`R3SchwartzConvectionTermSobolevEstimate 3`

is now proved as `r3SchwartzConvectionTermSobolevEstimate_three` in
`Formal/R3SchwartzConvectionSobolevEstimate.lean`.

The same file proves `r3SchwartzConvectionSobolevEstimate_three`, obtaining the full
`R3SchwartzConvectionSobolevEstimate 3` through an exported direct sum estimate with the same
documented factor-three triangle-inequality loss as the existing `.to_convection` reduction.

That density/bounded-extension target is now also closed. The completed object is the complex
Bessel-coordinate map

`r3ConvectionH3ToH2 : R3HsVelocity 3 →L[ℂ] R3HsVelocity 3 →L[ℂ] R3HsVelocity 2`.

Here “completed” means that the codomain and domains are the existing complete `L²`
Bessel-coordinate models. It does not mean that Lean constructed a separate topological
`Completion` of Schwartz space.

The order-aware Leray/projected-convection target is now closed as well. The new bounded
reconstruction

`r3H2ToL2Operator : R3HsVelocity 2 →L[ℂ] R3L2Velocity`

implements the actual `J⁻²` Fourier multiplier. Lean proves that it represents exactly the
order-two tempered decoder and that it intertwines `r3LerayH2Operator` with the existing physical
`r3LerayL2Operator`. The resulting complex bilinear map is

`r3ProjectedConvectionH3ToH2 : R3HsVelocity 3 →L[ℂ] R3HsVelocity 3 →L[ℂ] R3HsVelocity 2`.

It has the inherited operator and pointwise bounds, stored-coordinate and reconstructed-`L²`
solenoidality, and exact Schwartz decoder agreement with the existing literal
`r3ProjectedSchwartzConvectionL2`.

The positive-elapsed-time, positive-viscosity smoothing target is now closed as well.
`Formal/R3StokesH2H3Smoothing.lean` constructs the nontrivial complex Bessel-coordinate map

`r3StokesH2ToH3Operator : R3HsVelocity 2 →L[ℂ] R3HsVelocity 3`

for `ν > 0` and `τ > 0`. Its Fourier multiplier is exactly

`(1 + ‖ξ‖²)^(1/2) * exp(-(2π)² ν τ ‖ξ‖²)`.

Lean proves the application and operator-norm bounds with the explicit majorant

`r3StokesH2H3TimeKernel ν τ = 1 + (sqrt ((2π)² ν τ))⁻¹`,

and proves that this scalar majorant is interval-integrable on `[0,T]` for every `T ≥ 0`.
The new genuine reconstruction

`r3H3ToL2Operator : R3HsVelocity 3 →L[ℂ] R3L2Velocity`

implements `J⁻³`. Reconstruction of the smoothed coordinate is exactly the existing physical
`L²` Stokes evolution of the reconstructed order-two input, both in `L²` and after embedding in
tempered distributions. The file also supplies order-three Leray decoder semantics, exact
order-two/order-three Leray intertwining, and stored-coordinate and reconstructed-`L²`
solenoidal preservation.

## Merged infrastructure through PR #80

### Representative/Fubini bridge — PR #79

The old ordinary-scalar-convolution versus bundled-Bochner representative blocker is closed for the two concrete H² majorants.

Relevant merged files/theorems include:

- `Formal/R3YoungRealSetIntegralBridge.lean`;
- `Formal/R3YoungRealConvolutionCommutativity.lean`;
- `Formal/R3SchwartzMajorantYoungRepresentative.lean`:
  - `coeFn_r3H2RightMajorantYoungL2_eq_scalarMajorant`;
  - `coeFn_r3H2LeftMajorantYoungL2_eq_scalarMajorant`;
- `Formal/R3SchwartzScalarMajorantL2.lean`;
- `Formal/R3SchwartzConvectionH2L2Majorant.lean`:
  - `norm_r3H2WeightedVelocitySchwartz_fourier_convectionTerm_toLp_le_scalarMajorants`;
  - `norm_r3H2WeightedVelocitySchwartz_fourier_convectionTerm_toLp_le_YoungFactors`.

Do not generalize that representative/Fubini identification to unrelated convolution objects without another explicit theorem.

### Fourier-coordinate and H³ closure — PR #80

`Formal/R3H2CoordinateFourierBounds.lean` now proves:

- `fourier_r3SchwartzCoordinate_eq`;
- `integral_norm_fourier_r3SchwartzCoordinate_le_H3`;
- `norm_r3H2WeightedScalarSchwartz_fourier_coordinate_toLp_le_H3`.

The exact coordinate/Fourier identity

`𝓕 (r3SchwartzCoordinate i f) = r3SchwartzCoordinate i (𝓕 f)`

is therefore green and no longer an open bridge.

`Formal/R3SchwartzConvectionH3Closure.lean` now proves:

- `norm_r3H2WeightedVelocitySchwartz_fourier_convectionTerm_toLp_le_H3`;
- `norm_r3SchwartzToHsCLM_two_convectionTerm_le_H3`.

The proved physical per-coordinate estimate is

`‖r3SchwartzToHsCLM 2 (r3SchwartzConvectionTerm i u v)‖`

`≤ 4 * ‖r3H2InverseBesselWeightL2‖ * r3CoordinateDerivativeFrequencyConstant i * ‖r3SchwartzToHsCLM 3 u‖ * ‖r3SchwartzToHsCLM 3 v‖`.

Also already available:

`r3CoordinateDerivativeFrequencyConstant_nonneg (i : Fin 3)`.

### Uniform finite-coordinate closure — locally verified commit `6ecfcda...`

`Formal/R3SchwartzConvectionSobolevEstimate.lean` adds:

- `r3UniformCoordinateDerivativeFrequencyConstant`;
- `r3UniformCoordinateDerivativeFrequencyConstant_nonneg`;
- `r3CoordinateDerivativeFrequencyConstant_le_uniform`;
- `r3SchwartzConvectionH3Constant`;
- `r3SchwartzConvectionH3Constant_nonneg`;
- `r3SchwartzConvectionTermSobolevEstimate_three`;
- `r3SchwartzConvectionSobolevEstimate_three`.

The uniform derivative constant is the finite sum over `Fin 3`. Each coordinate constant is
nonnegative, so every summand is bounded by that sum. The common per-term witness is

`4 * ‖r3H2InverseBesselWeightL2‖ * r3UniformCoordinateDerivativeFrequencyConstant`.

`Formal/AxiomAudit.lean` now prints the axiom dependencies of both final estimate theorems. They
use only the standard mathlib foundations reported by the rest of this development (`propext`,
`Classical.choice`, and `Quot.sound`).

### Weighted density and completed convection — locally verified commit `5eb2984...`

`Formal/R3SchwartzSobolevDensity.lean` proves:

- `r3SobolevWeightComplex_mul_neg`;
- `r3SchwartzBesselMultiplier_inverse_apply`;
- `r3SchwartzBesselMultiplier_surjective`;
- `r3SchwartzToHsCLM_denseRange`.

The proof uses the inverse-order Bessel multiplier on Schwartz fields and mathlib's dense range of
the canonical Schwartz-to-`L²` map. Do not strengthen this to an inducing/dense-embedding claim for
the native Schwartz Fréchet topology.

`Formal/R3SobolevConvectionExtension.lean` applies `LinearMap.extendOfNorm` first in the second
input and then in the first input. It proves:

- `r3ConvectionH3ToH2_apply_schwartz`;
- `r3HsToTempered_r3ConvectionH3ToH2_schwartz`;
- `norm_r3ConvectionH3ToH2_le`;
- `norm_r3ConvectionH3ToH2_apply_le`;
- `r3ConvectionH3ToH2_unique`.

The bounds force both dense-core maps to vanish on the appropriate kernels, so the extensions are
well-defined and do not choose Schwartz representatives or approximating sequences. The axiom
audit reports only `propext`, `Classical.choice`, and `Quot.sound` for the new audited theorems.

`R3HsVelocity s` currently has a phantom order parameter and is definitionally the same `L²`
coordinate type for every `s`. Its physical meaning is fixed by `r3HsToTemperedCLM s`. Never use
the alias equality as a physical `H³ → H²` inclusion or as a smoothing theorem.

## Stage-A candidate gate campaign (2026-08-18)

The necessary-condition gate battery was pre-registered and run at literature level against
the fixed-ν Hou NS candidate (arXiv:2107.06509). Outcome: **route killed at candidate
level** — the candidate's own `‖u‖_∞ ~ (T−t)^{−1/2}` one-scale scaling is Type I, excluded
for axisymmetric NS by CSTY 2008/2009 + KNSS 2009. See
`docs/gates/BARKER_GATE_PREREGISTRATION_2026-08-18.md`,
`docs/gates/STAGE_A_LITERATURE_VERDICT_2026-08-18.md`, and the registry entry
`ns-singularity-certificate-lab/docs/candidates/HOU_FIXED_NU_TYPE1_NS_CANDIDATE_KILL_AUDIT_2026-08-18.md`.

Second pass (same date): the two-scale literature gate and the Type II survival map are
done — `docs/gates/TWO_SCALE_LITERATURE_GATE_2026-08-18.md`,
`docs/gates/TYPE2_SURVIVAL_MAP_2026-08-18.md`, figure `docs/gates/type2_survival_map.png`
(generator `experiments/type2_survival_map.py`), registry entry
`ns-singularity-certificate-lab/docs/candidates/HOU_HUANG_TWO_SCALE_NS_ROUTE_STATUS_2026-08-18.md`.
Outcome: the Hou–Huang two-scale scenarios are Clay-inadmissible (Euler / degenerate ν) and
their standard-ν NS transfer died in the authors' own test (max-vorticity growth < 2); the
survival map nevertheless leaves a **nonempty open window** — `γ ∈ (1/2, 1)`,
`max(2γ/3, 2γ−1) ≤ α < γ` for a core carrying the `L³` divergence (lower boundary
closed, as the source map prints it in [D3]/§5; the `2γ−1` clause was later frozen
strict as kill-table A7: `α > 2γ−1`), with sub-parabolic ring
collapse dead and swirl-dominated cores forced into ≥3-region structures.

Consequences for planning:

- the Lean program below is candidate-independent and continues unchanged;
- the abstract Chen–Hou-style skeleton (Stage B) remains the right 4/10 → 5/10 target, but
  its concrete instantiation must wait for a candidate **inside the survival window**;
- the admission test for any future (N)-level candidate is now fixed: fitted `(γ, α, ρ)`
  with confidence intervals inside the open window, converged `√(T−t)·‖u‖_{L∞} → ∞`, and
  gates G1–G7 with null/positive controls;
- next theory increment for the map (cheap): tabulate the exact hypotheses of the
  `|u| ≤ C/r` exclusion family and the slightly-supercritical / Type II refinements
  ([V1]/[V2] in the map document) — they can only shrink the window near its `γ = 1/2`
  edge.

Third pass (2026-08-19): adversarial audit + kill table —
`docs/gates/D1_ADVERSARIAL_AUDIT_2026-08-19.md`, `docs/gates/TYPE2_KILL_TABLE_2026-08-19.md`.
Outcomes:

- **[D1] withdrawn** (the `ρ < 1/2` CKN-cylinder kill was unsound: ε-regularity gives no
  uniform scale-invariant bound at the visited scale); replaced by the conditional transport
  cut [D1′] `ρ ≥ min(1−γ, 1/2)`; the on-axis blob window is unaffected; corrections
  propagated to the map document, figure footnote, and the lab registry entry;
- CSTY-II verified verbatim (arXiv:0709.4230): `|v| ≤ C_* r^{−1+ε}|t|^{−ε/2}` ⇒ regular,
  `C_*` arbitrary — inside the blob window its violation is automatic (no new cut); for
  rings it forces `γ > ρ` or a mesoscale violation region;
- conditional swirl razor (K9, unverified family): if `|u_θ| ≤ C r^{−d}` (`d < 1`) implies
  regularity, then the core swirl exponent is pinned to `σ = α` exactly — an
  amplitude-subdominant core carrying `O(1)` circulation `Γ`;
- **dimension answer**: after all currently-verified cuts, `S_survive` = a 2-D open wedge
  (blob) + a 3-D conditional slab (ring, `γ < 1` for core-carried `L³`) + the ≥3-region
  corridor — not a curve, not empty;
- **verification debts** (the next cheap theory items): K4 (KNSS exact `|v| ≤ C/r` form),
  K9 (exact swirl-component criteria), K10 (full-text extraction of Seregin
  arXiv:2402.13229, revised 2026-08 — the area is actively moving).

Fourth pass (2026-08-19): debts settled, map frozen, dominant-balance inversion done —
`docs/gates/DOMINANT_BALANCE_INVERSION_2026-08-19.md` and updated kill table / figure.

- K4 retired (non-load-bearing; verified K3 covers the map's uses); K9 paid
  (Chen–Fang–Zhang weighted swirl criterion; the `σ = α` core razor holds at the `L^∞`
  endpoint); K10 paid — **Seregin's Euler-scaling Type II class maps exactly onto the
  `γ + α = 1` edge, `γ ∈ (1/2, 3/5)`**, with conditional exclusion pressure there.
- New cut **K11: `γ + α ≥ 1`** (term balance and energy-flux derivations agree). Frozen
  window: `{1/2 < γ < 1, max(1−γ, 2γ/3, 2γ−1) ≤ α < γ}`.
- Balance classification: edge = generalized self-similar Euler (contested); interior =
  quasi-static steady-Euler (Bragg–Hawthorne) cores, slowly modulated; heat balance,
  `∂ₜ`-dominant dynamics, and convection–diffusion-balanced `L³`-carrying cores are all
  impossible in the wedge. Every survivor is asymptotically inviscid (`Re_core → ∞`).
- Deferred by plan (do NOT start yet): N-level harness, Stage B modulation/trapping
  formalization, new ansatz generation, non-axisymmetric pivot, further literature
  excavation. The one recorded research question for later: do Bragg–Hawthorne profiles
  compatible with `σ = α`, `O(1)` circulation, and the wedge exponents exist?

Fifth pass (2026-08-19): BH-profile taste pass (one bounded pass, per the external
reviewer's brief) — `docs/gates/BH_PROFILE_TASTE_REPORT.md`,
`experiments/bh_taste_exponents.py`. **Verdict: YELLOW.**

- Gate A: Gavrilov / Constantin–La–Vicol verified (localized steady Euler cores with swirl
  exist at fixed swirl fraction); Jiu–Xin rigidity verified at search level (compactly
  supported axisymmetric no-swirl steady Euler ⇒ 0).
- Gate B: fixed-profile scaling is a double no-go (`σ = γ` and `Γ → ∞`; circulation-tuned
  variant gives `γ = α`).
- Gates C/D: in core variables the swirl enters Grad–Shafranov at `O(ε²)`; a regular
  `ε → 0` family would converge to a nontrivial localized no-swirl flow — dead by
  rigidity. **Any admissible family must be singular**; existence unconstructed.
- Gate E: residual hierarchy formally perturbative in the interior; closed-streamline
  secular (Prandtl–Batchelor-type) argument obstructs `α ≥ 1/2` (homogenized `Γ` ⇒
  `F̂′ → 0` ⇒ swirl decoupling ⇒ no-swirl rigidity again). Proposed conditional K12
  (report-only, NOT applied to the frozen map): quasi-static interior needs `α < 1/2`.
- Smallest missing theorem: **quantitative no-swirl rigidity** (the forced degeneration
  rate of swirl-poor localized families). Deferred; do not start without a fresh decision.

**Resume point: return to the Lean program (next gate below — operator realness
preservation), per the frozen plan. Standing decision (2026-08-19, user-approved): once the
continuation criterion is closed on the Lean side, the BH branch reopens — i.e. the
quantitative no-swirl rigidity question and the K12 decision from
`docs/gates/BH_PROFILE_TASTE_REPORT.md` become the next Stage-A item at that point.**

## Exact next Lean gate

Do not reopen the completed convolution, bounded-extension, Leray, positive-time smoothing,
endpoint-safe two-space Duhamel, or Picard local-existence work unless current source regresses.

The Picard fixed-point layer demanded by the previous handoff is closed on `main`:

- `Formal/EndpointSafeTwoSpacePicard.lean` — cumulative smoothing mass (`kernelPrimitive`)
  with monotonicity/continuity/small-time smallness; exact reversed elapsed-time
  representation of the Duhamel integral; quantitative size/difference/time-difference bounds;
  `continuousOn_duhamelIntegral`; the Picard map on `C(Icc 0 T, X)` with ball invariance and
  contraction; `exists_pos_time_isMildSolutionOn` (existence on some `0 < T ≤ 1`, trajectory in
  the closed `‖u₀‖ + 1` ball, uniqueness among ball-valued mild solutions).
- `Formal/R3EndpointSafeProjectedLocalExistence.lean` —
  `r3EndpointSafeProjected_exists_localMildSolution`: for every `ν > 0` and order-three Bessel
  coordinate `u₀`, local existence + ball uniqueness for
  `IsR3EndpointSafeProjectedMildSolutionOn hnu T u₀ u`, plus the unfolded mild-equation form
  `r3EndpointSafeProjected_localMildSolution_equation`.

The first slice of the reality gate is closed by `Formal/R3ConjugationReflection.lean`:
fiber conjugation `r3CConj` with its fixed-point characterization, the norm-preserving carrier
involutions `r3L2Conj` (pointwise conjugation, `→L[ℝ]`) and `r3L2Reflect` (composition with
`x ↦ -x`, `→L[ℂ]`), their commutation, and the predicates `IsR3RealVelocity` /
`IsR3ConjugateSymmetricVelocity` with algebraic closure, closedness, and the a.e.
characterization `isR3RealVelocity_iff_im_ae`. Do not redefine these structures.

The Plancherel reality bridge demanded by the previous handoff is closed by
`Formal/R3FourierConjugationBridge.lean`: the Schwartz involutions `r3SchwartzConjCLM` /
`r3SchwartzReflectCLM`, the pointwise identity `r3Fourier_conj_eq`
(`𝓕 (conj ∘ f) ξ = conj (𝓕 f (-ξ))`), the `toLp` compatibility lemmas, the exact `L²`
intertwining `fourier_r3L2Conj` (`𝓕 (r3L2Conj g) = r3L2Reflect (r3L2Conj (𝓕 g))`), and the
equivalence `isR3RealVelocity_iff_fourier_conjugateSymmetric`. Do not re-prove these.

The next smallest mathematical task is **realness preservation of the concrete operators**
(FORMAL_SCOPE section 6, next gate 1). Slice 1 is **closed** (2026-08-19,
`Formal/R3StokesConjugationEquivariance.lean`, full gate 8748 jobs, axiom audit standard):
the generic theorems `reflect_conj_of_realEven_multiplier` (frequency side) and
`r3L2Conj_of_fourier_realEven` (physical side, via the Plancherel bridge and injectivity)
plus symbol realness/evenness give
`r3L2Conj_r3StokesL2Operator`, `r3L2Conj_r3StokesH3Evolution`,
`r3L2Conj_r3StokesH2ToH3Operator`, and the `IsR3RealVelocity` preservation corollaries.
Reuse `r3L2Conj_of_fourier_realEven` for every further scalar-multiplier operator
(including the Bessel weights / decoders if needed).

**The operator-realness gate is now FULLY closed** (2026-08-19). Slice 2
(`Formal/R3LerayConjugationEquivariance.lean`): fiber-level conjugation equivariance and
evenness of the complex Leray symbol, the matrix-multiplier generalization of the generic
equivariance theorems, `r3L2Conj_r3LerayL2Operator` plus the definitionally-equal order-two/
order-three variants, and the `IsR3RealVelocity` corollaries. Slice 3
(`Formal/R3ConvectionConjugationEquivariance.lean`): carrier antilinearity `r3L2Conj_smul`;
conjugation equivariance of real even Schwartz Fourier multipliers and hence of the Bessel
coordinate map (`r3L2Conj_r3SchwartzToHsCLM`); conjugation equivariance of the Schwartz
convection (via `fderiv` commuting with the real-linear fiber conjugation); the
triple-conjugated bilinear map `r3ConjugatedConvectionH3ToH2` (ℂ-bilinear again by three
conjugations), shown equal to `r3ConvectionH3ToH2` by the dense-core uniqueness theorem;
hence `r3L2Conj_r3ConvectionH3ToH2`, `r3L2Conj_r3ProjectedConvectionH3ToH2`, and
`IsR3RealVelocity.projectedConvection`.

**The real local mild solution is closed** (2026-08-19,
`Formal/R3RealLocalMildSolution.lean`): conjugation equivariance of the endpoint-safe
Duhamel integrand (`r3L2Conj_r3EndpointSafeProjectedDuhamelIntegrand`), the conjugated
trajectory of a mild solution with real datum is again a mild solution
(`IsR3EndpointSafeProjectedMildSolutionOn.r3L2Conj_comp`, using
`ContinuousLinearMap.intervalIntegral_comp_comm` to pass conj through the Bochner
integral), and — by the ball-uniqueness clause, with **no new fixed point** —
`r3EndpointSafeProjected_exists_realLocalMildSolution`: for `ν > 0` and physically real
`u0`, a horizon `0 < T ≤ 1` and a mild solution that is **physically real at every
certified time**, with the ball bound and ball uniqueness.

**The explicit quantitative lifespan is closed** (2026-08-19,
`Formal/R3QuantitativeLifespan.lean` + refactor of `Formal/EndpointSafeTwoSpacePicard.lean`):

- abstract layer: `exists_isMildSolutionOn_of_kernelPrimitive_lt` — existence + ball bound +
  ball uniqueness on **any** given horizon `T > 0` with
  `kernelPrimitive T < δ(‖u₀‖) = min (1/(‖B‖(R)²+1)) (1/(2(‖B‖·2R+1)))`, `R = ‖u₀‖+1`;
  the old existential `exists_pos_time_isMildSolutionOn` is now a corollary (statement
  unchanged);
- closed-form kernel mass: `r3EndpointSafeProjected_kernelPrimitive_eq` —
  `K(T) = T + √T/(π√ν)` for `T ≥ 0` (via `integral_rpow` at exponent `-1/2` and
  `√((2π)²ν) = 2π√ν`);
- explicit lifespan: `r3MildLifespan nu r = (δ(r)/(1 + (π√ν)⁻¹ + δ(r)))²` with
  `r3MildLifespan_pos`, `r3MildLifespan_le_one`, and the key inequality
  `r3EndpointSafeProjected_kernelPrimitive_mildLifespan_lt` (`K(T₀) < δ`, algebra:
  `K(T₀) = √T₀(√T₀ + c)` and `√T₀ = δ/(1+c+δ) ≤ δ < 1+δ`);
- quantitative existence: `r3EndpointSafeProjected_exists_mildSolutionOn_mildLifespan`
  (complex carrier) and `r3EndpointSafeProjected_exists_realMildSolutionOn_mildLifespan`
  (physically real data ⇒ pointwise-real solution), both on the explicit horizon
  `T₀(ν, ‖u₀‖)` depending only on the viscosity and the initial-datum norm.

**The mild restart identity and unrestricted uniqueness are closed** (2026-08-19,
`Formal/EndpointSafeTwoSpaceRestart.lean` + `Formal/EndpointSafeTwoSpaceUniqueness.lean`):

- restart (`IsMildSolutionOn.restart`, concrete
  `IsR3EndpointSafeProjectedMildSolutionOn.restart`): a mild solution restarted at a
  certified time `s` solves the shifted mild equation on `[0, T-s]` with datum `u s` —
  proof splits the Duhamel integral at `s`, pushes the linear evolution out of the head
  piece by `smoothing_coherent` (a.e.; the endpoint `σ = s` is null), and translates the
  tail by `σ ↦ s + σ` (`duhamelIntegrand_comp_add_left`, everywhere, no null set);
- contraction step (`isMildSolutionOn_eq_of_contraction`): two `R`-ball solutions with the
  same datum agree when `‖B‖·2R·K(T) < 1` — max of the difference norm on the compact
  horizon satisfies `M ≤ θM`, no fixed-point machinery;
- **`IsMildSolutionOn.unique` / `r3EndpointSafeProjectedMildSolution_unique`**: two mild
  solutions with the same datum agree on their common horizon, with **no ball
  restriction** (continuity gives a common bound `R`; small-time smallness gives a step
  `T_s` with contraction; restart + induction walk the agreement window; Archimedes ends);
- free corollary (`IsR3EndpointSafeProjectedMildSolutionOn.isR3RealVelocity`):
  **every** mild solution with physically real datum is pointwise physically real
  (the conjugated trajectory is a solution with the same datum; unconditional uniqueness
  pins it) — no ball hypothesis anywhere.

Lean tooling note for these files: rewriting under `ℝ≥0` anonymous-constructor arguments
(`⟨τ, hτ0⟩`) breaks `rw`'s motive check under `instances` transparency; use
`congr 1` + `exact`, `congrArg` on operator equalities, and applied congruence lemmas
(`positiveSmoothing_congr_apply`) instead. Dot notation on contract theorems must pass the
contract explicitly (`hu.restart C hs`), since `C` precedes the self argument.

**The maximal-continuation layer is closed in blow-up–dichotomy form** (2026-08-19,
`Formal/EndpointSafeTwoSpaceConcatenation.lean` + `Formal/R3MildContinuation.lean`),
completing the endorsed 3-gate plan:

- concatenation (`IsMildSolutionOn.concat`, concrete
  `IsR3EndpointSafeProjectedMildSolutionOn.concat`): a mild solution on `[0,s]` followed
  by a mild solution from the reached state glues to a mild solution on `[0, s+T']` — the
  restart computation in reverse (head piece absorbs the evolution by
  `smoothing_coherent` a.e., tail piece is the translated Duhamel integral; glued
  continuity via `ContinuousOn.union_of_isClosed`);
- `r3MildLifespan_antitone`: the explicit lifespan is antitone in the datum norm, so one
  bound `R` yields a uniform positive step `r3MildLifespan ν R`;
- `r3EndpointSafeProjected_exists_extension_of_bounded`: an `R`-bounded mild solution on
  `[0,T]` extends to `[0, T + r3MildLifespan ν R]`;
- `r3MildHorizons` (the set of certified horizons for a datum), nonempty by the explicit
  lifespan; `r3EndpointSafeProjected_horizons_unbounded_of_uniform_bound`: a uniform norm
  bound on all certified solutions forces the horizon set to be unbounded (a horizon
  within one uniform step of the supremum would extend past it);
- **`r3EndpointSafeProjected_blowup_dichotomy`**: either arbitrarily long horizons carry
  mild solutions, or the certified solution norms escape every ball.

Lean tooling note (in addition to the `ℝ≥0`-mk note above): rewriting under an applied
if-lambda trajectory fails because `rw` sees the unreduced application — insert
`show <beta-reduced form>` before rewriting; and `congr 1` can close subgoals via
`assumption` when the needed equality is in context, so prefer explicit `congrArg` when a
following tactic expects remaining goals.

**The 2026-08-19 vertical-integration audit + BH reopen pass is complete** (multi-agent
adversarial pass; deliverables `docs/formal/R3_NS_VERTICAL_INTEGRATION_STATUS.md` and
`docs/gates/BH_QUANTITATIVE_RIGIDITY_K12_AUDIT.md`; README/STATUS synchronized):

- vertical integration verdict: **CHAIN CLOSED TO CONTINUATION** (README was stale, the
  mathematics was closed); 5 required semantic edges remain to the official Clay
  statement (Bucket A of the status doc);
- BH verdict: **YELLOW** (grade unchanged, content replaced). The baseline power-vs-log
  dichotomy is retired as ill-posed; the smallest missing theorem is now the
  **swirl-fraction gap (★)**: for compactly supported axisymmetric steady Euler flows,
  is `inf s(u) > 0`, `s(u) = ∫|u_θ|²/∫|u_pol|²`? (`inf s > 0` ⇒ RED for blob *and*
  ring; a family with `s → 0` ⇒ YELLOW-GREEN.) One new hard result: the exact
  momentum-flux identity `∫u_r² + ∫u_θ² = 2∫u_z²` for localized steady axisymmetric
  Euler [H], equivalent form of (★). K12: **KEEP CONDITIONAL** (route (F) closed for
  `α > 1/2` up to a separatrix-sliver caveat; route (P) narrowed but open; `α = 1/2` is
  a grey line; ring corridor untouched — planar rigidity is false). Report-level
  annotations K12′/K12″ recorded; frozen map unchanged; K9 two-scale verification debt
  logged.

**The (★) P0 probe is complete** (2026-08-19,
`docs/gates/BH_SWIRL_FRACTION_PROBE_2026-08-19.md`; Gavrilov + CLV primary texts read in
full; verdict **YELLOW, content inverted twice**):

- published constructions pinned: `σ(A) = 1/2 − (21/32)A`, `s = 1/2 − (21/16)δ²` [H]
  (core swirl fraction 1/3 forced four ways, incl. CLV (52) [V]);
- but the corrected range is `(0, 1/2]`: continuing the same solution to its Hill-type
  separatrix and cutting a thin shell there gives an explicit candidate family with
  `σ ≃ 0.82√(A_H − A) → 0` [C on one continuation lemma] — **(★) as stated is likely
  answered NO** (`inf s = 0` over the naked A_NS);
- **but the branch does not go GREEN**: the realizing family (`r_min/R ~ s`, sheet
  thickness `~ s²`) is below the viscous cutoff `√(ντ)` on the whole interior blob
  wedge [C] — **(★) is decoupled from the branch verdict**; the decision object is now
  **(★_geo): `s(u) ≥ c·(r_min/r_max)^θ`** on the localizable class (θ = 1/5 proved
  per-streamline; θ ≥ 1/2 would empty the interior blob wedge; the explicit family sits
  at θ = 1);
- A_NS minimally defined (A1–A5; no normalization needed; a priori `q ≤ 2`);
  CLV F → 0 classified: F ≡ 0 dead [H, redundant vs Jiu–Xin]; radially thin pinned at
  `s = 1/2`; wide-aspect corridor = SURVIVING FAMILY (conditional); Scope B
  (non-localizable) open and decisive; stagnant-axis structural fact proved [H].

**The (★_geo) geometry gate is closed — Outcome A, θ = 1, sharp** (2026-08-19,
`docs/gates/BH_GEO_SWIRL_AGGREGATION_2026-08-19.md`; erratum appended to the P0 probe;
verdicts **GEO-RESTRICT / YELLOW-RED / CAP: DO NOT START**):

- **THEOREM [H, Scope A]**: on every regular closed poloidal streamline (`A > 0`) of a
  `p = p(ψ)` steady axisymmetric Euler flow, `s_level ≥ δ(ψ)/157` and
  `α/r_min² ≥ 1/42`; globally `s(u) ≥ (1/157)·δ_geo(u)` with
  `δ_geo = ⟨r_min(ψ)/r_max(ψ)⟩_{E_pol}` (barycentric; aggregation lossless). Convexity
  hypothesis retired; ω-machinery off the critical path (one-parameter elliptic-orbit
  rigidity: `s_level` is *determined* by `δ`); θ = 1 sharp at level scale [H], flow
  scale [C] (shell family sits exactly on the bound);
- frozen substitution: pure-geometry Prop G (`E = 2γ − α > 1/2` on the whole wedge, no
  contradiction from Euler alone) strictly separated from Prop V [C] (under the
  unpromoted V1 viscous premise the interior blob wedge empties; exact threshold θ < 4,
  correcting "θ ≤ 2"); **nobody may cite this as "blob dead"** — Scope A + V1 gates;
- **ring corollary [C, single-sourced, unverified]**: thin ring ⇒ δ(ψ) → 1 uniformly ⇒
  s ≥ c > 0, contradicting `s_ring → 0` — viscosity-free, θ-independent; contradicts
  the recorded "ring corridor has no rigidity kill";
- armed falsifier P6 (A↔σ dictionary, one number, [C-num]); sharp constant at σ*
  uncomputed (cosmetic).

**The ring corollary is verified and the scope freeze is executed** (2026-08-19,
`docs/gates/BH_RING_COROLLARY_ADVERSARIAL_AUDIT_2026-08-19.md`; verdicts
**RING-ONE-SCALE-KILL / YELLOW-RED / NEXT: MULTI-REGION AUDIT**; map annotation
authorized and appended to `TYPE2_KILL_TABLE_2026-08-19.md` with riders R1–R4):

- **certified kill (amplitude/circulation form, cheaper than the energy route)**: Scope-A
  top-speed level has `r_min ≤ √3·Γ₀/‖u‖_∞·(1+o(1))` (thin-endpoint pinning
  `u_θ² = |u|²/3`, three independent derivations) ⟹ contained one-scale ring forces
  `ρ ≥ γ` — contradiction with K3 *and* (via `ρ+2α ≥ 3γ`) K6; doubly sourced,
  viscosity-free, compactness-free, non-vacuous (`(0.6, 0.42, 0.45)` ∈ S_ring killed);
- **exact map wording (nothing broader)**: "one-scale localizable ring branch excluded by
  swirl-geometry pinning";
- **Scope B is a GAP, not an exit** [H, witness-backed]: Hill's spherical vortex is a
  steady axisymmetric Euler flow with `s_level ≡ 0` — the geometry-gate conclusion is
  false outside Scope A; `p = p(ψ)` is added and not removable. Sharp open question:
  must a *localized* steady axisymmetric Euler core with swirl satisfy the eikonal
  overdetermination `|∇ψ|² + F² = 2A(ψ)r²`?
- **"blob dies too" REFUTED**: Scope A relocates the swirl sup to the axis-grazing
  tongue tip (`r_min ≲ τ^γ`), where `Γ = O(1)` saturates; K9's `σ ≤ α` is a
  sup-location premise, not a theorem there — blob unchanged, still V1-conditional; new
  K9 debt (P6) logged in the map annotation;
- errata appended (not silently repaired): geometry-gate §8 global-`s` sentence
  withdrawn (amplitude form replaces it), `k = −P′/2` (P6 falsifier must be re-derived
  before evaluation), `α_g` notation; taste report §3 is the MHD GS form (`P = −B`).

**The multi-region audit is complete** (2026-08-20,
`docs/gates/BH_MULTIREGION_AUDIT_2026-08-20.md`; per-class verdicts **M2 RESTRICTED (no
independent members — "not a ring branch") · M3 OPEN · B2 RESTRICTED**; BH
**YELLOW-RED held**; next branch **FREEZE REVIEW**):

- K3 is a covering condition (concave min; middle-ε gap witness); K9 reduces to
  Γ-saturation and is a **trichotomy** in the saturation scale (`β_v = α` printed /
  `β_v ∈ (α,γ]` intra-core, unanalysed / `β_v < α` separate region); the map's `σ` is
  ill-posed for on-axis cores (`σ_core` vs `σ_sup`; in Scope A `σ_sup = γ` always);
- amplitude gate on multi-region flows: the second scale is **capped** (`ρ_T ≥ γ`),
  not pinned; every Scope-A blob is two-scale in the tongue sense; the tongue's energy
  share `→ 0` so **V1 does not bite it**; the Gate-C sacrifice is selected: uniform
  `C¹` fails at rate `1/ε`;
- **the interlock (highest value)**: amplitude-gate silence ⟺ K3 middle-ε gap ⟺ M3's
  swirl-dominated core — one object, covered exactly by the **retired row K4** (KNSS
  `|v| ≤ C/r`), whose retirement rationale is FALSE (`ρ=σ=γ` violates K3 for every ε
  yet obeys `|u| ≤ C/r`). **M3's blocking question = does KNSS bite the Γ-saturated
  core?** Only a freeze decision can re-arm a retired row;
- **P6 falsifier RESOLVED: PASS** (symbolic; `k` cancels; corrected
  `X = (1/3)(1−7σ²/16)`, test number `21/64 = 21/64`; retired: `23/32`, `0.5391`;
  residual [V?]: the `δ_probe = ℓ/R` reading);
- literature: Jiu–Xin verbatim abstract secured [V] (C¹, finite energy + constant far
  field; **no "no swirl" in the abstract** — body must carry it, debt sharper, not
  paid); **DVEP (arXiv:2005.04380, ARMA 2021) = Scope-B witness at weak regularity**
  (compactly supported, axisym-with-swirl, piecewise smooth, explicitly not
  localizable) — necessity of `p = p(ψ)` is false without a regularity hypothesis;
  the geometry gate's §10 trigger **as worded is met** (freeze review must fire or
  amend to primary-class wording); Peralta-Salas–Slobodeanu 2026: analytic localizable
  ⟹ axisymmetric (overdetermination reading confirmed);
- corrections queued for the freeze review: Prop G/V carry the far-field erratum
  (repair: per-level + Markov inside core energy, `E = 2γ−α` stands in weakened form);
  `S_blob` boundary `α > 2γ−1` strict; [D2] "≥3-regions" over-count (min 2).

**The M3 × KNSS gate is answered** (2026-08-20,
`docs/gates/BH_M3_KNSS_GATE_2026-08-20.md`; the K4 verification debt is PAID first-hand
from arXiv:0709.3599 full text):

- **Answer: NO** — frozen M3 (`γ₂ ≤ γ`) does not imply KNSS's global `|v| ≤ C/r`; the
  defeating member is the **amplitude-tie face `γ₂ = γ`**, whose ancient limit contains
  a non-decaying plateau = KNSS's own `u = b(t)` obstruction (their receding-axis
  branch is Type-I-only [V]);
- **but `M3 ∩ {γ₂ < γ}` DIES** [D, Scope-A-free, viscosity-free, conditional on (E)
  dictionary-exhaustiveness + (P) class transfer]: the L³ carrier's `C/r` violation
  escapes the `τ^γ` zoom, Prop 6.1 is amplitude-normalized and **rate-free (Type II is
  the enabler, not the obstruction)**, Thm 5.3 kills the limit;
- the tie face has `(γ, α₂) ∈ S_blob` by pure exponent arithmetic — **it is a B2 point
  wearing a Γ-saturated sub-core**: M3 moves **OPEN → RESTRICTED (no independent
  members)**; **the Scope-A open set contracts to B2 alone** (blockers: V1 [C] +
  quantitative rigidity rate);
- map queue additions (freeze review): K4 restore [V] with Thm 6.1 + rider
  (`K₄ ∩ M3 = ∅` — K4 never applies to the unzoomed flow); new conditional row K4′
  ("amplitude-normalized ancient limit decays like 1/r ⟹ regular", kills
  `M3 ∩ {γ₂ < γ}` mod (E)+(P)); elongated-filament one-region M3 (P5, cleanest K4′
  target); K5-not-scale-invariant legend (P7); K2 row corrections.

**The constant-exclusion pass is complete** (2026-08-20,
`docs/gates/BH_CONSTANT_EXCLUSION_ROW_2026-08-20.md`; ruling PARTIAL — better than
either hoped-for outcome):

- **branch (a) is RETIRED, not open** [D, row R-A]: KNSS Lemma 6.1 nowhere requires
  `C = 1`; re-centring the zoom on the Γ-saturated level (amplitude corollary,
  `C = √42`) keeps the axis at bounded rescaled distance — the limit is axisymmetric
  with a Γ-saturated core, for **every** Scope-A blob, B2 included. Branch (a) was an
  exact-maximizer artifact. (Boost-the-original refuted, R-NEG1; constants cannot be
  excluded by any scale-invariant estimate at an axisym singularity — Ożański–Palasek
  — but re-centring makes that moot, R-NEG2);
- **everything reduces to ONE literature-named open object (OO)**: nonzero bounded
  ancient mild axisymmetric NS solution with `Γ ∈ L^∞`, `Γ ≢ 0` (the survey's "most
  difficult remaining case");
- **certified primary conditional row R-B1 [V+C]**: Lei–Zhang JFA 2011 Thm 1.2
  (bounded weak ancient + `r|v_θ|` bounded + **stream function BMO** ⟹ `v ≡ 0`).
  Every hypothesis transfers FREE (Γ is exactly scale-invariant under the Prop-6.1
  zoom — new unconditional row K4‴) except **BMO of the boosted limit's stream
  function** — one hypothesis, one logarithm of slack over the (Q)-form. If
  discharged: **the tie face AND B2's Γ-saturated blob die — no Type-I, no viscosity,
  no Scope-A geometry**;
- (E) ⟹ (Q) holds but needs **(E⁺)** (adds C¹-exhaustiveness near the zoom centre);
  escalation: charging (E⁺) kills the tie face at the same strength as `γ₂ < γ`;
- freeze-review queue extended: K4′ amend to (E⁺); new rows K4″ [C] and K4‴ [D]; P7
  legend (`Γ ∈ L^p, p<∞` non-descending); KNSS implicit-(6.16) footnote; negative
  rows; branch wording ("M3 tie face and B2 reduce to one object (OO)").

**The Biot–Savart deviation ledger is complete — R-B2 DISCHARGED on the frozen
dictionary** (2026-08-20, `docs/gates/BH_BIOT_SAVART_LEDGER_2026-08-20.md`, tag [C]):

- `r_y|w_pol| ≤ C` τ-uniform on the receding ball `R₀ ≤ |y| ≤ R_k = ε₀τ^{(β−γ)/2}`
  (β = finest non-local gradient exponent: α for B2, ρ₂ for the tie face) ⟹
  `|w| ≤ C/r` globally on the re-centred ancient limit ⟹ **KNSS Thm 5.3 ⟹ w ≡ 0 ⟹
  Γ ≡ 0 — contradiction with the Γ-saturated core ⟹ M3 tie face AND B2's Γ-saturated
  blob excluded** (no Type-I, no viscosity, no energy, no Scope-A geometry, no V1);
- conditionals: **(E⁺⁺)** [C] (the tongue's `ω_θ` content is the core's — its recorded
  vorticity excess is `∇Γ`-generated `ω_r/ω_z`, invisible to the poloidal kernel) +
  (P) [C] + (N-Γ) [C-dict]. The kill routes through **KNSS 5.3, not Lei–Zhang**;
  R-B1's "one log of slack" REFUTED (BMO-stream ⟺ `w ∈ BMO^{-1}`, zero logarithms);
- **the debt is localized, not erased**: the single remaining substantive conditional
  is one exponent — the named negation witness **(NECK)** (poloidal shear layer of
  amplitude order riding the tongue's sub-saturated stretch; defeats both rows at rate
  R; dictionary-extension, inadmissible as a class member; exactly what (E⁺⁺)
  excludes);
- kernel formula sheet [H] established (monopole absent in far zone; axis-straddling
  2-D window empty; `b_τ` axial by derivation); corrections queued: gate's
  `r|u_pol| ≲ 1` is exterior-tail only (F5); tongue `‖ω‖` not chargeable to the
  poloidal kernel (F6); freeze queue F1–F8 with exact wordings.

**The neck ω_θ-budget is complete** (2026-08-20,
`docs/gates/BH_NECK_OMEGA_BUDGET_2026-08-20.md`; ruling: **outcome (b) in its
general clause — δ_T itself REFUTED**, three independent routes):

- the exact budget identity is established, twice-derived (2-D conservation form +
  Kelvin/winding): stretching = 2-D compressibility defect, cancels identically;
  **viscosity is a pure boundary flux with no sign (T4)** — the claimed bulk sink
  `−ν∫ω_θ/r²` does not exist (R-NEG4); production is oscillation-controlled,
  `|∮(Γ²/r³)dr| ≤ ½ osc_R(Γ²)(r₁^{−2}−r₂^{−2})`, δ-free in both tongue orientations;
- **δ_T is permanently removed from the branch** (F10) — not the missing exponent;
- **the missing exponent is a coherence time (COH)**: (E⁺⁺) ⟺ `θ_coh(ρ) ≥ 2ρ` on
  `ρ ∈ [(γ+α)/2, γ]`; below threshold (NECK) is reachable at damage rate
  `R = τ^{ρ−γ}`. Reference horizons: turnover `ρ+γ` (clears, ν-free), viscous `2ρ`
  (exactly marginal), lifetime `1` (fails everywhere on the neck — K11 `γ+α ≥ 1`
  says precisely that the whole neck is inside `√(ντ)`);
- with the full-lifetime horizon the budget is **vacuous on all of S_blob**
  (R-NEG3): both proposed exponent wedges refuted (`α+3γ<2` empty under K11;
  `γ+3α<2` outer-endpoint-only — W3 truncated sheet at `R* = τ^{(1−2γ)/3}`);
- **tag: (E⁺⁺) stays [C]**; both analyst outcome-(a) verdicts rested on undischarged
  viscous inputs; not ruled (c) — W3 is a negation witness only; (NECK) refined to
  any dyadic-annulus sheet at `R ≤ min(R*, R_k)`;
- freeze queue extended with **F9–F14** ((E⁺⁺) re-worded to the κ-form actually
  consumed, F12; `R₀` constant mismatch, F14).

**The (COH) winding pass is complete** (2026-08-21,
`docs/gates/BH_COH_WINDING_2026-08-21.md`; 3 analysts + 2 independent verifiers +
critic, outcome (ii) **unanimous and provenance-clean**):

- **(COH) not discharged at any radius; the winding form is RETIRED as a discharge
  vehicle** (structural + input starvation — residence, confinement, fold count,
  material preimage — but NOT proved impossible); (E⁺⁺) stays [C]; R-B2′ unchanged;
- **headline [D]: the INCREMENT/LEVEL GAP — the frozen (COH) "iff" is WRONG.**
  Budget and winding routes bound only `|κ̂(t) − κ̂₀|`; (E⁺⁺) needs `|κ̂(t)| ≤ C`;
  on the ancient limit there is no anchor, and the dictionary's only level bound at
  neck radii is the contour form `|κ̂| ≤ CR` — exactly (NECK) level. `θ_coh ≥ 2ρ`
  is **necessary but NOT sufficient**. The debt splits into TWO objects:
  **(COH-Δ)** (coherence, as printed) + **(ANCH)** (level/erasure for `κ̂`, carried
  only by T4 since there is no bulk sink — R-NEG4 re-verified by a fifth route);
- persistence ruled explicitly: "(NECK)-level `κ̂` present initially and
  persisting" is neither excluded nor forced (the adversary's "forced below ρ*"
  refuted); it does not re-open R-B2 (already conditional on (E⁺⁺)) but enlarges
  what a discharge must deliver;
- method facts to [C-dict]: exact winding identity (second viscous term cancels ⟹
  T4-only ledger confirmed); osc hint vacuous (`min(Γ₀, rτ^{−γ}) = Γ₀` identically
  on the neck — zero exponent); exponent equivalence (power-for-power with the
  production budget; R-NEG3 by a second route); **no Lagrangian localization**
  (Eulerian transfer licensed only on the turnover horizon — circular; F18);
- cumulative-free edge real but inert: `TV_s(θ)` is an unassigned Lagrangian
  geometric quantity with no maximum principle — sign-coherence debt converted to
  geometric debt, same size;
- freeze queue extended **F15–F20** (F16 = correction to frozen text: F11
  superseded; R-NEG5/R-NEG6; T4 = named unassigned input, sole carrier of (ANCH);
  witnesses W4/W6, renumber W5).

**The FREEZE REVIEW is EXECUTED** (2026-08-21, user's fork-(β) adjudication
received verbatim and applied; master record
`docs/gates/FREEZE_REVIEW_2026-08-21.md` (31-row adjudication table) + authorized
annotation A1–A20 appended to `docs/gates/TYPE2_KILL_TABLE_2026-08-19.md`; both
audited by a 3-lens Opus workflow — adjudication fidelity / source consistency /
completeness — all blockers and errors fixed before commit):

- **fork (β)**: the frozen dictionary **declines** the neck poloidal level bound,
  `sup(ω_θ/r)`, and `ℓ_neck` — nothing was invented at the review;
- adopted: σ_core/σ_sup split (A1); K9 saturation-scale trichotomy, `β_v ∈ (α,γ]`
  an open debt (A2); K6 [D2] "≥2 regions" under power-law `L³` (A3); Prop G/V
  per-level+Markov repair (A4); P6 `7/16`/`21/64` symbolic PASS + residual [V?]
  (A5); **K4 restored [V]** with the zoom-route-only rider and an explicit
  no-corridor-coverage clause (A6); `S_blob` `α > 2γ−1` strict (A7); §10 trigger
  amended in its Scope-B limb only — `A_NS`-internal witnesses; DVEP no fire (A8);
  K4′ [(E⁺)+(P)] (A9); K4″ ≡ R-B1 demoted to redundant confirmation (A10); K4‴
  (A11); P5 corollary-only (A12); P7 (A13); K2 correction (A14); **R-B2′ primary
  row [C]** with the full chain incl. `v = b·e_z` (A15); **(E⁺⁺) = (COH-Δ) +
  (ANCH)** κ-form + symbol legend (A16); ledger F5–F8 (A17); R-NEG1–R-NEG6
  (A18); winding retirements + `ℓ_neck` ≠ ledger-`β` disambiguation (A19);
  residuals incl. W6→W5 renumber, F15-conflict resolution, `R₀`-as-two-objects
  (A20);
- **post-freeze frontier (frozen)**: M2 RESTRICTED · M3 RESTRICTED · Scope-A
  quasi-static = **B2 alone**, killed by R-B2′ [C] on (COH-Δ)+(ANCH)+(P)
  (+(N-Γ) [C-dict]); (NECK) = standing dictionary-extension request (`θ_coh`,
  `ℓ_neck`); **all three in-house vehicles retired/blocked** (budget/winding;
  level route; T4-with-a-sign). BH **YELLOW-RED maintained**; no CAP trigger.

**The Scope-B reconnaissance is complete** (2026-08-21,
`docs/gates/BH_SCOPEB_RECON_2026-08-21.md`; 3 analysts + verifier + critic, all
decisive sources fetched first-hand; **record-only — F21–F29 are PROPOSED, not
executed**):

- **trigger ruling (T-c) OPEN — no fire, twice over**: DVEP (arXiv:2005.04380,
  read in full) fails `A_NS` (A1) — the velocity jump is structurally essential
  (Neumann `c > 0` forces `|u|² = c` inside vs 0 outside; solid torus, piecewise
  `C^s`, not `C⁰(R³)`) — **and** its non-localizability is **asserted, never
  proved** (4 `localiz` hits, no lemma/location of failure). The forcing
  direction is **empty in 3D**: all three papers with localizability as their
  subject (CLV 1903.11699; Peralta-Salas–Slobodeanu 2606.13462 — NEW, localizable
  + analytic ⟹ axisymmetric; Sato–Abe 2608.11547 — NEW) *assume* it. Canonical
  open question printed (recon §1); A8 stands, no gate revisit, no CAP;
- **scope classification (critic-ruled)**: every K-row, K4′/K4″/K4‴, R-NEG1–6,
  `S_blob`, and the tie-face merge are **SCOPE-FREE**; Scope-A enters only via
  the geometry gate's elliptic-orbit rigidity (per-level bounds, amplitude
  corollary, amplitude gate, Prop G/V, M2 dissolution, **R-B2′'s re-centring
  anchor on B2**); (E⁺⁺)/(NECK)/θ_coh/ℓ_neck/T4/W1–W5 are **undefined, not
  open, in Scope B**; per-level bound is **FALSE** outside Scope A (Hill) — no
  weakening route;
- **Scope-B landscape**: `S_blob` unchanged; **one-scale ring and M2 REOPEN**;
  M3 `γ₂<γ` still dies (K4′ scope-free); **B2 unkilled in Scope B**; cheapest
  missing object = **(SB-ANCH)** (scope-free re-centring anchor — K9 gives
  existence of a Γ-saturated region, not co-location; no substitute recorded);
- **defects found in our own frozen text** (repairs proposed, not executed):
  F22 — R-B2′'s "no Scope-A geometry" clause is **false of its anchor** (three
  documents; on B2 the row is Scope-A-gated; on M3 `γ₂<γ` it is scope-free);
  F24 — A8 patched the trigger but the gate's verdict sentence ("a single
  non-localizable localized steady flow would restore YELLOW immediately") was
  left regularity-free; F23 — the DVEP recording overstates ("explicitly
  non-localizable" → "authors assert, no proof").

**The R-B2′ anchor-independence audit is complete** (2026-08-21,
`docs/gates/BH_RB2_ANCHOR_AUDIT_2026-08-21.md`; 3 analysts + verifier + critic;
record-only — F30–F36 proposed, not executed):

- **fork (b)**: no recorded scope-free substitute; **(SB-ANCH) = the named
  primary Scope-B gap; B2 recorded UNKILLED in Scope B**; fork (c) does not
  fire under the operative unlisted-consumption test (C6 records that the
  recon's own printed (c)-wording would have fired — program item riding the
  next agenda);
- **two riders**: (i) the true Scope-A gate is the **exhaustiveness step**
  ("every Scope-A blob is two-scale"), not the zoom — R-B2′ is already
  scope-free on `B2 ∩ {β_v = γ}` (structurally the tie face); Scope B loses the
  theorem that this sub-class *is* B2; (ii) a granted (SB-ANCH) would still not
  make R-B2′ statable in Scope B (level ≠ labelled region; (E⁺⁺)/(NECK)
  undefined there) — outcome (a) alone would not have killed B2 in Scope B;
- **(SB-ANCH)-final**: (H1) sup-swirl saturation ∧ (H2) co-located Γ-saturation
  (distance clause deleted — derivable from (H1)+Γ-max; neither pointwise
  implication holds: (H1) ⇏ (H2) and (H2) ⇏ (H1) — 2026-09-01 erratum to B6/F32,
  queued F37);
  equivalent single form: the envelope `Γ(r) ≤ min(Γ₀, r‖u‖_∞)` attained within
  a constant at its corner ⟺ **`β_v = γ` τ-uniformly** = the top endpoint of
  A2's unanalysed middle limb;
- chain facts: 4 anchor-touch sites, 1 irreducible (zoom-centre selection); all
  five √42 constants anchor-inherited, chain constant-agnostic (any τ-uniform
  `c` substitutes verbatim); target partition (T1) tie face scope-free /
  (T2) `B2∩{β_v=γ}` undefined in Scope B / (T3) `B2∩{β_v<γ}` empty in Scope A
  only on the `ρ_T = γ` sub-branch (2026-09-01 erratum, queued F38: on `ρ_T > γ`
  the amplitude corollary supplies (H1), not (H2), and (T3)-emptiness is not
  established), never claimed in Scope B — frontier lines need the "Γ-saturated"
  qualifier;
- **new debt (C5/F31)**: (N-Γ)'s printed discharge route is not supplied by the
  anchor on the `ρ_T > γ` sub-branch, even in Scope A.

**FREEZE REVIEW ROUND 2 is EXECUTED** (2026-08-21, user's amended adjudication
— F21/F29/F31/F33/C6 amended, rest adopted as proposed; master record
`docs/gates/FREEZE_REVIEW_2_2026-08-21.md` + annotation **B1–B14** appended to
the kill table; 3-lens audit run before commit, all ERRORs fixed — incl. the
F26 open-question omission, the (E⁺)-gloss conflation, the (T-c) label
binding, and the round-1 §5 supersession):

- **the map's kill claim is narrowed to accuracy (F33/B2)**: frontier replaced
  — "Scope-A quasi-static = B2; **its Γ-saturated realization is the target of
  R-B2′ [C]**"; the Scope-A gate is the **exhaustiveness step**, not the zoom;
  target partition (T1) tie face scope-free / (T2) `B2∩{β_v=γ}` — machinery
  scope-free granted membership, undefined in Scope B / (T3) `β_v<γ` empty in
  Scope A (narrows A2's debt there to the endpoint), never claimed in Scope B
  (2026-09-01 erratum, queued F38: the Scope-A emptiness/narrowing holds only on
  `ρ_T = γ`);
- **(N-Γ) split (F31/B11)**: tie face / `ρ_T = γ` → [C-dict]; `ρ_T > γ` →
  **[C], discharge unsupplied** (blanket [C-dict] tags in A15/A16/round-1 §5
  superseded);
- **(ANCH) → (ANCH-κ)** renamed (B12); **`β_v` legend** = τ-uniform corner
  attainment, not bare exponent equality (B13); **fork-(c) frozen** = unlisted
  ∧ independent ∧ irreducible Scope-A input — does not fire (B14/C6);
- Scope B frozen: **B2 UNKILLED**; (SB-ANCH) = (H1)∧(H2) with the canonical
  open question printed verbatim (B6); the **non-transplant rider**
  ((SB-ANCH) alone does not port R-B2′ — labelled-region/exhaustiveness
  separate) printed three times; trigger (T-c) OPEN with re-check condition
  (B5); DVEP recording corrected (B3); gate verdict sentence patched with the
  `A_NS` qualifier (B4).

**The commissioned Stage-9 decision is EXECUTED and DECIDED** (2026-08-23, same day;
master record `docs/gates/BH_BETAV_ENDPOINT_PINNING_2026-08-23.md`; the user
explicitly commissioned the proof search after the selection):

> **RULING: `YES (CONSISTENT)`.** The middle limb `M = B2 ∩ {β_v ∈ (α,γ)}` (sub-core
> Γ-saturation with corner attainment failing) **is consistent with the conjunction of
> the frozen scope-free rows.** Scope-free exponent/region arithmetic does **not** pin
> `β_v` to `{β_v ≤ α} ∪ {β_v = γ, τ-uniform}`. Certificate conditionality: **NONE**
> (K4′ not consumed, so no `[(E⁺)+(P)]` print is owed).

- **Method**: 1 statement fixer → 4 independent pin provers (Γ-saturation structure /
  budgets / ancient-limit zoom / covering-and-combinatorics) → 3 witness builders →
  witness breaker + pin breaker + location-premise auditor → adjudicator, all reading
  the frozen sources first-hand. **All four pin attempts returned `PIN_FAILED`**; the
  pin breaker confirmed none was abandoned prematurely.
- **Witness `W★`** (exponent bookkeeping, **not** a solution): `γ = 3/5`, `α = 9/20`,
  `β_v = 1/2`; region C `(9/20, 9/20, 27/20, 12/20, 8/20)` = amplitude and `L³` carrier,
  **not** Γ-saturated; region S `(1/2, 1/2, 3/2, 1/2, 1/2)` = Γ-saturated sub-core; both
  in the **printed blob shape** only; realized by one circulation field
  `Γ(r,t) = Γ₀·min((r/τ^{1/2})^k, τ^{1/2}/r)`, `k > 1`. Every frozen row passes at its
  own evaluation radius, the mandatory `τ^{α−γ}` misfire check is performed and passed,
  and **the witness family projects onto ALL of `S_blob`** — the pin fails at every
  surviving exponent pair, not at one point.
- **Structural reason**: the frozen rows contain **no statement that LOCATES
  Γ-saturation**. Each is neutral or one-sided-monotone in `β_v` (Γ-max bounds `r` above
  never below; the envelope bounds `r_sat` only below; K9 is existential in the region,
  giving only a floor; K5 is monotone-relaxed by shrinking the structure and cannot cut a
  Γ-saturated region at any scale; K6 acts on the designated carrier; [D2]/A3 is a
  region-count floor that `M` meets constructively; K3's cover is monotone under added
  regions; K11 mentions only `(γ,α)`). Such a conjunction **cannot carve out the open
  interval `(α,γ)` while admitting both endpoints**.
- **The pin's two horns are exactly the two inputs the corpus removed from Scope B**:
  K9's razor location premise `r ≍ ℓ` (demoted by P6/A1/A2 — using it *is* the recorded
  misfire, so the mandatory check fires **against** the pin; and even granted in full it
  does not pin, because an enstrophy-free Γ plateau on `[τ^{β_v}, τ^α]` satisfies
  `σ_core = α` with `β_v > α`), and the **Scope-A amplitude corollary** (which is why
  `(T3)` is empty in Scope A on the `ρ_T = γ` sub-branch — 2026-09-01 erratum, queued
  F38 — granting it is a **class change**, not a condition, which is why the verdict
  is `YES` and not `PIN_CONDITIONAL`).
- **NAMED GAP — one new object, `(Γ-DEP)`** (*intra-core circulation depletion*;
  genuinely new, exists nowhere in the corpus at any scope):
  ∃ τ-uniform `c′ ∈ (0,1)`, `δ > 0` with
  `sup_{dist(x,axis) ≤ δτ^{α}} |Γ(x,t)| < c′Γ₀` near `T*` *(operative form since
  2026-09-01: **(Γ-DEP)_fld** with `c_* ∈ (0, c₀)` — decision-record erratum E5)*.
  It is sufficient *(the further claims "minimal" and "no third route" are
  **withdrawn** — decision-record erratum E1 / round-3 C0: an outright (SB-ANCH)
  proof and a memberwise dichotomy are the other recorded closure shapes)*.
  **(SB-ANCH) cannot serve as a premise**: B6+B13 give
  `(SB-ANCH) ⟺ {β_v = γ, τ-uniform}`, so it **is** the other horn — a pin conditional on
  its own conclusion. **V1 is unpromoted and, checked at source, is the `C/r` KNSS-type
  Liouville family, not a viscous cutoff — its hypothesis fails on `W★`, so it is inert
  even if promoted.** Granting the two strongest unavailable inputs *simultaneously*
  (unprinted per-region K11 + a viscous cutoff) yields `β_v = 1/2` exactly, still
  strictly inside the limb whenever `α < 1/2 < γ` — which `W★` is.
- **NOT decided** (printed in the record): exponent consistency is **not** existence —
  `W★` is bookkeeping, not a flow, and no blow-up and no Clay claim is made or implied;
  realizability is undecided (the single-time coexistence / one-pressure debt is
  inherited, not discharged); Scope A is untouched (`(T3)` stays empty there on
  `ρ_T = γ`; the blanket emptiness carries the 2026-09-01 F38 erratum);
  (SB-ANCH) itself is undecided; all marginal/log/sub-polynomial faces are recorded
  out-of-vocabulary, never adjudicated.
- **Record-only**: A2's middle-limb debt is **partially discharged in one direction
  only** (the NO side is closed; the debt as a whole is not). Proposals P1–P7 — including
  the two new true statements `{β_v < γ} = ¬(SB-ANCH)` exactly, and sup-swirl-poverty on
  all of `{β_v < γ}` (generalizing the anchor audit's (T3) note from `β_v = α` to every
  `β_v < γ`) — await the **next user-adjudicated freeze review**. Nothing is applied.

Historical note on authority: round-2 §6 reserved the next branch to the **user's
choice** with nothing commissioned; that slot is where this choice landed, and the
authority was the user's dated instruction — first to select, then to execute.

**The Scope-B `β_v` endpoint-pinning decision theorem** —
`docs/gates/STAGE9_DECISION_SELECTION_2026-08-23.md` (full amended statement,
kill/survive criterion, failcase audit, runner-up rejections, and the standing
obligations inherited by the task). Shape: for Scope-B class **B2** with `O(1)`
non-evanescent circulation and no Scope-A hypothesis, is the middle limb
`M` (sub-core Γ-saturation with corner attainment failing — in the power-law
vocabulary `β_v ∈ (α, γ)`) **CONSISTENT** with the conjunction of the frozen
scope-free rows (Γ-max, K3, K6+[D2]/A3, K9 at the correct radius, K11, K4‴ [D],
K4′ [C on (E⁺)+(P)]) — or does scope-free exponent arithmetic **PIN** `β_v` to
`{β_v ≤ α} ∪ {β_v = γ, τ-uniform}`?

- **NO (pinned)** kills the anchorless intermediate-saturation escape channel and
  splits the sole unkilled class into two named attackable structures.
- **YES (consistent)** certifies the first genuinely new Scope-B survival class
  since the corridor and shows (SB-ANCH) evadable in one specific mode.
- **Record-only**: any A2 discharge or new survival row is a *proposal* for the
  next user-adjudicated freeze review, never applied unilaterally. No numerics,
  no new ansatz, no profile discovery, no CAP trigger, no in-house Liouville.
- Failcase battery: **SURVIVES in amended form** (the one FAIL was wording
  fidelity — K4′ mis-glossed and its `[C on (E⁺)+(P)]` tags dropped; repaired).

Lane re-audit (three independent analysts, 2026-08-23): the BH / small-swirl /
localized-steady-Euler-degeneration / Type-II-window / K12 lane is still **BEST**,
argued not assumed — K2 forces Type II, K11 + the wedge force quasi-static BH
cores, and the registry's competing Monster/conveyor lane (alive-but-unproven, no
ARCH-KILL / no PDE-KILL 2026-08-10) lands at `γ = 5/9`–`2/3`, i.e. **inside the
same frozen window**, so it is a candidate mechanism within this frame, not a
replacement. The standing 2026-08-19 reopen clause has fired but its payload
pointer (quantitative rigidity rate / K12) is **stale and consumed** — superseded
through (★) → (★_geo) → geometry gate (closed, θ = 1 sharp); its successor on the
current frontier is exactly the (SB-ANCH)/`β_v` complex commissioned above.

Literature watch (June–August 2026): **Seregin arXiv:2606.29468** (28 Jun 2026)
generalizes the frozen `γ+α = 1` edge to log-corrected families and again reduces
exclusion to **open** Liouville theorems for ancient Euler solutions in scaled-energy
classes — a mandatory row-(i) update **queued for the next freeze review** (not a
blocker for the commissioned task). Peralta-Salas–Slobodeanu arXiv:2606.13462
assumes localizability, so **trigger (T-c) stays OPEN and B5 does not fire**;
Ionescu–Jia–Palasek arXiv:2606.07501 is on the non-uniqueness axis with
self-similar profiles — logged, no frozen row touched. Explicit null on any
discharge of (OO) or of the KNSS / CSTY / Lei–Zhang / Chen–Fang–Zhang rows.

Still deliberately deferred: K8/K10 on multi-region tuples; coexistence /
one-pressure vocabulary limit; Jiu–Xin body (paywalled; CLV surrogate recorded);
separatrix continuation lemma; ζ-averaging / K12″; the eikonal/localizability
necessity question (research-level, CAP-adjacent, watch only); the Seregin-class
ancient-Euler Liouville problem (**the natural successor decision after this
one**); and all optional formal refinements (glued maximal trajectory `u*`,
interface adapters — not blockers).

**The Stage-9 readiness pass is complete — Gates A/B/C PASS, formal plumbing STOPPED**
(2026-08-23; `Formal/R3DecodedVelocityRealness.lean`, `Formal/R3SchwartzInitialData.lean`,
`Formal/R3SchwartzDivergence.lean`; audit record
`docs/formal/STAGE9_READINESS_AUDIT_2026-08-23.md`):

- **Task A — the named cheapest Gate-A gap is CLOSED.** The decoder symbol
  `J⁻³ = (1+‖ξ‖²)^(-3/2)` is real and even, so the **existing** generic multiplier theorem
  `r3L2Conj_of_fourier_realEven` yields `r3L2Conj_r3H3ToL2Operator` and
  `isR3RealVelocity_r3H3ToL2Operator`; composed with the unconditional coordinate-level
  realness `IsR3EndpointSafeProjectedMildSolutionOn.isR3RealVelocity` this gives
  `r3EndpointSafeProjectedMild_isR3RealVelocity_decoded`: along **every** mild solution
  with physically real initial coordinate, the decoded velocity `U t` — the field in the NS
  capstone — is physically real at every certified time. No new reality framework, no
  classical `C^∞` upgrade, no pointwise representative theorem. The theorem is **actually
  consumed** by the Task-B entry capstone.
- **Task B — the concrete admissible initial-data adapter is CLOSED (edge 3-adapter).**
  `IsR3AdmissibleSchwartzDatum φ` = (conjugation fixed point) ∧ (`ξ·𝓕φ(ξ) = 0` for every
  `ξ`), and `isR3AdmissibleSchwartzDatum_iff` proves this is **exactly** "real and
  classically divergence-free" — the equivalence of the two divergence formulations on the
  Schwartz core is proved **in both directions** in `Formal/R3SchwartzDivergence.lean` via
  the transfer identity `𝓕(∑ᵢ∂ᵢφᵢ)(ξ) = 2πi·(ξ·𝓕φ(ξ))` and injectivity of the Schwartz
  Fourier transform. `r3H3ToL2Operator_r3SchwartzToHsCLM` gives **decode ∘ encode =
  identity** at order three (`r3H3ToL2Operator (r3SchwartzToHsCLM 3 φ) = φ.toLp 2` — the
  correct direction). `.encode_mem_solenoidal` discharges the capstone's solenoidal
  hypothesis; `.smooth`, `.decay`, `.classicalDivergence`, `r3SchwartzConjCLM_eq_self_iff`,
  `r3Schwartz_finiteEnergy` certify the remaining Gate-B properties **for the same datum**.
  Entry capstone `r3AdmissibleSchwartzDatum_navierStokes`.
  **Non-vacuity shipped**: `exists_isR3AdmissibleSchwartzDatum_ne_zero` — the explicit
  **nonzero** datum `𝓕⁻F` with `F(ξ) = i·b(ξ)(ξ₁e₀ − ξ₀e₁)`, `b` the existing plateau bump
  (`ξ·F ≡ 0` identically; `F` reflected-conjugation-fixed since `b` is real and even; `F ≠ 0`
  at `ξ* = (0,1/2,0)` where `b = 1` and the first component is `i/2`).
- **No `H³ ⇒ C^∞` and no `H³ ⇒` rapid decay** is proved, claimed, or used anywhere — that
  implication is false and the adapter runs the other way. **Edge 3 *proper* stays OPEN**
  and is recorded `NON-BLOCKING FOR STAGE 9`.
- **Gate C** is instantiation-only and is now *consumed*
  (`r3AdmissibleSchwartzDatum_blowup_dichotomy`); no maximal-trajectory packaging built.
- **`edge 4-uniform: DEFERRED / NON-BLOCKING FOR STAGE 9`** — pointwise-in-time finite
  energy suffices for readiness; no uniform bound, no energy inequality, no dissipation
  identity was built.

**Exact semantic strength of the certified Navier–Stokes statement (unchanged by this
pass):** componentwise in `𝓢'(R³,ℂ)` in space; strong `L²`-valued derivative in time;
**interior** times `Ioo 0 T` of a **local** certified horizon (no `t = 0`, no `t = T`, no
global time); pressure = the edge-2a Helmholtz witness, determined up to additive harmonic
terms, no regularity or decay claimed; `Δ` and `(U·∇)U` identified by theorem, not by
naming. **Not** a classical pointwise solution.

**Remaining non-blocking formal gaps:** classical `C^∞` semantics; endpoint derivatives;
global time; uniform-in-time energy / energy inequality; pressure regularity; canonical
maximal trajectory `u*`; edge 3 proper; edge 5 (Clay breakdown transfer and official
quantifier packaging). Per the stop rule **none of these may be worked on for
completeness** — only when a concrete Stage-9 theorem consumes one.

**Research-side freeze: UNCHANGED** (round 2, 2026-08-21). This pass commissioned the next
research question; it answered none.

The closed layers are statements on the Bessel-coordinate carrier (complex, and real via
the conjugation gate) plus the Clay semantic-promotion edges closed so far (coordinate
incompressibility 1a/1b, decoder bridge 3a/3b, generic Helmholtz pressure reconstruction
2a, convection source identification 2b-i, momentum equation 2b-ii.a/2b-ii.b, initial-data
adapter 3-adapter). Unconditional uniqueness and the continuation dichotomy are closed at
the coordinate level; **no Clay statement is available yet** — edges 3 proper, 4-uniform
and 5 remain open (all recorded non-blocking or deferred).

## 2026-09-01 mathematical audit pass (erratum layer; record-only for the map)

Commissioned by the user's 2026-09-01 instruction ("数学的におかしい部分があれば直して",
then continue). Method: 8 independent finders (decision-doc deep audit / frozen map /
2026-08-20 layer / 2026-08-21 layer / summary fidelity / Lean-source cross-check /
independent exponent recomputation / formal status docs) → dedup → adversarial
verification (majority-refute, up to 3 lenses per finding) → synthesis. 23 raw → 15
confirmed (2 major, 7 minor, 6 nit). Repair convention: frozen `docs/gates/` records
get **appended errata only**; kill-table corrections are **queued as F37–F43** for the
round-3 user-adjudicated freeze review (nothing applied to a row or annotation); live
docs repaired in place.

The two major findings (both in `BH_RB2_ANCHOR_AUDIT_2026-08-21.md`, executed into
kill-table B6/B2):

- **F37**: B6's clause "`(H2) ⟹ (H1)`" is false once the distance clause is deleted —
  neither pointwise implication holds; only the conjunction `(H1) ∧ (H2)` ⟺ τ-uniform
  corner attainment (`β_v = γ`, B13) is true. Nothing downstream consumes the false
  direction; no ruling moves.
- **F38**: "(T3) `B2 ∩ {β_v < γ}` empty in Scope A by the amplitude corollary" is
  unproved as cited on the `ρ_T > γ` sub-branch (the corollary supplies (H1) and only
  **caps** `Γ(L)` — F31's own direction; `Γ_L ≍ Γ₀τ^{ρ_T−γ} → 0` there). Established
  only on `ρ_T = γ`. Downstream restatements in the β_v decision record, the selection
  record, and this file carry erratum markers.

Minor/nit errata (appended at each source; queue items in parentheses): Seregin K10
edge endpoint `γ = 3/5` outside the class (F39); S_ring K8-arm strictness (F40);
S_ring missing the K11 clause — adjudication requested (F41); "lifetime `1` fails
everywhere by K11" is exactly-marginal at `ρ = 1/2` on the `γ+α = 1` edge (F42, plus
origin errata in the neck-budget and COH-winding docs); the COH-winding midrange
inequality silently drops its `∫T4` and viscous Γ-defect terms (F43); (Γ-DEP)
necessity/"no third route" overstated — sufficiency stands, an outright (SB-ANCH)
proof is the other admissible closure shape (β_v decision erratum E1); (Γ-DEP)
"In words" gloss weaker than its formula (E2); θ_coh fork-(β) provenance (E3);
selection record's "answered `inf s = 0`" was [C]-conditional, not settled;
survival-map [H2] is a limsup statement, not a full limit; HANDOFF window
transcription drift (`α ∈ (…)` → `max(…) ≤ α < γ`, repaired in place); pressure
ambiguity class is **additive constants** under the gradient identity, not general
harmonic terms (STATUS doc + `Formal/R3HelmholtzPressure.lean` docstring — comment
only, no proof touched).

**Unchanged**: every Lean theorem and its axiom audit; the `YES (CONSISTENT)` ruling,
`W★`, and (Γ-DEP) sufficiency; all frozen verdicts (BH YELLOW-RED · B2 UNKILLED in
Scope B · (T-c) OPEN · no CAP trigger · no Clay claim). The round-3 freeze review
agenda was **P1–P7 + Seregin row-(i) + F37–F43** — executed the same day (next
section).

## 2026-09-01 freeze review round 3 (EXECUTED)

Master record `docs/gates/FREEZE_REVIEW_3_2026-09-01.md`; kill-table annotation
block **C0–C14** + the **post-round-3 frontier** (supersedes round 2's closing
block). Adjudication authority: the user's dated 2026-09-01 instruction. Summary:

- **C0 (standing policy, user-directed):** (Γ-DEP) is cited as **sufficient only**;
  the recorded closure shapes for the middle limb are (Γ-DEP) / an outright
  (SB-ANCH) proof (never as a premise) / a memberwise dichotomy
  `(Γ-DEP) ∨ (SB-ANCH)` — no exclusivity claim. "Unique closer" / "no third route"
  retired from citation.
- **F37–F43 all ADOPTED** (C1–C7); F41 in option (a) — `S_ring` gains `γ + α ≥ 1`.
- **P1–P7 all ADOPTED** (C8–C14); P1/P2/P3 amended at adjudication (P1 for C0;
  P2/P3 for F38-consistency and C0 — their drafted texts contradicted the same-day
  F38 re-scoping and the sufficiency-only policy).
- **Seregin row-(i) ADOPTED** (C14): arXiv:2606.29468's log-corrected families add
  conditional pressure **on the OOV faces only** — a scope annotation, not a new
  cut; **[V?] full-text verification debt named** before any chain may consume it.
- **Frontier re-fixed uniquely:** Scope-A exhaustiveness (and hence the middle-limb
  endpoint-narrowing there) holds **only on `ρ_T = γ`**; on `ρ_T > γ`,
  (T3)-emptiness is **not established even in Scope A**. Scope B: B2 UNKILLED;
  (SB-ANCH) a genuine conjunction (neither clause implies the other); middle limb
  row-compliant on all of `S_blob`; `{β_v < γ} = ¬(SB-ANCH)` with sup-swirl-poverty
  throughout. BH YELLOW-RED · (T-c) OPEN · no CAP trigger · no Clay claim.
- **(EXT-ΓDEP-1) IMPORTED the same day** (round-3 record §8;
  `docs/gates/EXT_GAMMADEP_DECISION_2026-09-01.md` — two external documents
  verbatim + in-repo audit, **PASS at snapshot level**, every derivable claim
  recomputed). Content: `Γ-DEP = UNDERDETERMINED`; an actual smooth / compactly
  supported / axisymmetric / divergence-free / axis-regular counterprofile
  (`Γ_τ = mΓ₀χ(r/τ^β)η((z−z*)/τ^β)`, `c₀ < m < 1`, plus a `ψ₁`-streamfunction
  poloidal blob) realizing the middle limb within every frozen budget — **the
  static route to (Γ-DEP) is closed: any proof must consume the NS time
  evolution**; the operative field statement is now **(Γ-DEP)_fld**
  (`c_* ∈ (0, c₀)` — fixes the 08-23 print's vacuity gap); **(Γ-OSC)** (τ-uniform
  oscillation contraction at core scale) is *the most direct identified
  sufficient condition* — `(Γ-OSC) ⟹ (Γ-DEP)_fld` verified, converse/exclusivity
  unproved (C0-consistent hygiene); the counterprofile is a **standing test
  case** for every future Γ-depletion hypothesis. Named debts: D-1 [V?]
  Ożański–Palasek citations; D-2 bare-drift falsity risk (generic supercritical
  divergence-free drifts can defeat parabolic continuity — the decision must name
  the NS-specific structure it consumes); D-3 — **identified and triaged
  2026-09-02** (arXiv:2606.07869v1, claiming unconditional
  axisymmetric-with-swirl global regularity; first-hand read + adversarial
  adjudication: load-bearing gaps G1a/G1b/G2 CONFIRMED at the variational core
  and exhaustion layer; correctness NOT ESTABLISHED; consumed by nothing; no CAP
  fire; watch triggers recorded — `docs/gates/D3_TRIAGE_2606_07869_2026-09-02.md`).
- **Final next-decision verdict (round-3 §6 + §8): the Γ-OSC feasibility
  decision is commissioning-ready** — the reduced form: extract the weakest
  quantitative drift condition for `osc_{Q_{θR}}Γ ≤ q·osc_{Q_R}Γ` τ-uniformly at
  `R = τ^α` from known drift–diffusion / boundary-regularity theorems; verify
  both directions against frozen B2 (derivable? or violated by an explicit
  frozen-compatible smooth profile?); verdict `IMPLIED / VIOLATED /
  UNDERDETERMINED`; **no new exponent restrictions as substitutes**. The core
  question: does genuine NS structure beat the generic large-drift obstruction
  `R‖u‖ ≍ τ^{α−γ} → ∞`? **Registered termination rule:** continue past this
  decision only on IMPLIED (or a partial IMPLIED naming the consumed NS
  structure); VIOLATED ⟹ the Γ-depletion lane's expected value collapses
  (end/pivot justified); a second consecutive UNDERDETERMINED ⟹ the BH branch
  ends (pivot: the `SPEC.md` numerical candidate program, or literature-level
  Seregin watch). Commissioning is a user act; nothing started.

## Latest Lean verification

```text
runner: local Windows (Git Bash) process via Elan, scripts/lean-ci-local.sh
revision: working tree on main after 9928b21 (2026-09-01 audit pass; only Lean change:
  Formal/R3HelmholtzPressure.lean docstring — comment-only, no proof or statement touched)
toolchain: leanprover/lean4:v4.32.1
dependency manifest: committed lake-manifest.json; mathlib per lake-manifest.json
full scope: scripts/lean-ci-local.sh (pinned source scan + Formal.+ default target)
  — exit 0, pass (8769 jobs); remaining warnings are cache replays of pre-existing
  lints in untouched modules
source scan: pinned sorry/admit/axiom/opaque scan over Formal/ — clean
axiom scope: Formal.AxiomAudit — pass; audited declarations depend only on propext,
  Classical.choice, Quot.sound (unchanged)
scope note: docs-layer erratum pass; no theorem added, removed, or restated
GitHub Actions: not invoked (quota exhausted; hosted runs banned; user directive
  2026-09-01: all Lean runs local from now on)
```

Previous gate (Stage-9 readiness pass, commit c805a06):

```text
runner: local Windows (Git Bash) process via Elan, scripts/lean-ci-local.sh
revision: working tree on main after 1b9cb0a
  (new: Formal/R3DecodedVelocityRealness.lean, Formal/R3SchwartzInitialData.lean,
   Formal/R3SchwartzDivergence.lean; extended: Formal/AxiomAudit.lean)
toolchain: leanprover/lean4:v4.32.1
dependency manifest: committed lake-manifest.json; mathlib per lake-manifest.json
target scope: lake build Formal.R3DecodedVelocityRealness / Formal.R3SchwartzInitialData /
  Formal.R3SchwartzDivergence / Formal.AxiomAudit — pass; all three new files: zero errors,
  zero warnings
full scope: scripts/lean-ci-local.sh (pinned source scan + Formal.+ default target)
  — exit 0, pass (8769 jobs)
source scan: pinned sorry/admit/axiom/opaque scan over Formal/ — clean
axiom scope: Formal.AxiomAudit — pass; all 277 audited declarations, including the
  26 new ones (5 realness-transport, 21 admissible-data/divergence/witness/Gate-C),
  depend only on propext, Classical.choice, Quot.sound
scope note: Stage-9 readiness PASS (Gates A/B/C). NS semantics unchanged: componentwise
  Schwartz' in space, strong L2 in time, interior local times, local horizon, pressure up
  to harmonic terms. Realness of the decoded field is now transported (Gate-A gap closed).
  Uniform-in-time energy, classical smoothness and global time remain unproved and are
  recorded non-blocking/deferred.
GitHub Actions: not invoked (quota exhausted; hosted runs banned)
```

Previous gate (edge 2b-ii.b + edge 4 pointwise half, commit 1b9cb0a):

```text
runner: local Windows (Git Bash) process via Elan
revision: working tree on main after 41b875d
  (new: Formal/R3NavierStokesEquation.lean, Formal/R3FiniteEnergy.lean;
   extended: Formal/AxiomAudit.lean)
toolchain: leanprover/lean4:v4.32.1
dependency manifest: committed lake-manifest.json; mathlib per lake-manifest.json
target scope: lake build Formal.R3NavierStokesEquation / Formal.R3FiniteEnergy /
  Formal.AxiomAudit — pass, no new warnings (both new files: zero errors, zero warnings)
full scope: lake build (Formal.+ default target) — pass (8766 jobs; remaining warnings
  are cache replays of pre-existing lints in untouched modules)
source scan: pinned sorry/admit/axiom/opaque scan over changed files — clean
axiom scope: Formal.AxiomAudit — pass; the eight new audited declarations
  (r3EndpointSafeProjectedMild_mem_solenoidal, postcomp_r3LerayL2Operator_eq,
   r3EndpointSafeProjectedMild_navierStokes,
   exists_r3EndpointSafeProjectedMild_navierStokes, integrable_norm_sq_r3L2,
   integral_norm_sq_r3L2, r3DecodedVelocity_finiteEnergy,
   r3MildDecodedVelocity_finiteEnergy)
  depend only on propext, Classical.choice, Quot.sound
scope note: edge 2b is now THEOREM-CLOSED in full (2b-i + 2b-ii.a + 2b-ii.b) and edge 4
  is PARTIAL (pointwise-in-time only). The NS equation semantics: componentwise Schwartz'
  in space, strong L2 in time, interior local times, complex carrier, pressure up to
  harmonic terms; realness of the decoded field is NOT transported (named cheapest
  Gate-A gap) -- AS OF THAT COMMIT ONLY; that gap is closed by the 2026-08-23 pass above;
  the uniform-in-time energy bound, classical smoothness, and global time remain unproved
GitHub Actions: not invoked (quota exhausted; hosted runs banned)
```

Previous gates: edge 1a at 8757 jobs (098803b); edge 1b at 8758 jobs (9f4f08e);
edge 3a at 8759 jobs (778eaa2); edge 3b at 8760 jobs (0403c06); edge 2a at 8761 jobs
(faa0f96); edge 2b-i at 8762 jobs (ec3517b, witness addendum 62a879b); 2b-ii.a
infrastructure at 8763 jobs (5ddce9c); 2b-ii.a assembly at 8764 jobs (41b875d) — all
their audited declarations standard-axioms-only.

Previous gate (maximal-continuation layer): full `Formal.+` pass at 8756 jobs, all
eight continuation-layer declarations standard-axioms-only (see git history).

## Runner protocol for the next proof

Use a conforming ChatGPT-accessible Lean runner when connected; otherwise use the tested local
Elan path above. In either case, preserve the same pinned-revision evidence contract.

For each candidate change, record:

```text
runner: <tool/provider>
revision: <commit SHA or exact candidate patch>
toolchain: <value from lean-toolchain>
scope: <target module or full gate>
result: <pass/fail>
diagnostics: <exact Lean error when failing>
```

Preferred iteration:

```text
smallest target
-> exact Lean diagnostic
-> minimal proof edit
-> same target again
-> full pinned gate after target is green
```

Do not use GitHub-hosted PR runs as the diagnostic loop.

## Nonclaims / guardrails

- no `sorry`;
- no `admit`;
- no new local `axiom`;
- no source-level `opaque` proof hiding;
- do not report candidate code as proved before a conforming pinned Lean verification accepts it;
- do not merge an ungreen mathematical PR;
- do not auto-merge unless the user explicitly asks;
- the completed map is a complex Bessel-coordinate extension; arbitrary-`H³` decoder equality with
  a separately defined distributional product is not yet proved;
- (superseded 2026-08-23) pressure reconstruction is closed (edge 2a, consumed by the NS
  capstone) and realness is closed at **both** levels — coordinate
  (`IsR3EndpointSafeProjectedMildSolutionOn.isR3RealVelocity`) and decoded
  (`r3EndpointSafeProjectedMild_isR3RealVelocity_decoded`); the two-space Duhamel contract
  and the ball-local mild existence theorem are supplied by the merged Duhamel/Picard
  layers and must not be re-proved;
- the proved `H² → H³` Stokes operator requires `ν > 0` and positive elapsed time; no bounded
  cross-space operator is supplied at `τ = 0` or `ν = 0`;
- interval integrability of `r3StokesH2H3TimeKernel` is a scalar-majorant theorem, not yet a proof
  that an endpoint-totalized operator-valued Duhamel integrand is strongly measurable or Bochner
  integrable;
- do not claim that the nonsmooth-at-zero Leray symbol maps Schwartz space to itself; the proved
  core comparison is in `L²` and tempered distributions;
- do not use the phantom Sobolev-order alias itself as an inclusion or smoothing theorem; the
  positive-time result is justified by its explicit multiplier and decoder theorems;
- the mild solution lives in the complex Bessel-coordinate carrier; realness is available
  but **conditional on real data** — for a general complex coordinate nothing is real, so do
  not describe the carrier itself as physical;
- `IsR3AdmissibleSchwartzDatum` is **exactly** "real and classically divergence-free
  Schwartz" (`isR3AdmissibleSchwartzDatum_iff`) and is **non-vacuous**
  (`exists_isR3AdmissibleSchwartzDatum_ne_zero`); it is an adapter for **one concrete
  class**, never a characterization of arbitrary `R3HsVelocity 3` — and **no `H³ ⇒ C^∞` or
  `H³ ⇒` rapid-decay implication exists anywhere in this repository** (it is false);
- finite energy means `∫‖U(t,x)‖²dx = ‖U t‖² < ∞` for the **physical decoded field** at each
  time; it is **not** the uniform-in-time Clay predicate (Fefferman (A)) and there is no
  energy inequality and no dissipation identity;
- the certified Navier–Stokes statement is componentwise in `𝓢'` in space and strong `L²` in
  time, at **interior** times of a **local** horizon; it is **not** a classical pointwise
  solution, says nothing about `t = 0` or `t = T`, and says nothing global;
- `IsR3RealVelocity` / `IsR3ConjugateSymmetricVelocity` are related through the Plancherel
  `L²` Fourier transform; every concrete operator of the mild theory is
  conjugation-equivariant and realness-preserving; the local mild solution is physically
  real for physically real data — now **unconditionally** (every mild solution with real
  datum is pointwise real, no ball hypothesis). Still missing: the glued maximal
  trajectory with pointwise blow-up (the certified-horizon dichotomy IS formalized),
  pressure reconstruction, and any Clay statement;
- uniqueness is now **unrestricted** on a common horizon
  (`r3EndpointSafeProjectedMildSolution_unique`); the ball-uniqueness clauses of the older
  existence theorems remain valid but are superseded;
- the horizon is explicit (`r3MildLifespan nu ‖u₀‖ = (δ/(1+(π√ν)⁻¹+δ))²`, positive and
  `≤ 1`) and the continuation criterion is available in blow-up–dichotomy form over the
  certified-horizon set; the canonical glued maximal trajectory and its pointwise
  `limsup ‖u* t‖ = ∞` restatement are **not** yet constructed — do not cite the dichotomy
  as a trajectory-level statement, and do not present any of this as global regularity;
- do not spend hosted Actions as an interactive compiler while quota is scarce/exhausted.

## Minimal continuation prompt

`ns-mns2-flowmap-bridge を resume protocol どおり確認して続きから。

**形式側は完了・停止中**: Stage-9 readiness = PASS(docs/formal/STAGE9_READINESS_AUDIT_2026-08-23.md)。
実・divergence-free・有限エネルギーの Schwartz 初期データから、認証された局所 mild 解の decoded 物理速度が
**実際の incompressible Navier–Stokes 方程式**(成分別 𝓢' 空間 × 強 L² 時間微分、局所地平線の内部時刻、
明示的 Helmholtz 圧力、分布的 ∇·U = 0)を満たすところまで機械検証済み
(`r3AdmissibleSchwartzDatum_navierStokes` → `r3EndpointSafeProjectedMild_navierStokes`)。
local existence / 無制限一意性 / 明示的 lifespan / restart / concat / continuation / blow-up dichotomy も閉鎖済み。
**stop rule により、これ以上の formal plumbing はしない** — uniform energy、古典正則性、端点微分、
maximal trajectory u*、edge 3 proper、edge 5 Clay packaging は、Stage-9 の具体定理が要求するまで着手禁止。

**最初の Stage-9 decision は実行・決着済み**: docs/gates/BH_BETAV_ENDPOINT_PINNING_2026-08-23.md
= **`YES (CONSISTENT)`** — 凍結 scope-free 行は Γ 飽和の位置を決めないので中間肢
`β_v ∈ (α,γ)` を pin できない。明示 witness `W★`(γ=3/5, α=9/20, β_v=1/2、印字済み blob 形状のみ、
単一の Γ プロファイル `Γ₀·min((r/τ^{1/2})^k, τ^{1/2}/r)` で実現)が全行を各自の半径で通過し、
族は `S_blob` 全体に射影する。閉じ手は3形(round-3 **C0**、必要性表現は引用禁止):
**(Γ-DEP)[十分条件のみ]**/(SB-ANCH) の outright 証明(**前提としては**循環で不可)/
memberwise 二分法 `(Γ-DEP) ∨ (SB-ANCH)`。operative な field-level 文は **(Γ-DEP)_fld**
(`c_* ∈ (0, c₀)`、E5/EXT §B.5 — 08-23 印字の `c′ ∈ (0,1)` は vacuity ギャップにつき超越)。V1 は
未昇格かつ(出典確認済み)C/r Liouville 族であって粘性カットオフではなく、`W★` 上で仮説が破れる
ため昇格しても不活性。**指数算術の無矛盾性は NS 解の存在ではない**(coexistence/one-pressure
債務は継承。blow-up も Clay も一切主張しない)。A2 の中間肢債務は **NO 側のみ** 閉じ、
提案 P1–P7 は **round 3(2026-09-01)で全裁定・執行済み**(C8–C14; P1/P2/P3 は修正裁定)。

参考(元の commissioning 記録) = **Scope-B β_v endpoint-pinning decision**
(Scope-B の B2 クラス、O(1) 非消滅循環、Scope-A 仮説なしで、中間肢 M(sub-core Γ 飽和 かつ
corner attainment 不成立 = 冪則語彙で β_v ∈ (α,γ))が凍結 scope-free 行の連言と **CONSISTENT** か、
それとも scope-free な指数算術が β_v を {β_v ≤ α} ∪ {β_v = γ, τ-uniform} に **PIN** するか)。
NO なら anchorless intermediate-saturation escape channel が死に、唯一未 kill のクラスが2つの
名前付き攻撃対象に分裂。YES なら corridor 以来初の新 Scope-B 生存クラスが確定。
**record-only**: A2 債務の放電も新 survival 行も、次のユーザー裁定 freeze review への *提案* として書くだけ。
必ず継承する義務: K4′ を使う鎖には必ず [(E⁺)+(P)] を印字(条件付き [C] であり scope-free pin ではない)、
P6 残余 [V?] と Chen–Fang–Zhang endpoint 可容性は verification obligation として明示、
K9 適用ごとに τ^{α−γ} misfire チェック、marginal/log/sub-polynomial/循環消滅面は
out-of-vocabulary として記録(辞書を発明しない)。

**研究側 freeze の現在形 = round 3(2026-09-01 執行済み)**: 監査 F37–F43・提案 P1–P7・
Seregin row-(i) をすべて個別裁定(全 ADOPT、P2/P3 は F38 整合と C0 のため修正)。
kill table annotation **C0–C14** + **post-round-3 frontier** が現行(round-2 block を supersede):
Scope-A exhaustiveness は `ρ_T = γ` 枝でのみ成立、`ρ_T > γ` では (T3) 空性は Scope A でも未確立;
Scope B は B2 UNKILLED、(SB-ANCH) = (H1)∧(H2) は真の連言(どちらの含意も不成立、C1/F37)。
**C0(恒久方針): (Γ-DEP) は十分条件としてのみ引用**(「唯一の閉じ手」「third route なし」は引用禁止)。
BH YELLOW-RED、(T-c) OPEN、CAP なし、Clay 主張なしは全て不変。

**外部 record (EXT-ΓDEP-1) は import 済み**(`docs/gates/EXT_GAMMADEP_DECISION_2026-09-01.md`、
逐語2文書+リポジトリ内監査 PASS): `Γ-DEP decision = UNDERDETERMINED`。headline no-go =
**snapshot レベル(smooth/div-free/finite-energy の単一時刻場)では (Γ-DEP) は決まらない —
証明は NS の時間発展を消費しなければならない**(counterprofile
`Γ_τ = mΓ₀χ(r/τ^β)η((z−z*)/τ^β)` + ψ₁ poloidal blob、frozen budget 全通過、恒久テストケース)。
operative 文は **(Γ-DEP)_fld**(`c_* ∈ (0, c₀)`)。**(Γ-OSC)**(core scale での τ-uniform
oscillation contraction)は「特定できた最も直接的な十分条件」— `(Γ-OSC) ⟹ (Γ-DEP)_fld` のみ確立。
debts: D-1 [V?] Ożański–Palasek 引用、D-2 bare-drift 反例リスク(一般 supercritical div-free drift
では parabolic continuity が破れ得る — decision は消費する NS 固有構造を明示せよ)、
D-3 は **2026-09-02 に特定・一次 triage 済み**(arXiv:2606.07869v1 =
axisym-with-swirl 無条件大域正則性主張。全文一次読解+敵対的検証で変分核心 G1a/G1b と
exhaustion 層 G2 の load-bearing gap を確定。正しさ未確立・どこにも不使用・CAP 不発火。
再点検トリガー付き master record = `docs/gates/D3_TRIAGE_2606_07869_2026-09-02.md`)。

**Γ-OSC feasibility decision は実行・決着済み(2026-09-02)= `VIOLATED`**
(`docs/gates/GAMMA_OSC_FEASIBILITY_2026-09-02.md`): frozen B2 は既知の十分 drift 条件を
**一つも** imply しない(implied 部分領域は `S_blob` 上で**正確に空**。sup / `L^∞_tL³` /
local-energy cap は forced-amplitude lemma により class 全体で `ν^{−1}τ^{−(γ−α)}`
— local-energy cap は自乗レート `ν^{−2}τ^{−2(γ−α)}` — で**強制発散**)。かつ frozen 両立の明示的 smooth div-free 族が両ラダーの**全最弱段**を
τ-uniform に破る(power 対 高々 double-log。既知ラダーは scale invariance で終端 —
SSŠZ/SVZ/Wu の反例床。multi-scale 逃げ道は `(ln N)^{−p}, p ≤ 1` 閾値で閉鎖)。
D-1・D-2 は放電済み。C0-clean: `VIOLATED ⇏ ¬(Γ-OSC)`、`⇏ ¬(Γ-DEP)` — 生き残りは
record §5.3 の non-rung NS 構造(既知定理なし)のみ。

**第4回 freeze review は実行・執行済み(2026-09-02)**
(`docs/gates/FREEZE_REVIEW_4_2026-09-02.md`; kill table annotation **D0–D7** +
Post-round-4 frontier が現行の唯一 operative frontier): P1–P6 全 ADOPT、Γ-OSC
`VIOLATED` 行は正確な machinery-closure scope で map に反映(D1)。
**BH / Γ-depletion branch は active lane として終了・PARK(D0)** — 必須の区別:
**「未解決」≠「既知機構の枯渇」**(B2 は UNKILLED のまま、中間肢と (Γ-OSC)/(Γ-DEP) は
open のまま。尽きたのは in-house の既知機構在庫であり、3層で裁定済み: 指数算術は pin
できない → snapshot 幾何は決められない → 既知の動的機構は届かない)。BH verdict は
park 時点で YELLOW-RED に凍結。un-park は登録トリガー経由の freeze review 裁定のみ。
**D-3 / Seregin は standing passive watch register に分離**
(`docs/gates/LITERATURE_WATCH_REGISTER_2026-09-02.md`, W-1〜W-4。トリガー発火は
次回 freeze review の議題化のみで、自動の再開・採用はない)。

**現在の active lane = SPEC.md の verified nonlinear finite-cylinder
axisymmetric-with-swirl numerical candidate program。次の作業 = milestone M-1**
(選定済み・未着手): **Hou 2022 の no-slip wall-vorticity boundary closure の実装+検証**
(`docs/reports/HOU_WALL_VORTICITY_BOUNDARY_AUDIT_2026-08-13.md` の記録済み blocker の
解消)。受け入れ条件 = 同監査文書の要件1–8(離散 `ψ₁=0` / `∂_rψ₁=0` / `ω₁=−∂_r²ψ₁` /
`u₁=0` at `r=1`、極条件、holomorphic tangent / adjoint 整合、壁集中 JVP・adjoint テスト、
壁残差を interior と分離した refinement)+ SPEC §8 の候補不変条件(項別残差・収束列・
reload hash)。**fail-closed stencil rule**: Hou 2022 (DOI 10.1007/s10208-022-09578-4)
とその引用方法論から production stencil を一次資料で確定する。確定できなければ
`alternative wall closure` とラベルして導出を印字(「Hou production reproduction /
late-state validation / resolved singular regime」ラベルは gate 全通過+stencil
provenance 確定まで禁止)。着手前 preflight: AGENTS.md の external exclusion registry /
equation audit 照合を evidence bundle に記録。M-1 は Hou 再現でも `R³` 結果でも
Clay 主張でもない(有限円柱は domain-transfer 定理なしに `R³` へ昇格しない)。

数値作業は **M-1 の scope 内でのみ**行う(SPEC.md §§3–8 の規約と AGENTS.md の MNS-2
numerical invariants / Hou wall-vorticity gate に厳密準拠)。park 済み BH branch への
in-house 作業・新 ansatz・profile discovery・CAP・in-house Liouville は行わない
(un-park は freeze review 裁定のみ)。GitHub Actions は一切使わない
(quota 枯渇、ローカル Elan の pinned gate = scripts/lean-ci-local.sh が evidence contract)。
docs は照合後 main に直接 push。古い会話より実コード・実 ledger を優先。`
