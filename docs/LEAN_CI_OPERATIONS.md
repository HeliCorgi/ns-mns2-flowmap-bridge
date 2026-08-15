# Lean CI operations

This document describes how to verify the Lean formalization while minimizing GitHub-hosted Actions usage.

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

## Local workflow

The normal development path is local and incremental.

First setup:

```bash
bash scripts/lean-ci-local.sh --bootstrap
```

This installs/uses Elan, resolves the pinned Lake dependencies, and obtains the mathlib cache.

Normal full gate:

```bash
bash scripts/lean-ci-local.sh
```

Targeted development build:

```bash
bash scripts/lean-ci-local.sh Formal.SomeModule
```

For example:

```bash
bash scripts/lean-ci-local.sh Formal.R3SchwartzNormFieldL2
```

Clean only this project's build outputs while retaining downloaded dependencies:

```bash
bash scripts/lean-ci-local.sh --clean
```

Do not routinely delete `.lake/packages`; keeping dependencies and build outputs is what makes subsequent local checks incremental.

## GitHub-hosted policy

GitHub-hosted Lean CI is a scarce final/status-check resource. It should not be used as the normal proof-development compiler.

The intended hosted workflow after the CI-cost migration is:

- PRs to `main` emit the `Lean 4 formalization / build` check;
- automatic full Lean rebuilds on pushes to `main` are disabled;
- `workflow_dispatch` remains available;
- the legacy `lean4-formalization` push branch may remain covered;
- per-PR concurrency cancels superseded runs;
- official `leanprover/lean-action@v1` restores/saves `.lake` and obtains the mathlib cache;
- the explicit forbidden-source scan remains before the Lean build.

Do not re-enable automatic `main` push builds merely for convenience. The old arrangement commonly paid for the same formalization twice: once on the PR merge ref and again after the green PR was merged.

## CI migration state

PR #77 (`Cut hosted Lean CI usage and add cache`) is the migration PR for the above policy.

Important historical failure: its first lean-action attempt failed before compilation because the repository did not yet contain `lake-manifest.json`; `leanprover/lean-action@v1` requires the manifest during configuration. The PR was updated with a manifest matching the pinned mathlib `v4.32.1` dependency graph.

Always inspect the current PR/CI state rather than assuming this migration has already merged. `HANDOFF.md` records the latest known transition state, but GitHub is authoritative.

## Why `lake-manifest.json` is committed

The previous manual workflow ran `lake update` on every fresh runner, generating a manifest dynamically. That made the project work on an empty runner but defeated the official lean-action cache setup and repeatedly resolved/cloned the same dependency graph.

The committed manifest fixes the dependency revisions used by the pinned project and gives the cache a stable compatibility key.

Do not casually run `lake update` and commit a changed manifest unless a dependency/toolchain update is intended and reviewed.

## Hosted cache semantics

`leanprover/lean-action@v1` caches `.lake` using the platform, architecture, toolchain/manifest hashes, and commit information. If the exact commit cache misses, it can restore a compatible earlier cache for the same toolchain/manifest and then run `lake build`.

This does **not** weaken verification. Cached `.olean`/build artifacts are an optimization; Lake still determines which project modules and dependencies need rebuilding.

If cache behavior is suspicious, run a clean local build or temporarily disable the GitHub cache for diagnosis.

## Self-hosted fallback

If GitHub-hosted quota is exhausted, the preferred status-check replacement is a dedicated self-hosted GitHub Actions runner.

A self-hosted runner can keep the same workflow/check semantics while using the owner's machine or VPS for computation. Preserve the pinned toolchain and dependency/build cache between jobs where safe.

A suitable job should still perform:

```text
checkout
-> forbidden-source scan
-> pinned Lean/Lake environment
-> lake build
```

Self-hosting changes where computation runs; it does not change the mathematical proof boundary.

## ChatGPT/GPT operational rule

When a GPT session has no Lean/Lake runtime available, it must not compensate by pushing a long series of speculative commits to consume hosted Actions as an interactive compiler.

Preferred alternatives are:

- reason against the exact pinned source/API and make the smallest plausible change;
- ask for or use a local targeted build;
- use a self-hosted runner;
- batch only well-motivated changes into a deliberately spent hosted check.

If a hosted check fails, read the exact job log before changing code.

## Documentation-only changes

A required PR check may run even for documentation-only PRs. While hosted quota is scarce, documentation branches can be prepared without opening a PR. After the CI policy permits a cheap merge path, integrate them without unnecessarily spending a full hosted Lean build.

Do not add a workflow-level PR `paths` filter if branch protection requires the Lean check for every PR; doing so can leave required checks permanently pending. If documentation-only PRs need a cheap check, implement in-job changed-path detection while still emitting the required job.
