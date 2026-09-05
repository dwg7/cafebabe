# ideas/

`patterns/`は**実装に裏打ちされた知見**(誰かが実際にやったこと)だけを置く場所です。
一方、dwg7のミッション("test new technologies for future geospatial operations"、
[DWG7-CONTEXT.md](../DWG7-CONTEXT.md)参照)には、まだ誰も実装していないが検討する価値の
ある技術的アイデアも当然含まれます。それを`patterns/`に書くと、実例(Known uses)が無いのに
一般則めいた体裁になり、他プロジェクトへの誤ったお墨付きになりかねません。

`ideas/`は、そうした**まだ実装されていない探索テーマ**を置く、`patterns/`のsiblingです。
2026-09-06、hfuさんの提案で新設(D16、[DECISIONS.md](../DECISIONS.md)参照)。

## 書式

1アイデア=1ファイル。以下の型で書きます:

```markdown
# <アイデア名>

**状態**: 探索中 | 実装待ち | 却下(日付・理由) | patterns/へ昇格(日付・リンク)
**出典**: 誰が/いつ/どこで提起したか(issueへのリンク等)

**動機・背景(Why)**
なぜこれがdwg7にとって検討する価値があるか。関連するdwg7の原則(keep open軸等)との接続。

**未解決の問い(Open Questions)**
- 検討したい論点を箇条書きで

**関連(Related)**
- `patterns/`の関連ファイル、他の`ideas/`エントリ

**進捗ログ(Log、追記専用)**
- YYYY-MM-DD: 何があったか(DECISIONS.mdと同じく、書き換えず追記する)
```

## `patterns/`との関係

- アイデアが実際にどこかのプロジェクトで実装されたら、`patterns/`に正式なパターンとして
  書き起こす。`ideas/`側のファイルは削除せず、進捗ログに「→ `patterns/X.md`へ昇格
  (日付)」と追記して残す(実装に至った経緯の記録として価値がある)
- アイデアが「やらない」と決まった場合も、削除せず状態を「却下」に変更し、理由を追記する
  (`DECISIONS.md`の追記専用原則と同じ)

## 現在のアイデア

- [`osm-community-oauth.md`](osm-community-oauth.md) — 地理空間コミュニティ向けのオープンID
  としてOSM OAuthを使う([UNopenGIS/7#980](https://github.com/UNopenGIS/7/issues/980))
