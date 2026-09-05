# FDT material-frequency structural decision — 2026-09-06

**Status: STRUCTURAL SPLIT / EXACT COMMUTATION YES, UNIFORM EULERIAN BRIDGE NO.**

**Primary verdict:**

- `FDT-MAT-COMM = YES` for the canonical componentwise low-flow conjugated projector;
- `FDT-MAT-BRIDGE-UNIF = NO` without an independent deformation/strain budget;
- therefore the originally ambitious conjunction `FDT-MAT-STRUCT` is **NO as stated**.

This record follows the affine-strain no-go in
`docs/gates/FDT_LH_DYN_AFFINE_DECISION_2026-09-06.md`.

The purpose is to test whether replacing fixed Eulerian Littlewood–Paley shells by shells transported
with the low-frequency flow repairs the frequency/dissipation route. The answer is mixed. The
principal low transport can indeed be removed exactly by conjugation, and the affine shell-relabeling
defect becomes zero by construction. However the price is geometric distortion of the dyadic shells.
Without controlling the deformation gradient of the low flow, a fixed material shell can correspond
to arbitrarily high or arbitrarily low Eulerian frequencies even over one viscous window. Hence a
uniform material-tail bound does not by itself imply the fixed-Eulerian high-frequency tail needed by
the Cheskidov–Shvydkoy continuation criterion.

No global regularity theorem, blow-up theorem, or Clay alternative is proved.

---

## 0. Low flow and canonical material conjugation

Fix one high dyadic index `j`. Let

\[
 v_j(t,x):=u_{\le j-2}(t,x)
\]

be the divergence-free low field and let `X_j(t,s,y)` be its flow:

\[
 \partial_t X_j(t,s,y)=v_j(t,X_j(t,s,y)),
 \qquad X_j(s,s,y)=y.
\tag{0.1}
\]

For smooth times, incompressibility gives

\[
 \det D_yX_j(t,s,y)=1.
\tag{0.2}
\]

Define the componentwise material pullback

\[
 (\mathcal U_j(t,s)f)(y):=f(X_j(t,s,y)).
\tag{0.3}
\]

and the canonical material dyadic operator

\[
 \boxed{
 \Delta_j^{\rm mat}(t;s)
 :=\mathcal U_j(t,s)^{-1}\,\Delta_j\,\mathcal U_j(t,s).
 }
\tag{0.4}
\]

At the anchoring time `s`, this agrees with the ordinary Eulerian projector:

\[
 \Delta_j^{\rm mat}(s;s)=\Delta_j.
\tag{0.5}
\]

---

## 1. Exact transport commutation

Let

\[
 D_t^{(j)}:=\partial_t+v_j\cdot\nabla.
\]

Differentiating (0.4) gives

\[
 \partial_t\Delta_j^{\rm mat}
 +[v_j\cdot\nabla,\Delta_j^{\rm mat}]=0.
\tag{1.1}
\]

Equivalently,

\[
 \boxed{
 [D_t^{(j)},\Delta_j^{\rm mat}]=0.
 }
\tag{1.2}
\]

Thus the principal low–high transport commutator is not estimated; it vanishes by construction.
This exactly absorbs the shell relabeling exposed by the affine-strain decision.

### Decision

\[
 \boxed{\texttt{FDT-MAT-COMM = YES}.}
\]

This is an exact algebraic/geometric identity for smooth low flows.

---

## 2. Affine uniqueness and exact symbol

The obstruction appears already for the trace-free affine flow

\[
 v(x)=Sx,
 \qquad \operatorname{tr}S=0,
\tag{2.1}
\]

with flow

\[
 X(t,y)=e^{tS}y.
\tag{2.2}
\]

For a Fourier mode `e^{i xi·x}`, the pullback sends

\[
 e^{i\xi\cdot x}
 \mapsto
 e^{i(e^{tS^T}\xi)\cdot y}.
\]

Hence the material projector is a Fourier multiplier with symbol

\[
 \boxed{
 m_j^{\rm mat}(t,\xi)
 =\varphi_j(e^{tS^T}\xi).
 }
\tag{2.3}
\]

Among differentiable operator families with initial value `Delta_j` satisfying the exact commutation
equation (1.1), the conjugated family (0.4) is the canonical solution; in the affine Fourier-multiplier
class (2.3) is forced by the transport equation for the symbol.

Thus exact low-transport commutation necessarily transports the frequency shell by the inverse
transpose deformation.

---

## 3. Material shells are not uniformly Eulerian annuli

Assume the fixed LP cutoff is supported in an annulus

\[
 c_1\lambda_j\le |\eta|\le c_2\lambda_j.
\tag{3.1}
\]

From (2.3), the material shell at time `t` is

\[
 c_1\lambda_j
 \le |e^{tS^T}\xi|
 \le c_2\lambda_j.
\tag{3.2}
\]

Equivalently it is the ellipsoidal image

\[
 e^{-tS^T}\{\eta:c_1\lambda_j\le|\eta|\le c_2\lambda_j\}.
\tag{3.3}
\]

Take the exact affine strain used in the previous decision,

\[
 S_\gamma=\operatorname{diag}(-\gamma,\gamma,0).
\tag{3.4}
\]

Then

\[
 e^{-tS_\gamma^T}
 =\operatorname{diag}(e^{\gamma t},e^{-\gamma t},1).
\tag{3.5}
\]

Therefore a single material shell contains Eulerian frequencies whose sizes differ by factors of
order

\[
 e^{\gamma t}
 \quad\text{and}\quad
 e^{-\gamma t}.
\tag{3.6}
\]

There is no trajectory-independent constant `C` such that every material shell remains inside

\[
 C^{-1}\lambda_j\le |\xi|\le C\lambda_j
\tag{3.7}
\]

for all smooth divergence-free low flows.

---

## 4. The obstruction survives on one viscous window

Use the parent one-window length

\[
 \tau_j=\frac{a_*}{\nu\lambda_j^2}.
\tag{4.1}
\]

Choose

\[
 \gamma=\sigma\nu\lambda_j^2.
\tag{4.2}
\]

Then

\[
 \gamma\tau_j=\sigma a_*.
\tag{4.3}
\]

Hence the shell distortion factor is

\[
 \boxed{e^{\sigma a_*}.}
\tag{4.4}
\]

Since `sigma>0` is arbitrary, the distortion can be arbitrarily large within one viscous window.
Viscous time localization does not restore a universal comparison between material and Eulerian
indices.

---

## 5. Exact failure of the naive continuation bridge

Consider a passively transported mode in the compressive `x_1` direction. Its Eulerian frequency is

\[
 k(t)=e^{\gamma t}k_0.
\tag{5.1}
\]

But under the material projector,

\[
 e^{tS_\gamma^T}(k(t)e_1)=k_0e_1.
\tag{5.2}
\]

Thus its material dyadic index stays fixed while its physical Eulerian frequency grows by
`e^{gamma t}`.

Consequently a statement that all sufficiently high material blocks are subcritical need not imply
that all sufficiently high Eulerian blocks are subcritical with a uniform index conversion.

The Cheskidov–Shvydkoy dissipation wavenumber and the parent `FDT-INJ` first-contact theorem are
formulated in fixed Eulerian shells. To convert a material-tail estimate back to that criterion one
needs quantitative control of

\[
 \|D X_j(t,s)\|,
 \qquad
 \|D X_j(t,s)^{-1}\|.
\tag{5.3}
\]

For a general low flow these are controlled schematically by

\[
 \exp\!\left(
   \int_s^t\|\nabla v_j(\tau)\|_\infty\,d\tau
 \right).
\tag{5.4}
\]

But the previous FDT-LH operator decision already showed that ordinary energy and the one-window
`L^2` enstrophy budget do not force this strain integral to be small. Inserting (5.4) as an
assumption would reintroduce the continuation wall unless an independent budget is proved.

### Decision

\[
 \boxed{\texttt{FDT-MAT-BRIDGE-UNIF = NO}.}
\]

There is no uniform bridge from exact-commuting material shell control to the fixed Eulerian
frequency criterion without a deformation bound.

---

## 6. Divergence/Leray trilemma

The componentwise pullback (0.3) is chosen because it commutes exactly with componentwise transport
`partial_t+v·grad`. For a general volume-preserving nonlinear diffeomorphism, however, simple
componentwise composition does not preserve the divergence-free condition of a vector field. Thus
applying Leray after material conjugation creates a geometric/Leray defect.

One may instead use the contravariant Piola pullback

\[
 \widetilde w(y)=D X(y)^{-1}w(X(y)),
\tag{6.1}
\]

which preserves divergence when `det DX=1`. But its natural transport equation is Lie transport;
relative to Navier–Stokes componentwise convection it introduces the explicit deformation term

\[
 (\nabla v)w.
\tag{6.2}
\]

Therefore a material-frequency construction faces the following choice:

1. exact componentwise transport commutation, but a divergence/Leray geometric defect;
2. exact divergence preservation by Piola transport, but an explicit low-strain deformation term;
3. project back with Leray, creating a nonlocal commutator with the transported geometry.

No option removes low-frequency deformation for free.

---

## 7. Exact theorem-shaped ruling

Define the ambitious `FDT-MAT-STRUCT` conjunction as requiring all of the following with constants
independent of the actual smooth trajectory:

1. a material projector initially equal to `Delta_j`;
2. exact commutation with the principal low transport;
3. exact absorption of affine shell relabeling;
4. uniform comparison of material shell index with fixed Eulerian dyadic frequency on one viscous
   window;
5. a resulting material high-frequency tail criterion that implies the known Eulerian continuation
   criterion without assuming `int F`, `int ||grad u||_infinity`, Serrin, bounded `H^3`, or an
   equivalent regularity wall.

Then

\[
 \boxed{\texttt{FDT-MAT-STRUCT = NO as stated}.}
\tag{7.1}
\]

Items 1–3 force transported/deformed frequency shells, while the affine trace-free strain makes item
4 fail by an arbitrarily large factor over one viscous window. Without item 4, item 5 cannot be
obtained from the fixed-Eulerian Cheskidov–Shvydkoy criterion by a uniform shell comparison.

The positive exact sub-result remains

\[
 \boxed{\texttt{FDT-MAT-COMM = YES}.}
\tag{7.2}
\]

---

## 8. What is and is not killed

### Killed

- the naive plan “move to material LP shells, absorb LH transport, then reuse the same fixed Eulerian
  continuation argument with universal constants”;
- any claim that one viscous window automatically keeps the material shell comparable to the
  Eulerian shell;
- any exact-commuting material-shell proof which ignores the deformation gradient;
- any repair which simply assumes a small `int ||grad u_low||_infinity` without proving a new
  independent budget.

### Not killed

- parent `FDT-INJ` for one fixed real divergence-free Schwartz datum remains OPEN;
- a new continuation theorem formulated directly in a deformation-aware metric;
- a material observable coupled to a separately controlled deformation functional;
- cancellations among Leray, diffusion, HL, HH, and geometric defects;
- an admissible localization theorem approximating the affine shell-distortion obstruction by
  finite-energy Schwartz data over one window.

The affine countermodel is non-`L^2`, so this is not a Clay-admissible counterexample and does not
refute `FDT-INJ`.

---

## 9. Strategic ruling

The frequency route has now exposed two independent facts:

1. fixed Eulerian LH injection overcounts benign shell transport;
2. exact material shells remove that overcounting but lose uniform control of physical Eulerian
   frequency unless the low-flow deformation is controlled.

The highest-information next gate is:

### `FDT-DEF-BUDGET`
Ask whether the actual NS low-frequency flow has an independently finite/subcritical deformation
budget over viscous windows strong enough to compare material and Eulerian shells, without reducing
to `int F`, `int ||grad u||_infinity`, Serrin, or bounded `H^3`.

Attack counterexample-first. If NO, park the material-frequency regularity route.

An alternative is `FDT-MAT-CONT`: abandon the fixed Eulerian criterion and seek a genuinely new
continuation theorem directly in a deformation-aware material metric. Such a theorem must recover
classical regularity and cannot hide deformation control in the norm definition.

---

## 10. Formalization ruling

No Lean file is added. Formalizing flow-conjugated LP projectors before a surviving analytic
continuation bridge exists would be plumbing without proof-frontier value. No LP/Bony/Piola/
paracomposition Lean layer should be built until a load-bearing analytic gate survives.

`FORMAL_SCOPE.md` and `STATUS.md` remain unchanged.
