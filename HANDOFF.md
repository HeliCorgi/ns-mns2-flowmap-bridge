# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: 2026-09-05 JST (thirty-third session).

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
> The exact moving-max identity is
> `A'=(2q-d)A^2`; the candidate cone `q>=1/4`, `0<=d<=1/8` gives the conditional
> algebraic growth `A'>=(3/8)A^2`.  Both proposed universal inward barriers were
> independently killed: **Q-UNIV = NO** by a remote negative-swirl pressure torus
> that preserves the local maximum jet while sending the normalized pressure term
> negative, and **D-UNIV = NO** by the local quartic pure-swirl perturbation
> `Phi_M=-M(r-r0)^4 chi`, which preserves the zero-through-third maximum jet while
> sending the normalized fourth-order term outward.  The `(q,d)` S15 realization is
> therefore **PARKED BY DEFAULT**.  Reopening requires one propagated structure that
> excludes both counterfamilies and is weaker than a known regularity criterion.
> PR #83 merged as `c69315e32eead48c1fd681bf86c8bab1af815e64`, PR #84 as
> `0fa9cadf998fcb5935812cfb56b4a86ea49c81cd`, and PR #85 as
> `084aa0d1fca1d89726af1f544f3689a95a3f71ba`.
>
> **2026-09-05 (thirty-third session): FREQUENCY / DISSIPATION-SCALE ROUTE OPENED.**
> Record: `docs/gates/FREQUENCY_DISSIPATION_TRANSFER_DECISION_2026-09-05.md` on branch
> `research/frequency-dissipation-transfer-decision`.  This is deliberately a
> **regularity-side cross-track gate**; it does not silently replace the current
> `SPEC.md` breakdown-side priority.
>
> Fix a smooth inhomogeneous Littlewood–Paley decomposition `u_j=Delta_j u`,
> `lambda_j=2^j`, and the Cheskidov–Shvydkoy dissipation wavenumber `Q(t)`,
> `Lambda=2^Q`, with low-mode coefficient
> `F(t)=sup_{j<=Q} lambda_j ||u_j||_infinity`.  The published continuation input is
> `int_0^T F < infinity => continuation`; energy supplies only `Lambda in L^1`, while
> `Lambda in L^(5/2)` or a terminal-time-uniform small critical high-frequency tail
> is sufficient.
>
> The new exact decision object is **FDT-INJ**.  Choose fixed annular heat constants
> `C_H,c_H` and `a_*>0` with `C_H exp(-c_H a_*)<=1/4`, set the one-viscous-window
> length `tau_j=a_*/(nu lambda_j^2)`, and define
>
> `I_j(t) = lambda_j^(-1) || int_{max(0,t-tau_j)}^t
>              exp(nu(t-s)Delta) Delta_j P div(u tensor u)(s) ds ||_infinity`.
>
> **FDT-INJ asks:** for every `nu>0`, every real divergence-free Schwartz datum,
> and every finite horizon `L`, does there exist a finite datum-dependent `J` such
> that
>
> `sup_{0<t<min(L,T_*)} sup_{j>=J} I_j(t) <= (1/2)c_0 nu`?
>
> **Current verdict: OPEN.**  The norm is intentionally outside the time integral so
> time/phase/polarization/triad cancellations remain available.  A first-contact
> argument is fully recorded in the gate: Schwartz initial-tail smallness gives a
> `1/4` margin; one viscous-window Stokes decay gives another `1/4` homogeneous bound;
> FDT-INJ gives a `1/2` nonlinear bound; therefore no sufficiently high block can hit
> `lambda_j^(-1)||u_j||_infinity=c_0 nu`.  Hence `Q` is bounded on each finite horizon,
> `F` is integrable, and the published criterion continues the solution.  Under the
> stated universal quantifiers a YES would therefore provide a whole-space
> regularity-A route after the standard Clay admissibility checks.
>
> A tempting static shortcut was killed in the same record.  A datum-independent
> pointwise estimate `F(t)||u(t)||_2^2 <= C(nu)||grad u(t)||_2^2` is false already at
> `t=0`: for single-annulus divergence-free Schwartz data
> `u_0^{A,lambda}(x)=A v(lambda x)`, with `A/lambda` above the dissipation threshold,
> the ratio of the two sides scales like `A/lambda` and can be made arbitrarily large.
> Thus the new route must be genuinely dynamical; energy plus a static spectrum is
> not the missing theorem.
>
> The gate deliberately adds **no Lean theorem**.  Existing formal assets include the
> exact R3 Stokes/Leray/frequency infrastructure, positive-time H2->H3 Stokes
> smoothing, projected `H3 x H3 -> H2` convection, and Fourier convolution/Young
> bridges.  Missing FDT-specific layers are Littlewood–Paley projectors, annular
> L-infinity Bernstein/heat bounds, dyadic projected Duhamel in L-infinity, and the
> Bony commutator package.  Do not build this plumbing before an analytic sub-gate
> survives.

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
8. for why S15 is parked, the three Astra S15 gate records named above;
9. current GitHub `main`, open PRs, and the relevant Stokes/Leray/convection formal files.

## Handoff update contract

Every substantive session must, before ending:

1. record what was executed and what was deliberately not claimed;
2. rewrite **Next work** below with the exact next gate, read order, and forbidden shortcuts;
3. update `STATUS.md` / `FORMAL_SCOPE.md` only if the formal frontier actually moved;
4. keep the durable continuation here, not only in chat, PR comments, or commit messages.

### Next work (written 2026-09-05, thirty-third session)

Read first: the session-33 block above and
`docs/gates/FREQUENCY_DISSIPATION_TRANSFER_DECISION_2026-09-05.md` §§0–10.

- **Current target/state:** `FDT-INJ` is **OPEN**.  It is the active theorem-shaped
  frequency/dissipation-scale decision.  It is regularity-side and cross-track; the
  current `SPEC.md` breakdown specialization is not yet changed.  The old S15 `(q,d)`
  cone remains parked.
- **Next analytic gate: FDT-LH.**  Freeze one sufficiently high dyadic block `j` and
  one viscous window `tau_j`.  Write the exact Bony low–high piece as a transport term
  plus `[Delta_j,u_{<=j-2}·grad]u_j`-type commutator after Leray projection.  Decide,
  counterexample-first, whether its contribution to the vector Duhamel injection can
  be bounded by a fixed fraction of `c_0 nu` using a coefficient with an independently
  finite time budget.
- **If FDT-LH = NO:** record the exact actual-trajectory or theorem-level obstruction
  and decide whether it kills FDT-INJ or only that decomposition estimate.  Do not
  “repair” it by inserting `int F`, `||grad u||_infinity`, a Serrin norm, bounded H3,
  or another continuation criterion.
- **If FDT-LH survives:** next attack the comparable-high/high backscatter term, then
  the high–low summable tail.  Only after a load-bearing analytic estimate survives
  should any Littlewood–Paley/Bony Lean layer be commissioned.
- **Exact NO requirement for FDT-INJ:** one fixed `nu`, one fixed Schwartz datum, one
  finite horizon, and its actual solution must exhibit arbitrarily high blocks with
  one-window injection `I_j>(1/2)c_0 nu`.  A family of different bad data with the
  active block moved upward does not refute FDT-INJ because `J` is datum-dependent.
- **Forbidden shortcuts:** do not replace the norm of the time-integrated nonlinear
  vector by the integral of norms without explicitly accepting a stronger theorem;
  do not infer frequency transfer from shell energies alone; do not rely only on
  properties shared by Tao's averaged blow-up operator; do not claim that S7/S8 or
  FDT-INJ is already proved; do not change `SPEC.md` to an A-side program unless a
  genuinely surviving theorem justifies that strategic switch.

## Repository / verification state

- `main` at start of session 33: `084aa0d1fca1d89726af1f544f3689a95a3f71ba`
  (merged PR #85).
- Current branch: `research/frequency-dissipation-transfer-decision`.
- FDT gate first commit: `5141b8c95c423f8324ecdf2f0cbfcd7c4e51e6c5`.
- No Lean/runtime source changed in session 33; `FORMAL_SCOPE.md` and `STATUS.md` remain
  intentionally unchanged.
- Latest completed hosted integration check before this branch: PR #85, workflow
  `Lean 4 formalization`, run **#261** (`33934510992`), conclusion **success**.
  The formal tree was unchanged from the prior verified traveling-max tree; the
  proof-hole/local-axiom/opaque scan and full cached build passed.  The prior exact
  full-build baseline is Lean 4.32.1 / **8777 jobs PASS**.
- GitHub-hosted Actions remain a final/status resource, not an interactive compiler.

## Project claim boundary

Ultimate target: an exact official Clay/Fefferman A/B/C/D statement.  No current result proves
3D Navier–Stokes global regularity or blow-up.  The newest active result is an **open reduction**:
`FDT-INJ` would imply a known frequency continuation criterion by a first-contact argument, while a
static energy-only shortcut has been analytically ruled out.  This is research-direction refinement,
not a Clay result.
