# M-1 E3c near/far R1-R2 result — 2026-09-06

**Classification:** `NUMERICAL OBSERVATION / EVIDENCE-GRADE ONLY`.

This record closes the preregistered same-datum `E3c96` / `E3c128` filtered near/far comparison. It concerns a periodic `T^3` pseudo-spectral experiment only. It is not an `R^3` candidate, not a blow-up result, not a regularity theorem, and not a Clay A/B/C/D claim.

## Revision and workflow provenance

- branch: `numerics/m1-e3c-nearfar-r1r2`;
- PR: #102, `Numerics: run E3c near/far R1-R2 refinement gate`;
- numerical workflow head: `10b55fd43ad34fa8bddf971509311cefdbc13bd5`;
- workflow: `M-1 E3c near-far R1-R2`;
- run id: `34017370158`;
- both R1 jobs and the downstream R2 comparison job completed successfully.

The R1 jobs did **not** recompute the R0 screens. They recovered the accepted R0 artifacts, checked artifact metadata/digest and the exact fail-closed fields, then invoked the already-accepted `nearfar_rescue.py` unchanged.

Accepted R0 sources:

- E3c96: run `34013942287`, artifact `9983371155`, `m1-E3c96-resolution-screen`, digest `sha256:c8775148c3a9d00614fd474561e14f592711efe799e09934382c8f495000815b`, whole-run `max_tail = 3.274744131023e-07`;
- E3c128: run `34015004075`, artifact `9983774115`, `m1-E3c128-resolution-screen`, digest `sha256:9f8dd8f4cb79f3d84cab81701b98d85189c3ae74f3b01d56b51788f44455fc8e`, whole-run `max_tail = 2.845872144398e-09`.

## R1 execution

### E3c96

```text
samples = 36
sampled_max_tail = 3.241168846865e-07
walltime_s = 512.641
```

Artifact:

- name `m1-E3c96-nearfar-rescue`;
- id `9984447543`;
- digest `sha256:445c4cbbb0c9431a2d1bc14cc589b01d06941b733569576b5c0310b02975ada7`.

### E3c128

```text
samples = 36
sampled_max_tail = 2.834145621030e-09
walltime_s = 2182.173
```

Artifact:

- name `m1-E3c128-nearfar-rescue`;
- id `9984844033`;
- digest `sha256:8f0722332854e022c3a0976d015e46ee4a36fda0a0c2158235148ee2b422970e`.

Therefore both R1 diagnostics are revision-qualified descendants of whole-run R0-qualified grids.

## R2 common-time result

R2 artifact:

- name `m1-E3c96-E3c128-nearfar-R2`;
- id `9984845801`;
- digest `sha256:89e3284a6c3e377de9b4d32df38d2bf7b1f846d8e2b3dca38f1affccb3f6b320`.

There are 36 common physical times (`0.0, 0.1, ..., 3.5`). The sampled global enstrophy-growth event is identical at the two resolutions:

```text
E3c96 : t = 0.1 -> 1.8, E = 2059.1878655576575 -> 4681.591249147496
E3c128: t = 0.1 -> 1.8, E = 2059.1878657581206 -> 4681.591072571599
```

Relative growth is `1.2735134212145591` at N=96 and `1.2735133352429708` at N=128.

Across all 36 common times, the threshold-free symmetric relative differences are:

```text
E      max 1.143464942238e-07   mean 3.895394624637e-08
Lambda max 1.797119019246e-02   mean 2.045633324988e-03
s_v    max 9.026332434840e-03   mean 1.024823162380e-03
```

Thus the global event geometry is very stable between these two grids. This is still numerical evidence, not a continuum convergence theorem.

## Yu ladder: categorical and continuous comparison

The 17 common samples with positive **global** enstrophy growth were compared without introducing a post-hoc percentage tolerance.

### `c=16, sigma=0.125`

Categorical result:

```text
17 / 17 exact label agreement
FAR -> FAR: 17
```

Mean symmetric relative differences are approximately `1.6%` for `A_N`, `1.4%` for `A_F`, `1.4%` for `A_C`, `12.2%` for `A_L`, and `3.3%` for `g`. The filtered-budget residual absolute difference has mean `0.00258` and max `0.0293`.

However the Gaussian filter is only

```text
ell/dx: N96  1.127 .. 1.779
ell/dx: N128 1.503 .. 2.373
```

so this exact FAR agreement is not by itself a filter-resolution qualification.

### `c=16, sigma=0.25`

```text
16 / 17 exact label agreement
FAR -> FAR: 16
FAR -> NO_POSITIVE_LOCAL_GROWTH: 1 at t=1.4
```

The filter is better sampled (`ell/dx` about `2.25..3.56` at N=96 and `3.01..4.75` at N=128), but the filtered-budget residual difference has a large single-time maximum `0.9406`. No post-hoc rule is introduced to discard that sample.

### `c=32, sigma=0.125`

Only 28 common times have this ladder row, giving 10 common positive-global-growth samples. The categorical result is exact:

```text
10 / 10 exact label agreement
FAR -> FAR: 7
NO_POSITIVE_LOCAL_GROWTH -> NO_POSITIVE_LOCAL_GROWTH: 3
```

This is the cleanest continuous comparison in the current output. Mean symmetric relative differences are approximately:

```text
A_N 0.294%
A_F 0.172%
A_C 0.238%
g   1.37%
```

with maxima `1.53%`, `0.780%`, `1.17%`, and `13.7%`, respectively. Filter sampling is

```text
ell/dx: N96  2.254 .. 2.941
ell/dx: N128 3.006 .. 3.920
```

and the filtered-budget residual absolute difference has mean `0.00227`, max `0.0338`.

### `c=32, sigma=0.25`

```text
10 / 10 exact label agreement
NO_POSITIVE_LOCAL_GROWTH -> NO_POSITIVE_LOCAL_GROWTH: 10
```

The filter is the best sampled in the ladder (`ell/dx` about `4.51..5.88` at N=96 and `6.01..7.84` at N=128), but this scale does not exhibit positive local filtered growth at the common positive-global-growth samples. Therefore it is not evidence that FAR carries a local positive surplus at this ladder point.

### `c=8`

Both `sigma=0.125` and `sigma=0.25` have one N96 `NEAR_NOT_ABSORBED` sample at `t=0.7` that becomes `FAR` at N=128. The smallest filters are clearly grid-scale in the raw diagnostic (`ell/dx < 1` for part or all of the N=96/N=128 sequence at `sigma=0.125`). No filter-resolution threshold is declared after seeing this fact.

## Decision

The exact decisions at this stage are:

```text
M1-E3c-R1-EXECUTION = PASS
M1-E3c-GLOBAL-GROWTH-EVENT-96/128 = STABLE (numerical observation)
M1-E3c-FAR-CATEGORICAL-STABILITY = PROMISING BUT LADDER-CONDITIONAL
M1-E3c-MECHANISM-PROMOTION = NOT YET
```

The important positive result is that the historical FAR hypothesis survives the clean same-datum refinement at several ladder points, including exact `17/17 FAR->FAR` at `(c,sigma)=(16,0.125)` and exact categorical agreement at `(32,0.125)`.

The important limitation is that the current ladder mixes poorly sampled filters with better sampled filters, while no manufactured/filter-resolution test has yet supplied a preregistered quantitative adequacy or convergence tolerance. One mismatch also remains at `(16,0.25)`, and the best-sampled `(32,0.25)` row has no positive local growth. Consequently this result must not be promoted to a universal FAR mechanism.

This is **not** a STOP decision either: no common positive-growth sample flips FAR to COMM or LOC, and the clean larger-radius row is strongly stable. The correct next step is to preserve this as one-datum evidence, obtain the preregistered second fixed continuum datum (`E4c`), and separately manufacture the filter-resolution/tolerance test before any final mechanism promotion.

## Next work

1. Continue the preregistered R0 order with `E4c64` and `E4c96`.
2. If only one passes, follow the already-fixed E4c ladder to `E4c128`; do not move the tail threshold.
3. Before interpreting a cross-datum near/far agreement as a mechanism verdict, construct the separately justified manufactured/filter-resolution test required by `M1_RESOLUTION_RESCUE_PREREG_2026-09-06.md`.
4. A highest-grid `dt/2` rerun remains mandatory before promotion beyond diagnostic-only status.

## Forbidden promotions

Do not call this a continuum convergence theorem, an `R^3` result, a blow-up indication sufficient for singularity, a universal FAR law, or a Clay result. Do not use E3c64 in this verdict. Do not set a convergence percentage or filter-resolution cutoff after inspecting these outputs.