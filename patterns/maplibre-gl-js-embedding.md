# MapLibre GL JS: 埋め込み・UI

`patterns/maplibre-gl-js.md`(2026-09-02初出)の分割(2026-09-04)の1つ。他アプリへの埋め込み、
UIコンポーネント設計、状態同期など、ホスト環境とのつなぎ込みに関する知見を収録。
レンダリング・スタイル設計は[`maplibre-gl-js-rendering.md`](maplibre-gl-js-rendering.md)、
データ配信は[`maplibre-gl-js-data-serving.md`](maplibre-gl-js-data-serving.md)、出力・自動化
検証は[`maplibre-gl-js-output-testing.md`](maplibre-gl-js-output-testing.md)を参照。

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

**タグ**: 一般則(**推奨**、hfuさん承認、2026-09-03、claude-mct実施のD6サーベイより)

**状況(Context)**
`hash: true`でURLに地図状態を保持したいが、アプリ独自の状態(パネル開閉等)もURLハッシュに
持たせたい場面。

**問題/対立する力(Problem / Forces)**
`hash: true`だと、URLハッシュがアプリ独自の状態と衝突しうる。

**解決(Solution)**
`hash: "map"`にすると、URLハッシュが`#map=z/lat/lng/bearing/pitch`と名前空間化され、
MapLibreの`Hash`クラスは自分のキー以外に手を出さなくなる。アプリ独自の状態を同じhashに
同居させられる。

**実例(Known uses)**
- `zukaku`、`height-coverage`

---

## UIトグルの初期状態を決め打ちせず、実際のmap状態にイベントで同期する

**タグ**: 一般則(UI)

**状況(Context)**
terrain有効/無効の切り替えチェックボックスのように、map側の状態とUI表示を一致させたい
コントロールを実装する場面。

**問題/対立する力(Problem / Forces)**
HTML側の`checked`属性とJS側のデフォルト値を二箇所で管理すると、どちらかを変更し忘れた
ときに状態がずれる。TerrainControlのような組み込みボタンからmap状態が変わった場合、
チェックボックス側だけ追従できず食い違うこともある。

**解決(Solution)**
HTML側に`checked`属性を書かず、style.json側で宣言した状態を正とする。
`map.on('terrain', () => { checkbox.checked = !!map.getTerrain(); })`のように、map自身の
状態変化イベントを購読してUIを同期させる。デフォルト値の二重管理が構造的に発生しない。

**実例(Known uses)**
- `kitavolca` — terrainチェックボックスで採用。TerrainControlボタン経由の操作でも同じ
  イベント経由でチェックボックスが追従する(2026-09-04、terrain/hillshadeヒアリングより)

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
