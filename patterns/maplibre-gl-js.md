# MapLibre GL JS

dwg7・hfu の8プロジェクトエージェントへの調査(2026-09-02、claude-mct実施)と、
その後 vientiane-planning-map から届いた知見を初期セットとして収録。

---

## バージョン選定はバンドラの有無で決まる

**タグ**: 一般則

**状況(Context)**
MapLibre GL JSのバージョンを選ぶとき。

**問題/対立する力(Problem / Forces)**
「最新版を使うべき」という直感と、実際の互換性が食い違う。v6はUMDバンドル配布を廃止し、
ESモジュール専用になった。`unpkg.com/maplibre-gl@6.6.0/dist/maplibre-gl.js`は実際に404する。

**解決(Solution)**
- バンドラなし・素の`<script>`タグ構成 → v5系(`5.24.0`)またはv4に留める
- Vite/webpack等でESモジュールとして読み込む構成 → v6で問題なし

**実例(Known uses)**
- `mapterhorn-monitor` — `maplibre-gl@5.24.0`固定(v6のUMD廃止を理由に明示的に回避)
- `mapterhorn-japan-bridge`本体 — `maplibre-gl@4`のまま(サイト間でも不統一)
- `kitavolca` — `maplibre-gl@4`固定
- `sas0` — `maplibre-gl@5.24.0`固定。「ビルドステップなし」というアーキテクチャ制約(D1)のため
- `zukaku` — v6へESM移行済み(`<script type="module">` + `import { Map } from ".../maplibre-gl.mjs"`)
- `height-coverage` — v6のESM専用化を確認、書き換え必須と認識

---

## globe投影とfill-extrusionレイヤーの組み合わせは危険

**タグ**: 一般則

**状況(Context)**
`projection: "globe"`を有効にし、かつ`fill-extrusion`レイヤー(3D建物等)を使う場面。

**問題/対立する力(Problem / Forces)**
`queryRenderedFeatures()`をジオメトリ省略(ビューポート全体)で呼ぶと、fill-extrusionレイヤー
だけが常に空配列を返す。レンダリングは正常、ポイント指定クエリも正常——ビューポート全体
クエリだけが壊れる。v6.1.0のchangelogにある「pitch+3D建物のタイルカリング境界」修正が
クエリ側に及んでいない可能性がある。

**解決(Solution)**
globeを使うなら3D押し出しは諦めてflat fillにする(逆にfill-extrusionが必須ならglobeを諦める)。

**実例(Known uses)**
- `height-coverage` — 実機で確認済み

---

## zoomLevelsToOverscaleのv6デフォルト変更に注意

**タグ**: 一般則

**状況(Context)**
`queryRenderedFeatures()`をビューポート全体クエリで使う場面。

**問題/対立する力(Problem / Forces)**
`zoomLevelsToOverscale`のデフォルトがv6で4に変更されており、`source.maxzoom`を超える
ズームレベルでクエリが空になることがある。

**解決(Solution)**
`zoomLevelsToOverscale: undefined`を明示的に指定し、旧挙動に戻す。

**実例(Known uses)**
- `height-coverage` — 実機で確認済み

---

## terrainは明示的にnullで無効化する

**タグ**: 個別事情(印刷・帳票用途)

**状況(Context)**
style.jsonがterrainを宣言しているが、複数ページを継ぎ目なく貼り合わせる用途(印刷アトラス等)。

**問題/対立する力(Problem / Forces)**
terrainを明示的に無効化しないと、ページごとの見た目が微妙にずれ、貼り合わせた時に破綻する。
理由はスタイルの見た目の問題ではなく物理的制約——terrainの透視投影があると、印刷したページを
隣接させて貼り合わせる際に継ぎ目がズレる。画面上の地図なら気にならないが、紙で物理的に接続
する前提だと真上からの正投影が必須になる。

**解決(Solution)**
`map.setTerrain(null)`を明示的に呼ぶ。

**実例(Known uses)**
- `zukaku` — 印刷アトラスPDF生成で必須の処理として実施
  ([ADR 0004](https://github.com/dwg7/zukaku/blob/main/adr/0004-terrain-and-fill-extrusion-policy.md))

---

## ラベルの太い白背景は icon-image で作る

**タグ**: 一般則

**状況(Context)**
symbol layerのラベルに、視認性のための太い白背景をつけたい場面。

**問題/対立する力(Problem / Forces)**
`text-halo-width`はSDFグリフの固定バッファで頭打ちになり、太くできない。

**解決(Solution)**
`icon-image` + `icon-text-fit: "both"`で、単色画像をテキストのバウンディングボックスに
引き伸ばす方式が正攻法。

**実例(Known uses)**
- `zukaku`

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

---

## ヘッドレスレンダリングはWebGLキャンバスを含められない

**タグ**: 一般則

**状況(Context)**
Playwright等でMapLibre GL JSのページをPDF化・画像化する場面。

**問題/対立する力(Problem / Forces)**
`page.pdf()`(Playwright/CDP)は生きたWebGLキャンバスを含められない。

**解決(Solution)**
`canvas.toDataURL("image/png")`で画像化し、`<img>`に差し替える。

**実例(Known uses)**
- `zukaku`

---

## 実ブラウザの印刷とPlaywrightのpage.pdf()は別コードパス

**タグ**: 一般則

**問題/対立する力(Problem / Forces)**
実ブラウザの「印刷→PDF保存」とPlaywrightの`page.pdf()`は内部コードパスが違う。
Playwright検証だけでは、実ブラウザ特有の印刷不具合(色ズレ、Windowsドライバの向き切替
バグ等)を再現できないことがある。「自動テストで確認済み」は「実際のOSレベルのレンダリング/
印刷パイプラインを通した」ことの証明にならない。

**解決(Solution)**
印刷パイプラインの最終検証は、実ブラウザでも行う。
(参考: https://andre.arko.net/2025/05/25/chrome-headless-print-to-pdf/)

**実例(Known uses)**
- `zukaku` — 実機バグ報告3件([dwg7/zukaku#2](https://github.com/dwg7/zukaku/issues/2)、
  [#4](https://github.com/dwg7/zukaku/issues/4)、[#6](https://github.com/dwg7/zukaku/issues/6))
  すべてが、Playwrightでは一度も再現しなかった
  ([ADR 0007追記](https://github.com/dwg7/zukaku/blob/main/adr/0007-client-side-print-mode.md))

---

## ブラウザ自動化ツールの非表示ペインでは、コンテナサイズが0x0になりうる

**タグ**: 一般則

**状況(Context)**
Claude Codeのブラウザプレビューのような自動化ツールで、MapLibre GL JSページを検証する場面。

**問題/対立する力(Problem / Forces)**
`new maplibregl.Map()`はコンストラクタ実行時にコンテナのサイズを一度だけ測定してcanvasに
焼き込む仕様。プレビューペインが「表示されていない」タイミングだと、コンテナの
`getBoundingClientRect()`が実際には0x0を返すことがある(ツールの状態確認結果に"The Browser
pane is currently hidden."と出ているときは要注意)。ページ自体は正常でも、この一瞬に初期化が
走ると地図が完全に真っ黒になる。

**解決(Solution)**
`window`の`resize`イベントと`document`の`visibilitychange`(`visible`になった瞬間)の両方で
`map.resize()`を呼ぶ。後から正しいサイズが取れた時点で自動復旧する。

**実例(Known uses)**
- `vientiane-planning-map` — ブラウザプレビューツールでの検証中に地図が真っ黒になる現象に
  遭遇し特定。詳細は[`DECISIONS.md`#3](https://github.com/dwg7/vientiane-planning-map/blob/main/DECISIONS.md#3-地図が真っ黒になるバグmaplibreのコンテナサイズ誤測定)参照

---

## fitBoundsのpaddingでズームレベルシフトができる

**タグ**: 個別事情(オフスクリーンレンダリング用途)

**状況(Context)**
印刷物のように「後からズームインできない」出力先で、広い範囲を1ページに収めつつ、詳細な
ベクタタイル(建物形状・道路名ラベル等)を保ったまま表示したい場面。

**問題/対立する力(Problem / Forces)**
Webマップと違い、印刷は焼き付けた瞬間のズームレベル(=取得するベクタタイルのLOD)が永久に
そのまま。素直に`fitBounds`すると必然的に低いズームレベルのタイルが選ばれ、輪郭だけの
地図になってしまう。

**解決(Solution)**
`fitBounds`/`fitBoundsOptions.padding`はコンテナのpxサイズに応じてズームレベルが決まる
性質を利用し、オフスクリーンで実際より大きいコンテナにレンダリング→スナップショットを
縮小する、という「ズームレベルシフト」(ブラウザのCtrl+-相当)ができる。取得するタイルの
ズームレベル自体を、最終的な物理サイズから独立して制御できるのがポイント。

**実例(Known uses)**
- `zukaku` — 複数セルを1ページに収める概要(索引)ページで採用。実際より`rows×cols`倍
  大きいオフスクリーンコンテナでレンダリングしてから縮小する
  ([ADR 0009](https://github.com/dwg7/zukaku/blob/main/adr/0009-overview-zoom-level-shift.md))

---

## 左上パネルは折りたたみ可能にする

**タグ**: 一般則(UI)

**解決(Solution)**
`data-collapsed`属性 + トグルボタンで最小化可能にする。

**実例(Known uses)**
- `kitavolca` — 実装済み

---

## ホバー情報は固定ドッキングパネルで表示する

**タグ**: 一般則(UI)

**問題/対立する力(Problem / Forces)**
複数レイヤーが重なる箇所で、フローティングツールチップだと情報が読みにくい。

**解決(Solution)**
`queryRenderedFeatures(event.point, { layers: [...優先順位付き配列...] })`で、1つの
固定ドッキングパネルに情報を出す。

**実例(Known uses)**
- `sas0`

---

## hash:"map" で名前空間化する

**タグ**: 一般則

**問題/対立する力(Problem / Forces)**
`hash: true`だと、URLハッシュがアプリ独自の状態と衝突しうる。

**解決(Solution)**
`hash: "map"`にすると、URLハッシュが`#map=z/lat/lng/bearing/pitch`と名前空間化され、
MapLibreの`Hash`クラスは自分のキー以外に手を出さなくなる。アプリ独自の状態を同じhashに
同居させられる。

**実例(Known uses)**
- `zukaku`、`height-coverage`

---

## map.remove()を確実に呼ぶ(埋め込み先がビューを再構築する場合)

**タグ**: 一般則

**状況(Context)**
Open MCTのような、ビューを破棄・再構築するホスト環境にMapLibreを埋め込む場面。

**問題/対立する力(Problem / Forces)**
teardown処理が無いと、インスタンスを作り直すたびにWebGLコンテキストがリークする。

**解決(Solution)**
埋め込み先のview destroy時に`map.remove()`を確実に呼ぶ。

**実例(Known uses)**
- `sas0`(Open MCTインスツルメントとして埋め込み)

---

## iframe埋め込みよりネイティブ埋め込みを検討する

**タグ**: 個別事情(埋め込み型ダッシュボード)

**問題/対立する力(Problem / Forces)**
iframeでの埋め込みは、sandbox属性(`allow-same-origin`等)まわりの問題に繰り返し遭遇する。

**解決(Solution)**
ネイティブなインスツルメント/コンポーネントとして直接埋め込む形に切り替える。

**実例(Known uses)**
- `sas0` — 過去にiframe方式を試し、放棄してネイティブ埋め込みに移行

---

## GetLegendGraphicでSLDの色をJSON抽出する

**タグ**: 個別事情(GeoServer/WFS利用者)

**状況(Context)**
GeoServer配信のWFSレイヤー(SLDでスタイル定義)を、MapLibreのstyle定義に変換する場面。

**解決(Solution)**
GetLegendGraphicのリクエストで`format=application/json`を指定すると、SLDの色定義を
直接JSONとして抽出できる。

**実例(Known uses)**
- `vientiane-planning-map` — Virgo/GLUP2030(`geonode:glup2030_cdudcp_v1`、EPSG:32648、
  認証不要)で確認
