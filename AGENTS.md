# AGENTS.md

This repository contains numerical experiments and Lean 4 formalization for the MNS-2 flow-map bridge program.

## GPT-first operating contract

This repository is expected to be developed primarily through repeated GPT/Codex sessions. Chat history is not a durable source of truth.

Every new agent/session must execute the resume protocol in `docs/GPT_WORKFLOW.md` before choosing a task or modifying code. At minimum, read `PROJECT_GOAL.md`, `SPEC.md`, this file, `FORMAL_SCOPE.md`, `HANDOFF.md`, and `docs/LEAN_CI_OPERATIONS.md`, then inspect the current GitHub `main`, open PRs, relevant `Formal/` files, and latest Lean CI state.

When progress prose disagrees with actual code, current theorem statements and repository state control the formal frontier. Update stale handoff/scope documentation rather than reasoning from an old conversation.

At the end of a substantial session, update `HANDOFF.md` when the formal frontier, open PR, known blocker, or next theorem changed. Record exact theorem and file names, the next smallest gate, and any tempting but still-unproved identification that a later agent must not assume.

## CI cost policy

GitHub-hosted Lean Actions are a scarce final/status-check resource, not the normal interactive compiler.

- Prefer a conforming ChatGPT-connected external Lean runner when available; a local incremental
  run through `scripts/lean-ci-local.sh` is a fully valid reproduction/fallback path.
- Build the smallest relevant target while developing, then run the pinned full gate on the same
  runner path.
- If the current GPT environment has no Lean/Lake runtime, do not compensate with repeated speculative PR commits merely to use hosted Actions as a compiler.
- Preserve `.lake` and mathlib caches where the runner model allows it.
- Keep per-PR cancellation of superseded builds.
- Do not re-enable automatic full Lean builds on pushes to `main` without explicit user approval.
- If hosted quota is exhausted, continue with local or self-hosted verification; do not weaken the proof gate.
- Do not casually change workflow triggers, required-check names, or the pinned dependency manifest.

See `docs/LEAN_CI_OPERATIONS.md` for the operational details and the current CI migration state.

## Governing project goal

`PROJECT_GOAL.md` is the top-level goal and acceptance specification for this repository. Read it before choosing a research direction or promoting a result.

`SPEC.md` is the subordinate normative research/implementation specification for the current primary `R^3`, unforced, axisymmetric-with-swirl breakdown track. After `PROJECT_GOAL.md`, read `SPEC.md` before changing physical equations, sign conventions, axis regularity, 3D reconstruction, candidate-data invariants, numerical domains, or promotion language. If `SPEC.md` conflicts with `PROJECT_GOAL.md` or the official Clay statement, the higher-level target controls.

The ultimate target is a rigorous resolution of one of the official Clay/Fefferman Navier--Stokes statements A/B/C/D. The current primary attack is the breakdown side (C/D), with an unforced construction `f = 0` preferred when the mathematics supports it.

All local theorem scopes, numerical milestones, handoff notes, and candidate mechanisms are subordinate to that target. A result in a different domain, reduced model, finite cylinder, discrete map, or conditional functional-analytic setting is an intermediate result unless a rigorous chain connects it to the exact official Clay hypotheses.

## Non-negotiable claim boundary

Do **not** claim that this repository proves any of the following:

- global existence or smoothness for 3D Navier–Stokes;
- a Navier–Stokes blow-up counterexample;
- a closed-form or global general solution of Navier–Stokes;
- continuation of a solution map through a singular time;
- that the Hou late-state singular regime has been reproduced or validated here;
- that a discrete/numerical bridge automatically implies the continuum bridge.

The strongest currently formalized analytic implication is local and conditional:

> If a fixed-time map `S` is `C¹` on an open set `U` containing the entire initial-data path, then the exact path-integral reconstruction identity holds on that path.

For the affine path `s ↦ x + s • d`, the tangent is the fixed, unnormalized direction `d`.

## External exclusion / no-go registry

Before proposing, implementing, or promoting a new Navier–Stokes singularity mechanism or numerical route, consult the read-only external registry:

- repository/branch: `https://github.com/HeliCorgi/ns-singularity-certificate-lab/tree/fable5-mainline`
- binding verdicts: `https://github.com/HeliCorgi/ns-singularity-certificate-lab/blob/fable5-mainline/docs/research_notes/verification_sprint_v1/VERDICTS.md`
- numerical and whole-space audit gates: `https://github.com/HeliCorgi/ns-singularity-certificate-lab/blob/fable5-mainline/FABLE5_NEXT_TASK_AUDIT.md`
- equation audit: `https://github.com/HeliCorgi/ns-singularity-certificate-lab/blob/fable5-mainline/docs/equation_audit.md`
- external working agreement: `https://github.com/HeliCorgi/ns-singularity-certificate-lab/blob/fable5-mainline/AGENTS.md`

Treat this registry as negative-knowledge provenance, not as code owned by this repository.

- Do not reopen a route marked `KILLED` or `REJECTED` unless a new argument states exactly which hypothesis or binding reason is escaped and why the old no-go does not apply.
- Preserve every condition attached to a `CONDITIONAL` route; do not paraphrase it into an unconditional surviving mechanism.
- Before promoting numerical evidence, apply any relevant Fable5 stability, CFL, resolution, domain/truncation, provenance, and independent-reproduction gates.
- A formula marked `未確認`, `不整合`, or `誤り` in the external equation audit must not be used as an implementation premise here.
- Do not mutate `ns-singularity-certificate-lab` as part of work in this repository unless the user explicitly asks for a change there. The default use is read-only cross-checking.

The purpose of this cross-check is to prevent rediscovery or accidental promotion of exploration spaces that already have a recorded binding obstruction.

## Tangent-direction invariant

Never replace the path derivative `d` by any of the following unless the path itself has actually been changed and the derivative is rederived:

- `s • d`;
- a normalized copy of `d`;
- an arbitrary amplitude vector such as `q_amp`;
- a state-dependent retuned direction.

For a radial path `s ↦ s • d`, the derivative with respect to `s` is exactly `d`.

## Lean proof discipline

- No `sorry`.
- No `admit`.
- No new local `axiom` declarations.
- No `opaque` declarations used to hide missing proofs.
- Prefer existing mathlib theorems over restating analytic facts as assumptions.
- If a theorem is only algebraic endpoint cancellation, do not describe it as an analytic FTC theorem.
- Keep assumptions explicit in theorem statements or immediately documented above them.
- Do not weaken assumptions in prose after proving a theorem under stronger assumptions.
- Do not identify ordinary pointwise convolution with an `L²`-valued Bochner convolution until an explicit a.e. representative/Fubini theorem proves the identification.

The CI safety gate scans `Formal/**/*.lean` for proof holes and local axiom-like declarations before running `lake build`.

## Formal/analytic layers

Treat these as distinct layers:

1. algebraic endpoint telescoping;
2. Banach-valued FTC along a path;
3. Fréchet chain rule producing `DS[path]` applied to the fixed path tangent;
4. continuity of tangent action from operator-valued continuity;
5. `C¹` regularity implying differentiability plus continuous `fderiv`;
6. localization to an open admissible-data domain;
7. PDE-specific construction of a genuine fixed-time solution map and its domain.

Layers 1–6 are abstract functional analysis. Layer 7 is where Navier–Stokes-specific existence/regularity assumptions enter.

## Numerical-to-continuum guardrail

Never promote a discrete bridge, grid-converged scalar diagnostic, SVD approximation, or finite-dimensional coordinate identity to a continuum Navier–Stokes theorem without an explicit convergence argument strong enough to pass the solution map and pathwise tangent through the limit.

Keep these errors separate when reporting results:

- PDE discretization error;
- time-integration error;
- path quadrature error;
- low-rank/modal truncation error;
- operator/invariant-subspace error;
- discrete-to-continuum error.

## MNS-2 numerical invariants

When touching the numerical stack, preserve the project conventions unless a change is explicitly justified and tested:

- conservative cylindrical transport;
- LF-WENO7-JS transport where specified;
- frozen real LF speeds during holomorphic tangent windows;
- fixed positive WENO epsilon during a tangent/scan window;
- no state-dependent `max`, `abs`, or `sign` inserted inside a perturbed holomorphic map;
- physical-energy metric for tangent geometry;
- clustered singular subspaces rather than individual singular-vector identities through degeneracy;
- no per-path or per-amplitude schedule retuning when comparing path integrals.

For any candidate promoted toward the current `R^3` track, additionally satisfy the physical equations, `2π r dr dz` measure, axis regularity, Cartesian reconstruction, provenance, convergence, and candidate-certificate requirements in `SPEC.md`.

## Hou production wall-vorticity gate

The current v1.1 full holomorphic pilot is **not** a Hou-production no-slip wall-vorticity discretization. Before any longer-time result is promoted as a Hou production reproduction, Hou late-state validation, or resolved Hou singular regime, the numerical stack must implement and audit the transformed wall conditions described in Hou 2022, Section 2, equations (2.3)--(2.5), including

- `psi1=0` and `psi1_r=0` at `r=1`;
- `u1=0` at `r=1`;
- vorticity creation via `omega1=-psi1_rr` at `r=1`;
- matching JVP and adjoint contributions for the wall closure.

Do not invent an undocumented stencil and label it Hou's production stencil. See `docs/reports/HOU_WALL_VORTICITY_BOUNDARY_AUDIT_2026-08-13.md` for the current blocker and required verification gates.

Short synthetic finite-discrete flow-map/JVP regressions may continue under the existing pilot only under their explicitly limited scope.

## Provenance guardrail

Synthetic or analytic seeds are not Hou late-state evidence. Do not label them as such. A genuine late-state comparison requires explicit provenance for the numerical state and schedule.

## Pull requests

Every mathematical PR should state:

- which Clay statement, if any, the work is intended to support, or that it is infrastructure only;
- whether the current `SPEC.md` applies and, if not, which track/domain differs;
- the mathematical claim;
- the exact new assumptions;
- the Lean theorem(s) or numerical artifact(s) implementing it;
- what the change does **not** prove;
- whether it changes any numerical/runtime behavior;
- CI status.

Use `PROJECT_GOAL.md` as the project-level acceptance boundary, `SPEC.md` as the current physical/numerical research contract, `FORMAL_SCOPE.md` as the current Lean theorem/claim boundary, and `docs/GPT_WORKFLOW.md` as the repeat-session execution protocol.
