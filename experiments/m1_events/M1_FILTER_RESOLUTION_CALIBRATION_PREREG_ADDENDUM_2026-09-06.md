# M-1 filter-resolution calibration preregistration addendum — 2026-09-06

**Status:** committed before any manufactured calibration execution.

This addendum removes one otherwise discretionary phrase from the parent preregistration: a finite N=160/N=192 disagreement will **not** be called `grossly inconsistent` by a threshold selected after seeing the calibration.

For execution, a manufactured cell is `REFERENCE_UNSTABLE` only if a required reference quantity is non-finite, its diffusion denominator `P` is non-positive/non-finite, or the required ladder geometry is absent. Every finite N=160/N=192 disagreement, however large, is retained through the already-preregistered additive reference penalty

```text
|q_N - q_192| + |q_160 - q_192|.
```

Thus a poor reference pair automatically broadens the empirical envelope rather than being censored by an unregistered percentage. No calibration cell is discarded merely because its finite reference disagreement is inconveniently large.

All other definitions, bins, quantities and production margin rules in `M1_FILTER_RESOLUTION_CALIBRATION_PREREG_2026-09-06.md` are unchanged.