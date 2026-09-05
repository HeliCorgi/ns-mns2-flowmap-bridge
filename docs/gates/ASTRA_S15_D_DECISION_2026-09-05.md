# Astra S15 D-barrier YES/NO decision — 2026-09-05

**Status: NO-GO / DECISION THEOREM.**

**Verdict: `NO (UNIVERSAL-D FALSE)`.**

This record attacks the D-boundary condition introduced in
`docs/gates/ASTRA_S15_TRAVELING_MAX_2026-09-05.md` for the actual unforced,
axisymmetric-with-swirl Navier–Stokes system on `R^3`.

The result is deliberately narrower than a refutation of every possible existential Astra S15
construction.  It kills the **universal structural reading** of D: the upper-curvature boundary
cannot be made invariant from the lower moving-maximum jet alone.  A specially selected datum
could still satisfy D along its own trajectory, but any such theorem must use additional dynamical
structure that constrains the fourth-order swirl jet.

No Navier–Stokes blow-up, global regularity theorem, or Clay alternative is proved.

---

## 0. Exact YES/NO question

Use the variables and exact moving-max identities already audited in the previous record:

\[
U=\frac{u^\theta}{r},\qquad
S=-\frac{u^r}{r},\qquad
A=U(x_*),\qquad
q=\frac{S_*}{A},
\]

\[
d=-\frac{\nu(L_5U)_*}{A^2},\qquad
L_5=\partial_r^2+\frac3r\partial_r+\partial_z^2.
\]

At a smooth unique nondegenerate off-axis positive maximum `x_*`, the exact curvature-ratio
identity is

\[
 d'=A\,[2d^2-2qd-2e-f_4+h],
\tag{0.1}
\]

where, to avoid confusing the previous record's symbol `f` with physical forcing, this note writes

\[
 e:=\frac{\nu(L_5S)_*}{A^2},\qquad
 f_4:=\frac{\nu^2(L_5^2U)_*}{A^3},
\tag{0.2}
\]

\[
 h:=\frac{\nu}{A^3}
 \left([L_5,b\cdot\nabla]U_*-V_*\cdot\nabla L_5U_*\right),
\tag{0.3}
\]

and

\[
V_*=-H^{-1}(2A\nabla S_*+\nu\nabla L_5U_*),\qquad H=D^2U(x_*).
\tag{0.4}
\]

The previous symbol `f` equals `f_4` in this note.  The physical Navier–Stokes force remains
identically zero.

At the corner

\[
q=\frac14,\qquad d=\frac18,
\]

(0.1) becomes exactly

\[
\boxed{
 d'=A\left[-\frac1{32}+h-2e-f_4\right].
}
\tag{0.5}
\]

Thus inward pointing at this corner is equivalent to

\[
\boxed{h-2e-f_4\le\frac1{32}.}
\tag{D}
\]

The decision question is:

> **(D-UNIV)** For every real, smooth, compactly supported, divergence-free,
> axisymmetric-with-swirl datum whose actual local Navier–Stokes solution has at `t=0`
> a unique positive nondegenerate off-axis maximum of `U` satisfying
> `q=1/4` and `d=1/8`, must `(D)` hold there?

### Decision

\[
\boxed{\textbf{NO}.}
\]

The counterfamily fixes every local quantity entering `A,q,d,e,h` and changes only the fourth-order
quantity `f_4`.  The D left-hand side can then be sent to `+infinity`, and for large parameter the
actual local Navier–Stokes solution has `d'(0)>0` at the proposed upper cone boundary.

---

## 1. A compactly supported admissible core exists

Fix `nu>0`, an off-axis point

\[
x_0=(r_0,z_0),\qquad r_0>0,
\]

and an amplitude `A>0`.  Put

\[
\kappa:=\frac{A^2}{16\nu}.
\tag{1.1}
\]

Choose a nonnegative smooth cutoff `chi_0` supported in a sufficiently small ball around `x_0`,
with `chi_0=1` on a smaller ball and with support disjoint from the axis.  On that smaller ball set

\[
 U_0(r,z)=A-\frac\kappa2\big((r-r_0)^2+(z-z_0)^2\big).
\tag{1.2}
\]

After multiplying by `chi_0` and choosing the support small enough, one obtains a smooth compactly
supported scalar `U_0` whose unique positive global maximum is `A` at `x_0`, with negative-definite
Hessian there.  At `x_0`,

\[
\nabla U_0=0,\qquad (L_5U_0)_*=-2\kappa,
\]

so

\[
 d=-\frac{\nu(L_5U_0)_*}{A^2}
   =\frac{2\nu\kappa}{A^2}=\frac18.
\tag{1.3}
\]

Independently choose a smooth compactly supported stream-function scalar `psi_1` supported away
from the axis and satisfying, near `x_0`,

\[
 \psi_1(r,z)=\frac A4(z-z_0).
\tag{1.4}
\]

The standard reconstruction

\[
 u^r=-r\partial_z\psi_1,\qquad
 u^z=2\psi_1+r\partial_r\psi_1
\tag{1.5}
\]

is smooth, compactly supported, axisymmetric and divergence-free.  Near `x_0`,

\[
 S=\partial_z\psi_1=\frac A4,
\]

hence

\[
q=\frac14,\qquad \nabla S_*=0,\qquad (L_5S)_*=0,
\tag{1.6}
\]

so in particular `e=0` at the target point.

Finally set

\[
 u^\theta=rU_0.
\tag{1.7}
\]

Because all supports are a positive distance from the axis, (1.5) and (1.7) define a
`C_c^infty(R^3)` real axisymmetric divergence-free velocity with swirl.  Standard local strong
well-posedness therefore supplies the corresponding actual unforced Navier–Stokes solution for a
positive time.  Only its derivative at `t=0` is used below.

---

## 2. Quartic jet perturbation

Choose another nonnegative cutoff `chi`, supported in the same off-axis coordinate neighborhood,
with `chi=1` near `x_0`.  For `M>=0`, define

\[
 \Phi_M(r,z):=-M(r-r_0)^4\chi(r,z),
\qquad
 U_M:=U_0+\Phi_M.
\tag{2.1}
\]

This is a smooth compactly supported pure-swirl perturbation.  Since `Phi_M<=0` and
`Phi_M(x_0)=0`, the unique positive global maximum `A` remains at `x_0` for every `M`; the
negative-definite Hessian is unchanged.

Because `chi=1` near `x_0`, the complete jet through order three vanishes:

\[
 \partial^\alpha\Phi_M(x_0)=0
 \qquad (|\alpha|\le3).
\tag{2.2}
\]

In particular,

\[
 (L_5\Phi_M)_*=0,
 \qquad
 \nabla(L_5\Phi_M)_*=0.
\tag{2.3}
\]

Hence `A`, `H`, `q`, `d`, `e`, `nabla S`, and the maximizer velocity `V_*` are all independent of
`M` at `t=0`.

The fourth radial derivative is not zero.  Directly,

\[
 \partial_r^4\Phi_M(x_0)=-24M.
\tag{2.4}
\]

For the particular quartic monomial, the lower-order coefficient `3/r` in `L_5` contributes
nothing to `L_5^2` at the center beyond terms whose relevant jets vanish.  Explicitly,

\[
 L_5((r-r_0)^4)
 =12(r-r_0)^2+\frac{12(r-r_0)^3}{r},
\]

and therefore

\[
\boxed{(L_5^2\Phi_M)_*=-24M.}
\tag{2.5}
\]

Consequently

\[
\boxed{
 f_{4,M}=f_{4,0}-\frac{24\nu^2}{A^3}M.
}
\tag{2.6}
\]

---

## 3. Why `h` is unchanged

The only possible hidden issue is the commutator in `h`.  Write

\[
L_5=\partial_r^2+\partial_z^2+c(r)\partial_r,
\qquad c(r)=\frac3r,
\]

and `b=(b^r,b^z)`.  A direct expansion gives

\[
[L_5,b\cdot\nabla]U
=(\Delta b+c\partial_rb)\cdot\nabla U
+2\sum_{i\in\{r,z\}}(\partial_i b)\cdot\partial_i\nabla U
-b^r c'(r)\,\partial_rU.
\tag{3.1}
\]

At a critical point `nabla U=0`, this reduces to a quantity depending only on `b`, its first
derivatives, and the Hessian of `U`:

\[
\boxed{
[L_5,b\cdot\nabla]U_*
=2\sum_{i\in\{r,z\}}(\partial_i b)_*\cdot(\partial_i\nabla U)_*.
}
\tag{3.2}
\]

The quartic perturbation has zero two-jet, so the commutator value is unchanged.  By (2.3),
`nabla L_5U_*` is also unchanged, and therefore (0.4) gives the same `V_*`.  Thus

\[
\boxed{h_M=h_0.}
\tag{3.3}
\]

Since the meridional field was not changed, `e_M=e_0` as well.

---

## 4. D is violated arbitrarily strongly

Combining (2.6) and (3.3),

\[
 h_M-2e_M-f_{4,M}
 =h_0-2e_0-f_{4,0}
  +\frac{24\nu^2}{A^3}M.
\tag{4.1}
\]

Hence

\[
\boxed{
 h_M-2e_M-f_{4,M}\longrightarrow+\infty
 \quad\text{as }M\to\infty.
}
\tag{4.2}
\]

For sufficiently large `M`, condition `(D)` fails.  Because this counterfamily sits at the exact
corner `q=1/4`, `d=1/8`, equation (0.5) then gives

\[
\boxed{d'_M(0)>0.}
\tag{4.3}
\]

Thus the proposed upper curvature boundary is genuinely outward-pointing for the actual local
Navier–Stokes solution, not merely a failure of a convenient sufficient estimate.

This proves

\[
\boxed{\text{D-UNIV = NO / KILLED.}}
\]

---

## 5. Scope ruling

### Killed

1. The class-wide assertion that `(D)` follows from smoothness, axisymmetry, incompressibility,
   compact support, and the moving positive maximum geometry.
2. Any proof of D that only controls the zero-through-third local jet of `U` at the maximizer.
3. Any claim that the curvature ratio `d` has an automatic upper barrier at `1/8` merely because
   the point is a nondegenerate maximum.
4. The idea that the two-variable `(q,d)` cone has universal inward boundary signs.  Q-UNIV was
   already killed by nonlocal pressure; D-UNIV is now killed independently by a local fourth-jet
   perturbation.

### Not killed

1. The exact identity `A'=(2q-d)A^2`.
2. The elementary conditional implication
   `Q + D + cone entry => A' >= (3/8)A^2` while the smooth maximum branch and barriers persist.
3. A **datum-specific D-SPEC** statement imposing additional dynamical structure that controls
   `L_5^2U` (and therefore the fourth jet) along one selected trajectory.
4. A combined Q-SPEC/D-SPEC existential construction with genuinely global/dynamical coherence.
5. The broader Astra S15 idea using a different functional or a different invariant region.

However, after independent counterfamilies kill both universal boundary mechanisms of the present
`(q,d)` cone, this particular S15 realization should be **PARKED by default**.  Reopening it requires
a new theorem-shaped hypothesis that simultaneously explains why the remote pressure-poisoning
family from the Q decision and the quartic fourth-jet family here are excluded, and why that
hypothesis is propagated by the actual Navier–Stokes flow.  Merely adding another local jet variable
without a closure mechanism is not a sufficient reason to reopen the lane.

---

## 6. Lean / verification boundary

No Lean source is changed by this decision.  The existing Lean file
`Formal/R3TravelingMaxInvariantCone.lean` remains a correct formalization only of the elementary
conditional real-algebra implications.  It does not assert Q or D analytically.

There is little value in adding a theorem saying that subtracting an arbitrarily negative scalar
`f_4` violates D; the load-bearing content is the analytic realization of that scalar freedom by the
smooth quartic pure-swirl perturbation (2.1).  This record therefore leaves `FORMAL_SCOPE.md`
unchanged.

The repository claim boundary remains unchanged: no Clay A/B/C/D statement is established.
