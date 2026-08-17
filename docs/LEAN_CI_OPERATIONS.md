# Lean verification operations

This document describes how to verify the Lean formalization with a ChatGPT-connected external Lean runner as the normal interactive compiler while avoiding unnecessary GitHub-hosted Actions usage.

## Verification contract

The substantive Lean gate consists of two parts:

1. reject proof holes and local proof-bypassing declarations under `Formal/`;
2. build the pinned Lake project successfully.

The forbidden-source scan rejects:

- `sorry`;
- `admit`;
- local `axiom` declarations;
- source-level `opaque` declarations used to hide missing proofs.

The Lake project is pinned by `lean-toolchain`, `lakefile.lean`, and `lake-manifest.json`. The default target builds `Formal.+`.

No runner is allowed to silently replace these files, run against a different mathlib revision, or validate only a decontextualized snippet while reporting the repository theorem as proved.

## Standard ChatGPT external-runner workflow

The normal proof-development path is:

`ChatGPT -> external Lean runner -> exact Lean diagnostics -> ChatGPT revision -> external Lean runner`

The external runner may be provided through an API, MCP server, custom GPT Action, or another ChatGPT-accessible execution tool. The transport is not itself part of the proof boundary; exact source revision and pinned Lean/Lake environment are.

A conforming runner must be able to do all of the following:

- identify the exact repository revision or receive an exact patch/worktree snapshot;
- honor the repository `lean-toolchain`, `lakefile.lean`, and `lake-manifest.json`;
- provide the repository dependencies required by the target module;
- run a targeted Lake build for a named module;
- run the full repository Lake gate when requested;
- return exact Lean/Lake stdout/stderr diagnostics rather than only a boolean result;
- make clear whether a result is targeted or full-gate evidence;
- preserve enough identity metadata to record the checked revision and toolchain.

A provider-specific runner may cache toolchains, mathlib, `.lake/packages`, or build products. Cache reuse is an optimization only; the requested revision and pinned dependency graph still control what is checked.

## External-runner iteration protocol

For a mathematical change:

1. resolve the current Git branch and exact commit or patch being tested;
2. verify the pinned toolchain/dependency files have not changed unexpectedly;
3. run the forbidden-source scan against the candidate repository state;
4. build the smallest relevant target;
5. feed the exact diagnostic back into ChatGPT and revise only the smallest justified proof surface;
6. repeat the targeted build until green;
7. run the full pinned repository gate after the target is green;
8. record the verification evidence in `HANDOFF.md` when the frontier changes.

The intended targeted command semantics are equivalent to:

```bash
bash scripts/lean-ci-local.sh Formal.SomeModule
```

For example:

```bash
bash scripts/lean-ci-local.sh Formal.R3SchwartzNormFieldL2
```

The intended full-gate semantics are equivalent to:

```bash
bash scripts/lean-ci-local.sh
```

The runner does not have to invoke this shell script literally if its environment exposes Lean/Lake differently, but it must enforce the same source scan, pinned dependency graph, target build, and full-build proof boundary.

## Verification evidence record

For every verification result that is used to claim a theorem or branch is green, preserve at least:

```text
runner: <provider/tool identity>
revision: <exact commit SHA or explicitly described patch/worktree>
toolchain: <lean-toolchain value>
dependency manifest: <lake-manifest identity or exact repository revision>
scope: <Formal.Module or full Formal.+ gate>
result: <pass/fail>
diagnostics: <exact error location/message when failing>
```

A targeted green result proves only that target and its dependency closure. A full repository result remains a separate gate.

If the runner checked an uncommitted candidate patch, record that fact explicitly. Do not attribute the result to `main` or a branch commit until the checked content is identical.

## Local reproduction fallback

Local Lean remains a valid reproduction path but is no longer the required normal interactive compiler.

First setup:

```bash
bash scripts/lean-ci-local.sh --bootstrap
```

Normal full gate:

```bash
bash scripts/lean-ci-local.sh
```

Targeted development build:

```bash
bash scripts/lean-ci-local.sh Formal.SomeModule
```

Clean only this project's build outputs while retaining downloaded dependencies:

```bash
bash scripts/lean-ci-local.sh --clean
```

Do not routinely delete `.lake/packages`; keeping dependencies and build outputs is what makes subsequent local checks incremental.

A local reproduction is useful when diagnosing a runner discrepancy, but absence of a local Lean installation is not a reason to spend GitHub-hosted Actions interactively.

## GitHub-hosted policy

GitHub-hosted Lean CI is an optional scarce status/final-confirmation resource, not the normal proof-development compiler.

Current repository policy:

- automatic full Lean rebuilds on pushes to `main` are disabled;
- PR-to-`main` Lean checks may still exist and may be required by branch protection;
- `workflow_dispatch` may remain available;
- per-PR concurrency cancellation and `.lake`/mathlib caching should remain enabled when hosted checks are used;
- the explicit forbidden-source scan remains before the Lean build.

Do not open or update a PR merely to make Actions act as a remote Lean REPL. If hosted quota is exhausted, continue proof development through the ChatGPT-connected external runner or another explicitly identified non-hosted reproduction path.

Do not re-enable automatic `main` push builds merely for convenience.

## Current migration state

PR #77 (`Cut hosted Lean CI usage and add cache`) is merged and established the low-hosted-usage policy.

The latest mathematical hosted check before this workflow switch was PR #80 head `8f31dea042a72381e92bbf4cdeb1370525ba6d7b`, Lean run #256 (`31920218959`), which completed successfully before merge commit `73cf3b276179aedb0e830d2d46c3246b269c1f7f` landed on `main`.

PR #81 then merged the external-runner workflow documentation as main commit
`710709c34b8ee564b071e71fd27313be4cc383a6`. Its head
`18c64b80b6eebb95a4344dec5811fc024b963377` passed hosted Lean run #257
(`31924077773`); the head and merge commit have the same Git tree, while the merge SHA itself has no
separate run attached.

The next mathematical gate was developed without GitHub Actions. Local Windows/Elan verification
of commit `6ecfcda51d74b456b538def2577c52a403a0ff88`, under
`leanprover/lean4:v4.32.1` and the committed manifest, passed the source scan, targeted module,
axiom audit, and full `Formal.+` gate (8735 jobs).

The weighted-density and completed-convection gate was likewise developed without GitHub Actions.
Local Windows/Elan verification of commit
`5eb29848eea0529bf557c68a599e78317090f522`, with mathlib revision
`520045ab14e26149ee970e2e617ca04b09bde5d6`, passed targeted builds of
`Formal.R3SchwartzSobolevDensity`, `Formal.R3SobolevConvectionExtension`, and
`Formal.AxiomAudit`, followed by the pinned source scan and full `Formal.+` gate (8737 jobs).
The new audited theorems report only `propext`, `Classical.choice`, and `Quot.sound`.

Those results are evidence only for the exact revisions and trees identified above. Future
interactive development should use a conforming external runner or local reproduction rather than
consuming hosted quota.

Always inspect current repository/verification state rather than assuming this historical state is still current. `HANDOFF.md` records the latest known transition point, but exact Git contents and exact runner evidence are authoritative.

## Why `lake-manifest.json` is committed

The previous manual hosted workflow ran `lake update` on fresh runners, dynamically generating a dependency graph. The committed manifest fixes dependency revisions and makes reproducible caching possible.

Do not casually run `lake update` and commit a changed manifest unless a dependency/toolchain update is intended and reviewed.

The same rule applies to the external runner: it must not silently regenerate a different dependency graph and then report the repository as verified.

## Cache semantics

Caching is permitted on external, local, self-hosted, or GitHub-hosted runners.

Useful caches include:

- Lean toolchains;
- mathlib/dependency clones;
- `.lake/packages`;
- compatible build products.

A cache is never proof evidence by itself. Lean/Lake must still decide what must be rebuilt for the requested source revision and pinned manifest.

If cache behavior is suspicious, run a clean or minimally cached reproduction on a conforming runner.

## Self-hosted fallback

A self-hosted runner remains an acceptable fallback or independent reproduction path. It need not be registered as a GitHub Actions runner; a plain VPS/process reachable through the ChatGPT external-runner interface is sufficient if it satisfies the verification contract above.

If a GitHub self-hosted Actions runner is used, it can preserve PR check semantics without consuming GitHub-hosted compute, but it is not required for normal interactive development.

A suitable execution still has the logical shape:

```text
exact repository state
-> forbidden-source scan
-> pinned Lean/Lake environment
-> targeted or full lake build
-> exact diagnostics/result
```

Changing where computation runs does not change the mathematical proof boundary.

## ChatGPT/GPT operational rule

When a GPT session has a conforming external Lean runner, use it directly for iterative proof development.

When a GPT session has no conforming external runner available:

- do not claim new Lean code is verified;
- do not push a long sequence of speculative commits to consume hosted Actions;
- reason against the exact pinned source/API and keep changes as candidate code;
- use a local or self-hosted reproduction if one is explicitly available;
- use GitHub-hosted CI only when the user deliberately approves spending that check or repository integration requires it.

A runner connection problem is an infrastructure problem, not permission to weaken theorem statements or proof hygiene.

## Documentation-only changes

Documentation-only workflow maintenance does not require a Lean build unless it changes executable Lean/project configuration.

While hosted quota is scarce, a documentation branch may be prepared without opening a PR if opening the PR would trigger an unnecessary required Lean build. Once integration is desired, use a path that does not pretend an unrun Lean check exists.

Do not add a workflow-level PR `paths` filter if branch protection requires the Lean check for every PR; doing so can leave required checks permanently pending. If documentation-only PRs need a cheap check, implement in-job changed-path detection while still emitting the required job, or adjust branch protection deliberately as a separate policy change.
