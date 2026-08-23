# STATUS — 2026-08-23

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

研究側 Stage 9(NS の未解決数学そのもの)。commissioned 済みの decision theorem は
**Scope-B `β_v` endpoint-pinning decision** —
[`docs/gates/STAGE9_DECISION_SELECTION_2026-08-23.md`](docs/gates/STAGE9_DECISION_SELECTION_2026-08-23.md)
に statement・kill/survive 基準・failcase 監査・不採用理由・継承義務を固定。record-only。

形式側の残作業は非ブロッキング(uniform energy、maximal trajectory、classical regularity、
edge 5 Clay 転送)であり、Stage-9 の具体定理が要求するまで着手しない。
