# STATUS — 2026-08-19

## Formal (Lean) frontier

`R³` operator 層 → projected convection → endpoint-safe mild equation → local existence →
real local solution → explicit lifespan → unrestricted uniqueness → restart/concatenation →
continuation blow-up dichotomy まで定理として閉鎖(8756 jobs green、標準3公理のみ)。
定理依存連鎖と残存 edge は
[`docs/formal/R3_NS_VERTICAL_INTEGRATION_STATUS.md`](docs/formal/R3_NS_VERTICAL_INTEGRATION_STATUS.md)。
canonical maximal trajectory / pointwise limsup 形、pressure reconstruction、Clay への
semantic promotion(5 edges)は未着手。研究側は BH / Type-II 候補問題に復帰。

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

- 3D Navier–Stokes の一般解を得た
- continuum NS の singularity / counterexample を証明した
- Hou late-state state で mechanism を確認した
- production wall-vorticity solver と同一だと主張する

## 次の勝負

1. modal-coordinate bridge v2.3
2. rank/truncation errorを physical-energy metric で測る
3. grid / dt / modal-rank の3軸 convergence
4. continuum limit で tangent-path integral を一様制御できるか監査
