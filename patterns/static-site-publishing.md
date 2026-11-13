# 静的サイトの公開(GitHub Pages)

ビルドした、または手書きの静的サイトを、GitHub Pages などで配る場面の知見。
2026-11-13、hfuさんの推奨と`dwg7/dorayaki`の報告より新設。関連する既存の知見は、分散したまま
参照に留める(下の「関連」)。

---

## 静的サイトは、JSとCSSをインラインにした1ファイルの`index.html`にまとめる。ハッシュつきのファイル名を使わない

**タグ**: 一般則(**推奨**: hfuさん、2026-11-13)

**状況(Context)**
デモや小さな地図サイトを、GitHub Pages のサブパス(`dwg7.unopengis.org/<リポジトリ>/`)などに置く場面。

**問題/対立する力(Problem / Forces)**
複数ファイルに分かれたサイトは、置き場所に依存する。サブディレクトリの下に置くと、相対パスと
絶対パスの違いで資産が404になる。バンドラが付けるハッシュつきのファイル名は、ビルドのたびに
変わり、参照の書き換えと古いファイルの掃除が要る。別の場所へ移すときも、ファイルの集合ごと
運ぶ必要がある。

**解決(Solution)**
JSとCSSを`index.html`にインラインにし、**1ファイル**で完結させる。ファイル名にハッシュを付けない。
hfuさんが挙げた理由は2つ: (1) **1ファイルにすることで回避できるトラブルが多い**(サブディレクトリ、
相対パスと絶対パス)。(2) **移植が非常に容易になる**。

**例外として残るもの**: インラインにできない資産がある。MapLibre GL JS 6のワーカーは別ファイルで
なければならないので、`index.html`の隣に固定名で置き、ページ相対で指す
([`maplibre-gl-js-embedding.md`](maplibre-gl-js-embedding.md)の2026-11-13の追記参照)。
タイルなどのデータも別ファイルになる。

**他の選択との関係**: `dwg7/miso-geo`と`dwg7/doverture`は、Viteのハッシュつき資産(`assets/…-<hash>.js`)
を使っている。これらは各プロジェクトの独立した選択で、この推奨より前のもの。既存のサイトを
作り直すことまでは求めていない(cafebabeの理解。hfuさんには未確認)。

**実例(Known uses)**
- `dorayaki` — esbuildでアプリとMapLibreを1つのESM(約1.09MB)にまとめて`<script type="module">`に
  インラインし、CSSも`<style>`にインライン。ワーカーだけ`docs/maplibre-gl-worker.mjs`として隣に置く
  (報告、2026-11-13。ローカル配信のみで、Pages上は未確認)
- `rpi3-server-guide` — 単一の静的HTMLページ。公開ページ(約78KB)に外部の`<script src>`・
  `<link href>`が無く、`<style>`が1つだけであることをcafebabeが確認(2026-11-13)。
  この推奨に沿って作られたのか、独立にそうなったのかは未確認

---

## 関連(他のファイルにある、Pages公開の知見)

- `.nojekyll`が無いと、`docs/`配下のMarkdownは**生の`.md`のまま配信され、同時にJekyllが変換した
  `.html`も作られる**(2026-11-13にcafebabeが確認。当初ここに「処理される」とだけ書いたのは不正確だった)。
  公開元がリポジトリルートだと`CLAUDE.md`などの文脈ファイルも公開される →
  [`markdown-file-conventions.md`](markdown-file-conventions.md)
- `.gitignore`の`data/`は`docs/data/`まで無視する → [`local-dev-pitfalls.md`](local-dev-pitfalls.md)
- GitHub PagesはCSS/JSを10分キャッシュする(`cache-control: max-age=600`) →
  [`open-mct-operations.md`](open-mct-operations.md)
- MapLibre GL JS 6のワーカーURL → [`maplibre-gl-js-embedding.md`](maplibre-gl-js-embedding.md)
