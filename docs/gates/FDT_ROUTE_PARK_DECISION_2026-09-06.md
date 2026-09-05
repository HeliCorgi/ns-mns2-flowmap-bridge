# FDT regularity-route park decision — 2026-09-06

**Status: STRATEGIC PARK.  PARENT FDT-INJ REMAINS OPEN.**

**Primary ruling:**

- `FDT-DEF-BUDGET` is **not proved false** on Clay-admissible `R^3` data;
- however, as a reduction from already-controlled quantities it has failed the independence test;
- therefore the current frequency/dissipation material-shell route is **PARKED** pending a genuinely new deformation theorem from outside the present chain.

This record follows:

1. `FREQUENCY_DISSIPATION_TRANSFER_DECISION_2026-09-05.md`;
2. `FDT_LH_DECISION_2026-09-05.md`;
3. `FDT_LH_DYN_AFFINE_DECISION_2026-09-06.md`;
4. `FDT_MAT_STRUCT_DECISION_2026-09-06.md`.

No global regularity theorem, blow-up theorem, or Clay alternative is proved.

---

## 0. Why a separate park decision is needed

The material-frequency structural gate left one apparent escape hatch:

> prove an independently finite/subcritical deformation budget for the low-frequency flow, strong
> enough to compare material shells with fixed Eulerian dyadic shells, but strictly weaker than the
> known continuation walls.

Call this proposed gate `FDT-DEF-BUDGET`.

The present record asks a portfolio question rather than pretending to settle an open PDE theorem:

> Is `FDT-DEF-BUDGET` now a genuinely narrower lemma supported by the preceding reductions, or has
> the route simply moved the original regularity difficulty into the deformation gradient?

The answer is the latter.

---

## 1. Exact quantity that must be controlled

For the low field

\[
 v_j=u_{\le j-2}
\]

let `X_j(t,s,x)` be its flow and define the deformation matrix

\[
 F_j(t,s,x):=D_xX_j(t,s,x).
\]

Material and Eulerian frequency covectors are related by `F_j^{-T}`.  Therefore any two-sided shell
comparison requires control of the singular values of `F_j`.  A convenient distortion functional is

\[
 \boxed{
 K_j(t,s):=
 \sup_x \max\{\|F_j(t,s,x)\|,\|F_j(t,s,x)^{-1}\|\}.
 }
\tag{1.1}
\]

Equivalently one may use the condition number or the eigenvalues of the Cauchy--Green tensor
`F_j^T F_j`.  Up to harmless powers, these are the same shell-comparison datum.

The flow equation gives

\[
 \partial_tF_j=(\nabla v_j)(t,X_j)F_j.
\tag{1.2}
\]

Hence the standard deterministic control is

\[
 \boxed{
 K_j(t,s)
 \le
 \exp\!\left(
   \int_s^t\|\nabla v_j(\tau)\|_\infty\,d\tau
 \right).
 }
\tag{1.3}
\]

One may sharpen `||grad v_j||` to suitable extremal eigenvalues of the symmetric strain, but the
basic fact does not change: **the material/Eulerian bridge is a deformation-gradient problem.**

---

## 2. The required budget is scale-critical

Use the unforced `R^3` Navier--Stokes scaling at fixed viscosity,

\[
 u^{(\lambda)}(x,t)=\lambda u(\lambda x,\lambda^2t).
\tag{2.1}
\]

If a dyadic index is shifted so that the physical scale follows the scaling, then the one-viscous-
window strain quantity

\[
 \mathcal D_j(t)
 :=
 \int_{t-\tau_j}^{t}
 \|\nabla u_{\le j-2}(s)\|_\infty\,ds,
 \qquad
 \tau_j\asymp(\nu\lambda_j^2)^{-1},
\tag{2.2}
\]

is invariant under (2.1), up to the fixed LP indexing convention.

By contrast,

\[
 \|u^{(\lambda)}(0)\|_2^2=\lambda^{-1}\|u(0)\|_2^2,
\tag{2.3}
\]

and the total energy-dissipation budget has the same supercritical scaling.

Consequently the missing deformation control cannot be obtained as a small consequence of energy
or total enstrophy/dissipation at high frequency.  In particular, any proposed estimate whose right
side tends to zero solely because the energy/dissipation budget tends to zero is incompatible with
scaling whenever the base trajectory has nonzero scale-local strain.

This is the same structural message already seen constructively in the session-34 packet family:
ordinary energy and one-window `L^2` enstrophy do not make the low strain coefficient perturbative.

---

## 3. Why mere finiteness is not an independent reduction

For every compact interval strictly inside a smooth lifespan, `K_j(t,s)` is of course finite.  That
observation is useless for continuation.

To make the material-frequency route load-bearing one needs a bound that stays uniform as the
potential first singular time `T_*` is approached, uniformly over the relevant high dyadic indices:

\[
 \boxed{
 \sup_{j\ge J}
 \sup_{0<t<T_*}
 K_j(t,\max\{0,t-\tau_j\})<\infty.
 }
\tag{3.1}
\]

or a quantitatively equivalent shell-comparison statement.

But (3.1) is itself a new **critical deformation regularity statement**.  The preceding FDT work has
not reduced it to energy, dissipation, pressure cancellation, or another independently finite
quantity.  The only direct deterministic route is again a strain integral such as (1.3).

Therefore replacing the original FDT injection problem by (3.1) does not currently shorten the
proof chain.  It relocates the open regularity wall from fixed Eulerian frequency injection to
low-flow deformation.

This is the binding reason for parking.

---

## 4. Accumulated no-go evidence

The decision uses the entire chain, not the deformation issue in isolation.

### 4.1 Static/energy shortcut

A pointwise energy-only route to the Cheskidov--Shvydkoy coefficient was killed by critical packet
scaling in the parent FDT record.

### 4.2 Separate low--high operator closure

`FDT-LH-OP = NO`: a real divergence-free Schwartz packet family has a subcritical target block and
arbitrarily small ordinary energy / one-window enstrophy, but an arbitrarily large normalized frozen
LH commutator window.

### 4.3 Signed low-flow conjugation

`FDT-LH-DYN-AFF = NO`: in the exact affine-strain NS model, signed dynamic LH does not cancel.  It
is exactly an order-one LP multiplier boundary displacement caused by benign shell transport.

### 4.4 Material shells

`FDT-MAT-COMM = YES`, but `FDT-MAT-BRIDGE-UNIF = NO`: exact transport commutation deforms annuli
into material ellipsoids.  Affine strain gives arbitrarily large Eulerian/material shell distortion
inside one viscous window.

Thus every attempt to avoid paying low deformation has failed for a different structural reason.
The remaining proposal is precisely to control that deformation itself.

---

## 5. Exact decision

The mathematical status and the project status must be separated.

### Mathematical status

\[
 \boxed{\texttt{FDT-DEF-BUDGET on admissible R3 data: OPEN}.}
\]

No counterexample satisfying the parent fixed-Schwartz-datum quantifiers has been produced.  In
particular, the affine exact model is not finite energy.

### Reduction status

\[
 \boxed{\texttt{FDT-DEF-BUDGET-AS-INDEPENDENT-REDUCTION: FAIL}.}
\]

Reason: the required object is the critical low-flow deformation itself, and no independently finite
budget has survived or been derived from the present chain.  Assuming it by way of `int F`,
`int ||grad u||_infinity`, a Serrin norm, bounded `H^3`, or an equivalent strain criterion is
circular for the purpose of this route.

### Strategic status

\[
 \boxed{\texttt{FDT REGULARITY CROSS-TRACK: PARKED}.}
\]

This is not a theorem saying the frequency route is impossible.  It is a decision that further
LP/Bony/material-shell work has lower information value than returning to a different frontier
unless a genuinely new deformation theorem arrives independently.

---

## 6. Reopen conditions

The FDT route should be reopened only if at least one of the following appears:

1. **new deformation theorem:** a bound for `K_j` or Cauchy--Green distortion from an independently
   controlled NS quantity, demonstrably weaker than existing continuation criteria;
2. **new material continuation theorem:** a proof that regularity follows directly from a
   deformation-aware material metric without first comparing back to fixed Eulerian shells and
   without hiding strain control in the metric definition;
3. **admissible cancellation mechanism:** an actual fixed-Schwartz-datum identity coupling LH/HL/HH,
   pressure/Leray, and diffusion so that deformation need not be bounded separately;
4. **new external result:** literature or formal work materially changes the deformation frontier.

Absent one of these, do not add LP/Bony/Piola/paracomposition Lean plumbing.

---

## 7. Portfolio routing after park

The repository's declared main objective remains the breakdown-side Clay C/D program in `SPEC.md`.
The FDT work was explicitly a regularity-side cross-track experiment and never replaced that main
priority.

Therefore the next research session should return to the frozen breakdown-side frontier rather than
inventing another FDT observable.  Re-read, in order:

1. `SPEC.md`;
2. `docs/gates/STAGE9_DECISION_SELECTION_2026-08-23.md`;
3. `docs/gates/BH_BETAV_ENDPOINT_PINNING_2026-08-23.md`;
4. the latest breakdown-side kill table / readiness audit referenced there.

Then select one **actual-NS dynamical** decision beyond the already-settled scope-free exponent
arithmetic.  Do not reopen the parked Astra `(q,d)` cone unless a propagated structure excludes both
its pressure and fourth-jet counterfamilies.

---

## 8. Formalization ruling

No Lean source is added.

The formal frontier did not move.  Formalizing deformation-flow or material LP plumbing now would
encode an analytic route that has just been parked.  Existing Lean local NS infrastructure remains
useful for any future surviving theorem, but no new FDT-specific formal layer is commissioned.

`FORMAL_SCOPE.md` and `STATUS.md` remain unchanged.
