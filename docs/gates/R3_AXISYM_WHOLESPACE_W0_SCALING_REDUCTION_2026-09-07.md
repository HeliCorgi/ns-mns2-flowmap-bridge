# R3 W0 candidate — scaling reduction and first-time identities (2026-09-07)

**Status:** derived analytic preflight for the W0 datum family. No blow-up or regularity claim.

For the W0 family

\[
u_{1,0}(r,z)=A\,b(r^2/R^2)\,(z/Z)b(z^2/Z^2),\qquad \omega_{1,0}=\psi_{1,0}=0,
\]

with viscosity `nu>0`, the apparent four parameters `(A,R,Z,nu)` contain only two nontrivial dimensionless search parameters after Navier–Stokes scaling.

## 1. Dimensionless reduction

Under the exact NS scaling

\[
 u_1^{(\lambda)}(r,z,t)=\lambda^2u_1(\lambda r,\lambda z,\lambda^2t),
\]

the family parameters transform as

\[
 A\mapsto \lambda^2A,\qquad R\mapsto R/\lambda,\qquad Z\mapsto Z/\lambda,
\]

while viscosity is unchanged. Therefore

\[
 \boxed{\alpha:=\frac{A R^2}{\nu}},\qquad
 \boxed{\kappa:=\frac{Z}{R}}
\]

are scale invariant. Apart from the swirl orientation `sign(A)`, the W0/W1 search can be organized by `(alpha,kappa)` rather than scanning `A,R,Z` independently.

A convenient normalized representative is

\[
 R=1,\qquad Z=\kappa,\qquad A=\alpha\nu.
\]

Any dynamically interesting representative can later be rescaled back to another physical length without changing `(alpha,kappa)`.

## 2. Competing initial time scales

The initial nonlinear time associated with the swirl amplitude is

\[
 \tau_{nl}\sim A^{-1},
\]

while radial diffusion acts on `R^2/nu` and axial diffusion on `Z^2/nu`. Hence

\[
 \frac{R^2/\nu}{\tau_{nl}}=\alpha,
 \qquad
 \frac{Z^2/\nu}{\tau_{nl}}=\alpha\kappa^2.
\]

Thus `alpha` is the natural one-scale swirl Reynolds parameter, and `kappa` controls anisotropy. This is bookkeeping, not a proof that large `alpha` causes singular behavior.

## 3. Exact first-time source check

Because `omega1_0=psi1_0=0`, the normalized equations give

\[
 \partial_t\omega_1|_{0}=\partial_z(u_{1,0}^2),
 \qquad
 \partial_tu_1|_0=\nu L_5u_{1,0}.
\]

The generated `omega1` source has characteristic size `A^2/Z`; after one nonlinear time its characteristic size is `A/Z`. Under the NS scaling these have the correct weights `lambda^5` for `partial_t omega1` and `lambda^3` for `omega1`.

This supplies a strict first-step manufactured test for W1: a time integrator must reproduce the analytic `partial_z(u1_0^2)` source before any feedback through `psi1` is interpreted.

## 4. Energy scaling check

The physical initial energy satisfies

\[
 \|u_0\|_2^2
 = C_b\,A^2R^4Z
 = C_b\,\alpha^2\nu^2\kappa R,
\]

where `C_b>0` is a fixed dimensionless constant determined only by the frozen bump. Under `R -> R/lambda`, `A -> lambda^2 A`, this scales as `lambda^{-1}`, exactly matching the three-dimensional Navier–Stokes `L^2` scaling.

This is also a measure sanity check: using the lifted measure as though it were physical volume would give the wrong dimensional law.

## 5. Search consequence

If W0 passes, the first W1 pilot should not perform an unconstrained amplitude/box scan. Freeze a small preregistered `(alpha,kappa)` table, with at least one `kappa≈1` one-scale case and one anisotropy stress case, and treat physical box size/resolution as numerical-error axes rather than additional mechanism parameters.
