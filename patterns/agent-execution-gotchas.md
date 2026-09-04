# エージェント実行環境の癖

Claude Codeエージェント自身のツール実行環境(ブラウザ自動化、バックグラウンドプロセス、
シェル、権限システム等)に起因する、プロジェクトの技術内容とは独立した落とし穴について。
2026-09-02、全エージェントへの自由知見募集(D6)より、5プロジェクトから独立に集まった実例。

---

## 自動化ブラウザツールの非表示・バックグラウンドタブはWebGL描画を検証できない

**タグ**: 一般則

**状況(Context)**
Claude Codeのブラウザ自動化ツールで、MapLibre GL JS/CesiumJS等のWebGL系ページを検証する
場面。

**問題/対立する力(Problem / Forces)**
`document.visibilityState: "hidden"`のタブでは、ブラウザの意図的な最適化により、Cesiumの
ようなライブラリがタイルを実際に選択・描画しない。プレビューペインが非表示の間にMapLibreの
コンテナサイズ測定が走ると、`getBoundingClientRect()`が0x0を返すこともある
([`patterns/maplibre-gl-js-output-testing.md`](maplibre-gl-js-output-testing.md)にも関連実例
あり)。スクリーンショットで
「真っ黒/空」に見えても、それがバグなのかツール自体の制約なのか区別しにくい。

**解決(Solution)**
この種のツールでWebGL/Cesium系の描画を検証する場合、スクリーンショットに頼らず、直接
`fetch()`やネットワークリクエストのレベルで確認する方法に切り替える。MapLibreについては
`resize`/`visibilitychange`イベントで復旧させる対策も有効。

**実例(Known uses)**
- `plateau-mago-implicit` — CesiumJSがバックグラウンドタブでタイルを描画しない現象に遭遇
- `vientiane-planning-map` — プレビューペイン非表示時のコンテナサイズ0x0問題
  ([`patterns/maplibre-gl-js-output-testing.md`](maplibre-gl-js-output-testing.md)参照)

---

## 長時間バックグラウンド処理は`disown`ではなく、ハーネスが追跡できるポーリングでラップする

**タグ**: 一般則

**状況(Context)**
Claude Codeのようなハーネス上で、長時間かかるバックグラウンド処理を起動する場面。

**問題/対立する力(Problem / Forces)**
`nohup ... & disown`は、実行基盤(ハーネス)の完了通知の仕組みから処理を切り離してしまい、
「ラッパーコマンドの起動」自体を完了と誤検知するリスクがある。

**解決(Solution)**
`while pgrep <process>; do sleep 30; done`のような、ハーネス自体が追跡できる形の待機に
置き換える。ハーネスの`run_in_background`のような組み込み機構がある場合は、そちらを使う。

**実例(Known uses)**
- `plateau-mago-implicit` — 長時間処理の完了検知に`disown`を使わない方針を採用

---

## サンドボックス化シェルでの`curl`結果は変数経由ではなく一時ファイル経由で扱う

**タグ**: 一般則

**状況(Context)**
サンドボックス化されたシェル環境で、`curl`の出力をパイプ処理する場面。

**問題/対立する力(Problem / Forces)**
`curl url | シェル変数に代入 → printf '%s' "$var" | grep ...`という構成は、サンドボックス化
された環境だと稀に正しく読み取れないことがある。

**解決(Solution)**
一時ファイルに保存してから`grep`/`awk`にファイル引数で渡す方式に変える。

**実例(Known uses)**
- `kitavolca` — CLIツールでのスクレイピングスクリプトでこの問題に遭遇し、一時ファイル経由
  に変更して安定化

---

## バックグラウンドプロセス起動後、シェルのcwdが暗黙にリセットされることがある

**タグ**: 一般則

**状況(Context)**
Bashツールで`&`を使ってdevサーバー等をバックグラウンド起動する場面。

**問題/対立する力(Problem / Forces)**
その後のシェルの作業ディレクトリが暗黙にリセットされることがあり、直後に`git commit`すると
`fatal: not a git repository`のようなエラーで失敗する。

**解決(Solution)**
バックグラウンドプロセスを起動した直後のシェル操作は、明示的に`cd`し直すか`pwd`で現在地を
確認する習慣をつける。

**実例(Known uses)**
- `claude-mct` — devサーバーのバックグラウンド起動後、直後の`git commit`が失敗する現象に
  遭遇

---

## 権限分類器は、ユーザーの直接指示があっても自己の権限設定ファイルへの書き込みをブロックする

**タグ**: 一般則

**状況(Context)**
`.claude/settings.local.json`のような、エージェント自身の権限設定ファイルを、ユーザーの
明示的な指示のもとで編集しようとする場面。

**問題/対立する力(Problem / Forces)**
ユーザーから明示的に指示されていても、auto-mode classifierのような安全機構がWriteツール
自体をブロックすることがある。自己の権限を自己が拡張する操作は、指示の出どころに関わらず
特別扱いされる。

**解決(Solution)**
無理に回避しようとせず、ユーザーに手動でファイルを作成・編集してもらう形に切り替える。

**実例(Known uses)**
- `stars-fd` — `.claude/settings.local.json`へのBash許可ルール追記がブロックされ、ユーザー
  への差し戻しに切り替えた
