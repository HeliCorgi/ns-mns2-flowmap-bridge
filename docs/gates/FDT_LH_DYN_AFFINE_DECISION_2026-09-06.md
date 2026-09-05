# FDT-LH-DYN affine-strain decision — 2026-09-06

**Status: EXACT MODEL NO-GO / ADMISSIBLE R3 QUESTION REMAINS OPEN.**

**Primary verdict:** `FDT-LH-DYN-AFF = NO`.

This record continues `docs/gates/FDT_LH_DECISION_2026-09-05.md` and attacks the surviving
low-high dynamic question by the exact trace-free affine-strain model requested in the previous
handoff.

The result is deliberately scoped.  It proves that **low-flow conjugation plus signed time
integration does not, by itself, create a fixed small low-high commutator margin**.  The countermodel
is an exact smooth solution of the full incompressible Navier–Stokes equations, but its affine
background has infinite energy and is not Schwartz.  Therefore this record does **not** refute the
parent `FDT-INJ` statement for Clay-admissible data and does not prove either global regularity or
blow-up.

What it does kill is the proposed mechanism “conjugate by the low flow and the signed LH term will
cancel automatically.”  In the affine model the signed commutator can be integrated exactly and is
an order-one **boundary displacement of the LP multiplier**.

---

## 0. Setup

Fix viscosity `nu>0`.  Let

\[
 S_\gamma:=\begin{pmatrix}-\gamma&0&0\\0&\gamma&0\\0&0&0\end{pmatrix},
 \qquad \gamma>0,
\]

so `tr S_gamma=0`, and define the steady affine strain

\[
 a(x)=S_\gamma x=(-\gamma x_1,\gamma x_2,0).
 \tag{0.1}
\]

Let the high field be a transverse shear

\[
 w(t,x)=e_3 f(t,x_1).
 \tag{0.2}
\]

Then

\[
 \nabla\!\cdot a=\nabla\!\cdot w=0,
 \qquad
 (w\cdot\nabla)a=0,
 \qquad
 (w\cdot\nabla)w=0.
 \tag{0.3}
\]

Also

\[
 (a\cdot\nabla)a=S_\gamma^2x=(\gamma^2x_1,\gamma^2x_2,0),
\]

which is cancelled by

\[
 p(x)=-\frac{\gamma^2}{2}(x_1^2+x_2^2).
 \tag{0.4}
\]

Since `Delta a=0`, the full velocity

\[
 \boxed{u=a+w}
 \tag{0.5}
\]

solves the exact unforced incompressible Navier–Stokes equation provided `f` solves the scalar
strain-diffusion equation

\[
 \partial_t f-\gamma x_1\partial_{x_1}f=\nu\partial_{x_1}^2f.
 \tag{0.6}
\]

There is no hidden linearization: because of (0.3), (0.5) is an exact nonlinear solution.

The affine part is not in `L^2(R^3)`.  This is why the result below is an exact **model no-go**, not
a Clay-admissible counterexample.

---

## 1. Exact Kelvin/shear solution

Take

\[
 f(0,x_1)=B\cos(k_0x_1),\qquad B>0,\ k_0>0.
 \tag{1.1}
\]

Define

\[
 k(t):=k_0e^{\gamma t}
 \tag{1.2}
\]

and

\[
 D(t):=\exp\!\left[-\nu\int_0^t k(s)^2\,ds\right]
 =\exp\!\left[-\frac{\nu k_0^2}{2\gamma}
                 (e^{2\gamma t}-1)\right].
 \tag{1.3}
\]

Then

\[
 \boxed{
 f(t,x_1)=B D(t)\cos(k(t)x_1)
 }
 \tag{1.4}
\]

solves (0.6) exactly.  Indeed, `k'=gamma k`; the phase derivative from `partial_t f` is cancelled by
`-gamma x_1 partial_1 f`, while `D'=-nu k(t)^2D` gives diffusion.

Thus the low strain moves the high Fourier frequency exponentially:

\[
 k_0\longmapsto k(t)=e^{\gamma t}k_0.
 \tag{1.5}
\]

This is pure frequency deformation by incompressible strain, not amplitude growth from the high
self-interaction (which vanishes identically here).

---

## 2. Fixed LP block and exact commutator

Use the smooth LP decomposition of the parent FDT record.  Let

\[
 \varphi_j(\xi)=\varphi(2^{-j}\xi),\qquad \lambda_j=2^j.
\]

For the pure mode (1.4), set

\[
 m_j(t):=\varphi_j(k(t)e_1).
 \tag{2.1}
\]

Then

\[
 \Delta_jw(t)=m_j(t)w(t).
 \tag{2.2}
\]

For the low-high commutator from the previous gate,

\[
 \mathcal C_j(a,w):=\mathbb P[\Delta_j,a\cdot\nabla]w,
 \tag{2.3}
\]

all vector complications disappear in this geometry:

- `w` and `a·grad w` are in the `e_3` direction and independent of `x_3`, hence already
  divergence-free;
- Leray projection is the identity on this mode;
- `(w·grad)a=0` exactly.

Applying `Delta_j` to (0.6) and comparing with (2.2) gives the exact identity

\[
 \boxed{
 \mathcal C_j(a,w(t))=-m_j'(t)w(t).
 }
 \tag{2.4}
\]

Equivalently, the commutator is precisely the derivative of the LP cutoff seen along the strained
frequency trajectory.  There is no additional small parameter.

---

## 3. Exact low-flow conjugation

Let `X(t,y)=e^{tS_gamma}y` be the divergence-free low flow.  In coordinates `x=X(t,y)`, define

\[
 g(t,y):=w(t,X(t,y)).
 \tag{3.1}
\]

The phase is now fixed:

\[
 g(t,y)=e_3 B D(t)\cos(k_0y_1).
 \tag{3.2}
\]

The price of removing transport is anisotropic diffusion.  Since

\[
 e^{-tS_\gamma^T}e_1=e^{\gamma t}e_1,
\]

the conjugated Laplacian has Fourier quadratic form

\[
 q_t(\eta)=|e^{-tS_\gamma^T}\eta|^2.
 \tag{3.3}
\]

The fixed Eulerian LP projector becomes a time-dependent multiplier

\[
 M_j(t):\quad
 \widehat{M_j(t)h}(\eta)
 =\varphi_j(e^{-tS_\gamma^T}\eta)\widehat h(\eta).
 \tag{3.4}
\]

On the fixed mode `eta=k_0 e_1`, this is exactly `m_j(t)`.

Because both the conjugated diffusion and `M_j(t)` are Fourier multipliers, they commute.  Hence the
conjugated block satisfies

\[
 \partial_t(M_jg)
 =\nu L_t(M_jg)+(\partial_tM_j)g,
 \tag{3.5}
\]

where `L_t` is the conjugated anisotropic Laplacian.

Let `U_L(t,s)` denote the corresponding anisotropic heat propagator.  The signed dynamic commutator
Duhamel term is therefore

\[
 \mathcal K_j(t)
 :=\int_0^tU_L(t,s)(\partial_sM_j(s))g(s)\,ds.
 \tag{3.6}
\]

On the single mode, the heat factors from `[0,s]` and `[s,t]` multiply to the same full heat factor
from `[0,t]`.  The time integral telescopes exactly:

\[
 \boxed{
 \mathcal K_j(t)
 =[m_j(t)-m_j(0)]\,g(t).
 }
 \tag{3.7}
\]

Thus low-flow conjugation does **not** turn the LH commutator into a small oscillatory remainder.  It
turns it into an exact boundary displacement of the deformed LP multiplier.

This is the load-bearing identity of the decision.

---

## 4. One-viscous-window critical scaling

Use the parent viscous-window length

\[
 \tau_j=\frac{a_*}{\nu\lambda_j^2}.
 \tag{4.1}
\]

Choose a radius `rho>0` at which

\[
 m_*:=\varphi(\rho e_1)>0.
 \tag{4.2}
\]

Because `varphi` has compact annular support, one can choose `sigma>0` so large that

\[
 \varphi(\rho e^{-\sigma a_*}e_1)=0.
 \tag{4.3}
\]

Set

\[
 \gamma:=\sigma\nu\lambda_j^2,
 \qquad
 k_0:=\rho e^{-\sigma a_*}\lambda_j.
 \tag{4.4}
\]

Then

\[
 k(\tau_j)=\rho\lambda_j,
 \qquad
 m_j(0)=0,
 \qquad
 m_j(\tau_j)=m_*.
 \tag{4.5}
\]

The heat factor at the end of the window is

\[
 \boxed{
 D(\tau_j)
 =\exp\!\left[-\frac{\rho^2}{2\sigma}
                (1-e^{-2\sigma a_*})\right].
 }
 \tag{4.6}
\]

Crucially, this expression is independent of `j` and `nu`, and

\[
 D(\tau_j)\longrightarrow1
 \qquad(\sigma\to\infty).
 \tag{4.7}
\]

Strong strain moves the mode into the target shell late in the window, before viscosity has time to
damp it substantially.

---

## 5. Exact failure of a fixed signed dynamic margin

Fix any `theta` with

\[
 0<\theta<1.
 \tag{5.1}
\]

Choose `epsilon` with

\[
 \theta<\epsilon<1.
 \tag{5.2}
\]

Then choose `sigma` in Section 4 large enough that

\[
 \epsilon D(\tau_j)>\theta.
 \tag{5.3}
\]

Normalize the underlying shear amplitude by

\[
 B:=\frac{\epsilon c_0\nu\lambda_j}{m_*}.
 \tag{5.4}
\]

At the final time, the Eulerian target block is still strictly subcritical:

\[
 \lambda_j^{-1}\|\Delta_jw(\tau_j)\|_\infty
 =\epsilon c_0\nu D(\tau_j)
 <c_0\nu.
 \tag{5.5}
\]

But the exact signed conjugated commutator term (3.7) has size

\[
 \begin{aligned}
 \lambda_j^{-1}\|\mathcal K_j(\tau_j)\|_\infty
 &=\lambda_j^{-1}|m_*-0|\,B D(\tau_j)\\
 &=\epsilon c_0\nu D(\tau_j)\\
 &>\theta c_0\nu.
 \end{aligned}
 \tag{5.6}
\]

In particular choose `theta=1/2`.  Then

\[
 \boxed{
 \lambda_j^{-1}\|\mathcal K_j(\tau_j)\|_\infty
 >\frac12c_0\nu
 }
 \tag{5.7}
\]

while the target block itself remains subcritical.

There is no absolute-value-in-time loss here: (3.7) is the **exact signed vector Duhamel integral
after low-flow conjugation**.

---

## 6. The stronger interpretation: large LH is shell transport, not dangerous growth

The same exact solution explains why the previous strategy was conceptually over-demanding.

The high shear does not self-amplify:

\[
 (w\cdot\nabla)w=0.
\]

Its amplitude only decays by viscosity.  What the low strain does is move its Fourier frequency
across the fixed dyadic shell.  The large commutator in (5.6) records that **spectral relabeling**.

Thus an order-critical LH Duhamel contribution need not represent a dangerous forward cascade or
nonlinear amplitude creation.  It may be the bookkeeping cost of observing a benign packet in a
fixed Eulerian LP frame while the low flow deforms frequency.

This is important for the parent FDT route:

- trying to prove a small margin for the LH term **separately** is not merely technically hard;
- the affine model shows that such a margin is structurally false after the most natural exact
  low-flow conjugation;
- a viable frequency-transfer functional should absorb material shell transport rather than count it
  as nonlinear injection.

---

## 7. Decision

### Killed

\[
 \boxed{\texttt{FDT-LH-DYN-AFF = NO}.}
\]

More explicitly, the exact affine trace-free strain model kills:

1. the claim that signed time integration alone forces the low-high commutator below a fixed critical
   margin;
2. the claim that low-flow conjugation automatically makes the deformation commutator perturbative;
3. any proof whose only new ingredient beyond `FDT-LH-OP` is “move to Lagrangian coordinates and
   use cancellation” without a quantitative strain-distortion restriction;
4. the idea that a large LH commutator necessarily measures dangerous energy transfer rather than
   shell deformation.

### Not killed

1. `FDT-INJ` for real divergence-free Schwartz data on `R^3` remains OPEN;
2. an admissible-data theorem exploiting a genuinely propagated restriction on low-frequency strain;
3. cancellation between LH and other pieces of the full nonlinear Duhamel term;
4. a material/deformed dyadic decomposition which follows the low flow and does not count shell
   transport as injection;
5. HH backscatter and HL tails.

The affine background is not finite energy.  Therefore (5.7) is **not** a valid fixed-datum NO
certificate for the parent `FDT-INJ` quantifiers.

---

## 8. What coefficient the exact model says is unavoidable

For a general low flow, frequency deformation is controlled by the deformation gradient.  The
natural dimensionless quantity over one `j`-window is schematically

\[
 \boxed{
 \mathcal S_j(t)
 :=\int_{t-\tau_j}^t
   \|\nabla u_{\le j-2}(s)\|_\infty\,ds.
 }
 \tag{8.1}
\]

In the affine model,

\[
 \mathcal S_j=\gamma\tau_j=\sigma a_*,
 \tag{8.2}
\]

and the shell-frequency distortion is exactly exponential in this quantity.

The previous `FDT-LH-OP` counterfamily already showed that ordinary energy and one-window enstrophy
do not make this kind of low strain coefficient small.  Therefore reintroducing (8.1) as an
assumption merely moves the proof wall unless an **independent finite or small budget** for it is
proved.

This is the precise reason the separate LH route is now parked.

---

## 9. Recommended route change: material-frequency injection

The affine no-go suggests changing the object rather than trying a stronger estimate on the same
one.

A next theorem-shaped candidate should define a **material/deformed dyadic projector** following the
low-frequency divergence-free flow, so that in the affine model the multiplier deformation in
(3.7) is absorbed exactly into the projector rather than charged as nonlinear injection.

Call the next gate provisionally

\[
 \boxed{\texttt{FDT-MAT}.}
\]

The first task is not to prove regularity.  It is to decide whether one can define, for a finite
energy smooth NS solution and each high `j`, a low-flow-conjugated projector `Delta_j^mat(t)` such
that:

1. the principal `u_{<=j-2}·grad` transport commutes with `Delta_j^mat` by construction;
2. the affine model has **zero** material-shell transport defect;
3. the remaining diffusion/Leray/paraproduct defects can be written explicitly;
4. no coefficient `int F`, `int ||grad u||_infinity`, Serrin norm, or bounded `H^3` is inserted by
   hand;
5. the resulting one-window nonlinear injection still implies a known continuation criterion.

If this cannot be done without the strain budget (8.1), the frequency-transfer route should be
reassessed before spending effort on HH estimates or Lean LP plumbing.

---

## 10. Formalization ruling

No Lean file is added.

The new result is an exact analytic model identity involving affine transport, a deformed LP
multiplier, and anisotropic heat flow.  The repository still lacks the LP/Bony/paracomposition layer.
Formalizing only the scalar exponential identities would not move the actual proof frontier.

`FORMAL_SCOPE.md` and `STATUS.md` therefore remain unchanged.

---

## 11. Claim boundary

This record proves an exact no-go for a proposed **mechanism**, not a Clay result.

- The velocity `a+w` is a genuine exact smooth unforced NS solution.
- The affine background `a=S_gamma x` is not in `L^2` and is not Schwartz.
- Hence it is not admissible initial data for Clay A/C.
- `FDT-INJ` on admissible data remains open.
- No global regularity or finite-time blow-up statement is proved.

The durable conclusion is narrower and useful: **exact signed low-flow conjugation does not make the
low-high commutator small; in the canonical affine strain model it telescopes to an order-one LP
multiplier displacement.**