# R3 axisymmetric-with-swirl whole-space W0 preregistration — 2026-09-07

**Status:** research preregistration / exact datum construction. **No singularity claim. No Clay A/B/C/D claim.**

This record resumes the primary `SPEC.md` track after periodic M-1 PR #106 stopped under its preregistered all-FAR gate. The purpose of W0 is deliberately narrower than a time-evolution experiment: first construct an exact `R^3`, unforced, Cartesian-smooth, compactly supported axisymmetric-with-swirl datum and certify a genuinely free-space elliptic inversion path. Only after W0 passes should a time integrator be frozen.

The stopped periodic M-1 mechanism is not reopened here. The Hou finite-cylinder wall problem is not identified with this track. The external Fable5 P0-E audit is treated as binding negative knowledge: periodic `z` radial-wall sensitivity is not a whole-space transition test.

## 1. Exact candidate family

Define the standard compact bump on nonnegative arguments

\[
 b(s)=
 \begin{cases}
 \exp\!\left(-\dfrac{s}{1-s}\right),&0\le s<1,\\
 0,&s\ge1.
 \end{cases}
\]

Thus `b(0)=1`, `b` is smooth on `[0,\infty)`, all derivatives vanish at `s=1`, and

\[
 b'(s)=-\frac{b(s)}{(1-s)^2},\qquad 0\le s<1.
\]

For parameters

\[
 A\ne0,\qquad R>0,\qquad Z>0,
\]

set

\[
 u_{1,0}(r,z)
 =A\,b\!\left(\frac{r^2}{R^2}\right)
 \frac{z}{Z}\,b\!\left(\frac{z^2}{Z^2}\right),
 \qquad
 \omega_{1,0}=0,
 \qquad
 \psi_{1,0}=0.
 \tag{W0.1}
\]

The physical velocity is pure swirl initially:

\[
 u_0^r=u_0^z=0,\qquad u_0^\theta=r u_{1,0}.
 \tag{W0.2}
\]

In Cartesian coordinates,

\[
 \boldsymbol u_0(x,y,z)
 =\bigl(-y f(x^2+y^2,z),\;x f(x^2+y^2,z),\;0\bigr),
 \quad
 f(s,z)=A b(s/R^2)\frac{z}{Z}b(z^2/Z^2).
 \tag{W0.3}
\]

This family is chosen to satisfy the `SPEC.md` axis-regularity rule by construction: radial dependence is through `r^2`, not an arbitrary smooth function of `r`.

## 2. Exact preflight facts [DERIVED]

### 2.1 Compact support and Cartesian smoothness

From the bump definition,

\[
 \operatorname{supp}\boldsymbol u_0
 \subset\{r<R,\ |z|<Z\}.
\]

Because `f` is `C^\infty` in `(x^2+y^2,z)` and flat at the support boundary, (W0.3) is in `C_c^\infty(R^3;R^3)`. In particular there is no cylindrical-coordinate singularity at the axis.

### 2.2 Divergence-free exactly

Differentiating (W0.3),

\[
 \partial_x(-y f)+\partial_y(x f)
 =-2xy f_s+2xy f_s=0,
\]

and `u_{0,z}=0`, hence

\[
 \nabla\cdot\boldsymbol u_0=0
\]

pointwise. This is an algebraic identity, not a numerical divergence check.

### 2.3 Axis parity and swirl

`u_{1,0}` is even in signed `r` and odd in `z`; `u_0^\theta=r u_{1,0}` is odd in signed `r` and nonzero for `A\ne0`. Thus the datum is axisymmetric with swirl and satisfies every odd-radial derivative condition for `u_1` at `r=0`.

### 2.4 Finite physical three-dimensional energy

Using physical measure `2\pi r\,dr\,dz`,

\[
 \|\boldsymbol u_0\|_2^2
 =2\pi\int_{-Z}^{Z}\int_0^R r^3|u_{1,0}(r,z)|^2\,dr\,dz<\infty.
 \tag{W0.4}
\]

This is the physical `R^3` energy. The lifted measure `r^3drdz` is useful for `L_5`, but it must not be mislabeled as the physical volume measure.

### 2.5 Initial vorticity and first source generation

For a pure-swirl datum,

\[
 \omega_0^r=-r\partial_z u_{1,0},\qquad
 \omega_0^\theta=0,\qquad
 \omega_0^z=2u_{1,0}+r\partial_r u_{1,0}.
 \tag{W0.5}
\]

Hence `\omega_{1,0}=\omega_0^\theta/r=0`, consistent with `\psi_{1,0}=0` under free-space decay.

The normalized axisymmetric system then gives the exact initial derivatives

\[
 \partial_t u_1\big|_{t=0}=\nu\mathcal L_5u_{1,0},
 \qquad
 \partial_t\omega_1\big|_{t=0}=\partial_z(u_{1,0}^2).
 \tag{W0.6}
\]

Thus the datum starts with no meridional vorticity but immediately generates it from the swirl source. This is a useful manufactured first-step identity for any later time integrator.

Writing `q=z^2/Z^2`,

\[
 \partial_z u_{1,0}
 =\frac{A}{Z}b(r^2/R^2)
 \left[b(q)+2q b'(q)\right],
 \]

so `\partial_z(u_{1,0}^2)=2u_{1,0}\partial_z u_{1,0}` is explicit.

### 2.6 No instantaneous stretching gain in enstrophy

At `t=0`, the velocity is pure azimuthal while the vorticity lies in the `(e_r,e_z)` plane. The strain of a pure-swirl field has only `r\theta` and `z\theta` off-diagonal components, so

\[
 \omega_0\cdot S_0\omega_0=0
\]

pointwise. Consequently the exact smooth energy/enstrophy identities give

\[
 \frac12\frac d{dt}\|u(t)\|_2^2\Big|_{0}
 =-\nu\|\nabla u_0\|_2^2<0,
\]

\[
 \frac12\frac d{dt}\|\omega(t)\|_2^2\Big|_{0}
 =-\nu\|\nabla\omega_0\|_2^2<0
\]

for nontrivial `A`. Therefore any numerical run showing an immediate positive first derivative of energy or enstrophy for this exact datum fails a basic manufactured check. Later growth, if any, must arise only after the generated `\omega_1` feeds back through `\psi_1`.

## 3. Free-space `-L_5` inversion [DERIVED]

The equation

\[
 -\mathcal L_5\psi_1=\omega_1
\]

is the restriction of the scalar five-dimensional Poisson equation to functions radial in the first four coordinates. It is **not** a five-dimensional fluid equation.

Let `X=(\xi,z)\in R^4\times R`, `|\xi|=r`. The fundamental solution of `-\Delta_5` is

\[
 \Phi_5(X)=\frac{1}{8\pi^2}|X|^{-3}.
 \tag{W0.7}
\]

Therefore the exact free-space reference inversion is

\[
 \psi_1(X)=\frac1{8\pi^2}
 \int_{\mathbb R^5}\frac{\omega_1(Y)}{|X-Y|^3}\,dY.
 \tag{W0.8}
\]

For axisymmetric data `Y=(\rho\sigma,\zeta)`, `\sigma\in S^3`, this becomes

\[
 \psi_1(r,z)=\frac1{8\pi^2}
 \int_{\mathbb R}\int_0^\infty \rho^3\omega_1(\rho,\zeta)
 \int_{S^3}
 \frac{d\sigma}
 {(r^2+\rho^2-2r\rho\sigma_1+(z-\zeta)^2)^{3/2}}
 \,d\rho\,d\zeta.
 \tag{W0.9}
\]

This Green representation is the primary independent reference for W0. A finite-box elliptic solver is not accepted as free-space merely because box doubling looks small.

### 3.1 Simple analytic far-field enclosure for compact manufactured sources

If a manufactured `\omega_1` is supported in the lifted ball `|Y|\le S`, let

\[
 M_0=\|\omega_1\|_{L^1(\mathbb R^5)}.
\]

For `|X|\ge2S`, `|X-Y|\ge|X|/2`, so

\[
 |\psi_1(X)|\le \frac{M_0}{\pi^2|X|^3},
 \qquad
 |\nabla_5\psi_1(X)|\le\frac{6M_0}{\pi^2|X|^4}.
 \tag{W0.10}
\]

These are conservative analytic boundary-error envelopes for compact manufactured Poisson tests.

If additionally `\int\omega_1\,dY=0` and

\[
 M_1=\int |Y|\,|\omega_1(Y)|\,dY<\infty,
\]

then subtracting the monopole and applying the mean-value theorem gives

\[
 |\psi_1(X)|\le\frac{6M_1}{\pi^2|X|^4},\qquad |X|\ge2S.
 \tag{W0.11}
\]

The odd-`z` symmetry of this candidate makes the lifted total mass of any integrable odd `\omega_1` vanish. This cancellation is therefore a natural free-space boundary diagnostic, but W0 will measure it rather than assume numerical preservation.

For the evolved viscous solution, compact support is immediately lost. Equations (W0.10)–(W0.11) are **not** silently promoted to a global-in-time truncation theorem; an evolved-source tail enclosure remains a later obligation.

## 4. W0 fail-closed numerical gate

W0 contains no time evolution. It is a static whole-space-transition gate and must pass before W1 is opened.

### W0-A — exact datum generation

Generate (W0.1) on at least three independent resolutions with fixed physical `(A,R,Z)`. Save `u1_0, omega1_0, psi1_0` and Cartesian `u_0` reconstruction. Required:

- finite values everywhere;
- exact/roundoff-level axis parity;
- Cartesian divergence converging to roundoff under analytic derivative evaluation and at the advertised order under independent numerical differentiation;
- physical `R^3` energy quadrature converging under refinement;
- support metadata exactly matches `r<R, |z|<Z`.

### W0-B — manufactured free-space Poisson reference

Do **not** use `omega1_0=0` for this subtest. Freeze at least two nontrivial compact manufactured `\omega_1` sources:

1. one with nonzero lifted monopole;
2. one odd in `z` with zero lifted monopole.

Evaluate the Green reference (W0.9) to substantially higher quadrature accuracy than the finite-box solver. Compare `psi1`, `partial_r psi1`, and `partial_z psi1` on an interior receiver region.

### W0-C — independent box expansion

Increase `Rmax` while holding `Zmax` fixed, then increase `Zmax` while holding `Rmax` fixed. A single diagonal box-doubling sequence is insufficient. Record interior errors against the Green reference and the analytic envelopes (W0.10)–(W0.11).

### W0-D — low-frequency / long-axial-scale stress

Repeat W0-B/C with the axial source width enlarged while the core receiver region is fixed. The purpose is to expose the continuous low-frequency tail that periodic `z` would suppress. Any solver whose apparent wall independence disappears under this stress is not promoted.

### W0-E — symmetry and measure audit

For the odd source, record the lifted monopole `\int\omega_1 r^3drdz` and verify convergence to zero. Separately record physical three-dimensional quantities with `2\pi r drdz`; do not reuse lifted integrals as physical energy/enstrophy without the correct weights.

## 5. W0 decision

W0 passes only if all five subgates pass under fixed tolerances declared in the implementation PR **before** the first production output is inspected.

```text
R3-W0 = PASS
```

permits opening W1: a frozen nonperiodic time-evolution scheme with per-step stability/CFL/energy/parity diagnostics and an independent free-space elliptic check.

Any failure gives

```text
R3-W0 = STOP / REPAIR STATIC WHOLE-SPACE GATE
```

and no dynamic amplification run is started.

## 6. Explicit nonclaims and reopen rules

This record does not assert that (W0.1) is singular, near-singular, or even dynamically amplifying. It supplies an exact admissible datum family and a domain-correct numerical gateway.

Do not reopen the stopped periodic filtered near/far lane merely because W0 is difficult. Do not reuse Hou's no-slip wall closure in the free-space track. Do not call a finite-box result `R^3` until the Green/tail/domain gates above pass.

A later W1 integrator must address the standing Heun/RK2-plus-centered-advection stability objection before any growth is interpreted physically; W0 intentionally avoids that issue by containing no time stepping.
