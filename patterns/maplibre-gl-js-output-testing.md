# MapLibre GL JS: 出力・自動化検証

`patterns/maplibre-gl-js.md`(2026-09-02初出)の分割(2026-09-04)の1つ。PDF化・画像化、
ヘッドレス/自動化ツール上での検証、オフスクリーンレンダリングなど、「見えているものを
別の形で取り出す」際の落とし穴を収録。レンダリング・スタイル設計は
[`maplibre-gl-js-rendering.md`](maplibre-gl-js-rendering.md)、データ配信は
[`maplibre-gl-js-data-serving.md`](maplibre-gl-js-data-serving.md)、埋め込み・UIは
[`maplibre-gl-js-embedding.md`](maplibre-gl-js-embedding.md)を参照。

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

**訂正・深掘り(2026-10-02、zukakuより)**: 「`window.print()`と同じ印刷パイプラインを通る
はず」という想定自体は正しかったが、**オプトインが必要**だった——`page.pdf()`に
`preferCSSPageSize: true`を渡さないとCSSの`@page`が無視され、Letter判(612x792pt)に
戻る。生成PDFのmediabox(用紙サイズ)を実測するまで気づかなかった
(`scripts/render/lib.js`、zukaku ADR 0013追記・D18)。「同じはず」と思ったら、結果の
物理サイズを測って確かめる。

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
- `maplibre-gl-atlas`(2026-09-08〜09、2026-10-02にzukaku経由で報告) — プレビューペイン
  検証の癖が他にも3つ: (1) `wait`を連続して呼ぶだけだと合成が止まりMapLibreの`idle`が
  進まない(数秒おきに`screenshot`を挟むと進む)。(2) 非表示ペインでは
  `getBoundingClientRect()`が0を返し、座標計算が汚染される。(3) 同一タブで使い捨ての
  `Map`を`.remove()`せず作り続けると、WebGLコンテキストが枯渇して`load`が発火しなく
  なる。いずれもコードのバグではなく**検証環境の癖**で、「固まった」と見えても原因は
  こちらだった(maplibre-gl-atlas HANDOVER.md、adr/0002追記)

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

## 名前付き`@page`(landscape)の要素高さが@page高さと一致すると、最後に空白ページが1枚増える。検証は「向き×最後のシート」で組む

**タグ**: 一般則(Chromiumのprint-to-PDF固有の挙動)

**状況(Context)**
CSSの名前付き`@page`でlandscapeを割り当てた要素を、ChromiumでPDFへ印刷する場面。

**問題/対立する力(Problem / Forces)**
landscapeの`@page`を割り当てた要素の高さが、その`@page`の宣言高さと**厳密一致**すると、
**最後のシートの後に空白ページが1枚増える**。portraitの同形ルールでは再現しない。

【誤診の経緯】最初は`break-after: page`が原因と考え`:last-child`で解除したが直らなかった。
最小HTMLを作って二分探索したところ、`break-after`を外しても再現し、高さを0.1mm減らしても
再現、1mm減らすと解消した——と、仮説が覆った。

さらに、この問題は「最後のシートがlandscape」という条件でしか起きず、検証がportraitしか
通っていなかったため、**すでに本番公開済みの経路でも見逃していた**。

**解決(Solution)**
landscape要素の高さを`calc(210mm - 1mm)`のように、`@page`高さより僅かに小さくする(1mmは
標準の余白15mmに比べ知覚できない)。検証マトリクスには「向き(portrait/landscape)×最後の
シート」を入れる。

**実例(Known uses)**
- `maplibre-gl-atlas`(zukaku由来) — `src/strategy.ts`の`calc(${w}mm - 1mm)`(コメントに
  0.1mmでは再発・1mmで解消という二分探索の結果を記録、adr/0001追記・D13、
  2026-10-02。cafebabe側でコードの存在を確認)
