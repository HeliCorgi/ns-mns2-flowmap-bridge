# B2 modulation-compactness / shape-stationarity decision — 2026-09-06

**Classification:** `NO-GO / PARK DECISION` on the breakdown side. This record does **not** prove blow-up, global regularity, or any Clay A/B/C/D alternative.

## 0. Question and final decision

Session 44 found a conditional first-order obstruction for a **shape-stationary** steady-Euler core. The load-bearing question was whether one fixed hypothetical B2 Navier--Stokes solution in the K11 interior

`gamma > alpha`, `gamma + alpha > 1`

must actually become strongly compact and asymptotically shape-stationary in the natural core frame.

The answer from the currently controlled B2 quantities is **NO** for two independent reasons:

1. the exact dynamically normalized equation leaves the intrinsic convective-time derivative at order one; the small parameter controls only the drift of the amplitude/length parameters, not the internal shape dynamics;
2. the energy/dissipation budgets do not provide a uniform spatial translation modulus, so the vanishing-viscosity sequence can retain sub-core oscillations and a Reynolds defect.

Accordingly:

- **`B2-MODULATION-SLOW-PARAMETERS = YES`;**
- **`B2-MODULATION-SHAPE-STATIONARITY = NO` from current B2 hypotheses;**
- **`B2-MODULATION-STRONG-COMPACTNESS = NO` from current B2 budgets;**
- **`B2-MODULATION-COMPACTNESS = NO` as the proposed unconditional reduction;**
- the session-44 adjoint condition remains a correct **conditional fixed-shape test**, but it cannot currently be promoted to a B2 exponent cut;
- **the ancient/steady-Euler fixed-profile lane is PARKED.**

The parent B2 middle limb remains OPEN.

## 1. Exact dynamic normalization: the missing coefficient is not small

Let

`tau = T_* - t`,

`U(t) = tau^(-gamma)`, `ell(t) = tau^alpha`,

and let `x_c(t)` be an axis-preserving center. Define the convective time by

`ds/dt = U/ell`

and write

`u(x,t) = U(t) v(y,s)`,

`y = (x-x_c(t))/ell(t)`,

`p(x,t) = U(t)^2 q(y,s)`.

A direct differentiation gives the exact normalized equation

`partial_s v + (v.grad)v + grad q - c(s).grad v + delta D_{gamma,alpha} v = eps Delta v`,

`div v = 0`,

where

`c(s) = x_c'(t)/U(t)`,

`D_{gamma,alpha} v = gamma v + alpha (y.grad)v`,

`delta = ell/(U tau) = tau^(alpha+gamma-1)`,

`eps = nu/(U ell) = nu tau^(gamma-alpha)`.

In the K11 interior,

`delta -> 0`, `eps -> 0`.

The translation term can be removed by a suitable moving/Galilean core frame when that frame is available. The decisive point is independent of that choice:

**the coefficient of `partial_s v` is exactly `1`.**

Therefore the limiting leading equation is, at best,

`partial_s v + (v.grad)v + grad q = 0`,

not the steady Euler equation.

The inequality `alpha+gamma>1` says that the externally fitted collapse parameters `U` and `ell` vary slowly compared with the core convective clock. It does **not** say that the normalized field itself varies slowly on that clock.

Thus:

**`B2-MODULATION-SLOW-PARAMETERS = YES`.**

But no present B2 hypothesis implies

`partial_s v -> 0`

or even an averaged version strong enough to identify a stationary profile. Hence:

**`B2-MODULATION-SHAPE-STATIONARITY = NO` from the current hypotheses.**

This is the first obstruction and it is logically prior to the session-44 adjoint calculation.

## 2. Correction to the old "quasi-static Euler core" reading

The old dominant-balance record used amplitude growth to obtain the lower-scale statement

`|partial_t u| >=~ U/tau`

at an amplitude-achieving core point, but then printed `U/tau` as though it were a universal asymptotic size for the full time derivative.

That replacement is not justified for a general B2 solution. Internal core dynamics may have

`|partial_t u| ~ U^2/ell`,

while the scalar envelope `U(t)` and the fitted length `ell(t)` drift only on the slower collapse time `tau`.

The K11 cut `gamma+alpha>=1` is unaffected: if the amplitude itself changes at rate `U/tau`, some NS term must still respond, and the independent energy-flux derivation remains in force. What is withdrawn is only the **unconditional classification**

`gamma+alpha>1  =>  fixed / quasi-static steady-Euler shape`.

The correct general statement is:

> the K11 interior is high-Reynolds and asymptotically inviscid on the core scale; in convective coordinates its possible leading dynamics is **unsteady Euler**. A steady-Euler profile is a further shape-locking specialization.

An explicit erratum is appended to `DOMINANT_BALANCE_INVERSION_2026-08-19.md`; the frozen exponent cut itself is not changed.

## 3. What strong compactness would require

Take the session-44 snapshot normalization

`v_n(y,s)=U_n^(-1) u(x_n+ell_n y,t_n+theta_n s)`,

`theta_n=ell_n/U_n`,

with

`eps_n=nu/(U_n ell_n)->0`.

A local `L^infinity` envelope gives weak-* compactness, but identifying

`v_n tensor v_n -> v tensor v`

requires strong compactness, for example a Kolmogorov--Riesz spatial translation modulus on each compact spacetime cylinder.

The physical dissipation does not supply such a modulus. On a normalized cylinder `Q=B_R x [-S,S]`,

`int_Q |grad_y v_n|^2 dy ds`

scales as

`(1/(U_n ell_n^2)) int_{I_n} int_{B_{R ell_n}(x_n)} |grad_x u|^2 dx dt`.

The prefactor is

`1/(U_n ell_n^2) ~ tau_n^(gamma-2alpha)`.

Inside the frozen blob wedge one has `alpha >= 2gamma/3`, hence

`gamma-2alpha <= -gamma/3 < 0`,

so this prefactor diverges. The global finite-dissipation statement says only that the physical dissipation in a shrinking terminal interval tends to zero; it gives no rate capable of cancelling this diverging renormalization.

Equivalently, the normalized energy estimate naturally controls only an **`eps_n`-weighted** derivative quantity. Since `eps_n->0`, it does not give an unweighted positive spatial regularity bound.

Therefore the existing B2 energy/dissipation ledger does not yield a uniform `H^sigma_loc`, Besov increment, or translation estimate for any positive `sigma`.

Decision:

**`B2-MODULATION-STRONG-COMPACTNESS = NO` from the current B2 budgets.**

This is an insufficiency statement about the present reduction, not a theorem that no one-fixed-solution compactness result can ever exist.

## 4. The sub-core inertial window is parametrically large

The same obstruction can be seen directly from the normalized viscosity.

Over one `O(1)` convective-time interval, the normalized viscous length is

`sqrt(eps_n)`.

Because `eps_n->0`, there is a growing band of sub-core frequencies

`1 << k_n << eps_n^(-1/2)`

for which

`eps_n k_n^2 -> 0`.

Oscillations in this band are invisible to viscosity at leading order on one convective window. Thus the current high-Re scaling itself leaves room for oscillations on scales

`ell_n sqrt(eps_n) << r_n << ell_n`.

A simple exact-NS mechanism test makes this explicit. On the periodic box, for any `eps_n>0`,

`w_n(y,s)=exp(-eps_n k_n^2 s) sin(k_n y_2) e_1`

solves the full unforced Navier--Stokes equation with viscosity `eps_n`: the convection term vanishes identically. If `k_n->infinity` and `eps_n k_n^2->0`, then on every fixed compact time interval the sequence is uniformly bounded, while

`w_n weak-* -> 0`

and

`w_n tensor w_n weak-* -> (1/2) e_1 tensor e_1`

(up to the harmless time factor tending to one).

This periodic shear family is **not** an `R^3` axisymmetric B2 witness and is not used as a Clay counterexample. Its role is only to show that the normalized PDE, bounded amplitude, and vanishing viscosity do not by themselves remove quadratic oscillation defects. The session-44 axisymmetric high-frequency snapshot counterprofile separately shows that axisymmetry plus boundedness does not provide the missing compactness either.

Consequently any successful one-fixed-solution theorem would have to use genuinely propagated cross-scale information not present in the current ledger.

This conclusion is also consistent with the classical DiPerna--Majda high-Reynolds compactness picture: energy-level vanishing-viscosity sequences naturally lead to measure-valued / oscillation-defect Euler objects unless an additional compactness mechanism is supplied.

## 5. Energy pairing does not create a hidden modulation budget

For a globally `L^2` normalized profile, pairing the exact dynamic equation with `v` gives

`(1/2) d/ds ||v||_2^2`

`+ delta (gamma-3alpha/2) ||v||_2^2`

`+ eps ||grad v||_2^2 = 0`

after the transport, pressure, and translation terms cancel.

But

`||v||_2^2 = U(t)^(-2) ell(t)^(-3) ||u(t)||_2^2`.

Thus this identity is exactly the physical Navier--Stokes energy equality rewritten in the moving scale. Its exponent content is the existing K5 threshold `alpha>=2gamma/3`; it does not force `partial_s v` to be small and it does not kill the Reynolds defect.

So there is no unexploited free scalar modulation budget hiding in the basic energy identity.

## 6. Consequence for the session-44 adjoint obstruction

The calculation

`<V,L_V w>=0`,

`<V,D_{gamma,alpha}V>=(gamma-3alpha/2)||V||_2^2`,

`<V,-Delta V>=||grad V||_2^2`

remains correct for a nonzero compact **steady** Euler profile `V` and a bounded first-order fixed-shape expansion.

What fails is the unconditional bridge into that setting.

A generic convective-scale limit can be

- Euler--Reynolds rather than Euler;
- nonzero only after a further local-mass theorem;
- unsteady Euler even if the Reynolds defect vanishes;
- modulated through unresolved sub-core scales.

In any of those cases the fixed-profile linearized equation used by the adjoint test is not the leading equation.

Therefore:

**`B2-STEADY-EULER-MODULATION-ADJOINT` remains a conditional specialization test only.**

It may be reused if a future theorem independently proves shape locking, but it is not an active unconditional B2 cut.

## 7. Decision table

| Decision object | Verdict | Meaning |
|---|---|---|
| `B2-MODULATION-SLOW-PARAMETERS` | **YES** | `delta=tau^(alpha+gamma-1)->0`; fitted scale/amplitude drift is slow on the convective clock |
| `B2-MODULATION-SHAPE-STATIONARITY` | **NO from current hypotheses** | the exact normalized equation keeps `partial_s v` at order one |
| `B2-MODULATION-STRONG-COMPACTNESS` | **NO from current budgets** | dissipation has the wrong renormalized prefactor and allows a Reynolds defect |
| `B2-MODULATION-COMPACTNESS` | **NO as current unconditional reduction** | neither defect-free compactness nor shape locking is available |
| `B2-STEADY-EULER-MODULATION-ADJOINT` | **YES, conditional only** | valid once a nonzero steady fixed-profile first-order expansion is independently justified |

## 8. Strategic ruling

The chain

`B2 interior -> strong steady-Euler profile -> first-order adjoint obstruction`

is **PARKED**.

The stop is not because the adjoint algebra failed. It is because the two hypotheses needed to activate it are exactly the missing mathematics:

1. removal of the Euler--Reynolds / sub-core oscillation defect;
2. suppression of order-one intrinsic Euler dynamics on the convective clock.

Introducing an unproved positive-regularity norm, BKM/Serrin control, bounded `H^3`, or an equivalent one-scale profile assumption would merely rename those missing steps and is forbidden by the session-44 stop rule.

Reopen this lane only if one of the following appears independently:

- a one-fixed-NS-solution cross-scale compactness theorem that kills the Reynolds defect without continuation-strength hypotheses;
- a propagated shape-locking / asymptotic-stationarity theorem on the convective clock;
- an obstruction formulated directly for unsteady Euler--Reynolds limits, so strong steady-profile compactness is no longer required.

## 9. What is still genuinely established

Parking this lane does not erase the useful location-independent results from session 44:

- the normalized viscosity tends to zero;
- the convective time window becomes eternal in both directions;
- local boundedness reaches an Euler--Reynolds compactness endpoint;
- broad static steady-Euler Liouville/exponent kills are unavailable because compact axisymmetric swirl steady Euler templates exist;
- the fixed-shape adjoint identity is a valid conditional filter.

The parent B2 middle limb remains **OPEN**. No actual singular trajectory has been constructed or excluded.

## 10. Next research selection

Do not continue by inventing another compactness norm for the same profile route. The next breakdown-side gate should consume an **exact global or signed quantity of the original NS solution before taking a singular limit**, so that relocation and Reynolds-defect escapes are not available.

A candidate selection pass should prioritize quantities with all three properties:

1. an exact propagated identity/inequality for the actual `R^3` axisymmetric NS solution;
2. a sign or monotonicity not destroyed by pressure/nonlocal transport;
3. a scaling interaction with the surviving B2 wedge that is not already K5 energy/dissipation or the parked Gamma-saturation microgeometry.

Until such a quantity is identified, do not reopen the fixed-profile ancient-Euler lane.

## 11. Claim boundary

Do not claim:

- `B2-MODULATION-COMPACTNESS` is mathematically false for every hypothetical singular NS solution;
- the periodic shear mechanism is an `R^3` or axisymmetric blow-up witness;
- the B2 middle limb has been killed;
- the conditional adjoint obstruction is unconditional;
- Clay A/B/C/D.
