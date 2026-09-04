# Astra S15 traveling-max invariant-cone candidate — 2026-09-05

**Status: CONDITIONAL THEOREM / RESEARCH PROPOSAL.**

This record is a user-commissioned one-shot attempt to turn Astra's open S15 template

\[
\mathcal A'(t)\ge c\,\mathcal A(t)^{1+\eta}
\]

into a concrete invariant-regime problem for the **actual unforced axisymmetric-with-swirl
3-D Navier–Stokes equations on `R^3`**.  It does **not** prove finite-time breakdown,
Clay C/D, or a new Navier–Stokes theorem.  The analytic invariant-region obligations below
are open.  The companion Lean file formalizes only the elementary real-algebra implications
of the proposed cone and deliberately does not encode the open PDE assertions.

This work is exploratory and does not edit any frozen research verdict, does not un-park the
BH/Γ-depletion lane, and does not replace the current general-class H-SEL/T-GRAM frontier.

---

## 0. Short B-audit: Shahmurov arXiv:2606.07869 does not currently kill the branch

The repository already performed the requested short adversarial audit in
`docs/gates/D3_TRIAGE_2606_07869_2026-09-02.md`.  The paper is still arXiv
`2606.07869v1` (5 Jun 2026) as of this record.  Its stated theorem is unconditional global
regularity for smooth finite-energy axisymmetric 3-D Navier–Stokes with arbitrary swirl, so
if correct it would indeed kill the ambient axisymmetric breakdown class.

The existing audit found independent load-bearing gaps:

- **G1a/G1b:** the strict-bridge/no-saturator variational argument differentiates along a
  spatial dilation that is not shown to preserve the solution-generated endpoint class or
  the exact zero-ledger constraint; the constrained stationarity step therefore does not
  justify the printed derivative identity;
- **G2:** several routing outputs/thresholds are not quantitatively defined, and no
  rank-plus-budget decrease is supplied that excludes infinitely many rank-constant
  routing/absorption steps;
- **G3:** partly repairable, but the zero-output membership criteria drift and the
  backward-ancestor seam retain undischarged obligations.

The adjudicated repository verdict remains **correctness NOT ESTABLISHED —
unverified-with-confirmed-load-bearing-gaps**, not a refereed refutation.  No CAP trigger
fires and the paper is consumed by no theorem in this repository.  Current arXiv entry:
`https://arxiv.org/abs/2606.07869`.

Accordingly this record proceeds to A, without assuming either the truth or falsity of the
Shahmurov theorem.

---

## 1. Exact axisymmetric variables

Use the repository's audited sign convention from `SPEC.md` and
`docs/equation_audit.md`:

\[
U:=u_1=\frac{u^\theta}{r},\qquad
S:=\partial_z\psi_1=-\frac{u^r}{r},\qquad
b:=(u^r,u^z),
\]

and

\[
L_5:=\partial_r^2+\frac3r\partial_r+\partial_z^2,
\qquad
D_t:=\partial_t+b\cdot\nabla_{r,z}.
\]

The audited `u_1` equation is

\[
\boxed{D_tU=2SU+\nu L_5U.}
\tag{1.1}
\]

A second exact identity follows directly from the audited radial momentum equation.  Since
`u^r=-rS`,

\[
D_tu^r=rS^2-rD_tS,
\qquad
\frac{(u^\theta)^2}{r}=rU^2,
\]

and

\[
(\Delta_0-r^{-2})(rS)=rL_5S.
\]

Substitution into the radial Navier–Stokes equation gives

\[
\boxed{D_tS=S^2-U^2+\frac{p_r}{r}+\nu L_5S.}
\tag{1.2}
\]

No model reduction has been used in (1.1)–(1.2).

---

## 2. Moving positive maximum of `U`

For the first theorem-shaped attempt, impose the following **extra open hypotheses** on an
actual smooth axisymmetric solution over an interval `I=[t0,t1)`:

1. `U(·,t)` has a positive global maximum
   \(A(t)=U(x_*(t),t)>0\), with \(x_*=(R,Z)\) and \(R(t)>0\);
2. the maximizer is unique and `C^1` in time;
3. the `(r,z)` Hessian
   \(H(t)=D^2_{r,z}U(x_*(t),t)\) is negative definite.

The off-axis condition is only a first-pass technical simplification.  A serious proof must
replace it by a signed-`r`/axis-compatible argument or by a Dini-derivative formulation of
the supremum.  Nothing here assumes that a future singular maximum stays off-axis.

At the maximizer, \(\nabla U=0\).  Therefore (1.1) gives the **exact** amplitude identity

\[
\boxed{A'=2S_*A+\nu(L_5U)_*.}
\tag{2.1}
\]

Because \(U_r=0\) at the off-axis maximum,
\(L_5U=U_{rr}+U_{zz}\le0\) there.

Define the dimensionless quantities

\[
q:=\frac{S_*}{A},
\qquad
d:=-\frac{\nu(L_5U)_*}{A^2}\ge0.
\tag{2.2}
\]

Then

\[
\boxed{A'=(2q-d)A^2.}
\tag{2.3}
\]

Thus a lower bound for `q` together with an upper bound for viscous curvature `d` is exactly
the S15 growth mechanism, with no exponent bookkeeping in the derivation.

---

## 3. Maximizer relay identity

Differentiate the stationarity condition
\(\nabla U(x_*(t),t)=0\).  Using (1.1) and
\(\nabla U(x_*)=0\) yields

\[
H(\dot x_*-b_*)+2A\nabla S_*+\nu\nabla L_5U_*=0.
\]

Write the maximizer velocity relative to the fluid as

\[
V_*:=\dot x_*-b_*.
\]

Since `H` is invertible under the nondegeneracy hypothesis,

\[
\boxed{
V_*=-H^{-1}\bigl(2A\nabla S_*+\nu\nabla L_5U_*\bigr).
}
\tag{3.1}
\]

This is the candidate **traveling-max relay** mechanism: the maximizer need not be a
material particle.

Introduce

\[
\Pi:=\frac{(p_r/r)_*}{A^2},
\qquad
e:=\frac{\nu(L_5S)_*}{A^2},
\qquad
m:=\frac{V_*\cdot\nabla S_*}{A^2}.
\tag{3.2}
\]

Equation (3.1) expands `m` as

\[
\boxed{
m=-\frac2A\nabla S_*^T H^{-1}\nabla S_*
   -\frac{\nu}{A^2}\nabla S_*^TH^{-1}\nabla L_5U_*.
}
\tag{3.3}
\]

Because `H<0`, its inverse is also negative definite, hence the first term in (3.3) is
nonnegative.  The second, viscous mixed term has no sign.  This precise split is important:
**the relay is not proved positive as a whole**.

Along the moving maximizer, (1.2), (2.3) and the definition of `m` give

\[
\boxed{
q'=A\,[\Pi-1-q^2+e+qd+m].
}
\tag{3.4}
\]

The local two-variable ODE skeleton `U'=2SU`, `S'=S^2-U^2` would instead force
`q'=-A(1+q^2)`; (3.4) identifies exactly which full-NS terms would have to defeat that
depletion.

---

## 4. Curvature-ratio identity and corrected commutator sign

Let

\[
K:=(L_5U)_*,\qquad d=-\nu K/A^2.
\]

For the operator/transport commutator use the convention

\[
[L_5,b\cdot\nabla]U
:=L_5(b\cdot\nabla U)-b\cdot\nabla(L_5U).
\tag{4.1}
\]

At the maximizer, the product rule

\[
L_5(SU)=S L_5U+U L_5S+2\nabla S\cdot\nabla U
\]

loses its cross term.  Differentiating `K=L_5U(x_*(t),t)` therefore gives

\[
K'=V_*\cdot\nabla L_5U_*
   -[L_5,b\cdot\nabla]U_*
   +2S_*K+2A(L_5S)_*+\nu(L_5^2U)_*.
\tag{4.2}
\]

Define

\[
f:=\frac{\nu^2(L_5^2U)_*}{A^3},
\qquad
h:=\frac{\nu}{A^3}
\left([L_5,b\cdot\nabla]U_*-V_*\cdot\nabla L_5U_*\right).
\tag{4.3}
\]

Combining (4.2) with (2.3) yields

\[
\boxed{
d'=A\,[2d^2-2qd-2e-f+h].
}
\tag{4.4}
\]

This is the sign-corrected form used below.  In particular, a previous informal rendering
with the opposite sign convention for the commutator remainder must not be reused.

---

## 5. Concrete invariant cone

Take

\[
\kappa=\frac14,
\qquad
\delta=\frac18,
\]

and consider

\[
\mathcal C=\{A>0,\ q\ge1/4,\ 0\le d\le1/8\}.
\tag{5.1}
\]

Inside this cone, (2.3) gives immediately

\[
\boxed{A'\ge\frac38 A^2.}
\tag{5.2}
\]

The two nontrivial first-crossing barriers are:

### Q-boundary (`q=1/4`)

From (3.4), inward pointing is guaranteed by

\[
\boxed{
\Pi+e+\frac14d+m\ge\frac{17}{16}.
}
\tag{Q}
\]

Indeed this is exactly `q' >= 0` at `q=1/4`.

### D-boundary (`d=1/8`)

From (4.4), with `q>=1/4`,

\[
2d^2-2qd\le-\frac1{32}
\qquad(d=1/8).
\]

Therefore the sufficient inward condition is

\[
\boxed{
h-2e-f\le\frac1{32}.
}
\tag{D}
\]

It implies `d' <= 0` at the upper boundary.  The lower boundary `d=0` does not require a
separate ODE barrier as long as `x_*` remains a smooth interior maximum: `L_5U_*<=0`
already gives `d>=0` kinematically.

Under the smooth-maximizer hypotheses, if `(Q)` and `(D)` hold whenever their respective
boundaries are reached, the elementary first-crossing argument makes `C` positively
invariant.

Then (5.2) gives

\[
\left(\frac1A\right)'=-\frac{A'}{A^2}\le-\frac38,
\]

so no smooth continuation preserving the regime can exist past

\[
\boxed{
t_0+\frac{8}{3A(t_0)}.
}
\tag{5.3}
\]

If the actual Navier–Stokes solution ceases to be smooth earlier, that is already the
breakdown outcome.  If it remained smooth through the time in (5.3), the finite smooth
quantity `A=max(u^theta/r)` would be forced to become infinite, a contradiction.

---

## 6. The actual open theorem — not the algebra

The new mathematical burden is now explicit.  A usable breakdown theorem would need one
admissible smooth divergence-free compactly supported/Schwartz datum for which the actual
Navier–Stokes trajectory supplies all of the following until the ODE obstruction fires:

1. **MAX:** a well-defined positive maximum branch, or a replacement Dini-envelope
   argument that survives branch switching and axis contact;
2. **CONE-ENTRY:** at some `t0`, `q>=1/4` and `d<=1/8`;
3. **Q-BARRIER:** the pressure + strain-diffusion + relay combination `(Q)` at every first
   contact with `q=1/4`;
4. **D-BARRIER:** the commutator/fourth-order-viscous combination `(D)` at every first
   contact with `d=1/8`;
5. **TAIL/AXIS:** the global maximum and all integrations/reconstructions remain compatible
   with the `R^3` axis regularity and decay class;
6. **ADMISSIBILITY:** the datum belongs to the exact Clay-admissible class and the argument
   concerns the original three-dimensional solution, not a finite-cylinder or reduced
   system.

The Q- and D-barriers are the decisive new PDE lemmas.  Energy, incompressibility and the
Γ maximum principle alone do not imply them.  In particular, the favorable first relay term
in (3.3) does **not** by itself close Q because pressure, viscous mixing and the second relay
term remain uncontrolled.

This is therefore a falsifiable Stage-9 object, not a claimed construction:

> **Traveling-Max Invariant-Cone Problem.**  Does there exist a Clay-admissible unforced
> axisymmetric datum whose actual smooth pre-breakdown Navier–Stokes trajectory enters
> `C` and satisfies `(Q)` and `(D)` at all first contacts?

A proof yields finite-time nonextendibility.  A theorem showing that either `(Q)` or `(D)`
necessarily fails before the cone can persist kills this S15 realization.

---

## 7. Relation to the parked `beta_v` middle limb

There is a structural adjacency, but no identification is claimed.  If a future solution
also has a circulation-saturated moving maximum with

\[
\Gamma_*=R(t)^2A(t)\asymp 1
\]

and independently has the two-sided rate

\[
A(t)\asymp(T-t)^{-1},
\]

then

\[
R(t)\asymp A(t)^{-1/2}\asymp(T-t)^{1/2},
\]

so the saturation-location exponent would be `beta_v=1/2`.  This is compatible with the
previous frozen-vocabulary witness `(gamma,alpha,beta_v)=(3/5,9/20,1/2)` because
`9/20 < 1/2 < 3/5`.

Neither premise follows from (5.2): the differential lower bound alone does not prove the
two-sided rate, and the moving maximum need not be the Γ-saturation point.  Consequently
this paragraph is only a bridge hypothesis for future work and does not un-park or modify
any frozen `beta_v` verdict.

---

## 8. Lean scope

`Formal/R3TravelingMaxInvariantCone.lean` proves only three real-algebra facts used above:

- `q>=1/4`, `d<=1/8` implies `2q-d>=3/8`, hence the growth coefficient bound after
  multiplication by `A^2>=0`;
- `(Q)` implies the normalized `q` boundary vector field is inward;
- `(D)` together with `q>=1/4` implies the normalized `d` boundary vector field is inward.

It does not formalize (1.1)–(4.4), existence of the moving maximizer, pressure recovery,
axisymmetry, or any invariant-region theorem for Navier–Stokes.  Those are exactly the open
analytic obligations above.  `Formal/R3TravelingMaxInvariantConeAudit.lean` prints the
axiom dependencies of the three algebraic theorems without modifying the repository-wide
`AxiomAudit.lean`.
