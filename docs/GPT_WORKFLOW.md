# GPT-first repository workflow

This repository is expected to be developed primarily through repeated GPT/Codex sessions. This document is the operational contract for resuming, changing, checking, and handing off work without relying on chat history.

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
9. open PRs, especially the newest mathematical or CI PR;
10. the newest Lean CI result associated with the relevant head commit.

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

Never silently replace a difficult equality by a suggestive analogy. In particular, ordinary pointwise convolution and an `L²`-valued Bochner convolution are not interchangeable until an a.e. representative/Fubini identification is proved.

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

GitHub-hosted Actions are a scarce fallback resource, not the normal interactive compiler.

Preferred order while developing:

1. use local Lean with the pinned toolchain;
2. run the proof-hole/local-axiom scan;
3. build the smallest relevant target, for example:

   `bash scripts/lean-ci-local.sh Formal.R3SchwartzNormFieldL2`

4. iterate locally until the target is green;
5. run the local full gate:

   `bash scripts/lean-ci-local.sh`

6. only then use a GitHub PR check when a hosted or self-hosted status check is actually needed.

If the current ChatGPT execution environment has no Lean/Lake binary, do **not** use a series of trial PR commits merely to make GitHub Actions act as the compiler. Prefer a user/local/self-hosted build or isolate the smallest possible change before consuming hosted CI.

See `docs/LEAN_CI_OPERATIONS.md` for the current CI migration state and fallback commands.

## 6. GitHub change protocol

For normal mathematical work:

- work on a feature branch;
- keep each PR focused on one analytic or formal bridge;
- do not merge an ungreen mathematical PR;
- do not auto-merge unless the user explicitly asks;
- include scope, claim, assumptions, nonclaims, runtime impact, and CI state in the PR body;
- avoid unrelated cleanup in a mathematical PR;
- do not modify workflow triggers casually.

For documentation-only maintenance while hosted CI is scarce, avoid opening a PR that would trigger an expensive required Lean build unless that check is intentionally being spent. A prepared branch may be kept without a PR until the CI policy permits a cheap merge path.

## 7. CI cost policy

Treat GitHub-hosted Lean minutes as scarce.

- Do not re-enable automatic full Lean builds on `main` pushes without explicit user approval.
- Use `concurrency.cancel-in-progress: true` for PR builds so superseded runs stop.
- Preserve `.lake`/mathlib caches when using hosted or self-hosted runners.
- Prefer local incremental builds for proof development.
- If hosted quota is exhausted, continue by local or self-hosted verification rather than weakening the proof gate.
- A cache is only a performance optimization; `lake build` still determines what must be rebuilt.

## 8. Session-end handoff protocol

At the end of a substantial work session, update `HANDOFF.md` when the current frontier changed. The handoff should contain concrete symbols, not only prose.

Record:

- current `main` or relevant branch/PR;
- latest known Lean CI state;
- current target theorem;
- newly established theorem names and file names;
- exact remaining gate;
- known failed approaches that should not be repeated;
- whether any equality/estimate is still only a planned bridge;
- the next smallest Lean task.

Use a shape like:

```text
Current target:
  R3SchwartzConvectionTermSobolevEstimate 3

Completed infrastructure:
  <exact theorem/file list>

Next analytic gate:
  <exact missing equality or estimate>

Do not assume:
  <important tempting but unproved identification>
```

`FORMAL_SCOPE.md` should be synchronized less frequently, when the theorem boundary materially changes. `HANDOFF.md` should be the lightweight file updated at ordinary milestones.

## 9. Current formal-development invariant

The current H³-to-H² convection track must not silently identify the ordinary scalar majorants

- `r3H2LeftScalarMajorant`;
- `r3H2RightScalarMajorant`

with the bundled Young candidates

- `r3H2LeftMajorantYoungL2`;
- `r3H2RightMajorantYoungL2`.

`Formal/R3SchwartzConvectionScalarMajorants.lean` gives the ordinary pointwise convolutions. `Formal/R3SchwartzNormFieldL2.lean` gives the `L²` bundles and Young bounds. The representative/Fubini bridge between them remains a separate analytic obligation until a Lean theorem proves it.

## 10. Minimal resume prompt

A short user prompt should be sufficient:

`@GitHub ns-mns2-flowmap-bridge を GPT_WORKFLOW.md の resume protocol どおり確認して、最新 main/PR/CI と HANDOFF.md を照合して続きから。`
