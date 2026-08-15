# Lean CI cost reduction and local fallback

## Current cost profile

The hosted Lean workflow currently does the following on a fresh `ubuntu-latest` runner:

1. checkout;
2. reject `sorry` / `admit` and source-level `axiom` / `opaque` under `Formal/`;
3. install Elan and the pinned Lean toolchain;
4. run `lake update`;
5. run `lake exe cache get`;
6. run the default `lake build`, which builds the complete `Formal.+` library.

A representative successful PR run (#240 for PR #76) took about 9 minutes. The full project build occupied roughly 6m22s of that run. `lake update` also ran mathlib's downstream post-update hook, which fetched/decompressed the mathlib cache; the immediately following explicit `lake exe cache get` therefore found no files to download.

The workflow also runs again after a merged PR is pushed to `main`. For normal PR-based work this means the same formalization is commonly paid for twice: once on the PR merge commit and once again on the resulting `main` push.

The numerical workflow is path-filtered and is not the main source of current formal-development usage.

## Local zero-hosted-minute fallback

Use `scripts/lean-ci-local.sh`. Because GitHub's contents API does not preserve an executable bit, invoke it with `bash` unless you set the bit locally.

First setup:

```bash
bash scripts/lean-ci-local.sh --bootstrap
```

Normal incremental full gate:

```bash
bash scripts/lean-ci-local.sh
```

Target one Lean module while developing:

```bash
bash scripts/lean-ci-local.sh Formal.R3SchwartzNormFieldL2
```

Force a clean rebuild of this project's outputs while keeping downloaded dependencies:

```bash
bash scripts/lean-ci-local.sh --clean
```

The script preserves `.lake/packages` and ordinary local build outputs between runs, so after the first bootstrap Lake can do incremental recompilation instead of recreating the entire environment on every check.

## Recommended hosted-workflow changes

Do these in this order.

### 1. Remove the redundant `push` run on `main`

Keep the PR check and `workflow_dispatch`, but do not automatically rerun the full Lean build immediately after merging the already-green PR. This should cut the dominant PR workflow usage by close to half for the current development pattern.

If a separate direct-push branch still needs CI, retain only that branch under `push`.

### 2. Cancel superseded PR runs

Add workflow concurrency so a new commit to the same PR cancels the old in-progress build:

```yaml
concurrency:
  group: lean-${{ github.event.pull_request.number || github.ref }}
  cancel-in-progress: true
```

This matters when a compile error is fixed before the previous run has completed.

### 3. Cache the downstream `.lake` build

The official `leanprover/lean-action@v1` caches `.lake` by default. Its fallback cache key excludes the commit hash but includes the platform and Lake manifest, allowing a new PR commit to restore build artifacts from a previous compatible commit and then let Lake rebuild changed modules and their dependents.

A candidate replacement for the manual Elan/update/cache/build sequence is:

```yaml
- uses: leanprover/lean-action@v1
  with:
    auto-config: false
    build: true
    test: false
    lint: false
    use-mathlib-cache: true
    use-github-cache: true
```

Keep the repository's explicit proof-hole/local-axiom grep before this action.

Caching is an optimization, not a logical shortcut: `lake build` is still executed and Lake decides what must be rebuilt. If a cache ever behaves suspiciously, disable it and perform a clean build.

### 4. Optional cheap path for documentation-only PRs

The Lean check is currently required for every PR, so a workflow-level `paths` filter was intentionally avoided. If documentation-only PR traffic becomes material, keep the workflow itself running, perform a cheap changed-path detection inside the required job, and skip only the expensive Lean setup/build steps when no formalization-relevant path changed. This preserves an emitted required check instead of leaving branch protection pending.

## No-hosted-minute CI with GitHub status checks

A self-hosted GitHub Actions runner is the closest drop-in replacement for the current gate. GitHub documents Actions usage on self-hosted runners as free; the machine, network, and electricity/cloud cost are supplied by the repository owner.

For this repository the practical setup is:

- keep the same PR-triggered workflow and required check name;
- change `runs-on` to a dedicated self-hosted runner label;
- run the same proof-hole audit and `bash scripts/lean-ci-local.sh`;
- preserve the runner's Lean toolchain, `.lake/packages`, and project build artifacts between jobs where safe.

This keeps the GitHub PR check UI and branch-protection gate while avoiding GitHub-hosted runner minutes.

## Confidence levels

The local script is intended to reproduce the substantive current Lean gate: forbidden-token scan plus the pinned project's `lake build`. It does not by itself publish a GitHub status check.

The self-hosted runner preserves the GitHub Actions status-check mechanism and is therefore the preferred fallback if branch protection must remain unchanged.

The hosted caching proposal should be tested on a small number of PRs before treating its runtime savings as stable. The first cache-miss run can still cost approximately the current full-build time.
