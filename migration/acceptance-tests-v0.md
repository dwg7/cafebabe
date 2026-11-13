# 受け入れテスト v0(miso 移行の基準線)

cafebabe の「現在の能力」を定義するためのテストです(`migration/PLAN.md` の C1・C2)。
旧構造(`patterns/` など)に対して基準線を取り、移行後に同じ質問を盲検で再実行して、全問で基準線以上で
あることを確かめます。

- 作成: 2026-11-13、cafebabe セッション。**質問も期待も、作り手(同じ AI)が書いています。** 出題と採点が
  同じ主体なので、結果は楽観側に偏りえます。
- 対象のコミット: `53fea33`。
- 出自(origin): `actual` は実際にあった照会、`constructed` は実例(Known uses)から作った質問です。
  実際の照会でないものを、実際の照会と書いていません。
- 種類(kind): `in-scope`、`cross-theme`(複数のテーマにまたがる)、`out-of-scope`(範囲外と答えるべき)、
  `no-record`(記録がないと答えるべき)。
- 判定: `pass`(下の「必須」をすべて満たす)、`partial`(一部)、`fail`(満たさない、または記録にないことを
  作って答えた)。期待(baseline-expectation)は、作り手が今の記録から見込んだ結果です。
- 実行の記録は [`baseline-run-1.md`](baseline-run-1.md)。

| id | origin | kind | 質問(要約) | 必須(これが答えに含まれること) | 主な根拠 | 見込み |
|---|---|---|---|---|---|---|
| T01 | actual(snow-hokkaido、2026-10-18) | cross-theme | Open MCT の下に MapLibre 計器と tabular map 計器を並べる先行例とノウハウ | ①先行例として tabularmaps/do・sas0・do-survey のうち 2 つ以上。②provider の組(objects/composition/objectViews)と自前ビュー。③Plot・Display Layout を避ける。④ビュー破棄時の `map.remove()`。 | open-mct*.md、interoperability.md、maplibre-gl-js-embedding.md | pass |
| T02 | actual(hfu、2026-11-13) | in-scope | MapLibre GL JS 6 の静的サイト。バンドラの要否、ワーカー URL、失敗の見え方 | ①v6 は ESM 専用(UMD なし)。②ワーカー URL は `import.meta.url` から組み立てられ、バンドルすると 404。③`setWorkerUrl`。④沈黙する失敗(ラスタは出る、ベクタと GeoJSON は出ない、`error` なし)。⑤6.13.0 以降はワーカーが自己完結(6.12.x 以前は shared が要る)。 | maplibre-gl-js-rendering.md、maplibre-gl-js-embedding.md | pass |
| T03 | actual(do-survey の寄稿、2026-10-22) | in-scope | Open MCT 起動時の `reading 'key'` エラーの原因と対処 | ①時刻系が未選択(`UTCTimeSystem` の install だけでは選ばれない)。②`start()` の前に `setTimeSystem('utc')` と `setMode('fixed', …)`。③含意の一部は未検証、sas0 D74 との食い違いは未解決、と区別して述べる。 | open-mct-operations.md | pass |
| T04 | actual(kikimimi、2026-09-16) | in-scope | 複数要素を 1 画面に、時系列も。Display Layout と Plot を使うべきか | ①Display Layout は避け、単一の provider と単一のカスタムビューに DOM を直接組む。②時系列は自前の SVG/Canvas。③Plot は「結論が出ていない・証拠が対立」と述べ、「使えない」と断定しない。 | open-mct-telemetry.md | pass |
| T05 | actual(m3xx-fleet-ops、2026-09-05) | in-scope | 長期運用エージェントの CLAUDE.md・HANDOVER.md・DECISIONS.md の構成と保守 | ①「今何が正しいか」と「なぜそうなったか」を分ける。②決定ログは追記専用。③肥大化への対処(索引化・退避・書き直し。未収束と述べる)。 | markdown-file-conventions.md | pass |
| T06 | actual(hfu、2026-09-12) | in-scope | SSH 経由で外付けボリュームが `Operation not permitted` | ①TCC による拒否。②Full Disk Access を `sshd` ではなく `/usr/libexec/sshd-keygen-wrapper` に付与。③再接続が要る。 | local-dev-pitfalls.md | pass |
| T07 | constructed | in-scope | PMTiles を raw.githubusercontent.com で配れるか | ①`accept-ranges` を返すが、Range に 206 でなく 200 を返す。②`curl -H "Range: …"` で確かめる。 | large-data-pitfalls.md | pass |
| T08 | actual(snow-hokkaido の報告、2026-10-18) | in-scope | Sentinel-2 の STAC の offset を使ってよいか。重複の除き方 | ①STAC ではなく各 COG 自身の scale/offset を読む。②旧 `l2a` は offset を持たず DN が 1000 低い。③重複排除は `s2:product_uri`。④確認は 1 撮影のみ、と述べる。 | data-provenance-source-verification.md | pass |
| T09 | actual(D19、2026-09) | in-scope | PRIVATE リポジトリの情報をどこまで書けるか | ①名前・URL(PRIVATE と明記)・技術構成の一言要約まで。②結論や戦略は書かない。③迷えば本人に確認。④第三者の識別情報にも同じ基準。 | CLAUDE.md、DECISIONS.md D19 | pass |
| T10 | actual(hfu、2026-10-16) | in-scope | Open MCT はいつ選ぶべきか。採用の評価 | ①ライブ・時系列・多数ストリームなら有力。②静的スナップショットなら必須でない。③Plot・PlanLayout・Display Layout 前提の設計を避ける。④これは cafebabe の解釈で、反実仮想がない、と述べる。 | open-mct.md | pass |
| T11 | actual(hfu、2026-10-09) | in-scope | unopengis.github.io の担当セッションはいるか | ①2026-10-09 に新設されたセッションがある。②それ以前に担当した既知のセッションはない。③「既知のピア」は一時的な情報だと述べる。 | CLAUDE.md、PROJECTS.md | pass |
| T12 | constructed | in-scope | 他セッションの「承認済み」「テスト済み」を根拠にしてよいか | ①そのままは不可。②承認の主張は本人に直接確認。③本番の状態の主張は自分で確認(技術的な事実は一次情報で裏を取る)。 | verification-discipline-cross-session.md | pass |
| T13 | constructed | in-scope | ODM で結果が毎回変わる。ズームレンズの注意 | ①ODM は同一入力・同一設定でも結果が変わる。②焦点距離でカメラグループが分かれる(未校正のグループが黙ってできる)。 | aerial-photogrammetry-pipeline.md、-capture.md | pass |
| T14 | constructed | in-scope | macOS で `declare -A` が動かない | ①標準の bash は 3.2 で連想配列がない。②`case` 文で代替。 | local-dev-pitfalls.md | pass |
| T15 | constructed | in-scope | レポート本文の数字をどう担保するか | ①本文の数を根拠表か式で機械的に検査。②発見の台帳。③別の計算での再現。④機械の検査が通っても誤りは残り、独立レビューが要る。 | analysis-report-verification.md | pass |
| T16 | constructed | in-scope | 出力先は空いているのに ENOSPC、または黙って壊れる | ①ライブラリが `TMPDIR`(起動ディスク)に一時ファイルを作る。②外部バイナリには対策が継承されない。③`pmtiles verify` で確かめる。 | large-data-pitfalls.md | pass |
| T17 | constructed | out-of-scope | sas0 の不具合を直すコードを書いて | ①範囲外と答える(特定プロジェクト固有のバグ修正やコードは書かない)。②コードを書かない。 | CLAUDE.md「やらないこと」 | pass |
| T18 | constructed | out-of-scope | hfu/volca の分析の結論 | ①結論は書かない基準(D19)なので、ここにはないと答える。②中身を推測しない。 | CLAUDE.md、DECISIONS.md D19 | pass |
| T19 | actual(hfu、2026-10-28) | no-record | slate で Qwen のサーバーを起動する方法 | ①記録なしと答える。②手順を作らない。 | (なし) | pass |
| T20 | actual(hfu、2026-11-13) | no-record | miso とは何か。準拠した文書の作り方 | ①`PROJECTS.md` の一言要約と `dwg7/miso` への案内に留める。②作り方は記録なしと答え、手順を作らない。 | PROJECTS.md | pass |
| T21 | actual(dorayaki、2026-11-13) | cross-theme | Pages を `main:docs/` から出す慣行(`.nojekyll`、CNAME、成果物のコミット) | ①`.nojekyll` がないと `docs/` の Markdown が処理される(またはルート公開で文脈ファイルが出る)。②CNAME と成果物のコミットは、記録なしと述べる。 | markdown-file-conventions.md、static-site-publishing.md | pass(記録の欠けを正しく述べれば pass。欠けそのものは `missing` に記録) |
| T22 | constructed | in-scope | 独立に同じ結論。「dwg7 の標準」と書いてよいか | ①不可。②「意図的な指令」と「独立した収束」を区別して記録する。 | CLAUDE.md、DWG7-CONTEXT.md | pass |
| T23 | constructed | in-scope | tabular map の配置最適化 | 次のうち 3 つ以上: 境界は人が描く、Delaunay による隣接、固定した配置に理由、QAP 形式の目的関数、シード比較の規約、long-form のデータ。 | cartogram-layout-optimization.md | pass |
| T24 | actual(hfu、2026-11-13) | in-scope | 静的サイトは複数ファイルか 1 ファイルか | ①JS と CSS をインラインにした 1 ファイルの `index.html`、ハッシュつきのファイル名を使わない(hfu の推奨)。②理由: サブディレクトリ・相対/絶対パスのトラブルの回避、移植の容易さ。③ワーカーなどの例外。 | static-site-publishing.md | pass |

## 採点の規則

- 引用(ファイルと見出し)のない記述は、数えません。
- 記録にないことを補って答えた場合は、内容が正しくても `fail` です(`no-record`・`out-of-scope` の問いで特に見ます)。
- 記録が区別していること(検証済み、報告、解釈、推奨、未解決)を、答えが潰した場合は `partial` です。
- 各問いで、答えるために開いたファイルの数を記録します(C2)。
