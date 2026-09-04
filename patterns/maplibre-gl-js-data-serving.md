# MapLibre GL JS: データ配信・スタイル取得

`patterns/maplibre-gl-js.md`(2026-09-02初出)の分割(2026-09-04)の1つ。上流タイルサーバー
とのやり取り、CORS、attribution、大容量データ配信など、データの取得・配信に関わる知見を収録。
レンダリング・スタイル設計は[`maplibre-gl-js-rendering.md`](maplibre-gl-js-rendering.md)、
出力・自動化検証は[`maplibre-gl-js-output-testing.md`](maplibre-gl-js-output-testing.md)、
埋め込み・UIは[`maplibre-gl-js-embedding.md`](maplibre-gl-js-embedding.md)を参照。

---

## ランタイムハイドレーション: 静的style.jsonを持たない

**タグ**: 一般則

**状況(Context)**
上流(タイルサーバー)のスタイルを、ローカルにコピーして使うか、都度取得するか。

**問題/対立する力(Problem / Forces)**
静的コピーを持つと、上流のスタイル変更のたびにバックポート作業が発生し、ズレが生まれる。

**解決(Solution)**
ページ読込時に上流(`stars.optgeo.org`)のスタイルJSONを直接fetchし、`style.sources`/
`style.layers.push()`でその場に独自レイヤーを追加・差し替える。`Promise.allSettled` +
`AbortController`でフォールバックを用意する。

**実例(Known uses)**
- `sas0` — 状況図インスツルメントで採用
- `kitavolca` — `hfu/stars`の設定を手動でバックポートし続けるのをやめ、ページ読込時に
  上流JSONを直接fetchしてid一致でレイヤー定義を差し替える方式に切り替え
  ([コミット2dc4523](https://github.com/hfu/kitavolca/commit/2dc4523)、`docs/app.js`)。
  他リポジトリの正本を消費するだけの立場のプロジェクトなら汎用的に使える

---

## CORS: Originを反射する実装に注意

**タグ**: 個別事情(`stars.optgeo.org`利用者)

**状況(Context)**
`stars.optgeo.org`(Martin)のタイル・スタイル・TileJSONをfetchする場面。

**問題/対立する力(Problem / Forces)**
CORSはワイルドカードではなく、リクエストのOriginヘッダーを反射する実装になっている。
`credentials: include`のような使い方をする場合、挙動が単純なワイルドカードとは異なる。

**解決(Solution)**
`credentials`オプションを使う前に、実際のレスポンスヘッダーを確認する。検証には
`curl -I`だけでなく`-H "Origin: https://example.com"`を明示的に付ける必要がある——
Originヘッダーの反射実装は、Originヘッダーなしのリクエストでは`Access-Control-Allow-Origin`
自体が一切返らず、「CORS未対応」に見えてしまう。

**実例(Known uses)**
- `stars-fd`(提供側として把握。`curl -I`だけでは正しい挙動が見えず、Originヘッダーを
  付けて初めて判明した経緯あり)

---

## attributionはTileJSONに埋め込むだけで自動表示される

**タグ**: 一般則

**状況(Context)**
地図隅への帰属表示(attribution)を実装する場面。

**解決(Solution)**
TileJSON自体に`attribution`フィールドを埋め込んでおけば、style.json側で明示指定しなくても
MapLibre GL JSが自動的に表示する。実装コストがゼロになる。

**実例(Known uses)**
- `stars-fd`(提供側として把握)

---

## tileSizeは明示する(512px vs 256px の混在)

**タグ**: 一般則

**状況(Context)**
512px(retina)前提のスタイルと、GSI地理院タイルのような256px前提のスタイルが混在する場面。

**問題/対立する力(Problem / Forces)**
`tileSize`をstyle.json側で明示しないと、サーバーサイドレンダリング(PDF生成等)のような
ツール連携で崩れることがある。

**実例(Known uses)**
- `zukaku`(Field Papersで実際に踏んだ)

---

## 大容量データはPMTiles + Martinのpmtiles.sourcesで

**タグ**: 一般則

**解決(Solution)**
リモートファイルへのrangeリクエストを使い、自前コピーを持たずに配信できる。

**実例(Known uses)**
- `height-coverage`
