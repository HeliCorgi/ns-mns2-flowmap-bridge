# MNS-2 v2.14 abstract-regularity failcases

## FC-086 — Generic energy + harmonic-analysis estimates promoted to Navier–Stokes regularity

**Failure:** a proof treats the Navier–Stokes nonlinearity only through generic upper-bound function-space estimates together with the energy cancellation/identity, and then promotes those abstract bounds to global regularity, finite-time continuation, or a Clay A/B conclusion for the true three-dimensional equation.

**Why it fails:** Tao's averaged three-dimensional Navier–Stokes construction preserves the energy cancellation and essentially the same upper-bound harmonic-analysis estimates while admitting smooth finite-time blow-up. Therefore those coarse properties alone cannot distinguish the true Navier–Stokes nonlinearity strongly enough to prove global regularity.

**Required gate:** any positive regularity or continuation argument that goes beyond standard local theory must identify the additional structure of the exact Leray-projected convection operator that is used. If the argument would apply unchanged after replacing the exact bilinear term by Tao's averaged bilinear operator, it does not establish the desired true-Navier–Stokes conclusion.

**Primary reference:** Terence Tao, *Finite time blowup for an averaged three-dimensional Navier-Stokes equation*, arXiv:1402.0290, https://arxiv.org/abs/1402.0290 .

**Historical context:** the 2014 discussion around Otelbayev's proposed abstract approach is recorded at https://mathoverflow.net/questions/154440/otelbayevs-approach-to-navier-stokes . This link is context, not the rigorous no-go theorem used by this failcase.

## FC-087 — `FlowMapContinuationPackage` discharged from `L²` energy control or a generic quadratic carrier

**Failure:** the field `continuation_of_uniform_endpoint_bound` in `FlowMapContinuationPackage` is instantiated merely from bounded kinetic energy, bounded `L²(R³)` norm, or an abstract quadratic evolution estimate, without a concrete strong-solution restart theorem in the same normed carrier.

**Why it fails:** the bridge theorem only says that a uniform directional flow-map derivative bound gives a uniform endpoint bound. It does not say that every endpoint norm is a continuation norm. In three-dimensional Navier–Stokes, the energy inequality supplies an `L²` bound, but that alone is not a strong-solution continuation theorem. FC-086 also forbids manufacturing the missing continuation step from generic quadratic estimates plus energy cancellation.

**Required gate:** instantiate the continuation field only after proving or importing a concrete local well-posedness/restart theorem in a genuine strong carrier, with an explicit lifespan lower bound depending on the carrier norm. For the present `R³`, unforced track, an admissible target is an `H^m`-type strong theory with integer `m > 5/2`, matching `SPEC.md`. The exact PDE, divergence-free subspace, norm, restart time, and uniqueness/coherence hypotheses must be visible in the formal interface.
