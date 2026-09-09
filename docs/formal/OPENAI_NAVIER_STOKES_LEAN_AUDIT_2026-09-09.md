# OpenAI Navier–Stokes paper — adversarial Lean audit

Date: 2026-09-09 JST

Source under audit:

- `Finite Time Blowup for Navier–Stokes`, OPENAI, 166 pages.
- PDF: `https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf`

This is an adversarial formalization exercise. The purpose is to force load-bearing steps into explicit theorem statements and see where hypotheses, sign conditions, endpoint regularity, compact-support claims, or infinite summations become difficult to state and prove. Difficulty in Lean is not itself a mathematical gap, and a successful local formalization is not evidence for the whole manuscript.

## Paper claim being audited

Theorem 1.1 states, for every viscosity `nu > 0`, existence of a smooth compactly supported force on `R^3 x (0,infinity)`, zero initial velocity, and a smooth solution on `[0,1)` with uniformly bounded kinetic energy and unbounded `L^infinity` velocity as `t -> 1`. The paper says this establishes Fefferman alternative (C), with a compact-support periodicization giving (D).

We do **not** encode Theorem 1.1 as an axiom or opaque proposition.

## Dependency spine to attack

First-pass reading identifies the following load-bearing chain:

1. **Theorem 4.6 / Appendices A–C:** existence of the leading profile with the required axis regularity, moment matching, heat exterior, positivity, and admissible stress cone.
2. **Lemma 4.5:** algebraic equivalence and large-`p_s,1` sufficient condition for the stress cone.
3. **Propositions 7.5–7.6:** positive wave-covariance realization of the prescribed stress and differentiated amplitude corrections.
4. **Lemmas 9.7–9.8 + Proposition 9.9:** iteration/summation of corrections while preserving Cartesian regularity, endpoint regularity, exterior structure, residual decay, and inner growth.
5. **Lemma 10.2:** every Cartesian space-time derivative of the localized residual has a uniform `t -> 1-` limit on all of `R^3`, with compatible derivatives and fixed compact support.
6. **Lemma 10.3:** realization of those one-sided jets by a globally smooth compactly time-supported force.
7. **Lemma 10.5:** uniqueness/comparison on every `[0,T]`, `T<1`, for smooth solutions with only a uniform spatial `L^2` bound stated globally.
8. **Theorem 1.1 final step:** transfer of the explicit inner asymptotic to `L^infinity` blowup, exclusion of a global bounded-energy smooth competitor, and viscosity rescaling.

These are audit priorities, not accusations of error.

## Phase 1 — algebra with zero analytic assumptions

Implemented in `Formal/OpenAINavierStokesAudit.lean`:

- equation (4.20), `v_s = a(1+t_s^2) = a + b_s^2/a`;
- the `P_c` and `J_c` substitutions under `p_{s,2}=w p_{s,1}`;
- the factorization displayed in the proof of Lemma 4.5;
- the normalized threshold polynomial expansion used after the compactness argument.

These lemmas use only field algebra and have no paper theorem imported as an assumption.

## Next audit targets

### A. Finish Lemma 4.5 exactly

Formalize the equivalence between the square-root inequality (4.21) and polynomial cone test (4.22), including the domain `P_c>2`, `v_s>2`, the root ordering `2 < v_- <= P_c`, and every sign condition used to cancel positive factors. Then formalize the compact-set threshold argument rather than treating compactness as prose.

This is deliberately early because a missing sign or endpoint condition here propagates into the wave-realization layer.

### B. Proposition 7.5 covariance cone

Encode the two covariance vectors, positivity of squared amplitudes, and the exact statement that the required stress lies in their positive span. Check behavior as the stress becomes flat at annulus edges: normalized direction extension and positivity must not silently divide by a vanishing stress.

### C. Proposition 9.9 summation

This is the first major analytic stress test. Separate:

- local finiteness away from `q=0`;
- convergence near the singular point;
- differentiation under the infinite sum;
- preservation of divergence-free structure after cutoffs;
- compatibility of one-sided time derivatives of all orders;
- uniformity needed later in Lemma 10.2.

A Lean model should make all topologies and uniformity domains explicit.

### D. Lemmas 10.2–10.3 endpoint forcing

Audit the passage from derivative-wise one-sided limits to a single smooth spacetime force with compact support. In particular distinguish:

- spatial compatibility of the jets;
- time-jet compatibility;
- uniform support in a fixed compact `K`;
- smooth extension through `t=1`;
- subsequent cutoff in time without changing the pre-singular equation.

### E. Lemma 10.5 comparison

Formalize the uniqueness class actually used. The manuscript states smoothness plus `L^infinity_t L^2_x` on `[0,T]`; the proof invokes localized energy identities, pressure recovery, Sobolev approximation, and `H^3 -> W^{1,infinity}` for the constructed solution. The exact hypotheses on the competitor needed to justify integration by parts and the pressure term should be made theorem-visible.

## Gap labels

Use only these statuses:

- `FORMALIZED`: exact source step proved from explicit hypotheses.
- `FORMALIZATION_DEBT`: source step appears standard/credible but the Lean proof is unfinished.
- `HYPOTHESIS_MISMATCH`: proof needs a hypothesis not present in the source theorem/lemma statement.
- `SOURCE_AMBIGUITY`: notation or scope is insufficiently precise to determine one theorem statement.
- `POTENTIAL_GAP`: a concrete logical implication fails or an essential hypothesis cannot be recovered from earlier proved statements.

Do not use `POTENTIAL_GAP` merely because mathlib lacks infrastructure or because a proof is long.

## Current status

No mathematical gap has been established. Phase 1 only begins the exact transcription of the stress-cone algebra. The highest-value later targets are Proposition 9.9 and Lemmas 10.2/10.5 because they connect the local multiscale construction to a globally smooth compact force and to the final nonexistence conclusion.
