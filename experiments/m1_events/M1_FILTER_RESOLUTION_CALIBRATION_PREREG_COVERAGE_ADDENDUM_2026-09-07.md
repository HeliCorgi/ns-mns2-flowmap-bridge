# M-1 filter-resolution calibration coverage addendum — 2026-09-07

**Status:** committed before any manufactured calibration execution.

The fixed geometry in `M1_FILTER_RESOLUTION_CALIBRATION_PREREG_2026-09-06.md` does not populate every preregistered `ell/dx` bin on the coarse calibration grids. This is determined algebraically from the already-fixed grid/radius/sigma ladder, before observing any manufactured calibration value.

In particular, with

```text
N in {64,96,128}
R in {pi/12, pi/6, pi/3}
sigma in {1/8,1/4}
ell = sigma R
dx = 2pi/N
```

no coarse calibration cell lies in

```text
B3: 3 <= ell/dx < 4.
```

This addendum freezes the treatment of any empty calibration bin before execution:

```text
If a bin has zero manufactured calibration cells,
its epsilon values are UNAVAILABLE / NO_CALIBRATION_COVERAGE.
```

Consequences:

- do **not** interpret an empty-bin `epsilon = null` as zero error;
- do **not** borrow the envelope from B2 or B4;
- do **not** interpolate an epsilon across neighboring bins;
- do **not** add a new manufactured radius or sigma after seeing calibration results;
- any production sample whose `ell/dx` lies in an uncovered bin is `NUMERICALLY_UNCERTIFIED_RESOLUTION` for mechanism-promotion purposes.

The production sample may still be reported descriptively, but its FAR/COMM/LOC label cannot count toward the cross-datum GO rule.

All nonempty-bin envelope definitions and margin rules remain exactly those preregistered previously. This addendum intentionally accepts the possibility that the calibration will be too sparse to certify a production ladder; if so, that is evidence against promotion of the current numerical decomposition rather than a reason to tune the calibration after the fact.