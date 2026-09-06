# M-1 resolution rescue preregistration — 2026-09-06

**Classification:** `NUMERICAL EXPERIMENT PREREGISTRATION / EVIDENCE-GRADE ONLY`.

This branch resumes the periodic M-1 mechanism-discovery program after the analytic B2 narrowing lanes reached their current stop rules. Nothing here is an `R^3` candidate, a singularity claim, or a Clay A/B/C/D claim.

## 1. Why resolution rescue comes before another observable

The standing M-1 preregistration allows a run into the verdict only when its full-run spectral tail remains at or below `1e-5`.

The current stored summary is:

| run | N | max tail | standing verdict |
|---|---:|---:|---|
| E0 | 64 | `2.8691770713435234e-08` | PASS |
| E1 | 64 | `3.969158378526758e-05` | FAIL |
| E3 | 64 | `4.8422283231966924e-05` | FAIL |
| E4 | 64 | `5.9967246781271955e-05` | FAIL |
| E2 | 64 | `9.939773706363298e-04` | FAIL |
| E2b | 96 | `1.3196230254612794e-04` | FAIL |

Therefore the existing filtered near/far outputs cannot yet support a cross-datum mechanism verdict. `stateflow_harness.py` has a per-snapshot mask, but a few locally admissible snapshots do **not** override the older run-level fail-closed rule.

The currently stored Yu-structured near/far summaries are nevertheless useful as a hypothesis generator: wherever the mask admits growth-event samples, `A_N < 1` and the positive surplus is classified as FAR rather than COMM/LOC. This is not yet a cross-datum result because only E0 is globally resolved by the standing rule.

## 2. Continuum-datum bug in the old random runs

The legacy `ic_random_band` and the random perturbation inside `ic_r4` draw Gaussian numbers directly into arrays whose FFT shape depends on `N`. Holding the RNG seed fixed therefore does **not** define one fixed continuum trigonometric polynomial across different resolutions.

Consequently old E3/E4 files are valid one-grid diagnostics, but a naive `N=64 -> 96 -> 128` rerun would not be a spatial convergence sequence for one datum.

This branch adds `resolution_invariant_ic.py`. It defines a canonical finite set of integer wavevectors, draws sine/cosine coefficients in a resolution-independent order, projects each coefficient perpendicular to its wavevector, and samples the resulting finite trigonometric polynomial on each grid. New continuum-seeded analogues are named `E3c*` and `E4c*`; old E3/E4 provenance remains untouched.

## 3. Stage R0 — cheap whole-run screening

Run `resolution_rescue.py` before any expensive filtered near/far diagnostic.

The screen records at every accepted RK4 step:

- spectral tail and full-run maximum tail;
- finite-value status;
- kinetic energy and maximum positive single-step relative energy change.

At `0.1` physical-time cadence it additionally records:

- enstrophy;
- maximum vorticity;
- a simple advective CFL diagnostic.

Eligibility for the next stage requires

`max_tail <= 1e-5`

for the **entire run** and no non-finite state.

The resolution ladder is preregistered as follows.

### Taylor--Green E1

- `E1R96`: `N=96`, `dt=1/150`;
- `E1R128`: `N=128`, `dt=1/200`.

Both use the same analytic Taylor--Green continuum datum.

### Antiparallel tubes E2

Continue beyond failed E2/E2b:

- `E2R128`: `N=128`, `dt=1/200`;
- if needed `E2R160`: `N=160`, `dt=1/250`;
- if needed `E2R192`: `N=192`, `dt=1/300`.

The initial tube formula is unchanged.

### Continuum-seeded E3c / E4c

- `N=64`, `96`, `128` with `dt` proportional to `1/N`;
- E3c retains the deterministic two-mode backbone plus a 10% resolution-invariant low-band perturbation;
- E4c is a resolution-invariant random band with `1 <= |k| <= 2`.

These are new data families for convergence purposes. Do not silently compare their numerical values with old E3/E4 as though the initial fields were identical.

## 4. Stage R1 — rerun the literature-backed filtered near/far diagnostic

Only after a resolution screen passes may `nearfar_rescue.py` invoke the existing Yu-structured filtered near/far decomposition.

The decision question remains the one fixed in `M1_BOUNDARY_LOCALIZATION_ESTIMATE_AUDIT_2026-09-04.md`:

> In every resolved enstrophy-growth event, is positive near-field filtered stretching absorbed by diffusion while one reproducible residual class carries the positive surplus?

The candidate residual classes are FAR, COMM, and LOC.

The historical per-snapshot FAR pattern is a hypothesis only. It becomes an M-1 cross-datum mechanism candidate only if it survives full-run tail qualification and spatial/time refinement on fixed continuum data.

## 5. Stage R2 — convergence comparison before mechanism promotion

For each datum that reaches two tail-qualified resolutions, compare on common physical times:

- growth-event start/end times;
- maximum enstrophy and maximum vorticity;
- `A_N`, `A_F`, `A_C`, `A_L`, `g`;
- residual-class label at positive-growth samples;
- `R/dx` and `ell/dx`;
- filtered-budget residual.

No fixed percentage convergence threshold is invented here. A mechanism verdict requires a visibly stabilizing sequence and a separately documented tolerance justified by a manufactured/filter-resolution test; the tolerance must not be selected after seeing which value makes the desired mechanism pass.

After spatial qualification, the highest accepted grid must also be rerun with `dt/2` before the result is promoted beyond diagnostic-only status.

## 6. Stop/go rule

**GO:** if at least two genuinely different continuum data have tail-qualified, refinement-stable growth events and the same residual class carries the positive surplus after near-field absorption, select that residual as the next single M-1 proof/diagnostic target.

**STOP:** if residual dominance changes with datum or refinement, or the decomposition cannot be resolved without moving to impractical scales, park the filtered near/far M-1 mechanism rather than introducing another threshold or local observable.

## 7. Claim boundary

Do not claim:

- the current FAR pattern is already universal;
- a per-snapshot stateflow mask repairs a globally unresolved run;
- old E3/E4 form a fixed-datum convergence sequence;
- the periodic M-1 experiment is an `R^3` candidate;
- filtered near-field absorption proves regularity;
- any numerical growth proves blow-up.
