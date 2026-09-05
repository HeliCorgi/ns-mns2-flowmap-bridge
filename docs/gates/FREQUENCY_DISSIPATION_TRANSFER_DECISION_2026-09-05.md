# Frequency / dissipation-scale transfer YES/NO gate — 2026-09-05

**Status: OPEN DECISION THEOREM / REGULARITY-SIDE RESEARCH GATE.**

**Decision object: `FDT-INJ`.**

This record deliberately leaves the parked Astra S15 traveling-max cone and opens a different
whole-space route based on Littlewood–Paley frequency localization, the Navier–Stokes Stokes
semigroup, and the dissipation wavenumber of Cheskidov–Shvydkoy.

The present repository `SPEC.md` still names the `R^3`, `f=0`, axisymmetric-with-swirl breakdown
track as the primary attack.  `FDT-INJ` is therefore a **cross-track regularity experiment**.  It does
not silently change `SPEC.md`, `PROJECT_GOAL.md`, or the current Clay-side priority.  If `FDT-INJ`
were proved for all admissible data, it would support the whole-space regularity alternative A,
not the current breakdown construction C.

No global regularity theorem, no Navier–Stokes blow-up theorem, and no Clay alternative is proved
here.  The point of this file is to replace the vague phrase “control nonlinear transfer at the
dissipation scale” by one exact YES/NO statement with a complete sufficiency chain and a
counterexample-first attack protocol.

Primary frequency reference:

- A. Cheskidov and R. Shvydkoy, *A unified approach to regularity problems for the 3D
  Navier–Stokes and Euler equations: the use of Kolmogorov's dissipation range*,
  `https://arxiv.org/abs/1102.1944`.

---

## 0. Fixed analytic conventions

Fix once and for all a smooth inhomogeneous Littlewood–Paley decomposition

\[
 u=\sum_{j\ge-1}u_j,\qquad u_j=\Delta_j u,\qquad \lambda_j=2^j.
\]

Let `P` denote the Leray projector.  The exact projected Navier–Stokes mild equation is

\[
 u(t)=e^{\nu(t-s)\Delta}u(s)
 -\int_s^t e^{\nu(t-\tau)\Delta}
      \mathbb P\nabla\!\cdot(u\otimes u)(\tau)\,d\tau.
\tag{0.1}
\]

For each dyadic annulus there are fixed constants `C_H >= 1` and `c_H>0`, depending only on the
chosen decomposition, such that

\[
 \|e^{\nu\tau\Delta}v_j\|_\infty
 \le C_H e^{-c_H\nu\lambda_j^2\tau}\|v_j\|_\infty
 \qquad(\tau\ge0).
\tag{0.2}
\]

Choose once and for all `a_*>0` so large that

\[
 C_H e^{-c_Ha_*}\le\frac14.
\tag{0.3}
\]

The corresponding one-viscous-window length at block `j` is

\[
 \tau_j:=\frac{a_*}{\nu\lambda_j^2}.
\tag{0.4}
\]

The constants in this section are decomposition constants, not adjustable per datum or per time.

---

## 1. Dissipation wavenumber and the established continuation target

Fix the sufficiently small constant `c_0>0` in the Cheskidov–Shvydkoy dissipation-wavenumber
criterion.  For the actual maximal smooth unforced solution define

\[
 Q(t):=\min\Bigl\{q\in\mathbb N_0:
 \lambda_p^{-1}\|u_p(t)\|_\infty<c_0\nu
 \text{ for every }p>q\Bigr\},
 \qquad
 \Lambda(t):=2^{Q(t)},
\tag{1.1}
\]

and

\[
 F(t):=\sup_{-1\le j\le Q(t)}
 \lambda_j\|u_j(t)\|_\infty.
\tag{1.2}
\]

For smooth times the defining set is nonempty.  The published continuation theorem gives

\[
 \int_0^T F(t)\,dt<\infty
 \quad\Longrightarrow\quad
 \text{regular continuation through }T.
\tag{1.3}
\]

The same framework gives the familiar gap

\[
 \Lambda\in L^1_t\quad\text{from energy},
\qquad
 \Lambda\in L^{5/2}_t\quad\text{is sufficient for regularity},
\tag{1.4}
\]

and the critical-tail sufficient condition

\[
 \limsup_{j\to\infty}\ \sup_{0<t<T_*}
 \lambda_j^{-1}\|u_j(t)\|_\infty<c_0\nu.
\tag{1.5}
\]

The quantifier order in (1.5) is the point: smoothness at each fixed time only gives decay as
`j -> infinity` for that time; it does not give one terminal-time-uniform tail index.

---

## 2. The new exact object: one-viscous-window nonlinear injection

For `t>0` define

\[
 s_j(t):=\max\{0,t-\tau_j\}.
\tag{2.1}
\]

Define the **signed/vector-valued dyadic Duhamel injection**

\[
 \boxed{
 \mathfrak I_j(t):=
 \lambda_j^{-1}
 \left\|
 \int_{s_j(t)}^t
 e^{\nu(t-\tau)\Delta}
 \Delta_j\mathbb P\nabla\!\cdot(u\otimes u)(\tau)\,d\tau
 \right\|_\infty .
 }
\tag{2.2}
\]

The norm is deliberately taken **after** the time integral.  Replacing (2.2) by the integral of
pointwise norms throws away temporal, phase, polarization, and triadic cancellation and creates a
strictly stronger object.  Such a replacement is not authorized by this gate.

`FDT-INJ` asks whether the exact Navier–Stokes nonlinearity injects less than one critical unit into
every sufficiently high block during one viscous time.

---

## 3. Exact YES/NO question

> ### `FDT-INJ`
> Does there exist a choice of the fixed decomposition constants above such that the following is
> true?
>
> For **every** viscosity `nu>0`, **every** real divergence-free Schwartz datum
> `u_0 in S_sigma(R^3)`, and **every** finite horizon `L>0`, let `u` be its actual maximal smooth
> unforced Navier–Stokes solution on `[0,T_*)`.  Then there exists a finite integer
>
> \[
> J=J(u_0,\nu,L)
> \tag{3.1}
> \]
>
> such that
>
> \[
> \boxed{
> \sup_{0<t<\min\{L,T_*\}}
> \sup_{j\ge J}\mathfrak I_j(t)
> \le \frac12 c_0\nu .
> }
> \tag{FDT-INJ}
> \]

**Current verdict: OPEN.**

The constants `1/4` and `1/2` are bookkeeping margins.  Any fixed pair of margins whose sum is
strictly less than one gives the same decision problem after changing `a_*`.

The datum-dependent `J` is essential.  A universal `J` independent of `u_0` is neither needed nor
expected.

---

## 4. Why YES is enough: first-contact theorem

This section records the complete reduction from `FDT-INJ` to the published high-frequency-tail
criterion.  No new Navier–Stokes estimate is hidden here.

Because `u_0` is Schwartz,

\[
 \lambda_j^{-1}\|(u_0)_j\|_\infty\to0.
\]

After increasing `J` if necessary, arrange

\[
 C_H\lambda_j^{-1}\|(u_0)_j\|_\infty
 \le\frac14c_0\nu
 \qquad(j\ge J).
\tag{4.1}
\]

Assume for contradiction that some high block first reaches the critical threshold.  Let `t_*` be
the first time and `j_*>=J` an index with

\[
 \lambda_{j_*}^{-1}\|u_{j_*}(t_*)\|_\infty=c_0\nu,
\tag{4.2}
\]

while all `j>=J` were strictly below the threshold at earlier times.

Apply the exact dyadic mild equation on `[s_{j_*}(t_*),t_*]`.

### Case A: `t_* >= tau_{j_*}`

At the left endpoint the first-contact definition gives

\[
 \lambda_{j_*}^{-1}\|u_{j_*}(t_*-\tau_{j_*})\|_\infty<c_0\nu.
\]

By (0.2)–(0.4), its homogeneous Stokes contribution at `t_*` is at most

\[
 \frac14c_0\nu.
\tag{4.3}
\]

`FDT-INJ` bounds the nonlinear Duhamel contribution by

\[
 \frac12c_0\nu.
\tag{4.4}
\]

Thus

\[
 \lambda_{j_*}^{-1}\|u_{j_*}(t_*)\|_\infty
 \le\frac34c_0\nu,
\]

contradicting (4.2).

### Case B: `t_* < tau_{j_*}`

Use the mild equation from time zero.  The homogeneous term is bounded by (4.1), and the nonlinear
term by (4.4), giving the same contradiction.

Hence no such first contact occurs, and

\[
 \boxed{
 \sup_{0<t<\min\{L,T_*\}}\sup_{j\ge J}
 \lambda_j^{-1}\|u_j(t)\|_\infty<c_0\nu.
 }
\tag{4.5}
\]

Therefore `Q(t)<=J-1` throughout the finite horizon.  Since only finitely many lower blocks remain,
Bernstein plus the energy bound makes `F` bounded on that horizon, hence

\[
 \int_0^{\min\{L,T_*\}}F(t)\,dt<\infty.
\tag{4.6}
\]

If `T_*<infinity`, choose `L>T_*`; the published continuation criterion then extends the solution
through `T_*`, a contradiction.  Consequently a proof of `FDT-INJ` with the quantifiers in Section 3
would yield global smoothness for all unforced Schwartz data on `R^3`, i.e. a route to the official
whole-space regularity alternative A after the standard pressure/energy/admissibility checks.

This implication is why the gate is genuinely load-bearing rather than a diagnostic.

---

## 5. Counterexample-first preflight: kill the tempting static shortcut

Before attacking `FDT-INJ`, rule out a common disguised shortcut.  Energy gives

\[
 E(t):=\|u(t)\|_2^2\le E(0),
 \qquad
 \nu\int\|\nabla u\|_2^2<\infty.
\]

A tempting pointwise bridge would be

\[
 F(t)\,E(t)\le C(\nu)\|\nabla u(t)\|_2^2.
\tag{5.1}
\]

If true, it would immediately make `F` integrable (up to the harmless issue of a vanishing energy
denominator).  But (5.1) is **not** an admissible target: it is false already at time zero for smooth
Schwartz data.

Take a fixed nonzero divergence-free Schwartz field `v` with Fourier support in one annulus and set

\[
 u_0^{A,\lambda}(x)=A\,v(\lambda x).
\tag{5.2}
\]

Choose `A/\lambda` above the dissipation threshold, so the active annulus is the dissipation block.
Then, up to fixed profile constants,

\[
 F(0)\sim A\lambda,
 \qquad
 E(0)\sim A^2\lambda^{-3},
 \qquad
 \|\nabla u_0\|_2^2\sim A^2\lambda^{-1},
\]

and therefore

\[
 \frac{F(0)E(0)}{\|\nabla u_0\|_2^2}
 \sim\frac A\lambda.
\tag{5.3}
\]

Taking `A=M\lambda` sends (5.3) to infinity.  Thus no datum-independent pointwise estimate of the
form (5.1) can be the missing theorem.

**Ruling:** the next proof attempt must be genuinely dynamical and use the one-viscous-window
Duhamel transfer, or another object with comparable time/phase information.  Energy plus a static
spectrum cannot close the gap.

---

## 6. What a YES proof is allowed to use

A valid proof may exploit:

1. the exact Leray symbol and incompressibility cancellation;
2. the exact Stokes multiplier on each dyadic annulus;
3. Bony low–high / high–low / high–high decomposition, with the principal transport cancellation
   retained rather than estimated absolutely;
4. time cancellation inside the vector integral (2.2);
5. phase, polarization, and geometric constraints specific to the actual Navier–Stokes bilinear form;
6. the global energy inequality as a budget, but not as a substitute for item 1–5.

The proof must not use an estimate that already assumes `F in L^1`, a Serrin norm, bounded `H^3`,
small critical norm, or any other continuation hypothesis equivalent to the desired conclusion.

Tao's averaged Navier–Stokes blow-up construction is a standing warning: energy cancellation plus
generic harmonic-analysis bounds alone are not enough.  A successful `FDT-INJ` proof must consume
structure of the **exact** Navier–Stokes nonlinearity that the averaged operator does not preserve.

---

## 7. Exact NO certificate

`FDT-INJ` is not killed by an arbitrary bad divergence-free snapshot, because `J` may depend on the
datum and the theorem concerns the actual time evolution.

A valid **NO** certificate must produce one fixed `nu>0`, one fixed real divergence-free Schwartz
datum `u_0`, one finite horizon `L`, and its actual smooth solution on the relevant pre-maximal
interval such that for every integer `J` there exist `j>=J` and
`0<t<min{L,T_*}` with

\[
 \mathfrak I_j(t)>\frac12c_0\nu.
\tag{7.1}
\]

Equivalently, the exact nonlinear evolution must create arbitrarily high critical-size one-window
injections for a single datum.  A family of different data with the bad block moved to higher and
higher frequency does **not** refute `FDT-INJ`, because the allowed `J(u_0,nu,L)` changes with the
datum.

Numerical evidence for (7.1) is diagnostic only unless a continuum error/certificate argument proves
it for the actual PDE.

---

## 8. First analytic attack decomposition

The next session should not try to estimate (2.2) in one shot.  Freeze one high `j` and split

\[
 \Delta_j\mathbb P\nabla\!\cdot(u\otimes u)
 =T_j^{LH}+T_j^{HL}+T_j^{HH}
\tag{8.1}
\]

by a fixed Bony decomposition.

Recommended order:

1. **LH commutator gate.**  Move the low-frequency transport through `Delta_j` and keep the
   divergence-free cancellation.  Decide whether the remaining one-window commutator can be bounded
   below the fixed `c_0 nu` margin without inserting `int F` by hand.
2. **HH backscatter gate.**  Treat comparable frequencies whose product returns to block `j`.
   This is the most likely source of a genuine obstruction because shell energy alone does not fix
   phase or concentration.
3. **HL tail gate.**  Close the summable tail only after the two load-bearing pieces are explicit.
4. If any one component admits an exact counterfamily for a single actual trajectory, record a NO
   decision.  Do not compensate by strengthening the theorem with a hidden regularity assumption.

The first concrete sub-decision should be the **LH one-window commutator inequality**, not a full
Littlewood–Paley formalization.

---

## 9. Relation to the existing Lean stack

No Lean theorem is added by this decision record.  The repository already contains useful pieces:

- `Formal/R3StokesL2Operator.lean` and the Stokes frequency-symbol files;
- `Formal/R3StokesH2H3Smoothing.lean` for a positive-time explicit Stokes smoothing bound;
- `Formal/R3LerayL2Operator.lean`, `Formal/R3LerayFourierBridge.lean`, and related Leray files;
- `Formal/R3ProjectedSobolevConvection.lean` for the completed projected
  `H^3 x H^3 -> H^2` convection map;
- the exact Fourier product/convolution and weighted Young infrastructure recorded in
  `FORMAL_SCOPE.md`.

What is **not** yet formalized for `FDT-INJ` is equally important:

1. the fixed inhomogeneous Littlewood–Paley projector family on the physical `R^3` carrier;
2. annular `L^infinity` Bernstein estimates;
3. the exponential band-limited heat estimate (0.2) in the required `L^infinity` form;
4. the dyadic projected Duhamel identity in `L^infinity`;
5. Bony/commutator decomposition with exact constants.

Do not create these formal layers merely because they are missing.  Per the standing stop rule,
first decide at least the LH analytic sub-gate on paper.  Formalize only a load-bearing surviving
lemma.

---

## 10. Decision / claim boundary

- `FDT-INJ`: **OPEN**.
- Static energy-only pointwise closure (5.1): **KILLED / NO**.
- The Astra S15 `(q,d)` cone remains parked; nothing in this file reopens Q-SPEC or D-SPEC.
- No numerical/runtime behavior changes.
- No Lean source changes.
- No claim of Navier–Stokes global regularity, blow-up, or Clay A/B/C/D.

The next smallest gate is:

> **FDT-LH:** at one high dyadic block and over one viscous window, can the exact
> low–high commutator contribution to (2.2) be bounded by a fixed fraction of `c_0 nu`
> using quantities whose time budget is already known independently of regularity?

Attack `FDT-LH` counterexample-first.  A bound whose coefficient is merely `F`,
`||grad u||_infinity`, or another known continuation norm is a failed reduction, not a YES.
