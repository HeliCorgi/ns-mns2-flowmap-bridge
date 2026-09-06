# M-1 filter-resolution calibration result — 2026-09-07

**Classification:** `NUMERICAL CALIBRATION RESULT / EMPIRICAL ERROR ENVELOPE ONLY`.

This record executes the independent manufactured calibration preregistered in:

- `M1_FILTER_RESOLUTION_CALIBRATION_PREREG_2026-09-06.md`;
- `M1_FILTER_RESOLUTION_CALIBRATION_PREREG_ADDENDUM_2026-09-06.md`;
- `M1_FILTER_RESOLUTION_CALIBRATION_PREREG_COVERAGE_ADDENDUM_2026-09-07.md`.

No E3c/E4c production snapshot or initializer was used to select the fields, geometry, bins, or envelope rule. This is an empirical diagnostic-discretization calibration, not a rigorous continuum error theorem and not a Clay claim.

## Manufactured execution

Primary workflow: `M-1 filter resolution calibration`, run id `34049061871`.

Three explicit finite divergence-free trigonometric fields `M0/M1/M2` were evaluated at the fixed preregistered geometry on five grids. Every grid job completed successfully and produced 18 finite calibration cells with positive diffusion denominator `P`; manufactured Fourier divergence remained at roundoff level.

Artifacts:

| N | artifact id | SHA-256 digest |
|---:|---:|---|
| 64 | `9993994132` | `sha256:d1f907731ff938cb5841741a44b2b7ea0ce51e838ab72e1abb68225ebf908d16` |
| 96 | `9993989152` | `sha256:2e5666cac45392520e951975baf14fe638cf4083009048a9d61aa95fcaf29ac9` |
| 128 | `9993997487` | `sha256:f5a40bce399f00e898efe1c7c394f1d3fde79e3039865708d632fe0cc178008e` |
| 160 | `9994020260` | `sha256:d37ce9a6578782468d9590d534bbaf3556da30a6fe7f67cc82de743fd046647f` |
| 192 | `9994041502` | `sha256:8fb8f8868855e5439f3ca5de6dcfbe08b0fad33cebe478de177612395d8d845c` |

Example hosted verification at N=160 reported Fourier-divergence maxima

```text
M0 3.391e-15
M1 2.203e-15
M2 3.350e-15
```

and the same sanity gate passed on all five grids.

## Aggregation infrastructure incident

The first aggregate job in run `34049061871` failed before aggregation because that job omitted Python dependency installation:

```text
ModuleNotFoundError: No module named 'numpy'
```

This was an infrastructure error only; all five source-grid artifacts had already completed and were retained unchanged.

A separate rescue workflow installed the declared requirements and recovered the exact five artifacts from run `34049061871` without rerunning or modifying any manufactured grid result.

Rescue workflow:

- name `M-1 filter calibration aggregate rescue`;
- run id `34049373265`;
- job id `101530085033`;
- source head `35a39c2b5372ccc1a44df75f673849ab7a6f1856`;
- result **PASS**.

The rescue verified all five grid JSONs, froze the envelopes, enforced the preregistered empty-bin rule, and uploaded:

- artifact `m1-filter-calibration-envelope`;
- id `9994071254`;
- digest `sha256:6d6ca58697a1659d814dc5ae9736e105847ebdd690423d5233997f547129506e`.

## Frozen empirical envelopes

For each nonempty bin and quantity,

```text
eps_q(B) = max_manufactured ( |q_N - q_192| + |q_160 - q_192| ).
```

The exact frozen values are:

| bin | eps_A_N | eps_g | eps_B_F | eps_B_C | eps_B_L | eps_budget_resid |
|---|---:|---:|---:|---:|---:|---:|
| B0 | `6.8945663460310835e-3` | `3.5413556715919725e-3` | `1.960161040038466e-2` | `3.19599675328297e-5` | `2.6387636755327293e-3` | `2.6851145927342737e-5` |
| B1 | `6.475448975403433e-3` | `8.936244899508949e-4` | `2.4584563268122694e-2` | `2.057052509252255e-5` | `6.695920656003551e-4` | `7.481129326704014e-6` |
| B2 | `6.628136031402332e-3` | `1.023851486348093e-4` | `2.4259403812155134e-2` | `9.872584358694425e-6` | `6.761854101378431e-5` | `5.004442754207722e-8` |
| B3 | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable |
| B4 | `3.881200655061423e-3` | `5.45962783382592e-6` | `1.3268696673768676e-2` | `7.912242151464355e-7` | `3.3276714978824895e-6` | `8.193736753111733e-9` |

The aggregate workflow explicitly passed:

```text
aggregate coverage sanity PASS; B3 intentionally uncovered
```

## Empty-bin decision

The fixed preregistered geometry places no coarse calibration cell in

```text
B3: 3 <= ell/dx < 4.
```

Therefore, exactly as frozen before execution:

```text
B3 = NO_CALIBRATION_COVERAGE.
```

A B3 production sample is `NUMERICALLY_UNCERTIFIED_RESOLUTION`. Its raw diagnostic may be reported, but it cannot count toward mechanism promotion. No neighboring-bin interpolation, envelope borrowing, or post-result geometry extension is allowed.

## Production certification rule now frozen

For a production sample in a covered bin B:

- local growth is positive only when `g >= eps_g(B)`, negative/no-positive only when `g <= -eps_g(B)`, otherwise numerically ambiguous;
- near-field absorption is certified only when `A_N <= 1 - eps_A_N(B)`; non-absorption only when `A_N >= 1 + eps_A_N(B)`; otherwise ambiguous;
- residual scores are the **signed** normalized values
  `b_F = V_far/P`, `b_C = Rcomm/P`, `b_L = Lloc/P`;
- candidate winner `j` is certified only if `b_j > eps_j(B)` and `b_j-b_k > eps_j(B)+eps_k(B)` for every other residual `k`.

`A_F = Vp_far/P` is not the FAR winner score.

When two production grids are compared, a FAR/COMM/LOC agreement counts only if the label is independently margin-certified on both grids.

## Exact decision

```text
M1-FILTER-CALIBRATION-FIVE-GRID-EXECUTION = PASS
M1-FILTER-CALIBRATION-ENVELOPE = FROZEN
M1-FILTER-CALIBRATION-B3-COVERAGE = NO
M1-FILTER-CALIBRATION-RIGOROUS-CONTINUUM-BOUND = NO
```

## Next gate

Apply this frozen envelope mechanically to the already-computed E3c96/E3c128 R1 artifacts before spending another long run on E4c near/far. This is the cheapest decision-relevant test of whether the previously observed raw FAR pattern survives independent numerical certification.

If E3c's relevant positive-growth samples remain consistently certified FAR on both grids, proceed to E4c96/E4c128 R1/R2. If calibration renders the E3c evidence mostly ambiguous/uncovered or certifies a different residual, record that outcome without relaxing the envelope and reconsider/park the current mechanism program.

## Claim boundary

The frozen envelope is an empirical manufactured-field calibration. It does not bound continuum discretization error rigorously, does not prove Yu's estimate for this periodic/Gaussian implementation, and does not establish any singularity or regularity theorem.