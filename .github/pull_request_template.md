## Clay target alignment

<!-- Read PROJECT_GOAL.md first. State which official Clay/Fefferman statement (A/B/C/D) this PR is intended to support, or write `infrastructure / no direct Clay statement`. For a breakdown-side route, state whether it is unforced (`f = 0`) or forced. -->

## Mathematical / numerical claim

<!-- State exactly what this PR establishes. -->

## Assumptions

<!-- List new analytic, numerical, discretization, provenance, domain-transfer, or regularity assumptions. -->

## Implementation

<!-- Lean theorem names, scripts, tests, reports, or artifacts changed by this PR. -->

## What this does NOT prove

<!-- Explicitly state nearby stronger claims that remain unproved. In particular, do not silently promote a conditional bridge, Hou-cylinder computation, or discrete map to Clay A/B/C/D. -->

## Invariants / guardrails checked

- [ ] `PROJECT_GOAL.md` was checked and the claim is labeled at its actual Clay relevance level.
- [ ] The Fable5 exclusion/no-go registry was checked for a matching killed or conditional route when relevant.
- [ ] The physical 3D equation/domain is not silently replaced by a reduced, lifted, finite-cylinder, or discrete system.
- [ ] Fixed path tangent is derived from the path and is not silently normalized or retuned.
- [ ] Discrete/numerical evidence is not promoted to a continuum theorem without a convergence argument.
- [ ] Synthetic data are not described as Hou late-state evidence without provenance.
- [ ] Formal assumptions match the prose claim.

## Formal proof hygiene

- [ ] No `sorry` or `admit`.
- [ ] No new local `axiom` or proof-hiding `opaque` declaration.
- [ ] `lake build` passes if Lean files changed.

## Runtime impact

<!-- State whether numerical/runtime behavior changes. Use “none” for proof/docs-only PRs. -->

## CI

<!-- Link or summarize the relevant successful run once available. -->
