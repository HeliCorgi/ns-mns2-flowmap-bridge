# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: 2026-09-05 JST (thirty-second session).

> **Historical archive.**  The full session-by-session handoff through the
> twenty-ninth session is preserved verbatim at main commit
> `c69315e32eead48c1fd681bf86c8bab1af815e64` (the PR #83 merge).  This live file
> is intentionally the short-form continuation point; old research rulings are not
> rescinded by compaction.  Current source/theorem statements and dated gate records
> remain authoritative.
>
> **2026-09-05 (thirtieth session): ASTRA S15 TRAVELING-MAX ATTEMPT EXECUTED.**
> Record: `docs/gates/ASTRA_S15_TRAVELING_MAX_2026-09-05.md`.  For the actual
> unforced axisymmetric-with-swirl NS system, under an explicit smooth unique
> nondegenerate off-axis positive maximizer branch, the record derives
> `U = u^theta/r`, `S = psi1_z = -u^r/r`, `A = U(x_*)`,
> `q = S_*/A`, `d = -nu(L5 U)_*/A^2`, and
> **`A' = (2q-d)A^2`**.  The proposed cone is
> `q >= 1/4`, `0 <= d <= 1/8`; inside it
> **`A' >= (3/8)A^2`**.  The two analytic boundary obligations are
> **Q**: `Pi + e + d/4 + m >= 17/16` at `q=1/4`, and
> **D**: `h - 2e - f <= 1/32` at `d=1/8` (here `f` is the normalized
> fourth-order viscous term, not physical forcing).  PR #83 added the research
> record and only three real-algebra Lean consequences; no PDE barrier was encoded.
> PR #83 merged as `c69315e32eead48c1fd681bf86c8bab1af815e64`.
>
> **2026-09-05 (thirty-first session): Q DECISION EXECUTED —
> `NO (UNIVERSAL-Q FALSE)`.**
> Record: `docs/gates/ASTRA_S15_Q_DECISION_2026-09-05.md`, merged by PR #84 as
> `0fa9cadf998fcb5935812cfb56b4a86ea49c81cd`.  Q-UNIV asks whether all admissible
> compactly supported axisymmetric data at a moving positive maximum with
> `q=1/4`, `0<=d<1/8` must satisfy Q.  **No.**  A disjoint smooth negative
> pure-swirl torus preserves the complete local maximum jet but changes nonlocal
> pressure.  The exact Newtonian ring expansion gives a strictly negative radial
> pressure derivative for an exterior tangential ring; scaling the torus amplitude
> sends `Pi -> -infinity` while the local Q data stay fixed.  Thus Q can point
> outward for the actual local NS solution.  Q-UNIV is KILLED.  Q-SPEC, a
> datum-specific global pressure/relay coherence statement, remained logically open.
>
> **2026-09-05 (thirty-second session): D DECISION EXECUTED —
> `NO (UNIVERSAL-D FALSE)`.**
> Record: `docs/gates/ASTRA_S15_D_DECISION_2026-09-05.md` on branch
> `research/astra-s15-d-decision`.  The exact decision object **D-UNIV** asks whether
> every admissible smooth compactly supported axisymmetric-with-swirl datum whose
> actual local NS solution has at `t=0` a unique positive nondegenerate off-axis
> `U=u^theta/r` maximum with `q=1/4` and `d=1/8` must satisfy
> `h - 2e - f4 <= 1/32`, where
> `f4 = nu^2 (L5^2 U)_*/A^3` is the previous record's symbol `f`.
> **Answer: NO.**
>
> Fix a compactly supported off-axis core with the exact corner jet.  Independently
> of the meridional field, add the pure-swirl perturbation
> **`Phi_M = -M (r-r0)^4 chi`**, where `chi=1` near the positive maximum and is
> nonnegative and compactly supported away from the axis.  `Phi_M <= 0`, so the
> unique positive global maximum remains fixed.  Its complete jet through order
> three vanishes at the maximum, hence `A,H,q,d,e,nabla S,nabla L5 U,V_*` and `h`
> are unchanged.  The commutator identity at a critical point is
> `[L5,b·nabla]U_* = 2 sum_i (partial_i b)_* · (partial_i nabla U)_*`, so it uses
> only the Hessian of `U`.  But
> **`(L5^2 Phi_M)_* = -24 M`**, hence
> **`f4_M = f4_0 - 24 nu^2 M/A^3`** and
> `h_M - 2e_M - f4_M -> +infinity`.  For large `M`, D fails.  At the exact corner
> `q=1/4,d=1/8`, the exact identity
> **`d' = A[-1/32 + h - 2e - f4]`** then gives **`d'(0)>0` for the actual local
> Navier–Stokes solution**.  This is an analytic local fourth-jet counterfamily, not
> a numerical observation.
>
> **Ruling after sessions 31–32:** both universal boundary mechanisms of the present
> two-variable `(q,d)` cone are independently KILLED: Q-UNIV by nonlocal pressure
> freedom and D-UNIV by local fourth-jet freedom.  The exact moving-max identities
> and conditional scalar algebra remain correct, but this particular universal-cone
> realization of Astra S15 is now **PARKED BY DEFAULT**.  A future reopening must
> present genuinely new propagated structure that excludes *both* counterfamilies;
> simply adding more local jet variables or restating Q-SPEC/D-SPEC is not enough.
> No Lean source changed in sessions 31–32, so `FORMAL_SCOPE.md` and `STATUS.md`
> intentionally do not move.

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
9. `docs/gates/ASTRA_S15_D_DECISION_2026-09-05.md`;
10. current GitHub `main`, relevant `Formal/` files, open PRs, and latest Lean
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

### Next work (written 2026-09-05, thirty-second session)

Read first: the session-30/31/32 blocks above;
`docs/gates/ASTRA_S15_TRAVELING_MAX_2026-09-05.md` §§2–6;
`docs/gates/ASTRA_S15_Q_DECISION_2026-09-05.md` §§0,2–7;
`docs/gates/ASTRA_S15_D_DECISION_2026-09-05.md` §§0–5; `SPEC.md` §§2–6.

- **Current target/state:** the current `(q,d)` traveling-max S15 cone is **PARKED BY
  DEFAULT**.  Q-UNIV = NO/KILLED and D-UNIV = NO/KILLED by independent exact
  counterfamilies.  The conditional algebra `Q + D + cone entry => A' >= (3/8)A^2`
  remains true but has no universal PDE barrier behind it.  Q-SPEC and a possible
  D-SPEC are logical existential residues only; neither is an active theorem.  There
  is no Clay claim.
- **Latest meaningful Lean verification:** no Lean source changed in the Q or D
  decisions.  The latest hosted verification of the unchanged formal tree is GitHub
  Actions workflow `Lean 4 formalization`, run **#260** (`33932277589`), job
  `101213161122`, head `132b4e22ddc4b22eb640b49cf6c527d225c67fd7`, runner
  GitHub-hosted Ubuntu 24.04, Lean **4.32.1**; proof-hole/local-axiom/opaque scan PASS;
  full `lake build` **8777 jobs PASS**; the three traveling-max algebra theorem axiom
  prints remain `[propext, Classical.choice, Quot.sound]`.  D-decision work is docs-only
  and does not change this formal verification boundary.
- **Completed decision infrastructure:**
  `ASTRA_S15_TRAVELING_MAX_2026-09-05.md` (exact moving-max equations + conditional
  cone); `R3TravelingMaxInvariantCone.lean` and audit (three scalar algebra facts);
  `ASTRA_S15_Q_DECISION_2026-09-05.md` (remote-pressure Q no-go);
  `ASTRA_S15_D_DECISION_2026-09-05.md` (quartic fourth-jet D no-go).
- **Next analytic gate, recommended order (each is a new user act):**
  1. **Leave this S15 cone parked and return to a different theorem-shaped route.**
     Preferred fresh route: a frequency/dissipation-scale transfer decision on the
     existing `R^3` formal/analytic stack.  Start by defining one exact candidate
     estimate that would imply a known continuation criterion; then attack that estimate
     counterexample-first so that a disguised regularity assumption is not smuggled in.
  2. Alternative fresh route: ancient-solution inheritance + Liouville rigidity.  State
     the exact property claimed to survive blow-up rescaling before searching for a
     Liouville theorem; do not assume original finite energy survives the rescaling.
  3. Reopen traveling-max S15 only if a new hypothesis is supplied that is demonstrably
     violated by both the remote negative-swirl pressure torus and the local quartic
     fourth-jet perturbation, is propagated by actual NS evolution, and is weaker than a
     known regularity criterion.  Such a reopening should be a new gate, not a silent
     Q-SPEC/D-SPEC retry.
  4. Standing older lanes remain as in the archived twenty-ninth-session handoff:
     general head program parked/closed at audit level; numerical event-budget results
     diagnostic only; SEL-3/SEL-5/EB-1 Lean debts on hold; passive literature watch
     unchanged.
- **Do NOT assume / forbidden repeats:**
  - do not claim Q from local maximum jets; remote pressure changes Q while preserving
    them;
  - do not claim D from zero-through-third jets or maximum geometry; the quartic
    perturbation preserves them while sending the D left-hand side to `+infinity`;
  - do not convert the quartic family into a blow-up claim: it proves an outward
    derivative at one local-time cone boundary only;
  - do not formalize trivial scalar inequalities and present them as mechanization of
    either analytic no-go;
  - do not reopen this `(q,d)` cone by simply adding `L5^2 U` as another state variable
    unless a finite closure/invariance mechanism for the resulting derivative hierarchy
    is proved;
  - do not un-park BH/Γ, T-DIR/T-VAR/T-CONE/T-DET, HR-* or numerical routes without
    their recorded user-act/trigger rules.

## Repository / verification state

- `main` at the start of the thirty-second session:
  `0fa9cadf998fcb5935812cfb56b4a86ea49c81cd` (merged PR #84).
- Current work branch: `research/astra-s15-d-decision`.
- D-decision record first commit on that branch:
  `a7a4948a1c5a6cd26b4bc43bf6ae353c7f0d7c6a`.
- PR #83 and PR #84 are merged.  Do not reopen them; the D decision is a separate
  focused change.
- No Lean source is changed by the D decision.  `FORMAL_SCOPE.md` and `STATUS.md` are
  intentionally unchanged.
- Automatic/full hosted CI policy remains governed by `docs/LEAN_CI_OPERATIONS.md`;
  do not use hosted Actions as an interactive compiler.

## Project claim boundary

Ultimate target: an exact official Clay/Fefferman Navier–Stokes A/B/C/D statement.
Current physical specialization remains `R^3`, preferably `f=0`, axisymmetric with swirl,
breakdown side, governed by `SPEC.md`.

No current result proves Navier–Stokes blow-up or global regularity.  The newest theorem-level
research results are negative knowledge: the present traveling-max two-variable cone has no
universal Q barrier because nonlocal pressure can be changed independently of the local maximum
jet, and no universal D barrier because the fourth swirl jet can be changed independently of the
zero-through-third local jet.  These are route-refinement/no-go results, not Clay results.
