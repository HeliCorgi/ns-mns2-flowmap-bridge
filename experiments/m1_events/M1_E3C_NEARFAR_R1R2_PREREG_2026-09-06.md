# M-1 E3c near/far R1/R2 preregistration — 2026-09-06

**Classification:** `NUMERICAL EXPERIMENT PREREGISTRATION / EVIDENCE-GRADE ONLY`.

This gate follows the accepted E3c R0 results now on `main`:

```text
E3c64   max_tail = 5.956860730357e-05   FAIL
E3c96   max_tail = 3.274744131023e-07   PASS
E3c128  max_tail = 2.845872144398e-09   PASS
```

Only E3c96 and E3c128 are admitted. E3c64 is excluded.

## R1 execution

Run the existing `nearfar_rescue.py` without changing its solver, filter, cutoff, Yu-structured near/far split, scale ladder, output cadence, or diagnostic formulas.

The two accepted resolution-screen JSON inputs are recovered from their exact GitHub Actions artifacts rather than regenerated:

- E3c96: workflow run `34013942287`, artifact id `9983371155`, digest `sha256:c8775148c3a9d00614fd474561e14f592711efe799e09934382c8f495000815b`;
- E3c128: workflow run `34015004075`, artifact id `9983774115`, digest `sha256:9f8dd8f4cb79f3d84cab81701b98d85189c3ae74f3b01d56b51788f44455fc8e`.

The workflow must verify artifact identity/provenance and the fail-closed fields `tail_pass=true`, `finite_pass=true`, expected `N`, `nu`, `T`, `dt`, and `tail_tolerance=1e-5` before invoking `nearfar_rescue.py`.

## R2 comparison

Compare E3c96 and E3c128 only on common physical output times. The already-recorded quantities are:

- global enstrophy `E`, maximum vorticity `Lam`, and viscous scale `sv`;
- `A_N`, `A_F`, `A_C`, `A_L`, `g`;
- physical `R`, `ell` and grid counts `R/dx`, `ell/dx`;
- filtered-budget residual;
- residual-class label at common positive-global-enstrophy-growth samples.

Growth events keep the standing definition: maximal intervals on which sampled global enstrophy increases from a local minimum to the following local maximum. No new growth threshold is introduced.

### Residual-label rule fixed before the E3c R1 outputs

At one `(time, c, sigma)` sample:

1. if `g <= 0`, label `NO_POSITIVE_LOCAL_GROWTH`;
2. if `A_N >= 1`, label `NEAR_NOT_ABSORBED`;
3. otherwise inspect the signed budget contributions `V_far`, `Rcomm`, `Lloc`;
4. among strictly positive contributions, label the largest as `FAR`, `COMM`, or `LOC`;
5. exact equal maxima are reported as `TIE(...)`; if no positive residual exists, report `NONE`.

This label is bookkeeping for the filtered budget only. It is not a proof mechanism.

## No post-hoc convergence tolerance

This R2 gate does **not** introduce a percentage pass threshold for continuous diagnostics after seeing E3c96/E3c128. It reports:

- exact categorical label agreement/mismatch;
- symmetric relative differences for continuous axes;
- absolute differences for the filtered-budget residual;
- growth-event intervals and grid-scale counts.

A quantitative promotion tolerance remains deferred to a separate manufactured/filter-resolution test, as required by `M1_RESOLUTION_RESCUE_PREREG_2026-09-06.md`.

## Decision boundary

Even perfect E3c96/E3c128 agreement would establish only one fixed continuum datum with an internally stable diagnostic pattern. The broader M-1 GO rule still requires a second genuinely different fixed continuum datum, later time-step refinement of the highest accepted grid, and the same residual class after near-field absorption.

No `R^3`, blow-up, regularity, or Clay A/B/C/D claim is attached to this experiment.
