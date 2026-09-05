# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: 2026-09-05 JST (thirty-first session).

> **Historical archive.**  The full session-by-session handoff through the
> twenty-ninth session is preserved verbatim at main commit
> `c69315e32eead48c1fd681bf86c8bab1af815e64` (the PR #83 merge).  This file is
> intentionally compacted back to its stated role as the short-form continuation point;
> old research rulings are not rescinded by the compaction.  Current source/theorem
> statements and the dated gate records remain authoritative.
>
> **2026-09-05 (thirtieth session): ASTRA S15 TRAVELING-MAX ATTEMPT EXECUTED.**
> The user commissioned a direct attempt on the current `R^3`, `f = 0`,
> axisymmetric-with-swirl breakdown track, after a short re-audit of Shahmurov
> arXiv:2606.07869v1.  The D-3 verdict stayed unchanged: correctness NOT
> ESTABLISHED because the recorded G1a/G1b variational-class gap and G2
> exhaustion/routing gap remain load-bearing; the paper is consumed by nothing.
> Record: `docs/gates/ASTRA_S15_TRAVELING_MAX_2026-09-05.md`.
> From the audited NS equations the record derives, under an explicit smooth unique
> nondegenerate off-axis positive maximizer branch,
> `U = u^theta/r`, `S = psi1_z = -u^r/r`, `A = U(x_*)`,
> `q = S_*/A`, `d = -nu(L5 U)_*/A^2`, and the exact amplitude identity
> **`A' = (2q-d)A^2`**.  The proposed cone is
> `q >= 1/4`, `0 <= d <= 1/8`; inside it the elementary coefficient bound is
> **`A' >= (3/8)A^2`**.  The exact normalized boundary equations isolate two
> analytic obligations: **Q** at `q=1/4`,
> `Pi + e + d/4 + m >= 17/16`, and **D** at `d=1/8`,
> `h - 2e - f <= 1/32` (the commutator sign was rechecked and corrected before
> commit).  No invariant-region theorem, cone entry, maximizer persistence, NS
> breakdown, or Clay alternative is claimed.
>
> PR **#83** (`Research: traveling-max invariant cone for Astra S15`) added the
> research record plus `Formal/R3TravelingMaxInvariantCone.lean` and
> `Formal/R3TravelingMaxInvariantConeAudit.lean`.  Lean scope is deliberately only
> three real-algebra consequences: `travelingMax_growthCoefficient`,
> `travelingMax_qBoundary_inward`, `travelingMax_dBoundary_inward`; no PDE identity
> is asserted in Lean.  GitHub-hosted Lean run **#259** (`33930424998`, job
> `101207713329`) on the PR merge ref completed successfully under
> `leanprover/lean4:v4.32.1`: proof-hole/local-axiom scan PASS; full `lake build`
> **8777 jobs PASS**; the three new axiom prints contain only `propext`,
> `Classical.choice`, `Quot.sound`.  PR #83 was merged as
> `c69315e32eead48c1fd681bf86c8bab1af815e64`.
>
> **2026-09-05 (thirty-first session): THE Q YES/NO DECISION IS EXECUTED —
> `NO (UNIVERSAL-Q FALSE)`.**
> Record: `docs/gates/ASTRA_S15_Q_DECISION_2026-09-05.md` on branch
> `research/astra-s15-q-decision`.  The exact decision object is **Q-UNIV**:
> whether every admissible smooth compactly supported axisymmetric-with-swirl datum
> having at `t=0` a unique positive nondegenerate off-axis `U` maximum with
> `q=1/4`, `0<=d<1/8` must satisfy Q.  **Answer: NO.**
> The counterfamily is analytic, not numerical.  Fix a compactly supported local
> core whose complete maximum jet gives `q=1/4`, `e=m=0` and
> `0<d=nu*kappa/A<1/8`.  Add a disjoint thin **negative pure-swirl torus** at
> radius `R>r_*`.  It is `C_c^infty`, axisymmetric and divergence-free; because its
> normalized swirl is nonpositive it cannot replace the positive `U` maximum, and
> because it vanishes near the maximum it changes none of
> `A,q,d,e,m,H,nabla S,L5 S,nabla L5 U` there.  Its only relevant effect is the
> nonlocal pressure.
>
> The load-bearing sign is exact.  For the tangential line stress on a ring,
> with `G(x)=1/(4*pi*|x|)` and
> `J(r,R)=int_0^{2pi} G((r,0,0)-R e_r(theta)) dtheta`, integration by parts in
> `theta` gives `P_R = partial_R J`.  For `0<r<R`,
> `J=(1/(2R))*sum_{n>=0} c_n^2 (r/R)^(2n)`,
> `c_n=binom(2n,n)/4^n>0`, hence
> **`partial_r partial_R J = -sum_{n>=1} n(2n+1)c_n^2
> r^(2n-1)R^(-2n-2) < 0`**.  A smooth thin-torus approximation preserves this
> strict sign.  Scaling its amplitude by `B` gives
> `partial_r p_remote(x_*) = B^2 C_epsilon`, `C_epsilon<0`.
> Disjoint supports make the quadratic stresses add exactly, so
> `Pi_B = Pi_core + B^2 C_epsilon/(r_* A^2) -> -infinity` while all local Q
> data stay fixed.  Therefore for large `B`, Q fails and the exact moving-max
> identity gives **`q'(0)<0` for the actual local Navier–Stokes solution**.
>
> **Ruling:** **Q-UNIV is KILLED / NO.**  Consequently no proof using only the
> local maximum jet (or any hypothesis preserved by the remote-torus perturbation)
> can establish Q class-wide, and pressure does not automatically rescue the local
> two-variable depletion skeleton.  This does **not** kill the conditional algebra
> `Q + D + cone entry => A' >= (3/8)A^2`, does not decide D, and does not rule out
> a specially selected datum whose *global dynamical coherence* enforces Q along its
> trajectory.  Rename that residual existential obligation **Q-SPEC**.  Any Q-SPEC
> proof must explicitly consume a global hypothesis violated by the remote-torus
> counterfamily.  Merely sharpening Hessian/curvature/maximizer-relay algebra is a
> forbidden repeat.  No Lean source changed in the Q decision; `FORMAL_SCOPE.md`
> therefore did not move.

This is the short-form continuation point for future GPT sessions.  The repository is
expected to be developed primarily through repeated GPT sessions; do not rely on chat
history as durable state.

## Resume protocol

Follow `docs/GPT_WORKFLOW.md`. Read, in order:

1. `PROJECT_GOAL.md`;
2. `SPEC.md`;
3. `AGENTS.md`;
4. `FORMAL_SCOPE.md`;
5. this file;
6. `docs/LEAN_CI_OPERATIONS.md`;
7. `docs/gates/ASTRA_S15_TRAVELING_MAX_2026-09-05.md`;
8. `docs/gates/ASTRA_S15_Q_DECISION_2026-09-05.md`;
9. current GitHub `main`, relevant `Formal/` files, open PRs, and latest Lean
   verification evidence.

Current code and theorem statements override stale prose.  For pre-Astra history, consult
this file at `c69315e32eead48c1fd681bf86c8bab1af815e64` and the dated gate records;
do not reconstruct old rulings from chat history.

## Handoff update contract (standing specification)

**Specification (user directive, 2026-09-02): every session that does substantive work
MUST, before ending, write into this file what the next work is, in a form a fresh
session can execute without this session's chat history.**  Concretely, at end of
session:

1. update the dated block at the top of this file with what was executed, what was
   verified (exact gate evidence: runner, toolchain, scope, job count), and what was
   deliberately **not** done;
2. rewrite the **"Next work"** subsection below — it must name the next task(s) in
   recommended order, the exact files/records a fresh session must read first, any
   commission boundary, and any tempting-but-forbidden shortcut;
3. keep `STATUS.md` and `FORMAL_SCOPE.md` synchronized when the formal frontier moved
   (per `AGENTS.md`);
4. never leave the next-work description only in a commit message, chat reply, PR
   comment, or ephemeral plan — this file is the durable continuation point.

### Next work (written 2026-09-05, thirty-first session)

Read first: the thirtieth/thirty-first session blocks above;
`docs/gates/ASTRA_S15_TRAVELING_MAX_2026-09-05.md` §§2–6;
`docs/gates/ASTRA_S15_Q_DECISION_2026-09-05.md` §§0,2–7; `SPEC.md` §§2–6.

- **Current target/state:** the Astra S15 realization is a **conditional existential
  route with its universal Q mechanism killed**.  Q-UNIV = NO/KILLED by the remote
  negative-swirl pressure-poisoning counterfamily.  **Q-SPEC remains OPEN**: one
  specially chosen trajectory may still possess a global pressure/relay coherence that
  rules out the counterfamily.  **D remains OPEN**.  The conditional cone algebra and
  its three Lean real-algebra theorems remain valid.  There is no Clay claim.
- **Latest Lean verification:** runner = GitHub-hosted Actions; workflow = `Lean 4
  formalization`; run #259 / `33930424998`; job `101207713329`; checked PR #83
  merge ref for head `33e6ceecb1a6afb615718619809f87e959f8641b` under
  `leanprover/lean4:v4.32.1`; scope = source scan + full `Formal.+` / 8777 jobs;
  result = PASS; new theorem axiom prints standard only.  Q-decision work is docs-only,
  so it does not change the formal verification boundary.
- **Completed infrastructure:** `ASTRA_S15_TRAVELING_MAX_2026-09-05.md` (exact
  moving-max equations + conditional cone); `R3TravelingMaxInvariantCone.lean` and
  its audit (three algebraic theorems); `ASTRA_S15_Q_DECISION_2026-09-05.md`
  (Q-UNIV no-go via exact pressure-ring sign + smooth remote-torus counterfamily).
- **Next analytic gate, recommended order (each is a new user act):**
  1. **Q-SPEC global-coherence decision.**  Ask whether any *natural global condition
     already compatible with the current `R^3`, `f=0` candidate track* forbids remote
     pressure poisoning and is dynamically preserved up to the proposed first contacts.
     Counterexample-first.  A surviving condition must be stated as an exact pressure
     integral/sign inequality or another explicit global invariant and must identify
     exactly which feature of the remote torus it excludes.  If no such condition is
     found without importing a regularity wall, **PARK the Astra S15 realization**.
  2. **D YES/NO decision**, independently: attack
     `h - 2e - f <= 1/32` by a local/high-frequency or remote-perturbation
     counterfamily before attempting any proof.  Do not assume Q-SPEC while deciding D.
  3. Only if 1 and 2 survive: construct one exact admissible core with cone entry and
     formulate a Dini/branch-switching replacement for the unique off-axis maximizer
     hypothesis.
  4. Standing older lanes remain as in the archived twenty-ninth-session handoff:
     general head program parked/closed at audit level; numerical event-budget results
     diagnostic only; SEL-3/SEL-5/EB-1 Lean debts on hold; passive literature watch
     unchanged.
- **Do NOT assume / forbidden repeats:**
  - do not claim Q from local `U,S,H,L5U,L5S` data or from the favorable first relay
    term; the counterfamily preserves those data while reversing Q;
  - do not read `Q-UNIV KILLED` as `S15 existential route KILLED`;
  - do not formalize the trivial scalar statement "very negative Pi violates Q" and
    present it as a mechanization of the pressure no-go;
  - do not claim the remote-torus family is a blow-up construction; it is a local-time
    counterexample to a proposed boundary sign;
  - do not un-park BH/Γ, T-DIR/T-VAR/T-CONE/T-DET, HR-* or numerical routes without
    their recorded user-act/trigger rules;
  - no numerical sign observation may replace the exact pressure-kernel sign already
    proved in the Q decision record.

## Repository / verification state

- `main` at the start of the thirty-first session:
  `c69315e32eead48c1fd681bf86c8bab1af815e64` (merged PR #83).
- Current work branch: `research/astra-s15-q-decision`.
- Q-decision record first commit on that branch:
  `f72a13db8d59652b345d0b850d83f827ab4a3c5e`.
- PR #83 is merged.  Do not reopen it; the Q decision is a separate focused change.
- No Lean source is changed by the Q decision.  `FORMAL_SCOPE.md` is intentionally
  unchanged.
- Automatic/full hosted CI policy remains governed by `docs/LEAN_CI_OPERATIONS.md`;
  do not use hosted Actions as an interactive compiler.

## Project claim boundary

Ultimate target: an exact official Clay/Fefferman Navier–Stokes A/B/C/D statement.
Current physical specialization remains `R^3`, preferably `f=0`, axisymmetric with swirl,
breakdown side, governed by `SPEC.md`.

No current result proves Navier–Stokes blow-up or global regularity.  The newest theorem-level
research result is negative knowledge: a proposed **universal Q boundary sign is false** for
admissible initial data because nonlocal pressure can be altered independently of the fixed
local maximum jet.  This is a route-refinement/no-go result, not a Clay result.