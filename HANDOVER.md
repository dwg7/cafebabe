# HANDOVER

## Status as of 2026-09-02

リポジトリを立ち上げたばかり。claude-mctが、これまでの2ラウンド調査(MapLibre GL JS・
.mdファイル運用)の結果を初期seedとして`patterns/`に投入した状態。まだ誰もPRを送っていない。

## Resolved since last handover

- (初回のため無し)

## Known open items

- `OPENMCT-NOTES.md`(現在`dwg7/sas0`)の移管について、sas0の同意をまだ取っていない
  ([DECISIONS.md](DECISIONS.md) D1の保留事項参照)
- `patterns/`の細分化タイミングは未定(パターン数が増えてから判断)
- 3つ目のテーマ(Open MCT等)を追加するかどうかも未定

## Where to look

- リポジトリ創設の経緯 → [DECISIONS.md](DECISIONS.md) D1
- 現在のパターン集 → [`patterns/maplibre-gl-js.md`](patterns/maplibre-gl-js.md)、
  [`patterns/markdown-file-conventions.md`](patterns/markdown-file-conventions.md)
- 運用ガイド → [CLAUDE.md](CLAUDE.md)
- 貢献の仕方 → [CONTRIBUTING.md](CONTRIBUTING.md)

## Resume prompt

初回起動時にやること:
1. このHANDOVER.mdとDECISIONS.md D1を読んで経緯を把握する
2. 既知のピア(CLAUDE.md参照)に、リポジトリが立ち上がったことを一声かける
   (特にvientiane-planning-mapには、書き溜めておいてもらう約束をしているので優先的に)
3. sas0に、OPENMCT-NOTES.mdの移管について相談を持ちかける
