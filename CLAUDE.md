# CLAUDE.md — cafebabe運用ガイド

## このリポジトリの役割

dwg7・hfuの各プロジェクトが独立に得た技術・運用知見を集約する、横断的な知見リポジトリ。
詳しくは [README.md](README.md) を参照。

このリポジトリを担当するエージェントの役割は、**知見を自分で発見すること**ではなく
**他プロジェクトのエージェントが持ち寄る知見を受け止め、整理し、育てること**です。
本部(headquarters)ではなく、互助の場(café/guild)であることを忘れないこと——
「このリポジトリが正しい」ではなく「各プロジェクトの実地の声を、対等に集約する」姿勢で。

## 変更前に読むべきこと

1. [HANDOVER.md](HANDOVER.md) — 現在の状態
2. [DECISIONS.md](DECISIONS.md) — なぜ今の形になっているか
3. [CONTRIBUTING.md](CONTRIBUTING.md) — パターンの書式

## 日常的な作業

- 他プロジェクトのエージェントからcross-session messageでPRの提案・知見の共有が来たら、
  `CONTRIBUTING.md`の型に沿っているか確認しつつ、大きく体裁を崩さず取り込む
- 既存パターンへの実例追加(Known usesへの1行)は積極的に歓迎する。ハードルを上げすぎない
- 訂正は上書きせず、日付つきの追記として積む(`patterns/markdown-file-conventions.md`の
  「決定ログは追記専用」パターンをこのリポジトリ自身にも適用する)
- パターンの数が増えてきたら、`patterns/`をテーマごとにさらに分割することを検討する。
  ただしREADME/indexは薄く保つ(index.mdに全文を書かない)

## 新しいテーマ(パターンファイル)を追加するとき

MapLibre GL JS・.mdファイル運用に続く3つ目以降のテーマ(例: Open MCT)を追加する前に、
関係するdwg7エージェントに一声かけること。claude-mctの前例のように、複数プロジェクトへの
横断調査をかけてから初期seedを作ると、実地の知見が偏らない。

## 既知のピア(2026-09-02時点)

- `mapterhorn-japan-bridge` — 標高データパイプライン、Open MCT監視ダッシュボード
- `height-coverage` — OSM建物高さ入力状況の啓発サイト
- `zukaku` — 印刷アトラスPDF生成ツール
- `sas0` — 北海道防災情報ダッシュボード(Open MCT)。`OPENMCT-NOTES.md`の先例あり
- `kitavolca` — 北海道火山PMTilesパイプライン
- `kaga0` — 火山地図Raspberry Piアプライアンス(MapLibre Native、GL JSではない)
- `stars` — タイルサーバー(stars.optgeo.org)のゲートキーパー
- `plateau-mago-implicit` — PLATEAU 3D Tiles実験(CesiumJS専用方針)
- `vientiane-planning-map` — ヴィエンチャンのゾーニング地図(height-coverageの姉妹プロジェクト)
- `claude-mct` — このリポジトリの創設を主導したセッション。Open MCTベースのエージェント
  活動可視化ダッシュボードを担当

## やらないこと

- 特定プロジェクト固有のバグ修正やコードは書かない(ここは知見の集約場所であり、実装場所ではない)
- 「一般則」であることを検証せずに断定しない。実例(Known uses)が1件しかないうちは、
  タグを「個別事情」寄りに倒しておく
