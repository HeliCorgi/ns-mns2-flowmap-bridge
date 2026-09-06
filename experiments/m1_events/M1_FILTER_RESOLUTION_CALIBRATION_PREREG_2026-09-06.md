# M-1 near/far filter-resolution calibration preregistration — 2026-09-06

**Classification:** `NUMERICAL CALIBRATION PREREGISTRATION / EVIDENCE-GRADE ONLY`.

This calibration is required by `M1_RESOLUTION_RESCUE_PREREG_2026-09-06.md` before any filtered near/far diagnostic is promoted from same-grid categorical agreement to a mechanism verdict. It is designed after the E3c R2 output exposed mixed `ell/dx` sampling, but its acceptance rule is **not** chosen to make E3c or E4c pass. No production E3c/E4c values are used to fit a cutoff or percentage tolerance.

The calibration remains periodic `T^3` numerical work. It is not a continuum error theorem and not a Clay claim.

## 1. Problem to calibrate

The Yu-structured diagnostic uses

- Gaussian filtering at physical length `ell`;
- a sampled, smoothly cut off Biot--Savart far kernel at radius `rho R`, `rho=1/4`;
- FFT convolution for `S_far`;
- filtered commutator and localization terms;
- one-RK4-step frozen-cutoff finite difference for the filtered local budget check.

A raw production label such as `FAR` is not numerically meaningful merely because two grids happen to print the same string. The classification depends on signs and orderings of quantities that may be close to zero or to one another.

The calibration therefore does **not** preregister a single ad-hoc condition like `ell/dx >= K` or `relative difference <= p%`. Instead it builds an independent empirical error envelope and certifies a production label only when the observed label margin is larger than that envelope.

## 2. Manufactured fields

Use three deterministic real divergence-free trigonometric fields unrelated to E3c/E4c. Each is a finite sum of integer Fourier modes with coefficient vectors projected exactly perpendicular to the corresponding wavevector. Use only modes with `1 <= |k| <= 4` and fixed rational/integer amplitudes and fixed phases written explicitly in the calibration source.

No RNG, E3c/E4c initializer, or production snapshot is allowed in the manufactured suite.

The fields are sampled on every grid from the same explicit continuum trigonometric formula and then checked for Fourier divergence at roundoff level.

## 3. Fixed geometry

Do not use the vorticity maximum or the production dynamic radius in this calibration. Fix the physical center

```text
x0 = (0,0,0)
```

which lies on every grid, and fixed physical radii

```text
R in {pi/12, pi/6, pi/3}
rho = 1/4
sigma in {1/8, 1/4}
ell = sigma R
```

All radii obey `2R < L/2` for `L=2pi` except no equality case is used.

Use the same cutoff, Gaussian filter, far-kernel construction, commutator forcing and local budget formulas as `nearfar_yu.py`, but evaluated at this fixed geometry rather than at a dynamically selected vorticity maximum.

Set

```text
nu = 0.02
dt_cal = 1e-4
```

for the frozen-cutoff one-step budget check. `dt_cal` is common to all calibration grids so the spatial comparison is not confounded with the production `dt ~ 1/N` ladder.

## 4. Grid ladder and reference pair

Calibration grids:

```text
N = 64, 96, 128
```

Independent higher-resolution numerical reference pair:

```text
N_ref1 = 160
N_ref2 = 192
```

The N=192 result is the reference value. The N=160 vs N=192 difference is retained as a reference-stability penalty rather than silently treating N=192 as exact.

If the N=160/N=192 reference pair is non-finite or grossly inconsistent for a quantity, that calibration cell is `REFERENCE_UNSTABLE` and cannot certify a production sample.

## 5. Quantities

For each manufactured field, R, sigma and N, record at least

```text
P
A_N = Vp_near/P
g = (V_near + V_far - P + Rcomm + Lloc)/P
B_F = V_far/P
B_C = Rcomm/P
B_L = Lloc/P
budget_resid
R/dx
ell/dx
```

`B_F`, `B_C`, and `B_L` are the **signed** normalized contributions corresponding to the actual residual-label ordering. `A_F = Vp_far/P` may also be recorded for continuity with production reports, but it is not substituted for signed `B_F` in label certification.

## 6. Resolution bins

Assign each coarse-grid calibration sample to exactly one preregistered bin by its measured `ell/dx`:

```text
B0: ell/dx < 1
B1: 1 <= ell/dx < 2
B2: 2 <= ell/dx < 3
B3: 3 <= ell/dx < 4
B4: ell/dx >= 4
```

Do not move these bin boundaries after the calibration or production results are inspected.

## 7. Empirical error envelope

For each normalized quantity

```text
q in {A_N, g, B_F, B_C, B_L}
```

and each resolution bin B, define the empirical envelope

```text
eps_q(B) = max over manufactured calibration cells in B of
           ( |q_N - q_192| + |q_160 - q_192| ).
```

The first term measures coarse-to-reference disagreement; the second explicitly penalizes reference instability. No percentage is fitted to E3c/E4c.

Also report the analogous absolute envelope for `budget_resid`, but do not use a small budget residual alone to certify a residual class.

This is an empirical numerical envelope, **not** a rigorous upper bound on continuum discretization error.

## 8. Margin-based production certification rule

After the calibration envelope is frozen, a production sample may be assigned a numerically certified local residual label only as follows.

### Local-growth sign

For the sample's `ell/dx` bin B:

```text
g >= +eps_g(B)  => POSITIVE_LOCAL_GROWTH numerically separated from zero
g <= -eps_g(B)  => NO_POSITIVE_LOCAL_GROWTH numerically separated from zero
otherwise        => NUMERICALLY_AMBIGUOUS_G
```

### Near-field absorption

```text
A_N <= 1 - eps_A_N(B) => NEAR_ABSORBED numerically separated from the boundary
A_N >= 1 + eps_A_N(B) => NEAR_NOT_ABSORBED numerically separated from the boundary
otherwise              => NUMERICALLY_AMBIGUOUS_NEAR
```

### Residual winner

Let the signed normalized residual scores be

```text
b_F = B_F, b_C = B_C, b_L = B_L.
```

A candidate winner `j in {F,C,L}` is numerically certified only if

```text
b_j > eps_j(B)
```

and for every other `k`,

```text
b_j - b_k > eps_j(B) + eps_k(B).
```

Otherwise the residual class is `NUMERICALLY_AMBIGUOUS_RESIDUAL`.

This is a margin rule, not a percentage convergence rule. It follows the elementary interval-separation shape: if each score may move by its empirical envelope, the winner must remain separated under both movements.

## 9. Cross-resolution use

When two production grids are compared, a categorical FAR/COMM/LOC agreement counts toward mechanism promotion only if the label is independently margin-certified on **both** grids using the frozen calibration envelope.

An under-resolved or ambiguous grid is not repaired by agreement with a finer grid. Conversely, a production sample is not rejected merely because `ell/dx` is small if the manufactured envelope in that bin is sufficiently sharp and the observed margins dominate it.

This avoids post-hoc rules of both forms:

- `ell/dx >= K` chosen after seeing production data;
- `% convergence <= p` chosen after seeing which p preserves FAR.

## 10. Stop/go consequences

The calibration itself has no FAR/COMM/LOC preferred outcome.

- If the manufactured reference is unstable across the useful bins, mark the near/far decomposition numerically unqualified at those scales and do not promote it.
- If stable envelopes exist, apply the margin rule mechanically to E3c and later E4c outputs.
- If the previously observed FAR labels become ambiguous under the frozen envelope, report that; do not relax the envelope.
- If a different residual becomes certified, report that; do not redefine the label score.

The broader M-1 GO rule remains unchanged: at least two genuinely different continuum data must be tail-qualified, refinement-stable, and select the same residual mechanism after numerical certification and later highest-grid `dt/2` confirmation.

## 11. Claim boundary

This calibration does not prove a continuum near/far decomposition error bound. It does not prove Yu's estimate for the Gaussian/periodic implementation, does not prove regularity, and does not establish a singularity. Its sole role is to prevent a production mechanism label from being promoted when its numerical sign/order margins are smaller than independently measured diagnostic discretization errors.