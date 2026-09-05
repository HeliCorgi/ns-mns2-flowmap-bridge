# FDT low-high commutator decision — 2026-09-05

**Status: NO-GO FOR THE OPERATOR/ENERGY-BUDGET CLOSURE; AFFINE SIGNED-DYNAMIC REPAIR ALSO KILLED.**

**Primary verdict:** `FDT-LH-OP = NO`.

**Follow-up:** the exact affine-strain signed-dynamic repair is decided separately in
`docs/gates/FDT_LH_DYN_AFFINE_DECISION_2026-09-06.md`, with verdict
`FDT-LH-DYN-AFF = NO`.  The parent `FDT-INJ` statement on real divergence-free Schwartz data
remains OPEN.

This note attacks the first analytic sub-gate left by
`docs/gates/FREQUENCY_DISSIPATION_TRANSFER_DECISION_2026-09-05.md`.
The parent gate `FDT-INJ` is unchanged and remains OPEN.

The point is to separate two logically different questions which were previously both called
“FDT-LH”:

1. can the **low-high commutator operator itself**, after one viscous heat window, have a fixed
   `c_0 nu` margin from spectral separation, incompressibility, Leray projection, and the ordinary
   energy/dissipation budget alone?;
2. can the **actual signed time-dependent Navier–Stokes trajectory** produce extra temporal/phase
   cancellation which makes its low-high contribution small for all sufficiently high blocks?

The first question has a clean NO answer in this record.  The natural affine low-flow-conjugation
version of the second question is also NO by the 2026-09-06 follow-up, but the fully admissible
finite-energy/Schwartz `R^3` version is not refuted.

No global regularity theorem, no blow-up theorem, and no Clay alternative is proved.

---

## 0. Fixed LP conventions

Use the smooth Littlewood–Paley decomposition from the parent FDT record.  Write the Fourier
multiplier of `Delta_j` as

\[
\varphi_j(\xi)=\varphi(2^{-j}\xi),\qquad \lambda_j=2^j.
\]

Let `P` be the Leray projector.  For a low vector field `a` and a high vector field `b`, define the
projected low-high commutator

\[
\boxed{
\mathcal C_j(a,b)
:=\mathbb P\,[\Delta_j,a\cdot\nabla]b
=\mathbb P\bigl(\Delta_j(a\cdot\nabla b)-a\cdot\nabla\Delta_j b\bigr).
}
\tag{0.1}
\]

The standard kernel estimate is

\[
\|\mathcal C_j(a,b)\|_\infty
\lesssim
\|\nabla a\|_\infty\,\|b\|_\infty
\tag{0.2}
\]

when `a` is spectrally below `j` and `b` is spectrally concentrated near `j`.  The commutator gain
cancels the derivative on the high factor; it does **not** remove the low strain.

The parent one-viscous-window length is

\[
\tau_j=\frac{a_*}{\nu\lambda_j^2}.
\tag{0.3}
\]

---

## 1. Exact operator-level YES/NO question

Fix any positive margin fraction `theta>0`.  Define the frozen one-window low-high operator

\[
\boxed{
\mathcal W_j(a,b)
:=\lambda_j^{-1}
\int_0^{\tau_j}
 e^{\nu(\tau_j-s)\Delta}\,\mathcal C_j(a,b)\,ds .
}
\tag{1.1}
\]

The exact decision object is:

> ### `FDT-LH-OP`
> Is there a fixed `theta>0` and a class-wide argument using only
> - low/high spectral separation,
> - divergence-free structure,
> - the exact Leray projector,
> - the exact annular Stokes multiplier,
> - a subcritical target high block
>   `lambda_j^{-1}||b||_infinity <= epsilon c_0 nu` with fixed `0<epsilon<1`, and
> - the ordinary energy and one-window enstrophy/dissipation budgets,
>
> which forces
>
> \[
> \|\mathcal W_j(a,b)\|_\infty\le \theta c_0\nu
> \tag{1.2}
> \]
>
> for every sufficiently high `j`?

Here “using the ordinary energy/dissipation budgets” means that the proposed smallness is supposed
to come from quantities that vanish when the `L^2` energy and the viscous-window enstrophy budget
vanish.  A coefficient such as `int ||grad u||_infinity`, `int F`, a Serrin norm, or bounded `H^3`
is not an energy-budget closure; those are excluded by the parent gate.

### Verdict

\[
\boxed{\textbf{NO}.}
\]

There are real divergence-free Schwartz low/high packets for which the normalized high block is
strictly subcritical and both the energy and the one-window enstrophy budget are arbitrarily small,
yet the frozen low-high commutator window is an arbitrarily large multiple of `c_0 nu`.

---

## 2. The low-high commutator is genuinely nonzero

The Fourier formula for (0.1) is, with `zeta=xi-eta`,

\[
\widehat{\mathcal C_j(a,b)}(\xi)
=
 i\,P(\xi)
 \int
   (\zeta\cdot\widehat a(\eta))
   \bigl[\varphi_j(\xi)-\varphi_j(\zeta)\bigr]
   \widehat b(\zeta)
\,d\eta .
\tag{2.1}
\]

Because the LP multiplier is not constant on its transition annulus, choose one high frequency
`zeta_0` and one much smaller low frequency `eta_0` such that

\[
\varphi(\zeta_0+\eta_0)\ne\varphi(\zeta_0).
\tag{2.2}
\]

Choose `eta_0` not parallel to `zeta_0`.  Then choose a low polarization `A_0` and high
polarization `B_0` satisfying

\[
A_0\cdot\eta_0=0,
\qquad
A_0\cdot\zeta_0\ne0,
\qquad
B_0\cdot\zeta_0=0,
\tag{2.3}
\]

and, generically,

\[
P(\eta_0+\zeta_0)B_0\ne0.
\tag{2.4}
\]

The central bilinear symbol

\[
 i(A_0\cdot\zeta_0)
 \bigl[\varphi(\eta_0+\zeta_0)-\varphi(\zeta_0)\bigr]
 P(\eta_0+\zeta_0)B_0
\tag{2.5}
\]

is therefore nonzero.

Take sufficiently small smooth Fourier bumps around `+-eta_0` and `+-zeta_0`, project the
polarizations pointwise onto the divergence-free fibers, and impose conjugate symmetry.  This gives
**real divergence-free Schwartz fields** `a,b` with disjoint low/high Fourier supports and

\[
\boxed{\mathcal C_0(a,b)\not\equiv0.}
\tag{2.6}
\]

Normalize `||b||_infinity=1`.

---

## 3. Heat integration does not create a cancellation

Define the fixed base heat-resolved commutator

\[
G:=\int_0^{a_*} e^{\rho\Delta}\mathcal C_0(a,b)\,d\rho.
\tag{3.1}
\]

On the nonzero Fourier support of `C_0`, the multiplier of this integral is

\[
\frac{1-e^{-a_*|\xi|^2}}{|\xi|^2}>0.
\tag{3.2}
\]

Hence

\[
\boxed{G\not\equiv0.}
\tag{3.3}
\]

Set

\[
\Gamma_{LH}:=\|G\|_\infty>0.
\tag{3.4}
\]

Thus Leray projection, incompressibility, LP commutation, and one full annular heat window do not
supply an automatic low-high cancellation.

---

## 4. Critical dyadic counterfamily

Fix `0<epsilon<1`, for example `epsilon=1/4`, and let `M>0`.  For a dyadic frequency
`lambda_j=2^j`, define

\[
a_{j,M}(x)=M\nu\lambda_j\,a(\lambda_jx),
\qquad
b_j(x)=\epsilon c_0\nu\lambda_j\,b(\lambda_jx).
\tag{4.1}
\]

Their Fourier supports remain separated by the same fixed low/high ratio.  The target high packet is
strictly subcritical:

\[
\boxed{
\lambda_j^{-1}\|b_j\|_\infty=\epsilon c_0\nu<c_0\nu.
}
\tag{4.2}
\]

Exact dyadic scaling of `Delta_j`, `P`, the derivative, and the heat semigroup gives

\[
\mathcal C_j(a_{j,M},b_j)(x)
=
M\epsilon c_0\nu^2\lambda_j^3
\,\mathcal C_0(a,b)(\lambda_jx).
\tag{4.3}
\]

With `tau_j=a_*/(nu lambda_j^2)` and the change of variable
`rho=nu lambda_j^2(\tau_j-s)`, (1.1) becomes

\[
\boxed{
\mathcal W_j(a_{j,M},b_j)(x)
=
M\epsilon c_0\nu\,G(\lambda_jx).
}
\tag{4.4}
\]

Therefore

\[
\boxed{
\|\mathcal W_j(a_{j,M},b_j)\|_\infty
=M\epsilon\Gamma_{LH}\,c_0\nu .
}
\tag{4.5}
\]

Given any proposed fixed margin `theta c_0 nu`, choose

\[
M>\frac{\theta}{\epsilon\Gamma_{LH}}.
\tag{4.6}
\]

Then (1.2) fails for every dyadic `j`.

---

## 5. The ordinary energy and viscous-window budget can simultaneously vanish

Because the low and high Fourier supports are disjoint, their `L^2` cross term is zero.  Hence

\[
\|a_{j,M}+b_j\|_2^2
=
\nu^2\lambda_j^{-1}
\left(
 M^2\|a\|_2^2
 +\epsilon^2c_0^2\|b\|_2^2
\right).
\tag{5.1}
\]

For fixed `M`, this tends to zero as `j->infinity`.

Likewise

\[
\|\nabla a_{j,M}\|_2^2
=M^2\nu^2\lambda_j\|\nabla a\|_2^2,
\qquad
\|\nabla b_j\|_2^2
=\epsilon^2c_0^2\nu^2\lambda_j\|\nabla b\|_2^2.
\tag{5.2}
\]

Multiplying by the physical viscous-window factor `nu tau_j=a_*/lambda_j^2` gives

\[
\boxed{
\nu\tau_j
\|\nabla(a_{j,M}+b_j)\|_2^2
=O(\lambda_j^{-1})\to0.
}
\tag{5.3}
\]

Thus for every `E_*>0`, every `D_*>0`, and every fixed target margin `theta>0`, one can first choose
`M` by (4.6) and then choose `j` so large that simultaneously

\[
\|a_{j,M}+b_j\|_2^2<E_*,
\qquad
\nu\tau_j\|\nabla(a_{j,M}+b_j)\|_2^2<D_*,
\tag{5.4}
\]

while

\[
\|\mathcal W_j(a_{j,M},b_j)\|_\infty>\theta c_0\nu.
\tag{5.5}
\]

This is the binding no-go: **subcritical high amplitude plus arbitrarily small energy and
one-window enstrophy budget do not force a small low-high commutator window.**

---

## 6. Actual Navier–Stokes trajectory: the pointwise coefficient obstruction is already present at t=0

The preceding counterfamily is an operator theorem, not a frozen-field claim about an actual
one-window solution.  However it also appears immediately on genuine trajectories.

Use the real divergence-free Schwartz datum

\[
u_0=a_{j,M}+b_j.
\tag{6.1}
\]

The repository's existing local theory, and standard classical local well-posedness, give an actual
smooth unforced Navier–Stokes solution for a positive time.

Let `J_j^{LH}(t)` denote the **signed vector low-high commutator Duhamel term** on `[0,t]`, before
applying the final norm.  Smoothness implies

\[
\boxed{
\frac{d}{dt}J_j^{LH}(t)\Big|_{t=0}
=
\lambda_j^{-1}\mathcal C_j(a_{j,M},b_j).
}
\tag{6.2}
\]

Therefore

\[
\left\|\frac{d}{dt}J_j^{LH}(0)\right\|_\infty
=
M\epsilon c_0\nu^2\lambda_j^2
\|\mathcal C_0(a,b)\|_\infty.
\tag{6.3}
\]

This can be arbitrarily large while the initial energy tends to zero by taking `j` high.  Hence no
**pointwise-in-time** estimate of the low-high commutator coefficient from the ordinary energy
budget can be the missing theorem.

What (6.2) does **not** prove is that the signed time-integrated commutator on the actual trajectory
must exceed a fixed margin later in the window.  The actual solution may generate transport,
phase, polarization, or temporal cancellation.  The exact affine-strain follow-up shows that the
most natural low-flow-conjugation version of such cancellation is nevertheless false as a mechanism;
see `FDT_LH_DYN_AFFINE_DECISION_2026-09-06.md`.

---

## 7. Relation to the standard commutator bound

The usual absolute estimate gives schematically

\[
\|\mathcal C_j(u_{\le j-2},u_{\sim j})\|_\infty
\lesssim
\|\nabla u_{\le j-2}\|_\infty
\|u_{\sim j}\|_\infty.
\tag{7.1}
\]

If the target high packet is subcritical,

\[
\lambda_j^{-1}\|u_{\sim j}\|_\infty\lesssim c_0\nu,
\]

then the normalized one-window absolute estimate has the form

\[
\mathfrak I_j^{LH,abs}
\lesssim
c_0\nu
\int_{t-\tau_j}^t
\|\nabla u_{\le j-2}(s)\|_\infty\,ds.
\tag{7.2}
\]

Thus the missing coefficient is precisely a low-frequency deformation/strain integral.  Replacing
it by

- `int F`,
- `int ||grad u||_infinity`,
- a Serrin norm,
- bounded `H^3`,

would merely import a continuation wall forbidden by the parent gate.

The counterfamily above shows that ordinary energy and viscous-window enstrophy cannot replace this
coefficient.  The affine follow-up shows that exact signed low-flow conjugation does not remove the
same deformation either: it becomes an LP multiplier boundary displacement.

---

## 8. Decision and scope

### Killed

- **`FDT-LH-OP`: NO.**  There is no universal fixed low-high commutator margin coming from the
  operator structure plus ordinary energy/dissipation budget.
- Any proof that estimates the low-high commutator absolutely and then hopes the high-frequency
  viscous window itself makes the coefficient small.
- Any pointwise coefficient estimate that tries to control the low strain by only `L^2` energy or
  the one-window `L^2` enstrophy budget.
- Any claim that incompressibility + Leray projection annihilates the low-high commutator.

### Not killed by this record alone

- The parent **`FDT-INJ`** statement.  It remains OPEN.
- A datum-dependent high-frequency cutoff `J(u_0,nu,L)`.
- A fully admissible finite-energy/Schwartz dynamic theorem using genuinely new propagated
  structure.
- Cancellation between the LH piece and other parts of the full nonlinear Duhamel term.
- A material/deformed dyadic observable which absorbs low-flow shell transport.
- The high-high and high-low pieces of the FDT decomposition.

The family `(a_{j,M},b_j)` is a family of different data.  By the explicit NO rule in the parent
record, this does **not** refute `FDT-INJ`, because `J` is allowed to depend on the datum.

---

## 9. Follow-up ruling after the affine model

The 2026-09-06 exact affine record proves

\[
\boxed{\texttt{FDT-LH-DYN-AFF = NO}.}
\]

For a trace-free affine strain plus transverse shear, the full nonlinear NS equations reduce exactly
to strain-diffusion of the shear.  After low-flow conjugation, the signed commutator Duhamel term
is

\[
[m_j(t)-m_j(0)]g(t),
\]

so it is an order-one spectral-shell displacement, not a small oscillatory remainder.  It can exceed
`(1/2)c_0 nu` while the final target block is still subcritical.

The affine background is not in `L^2`, so this is not a Clay-admissible counterexample.  But it kills
the proposed mechanism “Lagrangianize the LH term and signed cancellation will make it small.”

**Strategic ruling:** separate-LH fixed-margin estimates are now PARKED.  The recommended next gate
is `FDT-MAT`: define a material-frequency observable that follows the low flow and therefore does
not charge benign shell relabeling as nonlinear injection.

---

## 10. Formalization ruling

No Lean file is added here.

The result is an analytic no-go about a Littlewood–Paley commutator and its critical scaling.  The
repository does not yet contain the LP/Bony `L^infinity` layer needed to mechanize the actual
operator.  Formalizing only the scalar scaling equalities would not move the proof frontier and
would violate the standing “no plumbing before an analytic gate survives” rule.

`FORMAL_SCOPE.md` and `STATUS.md` therefore remain unchanged.