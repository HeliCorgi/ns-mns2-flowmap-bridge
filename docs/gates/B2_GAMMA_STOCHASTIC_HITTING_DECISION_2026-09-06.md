# B2 Gamma stochastic-hitting / strain decision — 2026-09-06

**Status: ACTUAL-NS HITTING/STRAIN NECESSITY = YES; ELLIPTIC/ENERGY KILL = NO; GAMMA-SATURATION MICROGEOMETRY SUBPROGRAM PARKED.**

**Primary decisions:**

- `B2-GAMMA-HITTING-STRAIN = YES`;
- `B2-GAMMA-HITTING-NEW-EXPONENT-CUT = NO`;
- `B2-GAMMA-STRAIN-ELLIPTIC-KILL = NO`;
- `B2-GAMMA-SATURATION-MICROGEOMETRY = PARKED` as a project route, while the parent Scope-B B2 middle limb remains **OPEN**.

This record is the deliberately orthogonal pass commissioned after the flat-top/residence sublane was parked.  The idea is to exploit the fact that the radial diffusion in the exact circulation equation is a zero-dimensional squared-Bessel operator after the change of variable `y=r^2`, then ask whether maintaining a fixed fraction of the circulation near the axis forces enough inward meridional strain to contradict the actual Navier--Stokes coupling.

The first half succeeds: there is a clean actual-PDE barrier forcing a scale-critical inward-strain history.  The second half fails: that strain is fully compatible with the Type-II middle-limb amplitude and with finite energy/dissipation, and the elliptic relation between strain and azimuthal vorticity has a harmonic-strain loophole.  Continuing to chase co-location or another saturation-location escape would therefore recreate the same loop in a different language.

No singular Navier--Stokes solution is constructed.  No global regularity theorem, blow-up theorem, or Clay alternative is proved.

---

## 0. Setting

Let

\[
\Gamma(r,z,t)=r u^\theta(r,z,t)
\]

for a smooth axisymmetric-with-swirl unforced Navier--Stokes solution on `R^3` for `t<T_*`.  The exact pressure-free equation is

\[
(\partial_t+u^r\partial_r+u^z\partial_z)\Gamma
=\nu\left(\partial_r^2-\frac1r\partial_r+\partial_z^2\right)\Gamma,
\qquad \Gamma(0,z,t)=0.
\tag{0.1}
\]

Write

\[
S:=-\frac{u^r}{r}=\partial_z\psi_1.
\tag{0.2}
\]

Positive `S` is inward radial strain.

For the B2 middle limb, the first fixed-fraction saturation radius obeys

\[
R(t)=r_{\rm sat}(t;c')\asymp \tau^{\beta_v},
\qquad \tau=T_*-t,
\qquad \alpha<\beta_v<\gamma<1.
\tag{0.3}
\]

The previous gates established that a one-scale nondegenerate Gamma maximum at exponent `beta_v>=1/2` is impossible, that the flat-top transition enstrophy is still integrable, and that fixed-packet residence is not forced because late arrival/conveyor motion is allowed by the frozen budgets.

---

## 1. Exact Bessel reduction

Set

\[
y=r^2,
\qquad G(y,z,t):=\Gamma(\sqrt y,z,t).
\]

Then

\[
\Gamma_r=2rG_y,
\qquad
\Gamma_{rr}=2G_y+4yG_{yy},
\]

so the singular radial diffusion simplifies exactly:

\[
\boxed{
\Gamma_{rr}-\frac1r\Gamma_r=4yG_{yy}.
}
\tag{1.1}
\]

Also

\[
2r u^r G_y=-2S y G_y.
\]

Hence (0.1) becomes

\[
\boxed{
G_t-2S yG_y+u^zG_z
=4\nu yG_{yy}+\nu G_{zz}.
}
\tag{1.2}
\]

Equivalently,

\[
G_t
=4\nu yG_{yy}+\nu G_{zz}+2S yG_y-u^zG_z.
\tag{1.3}
\]

The radial diffusion generator `4 nu y d_yy` is a time-scaled **BESQ(0)** generator.  The hard edge `y=0` is absorbing for the scalar because `Gamma=0` on the physical axis.

This is the stochastic/hitting interpretation of the axis boundary.  We will use its deterministic barrier equivalent below, avoiding any time-reversal convention for stochastic flows.

---

## 2. Frozen inward strain: exact hitting probability

Freeze a constant inward strain `A>=0` and suppress the axial direction.  The radial generator is

\[
\mathcal L_A
=4\nu y\partial_y^2+2Ay\partial_y.
\tag{2.1}
\]

Let `p_A(y;L)` be the probability, for the corresponding one-dimensional diffusion, of reaching `L^2` before the absorbing edge `0`.  It solves

\[
\mathcal L_Ap_A=0,
\qquad p_A(0;L)=0,
\qquad p_A(L^2;L)=1.
\]

For `A>0`, direct integration gives

\[
\boxed{
 p_A(y;L)
 =\frac{1-e^{-Ay/(2\nu)}}{1-e^{-AL^2/(2\nu)}}.
}
\tag{2.2}
\]

The `A=0` limit is

\[
\boxed{p_0(y;L)=\frac{y}{L^2}.}
\tag{2.3}
\]

Thus pure Bessel diffusion suppresses fixed-fraction circulation quadratically near the axis.  Inward strain changes the harmonic measure by the dimensionless quantity

\[
\boxed{\mathrm{Pe}_S:=\frac{A R^2}{\nu}.}
\tag{2.4}
\]

For an outer reservoir parametrically farther than `R`, a fixed hitting fraction requires `Pe_S=O(1)` from below.

---

## 3. Actual-PDE running-sup barrier

The frozen calculation can be promoted to an actual Navier--Stokes comparison statement.

Fix a small but time-independent `L>0`.  Let

\[
M_0:=\|\Gamma(0)\|_\infty>0,
\qquad
C_L:=\sup_{0<r\le L,\,z\in\mathbb R}
\frac{|\Gamma(r,z,0)|}{r^2}<\infty.
\tag{3.1}
\]

The finiteness of `C_L` is the Cartesian smoothness condition `Gamma=O(r^2)` at the axis.

Choose the datum-dependent baseline

\[
A_0:=\frac{2\nu C_L}{M_0}.
\tag{3.2}
\]

For a fixed observation time `t<T_*`, define the running inward-strain ceiling

\[
A(t):=\max\left\{A_0,
\sup_{0\le s\le t}\sup_{0<r\le L,z\in\mathbb R}S(s,r,z)
\right\}.
\tag{3.3}
\]

Set

\[
a:=\frac{A(t)}{2\nu},
\qquad
P_A(r):=
\frac{1-e^{-a r^2}}{1-e^{-aL^2}}.
\tag{3.4}
\]

For either sign `sigma in {+1,-1}`, define the radial barrier

\[
\Phi(r):=2M_0P_A(r).
\tag{3.5}
\]

### 3.1 Initial and boundary domination

At `r=L`, `Phi=2M_0`, while the Gamma maximum principle gives `|Gamma|<=M_0`.  At `r=0`, both `Gamma` and `Phi` vanish.  At spatial infinity in `z`, the smooth decaying solution tends to zero.

At time zero, if `ar^2<=1`, then

\[
1-e^{-ar^2}\ge \frac12 ar^2,
\]

so

\[
\Phi(r)
\ge M_0 a r^2
\ge C_Lr^2
\ge |\Gamma(r,z,0)|.
\]

If `ar^2>=1`, then

\[
\Phi(r)\ge2M_0(1-e^{-1})>M_0\ge|\Gamma(r,z,0)|.
\]

Thus the barrier dominates the signed initial data and the lateral boundary data.

### 3.2 Supersolution property

In the `y=r^2` variable, the operator corresponding to (1.2) is

\[
\mathscr P
=\partial_t-4\nu y\partial_y^2-\nu\partial_z^2-2Sy\partial_y+u^z\partial_z.
\]

The radial profile `P_A` solves

\[
4\nu P_A''+2A(t)P_A'=0.
\]

Therefore

\[
\mathscr P\Phi
=2(A(t)-S)y\Phi_y\ge0
\tag{3.6}
\]

throughout the comparison cylinder.  The parabolic maximum principle, applied first away from the axis and then letting the inner radius tend to zero, gives

\[
\boxed{
\sigma\Gamma(r,z,t)
\le
2M_0\frac{1-e^{-A(t)r^2/(2\nu)}}
{1-e^{-A(t)L^2/(2\nu)}}
\qquad(0\le r\le L).
}
\tag{3.7}
\]

This is the load-bearing actual-PDE form of the stochastic hitting barrier.

---

## 4. Fixed-fraction saturation forces scale-critical inward strain

Suppose at time `t` there is a point with `0<rho<=R<L` such that

\[
|\Gamma(\rho,z,t)|\ge cM_0,
\qquad c\in(0,1).
\tag{4.1}
\]

Since the barrier is increasing in `r`, (3.7) implies

\[
\frac{1-e^{-aR^2}}{1-e^{-aL^2}}\ge\frac c2,
\qquad a=\frac{A(t)}{2\nu}.
\tag{4.2}
\]

Write

\[
q:=\frac{L^2}{R^2}.
\]

Assume `q>4/c`, which holds automatically for all sufficiently small middle-limb saturation scales.  Put `x=aR^2`.

If `qx<=1`, then

\[
1-e^{-x}\le x,
\qquad
1-e^{-qx}\ge\frac12 qx,
\]

so the quotient in (4.2) is at most `2/q<c/2`, contradiction.  Hence `qx>1`.  Then

\[
1-e^{-qx}\ge1-e^{-1},
\qquad
1-e^{-x}\le x,
\]

and (4.2) yields

\[
x\ge\frac c2(1-e^{-1}).
\]

Therefore

\[
\boxed{
A(t)R^2
\ge
c(1-e^{-1})\nu.
}
\tag{4.3}
\]

Since the baseline `A_0` is fixed, for sufficiently small `R` the running supremum term in (3.3) must carry this bound.  Thus any fixed-fraction circulation saturation approaching the axis forces

\[
\boxed{
\sup_{0\le s\le t}\sup_{0<r\le L,z}S^+(s,r,z)
\gtrsim_c\frac{\nu}{R(t)^2}.
}
\tag{4.4}
\]

For a power-law middle limb `R(t)~tau^{beta_v}`, there is consequently a sequence `s_n->T_*` with

\[
\boxed{
(T_*-s_n)^{2\beta_v}
\|S^+(s_n)\|_\infty
\gtrsim_c\nu.
}
\tag{4.5}
\]

This sequence statement follows because the running supremum in (4.4) cannot be attained forever on a compact subinterval of the smooth lifespan.

### Decision

\[
\boxed{\texttt{B2-GAMMA-HITTING-STRAIN = YES}.}
\]

This is a genuine actual-NS dynamical restriction, not exponent bookkeeping.

---

## 5. Why the strain requirement does not cut the frozen middle limb

The dimensionless condition from (4.3) is exactly scale-critical:

\[
S R^2/\nu\gtrsim1.
\tag{5.1}
\]

If it is realized locally at radius `r~R`, then

\[
|u^r|=rS\gtrsim\frac\nu R.
\tag{5.2}
\]

But the middle limb has `R~tau^{beta_v}` and `beta_v<gamma`, hence

\[
\frac\nu R\sim\nu\tau^{-\beta_v}
=o(\tau^{-\gamma}).
\tag{5.3}
\]

So the required diffusion-beating radial speed lies strictly **below** the allowed Type-II velocity envelope.

The same conclusion appeared heuristically in the residence gate; the hitting calculation now makes the scale-critical strain requirement exact.

Therefore

\[
\boxed{\texttt{B2-GAMMA-HITTING-NEW-EXPONENT-CUT = NO}.}
\]

---

## 6. The hoped-for elliptic coupling has a harmonic-strain loophole

The proposed second step was to combine the forced strain with

\[
S=\partial_z\psi_1,
\qquad
-\mathcal L_5\psi_1=\omega_1,
\qquad
\mathcal L_5=\partial_r^2+\frac3r\partial_r+\partial_z^2.
\tag{6.1}
\]

A pointwise lower bound on `S` does **not** force a comparable local lower bound on `omega_1`.
The exact obstruction is already visible in the affine harmonic mode

\[
\boxed{\psi_1(r,z)=Az.}
\tag{6.2}
\]

Then

\[
S=A,
\qquad
\mathcal L_5\psi_1=0,
\qquad
\omega_1=0,
\tag{6.3}
\]

while the reconstructed meridional velocity is

\[
 u^r=-Ar,
\qquad
 u^z=2Az.
\tag{6.4}
\]

This is exactly the local strain geometry underlying the affine exact-NS conveyor model from the residence gate.

The affine field is not finite energy, but the loophole is not removed by localization.  Let `chi` be a smooth axis-compatible cutoff equal to one on a unit meridional ball and supported on a slightly larger ball, and set at scale `R`

\[
\psi_{1,R}(r,z)=A R\,\big(z/R\big)\,\chi(r/R,z/R).
\tag{6.5}
\]

In the inner region, `S=A` and `omega_1=0` exactly; all elliptic source is moved into the cutoff shell.  Choosing

\[
A\asymp\nu/R^2
\tag{6.6}
\]

gives the hitting-scale strain while the characteristic poloidal speed is only

\[
U_{\rm pol}\asymp AR\asymp\nu/R.
\tag{6.7}
\]

The associated physical scaling costs are

\[
E_{\rm pol}\asymp A^2R^5\asymp\nu^2R,
\tag{6.8}
\]

\[
\|\nabla u_{\rm pol}\|_2^2\asymp A^2R^3\asymp\frac{\nu^2}{R}.
\tag{6.9}
\]

Over one local viscous time `R^2/nu`, the dissipation cost is therefore

\[
\nu\,(R^2/\nu)\,\|\nabla u_{\rm pol}\|_2^2
\asymp\nu^2R,
\tag{6.10}
\]

which tends to zero as `R->0`.

Thus neither the elliptic equation nor the standard finite energy/dissipation budget makes the forced strain perturbatively impossible.

### Decision

\[
\boxed{\texttt{B2-GAMMA-STRAIN-ELLIPTIC-KILL = NO}.}
\]

The failure is structural: `S` contains a local harmonic-strain component which need not be paid for by local `omega_1`.

---

## 7. Navier--Stokes scaling confirms the no-go

The same obstruction is visible directly from the exact Navier--Stokes scaling

\[
u^{(\lambda)}(x,t)=\lambda u(\lambda x,\lambda^2t).
\tag{7.1}
\]

For axisymmetric fields,

\[
\Gamma^{(\lambda)}(r,z,t)
=\Gamma(\lambda r,\lambda z,\lambda^2t),
\tag{7.2}
\]

so circulation amplitude is scale invariant, while

\[
S^{(\lambda)}=\lambda^2 S,
\qquad
R^{(\lambda)}=\lambda^{-1}R.
\tag{7.3}
\]

Hence

\[
\boxed{S^{(\lambda)}(R^{(\lambda)})^2=S R^2.}
\tag{7.4}
\]

The hitting/strain condition is exactly critical.

By contrast,

\[
\|u^{(\lambda)}(0)\|_2^2
=\lambda^{-1}\|u(0)\|_2^2.
\tag{7.5}
\]

A smooth compactly supported axisymmetric datum containing an inward-strain cell plus a bounded-Gamma swirl cell can therefore be rescaled to arbitrarily small `R`, preserving the dimensionless hitting geometry while making the energy and one-scaled-window dissipation cost tend to zero.  Its standard local smooth Navier--Stokes solution rescales with the same `R^2` time window.

This does **not** construct one fixed datum cascading through infinitely many scales.  It does prove that no local-in-scale energy argument can contradict the stochastic-hitting strain requirement.

---

## 8. Relation to known near-axis parabolic theory

External context, not used as a proof input: quantitative axisymmetric regularity work applies Harnack/De Giorgi methods to the autonomous swirl `Theta=r u_theta` equation near the axis and obtains Hölder control when a suitable critical drift norm is bounded.  This is consistent with the present barrier: fixed-fraction saturation at smaller and smaller radii can persist only if the relevant drift/strain control deteriorates.

The present result is narrower and elementary: it isolates one explicit inward-strain quantity through the exact Bessel structure and does not assume a global weak-`L^3` bound.

---

## 9. Strategic ruling

The stochastic idea produced one real theorem-shaped necessity but did **not** produce a new exclusion.

The surviving middle-limb picture now requires, in addition to the previously forced off-maximum vorticity layer,

\[
\boxed{
\text{scale-critical inward strain history }
S^+\gtrsim\nu/r_{\rm sat}^2
\text{ along arbitrarily late scales.}
}
\tag{9.1}
\]

However:

- the required radial speed `nu/R` is below the Type-II amplitude because `beta_v<gamma`;
- the strain condition is NS-scale-critical while energy is supercritical;
- a harmonic strain can have `omega_1=0` locally;
- compact localization moves the elliptic cost away and remains cheap in energy/dissipation;
- forcing co-location of strain, transition vorticity, and the `L^3` carrier is a **new structural hypothesis**, not a consequence of the present B2 assumptions.

Therefore continuing with `Gamma` saturation microgeometry by asking successively for co-location, max-displacement, another packet thickness, or another residence variable would reproduce the escape-clause loop that the previous stop/go rule was designed to prevent.

### Project decision

\[
\boxed{\texttt{B2-GAMMA-SATURATION-MICROGEOMETRY = PARKED}.}
\]

This parks the present proof mechanism, **not** the parent B2 middle limb and not the entire breakdown program.

Reopen only if one obtains at least one of:

1. a propagated theorem forcing co-location of inward strain with the mandatory `Gamma` transition vorticity;
2. a scale-to-scale material-history theorem for one fixed finite-energy solution, not a family of rescaled data;
3. a global elliptic/topological constraint excluding localized harmonic strain in the relevant B2 geometry;
4. a new external result supplying a critical drift bound genuinely weaker than a known continuation criterion.

Absent one of these, do not continue to `B2-GAMMA-MAX-DISPLACEMENT` merely as another location bookkeeping pass.

---

## 10. What to attack next

The next breakdown-side task should be **orthogonal to Gamma saturation location**.  Return to the post-K11 / ancient-limit / steady-Euler side of the Type-II funnel, or another actual-NS quantity with a signed or globally propagated budget.  The next selection should explicitly avoid introducing another local scale, packet location, or saturation exponent.

A good selection criterion is:

> choose a quantity whose obstruction is invariant under moving the bad set, so that remote relocation cannot reopen the same escape.

Pressure/strain identities are acceptable only if they survive the already-known remote-pressure and harmonic-strain counterfamilies.

---

## 11. Formalization ruling

No Lean source is added.

The new analytic statement uses the pointwise circulation equation, an axis barrier, and a parabolic comparison argument.  The current formal stack does not contain the required axisymmetric pointwise maximum/comparison machinery, and the route is strategically parked after the no-go half.  Formalizing only the scalar ODE for `p_A` would not move the Clay frontier.

`FORMAL_SCOPE.md` and `STATUS.md` remain unchanged.
