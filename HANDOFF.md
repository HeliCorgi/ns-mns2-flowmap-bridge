# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: 2026-08-13 (JST)

This file is the short-form continuation point for future GPT/Codex/Claude sessions. Read this file together with `AGENTS.md` and `FORMAL_SCOPE.md` before changing claims or formal statements.

## Current frontier

The current formal frontier is the time-indexed Navier–Stokes bridge interface added by merged PR #10:

- PR #10: `Add a time-indexed Navier-Stokes bridge interface`
- merge commit: `219e051939b751307913ba9da6e724d063f072a4`
- main formal file: `Formal/NavierStokesTimeBridge.lean`

The repository now has the following theorem/interface ladder:

1. `Formal/Bridge.lean` — algebraic endpoint telescoping only.
2. `Formal/FlowMapFTC.lean` — Banach-valued path FTC.
3. `Formal/FlowMapChainRule.lean` — derives the affine path derivative and fixed tangent direction.
4. `Formal/FlowMapOperatorContinuity.lean` — derives tangent continuity from operator-valued continuity.
5. `Formal/FlowMapContDiffOne.lean` — obtains the bridge from a global `C¹` map.
6. `Formal/FlowMapLocalContDiff.lean` — localizes to an open admissible data domain.
7. `Formal/PDEBridgeAdapter.lean` — packages the analytic bridge with an abstract fixed-time PDE semantic relation.
8. `Formal/NavierStokesTimeBridge.lean` — packages certified time slices using an externally supplied time-indexed Navier–Stokes semantic relation.

CI also contains proof-hole and local-axiom guardrails, and `Formal/AxiomAudit.lean` prints axiom dependencies of the strongest current theorems.

## Exact mathematical bridge currently formalized

For an open admissible set `U`, a fixed-time map `S`, and a path

`γ(s) = x + s d`, `s ∈ [0,1]`,

if `S` is `C¹` on `U` and the full path stays in `U`, then

`∫₀¹ (DS(x + s d))[d] ds = S(x + d) - S(x)`.

Radially,

`∫₀¹ (DS(s d))[d] ds = S(d) - S(0)`.

If a separate hypothesis proves `S(0) = 0`, then

`S(d) = ∫₀¹ (DS(s d))[d] ds`.

The path tangent is always the fixed, unnormalized direction `d`.

Do not replace it by `s • d`, a normalized direction, or an arbitrary amplitude tangent.

## Current Navier–Stokes interface

`Formal/NavierStokesTimeBridge.lean` is parameterized by an externally supplied relation of the form

`NSEvolvesAt : ℝ → X → Y → Prop`.

The time-indexed adapter carries only certified nonnegative time slices. At each certified time it must provide:

- an open admissible initial-data domain;
- a time-indexed state map;
- `C¹` dependence of that state map on the certified domain;
- proof that the state map realizes `NSEvolvesAt` on that domain.

A certified time slice can then be converted into the already-proved `FixedTimePDEBridgeAdapter`, so the exact affine/radial bridge follows there.

This is an interface theorem, not a proof that Navier–Stokes supplies such certified slices.

## Next formal step

The next intended step is to give `NSEvolvesAt` concrete Navier–Stokes semantics without smuggling in existence or regularity.

Preferred direction: define a mild-solution predicate/interface based on

`u(t) = exp(ν t Δ) u₀ - ∫₀ᵗ exp(ν (t-s) Δ) P div(u ⊗ u)(s) ds`.

Treat this first as a semantic predicate / contract. Do not claim that every datum has such a solution, that it is unique globally, or that the resulting solution map is globally `C¹`.

A safe decomposition is:

1. define the abstract ingredients needed for the mild equation (linear evolution operator, nonlinear term, time integral);
2. define `NSMildSolution` / `NSEvolvesAt` from those ingredients;
3. prove only structural adapter lemmas that follow from supplied hypotheses;
4. keep existence, uniqueness, regularity, and continuation assumptions explicit and separate.

## Numerical/research track

The numerical MNS-2 bridge work is distinct from the Lean continuum theorem.

Key numerical facts already established in the broader project:

- conservative cylindrical transport variables use
  `U = u^θ/r`, `Ω = ω^θ/r`, `ψ = ψ^θ/r`, `Γ = r² U = r u^θ`;
- tangent direction for amplitude-path reconstruction is fixed and unnormalized;
- v2.2 synthetic flow-map path-independence tests passed for radial, Gamma-first, Omega-first, and closed-rectangle paths under a single frozen schedule;
- finite-dimensional coordinate-path reconstruction is exact for the frozen discrete map;
- a continuum promotion still requires convergence of solution maps and pathwise tangent actions on a common time interval;
- a real provenanced Hou late-state handoff seed is still missing; synthetic seeds are not late-state evidence.

Planned numerical continuation after the formal interface layer is a modal-coordinate bridge (v2.3), with explicit truncation/tail accounting and path-order diagnostics before any low-rank claim.

## External exclusion / no-go registry — mandatory preflight

Before opening a new singularity mechanism, ansatz family, shadowing route, numerical promotion argument, or whole-space interpretation, cross-check the read-only Fable5 registry:

- root: `https://github.com/HeliCorgi/ns-singularity-certificate-lab/tree/fable5-mainline`
- recorded binding verdicts: `https://github.com/HeliCorgi/ns-singularity-certificate-lab/blob/fable5-mainline/docs/research_notes/verification_sprint_v1/VERDICTS.md`
- numerical/whole-space audit: `https://github.com/HeliCorgi/ns-singularity-certificate-lab/blob/fable5-mainline/FABLE5_NEXT_TASK_AUDIT.md`
- equation audit: `https://github.com/HeliCorgi/ns-singularity-certificate-lab/blob/fable5-mainline/docs/equation_audit.md`
- external research rules: `https://github.com/HeliCorgi/ns-singularity-certificate-lab/blob/fable5-mainline/AGENTS.md`

Operational rule:

- `KILLED` / `REJECTED` means do not spend search budget there again unless the new route explicitly identifies the hypothesis that differs and explains why the recorded binding obstruction no longer applies.
- `CONDITIONAL` means preserve the exact condition; do not silently promote it to a live unconditional mechanism.
- For numerical work, inherit the relevant Fable5 stability/CFL, all-step gate, resolution, whole-space, provenance, domain/truncation, and independent-reproduction requirements before promotion.
- Do not use formulas marked `未確認`, `不整合`, or `誤り` in the external equation audit as implementation premises.
- Treat `ns-singularity-certificate-lab` as read-only provenance by default. Do not modify it unless the user explicitly requests changes in that repository.

This external registry is specifically meant to stop future sessions from rediscovering exploration spaces that have already been killed or from forgetting the conditions on routes that only survived conditionally.

## Hard guardrails

Never claim any of the following unless a new proof actually establishes it:

- the Clay Navier–Stokes problem is solved;
- global smoothness or global existence for arbitrary 3D data;
- a blow-up counterexample;
- a closed-form general solution;
- continuation of a `C¹` solution map through a possible singular time;
- discrete MNS-2 bridge convergence to the continuum without an explicit convergence theorem;
- numerical path-independence as proof of continuum Navier–Stokes regularity or blow-up;
- synthetic Hou-like data as provenanced Hou late-state evidence.

Keep these error classes separate:

- exact path-integral identity;
- quadrature error;
- low-rank/modal truncation error;
- PDE discretization error;
- continuum-promotion error;
- model/provenance scope.

## Lean proof hygiene

The repository CI rejects proof holes and local proof-bypassing declarations under `Formal/`. Do not introduce `sorry`, `admit`, local `axiom`, or source-level `opaque` declarations to make CI green.

The axiom audit currently expects ordinary mathlib/Lean foundational dependencies such as `propext`, `Classical.choice`, and `Quot.sound`; these are not locally introduced Navier–Stokes assumptions.

## GitHub workflow

Repository: `HeliCorgi/ns-mns2-flowmap-bridge`

Branch/ruleset protection is not enforced for this private repository under the current GitHub account plan. Treat green Lean CI as a manual merge gate.

The workflow is configured to run Lean CI for every pull request to `main`, so future sessions should inspect the latest PR and its Actions result before merging.

## How to resume in a new project chat

A short prompt should be enough:

`@GitHub ns-mns2-flowmap-bridge の HANDOFF.md、AGENTS.md、FORMAL_SCOPE.md を読んで、Fable5 exclusion registry も照合して、最新PRとCIを確認して続きから。`

If continuing the formal track, proceed from the mild-solution semantics layer described above.

If switching back to the numerical track, resume from the planned modal-coordinate bridge v2.3, preflight against the external Fable5 registry, and preserve all guardrails above.
