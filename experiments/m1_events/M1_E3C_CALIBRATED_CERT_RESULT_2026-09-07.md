# M-1 E3c calibrated near/far certification result — 2026-09-07

**Classification:** `NUMERICAL OBSERVATION / FROZEN-CALIBRATION CERTIFICATION ONLY`.

This result applies the independently manufactured and already-frozen filter-resolution envelope to the existing E3c96/E3c128 near/far artifacts. No production tolerance was fitted or relaxed, and no near/far PDE simulation was rerun.

## Exact inputs

Frozen calibration envelope:

- source run `34049373265`;
- artifact `9994071254`;
- digest `sha256:6d6ca58697a1659d814dc5ae9736e105847ebdd690423d5233997f547129506e`.

Production R1 artifacts from run `34017370158`:

- E3c96 artifact `9984447543`, digest `sha256:445c4cbbb0c9431a2d1bc14cc589b01d06941b733569576b5c0310b02975ada7`;
- E3c128 artifact `9984844033`, digest `sha256:8f0722332854e022c3a0976d015e46ee4a36fda0a0c2158235148ee2b422970e`.

Certification workflow:

- `M-1 E3c calibrated near-far certification`;
- run id `34049792061`;
- job id `101531200494`;
- head `f578cda07f9267f0ad9c9e6a90479785b264e717`;
- result **PASS**.

Output artifact:

- `m1-E3c96-E3c128-calibrated-certification`;
- id `9994185333`;
- digest `sha256:f9a7e8eadddbba79ec42f70324854eb3e7066de97edf38856c645c46d9480d26`.

The workflow re-verified the exact source artifact ids/names/digests before applying the calibration.

## Common global-growth samples

Both E3c grids have the same 17 positive-forward global-enstrophy samples:

```text
t = 0.1, 0.2, ..., 1.7
```

These are the samples used for the calibrated two-grid comparison.

## Calibrated categorical result

### `(c,sigma) = (16, 0.125)`

All 17 samples lie in covered calibration bins on both grids and survive every frozen margin test:

```text
17/17: FAR -> FAR
```

Hence

```text
same independently certified FAR = 17
```

This is the cleanest E3c production row and is no longer merely raw string agreement.

### `(16, 0.25)`

```text
10: FAR -> NUMERICALLY_UNCERTIFIED_RESOLUTION
 7: NUMERICALLY_UNCERTIFIED_RESOLUTION -> FAR
```

The loss of two-grid certification is entirely due to the preregistered uncovered B3 interval `3 <= ell/dx < 4`. No adjacent-bin envelope is borrowed.

### `(32, 0.125)`

At the 10 common samples for which this ladder row exists:

```text
7: FAR -> NUMERICALLY_UNCERTIFIED_RESOLUTION
3: NO_POSITIVE_LOCAL_GROWTH -> NUMERICALLY_UNCERTIFIED_RESOLUTION
```

Again the high-grid samples land in uncovered B3, so this row cannot count toward promotion.

### `(32, 0.25)`

```text
10/10: NO_POSITIVE_LOCAL_GROWTH -> NO_POSITIVE_LOCAL_GROWTH
```

This row is numerically stable but is not FAR evidence because the frozen local-growth test does not identify positive local growth.

### `c = 8`

For each `sigma in {0.125, 0.25}`:

```text
15: FAR -> FAR
 1: NEAR_NOT_ABSORBED -> FAR
 1: NO_POSITIVE_LOCAL_GROWTH -> NO_POSITIVE_LOCAL_GROWTH
```

Thus each c=8 row contributes 15 same-grid-pair certified FAR samples while preserving the previously observed near-absorption mismatch rather than deleting it.

## Aggregate certified residual count

Across all ladder rows, counting each `(time,c,sigma)` cell separately:

```text
same certified FAR pairs = 47
same certified COMM pairs = 0
same certified LOC pairs = 0
```

This aggregate count is descriptive only; the rows are not independent statistical trials. The important decision-relevant fact is the existence of a complete covered row `(16,0.125)` with 17/17 independently certified FAR on both resolutions.

## Exact decision

```text
M1-E3c-CALIBRATED-CERT-EXECUTION = PASS
M1-E3c-CALIBRATED-CLEAN-ROW-(16,0.125) = 17/17 FAR/FAR
M1-E3c-CALIBRATED-FAR = YES on covered production rows
M1-E3c-CALIBRATED-B3-ROWS = UNCERTIFIED, as preregistered
M1-E3c-MECHANISM-PROMOTION = NOT YET (second datum + dt/2 still required)
```

The independent calibration therefore **does not kill** the E3c FAR candidate. It sharpens the earlier raw result: some ladder rows become unusable exactly because B3 was intentionally left uncovered, while the strongest `(16,0.125)` row remains fully certified.

## Next gate

The preregistered cross-datum step is now justified:

```text
M1-E4c-R1/R2 + frozen-calibration certification
```

Run the unchanged `nearfar_rescue.py` on the already R0-qualified E4c96/E4c128 pair, compare the same-datum outputs on common physical times, then apply the **same frozen envelope**. Do not add E4c64, change the filter ladder, modify B3, or fit any new tolerance.

If E4c selects the same certified FAR residual on a covered stable row, the numerical program reaches the two-datum spatial/mechanism criterion and should proceed to highest-grid `dt/2` confirmation before any promotion. If E4c selects another residual or cannot be certified, STOP/PARK the current filtered near/far mechanism rather than modifying calibration.

## Claim boundary

This result is numerical evidence under an empirical manufactured-field error envelope. It is not a continuum convergence theorem, does not prove a universal FAR law, does not prove Yu's analytic estimate for this implementation, and does not establish Navier–Stokes blow-up, regularity, or any Clay result.