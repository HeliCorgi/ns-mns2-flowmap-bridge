# GPT-first repository workflow

This repository is expected to be developed primarily through repeated ChatGPT/GPT sessions. This document is the operational contract for resuming, changing, checking, and handing off work without relying on chat history.

## 1. Mandatory resume protocol

At the start of every new session, before proposing code or mathematics, read in this order:

1. `PROJECT_GOAL.md` — repository-level acceptance target;
2. `SPEC.md` — current physical/numerical research contract;
3. `AGENTS.md` — non-negotiable repository rules and claim hygiene;
4. `FORMAL_SCOPE.md` — current Lean theorem/claim boundary;
5. `HANDOFF.md` — short-form current frontier and next gate;
6. `docs/LEAN_CI_OPERATIONS.md` — how Lean verification is currently expected to run.

Then inspect GitHub:

7. current `main` HEAD;
8. current contents of the relevant files under `Formal/`;
9. open PRs, especially the newest mathematical or verification-related PR;
10. the newest Lean verification evidence associated with the relevant commit, preferring a ChatGPT-connected external Lean runner result and using GitHub-hosted CI only when it was deliberately run.

If no Lean result exists for the relevant commit/toolchain, mark the code as unverified. Do not infer proof validity from a stale CI result, an old conversation, or a similar-looking source file.

Do not treat an old conversation, old PR description, or stale handoff sentence as stronger evidence than the repository itself.

## 2. Source-of-truth hierarchy

Use the following hierarchy when sources disagree:

- official Clay/Fefferman statement and `PROJECT_GOAL.md` for the ultimate target;
- `SPEC.md` for the current physical/numerical track;
- `AGENTS.md` for repository-wide operating rules;
- current `main`, current `Formal/`, and current theorem statements for the actual formal frontier;
- `FORMAL_SCOPE.md` for a maintained summary of that frontier;
- `HANDOFF.md` for the latest continuation point;
- chat history only as auxiliary context.

If `HANDOFF.md` or `FORMAL_SCOPE.md` is stale, update it after checking the code rather than forcing the code to match the prose.

## 3. Mathematical change protocol

Before writing a new theorem or proof:

1. identify the exact target theorem or missing bridge;
2. identify which existing theorem/file should feed it;
3. check whether mathlib already contains the needed theorem or API;
4. state assumptions explicitly;
5. state what the result does **not** prove;
6. avoid introducing a semantic adapter when the missing item is really an analytic estimate or identification theorem.

Never silently replace a difficult equality by a suggestive analogy. In particular, ordinary pointwise convolution and an `L²`-valued Bochner convolution are not interchangeable unless an explicit representative/Fubini theorem identifies the concrete objects in question.

## 4. Lean proof discipline

Every GPT session must preserve the repository proof-hygiene rules:

- no `sorry`;
- no `admit`;
- no new local `axiom`;
- no source-level `opaque` used to hide a gap;
- prefer existing mathlib theorems to restating them as assumptions;
- keep theorem names, file names, parameter order, Fourier conventions, and norm conventions exact;
- never report a theorem as proved until Lean has accepted the relevant source under the pinned toolchain.

A successful targeted build is evidence only for that target and its dependency closure. A full repository gate remains a separate check.

## 5. Lean development workflow

The normal interactive compiler is a **ChatGPT-connected external Lean runner**, not GitHub Actions and not a required local Lean installation.

The external runner may be exposed through an API, MCP server, custom GPT Action, or another ChatGPT-accessible tool, but it must satisfy the verification contract in `docs/LEAN_CI_OPERATIONS.md`.

Preferred order while developing:

1. resolve the exact repository commit/branch being checked and read `lean-toolchain`, `lakefile.lean`, and `lake-manifest.json`;
2. send or synchronize the smallest relevant repository state to the external runner without changing the pinned dependency graph;
3. run the proof-hole/local-axiom/proof-hiding source scan;
4. build the smallest relevant target, for example the external-runner equivalent of:

   `bash scripts/lean-ci-local.sh Formal.R3SchwartzNormFieldL2`

5. feed the exact Lean diagnostics back into the same ChatGPT session and iterate on the proof until the targeted module is green;
6. after the targeted development is green, run the external-runner equivalent of the full gate:

   `bash scripts/lean-ci-local.sh`

7. record the runner, commit/ref, pinned toolchain, target/command, and result in the session handoff when the formal frontier changes;
8. use GitHub-hosted Actions only when an intentionally spent hosted status check or independent final confirmation is actually required.

A runner result is not valid evidence if it used a different repository revision, a different Lean/mathlib dependency graph, or an isolated snippet that omits required project dependencies.

If the current ChatGPT session has no external Lean runner connected, do **not** compensate by pushing trial commits to consume GitHub Actions. Keep candidate code explicitly unverified until a conforming external runner, local reproduction, or deliberately approved hosted check accepts it.

Local Lean and self-hosted execution remain acceptable reproduction/fallback paths, but they are no longer the required normal interactive path.

See `docs/LEAN_CI_OPERATIONS.md` for the runner contract, evidence requirements, and fallbacks.

## 6. GitHub change protocol

For normal mathematical work:

- work on a feature branch;
- keep each PR focused on one analytic or formal bridge;
- do not merge an ungreen mathematical PR;
- do not auto-merge unless the user explicitly asks;
- include scope, claim, assumptions, nonclaims, runtime impact, and Lean verification state in the PR body;
- identify whether the accepted gate came from the external runner, local/self-hosted reproduction, or GitHub-hosted CI;
- avoid unrelated cleanup in a mathematical PR;
- do not modify workflow triggers casually.

Do not open or update a PR merely to obtain Lean diagnostics from GitHub Actions. During hosted-quota exhaustion, a branch may remain without a PR until the proof is externally verified and opening the PR is useful for review or integration.

For documentation-only maintenance while hosted CI is scarce, prefer a prepared branch without a PR if opening the PR would trigger an unnecessary required Lean build.

## 7. Verification cost policy

Treat GitHub-hosted Lean minutes as a scarce optional resource.

- The ChatGPT-connected external Lean runner is the preferred interactive verification path.
- Do not re-enable automatic full Lean builds on `main` pushes without explicit user approval.
- Do not use speculative PR commits as a remote REPL/compiler loop.
- Preserve caches on any runner where the cache does not weaken revision/toolchain identity.
- Prefer targeted builds during iteration and a full pinned gate only after the target is green.
- If hosted quota is exhausted, continue through the external runner or another explicitly identified non-hosted reproduction path rather than weakening the proof gate.
- A cache is only a performance optimization; Lean/Lake still determines what must be rebuilt.

## 8. Session-end handoff protocol

At the end of a substantial work session, update `HANDOFF.md` when the current frontier or verification state changed. The handoff should contain concrete symbols, not only prose.

Record:

- current `main` or relevant branch/PR;
- latest known Lean verification state;
- for the latest meaningful verification: runner/provider, exact commit/ref, pinned toolchain, target/full-gate scope, and pass/fail status;
- current target theorem;
- newly established theorem names and file names;
- exact remaining gate;
- known failed approaches that should not be repeated;
- whether any equality/estimate is still only a planned bridge;
- the next smallest Lean task.

Use a shape like:

```text
Current target:
  <exact smallest open theorem or construction>

Latest Lean verification:
  runner: <external runner / local / hosted>
  revision: <exact commit>
  scope: <target or full gate>
  result: <pass/fail>

Completed infrastructure:
  <exact theorem/file list>

Next analytic gate:
  <exact missing equality or estimate>

Do not assume:
  <important tempting but unproved identification>
```

`FORMAL_SCOPE.md` should be synchronized less frequently, when the theorem boundary materially changes. `HANDOFF.md` should be the lightweight file updated at ordinary milestones and whenever the verification mechanism/status materially changes.

## 9. Current formal-development invariant

Merged PR #79 explicitly closed the representative/Fubini identification for the two concrete H² scalar majorants, and merged PR #80 closed the Fourier-coordinate/H³ factor bookkeeping used by the current one-coordinate convection estimate.

Commit `6ecfcda51d74b456b538def2577c52a403a0ff88` closes the remaining finite `Fin 3`
packaging with an explicit nonnegative sum witness and proves both
`R3SchwartzConvectionTermSobolevEstimate 3` and
`R3SchwartzConvectionSobolevEstimate 3`. That commit passed the local pinned full gate.

Commit `5eb29848eea0529bf557c68a599e78317090f522` closes the next density and
bounded-extension gate. It proves `r3SchwartzToHsCLM_denseRange`, constructs

`r3ConvectionH3ToH2 : R3HsVelocity 3 →L[ℂ] R3HsVelocity 3 →L[ℂ] R3HsVelocity 2`,

and proves exact Schwartz-core agreement, order-two decoder agreement on
Schwartz inputs, the global bilinear norm bound, and uniqueness among
continuous complex-bilinear maps with those dense-core values. That exact
commit passed the local pinned full gate.

Commit `2127757807768709d1ac19a0ec6f760c48a973cc` closes the order-aware
`H²` Leray and projected-convection gate. It constructs the genuine bounded
`J⁻²` reconstruction `r3H2ToL2Operator`, proves exact order-two decoder and
physical-`L²` Leray commutation, and defines

`r3ProjectedConvectionH3ToH2 : R3HsVelocity 3 →L[ℂ] R3HsVelocity 3 →L[ℂ] R3HsVelocity 2`.

The new map has the inherited operator/pointwise norm bounds, its physical
`L²` reconstruction is solenoidal, and its decoder agrees on Schwartz inputs
with the existing literal `r3ProjectedSchwartzConvectionL2`. That exact commit
passed the local pinned source scan and full gate (8739 jobs), without GitHub
Actions.

Do not generalize these results beyond the exact proved objects. In particular, analogous
ordinary-convolution versus bundled-Bochner identifications elsewhere still require explicit
representative/Fubini results. The completed map is a result about the complex Bessel-coordinate
model; it does not identify its decoded value with a separately defined distributional product for
all `H³` inputs and does not construct the physical real-valued restriction.

`R3HsVelocity s` has the same underlying `L²` type for every order, with semantics supplied by the
order-dependent decoder. Never use that definitional equality to assert a physical `H³ → H²`
inclusion or an `H² → H³` smoothing bound.

The current near-term formal gate is positive-elapsed-time, positive-viscosity `H² → H³` Stokes
smoothing with multiplier `(1 + ‖ξ‖²)^(1/2) * exp(-(2π)² ν τ ‖ξ‖²)`, exact decoder and
Leray compatibility, an explicit `O(1 + (ν τ)^(-1/2))` (or sharper) bound, and local
time-integrability. No such bounded smoothing exists at `τ = 0` or `ν = 0`. The following gate
is a two-space Duhamel interface. The existing same-space `LerayProjectedQuadraticContract V`
cannot accept this two-space map without additional structure or a genuinely same-space estimate.

## 10. Minimal resume prompt

A short user prompt should be sufficient:

`@GitHub ns-mns2-flowmap-bridge を docs/GPT_WORKFLOW.md の resume protocol どおり確認して、最新 main/PR/Lean verification と HANDOFF.md を照合して続きから。Lean の反復検証は ChatGPT 接続の外部 runner を使い、GitHub Actions は明示的に必要な場合だけ使って。`
