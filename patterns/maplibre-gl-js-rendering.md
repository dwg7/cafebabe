# MapLibre GL JS: レンダリング・スタイル設計

`patterns/maplibre-gl-js.md`(2026-09-02、8プロジェクト調査+vientiane-planning-mapの知見)が
425行・21パターンまで肥大化したため、2026-09-04にテーマ別4ファイルへ分割した1つ。
バージョン選定・投影・terrain/hillshade・スタイル定義変換など、レンダリング結果そのものに
関わる知見を収録する。データ配信は[`maplibre-gl-js-data-serving.md`](maplibre-gl-js-data-serving.md)、
出力・自動化検証は[`maplibre-gl-js-output-testing.md`](maplibre-gl-js-output-testing.md)、
埋め込み・UIは[`maplibre-gl-js-embedding.md`](maplibre-gl-js-embedding.md)を参照。

---

## バージョン選定はバンドラの有無で決まる

**タグ**: 一般則(**推奨**: バンドラ使用時はv6以降の最新版を推奨。hfuさん承認、2026-09-03、
claude-mct実施のD6サーベイより)

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

## 3D terrain併用の可否は、データ規模とハードウェア制約で判断が分かれる(独立分岐)

**タグ**: 個別事情(標高データを持つプロジェクト間で判断が分かれている。「terrainは明示的に
nullで無効化する」(zukaku、上記)とは無効化の理由が異なる——zukakuは印刷物の物理的な
貼り合わせ制約のためだが、こちらは表現力とコストのトレードオフの問題)

**状況(Context)**
標高データを持つプロジェクトが地形の起伏を陰影で伝えたい場面。いずれも同じ形の
raster-dem source(Terrarium形式標高タイル)から2Dの`hillshade`**レイヤータイプ**を使う
ところまでは共通するが、3D `style.terrain`を併用するかどうかで実際の判断が3方向に分かれた。
2026-09-04、mapterhorn-japan-bridge・kitavolca・kaga0への横断ヒアリングで判明。

**問題/対立する力(Problem / Forces)**
3D terrainを有効にすると起伏の説得力は増すが、他レイヤーとの描画順序・パフォーマンスの
考慮が複雑になる。避ければ複雑さを構造的に回避できるが、表現は2Dの陰影止まりになる。
判断を分けている実質的な変数は「データ規模」と「ハードウェアの描画余力」であり、技術的な
好みの違いではない。

**解決(Solution)**
3パターンの実例がある:

1. **terrainを封印し、hillshadeのみ**(mapterhorn-japan-bridge) — `style.terrain: null`の
   まま、hillshadeレイヤーを`background`直後の最下層に配置し、他ベクタレイヤーとの重なり順の
   競合そのものを発生させない設計。terrain併用時のレイヤー順序・パフォーマンス問題自体は
   「まだ実地の知見が乏しい」と正直に報告——解決したのではなく問題を構造的に迂回している
2. **terrain+hillshadeを併用**(kitavolca) — `style.terrain`をトップレベルで明示的に有効化
   (`exaggeration: 1`)し、同じraster-demソースからのhillshadeレイヤーも常設で両方使う。
   対象データが北海道の一部火山周辺に限られ規模が小さいためか、レイヤー順序・パフォーマンス
   で明確な問題には当たっていないと報告
3. **どちらも実装しない、ただし理由と将来の位置づけは明確**(kaga0) — v0スコープとして
   意図的に対象外。ロードマップ上は「hillshadeはv1で対応検討、terrainはv2で再評価」と
   hillshadeの方を先に置いている。根拠はRaspberry Pi 4B+V3D GPUという実機で、純粋な2Dベクタ
   描画だけで既にfpsが逼迫している(1440p・z16構成で11-12fps)こと——terrain/hillshadeの
   追加コスト(raster-demサンプリング・陰影計算・可視タイル数増加)が確実にさらなるfps低下を
   招くという推測に基づく判断。唯一の標高表現は、火山基本図(VBM)自体が持つ等高線
   (`vt_alti`属性付きベクタ線)で、raster-demのシェーディングとは別物の2D表現

**実例(Known uses)**
- `mapterhorn-japan-bridge` — `style.json`で`terrain: null`のまま、`hillshade`レイヤーを
  自前の`mapterhorn` raster-dem source(Terrarium形式標高PMTiles、DECISIONS.mdで議論した
  ものと同一アーカイブ)から生成。paint設定:
  `hillshade-exaggeration: 0.6`、`hillshade-shadow-color: rgba(60,60,60,1)`、
  `hillshade-highlight-color: rgba(255,255,255,1)`、`hillshade-accent-color:
  rgba(90,90,90,1)`(光源角度はMapLibreのデフォルトのまま)。レイヤー順序は
  background→hillshade→行政界の塗り→それ以外の全ベクタレイヤー・ラベル、という最下層配置
- `kitavolca` — `"terrain": {"source": "mapterhorn", "exaggeration": 1}`をトップレベルで
  明示指定し3D terrainをデフォルト有効。同じmapterhornソースから2D hillshadeレイヤーも
  常設。レイヤー順序は`background → 行政区画(fill) → 航空写真(raster) → hillshade →
  水域(fill) → ...`と、航空写真の上・大半のベクタの下という中間位置。paintは
  `hillshade-exaggeration: 0.6`でグレー系(shadow/highlight/accentとも`rgb(60,60,60)`系)に
  シンプル統一
- `kaga0` — terrain・hillshadeとも未実装(意図的なv0スコープ外)。パフォーマンス制約を
  理由にhillshadeをterrainより先にロードマップへ置いている

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
