# STATUS — 2026-09-04 (第19セッション: 初の proof session まで反映 — ONE-SUBLEMMA: T-VAR)

## 2026-09-01/02 数学監査パス + FREEZE REVIEW ROUND 3/4 + Stage-9 decisions(すべて執行済み)

corpus 全体の数学監査(8 finder → 敵対的検証 → 統合)で 15 件の欠陥を確定
(major 2 / minor 7 / nit 6)。凍結 gate 文書には erratum を追記(silent repair なし)、
kill table への修正は F37–F43 として queue、live 文書は直接修正。major 2 件:
B6 の `(H2) ⟹ (H1)` は距離節削除後は偽(F37)、B2 (T3) の「Scope A で空」は
`ρ_T = γ` 枝でのみ確立(F38)。

同日、ユーザー裁定により **FREEZE REVIEW ROUND 3 を執行**
([`docs/gates/FREEZE_REVIEW_3_2026-09-01.md`](docs/gates/FREEZE_REVIEW_3_2026-09-01.md)):
F37–F43・P1–P7・Seregin row-(i) を個別裁定(全 ADOPT、P1/P2/P3 は修正裁定)、kill table に
annotation **C0–C14** + **post-round-3 frontier** を執行。**C0: (Γ-DEP) は十分条件として
のみ引用**。frontier: Scope-A exhaustiveness は `ρ_T = γ` 枝のみ、Scope B で B2 UNKILLED。
BH YELLOW-RED・(T-c) OPEN・CAP なし・Clay 主張なしは不変。**定理・ruling は動いていない**。

**D-3 preprint は特定・一次 triage 済み(2026-09-02)**: arXiv:2606.07869v1(Shahmurov、
axisym-with-swirl 無条件大域正則性を主張、99頁)をユーザー提供 PDF で全文一次読解し、
gap-finding を敵対的に検証。**変分核心(strict bridge の no-saturator 論法: dilation 曲線が
solution-generated 制約と zero-ledger 集合の双方を離脱、制約適格性も退化)と exhaustion 層
(ledger 4成分が定量未定義で (B) 終結の減少量が不存在)に load-bearing gap を確定**。
正しさ未確立、どこにも不使用、**branch 終了イベントは不発火**(再点検トリガー登録済み)。
詳細: [`docs/gates/D3_TRIAGE_2606_07869_2026-09-02.md`](docs/gates/D3_TRIAGE_2606_07869_2026-09-02.md)。

外部 record **(EXT-ΓDEP-1)**(ChatGPT 側、ユーザー経由で逐語受領)を import・監査
([`docs/gates/EXT_GAMMADEP_DECISION_2026-09-01.md`](docs/gates/EXT_GAMMADEP_DECISION_2026-09-01.md)、
snapshot レベルで PASS): `Γ-DEP = UNDERDETERMINED`、smooth div-free snapshot counterprofile
により **静的ルートは閉鎖**(証明は NS 時間発展を消費する必要)、operative 文は
(Γ-DEP)_fld(`c_* ∈ (0,c₀)`)、(Γ-OSC) は最直接の**十分**条件(必要性未証明)。
counterprofile は今後の Γ-depletion 型仮説の**恒久テストケース**として保存。

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

**2026-09-02(第2セッション、ユーザー commission): T-SEL bridge の Lean 形式化を執行**
([`docs/formal/TSEL_BRIDGE_FORMALIZATION_2026-09-02.md`](docs/formal/TSEL_BRIDGE_FORMALIZATION_2026-09-02.md))。
SEL-1〜SEL-10 の全10補題が Lean artifact 化:
**証明済み** = SEL-6(Grönwall–Bellman 積分形、新規独立インフラ)、SEL-2(decoded
embedding、明示定数つき定量形 `sup + gradSup ≤ C_emb‖f‖`)、SEL-7 の消費部
(連続性・可積分性・Q 単調性)、SEL-8(実性)、SEL-9(ladder 仮定つき指数 carrier
bound、ν-free)、SEL-10(uniqueness transfer + sSup/BddAbove plug discharge)、
および条件付き連鎖 **N0→N1→N2→N3**(`r3TSel_conditional_globalContinuation`)。
**陳述のみ(OPEN、無主張、公理化なし)** = head N0(`R3TSelGradientBound`/`R3TSelHead`
— **proof search は commission により未着手**)、SEL-4 Kato–Ponce、SEL-5 積分形 H³
ladder、SEL-3 内部平滑化節、SEL-1 古典ノルム同値節(いずれも明示仮定 Prop)。
フルゲート PASS(8772 jobs)、公理監査は新定理21件すべて標準3公理のみ。

**2026-09-02(第3セッション、ユーザー commission): bridge 放電ステップを執行 —
SEL-1 と SEL-4 を完全証明**
([`docs/formal/TSEL_BRIDGE_DISCHARGE_2026-09-02.md`](docs/formal/TSEL_BRIDGE_DISCHARGE_2026-09-02.md))。
**SEL-1**: 古典 Sobolev 同値性 `r3TSel_classicalSobolevComparability`(明示定数
c₁ = 1/81, c₂ = 27(2π)⁶; Schwartz core、iterated line-derivative Fourier 計算+
Schwartz Plancherel+方向タプル展開)。**SEL-4**: BKM 微分タプル交換子
`r3TSel_katoPonceCommutator`(明示定数 93(2π)³)— 監査記録 SS-6 自身の D^α 形で
述べ直して証明(sharp fractional J³ Kato–Ponce は鎖のどこにも消費されず無主張の
まま; 途中で Fourier-at-zero 部分積分・by-parts Gagliardo–Nirenberg 四次補間
`r3TSel_gn_quartic`・微分交換(C² 対称性、解析性不要)等の新基盤を証明)。
**Ladder(SEL-5)Prop に実データ仮定 `IsR3RealVelocity u0` を追加**(輸送消去は実
場を要求; admissible データでは SEL-8 が供給、下流連鎖は不変)。**SEL-3/SEL-5 は
未証明のまま OPEN**(モリファイド・エネルギー法+Friedrichs 交換子+SEL-4 の
mollified 場への拡張という放電経路と、検証済みの行き止まりを放電 record §4 に
記録)。フルゲート PASS(8775 jobs)、公理監査標準。head N0 は不変・未着手。

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

## 研究側の経過(Stage 9 → round-4 park)

研究側 Stage 9(NS の未解決数学そのもの)。最初の decision theorem
(**Scope-B `β_v` endpoint-pinning decision**,
[選定記録](docs/gates/STAGE9_DECISION_SELECTION_2026-08-23.md))は
**実行・決着済み: `YES (CONSISTENT)`** —
[`docs/gates/BH_BETAV_ENDPOINT_PINNING_2026-08-23.md`](docs/gates/BH_BETAV_ENDPOINT_PINNING_2026-08-23.md)。

凍結された scope-free 行は **Γ 飽和の位置を一切決めない**ため、中間肢 `β_v ∈ (α,γ)` を
排除できない。明示的 witness `W★` (`γ=3/5, α=9/20, β_v=1/2`)が全行を通過し、その族は
`S_blob` 全体に射影する。閉じ手は3形(round-3 C0): **(Γ-DEP)**(十分条件としてのみ引用)、
(SB-ANCH) の outright 証明(前提としては循環で不可)、memberwise 二分法。
**指数算術の無矛盾性は解の存在ではない**。BH は YELLOW-RED、B2 は Scope B で UNKILLED、
(T-c) は OPEN のまま。map への反映は round 3 で執行済み(C0–C14 + post-round-3 frontier)。

**Γ-OSC feasibility decision: 実行・決着済み(2026-09-02)= `VIOLATED`**
([`docs/gates/GAMMA_OSC_FEASIBILITY_2026-09-02.md`](docs/gates/GAMMA_OSC_FEASIBILITY_2026-09-02.md))。
frozen B2 は既知十分 drift 条件を一つも imply せず(implied 領域は正確に空、主要 cap は強制発散)、
frozen 両立の明示的族が全最弱段を τ-uniform に破る。既知機構ルートは frozen scope で閉鎖
(SSŠZ/SVZ/Wu の反例床 + `(ln N)^{−p}` 閾値)。D-1/D-2 放電。C0-clean(¬(Γ-OSC)/¬(Γ-DEP) は主張しない)。

**第4回 freeze review 執行済み(2026-09-02、ユーザー裁定)**: P1–P6 全 ADOPT、Γ-OSC
`VIOLATED` を正確 scope で map に反映(kill table D0–D7 + Post-round-4 frontier)。
**BH / Γ-depletion branch は active lane として終了・PARK**(「未解決」≠「既知機構の枯渇」を
明記: B2 UNKILLED・中間肢 open・(Γ-OSC)/(Γ-DEP) open のまま。尽きたのは in-house 既知機構の
3層在庫。BH verdict は park 時点で YELLOW-RED に凍結。un-park は登録トリガー経由の
freeze review 裁定のみ)。D-3 / Seregin は standing passive watch register に分離
([`LITERATURE_WATCH_REGISTER_2026-09-02.md`](docs/gates/LITERATURE_WATCH_REGISTER_2026-09-02.md))。
D-3(arXiv:2606.07869)は triage 済み: load-bearing gap 確定、不使用、CAP 不発火。

## 2026-09-02(後刻): M-1 保留 + Stage-9 Reverse-Gap Audit 実行済み

M-1 はユーザー指示により**保留**(数値 lane は破棄せず・未着手)。代わりに
**Stage-9 Reverse-Gap Audit** を1回限りの sanctioned bounded analysis として実行
([`docs/gates/STAGE9_REVERSE_GAP_AUDIT_2026-09-02.md`](docs/gates/STAGE9_REVERSE_GAP_AUDIT_2026-09-02.md)、
RECORD-ONLY — verdict/frontier/park 不変更)。Lean 継続インターフェイスの plug spec を
ソースから抽出、3レーン19候補を反例先行で裁定(18生存・1 banned)、K12 複合体を再検証
(EP-1〜EP-8 の erratum 提案、うち2件は真正の printed-statement defect)。
**選定定理 T-SEL = L_a: `∫₀^{T′}‖∇U‖_{L∞}ds ≤ G(T;ν,‖u₀‖)`**(dependency chain
N0→N3 完全明記。bridge は既知数学10補題 SEL-1〜10、head N0 は OPEN・Clay 級)。
→ **bridge 形式化は第2セッション、SEL-1/SEL-4 の放電は第3セッションで執行済み**
(上の Formal frontier 節参照)。**head N0 の proof search は未 commission・未着手の
まま**。残 bridge 義務は SEL-3/SEL-5 のみ(経路 = 放電 record §4)。

## 2026-09-02(第4セッション): SEL-3/SEL-5 保留 + T-SEL head reduction audit 実行済み

ユーザー指示により **SEL-3/SEL-5 の Lean 実装は保留**(既知数学の formalization debt として
carry; `R3TSelH3Ladder` は研究上の未知命題として扱わない。放電経路=放電 record §4 は
再開時の拘束プランとして不変)。**N0 の直接 proof search は引き続き未 commission**。
代わりに **T-SEL head reduction audit** を RECORD-ONLY で実行
([`docs/gates/TSEL_HEAD_REDUCTION_AUDIT_2026-09-02.md`](docs/gates/TSEL_HEAD_REDUCTION_AUDIT_2026-09-02.md)、
Lean 無変更): ノルム軸は崩壊(fence 6 行 — subcritical sup-norm は古典問題と EQUIVALENT、
critical は既知の壁、supercritical は橋なし)、構造的 head 7 本を生成(幾何/スペクトル/
分布形の3レーン)し、反例バッテリー(scaling・frozen-B2 算術・Type-I・multi-scale・
u_τ/𝒱 guard・FC-086)を証明探索より先に実行 — **7本全 SURVIVE、全て正しい両側 polarity**。
**選定 head: H-SEL = HR-5(reverse-interpolation / anti-intermittency head)**
`‖∇U(t)‖_∞ ≤ Q₀(T;ν,‖u0‖)(1+‖∇U(t)‖_{L²}^{4/3})` — N0 への橋は既知2 arrow
(energy equality [Lean debt EB-1・未 commission] + Hölder)で証明済み Lean 連鎖に着地。
frozen window は class-wide に rate `τ^{−(5α−γ)/3}` で violate(最鋭 margin)、Tao averaged
blow-up は類似形を violate(証明は exact-NS 構造を消費する必要 — FC-086 の位置特定)、
反証 observable はスカラー比 `Q₅(t)` 1本。次点(C0): HR-1(渦度方向 coherence head)。
**H-SEL への着手(P-1 文献一次 sweep → P-2 数値比プローブ → P-3 解析的反証試行、
いずれも証明探索より先)は各々ユーザー commission を要する。** 引用は全て [H]
(一次 fetch 前・不消費、debts V-1…V-6)。

**第5セッション(ユーザー commission、one-shot): H-SEL statement correction audit
実行済み**(同 record §9 に追記、原文は注記つきで保存)。**EH-1**: energy equality
だけで N0 に閉じる power family の正確な endpoint は **p = 2**(p ≤ 2 は閉じる —
p = 2 は Hölder 不要で直接、p > 2 は enstrophy time-spike モデルで閉じない)。
旧 print「4/3 が最大」は誤り(不要な Hölder 分割由来の false superlative)。
4/3 head ⟹ p=2 head なので修正は「energy で閉じる最弱メンバー」への移動 =
selection 保存・statement 改善。**operative H-SEL:
`‖∇U(t)‖_∞ ≤ Q₀(T;ν,‖u₀‖)(1+‖∇U(t)‖_{L²}²)`**(橋 = EB-1 + 直接積分、
`G = Q₀(T+‖u₀‖²/2ν)`、scaling λ² vs λ¹)。**EH-2**: reverse-GN 読み
(`‖∇³U‖₂` の上界主張)は不等式の論理方向逆転で**撤回**(反例モデル
`N^{−1}sin(Nx₁)φ`; anti-intermittency 解釈は heuristic に降格)。修正版で
バッテリー再実行: S_blob は class-wide rate `τ^{−(2α−γ)}`(≥ γ/3; 「最鋭 margin」
superlative は撤回 — HR-1 の `τ^{−α/2}` 以上、`α = 2γ/3` 縁で非狭義)、Type-I
`(T−t)^{−1/2}`、Tao averaged 類似形 `N^{1/2}`(exact-NS 構造消費の要請は不変)、
multi-scale 不変 — **全 polarity PASS。ランキング再計算(HR-1/HR-3 再確認、
120/60/45…)、選定再確認: H-SEL(p = 2 形)、次点 HR-1。** Lean 無変更・proof
search なし・文献 fetch なし(V-1…V-6 未放電)。

**第6セッション(ユーザー commission): P-1 = H-SEL 一次文献 sweep 実行済み —
判定: H-SEL SURVIVES(降格なし・棄却なし)、P-2 進行可**
([`docs/gates/HSEL_P1_LITERATURE_SWEEP_2026-09-02.md`](docs/gates/HSEL_P1_LITERATURE_SWEEP_2026-09-02.md)、
4並列一次検証レーン+main-loop 裁定、RECORD-ONLY)。**降格チェック**: family の
どのメンバー(scale-invariant p=4 含む)も瞬時形では未証明 — 既知フロンティアは
FGT 時間平均 `⟨‖∇u‖∞^{1/2}⟩`(必要指数1に対し 1/2)+ historical analyticity-radius
換算 p=5 のみ。同一形の既知仮説なし(最近接 architecture 前例 = Gibbon et al.
Nonlinearity 27 (2014) regime-I — novelty 主張時は要引用)。**棄却チェック**:
反例探索2レーン独立で空、worst-case 数値(Kang–Yun–Protas `ℰ₀^{3/2}`、depletion)は
支持的。**証明経路制約3件を命名**: C-1(Lu–Doering maximizer が p<4 を kinematic に
偽にする — 証明は dynamical 必須)、C-2(Palasek arXiv:2509.18595 — Q₀ の subcritical
依存は本質的)、C-3(Tao averaged cascade は p<5/2 を violate — energy+bilinear では
不可、exact-NS 構造必須)。**HR-1/HR-3 の plug-in を verbatim 検証**(V-1/V-3/V-5
放電): HR-1 は BdVB DIE 15 (2002)(β=1/2・定数任意)に re-base(CF 1993 は
Lipschitz 限定で NEAR-MISS; 局所化 sub-debt V-1′)、HR-3 は BFG ARMA 231 (2019)
Thm 19(仮説は印字形より弱い — **HR-3′ 弱形 restatement 提案**; Albritton–Bradshaw
の energy-homogeneity 注意も記録)。BKM の NS remark を一次 [V] 化。ランキング
再確認(120/60/45、HR-2/4/7 は scope 外で不変)。**P-2(`Q₅(t)` 数値プローブ)
commission はユーザー行為。proof search(H-SEL/N0)は引き続き未 commission。**

**第7セッション(ユーザー commission): H-SEL quantifier/falsification audit 実行済み —
operative head を norm-uniform 形 `H-SEL^nu` に確定**
([`docs/gates/HSEL_QUANTIFIER_AUDIT_2026-09-02.md`](docs/gates/HSEL_QUANTIFIER_AUDIT_2026-09-02.md)、
RECORD-ONLY、Lean は読み取りのみ)。**EQ-1/2**: 従来表記 `Q₀(T;ν,‖u₀‖)` は
datum-specific 形のみを主張(記法 ruling)。Lean N0(`R3TSelGradientBound`)は
verbatim で datum-specific(∃G は (ν,u0,T) 固定後)。**EQ-3**: 連鎖 N0→N3 は ds で
十分、nu ⟹ ds は自明、**ds ⟹ nu は OPEN**(非コンパクト H³ 球上の uniform
boundedness/effectivity 問題)。**EQ-4**: ds の反証 certificate は検証済み blow-up
certificate と同値(両方向)— 独立反証不能、単一軌道 Q₅ は necessary-signature 役のみ。
**EQ-5**: nu の反証 certificate = 固定 (ν,T,M) の norm-bounded admissible 族で
`sup_t Q₅^{(k)} → ∞`(各メンバーは大域滑らかで可; theorem-level 反証は
non-uniformity 定理 = Palasek/C-2 隣接で Clay 択一に中立 — 非対称性を明記)。
**EQ-6**: nu は既存 Lean lifespan `T₀(ν,M)` までは既知機械で成立(非自明性チェック;
open content = `T₀` を越える horizon 延長)。**EQ-7 再裁定: operative research head =
`H-SEL^nu`**(ds は連鎖十分な fallback; falsifiability 採点は nu 読みでのみ正当)。
**EQ-8**: roster 全体(HR-1/HR-3′…)に同じ nu 読み discipline を固定、ランキング不変。
**P-2 は EQ-5 の族プローブに再定義**(単一軌道プローブではない)。nu もバッテリー
SURVIVES(既録 violator は全て単一軌道; smooth-family 攻撃の既知例なし)。P-2/P-3・
proof search はいずれも未 commission。

**第8セッション(ユーザー commission): P-3 = H-SEL^nu の解析的反証探索を P-2 に
先行して実行済み — 判定: SURVIVES(certificate は現行既知数学から構成不能)**
([`docs/gates/HSEL_P3_FALSIFICATION_SEARCH_2026-09-02.md`](docs/gates/HSEL_P3_FALSIFICATION_SEARCH_2026-09-02.md)、
RECORD-ONLY、Lean 無変更・数値なし・open core への proof search なし)。障害補題4件
([D]-standard): **O-1** small-critical persistence(`‖u₀‖_{Ḣ^{1/2}} ≤ ε₀ν` の部分球では
`sup_t‖u‖_{H³} ≤ Me^{Cε₀²}` — head はそこで既知数学として成立)、**O-2** frequency
quarantine(ball 内で O(1) critical ノルムは `N*(ν,M) = (M/ε₀ν)^{2/5}` 以下でのみ
運搬可能 — 高周波族は自動的に O-1 に落ちる)、**O-3** 固定 horizon への scaling
import 不能(正味 `λ^{−1/2} → 0`)、**O-4** 二重障害(非摂動 seed は成長下界定理と
[0,T] 滑らかさ保証の両方を欠く)。seed 裁定: S-1 高周波 staircase・S-6 small-data
は CLOSED、S-4 shear/strain transient は機構として CLOSED、S-2 multi-scale・
S-3 Lu–Doering 幾何・S-5 O(1) core は UNCONSTRUCTIBLE(depletion 数値も adverse)。
**新発見 S-7 = C²-escape window**: `H³ ↪ C^{1,1/2}` 止まりで ball は `‖∇²u₀‖∞` を
制御しない — `D₀^{(k)} = ‖ω₀/r‖∞ ~ k → ∞` の axisymmetric **no-swirl** 族は ball 内に
構成可能かつ**各メンバーの大域滑らかさが無条件に既知**(Ladyzhenskaya/UY [H]、
debt V-11)で、既知の定量評価は全て D₀ 経由で劣化 — 最鋭の live seed として
**P-2 の priority family に指定**(下界定理は無く certificate ではない)。反証
フロンティアはこの window(+S-5 core、動的到達 LD 幾何)に固定。除外則
(snapshot/averaged/torus/finite-cylinder/Palasek 族)は全て維持。次 = P-2(S-7
priority、V-11 放電を先行)または proof-route selection — いずれも user commission。

**第9セッション(ユーザー commission): S-7 axisymmetric-no-swirl uniformity decision
実行済み — 判定: UNIFORM-BOUND、S-7 は CLOSED、V-11 一次放電**
([`docs/gates/HSEL_S7_UNIFORMITY_DECISION_2026-09-02.md`](docs/gates/HSEL_S7_UNIFORMITY_DECISION_2026-09-02.md)、
RECORD-ONLY、Lean 無変更・数値なし)。**artifact 裁定**: `D₀ = ‖ω₀/r‖∞` 依存は
U–Y 提示の proof artifact — **Ladyzhenskaya 1968(ロシア語原文全23頁 [V-P])は
D₀ を一切使わない**(データ級 (45)–(46) = energy + enstrophy + `ω₀/r ∈ L²`、
stretching 評価 (33) は伝播 L² ノルムを消費)、LMNP 1999 [V-P] は `v₀ ∈ H²` のみ、
measure-data 理論(Feng–Šverák ARMA 215、Gallay–Šverák 2015/2019 [V-P])は L∞ 層を
粘性平滑化で再生成。D₀ が本質的なのは ν-uniform/Euler の p=∞ endpoint のみ。
**一様評価の導出(2経路)**: Route A = LMNP 定数 + Agmon/Kato–Ponce ladder 1段
[D-standard]、Route B = 新 [D] Hardy データ評価 `‖ω₀/r‖_{L^{3,1}} ≤ CM` + L^p 単調性
[V-P] + 検証済み補題 (L*) `‖u^r/r‖∞ ≲ ‖ω/r‖_{L^{3,1}}`(Abidi–Hmidi–Keraani
Math. Ann. 347 (2010) Prop 4.1(i) [V-P])+ stretching Grönwall + bootstrap ⟹
**`sup_{t≤T}Q₅ ≤ C(ν,T,M)`(axisym no-swirl M-ball 上)— H-SEL^nu が成立する
初の large-data 部分クラス**。下界側は否定的に閉鎖(D₀→∞ は何も強制しない)。
**機構ノート**: 閉鎖は ball 制御可能な単調量(η の L^p)経由 = C-3 型の exact-NS
構造で、swirl があると `∂_z(Γ²/r⁴)` source が単調性を壊す(凍結 Γ-lane 知見と整合)。
**閉鎖後のフロンティア = axisym-WITH-swirl C²-escape 族(P-2 retarget 提案・優先)
+ S-5 generic core。** 残債: U–Y 内部(非載荷)、Shirota–Yanagisawa 原文(Route B
のみ載荷)。P-2 / proof-route selection はいずれも user commission 待ち。

**第10セッション(ユーザー commission): H-SEL proof-route selection audit 実行済み —
最小 source-control theorem T-SRC を1本選定**
([`docs/gates/HSEL_PROOF_ROUTE_SELECTION_2026-09-02.md`](docs/gates/HSEL_PROOF_ROUTE_SELECTION_2026-09-02.md)、
RECORD-ONLY、Lean 無変更・数値なし・proof search なし)。no-swirl 機構を4部品に分解:
**C-P1**(Hardy datum 入口 — swirl でも生存; おまけ: `q = u_θ/r = Γ/r²` は ∇u-次
なので `‖q₀‖_{L^p} ≤ C_pM` が p ∈ (2,∞] 全域 ball 一様 — q は C²-escape しない)、
**C-P2**(η の L^p 伝播 — **唯一の破断点**: Hou–Li 変数で source は正確に `∂_z(q²)`
であり、divergence 構造+散逸吸収で必要は quartic budget `∫‖q‖⁴_{L^{2p}}dt` のみ —
source の L∞ は一切不要)、**C-P3**((L*) static 評価 — verbatim 生存)、**C-P4**
(閉鎖 — 条件付き既知級、debt V-12)。無条件閉鎖は Osgood ループで不可能
(= 局所理論; 未解決を誤って証明していないことの確認)。energy は無条件に
`∫‖q‖²_{L²}dt ≤ M²/2ν` を供給。候補 R-1(q-sup)/R-2(sup-L^s)/R-3(budget)/
R-4(negative-Sobolev — 同一 scaling line)/R-5(drift `∫‖u_r/r‖∞` — 言い換え
リスク高、fallback)を反例先行4フィルタで検査(全 polarity PASS)。
**選定: T-SRC(norm-uniform)= `‖u_θ/r‖_{L⁴_t(L⁵∩L⁸)} ≤ Q₀(ν,T,M)`**(族
`4<s₀<6<s₁`、`s₁↓6⁺` で最弱化; Γ が軸近傍で r² より速く L⁴_tL^s 減衰する
time-integrated Γ-depletion 型)。連鎖: T-SRC + energy ⟹ [S1–S2, D] η ⟹
[S3 = AHK (L*)] `sup‖u_r/r‖∞` ⟹ [S4 既知級 + V-12] uniform H³ ⟹ SEL-2 ⟹
**H-SEL^nu|axisym(with swirl — S-7 検証の拡張; 一般クラスは OPEN のまま)**。
反証意味論: 族 budget 発散 = Clay 中立の non-uniformity 定理 / 単一軌道発散 =
axisym blow-up signature(凍結 window 候補は必ず発散 — rate 印字済み)。cross-link
(C0-clean・proposal-level): S3 は Γ-OSC §5.3(iii) の未知量 u_r/r を bound する;
`q = Γ/r²` は (Γ-DEP) 型と隣接(un-park trigger は不発火 — 定理未証明)。
**新 debt V-12**(u_θ/r・u_r/r 型既知判定基準の targeted 一次 sweep — Arrow S4 と
言い換えフィルタに載荷; T-SRC の消費・proof commission に先行必須)。

**第11セッション(ユーザー commission): V-12 targeted primary audit 実行済み —
複合裁定: T-SRC(印字形)は DEMOTED、head を T-SRC′ に re-base、bridge は
VERIFIED(published)、u_r/r arrow は GAP-FOUND(退役)**
([`docs/gates/HSEL_V12_PRIMARY_AUDIT_2026-09-02.md`](docs/gates/HSEL_V12_PRIMARY_AUDIT_2026-09-02.md)、
RECORD-ONLY、2一次レーン)。**(Q3)** Hou–Li (q,η) 系は verbatim 検証 [V-P]
(arXiv:math/0608295 (96)–(98) — 符号・係数とも route record の代数どおり)。
**(Q2)** 決定的発見: **Li–Pan, DCDS 42 (2022), arXiv:2011.03146, Thm 1.3/Cond 1.1
(s=1)** [V-P] — `u_θ/r ∈ L^q_tL^p_x`、`3/p+2/q ≤ 2`、`p>3/2`、**smallness 不要・
有限性のみ** ⟹ regularity(凍結 corpus に無い新定理; K9/L-AX4 は d ≥ 0 止まり)。
T-SRC 印字形(criticality 1.1)は margin 0.9 で内側 — **支配され demote**。
**(Q1)** `sup_t‖u_r/r‖∞ ⟹ H³` は**どこにも出版されていない**(Kubica-II は
該当 corner の3端点全て除外+正部分のみ+swirl 副条件; 定量的 H³ 結論
`C(ν,T,M,K)` を印字する論文もゼロ)— Arrow S4 印字形は文献 GAP、ただし退役で
無害。**(Q4)** 最短 bridge = published 定理1本(Li–Pan)。**re-based head:
T-SRC′ = `‖u_θ/r‖_{L⁴_tL²_x} ≤ Q₀(ν,T,M)`**(critical line `3/p+2/q=2` の
canonical member — energy 恒等式が無条件で与える同一チャネル
`∫‖u_θ/r‖₂²dt ≤ M²/2ν` の時間可積分性を L¹→L² に上げるだけ = 既知無条件数学の
**半 criticality 単位**上、swirl-dissipation channel の時間集中禁止文)。連鎖:
T-SRC′ ⟹ [Li–Pan、残差 V-13(i,ii)] H-SEL^ds|axisym ⟹ [V-13(iii) 定量性、
なければ CFZ/RZ toolkit で有界再構成] H-SEL^nu|axisym。バッテリー: Type-I は
正確に log rate で violate(head は exact scale-critical)、凍結 window の violation
局在は β_v に直結(subcore channel は β_v ≥ 1/2 でのみ発散; core 包絡は発散を
許すが強制せず — **class-wide kill は不成立と確認**)。**提案(record-only)**:
P-LP(Li–Pan の解レベル β_v–budget tie → watch/freeze-review; un-park trigger
不発火)、Shahmurov arXiv:2605.01875/2605.09797 の watch routing(D-3 と同著者)。
**V-12 放電・新 debt V-13**(Li–Pan の還元節・等号端点・証明定量性 — nu 層の
消費と proof commission に先行必須)。

**第12セッション(ユーザー commission): V-13 放電 — 判定: QUANTITATIVE-BRIDGE**
([`docs/gates/HSEL_V13_DISCHARGE_2026-09-02.md`](docs/gates/HSEL_V13_DISCHARGE_2026-09-02.md)、
RECORD-ONLY、一次深読1レーン+main-loop 再導出)。**(i)** pure NS 還元はクリーン
(`h₀ ≡ 0, ρ₀ ≡ 0` を排除する評価は皆無; `μ = 1` 正規化 — 一般 ν は scaling
`(T,M,M′,Q) ↦ (νT, ν⁻¹M, ν⁻¹M′, ν⁻³Q)` で復元)。**(ii)** `s=1, (q,p)=(4,2)`
等号端点は**証明の native case**(Young が生む Grönwall 指数 `2p/((1+s)p−3)` が
そこで正確に 4; 非厳密 `≤` 印字どおり; 除外は `p = 3/(1+s)` のみ = smallness 枝;
区間分割不要)。**(iii)** 証明は端から端まで定量的(明示的 energy/Grönwall 連鎖で
`H^m` bound を**証明**; compactness・矛盾法・BKM 委譲なし; F = 明示的二重指数塔)。
**唯一の実質的 carry: 暗黙 datum `M′ = ‖ru₀^θ‖_{L∞}`**(Lemma 3.1(i) と s=1 の
J-step (3.22) が消費; swirl torus 族で `Γ₀ ≲ MR^{1/2} → ∞` — H³-ball 非一様の
far-field-weight escape window であることを main-loop 検証; 凍結 corpus の class
datum `Γ₀` そのもの)。**EV-1 量化子精密化**: T-SRC′ の定数は `Q₀(ν,T,M,M′)`、
nu 層は2パラメタ球 `(M,M′)` 上の一様性(per-datum ds は無制限)。**T-SRC′ →
H-SEL|axisym の下流連鎖は published + quantitative で完全検証済み — 系譜で初めて
「開いているのは head そのものだけ」の状態に到達。** 改良機会(J-step の Γ₀ 消費
回避 ⟹ M-only 一様性 — 有界な新作業、未 commission)を記録。次 = P-2(観測量
確定: Q₅・budget・時間プロファイル h(t))→ T-SRC′ proof commissioning → P-LP/
Shahmurov watch 裁定 — いずれも user commission。

**第13セッション(ユーザー commission): T-SRC′ temporal-spike mechanism audit
実行済み — T-SRC′ は単一の spike-exclusion lemma に縮約可能(YES)、stop rule
発火で axisym lane 停止・general 側へ復帰**
([`docs/gates/HSEL_TSPK_MECHANISM_AUDIT_2026-09-02.md`](docs/gates/HSEL_TSPK_MECHANISM_AUDIT_2026-09-02.md)、
RECORD-ONLY、main-loop 導出 [D]、Lean/数値/proof search なし)。**正確な恒等式**:
`h′ = −2νD − 4S`(D = ‖∇q‖₂² + 軸トレース ≥ 0、S = ∫(u_r/r)q²dx — h を成長させ
うるのは inflow spin-up のみ)。機構表: M-A 恒等式 CLOSES、M-B 片側 h′ 単独
DEAD-END、M-C 高さ–寿命は減衰側 CLOSES(普遍包絡 `h ≤ 1/(κΔt+1/h₀)`)、
**M-D CLOSES = エンジン**: 外側分割(u_θ = rq)+ スライスごと 2D GN(軸 log
回避)で `D ≥ c·h²/M²` を証明 [D] ⟹ `h′ ≤ −κh² + 4S₋`(κ = 2νc/M²)、M-E
(Γ-max)は未使用補助 — **縮約は M′ 不要**、M-F stretching 構造 SURVIVES
(双対形 `S = ⟨ψ₁,∂_z(q²)⟩`; **非荷重版 ∫∫(u_r/r)u_θ² は energy 恒等式で無料**
— open content は正確に r^{−4} 荷重 + Γ-OSC §5.3(iii) の unsigned u_r)。
**縮約(証明済み [D])**: `κ∫h²dt ≤ h(0) + 4𝔖₋`、h(0) ≤ CM² ball 一様 ⟹
**T-SPK(OPEN)**: `𝔖₋ = ∫∫(u_r/r)₋q²dxdt ≤ Q₀(ν,T,M,M′)` ⟹ T-SRC′ ⟹
H-SEL|axisym — 単調・符号局在のスカラー1個(inflow spin-up work)、凍結 window
全メンバーが profile レベルで violate(K11 により `Γ₀²τ^{−γ−α−β}` 発散)。
**stop rule 裁定**: architecture は一般 3D に逐語転送可能(`E ≤ ‖u‖₂‖Δu‖₂` ⟹
production budget ⟹ `E ∈ L²_t` ⟹ `u ∈ L⁴_tḢ¹ ↪ L⁴_tL⁶` = Serrin 対 (4,6))
— しかし転送先は **E-2/L_d Serrin 壁そのもの**(fence 分類・不適格)。
**構造的発見**: 同一の free architecture が swirl channel では壁の内側
(Li–Pan)、full enstrophy では壁の上に着地 — axisym 半単位 vs 一般1単位の
機構レベルの説明; この経路での一般突破には「独自の free L¹_t budget と
sub-wall criterion を持つ部分 enstrophy channel」が必要で、既知構造には無い。
**適格な生存機構は全て axisym-specific ⟹ lane 停止; T-SPK は縮約証明つきで
park; general N0/H-SEL 側へ復帰。** 次の commission は自由 fork(general
channel-search audit / 一般形 P-2 / axisym lane 再開 / freeze-review 裁定 /
Lean 債務再開)— いずれも user act。

**第14セッション(2026-09-03、ユーザー commission): general N0 channel-search
audit 実行済み — 判定: ONE-CHANNEL-SELECTED = 方向微分 channel、候補定理 T-DIR**
([`docs/gates/HSEL_CHANNEL_SEARCH_2026-09-03.md`](docs/gates/HSEL_CHANNEL_SEARCH_2026-09-03.md)、
RECORD-ONLY)。channel 表: Ch-1 strain/vorticity は collapse check で即棄却
(`‖S‖₂² = ½‖∇u‖₂²`)、Ch-2 λ₂⁺ は COERCIVITY ✗(固有値交差で evolution identity
なし — 最近接 miss)、Ch-4 helicity(無符号散逸)・Ch-5 周波数 shell(Besov 壁崩壊
+ **averaging-STABLE = C-3 違反**)・Ch-5′ 局所 enstrophy(CKN 族 + FC-086 圧力
flux)・Ch-6 ω₃ 単独(bridge OPEN — Neustupa–Penel が verbatim "challenging open
problem")は棄却。**選定 Ch-3a: `X_e = ‖∂_e u‖₂²`** — [D] 検証済み構造:
**evolution identity から圧力が完全消滅**(`div ∂_e u = 0`)、production は純
strain 形 `P_e = ∫(∂_e u)ᵀS(∂_e u)dx`、減衰定数は正確に `κ = 2ν/M²`(GN 不要)。
**bridge 一次検証 [V-P]**: native member `∂₃u ∈ L⁴_tL²_x`(正確に臨界)は
smallness 不要の published criterion が2本 — Zhang BMS 7 (2017) Thm 2(window
[1.562,3] ∋ 2、Leray–Hopf)+ Chen–Fang–Zhang MMAS 44 (2021) Thm 1.1(window
(3/2,6]);Wolf 2015 は `∇u₃` を正確に (4,2) で、Chae–Choe 1999 は2成分 ω̃ を
cover;pre-2015 の Kukavica–Ziane window は q = 2 に届かない(post-2015 文献が
閉じた点)。**候補定理 T-DIR**(∃方向・norm-uniform): ∃e ∈ S²:
`∫₀^{T′}‖∂_e u‖⁴_{L²}dt ≤ Q₀(ν,T,M)`;縮約証明 [D]: `κ∫X_e²dt ≤ M² + 2𝔓₋` ⟹
**T-DIR-SPK**: `𝔓₋ = ∫(−∫(∂_e u)ᵀS(∂_e u)dx)₊dt ≤ Q₀`(一方向の圧縮 strain
増幅仕事、圧力消去済み)。連鎖: T-DIR(-SPK) ⟹ [Zhang/CFZ] **一般クラス N0^ds**
⟹ [新 debt V-15: criterion 証明の定量性、nu 層のみ] H-SEL^nu ⟹ Lean N1→N2→N3。
**一般 lane が axisym lane と同じ single-open-link 形に到達 — 一般 certified
class について「開いているのは head だけ」。** T-DIR は HR-7 族の T-SPK
architecture による upgrade。**EC-1**: T-SPK record §4 の「no known structure
supplies one」節は検証により覆り訂正(in-place 注記; 当時の stop ruling 自体は
規則の正しい適用)。バッテリー全 polarity PASS。次 = ① T-DIR 反証バッテリー
(∃e の回転自由度は未検証領域 — 全方向を破る certified 族の探索)→ ② V-15 放電
→ ③ P-2 型プローブ → ④ proof commissioning — いずれも user act。

**第15セッション(ユーザー commission): T-DIR quantifier + adversarial battery
audit 実行済み — 判定: SURVIVES(QUANTIFIER-GAP なし・COUNTERFAMILY なし)**
([`docs/gates/HSEL_TDIR_QUANTIFIER_BATTERY_2026-09-03.md`](docs/gates/HSEL_TDIR_QUANTIFIER_BATTERY_2026-09-03.md)、
RECORD-ONLY、main-loop 導出 [D])。**DQ-1(方向抽出補題)完全閉鎖・定数損失ゼロ**:
`X_e = eᵀG(t)e`(G = 勾配 Gram 行列)と書き、compact horizon 上の `F_T(e)` の
連続性 + S² compact + 単調収束の対角論法で、∃-per-horizon 形から単一固定方向 e*
を同じ Q₀ のまま抽出 — **印字量化子は確認済み・修正不要**(plug は SEL-10 型;
weak-limit/class-match 帳簿は V-15 節へ編入)。**ONB 恒等式検証 [D]**:
`Σᵢ X_{eᵢ} = tr G = ‖∇u‖₂²`、`Σᵢ P_{eᵢ} = −∫ωᵀSω`(`⟨u·∇u,Δu⟩ = ∫ωᵀSω` 経由)。
帰結 = **averaging no-go**: e-一様平均は `∫(E/3)²dt` = E-2/L_d 壁しか与えず、
∃e の回転自由度は energy/stretching averaging では閉じない — head の open content
は「時間的にコヒーレントな等方的臨界集中の排除」(Gram 形
`inf_e ∫(eᵀG(t)e)²dt ≤ Q₀` が正準形)。**バッテリー**: F1 高周波 CLOSED
(O-1∘O-2)、**F2 回転異方性 — kinematic violator は存在**(回転 `diag(g,ε,ε)`
profile が全固定方向を g² レベルで破る)⟹ 規則どおり **exact-NS-dynamics
barrier** として記録(反例に数えず; certified 版は O-4 で構成不能)、F3 LD/
多方向 strain 構成不能、F4 small-data は head を検証する側、F5 Tao guarded
(C-3)、F6 凍結 profile は全方向 violate = polarity PASS、F7 2.5D sanity PASS。
**T-DIR は V-15 へ進行可(commission は user act)。**

**第16セッション(2026-09-04、ユーザー commission): V-15 放電 — 判定:
QUANTITATIVE-BRIDGE、prior art による demote なし**
([`docs/gates/HSEL_V15_DISCHARGE_2026-09-04.md`](docs/gates/HSEL_V15_DISCHARGE_2026-09-04.md)、
RECORD-ONLY、2レーン: 両 bridge 論文の一次深読 + Gram 形 targeted prior-art)。
**(1)** (4,2) は両論文で smallness-free・q=2 非退化(P1 = Zhang BMS 2017 Thm 2、
閉 window [1.562,3]、q=2 での補間指数すべて内部; P2 = Hui Chen–Fang–Zhang MMAS
2021 Thm 1.1、window (3/2,6]、q=2 は非退化中間枝)。ν=1 正規化、復元則
`F(ν,T,M,Q) = unscale F(1,νT,ν⁻¹M,ν^{−3/4}Q)`。**(2) class-match はクリーン —
commission の想定より良い: P2 の定理は H¹ strong solution そのものについて陳述**
— certified solution がそのまま対象、Leray–Hopf 経由不要(CLASS-GAP なし)。
**(3) 定量的・P2 自己完結**: 全ステップ明示的(compactness・矛盾法・外部委譲
なし)、tail-smallness は分割 `N ≤ ⌈(2C₁Q)⁴⌉+1` で定量化 ⟹
`sup_t‖u‖_{H³} ≤ F(ν,T,M,Q)`(F 明示的、Q⁴ の二重指数型)— **しかも M-only:
axisym lane の M′ に相当する追加 datum 入力なし**。P1 は corroboration(終端の
[33] 委譲は未検証 flag、非載荷)。**(4)** 回転 e↦e₃ は定数不変(絶対定数)。
**(5)** DQ-1 は追加仮定ゼロで組み込み(strong-solution 枠組み、SEL-10 型)。
**prior art: NOT-DEMOTED** — `inf_e∫(eᵀGe)²dt ≤ Q₀` と同値・支配する定理は
存在せず(最近接: CFZ/Zhang = pairing consumer; Miller arXiv:2002.02152
Thm 1.6 = 唯一の existential-direction L⁴L² budget 型だが v×ω・conditional —
構造的隣人・variant channel 候補として記録; strain 固有値系は pointwise で
incomparable; small-∂₃u/almost-2D 系は smallness 側の validating relative;
CF は別対象)。**一般 lane の橋は完全検証済み — 開いているのは T-DIR のみ、
M-only の定量的 published 連鎖で N0・Lean assembly まで到達。系譜の最強検証
状態。** 次 = ① P-2 型プローブ(`X_e`・`𝔓₋`・spec G)→ ② T-DIR/T-DIR-SPK
proof commissioning — いずれも user act。

**第17セッション(ユーザー commission): T-DIR-SPK proof-route decomposition
実行済み — 判定: ONE-LEMMA REDUCTION FOUND、T-GRAM 選定**
([`docs/gates/HSEL_TGRAM_DECOMPOSITION_2026-09-04.md`](docs/gates/HSEL_TGRAM_DECOMPOSITION_2026-09-04.md)、
RECORD-ONLY、main-loop 導出 [D])。**構造的収穫**: **Y-1** 行列発展恒等式
`G′(t) = −2νD(t) − 2𝒫(t)`(𝒫 = 生産テンソル `∫(∂ᵢu)ᵀS(∂ⱼu)dx`、trace は古典
enstrophy 恒等式)、**Y-2 = 鍵**: 正準固定方向の free L¹ budget — `ē` =
`∫₀^{T′}G dt` の最小固有ベクトルに対し `∫X_ē dt = λ_min(∫G) ≤ M²/(6ν)` が
**無料**(「固定方向 + free budget」の同時実現 — per-time では不十分という制約を
正準構成で突破)、Y-3: det/異方性汎関数に符号構造なし。**機構裁定**: R1 alignment
depletion は adverse(channel vector は gradient-like で圧縮整列が DNS 的に
generic — 単独 FAILCASE)、R2 CF coherence は open head への route-swap、R3
spectral split(SP-a 生産異方性 × SP-b frame coherence)は両因子 NEW-MATH、
R4 回転率の energy/dissipation 制御は **free level で不可**(rate ~ ‖G′‖/gap は
壁 budget を要し、gap は悪い等方 regime でちょうど消える)。**選定補題 T-GRAM
(OPEN)**: `∫₀^{T′}(−ēᵀ𝒫(t)ē)₊dt ≤ Q₀(ν,T,M)`。証明済み連鎖 [D]: Y-1 を ē 沿いに
積分 + 符号捨て ⟹ `sup_t X_ē ≤ M²+2Q₀`、Y-2 と組んで `∫X_ē²dt ≤
(M²+2Q₀)M²/(6ν)` ⟹ T-DIR(T′ 依存は DQ-1)⟹ V-15 検証済み橋 ⟹ H-SEL^nu ⟹
N0 ⟹ Lean。**一般レベルの architecture が完成: 正準固定方向の free L¹ budget +
証明済み sup-arrow + published 定量橋 — 開いているのは生産 budget 1個。**
注意(印字済み): T-GRAM は specialization(T-DIR より真に強い可能性; probe で
ē が adversarial に悪ければ T-DIR-SPK(∃e) へ fallback)。probe 条項は auto-fire
せず(縮約が見つかったため)。次 = ① T-GRAM observable のプローブ(ē・X_ē(t)・
(−ēᵀ𝒫ē)₊(t)・spec G(t))→ ② T-GRAM proof commissioning — いずれも user act。

**第18セッション(ユーザー commission): T-GRAM specialization stress-test /
probe 実行済み(数値・preregistered・fail-closed・EVIDENCE-GRADE)— 判定:
CANONICAL-ADVERSE、T-GRAM は park、operative head は T-DIR-SPK(∃e) に復帰**
([`docs/gates/HSEL_TGRAM_PROBE_2026-09-04.md`](docs/gates/HSEL_TGRAM_PROBE_2026-09-04.md)、
prereg は実行前 commit `906601f`、solver/結果は `experiments/tgram_probe/`)。
新インフラ: 自前 64³ 擬スペクトル NS ソルバ(numpy のみ、rotational form、
2/3 dealias、RK4)— TG 解析値との energy 一致・機械零 div・粘性減衰一致に加え
**Y-1 行列恒等式 `G′ = −2νD − 2𝒫` を残差 ~3.7×10⁻⁴ で数値検証**(コードと数学の
同時検証)。fail-closed: R2–R4 は V3(tail 3.6–4.8×10⁻⁵ > 10⁻⁵)で verdict 除外。
resolved = {R1 TG: STABLE(R̃ ≡ 1.000 — 三重縮退で E_min = 全球、半ば定義的)、
R5 small-data control: **ADVERSE — R̃ 最大 309・終端 ≈17**(B ≈ 3.3×10⁻² vs
B_all ≈ 1.9×10⁻³ — 絶対値は微小で T-GRAM 自体は成立するが、commissioned な
比テストが発火)}。機構 [D]: Stokes 支配 regime では ē(∫G 固定)と 𝒫 の frame
(datum 固定)が共にデータ凍結で動的混合なし — **正準方向の最適性 margin は
力学が最弱の regime でちょうど非有界**;対照的に非線形4 run(除外3本含む・
診断のみ)は R̃ ≈ 1.00–1.06 で正準方向は near-optimal。**帰結(prereg 規則
どおり)**: T-GRAM park(Y-1/Y-2 は record の定理として存続)、operative head =
**T-DIR-SPK(∃e)**(Y-1 sup-arrow + DQ-1 + V-15 検証済み M-only 橋は ∃e のみ
消費 — 位置は不変)、T-GRAM proof search は不 commission。re-test 提案record 済み
(絶対スケール gate つき比・96³)。次 = ① T-DIR-SPK(∃e) proof commissioning
(反例先行 discipline は系譜全体で充足済み)→ ② 任意の probe re-test —
いずれも user act。

**第19セッション(ユーザー commission): T-DIR-SPK(∃e) の初 proof session
実行済み — 判定: ONE-SUBLEMMA(T-VAR)、commissioned head は re-base**
([`docs/gates/HSEL_TDIRSPK_PROOF_SESSION_2026-09-04.md`](docs/gates/HSEL_TDIRSPK_PROOF_SESSION_2026-09-04.md)、
Lean/数値なし; 証明済み項目は [D] flag、open statement は無主張)。**P-a**: 正確な
再定式化 `½TV₊(X_e) ≤ K(e) ≤ ½TV₊(X_e) + ν∫eᵀDe dt` — **T-DIR-SPK は連鎖が
不要とする方向 H² 散逸 budget を余分に強制**(EH-1 前例により re-base)。
**P-b**: 補題 **T-VAR**(`∃e: ∫(d/dt‖∂_eu‖²)₊dt ≤ Q₀(ν,T,M)` = channel energy の
総上昇 budget)を定義し、**両 arrow を証明**: T-DIR-SPK ⟹ T-VAR ⟹ T-DIR
(`sup X_e ≤ M²+Q₀` ⟹ `∫X_e² ≤ T(M²+Q₀)²`)— **T-VAR が連鎖を閉じる最弱
メンバー**。**P-c**: rise-tensor 形 `T-VAR ⟺ ∃e: ∫(−eᵀRe)₊dt ≤ Q₀/2`
(`R = νD+𝒫 = −½G′`)+ 新 free 恒等式 `∫trR dt = ½(E(0)−E(T′)) ≤ M²/2`
(unbudgeted なのは方向ごとの振動のみ)。**P-d**: free 行列パス補題は**偽**
(回転異方性パス: free budget 全固定で `TV₊ ~ fTg → ∞`)— **barrier を局在化:
証明は「1方向についての Gram frame 振動周波数の NS 力学的 bound」を要する**。
5チェック: (1) 球面最小化は trace/averaging = 壁のみ(即棄却)、(2) `𝒫 ≺ 0` に
障害なし・残資源は R の負錐回転、(3) `G′`/`D⪰0` は P-a/P-c 構造を与えるが free
TV bound なし、(4) coherence + λ₂-整列は良方向を生成し得る(`∂_eu = Se + ½ω×e`)
が open head 2個 ⟹ **ROUTE-SWAP(記録のみ・不採用)**、(5) Miller 親縁
(`ω×e = 2Ae`)・転用なし。**commission の規定により T-VAR が唯一の次 target。**
バッテリー: polarity 強制・回転 kinematic は標準 barrier・small-data 部分クラスは
成立。次 = ① T-VAR proof session(P-c 恒等式・check-4 map・probe インフラが資産)
→ ② 任意の T-VAR 向け probe(要 prereg)— いずれも user act。

## 現在の active lane と次の作業(M-1 は保留中)

**Active lane = SPEC.md の verified nonlinear finite-cylinder axisymmetric-with-swirl
numerical candidate program。次 = milestone M-1(選定済み・未着手)**:
**Hou 2022 no-slip wall-vorticity boundary closure の実装+検証**
(`docs/reports/HOU_WALL_VORTICITY_BOUNDARY_AUDIT_2026-08-13.md` の blocker 解消。
受け入れ条件 = 同文書の要件1–8 + SPEC §8 不変条件。fail-closed stencil rule 適用。
Hou 再現・`R³`・Clay の主張は一切しない)。詳細:
[`FREEZE_REVIEW_4_2026-09-02.md`](docs/gates/FREEZE_REVIEW_4_2026-09-02.md) §5。

形式側の残作業は非ブロッキング(uniform energy、maximal trajectory、classical regularity、
edge 5 Clay 転送)であり、Stage-9 の具体定理が要求するまで着手しない。
