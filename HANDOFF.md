# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: 2026-08-16 JST.

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

## Repository / verification state

- PR #77 (`Cut hosted Lean CI usage and add cache`) is merged.
- PR #78 (`Gpt handoff protocol`) is merged.
- PR #79 (`R3 young real set integral bridge`) is merged.
- PR #80 (`Close R3 Schwartz H3-to-H2 convection factors`) is merged.
- PR #80 head `8f31dea042a72381e92bbf4cdeb1370525ba6d7b` passed Lean run #256 (`31920218959`). The hosted run completed successfully before merge.
- Current `main` HEAD at this handoff is merge commit `73cf3b276179aedb0e830d2d46c3246b269c1f7f`.
- At the latest check there are no open PRs.
- Automatic full Lean builds on pushes to `main` remain disabled.
- PR-to-`main` hosted Lean checks may remain configured, but GitHub-hosted Actions are no longer the normal interactive compiler.
- The preferred interactive path is now **ChatGPT -> external Lean runner -> exact diagnostics -> ChatGPT iteration** under the contract in `docs/LEAN_CI_OPERATIONS.md`.
- Local/self-hosted execution remains a valid reproduction/fallback path.
- GitHub-hosted Actions should be used only for deliberately spent status/final-confirmation checks or when repository integration policy explicitly requires one.

## Workflow migration branch

Prepared documentation branch:

`agent/chatgpt-external-lean-workflow`

This branch changes the operational contract from local/self-hosted-first plus scarce hosted fallback to a ChatGPT-connected external Lean runner as the standard interactive verification path. It also synchronizes stale PR #80 handoff/formal-scope text.

No PR is opened for this documentation branch at this handoff because opening a PR may trigger a hosted Lean check while hosted quota is exhausted. Integrate it later through an explicitly chosen cheap/non-hosted path.

The workflow documents are provider-agnostic: an external runner may be exposed through API, MCP, custom GPT Action, or another ChatGPT-accessible execution tool, but it must reproduce the pinned repository/toolchain gate and return exact diagnostics.

Important operational status: this specific ChatGPT runtime does **not yet have a conforming external Lean runner tool connected**. The workflow migration is documented, but new Lean proof changes remain unverified until such a runner is connected or another conforming reproduction path is deliberately used.

## Project claim boundary

Ultimate target: an exact official Clay/Fefferman Navier–Stokes A/B/C/D statement.

Current physical research specialization remains the `R^3`, preferably unforced `f = 0`, axisymmetric-with-swirl breakdown track governed by `SPEC.md`.

No current Lean theorem is a Clay result. Do not claim global regularity, blow-up, local well-posedness of the full concrete `R^3` problem, finite-cylinder transfer, or discrete-to-continuum promotion unless separately proved.

## Current formal target

The active near-term target remains

`R3SchwartzConvectionTermSobolevEstimate 3`

from `Formal/R3SchwartzConvectionSobolevReduction.lean`.

Its definition requires one explicit `C : ℝ`, `0 ≤ C`, uniformly valid for every `i : Fin 3`, followed by the one-coordinate H² estimate with the two H³ input norms.

Once this theorem is proved, the existing `.to_convection` reduction supplies `R3SchwartzConvectionSobolevEstimate 3` with the factor-three summation loss.

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

## Exact next Lean gate

Do not reopen the Fourier-coordinate or representative/Fubini work unless the current source actually regresses.

The next smallest mathematical task is finite-dimensional constant packaging:

1. define or choose an explicit uniform nonnegative constant over `i : Fin 3` dominating `r3CoordinateDerivativeFrequencyConstant i`;
2. a finite sum or finite maximum is sufficient; sharpness is irrelevant;
3. use `norm_r3SchwartzToHsCLM_two_convectionTerm_le_H3` plus the uniform domination to prove `R3SchwartzConvectionTermSobolevEstimate 3` with the exact definition in `Formal/R3SchwartzConvectionSobolevReduction.lean`;
4. then invoke `.to_convection` for `R3SchwartzConvectionSobolevEstimate 3`;
5. only after that move to the projected quadratic / mild-theory layer.

A natural non-sharp candidate is to dominate each coordinate constant by a finite `Finset.univ` sum of the nonnegative constants, then absorb the common factor `4 * ‖r3H2InverseBesselWeightL2‖` into the witness `C`.

## External-runner verification protocol for the next proof

Once a conforming ChatGPT-accessible Lean runner is connected, use it as the interactive compiler.

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
- the merged H³→H² per-coordinate theorem does not yet supply the uniform `Fin 3` witness required by `R3SchwartzConvectionTermSobolevEstimate 3`;
- do not spend hosted Actions as an interactive compiler while quota is scarce/exhausted.

## Minimal continuation prompt

`@GitHub ns-mns2-flowmap-bridge を docs/GPT_WORKFLOW.md の resume protocol どおり確認して、最新 main/PR/Lean verification と HANDOFF.md を照合して続きから。Lean の反復検証は ChatGPT 接続の外部 runner を使い、GitHub Actions は明示的に必要な場合だけ使って。古い会話より実コードを優先して。`
