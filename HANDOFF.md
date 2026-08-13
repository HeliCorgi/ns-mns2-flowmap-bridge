# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: 2026-08-13 (JST)

This file is the short-form continuation point for future GPT/Codex/Claude sessions. Read `PROJECT_GOAL.md` first, then `SPEC.md`, then this file together with `AGENTS.md` and `FORMAL_SCOPE.md` before changing claims, physical equations, numerical promotion rules, or formal statements.

## Governing project target

`PROJECT_GOAL.md` is the repository's top-level specification.

`SPEC.md` is the subordinate normative research/implementation contract for the current primary `R^3`, `f = 0`, axisymmetric-with-swirl breakdown track. It fixes the working physical equations, sign conventions, axis regularity, 3D reconstruction, physical measure, candidate-data invariants, and numerical-to-proof promotion ladder. If it conflicts with the official Clay/Fefferman statement or `PROJECT_GOAL.md`, the higher-level target controls.

Ultimate acceptance target: rigorously establish one of the official Clay/Fefferman Navier--Stokes statements A/B/C/D with the exact official hypotheses and domain.

Current primary attack: the breakdown side (C/D), with an unforced route `f = 0` preferred when supportable. Hou-cylinder, MNS-2, flow-map, mild-solution, POD/SVD, and Lean bridge results are intermediate infrastructure or candidate evidence until a rigorous chain reaches an exact Clay statement.

## Current frontier

The formal frontier now includes the mild-solution semantic and quadratic-nonlinearity layers through merged PR #15:

- PR #12: `Formalize the mild-solution Duhamel semantics`
- PR #13: `Connect the radial flow-map bridge to mild Duhamel endpoints`
- PR #14: `Derive the zero-fixed bridge condition from mild uniqueness`
- PR #15: `Formalize the derivative of a quadratic mild nonlinearity`
- PR #16: `Link the Fable5 exclusion registry`

The repository now has the following theorem/interface ladder:

1. `Formal/Bridge.lean` — algebraic endpoint telescoping only.
2. `Formal/FlowMapFTC.lean` — Banach-valued path FTC.
3. `Formal/FlowMapChainRule.lean` — derives the affine path derivative and fixed tangent direction.
4. `Formal/FlowMapOperatorContinuity.lean` — derives tangent continuity from operator-valued continuity.
5. `Formal/FlowMapContDiffOne.lean` — obtains the bridge from a global `C¹` map.
6. `Formal/FlowMapLocalContDiff.lean` — localizes to an open admissible data domain.
7. `Formal/PDEBridgeAdapter.lean` — packages the analytic bridge with an abstract fixed-time PDE semantic relation.
8. `Formal/NavierStokesTimeBridge.lean` — packages certified time slices using an externally supplied time-indexed Navier–Stokes semantic relation.
9. `Formal/MildSolutionSemantics.lean` — represents a Banach-valued Duhamel equation with mathlib interval integrals.
10. `Formal/MildFlowMapBridge.lean` — connects certified flow-map reconstruction to mild endpoint witnesses.
11. `Formal/MildZeroUniqueness.lean` — derives the zero-fixed endpoint condition from explicit mild uniqueness assumptions.
12. `Formal/QuadraticMildNonlinearity.lean` — formalizes `B(u)=Q(u,u)` and `DB(u)[v]=Q(u,v)+Q(v,u)` for a continuous bilinear map.

CI also contains proof-hole and local-axiom guardrails, and `Formal/AxiomAudit.lean` prints axiom dependencies of the strongest current theorems.

## Exact mathematical bridge currently formalized

For an open admissible set `U`, a fixed-time map `S`, and a path

`γ(s) = x + s d`, `s ∈ [0,1]`,

if `S` is `C¹` on `U` and the full path stays in `U`, then

`∫₀¹ (DS(x + s d))[d] ds = S(x + d) - S(x)`.

Radially,

`∫₀¹ (DS(s d))[d] ds = S(d) - S(0)`.

If a separate argument proves `S(0) = 0`, then

`S(d) = ∫₀¹ (DS(s d))[d] ds`.

The path tangent is always the fixed, unnormalized direction `d`.

Do not replace it by `s • d`, a normalized direction, or an arbitrary amplitude tangent.

## Current Navier–Stokes / mild interface

`Formal/NavierStokesTimeBridge.lean` is parameterized by an externally supplied relation of the form

`NSEvolvesAt : ℝ → X → Y → Prop`.

The time-indexed adapter carries only certified nonnegative time slices. At each certified time it must provide an open admissible initial-data domain, a time-indexed state map, `C¹` dependence on the certified domain, and proof that the state map realizes the semantic relation.

`Formal/MildSolutionSemantics.lean` supplies a concrete abstract Duhamel-shaped relation

`u(t) = H(t)u₀ - ∫₀ᵗ H(t-s) B(u(s)) ds`,

with endpoint existence existential in a witnessing trajectory rather than silently assuming uniqueness.

`Formal/MildFlowMapBridge.lean` connects this mild relation to the radial flow-map identity. `Formal/MildZeroUniqueness.lean` isolates the uniqueness hypothesis needed to derive `stateMap t 0 = 0`. `Formal/QuadraticMildNonlinearity.lean` formalizes the derivative of a quadratic diagonal `B(u)=Q(u,u)`.

This remains an interface/functional-analysis layer. It does not yet construct the actual three-dimensional Stokes semigroup, Leray projection, admissible Clay-domain solution theory, or a singular solution.

## Next formal step

The next useful formal direction is to move from the generic quadratic mild kernel toward a concrete Navier--Stokes adapter without smuggling in existence or global regularity.

High-value targets include:

1. an explicit function-space contract for the intended Clay domain, consistent with `SPEC.md` for the current `R^3` track;
2. a concrete projected convection operator interface with physical three-dimensional incompressibility preserved;
3. a residual/error theorem for approximate tangent reconstruction;
4. eventual instantiation of the abstract `H` and `Q` with genuine Stokes/Leray objects once the required mathlib infrastructure and analytic hypotheses are available.

Do not identify a finite-cylinder Hou operator with the Clay `R^3` or periodic-box problem unless a rigorous domain-transfer result has been proved.

## Numerical/research track

The numerical MNS-2 bridge work is distinct from the Lean continuum theorem.

Key numerical facts already established in the broader project:

- conservative cylindrical transport variables use `U = u^θ/r`, `Ω = ω^θ/r`, `ψ = ψ^θ/r`, `Γ = r² U = r u^θ`;
- tangent direction for amplitude-path reconstruction is fixed and unnormalized;
- v2.2 synthetic flow-map path-independence tests passed for radial, Gamma-first, Omega-first, and closed-rectangle paths under a single frozen schedule;
- finite-dimensional coordinate-path reconstruction is exact for the frozen discrete map;
- a continuum promotion still requires convergence of solution maps and pathwise tangent actions on a common time interval;
- a real provenanced Hou late-state handoff seed is still missing; synthetic seeds are not late-state evidence;
- full-operator low rank is not assumed; the more plausible reduced object is the pathwise tangent correction, and any POD/SVD reconstruction requires a residual certificate before promotion.

Planned numerical continuation is a modal/reduced tangent bridge with explicit truncation, path quadrature, tail, and path-order diagnostics before any continuum or Clay claim.

For promotion toward the current `R^3` primary track, apply every relevant physical/reconstruction/candidate-data gate in `SPEC.md` in addition to the numerical-stack-specific gates below.

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
- synthetic Hou-like data as provenanced Hou late-state evidence;
- finite-cylinder Hou behavior as an `R^3` or periodic-box Clay construction without a rigorous transfer.

Keep these error classes separate:

- exact path-integral identity;
- quadrature error;
- low-rank/modal truncation error;
- PDE discretization error;
- continuum-promotion error;
- domain-transfer error;
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

`@GitHub ns-mns2-flowmap-bridge の PROJECT_GOAL.md、SPEC.md、HANDOFF.md、AGENTS.md、FORMAL_SCOPE.md を読んで、Fable5 exclusion registry も照合して、最新PRとCIを確認して続きから。`

If continuing the formal track, proceed from the concrete Navier--Stokes / reduced-tangent certification obligations above while respecting the physical `R^3` contract in `SPEC.md`.

If switching back to the numerical track, resume from the reduced/modal tangent bridge, preflight against the external Fable5 registry, and preserve all `SPEC.md`, Clay-domain, and continuum-promotion guardrails above.
