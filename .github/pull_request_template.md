## Mathematical / numerical claim

<!-- State exactly what this PR establishes. -->

## Assumptions

<!-- List new analytic, numerical, discretization, provenance, or regularity assumptions. -->

## Implementation

<!-- Lean theorem names, scripts, tests, reports, or artifacts changed by this PR. -->

## What this does NOT prove

<!-- Explicitly state nearby stronger claims that remain unproved. In particular, do not silently promote a conditional bridge to Navier–Stokes global regularity, blow-up, or a continuum theorem. -->

## Invariants / guardrails checked

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
