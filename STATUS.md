# STATUS — 2026-09-01

## 2026-09-01 数学監査パス(erratum 層のみ、map は record-only)

corpus 全体の数学監査(8 finder → 敵対的検証 → 統合)で 15 件の欠陥を確定
(major 2 / minor 7 / nit 6)。**定理・ruling・凍結 verdict はどれも動いていない**。
凍結 gate 文書には erratum を追記(silent repair なし)、kill table への修正は
**F37–F43 として第3回 freeze review へ queue**(row/annotation は未編集)、live 文書
(HANDOFF / formal status / Lean docstring 1件=コメントのみ)は直接修正。major 2 件:
B6 の `(H2) ⟹ (H1)` は距離節削除後は偽(F37)、B2 (T3) の「Scope A で空」は
`ρ_T = γ` 枝でのみ確立(F38)。詳細は
[HANDOFF.md](HANDOFF.md) の「2026-09-01 mathematical audit pass」。

## Formal (Lean) frontier

`R³` operator 層 → projected convection → endpoint-safe mild equation → local existence →
real local solution → explicit lifespan → unrestricted uniqueness → restart/concatenation →
continuation blow-up dichotomy → **decoded 物理速度の意味論** →
**incompressible Navier–Stokes 方程式そのもの** →
**admissible(real / divergence-free / Schwartz)初期データ adapter** まで定理として閉鎖。
`Formal/AxiomAudit.lean` は標準3公理のみ。

現在の意味論の正確な強さ:

- 空間: 成分別 tempered distribution (`𝓢'`)
- 時間: 強 `L²` 値微分、地平線の**内部時刻**のみ(`t = 0` / `t = T` は除く)
- 時間の広がり: **局所**(明示的 lifespan `T₀(ν, ‖u₀‖)`)
- エネルギー: 各時刻で有限(uniform-in-time bound / energy inequality は未証明)
- 圧力: edge 2a の明示的 Helmholtz witness、調和項の差を除いて決定
- 実性: 実データに対し座標側・decoded 側とも各時刻で実

定理依存連鎖と残存 edge は
[`docs/formal/R3_NS_VERTICAL_INTEGRATION_STATUS.md`](docs/formal/R3_NS_VERTICAL_INTEGRATION_STATUS.md)。
Stage-9 readiness audit は
[`docs/formal/STAGE9_READINESS_AUDIT_2026-08-23.md`](docs/formal/STAGE9_READINESS_AUDIT_2026-08-23.md)。

## いま通ってるやつ(数値側)

- conservative LF-WENO7 holomorphic transport: discrete structure / JVP regressionあり
- full holomorphic pilot: PASS on synthetic controls
- matrix-free physical-metric adjoint: PASS on synthetic controls
- adaptive clustered SVD: PASS on manufactured controls
- 4-way projector geometry: PASS on manufactured controls
- temporal onset logic: fail-closed regressionあり
- flow-map amplitude-path bridge: discrete-map positive controls PASS
- path-independence / zero-holonomy: synthetic MNS control PASS

## まだ言っちゃダメなやつ

- 3D Navier–Stokes の一般解を得た / Clay problem を解いた
- global regularity を証明した / blow-up を証明した
- 古典解(pointwise classical solution)を構成した
- continuum NS の singularity / counterexample を証明した
- Hou late-state state で mechanism を確認した
- production wall-vorticity solver と同一だと主張する

## 次の勝負

研究側 Stage 9(NS の未解決数学そのもの)。最初の decision theorem
(**Scope-B `β_v` endpoint-pinning decision**,
[選定記録](docs/gates/STAGE9_DECISION_SELECTION_2026-08-23.md))は
**実行・決着済み: `YES (CONSISTENT)`** —
[`docs/gates/BH_BETAV_ENDPOINT_PINNING_2026-08-23.md`](docs/gates/BH_BETAV_ENDPOINT_PINNING_2026-08-23.md)。

凍結された scope-free 行は **Γ 飽和の位置を一切決めない**ため、中間肢 `β_v ∈ (α,γ)` を
排除できない。明示的 witness `W★` (`γ=3/5, α=9/20, β_v=1/2`)が全行を通過し、その族は
`S_blob` 全体に射影する。閉じるには新規の1定理 **(Γ-DEP)**(core 内での循環枯渇)が必要で、
**(SB-ANCH) は使えない**(それ自体がもう一方の端点と同値)。**指数算術の無矛盾性は解の存在では
ない**。BH は YELLOW-RED、B2 は Scope B で UNKILLED、(T-c) は OPEN のまま。map への影響は
すべて次回 freeze review への **提案**(record-only)。

形式側の残作業は非ブロッキング(uniform energy、maximal trajectory、classical regularity、
edge 5 Clay 転送)であり、Stage-9 の具体定理が要求するまで着手しない。
