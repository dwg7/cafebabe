# 外からのリンクの調査(段階 0、能力 C8)

cafebabe のファイル名を変えると、外からのリンクが切れます(GitHub は、ファイル名の変更を転送しません)。
切り替えの前に、どこから、どのパスが参照されているかを数えました。

- 実施: 2026-11-13、cafebabe セッション。
- 方法: `dwg7`・`hfu`・`optgeo`・`tabularmaps`・`UNopenGIS` のうち、2026-09-01 以降に push があり、
  アーカイブされていないリポジトリ 75 件(cafebabe 自身を除く)を、既定ブランチの最新だけ浅く clone し、
  `cafebabe` の語を全文検索しました。cafebabe の創設(2026-09-02)より前から動いていないリポジトリは、
  参照を持ちえないので対象外です。
- 限界: 既定ブランチの最新だけを見ています。ほかのブランチ、issue、PR、Wiki、GitHub の外(スライドなど)は
  見ていません。1 件は空のリポジトリでした。

## 結果

| 項目 | 値 |
|---|---|
| cafebabe に言及するリポジトリ | 28(公開 22、非公開 6) |
| 言及の行数 | 161 |
| ファイルのパスつきの URL(`github.com/dwg7/cafebabe/blob/main/…`) | 14。対象は 2 ファイルだけ |
| パスだけの言及(`patterns/….md`) | 35。対象は 17 ファイル |
| 見出しへのアンカー(`#…`)つきの参照 | 0 |
| コミットを固定した参照(`blob/<ハッシュ>/…`) | 0(すべて `main`) |

**URL として切れるもの**(切り替えで 404 になる):

| パス | 件数 | 参照元 |
|---|---|---|
| `patterns/open-mct.md` | 9 | sas0、mapterhorn-japan-bridge、非公開 1 件 |
| `patterns/markdown-file-conventions.md` | 5 | say-your-grid、adsb-survey、nuye |

**パスだけの言及**(文章やコードのコメントの中。リンクではないが、読んだ人やエージェントが辿る):

| パス | 件数 |
|---|---|
| `patterns/markdown-file-conventions.md` | 6 |
| `patterns/open-mct.md` | 5 |
| `patterns/open-mct-operations.md` | 4 |
| `patterns/maplibre-gl-js-embedding.md` | 3 |
| `patterns/local-dev-pitfalls.md`、`gatekeeping.md`、`agent-execution-gotchas.md` | 各 2 |
| `patterns/maplibre-gl-js.md` | 2(**すでに存在しない**。下記) |
| そのほか 9 ファイル | 各 1 |

公開リポジトリの内訳(パスつきの参照を持つもの): sas0、doverture、mapterhorn-japan-bridge、
ferspas-html-demo、do-survey、tabularmaps/do、tabularmaps/cldr、adsb-survey、say-your-grid、nuye、
dorayaki、stars。リポジトリ名だけに言及するもの: kikimimi、staccato-ecosystem、vientiane-planning-map、
maplibre-gl-atlas、kaga0、snow-hokkaido、kcai-terrio、miso、bvmap、kitaphoto17-navara。
非公開の 6 件は、名前と内訳を書きません(D19)。

**コードと HTML の中の言及**: 8 リポジトリにあります(tabularmaps/do、do-survey、adsb-survey、stars、
doverture、snow-hokkaido、tabularmaps/cldr、dorayaki)。確認した範囲では、いずれもコメントで、
実行時に cafebabe を読みに行くものはありません。

## 分かったこと

1. **切れる URL は少ない**(14 件、2 ファイル)。ただし、パスだけの言及が 35 件あり、こちらは機械的には
   「切れ」として現れません。読んだエージェントが、存在しないパスを探すことになります。
2. **アンカーつきの参照は 0 件**。見出しを変えても、外からの参照は壊れません(D18 のときの確認と同じ)。
3. **すでに切れている言及が 1 つある**。`say-your-grid` は `patterns/maplibre-gl-js.md` に言及していますが、
   このファイルは 2026-09-04 の分割でなくなっています。つまり、ファイルの分割は過去にも外の言及を
   置き去りにしており、今回が初めてではありません。
4. **最も多く参照されているのは Open MCT と .md 運用の 2 テーマ**。試行のテーマ(Open MCT)は、
   外からの参照の影響が最も大きいテーマでもあります。

## 切り替えのときにすること(段階 4)

- 旧構造の最後のコミットにタグ `pre-miso` を付ける。`blob/main/…` を `blob/pre-miso/…` に変えれば、
  旧ファイルを辿れる。
- 旧パスから新しい置き場所(ファイルと仮想パス)への対応表を、メインツリーに置く。
- パスつきの参照を持つリポジトリの担当に、対応表を添えて知らせる。直すかどうかは、各リポジトリの判断。
  cafebabe は、他のリポジトリを編集しない。
