# R3 W0 static implementation preregistration — 2026-09-07

**Status:** frozen numerical gate specification before production W0 output. No singularity, regularity, or Clay A/B/C/D claim.

This addendum instantiates the five subgates in `R3_AXISYM_WHOLESPACE_W0_PREREG_2026-09-07.md`. The values below are fixed before the first production invocation of the W0 gate. Failed rows are not rescued by changing tolerances, source widths, receiver points, or box sequences after output inspection.

## 1. Normalization and exact datum row (W0-A)

For the static datum-generation audit use

```text
A = 1
R = 1
Z = 1
Cartesian audit box = [-1.25,1.25]^3
N = 33, 65, 129
```

with

`u1(r,z) = A b(r^2/R^2) (z/Z) b(z^2/Z^2)`.

The Cartesian reconstruction is

```text
u_x = -y u1
u_y =  x u1
u_z =  0.
```

Acceptance:

1. every stored field is finite;
2. analytic divergence is identically zero by the frozen formula, and the independently centered Cartesian finite-difference divergence has, on the two-cell interior of the `N=129` cube,
   - `max_abs_div <= 4e-3`,
   - `rms_div <= 4e-4`;
3. both numerical divergence norms decrease from `N=33 -> 65 -> 129`;
4. signed-r parity checks for `u1` are at roundoff (`<= 5e-15` absolute);
5. the Cartesian energy quadrature is refinement-stable:
   `abs(E129-E65)/abs(E129) <= 1e-5`;
6. all nonzero samples satisfy `r < R` and `|z| < Z` up to floating-point evaluation of the exact bump support.

These are implementation gates, not continuum error bounds.

## 2. Frozen manufactured sources and receivers (W0-B/C)

Let

```text
rc2 = 1.0
d2  = 0.36
q_r(rho) = ((rho^2-rc2)/d2)^2
B_r(rho) = b(q_r(rho))
```

so the radial support is the smooth annulus

```text
sqrt(0.64) < rho < sqrt(1.36).
```

For base axial width `w=0.6`, freeze

```text
omega_even(rho,zeta) = B_r(rho) b((zeta/w)^2)
omega_odd (rho,zeta) = B_r(rho) (zeta/w) b((zeta/w)^2).
```

The odd source has exact zero lifted monopole by `zeta` parity. Both sources are smooth and compactly supported and are separated radially from the receiver set

```text
P1 = (r,z) = (0.12,  0.00)
P2 = (r,z) = (0.24,  0.20)
P3 = (r,z) = (0.28, -0.24)
P4 = (r,z) = (0.20,  0.32).
```

No receiver lies in the source support. This is deliberate: W0 first audits the free-space/domain machinery without a singular Green quadrature cell. A later gate may add in-support receivers with singularity subtraction.

## 3. Independent Green reference

Use the exact 5-D representation reduced over `S^3`:

```text
psi(r,z) = (1/(2*pi)) int int rho^3 omega(rho,zeta)
           [int_{-1}^1 sqrt(1-t^2) D^(-3/2) dt] drho dzeta,
D = r^2 + rho^2 - 2 r rho t + (z-zeta)^2.
```

Derivatives are differentiated under the separated-support integral:

```text
partial_r D^(-3/2) = -3 (r-rho*t) D^(-5/2)
partial_z D^(-3/2) = -3 (z-zeta) D^(-5/2).
```

Use Gauss-Legendre in `rho,zeta` and Gauss-Chebyshev of the second kind for the `sqrt(1-t^2)` angular weight. The production reference is the 64x64x64 rule. The independent quadrature check is the 48x48x48 rule.

Acceptance:

```text
max_abs(reference64-reference48)
```

over all four receivers, both sources, and the three fields `(psi,partial_r psi,partial_z psi)` is `<= 1e-9`.

## 4. Finite-box discretization check with exact Green boundary (W0-B)

Discretize `-L5 psi = omega` on a uniform `(r,z)` grid, including the axis. Use second-order centered differences for `r>0`, the even-axis limit

```text
L5 psi(0,z) = 4 psi_rr(0,z) + psi_zz(0,z)
```

with the even ghost relation, and exact Green-reference Dirichlet data on the outer `r=Rmax` and `z=+-Zmax` boundaries.

Freeze

```text
Rmax = 2.0
Zmax = 1.2
h = 0.04, 0.02.
```

At the frozen receivers compare `(psi,partial_r psi,partial_z psi)` using centered grid derivatives. For each source define the combined relative receiver error as the Euclidean norm of the 12-component error divided by the Euclidean norm of the 12-component Green-reference vector.

Acceptance for each source:

```text
E(h=0.02) <= 0.25 * E(h=0.04)
E(h=0.02) <= 5e-4.
```

The exact-boundary row isolates the interior discretization; it is not itself the free-space truncation test.

## 5. Independent zero-boundary box expansions (W0-C)

Use homogeneous outer Dirichlet data only for this truncation row. Hold `h=0.02` fixed.

Radial expansion:

```text
Zmax = 6.0
Rmax = 2.0, 3.0, 4.0, 6.0.
```

Axial expansion:

```text
Rmax = 6.0
Zmax = 1.2, 2.0, 3.0, 4.0, 6.0.
```

For each source the combined relative receiver error must strictly decrease at every expansion step in both sequences, and the common final `(Rmax,Zmax)=(6,6)` error must satisfy

```text
E_final <= 5e-3.
```

At the final box also compute the exact Green values on the outer boundary and record the conservative analytic far-field envelopes from W0.10/W0.11 wherever `|X| >= 2S`. The measured boundary values must not exceed the corresponding analytic envelope by more than `1e-10` absolute plus `1e-10` relative slack.

## 6. Long-axial-scale stress (W0-D)

Keep the radial shell and receivers frozen and enlarge only the axial source width to

```text
w_stress = 1.2.
```

Use the 64x64x64 Green reference with the same 48x48x48 self-check. With homogeneous outer Dirichlet data and `h=0.02`, freeze

```text
Rmax = 6.0
Zmax = 2.0, 3.0, 4.0, 6.0, 8.0.
```

Acceptance for each source:

1. Green self-check `<= 1e-9` as above;
2. combined relative receiver error strictly decreases at every axial expansion;
3. final error at `(Rmax,Zmax)=(6,8)` is `<= 6e-3`.

This row is intended to make the continuous low-axial-frequency tail more expensive than the base row, not to emulate a periodic Fourier gap.

## 7. Symmetry and measure audit (W0-E)

Use symmetric Gauss-Legendre quadrature for lifted source moments.

Acceptance:

```text
abs(M0_odd) / L1_odd <= 1e-12,
```

where

```text
M0_odd = 2*pi^2 int rho^3 omega_odd drho dzeta
L1_odd = 2*pi^2 int rho^3 |omega_odd| drho dzeta.
```

For the W0 datum, record physical energy with the physical `R^3` measure (or Cartesian volume) under the key `physical_energy`. Any lifted `r^3 dr dz` diagnostic must be stored under a distinct `lifted_*` key. The JSON schema check fails if a lifted quantity is substituted for `physical_energy`.

## 8. Decision and output

The implementation writes a machine-readable JSON report containing every row above and a final decision.

```text
R3-W0 = PASS
```

only if W0-A/B/C/D/E all pass exactly as frozen here. Otherwise:

```text
R3-W0 = STOP_REPAIR_STATIC_WHOLE_SPACE_GATE.
```

No failed production run is rescued by changing the frozen constants in this document. W1 remains closed until a passing W0 report is independently reproduced and reviewed.
