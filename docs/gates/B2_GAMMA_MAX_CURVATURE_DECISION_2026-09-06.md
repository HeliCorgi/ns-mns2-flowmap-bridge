# B2 Gamma-max curvature decision — 2026-09-06

**Status: ACTUAL-NS DYNAMICAL CUT.  THE MIDDLE LIMB SURVIVES ONLY WITH A NEW FLAT-TOP / MAX-DISPLACEMENT ESCAPE WHEN `beta_v >= 1/2`.**

**Primary results:**

- `B2-GAMMA-CURVATURE-BUDGET = YES`;
- `B2-GAMMA-ONESCALE(beta_v >= 1/2) = NO`;
- the arithmetic witness `W★ = (gamma,alpha,beta_v)=(3/5,9/20,1/2)` from
  `BH_BETAV_ENDPOINT_PINNING_2026-08-23.md` is **not dynamically realizable with a
  uniformly nondegenerate one-scale Gamma peak at the saturation radius**;
- the full Scope-B middle limb is **not killed**: it can still escape through curvature
  depletion / flat-top formation, separation of the Gamma maximum from the first saturation
  radius, or a more complicated multiscale geometry.

This is the first post-Stage-9 decision here that uses the actual axisymmetric Navier--Stokes
circulation PDE rather than only frozen exponent/region arithmetic.

No finite-time singular solution is constructed.  No Clay alternative is proved.

---

## 0. Frozen setting and why this gate is load-bearing

Use the repository's current breakdown-side setting:

- unforced incompressible Navier--Stokes on `R^3`, viscosity `nu>0`;
- smooth axisymmetric-with-swirl solution on every compact subinterval of a maximal lifespan
  `[0,T*)`, with a hypothetical first singular time `T*<infinity`;
- `tau=T*-t`;
- Type-II amplitude `||u(t)||_infinity ~ tau^{-gamma}`;
- on-axis B2 core scale `ell ~ tau^alpha`, `(gamma,alpha) in S_blob`;
- non-evanescent circulation `Gamma=r u_theta`, `liminf ||Gamma(t)||_infinity >= c0 Gamma0>0`;
- Scope-B middle limb `beta_v in (alpha,gamma)` for a sub-core Gamma-saturation scale
  `r_sat ~ tau^{beta_v}`.

The previous endpoint-pinning decision proved only that the frozen rows do not locate Gamma
saturation.  Its explicit witness `W★` used a synthetic circulation profile with a turnover at
`r ~ tau^{1/2}`.  That record explicitly did **not** assert that the profile is an actual
Navier--Stokes trajectory.

The present gate asks whether the real Gamma equation permits such a turnover geometry.

---

## 1. Exact circulation equation

For a smooth axisymmetric solution define

\[
 Gamma(r,z,t)=r u^\theta(r,z,t).
\]

Then on `r>0`,

\[
 \boxed{
 (\partial_t+u^r\partial_r+u^z\partial_z)\Gamma
 =\nu\left(\partial_r^2-\frac1r\partial_r+\partial_z^2\right)\Gamma .
 }
 \tag{1.1}
\]

Smooth Cartesian axisymmetry gives `Gamma(0,z,t)=0`.  For compactly supported or Schwartz
smooth data, the relevant signed spatial suprema are attained at finite radius for every smooth
time.

The key structural point is that at a nonzero signed spatial maximum of `Gamma`,

\[
 \partial_r\Gamma=\partial_z\Gamma=0.
\]

Therefore **both the meridional advection and the singular first-order radial diffusion term
vanish at the maximum**.  Pressure does not occur in (1.1).

---

## 2. Signed maxima and the exact curvature budget

For `sigma in {+1,-1}` define

\[
 M_\sigma(t)=\sup_{r\ge0,z\in\mathbb R}\sigma\Gamma(r,z,t).
 \tag{2.1}
\]

By the Gamma maximum principle, each `M_sigma` is nonincreasing.  The B2 non-evanescence
assumption

\[
 \liminf_{t\uparrow T_*}\|\Gamma(t)\|_\infty\ge m_0>0
 \tag{2.2}
\]

implies that at least one fixed sign `sigma_*` has a nonzero monotone limit

\[
 M_{\sigma_*}(T_*-)\ge m_0.
 \tag{2.3}
\]

For that sign let

\[
 \mathcal M_\sigma(t)
 =\operatorname{Argmax}_{r,z}\sigma\Gamma(r,z,t).
\]

Every point of `M_sigma(t)` has `r>0` once `M_sigma(t)>0`, because `Gamma=0` on the axis.
Define the least transverse curvature among active maximizers,

\[
 \boxed{
 \kappa_\sigma(t)
 :=\min_{x\in\mathcal M_\sigma(t)}
 \left[-(\partial_r^2+\partial_z^2)(\sigma\Gamma)(x,t)\right]\ge0.
 }
 \tag{2.4}
\]

At almost every time at which `M_sigma` is differentiable, the standard derivative-of-a-maximum
(Danskin/envelope) identity and (1.1) give

\[
 \boxed{
 -M_\sigma'(t)=\nu\,\kappa_\sigma(t).
 }
 \tag{2.5}
\]

Indeed the derivative of the maximum is the largest time derivative among active maximizers;
there `partial_r Gamma=partial_z Gamma=0`, so each active time derivative equals
`nu(partial_r^2+partial_z^2)(sigma Gamma)`, and the largest of these negative numbers is
`-nu` times the least nonnegative curvature.

Integrating (2.5) yields the exact finite budget

\[
 \boxed{
 \nu\int_{t_0}^{T_*}\kappa_{\sigma_*}(t)\,dt
 =M_{\sigma_*}(t_0)-M_{\sigma_*}(T_*-)<\infty.
 }
 \tag{2.6}
\]

This uses no exponent ansatz, no pressure estimate, no ancient limit, and no Scope-A hypothesis.

### Curvature length

Because `M_{sigma_*}(t)>=m_0` for all sufficiently late times, define

\[
 \ell_\Gamma(t)
 :=\left(\frac{M_{\sigma_*}(t)}{\kappa_{\sigma_*}(t)}\right)^{1/2},
 \qquad \ell_\Gamma=\infty\text{ if }\kappa=0.
 \tag{2.7}
\]

Then

\[
 \boxed{
 \int^{T_*}\frac{dt}{\ell_\Gamma(t)^2}<\infty.
 }
 \tag{2.8}
\]

This is the dynamical object the frozen arithmetic did not see.

### Decision

\[
 \boxed{\texttt{B2-GAMMA-CURVATURE-BUDGET = YES}.}
\]

---

## 3. One-scale Gamma peaks cannot shrink at exponent `>=1/2`

Suppose a proposed B2 realization has a signed non-evanescent Gamma maximum whose turnover remains
uniformly one-scale with a length `R(t)`:

\[
 \kappa_{\sigma_*}(t)
 \ge c\,\frac{M_{\sigma_*}(t)}{R(t)^2}
 \tag{3.1}
\]

for all sufficiently late times, with fixed `c>0`.  Equivalently
`ell_Gamma(t) <= C R(t)`.

If

\[
 R(t)\asymp\tau^\beta,
 \tag{3.2}
\]

then (2.8) requires

\[
 \int_0 \tau^{-2\beta}\,d\tau<\infty.
\]

Therefore

\[
 \boxed{\beta<\frac12.}
 \tag{3.3}
\]

At `beta=1/2` the forbidden integral is logarithmic; for `beta>1/2` it diverges by a power.

### Exact no-go

\[
 \boxed{\texttt{B2-GAMMA-ONESCALE(beta >= 1/2) = NO}.}
\]

The statement is intentionally geometric: it does **not** say that every saturation radius must
have `beta<1/2`.  It says that a non-evanescent Gamma **maximum cannot keep an order-one
self-similar curvature turnover on a scale shrinking like `tau^beta` with `beta>=1/2`.**

For `beta>=1/2`, at least one of the following must happen:

1. the Gamma peak becomes curvature-depleted / flat-topped, so
   `ell_Gamma / tau^beta -> infinity` along arbitrarily late times;
2. the non-evanescent global Gamma maximum is not located on the saturation scale being tracked;
3. the turnover is genuinely multiscale, so no uniform one-scale lower curvature bound like
   (3.1) holds.

Branch switching among spatial maximizers does not evade the theorem because `kappa_sigma` is
defined as the least curvature over the entire active maximizing set.

---

## 4. Consequence for the Stage-9 witness `W★`

The endpoint-pinning record used

\[
 (\gamma,\alpha,\beta_v)=\left(\frac35,\frac9{20},\frac12\right)
 \tag{4.1}
\]

and the synthetic circulation

\[
 \Gamma(r,t)=\Gamma_0\min\left[
   \left(\frac r{\tau^{1/2}}\right)^k,
   \frac{\tau^{1/2}}r
 \right],\qquad k>1.
 \tag{4.2}
\]

Its purpose was arithmetic consistency.  It has a turnover at

\[
 r_s\asymp\tau^{1/2}.
\]

The literal formula has a cusp.  Any smooth regularization whose turnover width remains comparable
to `r_s` has

\[
 -\Delta_{r,z}\Gamma\gtrsim \frac{\Gamma_0}{r_s^2}
 \asymp \frac{\Gamma_0}{\tau}
\]

at a signed maximum, up to fixed shape constants.  By (2.5), this would force

\[
 -M'(t)\gtrsim\frac{\nu\Gamma_0}{\tau},
\]

whose integral diverges logarithmically, contradicting non-evanescence.

Hence the correct audit statement is:

> `W★` remains a valid **frozen-row consistency certificate**, but it is **not an actual-NS
> dynamical witness** if its Gamma maximum is smoothed with a tau-uniform one-scale turnover.

To upgrade a `beta_v=1/2` realization to actual NS, one must add a new mechanism:

- asymptotic flat-top curvature depletion;
- a Gamma maximum at a parametrically different radius from `r_sat`;
- or a multiscale transition with turnover width much larger than `r_sat`.

This is a real narrowing of the B2 middle limb that was absent from the Stage-9 arithmetic pass.

---

## 5. Exponent-space consequence inside `S_blob`

For the middle limb, `beta_v>alpha`.

If a proposed middle-limb realization also satisfies the one-scale maximum hypothesis, Section 3
gives

\[
 \alpha<\beta_v<\frac12.
 \tag{5.1}
\]

Therefore necessarily

\[
 \alpha<\frac12.
\]

In the frozen blob wedge,

\[
 \alpha\ge\max(1-\gamma,2\gamma/3,2\gamma-1).
\]

For `gamma>=3/4`, this lower envelope is at least `1/2` (equal at `gamma=3/4`, larger above).
Thus:

\[
 \boxed{
 \gamma\ge\frac34
 \quad\Longrightarrow\quad
 \text{every B2 middle-limb realization must use the flat-top / displaced-max / multiscale escape.}
 }
 \tag{5.2}
\]

For `1/2<gamma<3/4`, a nondegenerate one-scale middle limb is not ruled out by this theorem, but
only in the subregion where one can choose

\[
 \alpha<\beta_v<\frac12.
\]

This is not a new frozen-map edit; it is a proposed post-freeze dynamical refinement for user
adjudication.

---

## 6. Why the result is not already K5 / K9 / K11

- **Not K5:** energy and total dissipation only constrain integrated velocity-gradient budgets.
  Equation (2.5) is a pointwise-in-space identity at active Gamma maxima and directly couples
  maximum loss to local transverse curvature.
- **Not K9:** no weighted swirl regularity criterion is invoked.  The result applies precisely in
  the Gamma-saturated branch that violates the small-swirl criteria.
- **Not K11:** K11 is a dominant-balance statement for the amplitude-growing velocity core.  The
  present theorem concerns the circulation maximum, which may live in a distinct sub-core region
  and may be amplitude-subdominant.
- **No pressure loophole:** pressure is absent from the Gamma equation.
- **No S15 fourth-jet loophole:** only the actual second derivative at a maximum enters, and its
  time integral is tied exactly to the monotone maximum loss.

---

## 7. Scope and technical caveats

The theorem is an actual-solution statement on every smooth time interval before `T*`.  To turn it
into a fully publication-style lemma one should write the standard maximum-envelope argument with
upper Dini derivatives if the maximizing set is nonunique.  The a.e. identity (2.5) is the clean
form used here; the integrated inequality needed for all consequences is stable under the Dini
formulation.

The result does **not** prove:

- `beta_v <= 1/2` for the full B2 middle limb;
- existence or nonexistence of a flat-top circulation maximum;
- global regularity of axisymmetric swirl;
- a singular solution;
- any Clay alternative.

It kills only the one-scale nondegenerate Gamma-maximum realization at and above the diffusive
exponent `1/2`.

---

## 8. Next gate: `B2-GAMMA-FLATTOP`

The new live question is no longer endpoint pinning.  It is:

> Can a non-evanescent B2 middle-limb circulation maximum satisfy the curvature depletion forced by
> Section 3 while remaining compatible with actual NS, finite energy/dissipation, the separate
> `L^3` carrier, and the frozen Type-II wedge?

The next pass should be counterexample-first and split two possibilities:

1. **flat-top branch:** quantify a neighborhood-scale version of curvature depletion and ask whether
   physical enstrophy / vorticity production gives a lower bound that contradicts the required
   flattening;
2. **max-displacement branch:** allow first fixed-fraction saturation at `r_sat` but place the true
   non-evanescent Gamma maximum at a larger radius; determine whether this creates an unavoidable
   third region or violates the K6/K9 location bookkeeping.

A useful exact variable for the flat-top branch is the signed curvature length `ell_Gamma` from
(2.7), not a new exponent guessed in advance.

Do not return to scope-free exponent arithmetic alone.  Do not treat the synthetic `W★` profile as
an actual PDE trajectory after this audit.

---

## 9. Formalization ruling

No Lean source is added in this session.

The result depends on the actual circulation PDE, spatial maximizers, and an envelope/Dini argument.
The repository's current Lean layer does not yet contain the axisymmetric pointwise Gamma maximum
principle machinery.  Formalizing only the scalar integral `beta>=1/2 => integral tau^{-2 beta}
diverges` would not move the proof frontier.

`FORMAL_SCOPE.md` and `STATUS.md` remain unchanged.
