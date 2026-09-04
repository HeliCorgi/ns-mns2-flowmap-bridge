# M1 GPT-side independent Betchov cross-check — 2026-09-04

**Status:** EVIDENCE-GRADE / DIAGNOSTIC ONLY. No repo files modified. The solver/data definitions were independently reimplemented from the public `experiments/m1_events/events.py` conventions. E2b 96^3 was attempted but did not reach the first requested checkpoint within the available runtime; no GPT-side E2b beta value is claimed.

## Observable

Using the exact local Betchov identity

`q + 4 det S = div J_B`,  `q = omega^T S omega`,

define for a region `Omega`

`beta_B(Omega) = (-4 int_Omega det S)/(int_Omega q)`.

Thus `1-beta_B` is the fraction of the net stretching integral supplied by `int div J_B` (with the actual modified enstrophy flux equal to `-J_B`). `beta_B>1` means the Betchov flux term opposes/export-cancels part of the local determinant source; `beta_B<1` means the modified flux `-J_B` converges into the region and supplies part of the net stretching.

Two masks were used: (i) Fable-style intense/middle-strain mask `{lambda_2>0} intersect {|omega|>0.25 Lambda}`; (ii) top 1% of positive `q`. All full-domain checks returned `beta_global=1` to floating precision, validating the integrated identity in the implementation.

## Event medians

| run | GPT beta intense | GPT beta top-q 1% | GPT C1 intense | source/gross intense | flux/gross intense | Fable C1 | Fable C4 | resolution |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| E0 | 1.124 | 0.067 | 0.251 | 0.282 | -0.031 | 0.282 | 0.492 | yes |
| E3 | 0.978 | 0.791 | 0.184 | 0.180 | +0.004 | 0.179 | 0.058 | no |
| E4 | 0.778 | 0.634 | 0.226 | 0.176 | +0.050 | 0.199 | 0.101 | no |
| E2 | 0.569 | 0.613 | 0.129 | 0.073 | +0.055 | 0.081 | -0.042 | no |

`C1_int` is recomputed on the intense mask, so it is not expected to equal Fable's globally reported C1. `source/gross=C1_int*beta_B`, `flux/gross=C1_int*(1-beta_B)`.

## Main finding: the simple event-level source/flux dichotomy does not survive conditioning

E0 (the only fully tail-resolved case) changes character dramatically with localization. Over the broad intense mask its median `beta_B=1.124` (source-dominated, with a small opposing/export flux term), whereas on the top 1% positive-production core its median is only `0.067` (about 93% of the net core stretching is the Betchov divergence contribution). Thus one and the same event is source-dominated on a broad intense region and flux-fed at its hottest production core.

At representative snapshots the top-q localization profile `beta_B(theta)` is:

| run/time | top 0.5% | 1% | 2% | 5% | 10% | 20% | intense mask |
|---|---:|---:|---:|---:|---:|---:|---:|
| E0 / 1.6 | 0.048 | 0.077 | 0.096 | 0.147 | 0.211 | 0.291 | 1.226 |
| E3 / 1.2 | 0.806 | 0.853 | 0.897 | 0.945 | 0.961 | 0.958 | 0.968 |
| E4 / 1.2 | 0.719 | 0.682 | 0.681 | 0.701 | 0.721 | 0.735 | 0.764 |
| E2 / 2.4 | 0.748 | 0.643 | 0.559 | 0.524 | 0.561 | 0.639 | 0.631 |

This is robust enough to reject a mask-free binary label `source-dominated vs flux-dominated` as the new head. The surviving object is a **localization profile** `theta -> beta_B(theta,t)`, not a single event scalar. E0 exhibits a particularly sharp nested structure: a flux-fed production hotspot embedded in a broader source-driven intense region. E3 is source-dominated across scales; E4 and E2 are mixed.

## Pressure-shielding comparison

Comparing the intense-mask `beta_B` ordering against Fable's event-median C4 gives a suggestive but non-universal trend: E0 `(1.124, 0.492)`, E3 `(0.978, 0.058)`, E4 `(0.778, 0.101)`, E2 `(0.569, -0.042)`. Lower beta often accompanies stronger pressure shielding, but E3 is a direct counterexample to a one-parameter law: it is nearly pure local-source by beta while C4 is already near zero. With only E0 resolved, this is not a statistical claim.

Therefore `beta_B` and C4 should be treated as **two independent mechanism coordinates**, not as interchangeable branches. A useful event map is `(gross->net depletion C1, source/flux localization beta_B(theta), pressure shielding C4)`.

## Verdict

**MIXED / DIAGNOSTIC-ONLY.** The exact Betchov decomposition is confirmed numerically and adds genuinely new localization information to the project, but the proposed datum-level `source branch / flux branch` dichotomy is killed by mask dependence. The refined candidate is the nested localization profile `beta_B(theta,t)`. No regularity criterion or sub-wall bound follows yet.

The most decision-relevant next numerical test would preregister `beta_B(theta,t)` on the same E0/E3/E4/E2 family, then obtain a resolved high-Re/tube case (>=128^3) before attempting any analytic promotion. A proof-oriented route would require a free bound on the boundary/divergence contribution or a monotone/sign structure of the beta profile; neither is currently established.
