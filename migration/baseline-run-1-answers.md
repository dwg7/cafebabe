# 基準線の実行 1: 回答の全文

`migration/acceptance-tests-v0.md` の 24 問に、別のエージェントが旧構造(コミット `53fea33`)だけを読んで答えた
ものです(2026-11-13)。期待する答えは見せていません。採点と所見は [`baseline-run-1.md`](baseline-run-1.md)。
以下は回答者の出力そのままで、cafebabe は手を入れていません。

### Q01
- answer:
  - 先行例(1) snow-hokkaido: Open MCT 4.3.1 の下に MapLibre 計器と tabularmaps 計器(`tabularmaps/do` の描画コアを vendoring)を別リーフで並べる構成(`PROJECTS.md › dwg7 org`)。ただし「実装中」とされ(`patterns/open-mct.md › 限界と選ぶ基準`)、実装知見は「後で戻す予定」でまだ戻っていない(`CLAUDE.md › 既知のピア`)。
  - 先行例(2) sas0: MapLibre を Open MCT 計器としてネイティブ埋め込み(`patterns/maplibre-gl-js-embedding.md › map.remove()を確実に呼ぶ`、`同 › iframe埋め込みよりネイティブ埋め込みを検討する`)。do の tabular map を既存計器の表示切替として採択し、`docs/vendor/tabularmap/` にコミットハッシュつきで vendoring(`patterns/interoperability.md › 部品を他のダッシュボードに採択してもらう時は…`)。
  - 先行例(3) do-survey: 描画コア(`TabularMap.create`)だけ vendoring し、ツリーと provider は自前(`patterns/interoperability.md › 同・変種(2026-09-24)`)。
  - ノウハウ: view destroy 時に `map.remove()`(WebGL コンテキストのリーク防止)(`patterns/maplibre-gl-js-embedding.md › map.remove()…`)。部品は「取得・配色・置き場所」を注入可能に(`patterns/interoperability.md › 同`)。provider 三点セット+独自 type+自前描画、`composition: []` は不要(`patterns/open-mct-object-model.md › 唯一、一貫して信頼できる拡張ポイント`)。Telemetry API を使わず view 内で fetch+setInterval、指標契約 `{label, unit, asOf, min, max, values}`(`patterns/open-mct-telemetry.md › request()/subscribe()`)。Espresso 内では `--surface: transparent`、浮いたパネルには専用の面色トークン(`patterns/open-mct-operations.md › フルスクリーン／キオスクモードのパターン`)。`start()` 前に時刻系を設定(`patterns/open-mct-operations.md › 起動時のreading 'key'エラーの原因は…`)。
  - 未再現の報告: Open MCT 計器内の `raster-resampling: 'nearest'` が組み込みブラウザで真っ黒(snow-hokkaido 報告、cafebabe は再現を試みていない)(`patterns/maplibre-gl-js-rendering.md › raster-resampling: 'nearest'が…`)。
- files: README.md, PROJECTS.md, CLAUDE.md, patterns/open-mct.md, patterns/open-mct-object-model.md, patterns/open-mct-telemetry.md, patterns/open-mct-operations.md, patterns/interoperability.md, patterns/maplibre-gl-js-embedding.md, patterns/maplibre-gl-js-rendering.md
- confidence: medium
- gaps: 「MapLibre 計器と tabular map 計器を並べる」ことを主題にしたパターンは無く、知見は6ファイルに分散。snow-hokkaido の実装知見は未収録。README の索引からは snow-hokkaido に辿れない(PROJECTS.md か CLAUDE.md を開く必要がある)。

### Q02
- answer:
  - バンドラは必須ではない。記録されている形は4つ。
    1. CDN 直読み: v6 は ESM のみで `dist/maplibre-gl.js` は 404。`<script type="module">` で `dist/maplibre-gl.mjs` を読む(plateau-juice 報告、cafebabe も v6.11.2 で確認)(`patterns/maplibre-gl-js-embedding.md › MapLibre GL JS v6 をバンドラで取り込むなら…・CDNで直接読む場合`)。
    2. 並置(バンドラなし): `docs/vendor/maplibre-gl/` に mjs・worker・css を置き import map を相対パスで向ける。ワーカーは隣から解決され `setWorkerUrl` は不要(`同 › 追記(2026-11-13、dorayakiの報告)`)。
    3. バンドラ使用: `import.meta.url` がバンドル先になり、存在しないワーカーを探して 404。`…/maplibre-gl-worker.mjs?url` を import して `maplibregl.setWorkerUrl()`(`同 › 解決`)。6.12.x 以前はワーカーが shared を import するので閉包ごと運ぶ。6.13.0 以降は自己完結で1行で足りる(`同 › 訂正・追記(2026-11-13)`)。
    4. 1ファイル化: ワーカーだけ隣に置き、`setWorkerUrl(new URL("maplibre-gl-worker.mjs", document.baseURI).href)`(`同 › 追記(dorayaki)`)。
  - 失敗の見え方: ラスタは表示される/GeoJSON もベクタも沈黙/`map.on('error')` は何も出さない/`isSourceLoaded` が false のまま/`idle` が来ない/ビルドは警告なし(`同 › 問題`)。doverture は開発サーバーのアクセスログの 404 で確定(`同 › 実例`、`patterns/local-dev-pitfalls.md › ローカル開発サーバーのアクセスログを潰さない`)。
  - 確度の区別: 3 の 6.13.0 以降の話は cafebabe の再検証だが「ビルド成果物の確認まで、ブラウザ実行は未確認」。2 と 4 は dorayaki の報告で、ローカル配信のみ・GitHub Pages 上は未確認・コード未 push。
  - 紛らわしい症状: 非表示のブラウザペインでは `load` が発火しない。アクセスログ(ワーカーが 200 か 404 か)で区別(`patterns/agent-execution-gotchas.md › 自動化ブラウザツールの非表示・バックグラウンドタブは…`)。
- files: README.md, patterns/maplibre-gl-js-embedding.md, patterns/static-site-publishing.md, patterns/local-dev-pitfalls.md, patterns/agent-execution-gotchas.md
- confidence: high
- gaps: バンドラなし/1ファイルの形は GitHub Pages 上で未確認。6.13.0 以降のブラウザ実行は cafebabe では未確認。パターンの見出しが「バンドラで取り込むなら」なので、バンドラ不要の答えは同じ節の末尾の追記まで読まないと見つからない。

### Q03
- answer:
  - 原因(do-survey D47 が特定、cafebabe が 4.3.1 の最小ページで再現): 起動時に URL と時刻を同期する処理(`setUrlFromTimeApi`)が `openmct.time.getTimeSystem().key` を読む。`UTCTimeSystem()` を `install` するだけでは時刻系が選択されず `undefined` になる。Open MCT 本体の不具合ではなく利用側の設定漏れ(`patterns/open-mct-operations.md › 起動時のreading 'key'エラーの原因は、時刻系を選んでいない設定漏れだった(2026-10-22)`)。
  - 対処: `openmct.start()` の前に `openmct.time.setTimeSystem('utc');` と `openmct.time.setMode('fixed', { start: Date.now() - 24*60*60*1000, end: Date.now() });` を呼ぶ(時刻を使わないダッシュボードでも。値に意味は無くてよい)。副作用として URL に `tc.*` が付く(同節)。
  - cafebabe の再現結果: 時刻設定なし → エラーが出て `'start'` コールバックが発火しない。時刻設定あり → エラーなし、`'start'` 発火(同節)。
  - 推論・未検証: これまで「既知の無害なエラー」としてきた記述、mapterhorn-monitor の `'start'` 不発、kikimimi の `router.setPath()` 不効も同じ原因の「可能性が高い」が、その構成では未検証(同節・含意)。
  - 未解決の食い違い: sas0 D74 は、エラーが出ているのに `'start'` は発火し `setPath` も効いたと記録(同節・食い違い)。
  - 検証の注意: 内蔵ブラウザのコンソールは同じタブでページを切り替えても消えない。比較は新しいタブで(同節・検証の落とし穴)。
- files: README.md, patterns/open-mct-operations.md
- confidence: high
- gaps: 同じファイルの上の節(`ブートストラップの落とし穴`)は今も「無害なコンソールエラー」「原因は特定できていない」と書いたまま(追記方式のため)。上だけ読むと古い結論で止まる。

### Q04
- answer:
  - 記録上は、どちらも前提にしない方がよい。
  - Display Layout: m3xx-fleet・sas0 は採用していない(kikimimi がコードを読んで確認、2026-09-16)。代わりに「単一の非永続 object provider+単一の view provider」で、`view().show(element)` 内に HTML テーブル・SVG 等を直接組む。kikimimi も同じ形にした(`patterns/open-mct-telemetry.md › Plot / Telemetry API — 結論はまだ出ていない`)。ただし Display Layout が実際に動かないことを試した記録ではなく、「相性が悪いのでは」という懸念を踏まない回避である(同節)。
  - Plot: 結論は出ておらず、証拠が対立している。sas0(4.3.0-rc1)は無描画・無エラーのまま自前 SVG に切り替えた。claude-mct は本体アプリ(4.2.0)では描画できたが、最小再現環境では全バージョンで描画されなかった。原因は未特定(同節)。
  - 確定したバグ: `telemetry.values` は domain(時間軸)を先、range を後に書く。逆だと `getXVal is not a function`(同節)。
  - 実践的な結論: 高機能ビューは自分のバージョン・構成で試すまで動作を仮定しない。素の SVG/Canvas を自前のビューで描くのが実績ある代替(同節)。
  - cafebabe の解釈(案、2026-10-20): 「Plot・PlanLayout・Display Layout を前提にした設計は避ける」(`patterns/open-mct.md › 限界と選ぶ基準`)。
- files: README.md, patterns/open-mct.md, patterns/open-mct-telemetry.md
- confidence: high
- gaps: Display Layout を実際に試して失敗した記録は無い(避けた実績のみ)。「+Create された永続オブジェクトなら Plot が動くか」は未検証。

### Q05
- answer:
  - 役割の分離(hfu 承認の推奨): CLAUDE.md/README.md は現在形(今何が正しいか)、DECISIONS.md は過去形(経緯、追記専用)。混入に気づいたら明示的に redirect する(`patterns/markdown-file-conventions.md › 「今何が正しいか」と「なぜそうなったか」を同じファイルに混ぜない`)。
  - 決定ログ(hfu 承認の推奨): D1, D2… の通し番号で追記のみ。判断が変わっても古いエントリは残す。mapterhorn-japan-bridge は各エントリに `Status` と `Resume prompt` を付ける(`同 › 決定ログは追記専用、既存エントリを書き換えない`)。
  - HANDOVER.md の肥大化: アーカイブ退避+圧縮/定期的に書き直す/索引化の3通りがあり、未収束(`同 › 肥大化への対処`)。cafebabe 自身は、書き直す前に恒久的価値のある情報を CLAUDE.md や DECISIONS.md に定着させる(`CLAUDE.md › 日常的な作業`、`DECISIONS.md › D11`)。
  - 保守(hfu 承認の推奨): ドキュメント更新はコードと同じコミット・同じターンで(`patterns/markdown-file-conventions.md › ドキュメント更新はコードの変更と同じコミット・同じターンで行う`)。見出しを変えたら grep で相互参照を同期(`同 › 見出しのリネームは…`)。真実は1箇所に集約し他はポインタ(`同 › 1箇所に真実を集約し…`)。
  - 相談の実績: m3xx-fleet-ops から長期運用エージェントの3ファイル構成の相談を受け、`markdown-file-conventions.md` と `gatekeeping.md` を紹介した(`CLAUDE.md › 既知のピア`)。
- files: README.md, CLAUDE.md, DECISIONS.md, patterns/markdown-file-conventions.md
- confidence: high
- gaps: 「長期運用エージェント向け」に絞った専用パターンは無い。m3xx-fleet-ops がその後どう構成したかの結果は記録なし。

### Q06
- answer:
  - 原因: macOS の TCC(プライバシー保護、リムーバブルボリュームへのアクセス制御)による拒否。`Permission denied` ではなく `Operation not permitted` という文言がその手がかり。GUI アプリは許可ダイアログを出せるが、SSH のヘッドレスセッションには出す経路が無い(`patterns/local-dev-pitfalls.md › macOSでSSH経由の外部ボリュームアクセスが…`)。
  - 対処: System Settings → Privacy & Security → Full Disk Access で、`/usr/sbin/sshd` ではなく `/usr/libexec/sshd-keygen-wrapper` に付与する(sshd 本体に付けても「効かないことがある」)。Finder の選択には出ないので `Cmd+Shift+G` でパスを直接入力する。付与後は SSH を切断して再接続する(同節)。
  - 実例: slate で `/Volumes/Migrate-2025-04`・`/Volumes/pmtiles-store` が解決(2026-09-12)(同節・実例)。
- files: README.md, patterns/local-dev-pitfalls.md
- confidence: high
- gaps: 実例は1台(slate)のみ。macOS のバージョンは記録されていない。

### Q07
- answer:
  - 実用にならない、というのが記録。`raw.githubusercontent.com` は `accept-ranges: bytes` を返すが、`Range: bytes=0-99` を送っても 206 ではなく 200(全文)が返る。大きいファイルでは毎回全文ダウンロードになり致命的(`patterns/large-data-pitfalls.md › GitHub rawはaccept-rangesヘッダーを返すが、実際はRangeリクエストに応答しない`)。
  - 確認方法: 採用前に `curl -H "Range: bytes=0-99"` で実際のステータスコードを見る(同節・解決)。
  - 実例: stars-fd が 76KB・530KB の2ファイルで実測。vientiane-planning-map は同じ問題を見つけ、ローカルパス方式に切り替えた(同節・実例)。
  - 代替として記録されているもの: PMTiles+Martin の `pmtiles.sources`(height-coverage)(`patterns/maplibre-gl-js-data-serving.md › 大容量データはPMTiles + Martinのpmtiles.sourcesで`)。
- files: README.md, patterns/large-data-pitfalls.md, patterns/maplibre-gl-js-data-serving.md
- confidence: high
- gaps: 実測の日付と再確認の記録が無い(現在も同じ挙動かは不明)。GitHub Pages が Range に応答するかは、開いた範囲では記録なし。

### Q08
- answer:
  - そのまま使ってはいけない。Earth Search の 2026 年の item では、`sentinel-2-l2a` も `sentinel-2-c1-l2a` も `raster:bands` に `scale: 0.0001, offset: -0.1` と書いてあるが、実ファイルは揃っていない。`c1-l2a` の COG は自身のメタデータに scale/offset を持つ。旧 `l2a` の COG は持たず、DN が一律 1000 低い。旧 `l2a` に STAC の値を当てると反射率が負になり NDSI が壊れる(`patterns/data-provenance-source-verification.md › STACのraster:bandsのscale/offsetを信じず、各COG自身のメタデータを読む`)。
  - 対処: scale/offset は各 COG 自身から読む(`gdalinfo` の `Offset:`/`Scale:`、または `band.GetOffset()`)。STAC の値は突き合わせの対象に留める(同節・解決)。
  - 重複排除: 同一撮影の重複排除は `s2:product_uri` で行う。`s2:datatake_id` は同じパスの全タイルが共有するので、重複排除キーではなくパス単位のグループキー(同節・解決)。
  - 確度の区別: snow-hokkaido の報告(2026-10-18)。cafebabe の再検証は1撮影・1窓(2026-10-10、S2A、54TXP、B04)のみで、全画素 +1000 と `s2:product_uri` の一致を確認。他の baseline・タイルへの一般化は未検証。「同じパスが北海道で 27〜28 タイル」は cafebabe 未検証。タグは「個別事情」(同節・タグ、実例)。
- files: README.md, patterns/data-provenance-source-verification.md
- confidence: high
- gaps: 他の baseline・他のタイル・他の STAC カタログでは未検証。

### Q09
- answer:
  - 基準は D19(hfu 承認、2026-09-09)。`dwg7/cafebabe` は Public で、書いたものは誰でも読める(`DECISIONS.md › D19`)。
    1. 書いてよい: プロジェクト名・URL(PRIVATE タグを明記)・技術構成レベルの一言要約(何のデータソースを使い、何を作っているか)。
    2. 書かない: その分析・活動から得た結論や戦略の中身。当該 PRIVATE リポジトリ内に留める。
    3. 迷う場合: 登録前に該当セッション本人へ「この要約で公開して問題ないか」を確認する。
    (`DECISIONS.md › D19 決定`、`CLAUDE.md › PRIVATEリポジトリの情報を書くときの基準(D19)`)
  - 追記(2026-09-13): プロジェクトに関わる第三者にも同じ基準を適用する(同意の無い識別情報は書かない)(`DECISIONS.md › D19 追記`、`HANDOVER.md › Status`)。
  - 関連する実例: Pages をリポジトリルートから公開すると CLAUDE.md 等も公開物になる(rpi3-server-guide)(`patterns/markdown-file-conventions.md › GitHub Pagesをリポジトリルートから公開すると…`)。
  - 保留: 既存の2件(claude-mct・kitaphoto17-navara)は遡った再点検をしていない(目視では問題なしと判断)(`DECISIONS.md › D19 保留事項`)。
- files: README.md, CLAUDE.md, DECISIONS.md, HANDOVER.md, patterns/markdown-file-conventions.md
- confidence: high
- gaps: なし

### Q10
- answer:
  - 評価は `patterns/open-mct.md` に2つの節で記録されている。「強み」は採用側プロジェクトの声。「限界と選ぶ基準」は cafebabe の解釈(2026-10-20)で、「推論を含む」と明記(`patterns/open-mct.md › Open MCTの強み`、`同 › 限界と選ぶ基準`)。
  - 選ぶ基準(案):
    1. ライブ・時系列・多数ストリームを扱うなら有力(Telemetry API の出番がある、claude-mct 型)。
    2. 静的なスナップショットを少数の計器で見せるなら必須ではない。選ぶ理由は「殻(ツリーとビュー切り替え)、運用者の語彙、横断的な一貫性」と自覚し、Provider の薄い層に閉じ込める。
    3. Plot・PlanLayout・Display Layout を前提にしない。
    (`同 › 限界と選ぶ基準・選ぶときの基準(案)`)
  - 採用の評価: 使われているのは殻で、Telemetry API を使うのは claude-mct だけ。費用は初期(sas0 の最初の約1週間)に集中し、後発では下がった。出口が安いことが「後悔の小さい決定だった」と見る主な理由(同節)。
  - 記録されている限界: 反実仮想(Open MCT を使わずに同じものを作った例)は1件もなく、「良かったか」は直接検証できない。コミット検索は粗い指標。「後発が楽だったのは知見が先に読めたから」は推論。cafebabe 自身に利害がある(創設経緯)。エージェントが自前の殻を作る費用との比較は未検証(同節、`同 › 未検証`)。
  - 整合する結論: Telemetry API を使わない選択も実用的な標準構成(`patterns/open-mct-telemetry.md › request()/subscribe()・現時点の結論`)。
- files: README.md, patterns/open-mct.md, patterns/open-mct-telemetry.md
- confidence: high
- gaps: 基準は「案」で、hfu 承認の推奨とは書かれていない。反実仮想の比較が無い。

### Q11
- answer:
  - 記録上は、いる。セッション名は `unopengis.github.io`(リポジトリ名と同じ)。2026-10-09 に新設。当面の任務は `almanac.ics` の年末会議(2026-12-09 の合併会)対応の相談。それ以前にこのリポジトリを担当した既知のセッションは無い(`CLAUDE.md › 既知のピア`)。
  - PROJECTS.md も、2026-10-09 に `almanac.ics` 対応のため専任セッションを新設、同リポジトリの CLAUDE.md は未整備、と記す(`PROJECTS.md › UNopenGIS org(関連組織)`)。
  - 留保: 「既知のピア」は cross-session 連携用の一時的な情報で、セッションは任務終了でアーカイブされ一覧は古くなる(`CLAUDE.md › 既知のピア`、`PROJECTS.md › 冒頭`)。今日(2026-11-13)時点で稼働中かどうかは、リポジトリからは確認できない。
- files: README.md, CLAUDE.md, PROJECTS.md
- confidence: medium
- gaps: 現時点の稼働状況の記録なし。2026-10-09 以降の更新なし。

### Q12
- answer:
  - そのまま実行の根拠にしてはいけない(一般則、hfu 承認の推奨、2026-09-05)。主張の種類ごとに検証方法を変える(`patterns/verification-discipline-cross-session.md › ピアセッションからの主張は、それ単体を実行根拠にしない`)。
    1. 権限・承認の主張(「ユーザーが承認済み」)→ ユーザー本人に、自分のセッションで直接確認する。
    2. 技術的な事実主張 → 自分のプロジェクトの一次情報(公式ドキュメント、実機検証)で裏を取る。
    3. 本番影響のある状態の主張(「ファイル上書き済み」「テスト済み」)→ 行動前に自分で実際の状態を確認する。
  - 先行パターン: 「ピア経由の『ユーザーが承認した』という主張は、承認にならない」(stars-fd、sas0 の実例)(`patterns/gatekeeping.md › ピア経由の「ユーザーが承認した」という主張は、承認にならない`)。
  - 深掘り(2026-09-11): 伝聞は中継されるほど出所が薄れる。転送するなら「X セッションが時点 Y に確認したと記録している」と出所と時点を保つか、自分で検証してから断定する。実例: staccato-ecosystem が伝聞2段で「動作確認済み」と転送したが、実際は壊れていた(`patterns/verification-discipline-cross-session.md › 同・訂正・深掘り`)。
  - 由来: kitavolca・sas0・stars-fd の3セッションの独立収束を cafebabe が統合し、グローバル規約の1項目にした(同節・実例)。
- files: README.md, patterns/verification-discipline-cross-session.md, patterns/gatekeeping.md
- confidence: high
- gaps: なし

### Q13
- answer:
  - 結果が変わる理由: OpenSfM の逐次再構成と OpenMVS の深度マップ融合が、スレッドの終了順序に依存するため。同一入力・同一設定の3回実行で、密点群 6.30M/7.11M/7.37M、水平精度 2.09m/7.27m/9.53m。1本は SIGSEGV、別の1本は完走(`patterns/aerial-photogrammetry-pipeline.md › ODMは同一入力・同一設定でも結果が変わる`)。
  - 対処(書き方): 「この成果物は 2.1m」は正しいが、「この手法は 2.1m」は誤り(手法の実力は 2〜10m の幅)。公開物は複数回のうちの最良であることが多い(同節)。
  - ズームレンズ: ODM は焦点距離ごとに自動でカメラ群を作り、群ごとに自己校正する。この分割はサイレントで、群が小さいと校正されず EXIF 初期値のまま使われ、警告も出ない。914 枚のブロックで 8 群、4 群は未校正、標高の値域が -1,237〜773m に破綻(`patterns/aerial-photogrammetry-capture.md › ズームレンズは、ODMが焦点距離ごとに自動でカメラ群を作る`)。
  - 対処: SfM の前に焦点距離の混在を確認する。`tools/check_camera_drift.py` で、最適化後の焦点距離を EXIF 初期値と比べる。単一焦点距離に絞ると、28mm のみ(914→370 枚)で高さ残差 56.5m→17.9m(同節・解決)。
  - 出所: いずれも tokachi20260911 の実測(2026-09-11〜15)。実例は1プロジェクト(両節・実例)。
- files: README.md, patterns/aerial-photogrammetry-pipeline.md, patterns/aerial-photogrammetry-capture.md
- confidence: high
- gaps: 実例は tokachi20260911 のみ。ODM のバージョンは、開いた節には書かれていない。結果を決定的にする方法は記録なし。

### Q14
- answer:
  - 理由: macOS 標準の bash は 3.2 で、`declare -A`(連想配列)が無い。GNU bash 4+ 前提のスクリプトは動かない(`patterns/local-dev-pitfalls.md › macOS標準のbash 3.2にdeclare -A(連想配列)は無い`)。
  - 対処: 移植性を優先するなら `case` 文で代替する(同節・解決)。
  - 実例: kitavolca が `scripts/fetch-vlcm.sh` で `case` 文による代替を採用(同節・実例)。
- files: README.md, patterns/local-dev-pitfalls.md
- confidence: high
- gaps: 記録されている対処は `case` 文のみ(新しい bash を入れる等の選択肢は記録なし)。実例1件。

### Q15
- answer:
  - do-survey の寄稿(2026-10-22)による検査ハーネス。タグはすべて「個別事情(do-survey)」で、他プロジェクトでの再現は未確認(`patterns/analysis-report-verification.md › 冒頭`)。
    1. 数字の機械検査: `scripts/check_numbers.py` が、本文の2桁以上の数と小数を拾い、同じフォルダの根拠表にあるか、`checks.csv` の式(`expr`)・参照(`ref`)で裏付けられるかを確かめる。導入前は 368 のうち 45 が根拠表に無かった。わざと変えた数を拾うことも確かめた(`同 › レポート本文の数字は…`)。
    2. 会話で計算した数は、生成スクリプトで根拠表にするまで根拠ではない(`同 › 会話で計算した数は…`)。
    3. 発見の台帳 `findings.csv`: 1行1発見、状態は確認/集計/推定/否定/置き換え(`同 › 発見の台帳`)。
    4. 台帳の主張を、根拠表を作るスクリプトとは別の計算で元データから再現する。`PYTHONHASHSEED` を変えて一致を確認(`同 › 台帳の主張を、根拠表とは別の計算で…`)。
    5. 人が書いた仕分け表と計算で求めた集合が、ちょうど一致しなければ止める(`同 › 人が書く仕分けの表と…`)。
    6. 独立レビュー: 別文脈のレビュアー4人が読むだけ。指摘は作り手が元データで確かめてから直す(`同 › 機械の検査が全部通っても誤りは残る`)。
  - 限界: どの項目の数かまでは見ない。検査が全部通っても、起点の年の選び方・項目の取り違え等は残り、誤りは検査の範囲外の本文に集まった(同・1 と 6 の節)。
- files: README.md, patterns/analysis-report-verification.md
- confidence: high
- gaps: 実例は1プロジェクトのみ。スクリプト本体は do-survey 側にあり、ここには無い。

### Q16
- answer:
  - まず疑うのは、外部ライブラリが暗黙に `TMPDIR`(通常は起動ディスク)へ一時ファイルを作ること。`pmtiles`(Python)の `Writer` は `tempfile.TemporaryFile()`(パス引数なし)でタイルデータをバッファする。出力ボリュームに 900GB 以上の空きがあっても、起動ディスク(空き約 100GB)が先に枯渇して `ENOSPC` になる(`patterns/large-data-pitfalls.md › 外部ライブラリが暗黙にTMPDIR(起動ディスク)へスクラッチファイルを作る`)。
  - 対処: スクリプト冒頭、ライブラリのインスタンス化より前に `os.environ.setdefault('TMPDIR', <出力先ボリューム上のパス>)`(同節・解決)。
  - この対策はプロセスをまたいで継承されない。shell out する外部バイナリ(`pmtiles`、`gdalwarp`、`ogr2ogr`、`tippecanoe` 等)は、それぞれ `TMPDIR` が export されているかを確認する(同節)。
  - エラーなく終わったのに壊れていた場合: 同じ原因のサイレント破損。`pmtiles cluster`(Go CLI、`os.TempDir()` 依存)が、起動ディスクの枯渇中にエラーなく完了し、310GB のアーカイブが破損した。後から `pmtiles verify` で `Tile data offset=... out of bounds` と分かった(同節・実例)。
  - 教訓: 処理後に `pmtiles verify` 等を実行する。「エラーなく終わった」を「正しく書き込まれた」の証拠にしない(同節・解決)。
  - 出所: mapterhorn-japan-bridge の実例(3回)。タグは一般則(同節)。
- files: README.md, patterns/large-data-pitfalls.md
- confidence: high
- gaps: 実例は mapterhorn-japan-bridge の1プロジェクト。tippecanoe・GDAL 個別の一時ファイルの挙動は、名前が挙がるだけで実測の記録は無い。

### Q17
- answer:
  範囲外: このリポジトリは「特定プロジェクト固有のバグ修正やコードは書かない(ここは知見の集約場所であり、実装場所ではない)」と定めている(`CLAUDE.md › やらないこと`)。sas0 固有の知見と実装は sas0 自身のリポジトリ(https://github.com/dwg7/sas0)の CLAUDE.md/DECISIONS.md が一次情報源(`PROJECTS.md › 冒頭`、`PROJECTS.md › dwg7 org`)。参考になりうる横断知見としては、sas0 の状況図に関する記述が `patterns/maplibre-gl-js-data-serving.md › ランタイムハイドレーション`、`patterns/maplibre-gl-js-embedding.md › ホバー情報は固定ドッキングパネルで表示する`・`map.remove()を確実に呼ぶ`、`patterns/open-mct.md › Open MCTの強み` にある。
- files: CLAUDE.md, PROJECTS.md, patterns/maplibre-gl-js-data-serving.md, patterns/maplibre-gl-js-embedding.md, patterns/open-mct.md
- confidence: high
- gaps: 「不具合」の内容が質問に無く、sas0 の状況図の現在の不具合に関する記録もこのリポジトリには無い。

### Q18
- answer:
  範囲外: D19 により、PRIVATE リポジトリの「分析・活動から得た結論や戦略の中身そのもの」は cafebabe に書かず、当該 PRIVATE リポジトリ内に留める(`DECISIONS.md › D19 決定`、`CLAUDE.md › PRIVATEリポジトリの情報を書くときの基準(D19)`)。記録されているのは技術構成レベルの一言要約だけ。`hfu/volca`(PRIVATE)は、北海道の常時観測火山9火山の防災計画・避難計画 PDF を収集・横断分析し、北海道地方測量部と dwg7 への戦略を立案する(`PROJECTS.md › hfu 個人名前空間`)。この要約は基準1の範囲内と hfu が是認した(`DECISIONS.md › D19 決定`)。別に、volca が検証規律について寄せた実例(自分たちの持ち物についての推論の誤り4例)は、`patterns/verification-discipline-cross-session.md › ピアセッションからの主張は…・訂正・深掘り(2026-09-11)` にあるが、防災計画の評価の中身ではない。
- files: DECISIONS.md, CLAUDE.md, PROJECTS.md, patterns/verification-discipline-cross-session.md
- confidence: high
- gaps: 意図的に収録していない(D19)。

### Q19
- answer:
  記録なし: 追跡対象の Markdown 全体を「qwen」「llama」「ollama」「mlx」「LLMサーバ」で検索したが、該当は無い。slate について記録されているのは次の3点だけ。(1) hfu の個人マシンで、mapterhorn-japan-bridge 等の生データの保管先。SSH 経由の外部ボリュームの TCC 問題の実例(`patterns/local-dev-pitfalls.md › macOSでSSH経由の外部ボリュームアクセスが…`)。(2) mapterhorn-japan-bridge の進捗公開で「slate 側の生データには触れず」という言及(`patterns/unattended-progress-visibility.md › 実例`)。(3) `patterns/agent-repository-boundaries.md` に、ローカルマシン(slate)のディレクトリパス名への言及(grep の該当のみ。本文は未読)。
- files: patterns/local-dev-pitfalls.md, patterns/unattended-progress-visibility.md, patterns/agent-repository-boundaries.md(grep の該当のみ)
- confidence: high
- gaps: ローカル LLM の運用に関する知見が、リポジトリに全く無い。

### Q20
- answer:
  - miso とは(一言要約のみ記録): 人と AI が時間をかけて醸す知識を、1つの Markdown ファイル(境界を持つエージェントが携行する「宇宙」)に収める方法。運用型と探索・理解型がある。旧称 kcaim(2026-11-07 に `dwg7/kcaim` から改称、旧 URL は転送)。CC0 1.0、2026-10-27 作成。リポジトリは https://github.com/dwg7/miso (`PROJECTS.md › dwg7 org`)。
  - 関連して登録されているもの: kcai(出典つきの短い Markdown「踏み跡」を共有する原則・形式・流れ、BYOA)、miso-geo(Markdown の `## geometry` に GeoJSON+小さな MapLibre ビューア)、kcai-terrio(正本は `miso/terrio.md`)(`PROJECTS.md › dwg7 org`)、universe(公開できる出典に基づく miso のファイルを集め `CATALOG.md` を付ける)(`PROJECTS.md › hfu 個人名前空間`)。
  記録なし: 「miso に準拠した文書の作り方」(必須の節、形式、検査方法など)は、このリポジトリのどのファイルにも無い。`patterns/` に miso を扱うテーマは無く、他の言及は miso-geo の Vite 構成に触れる2箇所だけ(`patterns/maplibre-gl-js-embedding.md › 訂正・追記(2026-11-13)`、`patterns/static-site-publishing.md › 他の選択との関係`)。作り方は `dwg7/miso` 自身を見る必要がある(`PROJECTS.md › 冒頭`)。
- files: README.md, PROJECTS.md, patterns/maplibre-gl-js-embedding.md, patterns/static-site-publishing.md
- confidence: high(記録が無いことについて)/ medium(定義は一言要約のみ)
- gaps: miso の仕様・準拠文書の作り方・実例のいずれも未収録。README の索引にも miso は出てこない。

### Q21
- answer:
  - 有効化: `gh api -X POST repos/{owner}/{repo}/pages -f "source[branch]=main" -f "source[path]=/docs"` で完結する。`pages/builds/latest` の `.status` が `"built"` になるまでポーリング(tabularmaps/do)(`patterns/markdown-file-conventions.md › GitHub Pagesの有効化はgh apiで完結できる`)。
  - `.nojekyll`: 無い状態で Markdown を `docs/` 配下に置くと、フロントマターが無い限り Jekyll が変換せず、生テキストのまま配信される(sas0 D65 で実際に踏んだ)。横断ドキュメントは `docs/` の外に置く(`同 › 横断ドキュメントは自分のDECISIONS.mdに混ぜず、独立させる`)。
  - 公開元: リポジトリルートから公開すると CLAUDE.md・DECISIONS.md も公開物になる。`docs/` に限定すれば配信対象外。初回 push の前に走査する(rpi3-server-guide)(`同 › GitHub Pagesをリポジトリルートから公開すると…`)。
  - `.gitignore` の `data/` は `docs/data/` まで無視する。`/data/` と書く(plateau-juice)(`patterns/local-dev-pitfalls.md › .gitignoreのdata/は…`)。
  - キャッシュ: CSS/JS は 10 分(`max-age=600`)(`patterns/open-mct-operations.md › フルスクリーン／キオスクモード・小ネタ`)。デプロイ直後は、CDN が古い 404 を返し続けることがある(stars)(`patterns/aerial-photogrammetry-pipeline.md › 追加知見(stars、GitHub Pages側の類似の罠)`)。
  - Free プランの Private リポジトリでは Pages を有効化できない(422)(`patterns/unattended-progress-visibility.md › 副次的な効能`)。
  - 成果物の形: 1ファイルの `index.html`、ハッシュつきファイル名を使わない(hfu 推奨、2026-11-13)(`patterns/static-site-publishing.md › 静的サイトは…`)。
  記録なし: CNAME(カスタムドメイン)の扱いの記述は無い(全ファイル検索で該当 0。`dwg7.unopengis.org/<リポジトリ>/` というサブパスの言及のみ: `patterns/static-site-publishing.md › 状況`)。「ビルド成果物を docs/ にコミットするか」を定めた慣行の記述も無い(実例として dorayaki の `docs/maplibre-gl-worker.mjs`、sas0 の `docs/vendor/tabularmap/`、plateau-juice の `docs/data/grid.json` がコミットされている、という個別の言及のみ)。
- files: README.md, patterns/static-site-publishing.md, patterns/markdown-file-conventions.md, patterns/local-dev-pitfalls.md, patterns/open-mct-operations.md, patterns/aerial-photogrammetry-pipeline.md, patterns/unattended-progress-visibility.md, patterns/interoperability.md, patterns/maplibre-gl-js-embedding.md
- confidence: medium
- gaps: CNAME、`.nojekyll` を置く場所と手順、成果物のコミット方針(docs/ か Actions か)は未収録。`.nojekyll` が無いときの挙動の書き方が2ファイルで揃っていない(meta 参照)。Pages の知見が6ファイルに分散している。

### Q22
- answer:
  - 観測しただけで、そう書いてはいけない。標準化が「意図的な指令」か「独立した収束」かを区別して記録し、複数プロジェクトが独立に同じ結論に達したことを「dwg7 の標準規約」であるかのように書かない(`CLAUDE.md › dwg7の組織文脈・パターン化にあたって特に注意すること 2`、`DWG7-CONTEXT.md › 6. cafebabeへの期待 2`)。
  - 背景: dwg7 は「個人単位の多中心的協調」で、中央からのトップダウンの技術指令は無い。各プロジェクトの CLAUDE.md/DECISIONS.md が一次情報源(`DWG7-CONTEXT.md › 2. カルチャー・意思決定`)。MapLibre や PMTiles+Martin の普及も、強制された標準化ではない(`DWG7-CONTEXT.md › 3. 技術的な方針`)。
  - 補足(2026-09-06): 規約への昇格が禁止されているわけではない。独立収束は昇格の「根拠」に使ってよいが、昇格の「決定」は hfu を含めた形で行う。戒めているのは「確認も無く規約であるかのように書くこと」。実例は D15(3セッションの独立収束から `~/.claude/CLAUDE.md` を作った)(`DWG7-CONTEXT.md › 6. cafebabeへの期待 2・補足`)。
  - 書き分けの実例: stars は独立収束ではなく「助言→実装→検証」で、証拠の重みが異なると注記(`patterns/open-mct-object-model.md › Object Providerの構造・stars実例についての注記`、`HANDOVER.md › Known open items`)。
  - 矛盾する判断が見つかっても、無理に統一理論へ解消しない(`CLAUDE.md › dwg7の組織文脈 3`)。
- files: README.md, CLAUDE.md, DWG7-CONTEXT.md, patterns/open-mct-object-model.md, HANDOVER.md
- confidence: high
- gaps: なし

### Q23
- answer:
  - `patterns/cartogram-layout-optimization.md`(tabularmaps/do・cldr の寄稿、2026-09-17〜20。dwg7 外の実例)に次が記録されている。
    1. 全域を1つの目的関数(焼きなまし等)で解かない。境界(領土図)は人が描き、最適化は境界内の並び順とセル数の検算に限る。全域焼きなましでは「継ぎ目の迷子」が重み調整で消えなかった(`同 › 「全域を1つの目的関数で解く」より…`)。
    2. 境界ポリゴンが無いときの隣接関係: 代表点の Delaunay 三角分割+二段閾値(40km 以下は無条件、40〜85km は互いの3近傍のときのみ)(`同 › 行政境界データが無い場合の隣接関係は…`)。
    3. 読みやすさの判断は目的関数に入れず、ピン(人手固定)+理由コメント+決定ログへの転記(`同 › 人手で固定した配置には理由コメントを必須にし…`)。
    4. 自己検査: 実座標(緯度・経度)に基づく色で塗り、単調性の崩れを見る(`同 › 配置の妥当性は…`)。
    5. データ契約: 一次データは long-form(`placements[…]`)、2D 配列は派生物、空白セルは `structural_spaces` に明示(`同 › 一次データはlong-form…`)。
    6. 目的関数を QAP 形式 Σ F[i,j]·D[cell_i,cell_j] に揃え、1手評価を O(n) に。採点器と最適化器を共有(cldr)(`同 › 目的関数をQAP形式に揃えると…`)。
    7. 候補の比較は「A の最悪シードが B の最良シードを上回るか」(cldr)(`同 › グリッド候補の比較は…`)。
    8. オプションで出し入れする要素(北方領土6村)は外縁の1列に置く(`同 › オプションで出し入れする要素は…`)。
- files: README.md, patterns/cartogram-layout-optimization.md
- confidence: high
- gaps: 各パターンの実例は do か cldr の1件ずつ(タグは一般則)。重み・反復数などの具体値は先方のリポジトリ側にある。

### Q24
- answer:
  - 推奨(hfu、2026-11-13、タグは一般則): JS と CSS を `index.html` にインラインにし、1ファイルで完結させる。ファイル名にハッシュを付けない(`patterns/static-site-publishing.md › 静的サイトは、JSとCSSをインラインにした1ファイルのindex.htmlにまとめる`)。
  - hfu が挙げた理由は2つ: (1) 1ファイルにすることで回避できるトラブルが多い(サブディレクトリ、相対パスと絶対パス)。(2) 移植が非常に容易になる(同節・解決)。
  - 背景の問題: 複数ファイルのサイトは置き場所に依存し、サブディレクトリの下で資産が 404 になる。ハッシュつきファイル名はビルドのたびに変わり、参照の書き換えと古いファイルの掃除が要る(同節・問題)。
  - 例外: インラインにできない資産は残る。MapLibre GL JS 6 のワーカーは別ファイルで、`index.html` の隣に固定名で置き、ページ相対で指す。タイルなどのデータも別ファイル(同節・例外、`patterns/maplibre-gl-js-embedding.md › 追記(2026-11-13、dorayakiの報告)`)。
  - 留保: miso-geo と doverture は Vite のハッシュつき資産を使うが、推奨より前の独立した選択。「既存サイトの作り直しまでは求めていない」は cafebabe の理解で、hfu には未確認(同節・他の選択との関係)。
  - 実例の確度: dorayaki は報告(ローカル配信のみ、Pages 上は未確認)。rpi3-server-guide は、cafebabe が公開ページを確認したが、推奨に沿ったものか独立にそうなったのかは未確認(同節・実例)。
- files: README.md, patterns/static-site-publishing.md, patterns/maplibre-gl-js-embedding.md
- confidence: high
- gaps: Pages 上で確認済みの1ファイル MapLibre サイトの実例は、まだ無い。推奨が既存サイトに及ぶかは hfu に未確認。

### meta
- total distinct files opened: 28(README.md, CLAUDE.md, CONTRIBUTING.md, DECISIONS.md, HANDOVER.md, PROJECTS.md, DWG7-CONTEXT.md と、patterns/ の21ファイル。DECISIONS.md・DWG7-CONTEXT.md と patterns の8ファイルは該当節のみの部分読み。別に、追跡対象の Markdown 全体への `git grep` を7回実行。`scratch/`・`migration/` は未追跡で、検索対象に入っていない)
- anything in the repository that contradicted itself or looked stale:
  - `patterns/open-mct.md › 冒頭`: 「sas0が…フラッグシップ…このリポジトリでマスターを管理しています」「他リポジトリはここへのリンクを張り」は sas0 時代の文面のまま。同ファイルの `由来` と `PROJECTS.md › dwg7 org`(sas0=旧マスター管理者)と食い違う。同ファイルの表の sas0 `4.3.0-rc1` も古い(`patterns/open-mct-operations.md › 訂正(2026-10-20)` が「読み替えること」と指示)。
  - `patterns/open-mct-operations.md`: `ブートストラップの落とし穴` は「無害なコンソールエラー」「原因は特定できていない」のまま、下の `起動時のreading 'key'エラーの原因は…(2026-10-22)` が設定漏れと特定。2026-10-20 の訂正にも「起動時の無害なエラーも消えていない」と残る。「4.3.0 の正式版は一度も出ていない」も本文に残り、末尾で訂正(追記方式の帰結だが、上だけ読むと誤る)。
  - `patterns/open-mct.md › 限界と選ぶ基準`「Plot…は実績が無いか避けられている」と、`patterns/open-mct-telemetry.md`(claude-mct の本体アプリは 4.2.0 で Plot が正常に描画)・`patterns/open-mct-object-model.md › カスタムtype登録`(claude-mct は型ごとに Table・Plot を使い分け)の間に緊張がある。
  - `.nojekyll` が無いときの挙動: `patterns/static-site-publishing.md › 関連` は「Markdown が処理される」、`patterns/markdown-file-conventions.md › 横断ドキュメントは…` は「Jekyll が変換せず生テキストのまま配信される」。書き方が逆向き。
  - `HANDOVER.md`: 「Status as of 2026-09-24」のまま。patterns 36 ファイル(現在の追跡は 39)、PROJECTS.md 42 件(現在の表は 45 行)、ADR は D19 まで。「この期間にあったこと(2026-09-09〜24)」の中に 2026-10-02 の教訓調査が入っている。10〜11月の追加(do-survey 寄稿、kcai/miso 系、dorayaki、static-site-publishing)は反映なし。
  - `DECISIONS.md`: 最後が D19(2026-09-09、追記 09-13)。その後の構成変更(verification-discipline・data-provenance の分割、static-site-publishing の新設、Open MCT「限界と選ぶ基準」の追加)の ADR は見当たらない(見出し一覧で確認)。
  - `CLAUDE.md › 既知のピア(2026-09-09時点)`: 見出しの日付に対し、中身は 2026-10-22 までの追記を含む。claude-mct の現行担当セッションは「不明」。
  - `DWG7-CONTEXT.md › 4. 当面の方向性(2026年9月時点)`: kaga0「ちょうど着手段階」、zukaku「新設予定」など、時点が古い。
  - `README.md › 貢献の仕方`「まだ立ち上がったばかりです」は現状(39 パターンファイル)と合わない。
  - `patterns/maplibre-gl-js-embedding.md › MapLibre GL JS v6 をバンドラで…`: 本文の「ワーカー1ファイルでは足りない」は 6.12.x 以前に限る、と末尾で訂正(見出しと本文だけ読むと古い結論になる)。
- difficulties finding things:
  - README の索引は patterns のテーマ別で、プロジェクト名(snow-hokkaido、miso、dorayaki)や「Pages」「Open MCT+MapLibre」のような横断の問いからは引けない。Q01・Q21 は grep で6ファイル前後を渡り歩いた。
  - miso・kcai は PROJECTS.md にしか無く、README からは辿れない。
  - 最新の結論が長いパターンの末尾の「訂正・追記」にある(Q02・Q03)。見出しから結論を推測すると外れる。
  - Q11 のようなセッションの問いは CLAUDE.md(運用ガイド)にあり、README の案内(PROJECTS.md は担当一覧ではない)を読んで初めて行き先が分かる。
  - CNAME・成果物のコミット方針・Qwen は、全文検索で該当なしと確かめるしかなかった。
