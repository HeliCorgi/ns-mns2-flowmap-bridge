# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: 2026-09-05 JST (thirty-fourth session).

> **Historical archive.** The full session-by-session handoff through the
> twenty-ninth session is preserved at main commit
> `c69315e32eead48c1fd681bf86c8bab1af815e64` (PR #83 merge).  This live file is
> intentionally the short-form continuation point.  Current theorem/source files and
> dated gate records override stale prose.
>
> **Sessions 30–32: ASTRA S15 traveling-max cone explored, then parked.**
> Read, in order:
> `docs/gates/ASTRA_S15_TRAVELING_MAX_2026-09-05.md`,
> `docs/gates/ASTRA_S15_Q_DECISION_2026-09-05.md`, and
> `docs/gates/ASTRA_S15_D_DECISION_2026-09-05.md`.
> The exact moving-max identity is `A'=(2q-d)A^2`; the candidate cone
> `q>=1/4`, `0<=d<=1/8` gives conditional `A'>=(3/8)A^2`.  Q-UNIV was killed by
> remote pressure freedom and D-UNIV by local fourth-jet freedom.  The `(q,d)` S15
> realization is therefore **PARKED BY DEFAULT**.  PR #83 merged as
> `c69315e32eead48c1fd681bf86c8bab1af815e64`, PR #84 as
> `0fa9cadf998fcb5935812cfb56b4a86ea49c81cd`, and PR #85 as
> `084aa0d1fca1d89726af1f544f3689a95a3f71ba`.
>
> **2026-09-05 (thirty-third session): FREQUENCY / DISSIPATION-SCALE ROUTE OPENED.**
> Record: `docs/gates/FREQUENCY_DISSIPATION_TRANSFER_DECISION_2026-09-05.md`.
> This is a regularity-side cross-track gate; it does not silently replace the current
> `SPEC.md` breakdown-side priority.
>
> With a smooth inhomogeneous Littlewood–Paley decomposition `u_j=Delta_j u`,
> `lambda_j=2^j`, define one-viscous-window lengths
> `tau_j=a_*/(nu lambda_j^2)` and the signed vector Duhamel injection
>
> `I_j(t) = lambda_j^(-1) || int_{max(0,t-tau_j)}^t
>              exp(nu(t-s)Delta) Delta_j P div(u tensor u)(s) ds ||_infinity`.
>
> **FDT-INJ asks:** for every `nu>0`, every real divergence-free Schwartz datum,
> and every finite horizon `L`, is there a datum-dependent finite `J` such that
>
> `sup_{0<t<min(L,T_*)} sup_{j>=J} I_j(t) <= (1/2)c_0 nu`?
>
> **FDT-INJ remains OPEN.**  A first-contact argument in the gate shows that YES would
> bound the dissipation wavenumber on each finite horizon, make the Cheskidov–Shvydkoy
> coefficient `F` integrable, and yield a route to whole-space regularity A after the
> standard Clay admissibility checks.  A static energy-only shortcut was killed.
> PR #86 merged as `2fa19df787201a3f306043fd632f569fc245cf4c`.
>
> **2026-09-05 (thirty-fourth session): FDT LOW–HIGH GATE ATTACKED.**
> Record: `docs/gates/FDT_LH_DECISION_2026-09-05.md` on branch
> `research/fdt-lh-decision`.
>
> The broad phrase “FDT-LH” is split into an operator/energy-budget question and a
> genuinely signed dynamic question.  For low `a` and high `b`, define
>
> `C_j(a,b) = P [Delta_j, a·grad] b`
>
> and the frozen one-window operator
>
> `W_j(a,b) = lambda_j^(-1) int_0^{tau_j}
>                 exp(nu(tau_j-s)Delta) C_j(a,b) ds`.
>
> The exact Fourier symbol is
>
> `i P(xi) int ((xi-eta)·a_hat(eta))
>               [phi_j(xi)-phi_j(xi-eta)] b_hat(xi-eta) d eta`.
>
> Because the LP multiplier changes on its transition annulus, one can choose separated
> low/high frequencies and divergence-free polarizations for which this symbol is
> nonzero.  Smooth compact Fourier bumps plus conjugate symmetry give **real
> divergence-free Schwartz** profiles `a,b` with `C_0(a,b) != 0`.  Heat integration
> does not annihilate it because its multiplier
> `(1-exp(-a_*|xi|^2))/|xi|^2` is strictly positive on the nonzero support.
>
> Fix `||b||_infinity=1`, `0<epsilon<1`, and set
>
> `a_{j,M}(x)=M nu lambda_j a(lambda_j x)`,
> `b_j(x)=epsilon c_0 nu lambda_j b(lambda_j x)`.
>
> Then the high packet is strictly subcritical,
> `lambda_j^(-1)||b_j||_infinity=epsilon c_0 nu`, while exact critical scaling gives
>
> **`||W_j(a_{j,M},b_j)||_infinity
>     = M epsilon Gamma_LH c_0 nu`**, `Gamma_LH>0`.
>
> Thus any fixed margin is violated by choosing `M` large.  At the same time
>
> `||a_{j,M}+b_j||_2^2 = O(lambda_j^(-1)) -> 0`,
>
> and
>
> `nu tau_j ||grad(a_{j,M}+b_j)||_2^2 = O(lambda_j^(-1)) -> 0`.
>
> Therefore **`FDT-LH-OP = NO`**: spectral separation, incompressibility, Leray,
> annular heat damping, a subcritical target high block, and the ordinary energy /
> one-window enstrophy budget do **not** force a fixed low-high commutator margin.
> This is an analytic theorem-level obstruction, not a numerical observation.
>
> For the actual local NS solution with datum `u_0=a_{j,M}+b_j`, the signed low-high
> Duhamel vector has exact right derivative at zero
>
> `d/dt J_j^LH(0) = lambda_j^(-1) C_j(a_{j,M},b_j)`,
>
> which can be arbitrarily large while the initial energy tends to zero.  Hence no
> pointwise-in-time energy-budget coefficient can repair the operator estimate.
>
> **Important scope:** this does **not** refute FDT-INJ.  The counterfamily uses
> different data as `j` changes, while FDT-INJ allows `J=J(u_0,nu,L)`.  It also does
> not rule out cancellation in the actual signed time-dependent window.  Rename that
> surviving question **FDT-LH-DYN**.  No Lean/runtime source changed; `FORMAL_SCOPE.md`
> and `STATUS.md` intentionally remain unchanged.

This is the durable continuation point for future GPT sessions.  Do not rely on chat history.

## Resume protocol

Follow `docs/GPT_WORKFLOW.md`. Read, in order:

1. `PROJECT_GOAL.md`;
2. `SPEC.md`;
3. `AGENTS.md`;
4. `FORMAL_SCOPE.md`;
5. this file;
6. `docs/LEAN_CI_OPERATIONS.md`;
7. `docs/gates/FREQUENCY_DISSIPATION_TRANSFER_DECISION_2026-09-05.md`;
8. `docs/gates/FDT_LH_DECISION_2026-09-05.md`;
9. for why S15 is parked, the three Astra S15 gate records;
10. current GitHub `main`, open PRs, and the relevant Stokes/Leray/convection formal files.

## Handoff update contract

Every substantive session must, before ending:

1. record what was executed and what was deliberately not claimed;
2. rewrite **Next work** below with the exact next gate, read order, and forbidden shortcuts;
3. update `STATUS.md` / `FORMAL_SCOPE.md` only if the formal frontier actually moved;
4. keep the durable continuation here, not only in chat, PR comments, or commit messages.

### Next work (written 2026-09-05, thirty-fourth session)

Read first: the session-33/34 blocks above,
`docs/gates/FREQUENCY_DISSIPATION_TRANSFER_DECISION_2026-09-05.md` §§0–10, and
`docs/gates/FDT_LH_DECISION_2026-09-05.md` §§0–10.

- **Current target/state:** `FDT-INJ` is still **OPEN**.  The natural
  operator/absolute low-high closure is now **KILLED** as `FDT-LH-OP = NO`.  The
  surviving low-high question is **FDT-LH-DYN**, which must consume actual signed
  time evolution rather than energy-budget smallness.  The old S15 `(q,d)` cone
  remains parked.
- **Next analytic gate: FDT-LH-DYN / low-flow conjugation.**  Conjugate a high block
  by the divergence-free low-frequency flow over one viscous window (paracomposition
  / Lagrangian renormalization).  Derive the exact deformation-of-frequency and
  heat-commutator terms.  Decide counterexample-first whether their signed vector
  contribution admits a fixed critical margin with a coefficient whose time budget
  is already known independently of continuation.
- **Required symbolic test:** use a trace-free affine strain as the local model.
  Constant translation is not the obstruction because radial LP multipliers commute
  with translations; strain is the mechanism that moves frequency and creates the
  nonzero commutator symbol.
- **If FDT-LH-DYN = NO:** state whether the obstruction only kills the FDT proof
  strategy or also produces an actual fixed-datum NO certificate for FDT-INJ.  Do not
  conflate a scaling family of data with the fixed-datum quantifiers of FDT-INJ.
- **If FDT-LH-DYN survives:** next attack the comparable-high/high backscatter term,
  then the high-low summable tail.  Only after a load-bearing analytic estimate
  survives should any LP/Bony Lean plumbing be commissioned.
- **Forbidden repairs:** do not insert `int F`, `int ||grad u||_infinity`, a Serrin
  norm, bounded `H^3`, or another continuation criterion; do not replace the signed
  time integral by an integral of norms and call it equivalent; do not use the
  `FDT-LH-OP` counterfamily as a claimed refutation of FDT-INJ; do not change
  `SPEC.md` to an A-side program yet.

## Repository / verification state

- `main` at start of session 34: `2fa19df787201a3f306043fd632f569fc245cf4c`
  (merged PR #86).
- Current branch: `research/fdt-lh-decision`.
- FDT-LH decision record first commit:
  `3306bbead924c1f7c4c8812c5bf5b206b6eb6d01`.
- No Lean/runtime source changed in session 34; `FORMAL_SCOPE.md` and `STATUS.md` remain
  intentionally unchanged.
- Latest completed hosted integration check: PR #86, workflow `Lean 4 formalization`,
  run **#262** (`33948255282`), job `101258127783`, conclusion **success**; source
  proof-hole/local-axiom scan and cached full build both passed.  The prior exact
  formal baseline remains Lean 4.32.1 / **8777 jobs PASS**.
- GitHub-hosted Actions remain a final/status resource, not an interactive compiler.

## Project claim boundary

Ultimate target: an exact official Clay/Fefferman A/B/C/D statement.  No current result proves
3D Navier–Stokes global regularity or blow-up.  The newest result is negative knowledge on the
regularity-side reduction: the low-high commutator has no intrinsic fixed critical margin from
ordinary energy/dissipation budgets, even with a subcritical target high block.  The full signed
FDT-INJ route remains open and now requires genuinely dynamical cancellation or a different
renormalized object.
