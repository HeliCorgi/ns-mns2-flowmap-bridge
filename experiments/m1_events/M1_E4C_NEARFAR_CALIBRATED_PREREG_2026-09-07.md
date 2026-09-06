# M-1 E4c near/far + frozen-calibration preregistration — 2026-09-07

**Status:** committed before any E4c96/E4c128 near/far R1 execution on this branch.

## Scope

Periodic `T^3` evidence-grade mechanism selection only. This is not an `R^3` candidate, not a blow-up theorem, not a global-regularity theorem, and not a Clay A/B/C/D result.

This gate asks whether the same independently calibrated residual class that survived on the fixed-continuum E3c datum also survives on the distinct fixed-continuum E4c datum.

## Frozen inputs

Only the R0-qualified E4c pair is admissible:

```text
E4c96
  N = 96
  nu = 0.02
  T = 6.0
  dt = 1/120
  max_tail = 1.134755892947e-06
  tail_pass = True
  finite_pass = True
  artifact = 9985091027
  digest = sha256:ca63edd772797ad325e819b682f8187f6aa1500eb34484400e0c30cd5ddae8da

E4c128
  N = 128
  nu = 0.02
  T = 6.0
  dt = 1/160
  max_tail = 3.536985710923e-08
  tail_pass = True
  finite_pass = True
  artifact = 9985610481
  digest = sha256:9f17b8e926f9a90c69b33a61701a22e724a15da46931e3e19f8eb914d1aeef88
```

E4c64 is excluded because it failed the standing whole-run R0 spectral-tail gate.

The filter-resolution calibration is already frozen and must not be changed:

```text
artifact = 9994071254
digest = sha256:6d6ca58697a1659d814dc5ae9736e105847ebdd690423d5233997f547129506e
reference pair = N160/N192
B3 = NO_CALIBRATION_COVERAGE
```

No production value may be used to modify the calibration bins or epsilon values.

## R1 execution

Run the existing `nearfar_rescue.py` unchanged on E4c96 and E4c128 after recovering and rechecking the exact accepted R0 JSON artifacts.

The existing numerical definitions remain frozen:

- `c in {8,16,32}`;
- `sigma in {0.125,0.25}`;
- `rho = 0.25`;
- same Gaussian filter;
- same periodic sampled far-strain kernel;
- same local filtered-enstrophy budget;
- same 0.1 physical-time output cadence;
- same `A_N`, signed `B_F=V_far/P`, `B_C=Rcomm/P`, `B_L=Lloc/P`, and `g` definitions.

No ladder point may be inserted after seeing E4c output.

## R2 comparison

Run `compare_nearfar_refinement.py` unchanged on the two E4c R1 JSONs. This comparison is threshold-free and reports:

- global growth events on common physical times;
- continuous-axis symmetric relative differences;
- raw categorical labels on common positive-forward global-enstrophy times;
- `R/dx`, `ell/dx`, and filtered-budget residual information.

No convergence percentage is introduced here.

## Frozen-calibration certification

Run `certify_nearfar_with_calibration.py` unchanged using the already-frozen manufactured envelope.

For each production sample:

1. map measured `ell/dx` to B0--B4;
2. B3 is `NUMERICALLY_UNCERTIFIED_RESOLUTION` with no interpolation or neighboring-bin borrowing;
3. local-growth sign must clear `eps_g`;
4. near absorption/non-absorption must clear the `A_N=1` boundary by `eps_A_N`;
5. residual winner uses signed `B_F`, `B_C`, `B_L` only;
6. a winner must be positive beyond its own envelope and pairwise separated from competitors by the sum of both envelopes;
7. `A_F=Vp_far/P` is never used as the FAR winner score.

## Predeclared cross-datum decision row

The load-bearing E3c row is already fixed as

```text
(c,sigma) = (16,0.125)
E3c96/E3c128: 17/17 FAR -> FAR after frozen calibration.
```

Therefore the **primary E4c cross-datum row is fixed in advance to the same `(16,0.125)` row**. It is not selected after seeing E4c output.

### GO to temporal-refinement stage

The spatial/mechanism gate is `GO_TO_DT2` only if all of the following hold:

- E4c96 and E4c128 retain a common positive-forward global-enstrophy event;
- the `(16,0.125)` row is calibration-covered on both grids at every common positive-forward sample on which that combo exists;
- every such sample is independently certified `FAR -> FAR`;
- there is at least one such sample;
- no sample in that primary row is certified COMM or LOC.

If this holds, the next gate is the already-required highest-grid `dt/2` confirmation; it is not a mechanism theorem or continuum-convergence theorem.

### STOP/PARK

The filtered near/far mechanism is stopped/parked for promotion if the primary row contains a certified COMM/LOC outcome, or if it fails to provide a comparable covered independently certified FAR row under the frozen rules.

Other ladder rows are still reported in full. A different post-hoc row cannot replace the primary `(16,0.125)` row to rescue the GO decision. If a secondary row is interesting while the primary gate fails, record it as diagnostic evidence only.

## Artifact provenance and durable evidence

Every recovered source artifact must be checked by exact id/name/digest before use. Workflow outputs are revision-specific evidence.

The user has explicitly allowed pushing the contents of the resulting Actions ZIP artifacts into the feature branch when useful for durable review. If this is done, only exact generated JSON/TXT result files are committed; the ZIP container itself is not treated as mathematical evidence beyond its recorded digest.

## Forbidden shortcuts

Do not:

- use E4c64;
- change the R0 threshold;
- change the filter ladder;
- change calibration bins or epsilons;
- fill B3 after seeing E4c;
- use `A_F` as a residual winner score;
- choose a new primary row after seeing E4c;
- identify numerical agreement with a continuum theorem;
- claim singularity, regularity, or Clay A/B/C/D.
