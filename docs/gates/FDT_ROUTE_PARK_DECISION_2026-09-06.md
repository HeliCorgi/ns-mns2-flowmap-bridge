# FDT regularity-route park decision — 2026-09-06

**Status: STRATEGIC PARK. PARENT FDT-INJ REMAINS OPEN.**

**Primary ruling:**

- `FDT-DEF-BUDGET` is **not proved false** on Clay-admissible `R^3` data;
- however, as a reduction from already-controlled quantities it has failed the independence test;
- therefore the current frequency/dissipation material-shell route is **PARKED** pending a genuinely new deformation theorem from outside the present chain.

This record follows `FREQUENCY_DISSIPATION_TRANSFER_DECISION_2026-09-05.md`,
`FDT_LH_DECISION_2026-09-05.md`, `FDT_LH_DYN_AFFINE_DECISION_2026-09-06.md`, and
`FDT_MAT_STRUCT_DECISION_2026-09-06.md`.

No global regularity theorem, blow-up theorem, or Clay alternative is proved.

## 1. Exact object that remains

For the low field `v_j=u_{<=j-2}`, let `X_j(t,s,x)` be its flow and `F_j=D_x X_j`. Material and Eulerian frequency covectors are related by `F_j^{-T}`. Thus any two-sided material/Eulerian shell comparison requires control of the singular values of `F_j`.

A convenient distortion functional is

\[
K_j(t,s)=\sup_x\max\{\|F_j(t,s,x)\|,\|F_j(t,s,x)^{-1}\|\}.
\]

The flow equation gives `partial_t F_j=(grad v_j)(t,X_j)F_j`, hence

\[
K_j(t,s)\le\exp\left(\int_s^t\|\nabla v_j(\tau)\|_\infty d\tau\right).
\]

The material/Eulerian bridge is therefore a deformation-gradient problem.

## 2. Scale-criticality

The one-viscous-window low-strain quantity

\[
\mathcal D_j(t)=\int_{t-\tau_j}^t\|\nabla u_{\le j-2}(s)\|_\infty ds,
\qquad \tau_j\asymp(\nu\lambda_j^2)^{-1},
\]

is scale invariant after the corresponding dyadic-index shift. Energy and total dissipation are supercritical. Hence the missing deformation control cannot be obtained as a small high-frequency consequence of those budgets.

## 3. Why mere finiteness is not a reduction

For every compact interval strictly inside a smooth lifespan, `K_j` is finite. A continuation argument instead needs uniform control as a possible first singular time is approached, across the relevant high scales. That is itself a new critical deformation regularity statement. The present FDT chain has not reduced it to an independently finite quantity.

## 4. Accumulated decisions

- static/energy shortcut: killed;
- `FDT-LH-OP = NO`;
- `FDT-LH-DYN-AFF = NO`;
- `FDT-MAT-COMM = YES`;
- `FDT-MAT-BRIDGE-UNIF = NO`;
- `FDT-MAT-STRUCT = NO as stated`.

Every attempt to avoid paying low deformation has failed for a distinct structural reason. The remaining proposal is precisely to control that deformation itself.

## 5. Exact decision

**Mathematical status:** `FDT-DEF-BUDGET` on admissible `R^3` data remains **OPEN**. No valid fixed-Schwartz-datum counterexample has been produced; the affine model is not finite energy.

**Reduction status:** `FDT-DEF-BUDGET-AS-INDEPENDENT-REDUCTION = FAIL` for the present chain. Assuming `int F`, `int ||grad u||_infinity`, Serrin, bounded `H^3`, or an equivalent strain criterion is circular for this purpose.

**Strategic status:** **FDT REGULARITY CROSS-TRACK = PARKED.** This is not a theorem that frequency methods are impossible. It is a portfolio decision to stop spending on this chain unless a genuinely new deformation input appears independently.

## 6. Reopen conditions

Reopen only for a new independent deformation theorem, a genuinely new material continuation theorem, an admissible full-term cancellation identity, or an external result that changes this frontier. Absent one of these, do not build LP/Bony/Piola/paracomposition Lean plumbing.

## 7. Portfolio routing

Return to the repository's declared breakdown-side Clay C/D priority. Re-read `SPEC.md`, `docs/gates/STAGE9_DECISION_SELECTION_2026-08-23.md`, `docs/gates/BH_BETAV_ENDPOINT_PINNING_2026-08-23.md`, and the latest breakdown-side kill table / readiness audit referenced there. Select one **actual-NS dynamical** decision beyond the already settled scope-free exponent arithmetic.

Do not reopen the parked Astra `(q,d)` cone unless a propagated structure simultaneously excludes its remote-pressure and fourth-jet counterfamilies.

## 8. Formalization ruling

No Lean source is added. `FORMAL_SCOPE.md` and `STATUS.md` remain unchanged.
