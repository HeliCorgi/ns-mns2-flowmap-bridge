# B2 Gamma transition-residence decision — 2026-09-06

**Status: RESIDENCE-BASED KILL FAILS / FLAT-TOP-RESIDENCE SUBLANE PARKED.**

Primary decisions:

- `B2-GAMMA-RESIDENCE-DIFFUSIVE-CLOCK = YES`;
- `B2-GAMMA-LATE-ARRIVAL-BARRIER = NO` with the currently controlled quantities;
- `B2-GAMMA-TRANSITION-RESIDENCE-KILL = NO` as an unconditional reduction on the frozen B2 middle limb;
- the current `B2-GAMMA-FLATTOP / TRANSITION-RESIDENCE` sublane is **PARKED**.

The parent Scope-B B2 middle limb is **not killed**.  What fails is the proposed proof mechanism that would turn the Gamma advection--diffusion equation plus the known finite budgets into a mandatory residence time near the axis.

No singular Navier--Stokes solution is constructed.  No global regularity theorem and no Clay alternative is proved.

---

## 0. Stop/go question

The preceding curvature gate showed that a non-evanescent Gamma maximum cannot keep a uniformly nondegenerate one-scale turnover at `R(t)~tau^beta` when `beta>=1/2`.  The flat-top/enstrophy gate then showed that the mandatory axis-to-saturation transition carries large pointwise vorticity but spends only a time-integrable `L^2` enstrophy budget throughout the frozen middle limb.

The present stop/go gate asks:

> Does the actual axisymmetric Navier--Stokes transport--diffusion equation force high-`Gamma` material at `R(t)~tau^{beta_v}` to reside there long enough for diffusion to destroy non-evanescence?

If YES, the flat-top escape is genuinely cut.  If NO without importing a continuation-strength drift estimate, this sublane is to be parked rather than followed through more escape clauses.

---

## 1. Exact Gamma equation and diffusive clock

For

\[
\Gamma=r u^\theta
\]

we use

\[
(\partial_t+u^r\partial_r+u^z\partial_z)\Gamma
=\nu\left(\partial_r^2-\frac1r\partial_r+\partial_z^2\right)\Gamma.
\tag{1.1}
\]

A transition whose relevant transverse width is `R(t)` has the natural parabolic clock

\[
\boxed{
\mathfrak D(t_0,t_1)
:=\nu\int_{t_0}^{t_1}\frac{ds}{R(s)^2}.
}
\tag{1.2}
\]

If

\[
R(t)\asymp \tau^{\beta_v},\qquad \tau=T_*-t,
\]

then

\[
\mathfrak D(t_0,T_*)\asymp
\nu\int_0^{\tau_0}\tau^{-2\beta_v}\,d\tau.
\]

Hence

\[
\boxed{
\beta_v\ge\frac12
\Longrightarrow
\mathfrak D(t_0,T_*)=\infty.
}
\tag{1.3}
\]

So a packet that genuinely remains trapped on one `R(t)`-scale all the way to `T_*`, with no replenishment and with a quantitative transverse spectral/capacity gap, would experience an infinite amount of diffusive time.

This is a real positive statement:

\[
\boxed{\texttt{B2-GAMMA-RESIDENCE-DIFFUSIVE-CLOCK = YES}.}
\]

But (1.3) by itself is not a decay theorem.  To turn it into fixed-factor loss of `Gamma` one must know that the same high-`Gamma` material stays in a region whose effective transverse width is `O(R)` and is not continually replaced from outside.  Neither property follows from the frozen B2 hypotheses.

---

## 2. Why late arrival is compatible with the middle-limb amplitude budget

Suppose high-`Gamma` material is delivered over a radial distance comparable to

\[
R(t)\asymp\tau^{\beta_v}.
\]

### 2.1 Arrival over the remaining physical time `tau`

To move `O(R)` in `O(tau)` requires only

\[
|u^r|\gtrsim \frac{R}{\tau}
\asymp \tau^{\beta_v-1}.
\tag{2.1}
\]

The frozen Type-II amplitude is

\[
\|u(t)\|_\infty\asymp\tau^{-\gamma}.
\]

The middle limb has `beta_v>alpha`, while K11 gives `alpha>=1-gamma`.  Thus

\[
\beta_v>1-\gamma,
\]

and therefore

\[
1-\beta_v<\gamma.
\]

Equivalently,

\[
\boxed{
\tau^{\beta_v-1}=o(\tau^{-\gamma}).
}
\tag{2.2}
\]

So even transport across an `O(R)` radial distance during the entire remaining time is strictly below the available Type-II velocity amplitude.

### 2.2 Arrival faster than one local diffusion time

The local diffusion time is

\[
t_{\rm diff}\asymp\frac{R^2}{\nu}.
\]

To traverse `O(R)` within one such time needs

\[
|u^r|\gtrsim\frac{\nu}{R}
\asymp \nu\tau^{-\beta_v}.
\tag{2.3}
\]

Because the middle limb has

\[
\beta_v<\gamma,
\]

we have

\[
\boxed{
\nu\tau^{-\beta_v}=o(\tau^{-\gamma})
}
\tag{2.4}
\]

for fixed viscosity.  Thus the frozen amplitude budget permits meridional transport that outruns local diffusion.

This is the key no-go for a residence proof based only on `R`, `nu`, and the already-frozen amplitude exponents.

---

## 3. Known finite energy/dissipation budgets also do not prevent a localized conveyor

A scale-`R` meridional transport region with speed `U` occupies physical volume `~R^3` in the simplest axisymmetric blob bookkeeping.  Its rough energetic costs are

\[
E_{\rm conv}\sim U^2R^3,
\qquad
\mathcal E_{\rm conv}\sim \frac{U^2}{R^2}R^3=U^2R.
\tag{3.1}
\]

If it transports across `R` in a time `R/U`, the integrated enstrophy cost is

\[
\mathcal E_{\rm conv}\frac{R}{U}
\sim U R^2.
\tag{3.2}
\]

For diffusion-beating speed `U~nu/R`,

\[
E_{\rm conv}\sim \nu^2R,
\qquad
\left(\int\mathcal E_{\rm conv}dt\right)_{\rm one\ transit}
\sim \nu R.
\tag{3.3}
\]

Both vanish as `R->0`.

For transport over the remaining time, `U~R/tau`,

\[
E_{\rm conv}\sim \frac{R^5}{\tau^2}
\asymp \tau^{5\beta_v-2},
\tag{3.4}
\]

and

\[
\left(\int_{t}^{T_*}\mathcal E_{\rm conv}ds\right)
\sim \frac{R^3}{\tau}
\asymp \tau^{3\beta_v-1}.
\tag{3.5}
\]

For the branch presently at issue, `beta_v>=1/2`, both powers are positive.  Thus neither ordinary energy nor the standard finite dissipation budget forces the conveyor to stop.

These are scaling costs, not a construction of a singular trajectory.  They show that the known finite budgets have the wrong sign/power to impose a mandatory `O(R^2/nu)` residence time.

---

## 4. Exact full-NS affine-strain model: transport can neutralize local Gamma diffusion

There is an exact nonlinear axisymmetric unforced Navier--Stokes model illustrating why a drift-independent residence theorem is impossible.

Take

\[
u^r=-a(t)r,
\qquad
u^z=2a(t)z,
\qquad
u^\theta=\Omega(t)r,
\tag{4.1}
\]

with

\[
\Omega'(t)=2a(t)\Omega(t).
\tag{4.2}
\]

The velocity is affine in Cartesian coordinates.  Its Laplacian is zero, and the antisymmetric part of `M'+M^2` vanishes exactly by (4.2); the remaining affine acceleration and centrifugal term are absorbed by a quadratic pressure.  Hence (4.1)--(4.2) is an exact full Navier--Stokes solution for every smooth `a(t)`.

Its circulation is

\[
\Gamma(r,t)=\Omega(t)r^2.
\tag{4.3}
\]

The radial diffusion operator annihilates `r^2`:

\[
\left(\partial_r^2-\frac1r\partial_r\right)r^2=0.
\tag{4.4}
\]

Meanwhile radial characteristics satisfy

\[
r'=-a(t)r.
\]

Along them,

\[
\frac d{dt}\Gamma(r(t),t)=0.
\tag{4.5}
\]

Thus actual nonlinear NS transport can carry nonzero circulation inward with **zero local diffusive loss** on this mode.

Choosing

\[
a(t)=\frac{\beta}{\tau}
\]

gives

\[
r(t)\asymp\tau^\beta,
\qquad
u^r(r(t),t)\asymp-\tau^{\beta-1},
\qquad
u^\theta(r(t),t)\asymp\tau^{-\beta}.
\tag{4.6}
\]

Both are compatible with a middle-limb Type-II envelope `tau^{-gamma}` whenever

\[
1-\beta<\gamma,
\qquad
\beta<\gamma,
\]

which are exactly available from `beta>alpha>=1-gamma` and `beta<gamma`.

### Scope warning

The affine model is not finite energy, `Gamma=Omega r^2` is not globally bounded, and it has no non-evanescent finite-radius Gamma maximum.  Therefore it is **not** a Clay-admissible B2 trajectory and does not prove the middle limb exists.

Its role is narrower but decisive for the residence mechanism:

> the transport--diffusion equation itself has no drift-independent principle saying that circulation at radius `R` must decay on the clock `R^2/nu`.

One must additionally control the drift, confinement, replenishment, or material history.

---

## 5. Admissible local snapshots show the same drift freedom is not excluded by finite energy

Independently of the affine model, one can choose a real smooth compactly supported axisymmetric divergence-free datum with

- a high-`Gamma` plateau supported away from the axis;
- a compactly supported meridional streamfunction producing inward `u^r` on that plateau;
- arbitrary finite amplitude of that local inward drift.

Standard local strong theory gives an actual NS solution for a positive time from such data.  Under the exact NS scaling

\[
u^{(\lambda)}(x,t)=\lambda u(\lambda x,\lambda^2t),
\tag{5.1}
\]

circulation is invariant:

\[
\Gamma^{(\lambda)}(r,z,t)
=\Gamma(\lambda r,\lambda z,\lambda^2t).
\tag{5.2}
\]

Taking `lambda=1/R` places the same circulation geometry at radius `R`, with meridional speeds of order `R^{-1}` times the base speed and time scale `R^2` times the base time, while the physical energy scales like `R` times the base energy.

Therefore there is no trajectory-independent lower residence time at scale `R` derivable merely from finite energy, finite total dissipation, smoothness, and the local Gamma equation.  A stronger claim about repeated delivery all the way to `T_*` would require genuinely new cross-scale dynamics; it is not supplied by the present route.

---

## 6. What the diffusive clock *does* kill

The positive part should not be discarded.

Suppose one adds a quantitative hypothesis that a fixed high-`Gamma` packet

1. remains confined to a transverse width `<= C R(t)`;
2. is not replenished by material entering from larger radius;
3. has a uniform Poincare/capacity gap relative to the axis-zero boundary;
4. persists to `T_*`.

Then `mathfrak D=\infty` for `beta_v>=1/2` is precisely the correct signal for compulsory diffusive loss.

But each item above is **extra structure**.  The flat-top capacity audit already showed that pointwise maximum flatness does not supply the needed thickness/capacity gap, and the present scaling/affine audit shows that the drift can deliver fresh high-Gamma material fast enough to evade residence.

So the actual surviving escape is no longer "a flat peak just sits there".  It is a **late-arrival / conveyor / max-displacement / multiscale replenishment** mechanism.

---

## 7. Stop/go decision

The requested criterion was: if actual NS transport--diffusion does not genuinely reduce the flat-top escape without importing a new continuation-strength drift theorem, stop this branch.

That criterion is met.

### Mathematical status

\[
\boxed{\texttt{B2-GAMMA-TRANSITION-RESIDENCE-KILL = NO as an unconditional current reduction}.}
\]

This is not a theorem that no residence-based argument can ever work.  It states that the actual Gamma equation plus the presently controlled B2 quantities do not force the residence/confinement needed for the divergent diffusive clock to become a contradiction.

### Strategic status

\[
\boxed{\texttt{B2-GAMMA-FLATTOP / RESIDENCE SUBLANE = PARKED}.}
\]

Do not continue by inventing another residence exponent, another static transition norm, or another local capacity quantity.

The parent Scope-B B2 middle limb remains open through precisely the mechanisms the current route cannot control:

- late arrival / circulation conveyor;
- displacement of the true non-evanescent Gamma maximum from `r_sat`;
- genuinely multiscale replenishment.

---

## 8. Reopen conditions

Reopen this sublane only if at least one of the following appears independently:

1. a new theorem controlling meridional radial delivery to the axis from a quantity strictly weaker than known continuation criteria;
2. a material-history estimate for Gamma that prevents repeated fresh high-circulation replenishment across shrinking radii;
3. a quantitative superlevel-capacity theorem propagated by the actual NS flow, not assumed at one time;
4. an interaction with the separate `L^3` carrier or pressure/strain geometry that forces the high-Gamma packet to remain resident for a diffusive clock;
5. an external result materially changing the axisymmetric transport frontier.

Absent one of these, more residence bookkeeping has low information value.

---

## 9. Portfolio routing after park

The highest-information remaining B2 question is not another flat-top estimate.  It is the distinct location problem already carried in the handoff:

\[
\boxed{\texttt{B2-GAMMA-MAX-DISPLACEMENT}.}
\]

Ask whether first fixed-fraction saturation at `r_sat` while the true non-evanescent Gamma maximum sits parametrically farther out is compatible with the actual two-region `C+S` bookkeeping, or whether it necessarily creates an additional dynamically relevant region that collides with K6/K9 or the `L^3`-carrier geometry.

This should be treated as a separate gate, not as a continuation of the parked residence sublane.

---

## 10. Formalization ruling

No Lean source is added.  The formal frontier did not move.  The decisive content is an analytic stop/go decision involving the actual Gamma PDE, transport scaling, and an exact affine NS model.  Formalizing scalar exponent arithmetic or the affine matrix algebra alone would not advance the Clay frontier.

`FORMAL_SCOPE.md` and `STATUS.md` remain unchanged.
