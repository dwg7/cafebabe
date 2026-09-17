# HANDOVER

## Status as of 2026-09-09

パターン集は26テーマ(`patterns/`実ファイル数)。`ideas/`ディレクトリ(D16)——実装に
裏打ちされていない技術的アイデアを`patterns/`と分離して置く場所——も稼働中。`PROJECTS.md`
(dwg7組織11件+UNopenGIS org1件+hfu個人8件のリポジトリ)、`DWG7-CONTEXT.md`(組織文脈、
エージェンシー経済学セクション含む)、`STACCATO-CONTEXT.md`(staccato-spec 4パーティ
モデルと一般化拡張議論、ferspas57のnarrative libraryを追記済み)を保有。

D1〜D19まで19件のADRが完了。直近の3件: D17(Fableによる知見ベース全体レビューと
「局面 vs 大局」の区別)、D18(`patterns/open-mct.md`のテーマ別3分割)、D19(PRIVATE
リポジトリ情報をPublicなcafebabeに書く際の基準)。

**運用(D14)**: 判断待ち事項は2〜3件溜まったら通常の会話内でまとめて確認するのが基本形。
1件だけ即時性が高ければその場で確認してよい。5件を超える、または複数テーマにまたがる
棚卸しはPlanモードでのレビュー(D10方式)に切り替える。

**運用(D17)**: cafebabe自身の解釈・分析は知識創造として恒常的に歓迎される——hfuさんの
確認が無いことそれ自体を問題視しない。他者からの指摘(外部モデルによるレビュー等)を
評価する際は、「局面での方針」と「大局的な方針」を区別してから食い違いの有無を判断する
こと(詳しくは`CLAUDE.md`の該当節、経緯はD17参照)。

**2026-09-06〜07、hfuさん自身のOpen MCT学習に伴い、Open MCT利用5プロジェクト
(sas0・claude-mct・m3xx-fleet・mapterhorn-monitor・stars)への横断ヒアリングを実施した。**
カスタムtype登録・ツリーのDAG性・Object Providerの構造・addRootの形・Plot API失敗の
分類・request/subscribe実装、と多岐にわたる内容で`patterns/open-mct.md`を24KB→39KBまで
太らせた結果、D18でテーマ別3ファイルに分割した(下記Resolved参照)。starsからの相談には
このヒアリング結果を使って直接設計助言を行い、本番環境での実地検証まで得られた——
cafebabeが単に知見を集約するだけでなく、集めた知見を使って新規の相談に答え、その結果を
また知見として取り込むという循環が実際に機能した例。

## Resolved since last handover

- D1〜D15(創設〜グローバル`~/.claude/CLAUDE.md`策定協力)完了
- D16「`ideas/`ディレクトリ新設」完了。`ideas/osm-community-oauth.md`を初回エントリとして
  作成
- D17「Fableによる知見ベース全体レビューとその対応」完了(2026-09-06)。詳細はDECISIONS.md
  D17参照
- `patterns/agent-execution-gotchas.md`にm3xx-fleet-opsから新たに2件反映(2026-09-06):
  「短いtimeoutで更新→即reboot」の新規パターン、「権限分類器が自己の設定ファイル編集を
  ハードブロックする」パターンへの2件目のKnown use
- **Open MCT横断ヒアリング(2026-09-06〜07)完了**。`patterns/open-mct.md`に以下を追加
  (D18で分割後の新ファイルに反映済み):
  - カスタムtype登録・ツリーのDAG性・Object Providerの構造(単一役/多役)・addRootの形
    (`patterns/open-mct-object-model.md`)——5プロジェクトへのヒアリング
  - Plot API失敗の分類深掘り(sas0の壁は表現力ではなくメタデータ/設定面の問題だったと
    訂正確認)・request/subscribe実装状況(5プロジェクト中4プロジェクトがTelemetry API
    自体を不使用)(`patterns/open-mct-telemetry.md`)
  - starsからの新規相談(監視ダッシュボードの計器ごとオブジェクト分割)にヒアリング結果で
    設計助言→本番実装→検証完了、というcafebabe初の「助言の実地検証」ループが成立
- **D18「`patterns/open-mct.md`のテーマ別3分割」完了(2026-09-08)**。202行・39KBまで
  太った本文を、概要ファイル(51行)+3テーマファイル(object-model/telemetry/operations、
  各60〜82行)に分割。README.mdのリンクも更新。外部3リポジトリ(sas0/mapterhorn-monitor/
  claude-mct)はファイル全体へのリンクのみのため、リンク自体は変更不要と確認済み
- zukakuでの`.claude/rules/`symlink試行(D14)が完了、**否定的な結論**(D14追記、
  2026-09-08)。「公開リポジトリ+ローカルクローン前提のシンボリックリンク」は筋が悪いと
  hfuさん本人が判断。他プロジェクトへの展開は見送り
- zukakuからのPrint-in-Browser機能の独立リポジトリ切り出し相談に対応(2026-09-08)。
  差別化ポイント(window.print()+CSS named pages vs 既存プラグインのjsPDF単発出力)の確認、
  命名(リポジトリ名とnpmパッケージ名の分離)、cafebabeパターンとの関係(一般則は
  cafebabeに残し実装例のリンクだけ差し替える)の3点で意見を返した。hfuさんのレビュー
  結果待ち
- D18完了後の周知(sas0-74・faceless-cartographer-8b・claude-25への新構造連絡)完了
  (2026-09-08)
- 単一実例のまま長期間増えていない「一般則」タグの棚卸し完了(2026-09-08、hfuさん承認)。
  `interoperability.md`・`ci-cd-pitfalls.md`・`robust-pipeline-design.md`(2パターンとも)・
  `raspberry-pi-appliance.md`の「systemd Conflicts=」パターン、計5パターンを「個別事情」に
  再タグ付け
- hfuさんの依頼で、「hfuさん独特で文脈が無いと理解されにくい表現」の全ファイル棚卸しを
  実施(2026-09-08)。`DWG7-CONTEXT.md`(江戸期与力/寄騎制度・GGKIC比較・隠れキリシタン
  三役構造由来の命名等、計8箇所)と`patterns/agent-personification.md`(藩の役職の比喩)を
  「表現の修正」として静かに修正。他ファイルは概ねクリーンと確認(コミット
  `f6bd223`・`93c5ea2`)
- **D1'**: 優先候補3件すべてレビュー完了(2026-09-08、hfuさん承認)。
  `patterns/open-mct*.md`(分割後の4ファイル)・`STACCATO-CONTEXT.md`(「気に入っている」との
  評価)・`patterns/gatekeeping.md`、いずれもOK。
- **D1'次バッチ完了(2026-09-11、hfuさん「まとめて承認」)**:
  `patterns/markdown-file-conventions.md`・`patterns/verification-discipline.md`・
  `patterns/case-study-research.md`、いずれもOK。D1'対象は計6ファイルレビュー完了、
  残り約9ファイル(2026-09-09時点でHANDOVER.mdに明文化したリスト参照)
- **新規参加プロジェクト3件の紹介・登録完了(2026-09-09)**: hfuさんの指示で、ListAgentsに
  現れた未知のセッション(volca-4e・staccato-spec-42・staccato-ecosystem-85)へ順に(一括で
  なく個別に)自己紹介を依頼。`volca`(hfu/volca、Private、北海道9常時観測火山の防災計画
  横断分析)・`staccato-spec`(UNopenGIS/staccato-spec、規範仕様本体)・`staccato-ecosystem`
  (dwg7/staccato-ecosystem、staccato-specのコンパニオン、価値提案/成長戦略)を`PROJECTS.md`・
  `CLAUDE.md`既知のピアに登録。staccato-spec本人から、ferspas57の位置づけ(「staccato-specの
  Cartographerを構築中」ではなく独立したCartographer実装の1つ)の訂正も受けて反映
- **D19「PRIVATEリポジトリ情報をPublicなcafebabeに書く際の基準」完了(2026-09-09)**。
  volca登録の途中でhfuさんから提起。書いてよいもの(プロジェクト名・URL・技術構成レベルの
  一言)/書かないもの(分析結論・戦略の中身)/迷う場合(本人に確認)の3点。`CLAUDE.md`にも
  運用ガイドとして転記済み
- **tabularmaps/do(dwg7外)からの大量寄稿を反映(2026-09-17)**。北海道179市町村→16×16
  tabular mapプロジェクトから、hfuさんの指示で14件の知見が届いた。Open MCT関連5件は
  `patterns/open-mct-*.md`に反映(providerパターンの5例目確認、ブラウザ自動化での
  展開三角セレクタの罠、無害エラーの追加確認、データ契約の具体例、Espressoテーマ内での
  CSS透過テクニック)。北海道179市町村データの罠(総務省Excelの北方領土6村混入)+
  xlsx最小パース技法は`patterns/data-provenance.md`に、CI設計は`patterns/ci-cd-
  pitfalls.md`に、GitHub Pages有効化の`gh api`手順は`patterns/markdown-file-
  conventions.md`に追加。カルトグラム的配置最適化の方法論5件は新規
  `patterns/cartogram-layout-optimization.md`として独立ファイル化(do自身が新設候補として
  提案)。`tabularmaps/do`を`PROJECTS.md`(新設「tabularmaps org」セクション)に登録。
  返信不要の指示だったため、doへの返信は送っていない
- **DWG7-CONTEXT.mdに「潜水艦原則」を追記(2026-09-16)**。hfuさんとの対話より、
  「技術の開放性とデータの開放性を分離する」という設計哲学(オープン技術+必要時のみ
  air-gapped化するデータ)を新セクションとして追加。当初「DWG1」を名指しした対比案が
  あったが、他DWGへの一方的な特徴づけを避け「他のDWG」に一般化した(hfuさん判断)。
  rpi-geoserver0(HDXベンチマークデータ)・kikimimi(signal vs verified intelligence)・
  kaga0(オフライン設計)の3実例、既存のAntigravity・個人単位の多中心的協調とも
  相互参照させた
- **kikimimiからの実装確認2件(2026-09-16)**: (1) 合成ダッシュボードはDisplay Layoutでは
  なく「単一の非永続provider+単一view providerで直接DOM生成」がm3xx-fleet・sas0の実績
  パターンだとコード確認、`patterns/open-mct-telemetry.md`のPlanLayout注記に並記。
  (2) `openmct.on('start', () => router.setPath(...))`がCDN経由で例の無害コンソール
  エラーを引き起こし、今回は遷移が効かないという実害を伴うことを確認、
  `patterns/open-mct-operations.md`の該当箇所を訂正
- **kikimimi(新Open MCTプロジェクト)への設計助言+新規参加(2026-09-16)**。
  hfuさん本人から、既存4プロジェクト(sas0/claude-mct/m3xx-fleet/mapterhorn-monitor)の
  知見を踏まえた設計相談(m3xx-fleet型の妥当性・Plot APIの壁の再発可能性・root固定
  identifierの踏襲・ツリー/モバイル対応)を受け、`patterns/open-mct-*.md`に基づき回答。
  直後にkikimimi本人からも同内容の確認が届き、回答の一致を確認。OpenSpeechMap/
  whisper.cpp/RPi 4Bの実測知見はdwg7に蓄積が無いと正直に回答。`dwg7/kikimimi`(Public)を
  `PROJECTS.md`/`CLAUDE.md`に登録
- **cafebabe自身の誤帰属を訂正(2026-09-15)**。上記の「grep戻り値」実例を
  `mapterhorn-japan-bridge`と記載していたが、tokachi20260911からの伝聞(セッション名
  「【現役3号】」、対応リポジトリ不明)を`ListAgents`の類似セッション名から勝手に
  結びつけた誤り。本人からの訂正を受けて修正し、`patterns/agent-repository-
  boundaries.md`に自戒として3回目の再発例を記録した。次回の`verification-
  discipline.md`分割時は、tokachi20260911からの提案(「検査の検定」と「測定器の検定」
  ——既知の答えを測らせて検証器自体を確かめる、D31/D44の実例——は対象が違うだけで
  同じ構造なので同居できる)を構成の参考にする
- **tokachi20260911の第2弾続報+全プロジェクト横断の検証知見(2026-09-15)**。ODM固有では
  「同一入力・同一設定でも結果が変わる」非決定性(点群17%幅、水平精度2.09〜9.53m、
  SIGSEGV有無まで非決定)を確認し、精度は「成果物の値」であって「手法の値」ではないと
  明記する必要性を`patterns/aerial-photogrammetry-pipeline.md`に追加。焦点距離混在の
  害を美瑛拠点の実例で再確認。**より重要なのは横断的な検証知見**:
  同じ日にtokachi20260911とmapterhorn-japan-bridgeが独立に同型の事故(検査の戻り値を
  正しく評価せず、壊れているのに「成功」と誤記録)を踏んだことから、「検査を書いたら
  わざと失敗させて赤く光ることを確かめるまで信用しない」という新パターンを
  `patterns/verification-discipline.md`に追加(強い独立収束のため「推奨」タグ)。
  加えて共有マシンでの計測汚染事故(自分の後処理と他セッションの負荷試験が同時に載り
  実験6本が全滅)から「計測中は明示的な独占宣言が要る」パターンを
  `patterns/robust-pipeline-design.md`に追加。verification-discipline.mdが315行まで
  増え閾値超過(下記Known open items参照)
- **starsからの訂正(2026-09-14)**: PMTiles配信の2知見(Martinの`name`=ID衝突、
  Cloudflareの4時間キャッシュ)は、実はtokachi20260911の発見ではなくstars側が先に
  `docs/KNOWN_FACTS.md`で記録済みの既知事実で、事前にtokachi20260911へ共有していたと判明。
  `patterns/aerial-photogrammetry-pipeline.md`のKnown usesを訂正し、starsからの追加知見
  (GitHub Pages CDNが`fetch({cache:"no-store"})`を素通りしデプロイ直後に古い404を返す件)
  も追記した
- **tokachi20260911のODM続報+`patterns/aerial-photogrammetry.md`をテーマ別3分割
  (2026-09-14)**。進捗確認(cafebabeから能動的に一声かけた)に対し、実測に基づく12件の
  新知見が届いた:焦点距離混在でODMがサイレントに未校正カメラ群を使う問題(最大の発見、
  既存パターンを訂正・大幅強化)、交差パスのバンドル調整、間引きによるトラック長劣化、
  ヘイズ/基線の上限、Apple SiliconでのDocker版ODM実行、OOMの真因が点群の空間的広がりで
  あること、PMTiles配信の3つの落とし穴、stars(Martin+Cloudflare)の4時間メタデータ
  キャッシュ(個別事情)、位相相関棄却率による共登録可能性の事前見積もり。当初の噴煙
  シグネチャ仮説は支持されず、土地被覆(地面の時間的安定性)が効いていたという「仮説が
  覆った」経緯も含めて記録。ファイルが343行まで増えたため、概要+3テーマファイル
  (capture/screening/pipeline)に分割した。README.mdのリンクも更新
- **rpi-geoserver0の新規参加+D19拡張(2026-09-13)**。RPi3+Ubuntu Server+GeoServerの
  ハードウェア限界計測プロジェクト。5点の横断照会に回答(3問は該当知見なし、2問は
  測定記録の構造化パターンで回答)。D19に「第三者の識別情報にも同じ基準を適用する」という
  追記を行った。要約は本人(hfuさん)の指示で「GeoServer on Raspberry Pi」を主キーとする
  技術構成のみの形に調整
- **tokachi20260911の新規参加+ODM初知見(2026-09-11〜12)**。十勝岳ヘリ空撮データを
  OpenDroneMapで処理する、dwg7初のODM実例。`PROJECTS.md`/`CLAUDE.md`に登録(Private、
  hfuさん承認済みの一言要約使用)。dwg7標準リポジトリスタイル・PMTiles配信・ODM運用の
  横断照会に回答(ODM自体の蓄積は無いと正直に回答)。折り返し、実データ調査で確定した
  5件のSfM/ODM知見(GPS 1Hz量子化、ファイルサイズ↔鮮鋭度相関の弱さ、ラプラシアン分散の
  ボケ/ヘイズ混同、JPEG DRI部分デコードの汚染、ズームレンズのカメラグループ分割)を
  受け取り、新規`patterns/aerial-photogrammetry.md`として記録した
- **観測の食い違いの決着技法、知見反映(2026-09-11)**。同じspiccato描画問題の続報として、
  staccato-ecosystemが2回連続で誤った原因断定をvolca/kataribeに訂正された末、単一変数の
  A/B再現手順に変換して渡したところ一発で真因(resizeイベント依存)とvolca側の観測環境の
  交絡(ブラウザペイン非表示時のcanvas既定サイズ)の両方を特定できた実例を、
  `patterns/verification-discipline.md`に新規パターンとして追加(「反証もまた検証責任を
  負う」「条件を書き合うのではなく単一変数の手順に変換する」)
- **伝聞の劣化+自分の持ち物への検証漏れ、知見反映(2026-09-11)**。staccato-ecosystemが
  spiccatoの動作確認(2026-08-21)をkataribeのHANDOVER.md経由で伝聞2段のままvolcaへ断定
  転送し、実際には壊れていた実例(volcaが発見)と、volca側でも独立に4例観察された「相手
  への推論は疑うが自分の持ち物への推論は疑わない」非対称性を、`patterns/
  verification-discipline.md`の既存パターン(「ピアセッションからの主張は実行根拠に
  しない」)への訂正・深掘りとして追加。双方向の相互検証が機能した実例としても記録
- **kataribeのpush漏れ事故+知見反映(2026-09-11)**。staccato-ecosystemから、リポジトリ
  創設→専任セッション引き渡し時に3日分の作業が一度もpushされていなかった実例(定期的な
  エコシステム横断レビューで発覚、hfu承認を得て無改変でpush済み)が届いた。「push まで
  完了していない創設は、整ったHANDOVER.mdがあっても外部から不可視」というパターンを
  `patterns/verification-discipline.md`に追加。`dwg7/kataribe`も`PROJECTS.md`に登録
- **claude-25の担当替え発覚+知見反映(2026-09-10)**。`claude-25`をclaude-mct担当と
  記録していたが、実際は`say-your-grid→nuye→adopt-hokkaido-lidar`と順に担当替えしており、
  claude-mctを今も担当している現行セッションは不明と判明(claude-25本人が「永続メモリの
  記録は同一セッションの証拠にならない」と正直に留保)。`patterns/agent-repository-
  boundaries.md`に新規パターンとして記録し、`CLAUDE.md`既知のピアも訂正。あわせて
  `optgeo/adopt-hokkaido-lidar`を`PROJECTS.md`(新設「optgeo org」セクション)に登録し、
  Source Cooperative CLIのセッション延長知見(`--duration`明示指定でSTSクランプを回避
  できた実例)を`patterns/robust-pipeline-design.md`に追加
- **zukakuのPrint-in-Browser切り出し完了(2026-09-09)**。`dwg7/maplibre-gl-atlas`
  (`AtlasControl`/`AtlasSheet`、CC0 1.0)として公開・実機検証済み(`PROJECTS.md`登録済み)。
  副産物として2件の実バグを発見(`setProjection()`のスタイルロード前同期呼び出し、
  `renderScale`のスケールバー幅未補正)——後者は**zukaku本体にも現存するバグ**と判明し
  [dwg7/zukaku#9](https://github.com/dwg7/zukaku/issues/9)を起票。「機能を切り出す作業
  自体が元実装の潜在バグの発見機会になる」実例として記録価値あり(未反映、下記Known open
  items参照)。ライセンス選定の経緯(法人格を持たないdwg7ではCC0がMITより素直)を
  `patterns/licensing.md`(新規)に記録した。zukaku本体側の移行(PR2/PR3)はまだ未着手

## Pending long-running tasks(急がず進める)

1. **D1'**: cafebabeが自律的に書き起こしたがhfuさん未レビューの.mdファイルの棚卸し。
   計6ファイルレビュー完了(2026-09-08優先候補3件+2026-09-11次バッチ3件、いずれも
   hfuさん承認)。残り候補(優先度低、未提示): `patterns/agent-execution-gotchas.md`・
   `patterns/agent-personification.md`・`patterns/agent-repository-boundaries.md`・
   `patterns/data-provenance.md`・`patterns/interoperability.md`・
   `patterns/large-data-pitfalls.md`・`patterns/local-dev-pitfalls.md`・
   `patterns/maplibre-gl-js-*.md`(4ファイル)・`patterns/progress-reporting.md`・
   `patterns/raspberry-pi-appliance.md`・`patterns/robust-pipeline-design.md`・
   `patterns/style-composition.md`・`patterns/unattended-progress-visibility.md`・
   `patterns/vector-tile-sizing.md`・`patterns/licensing.md`(新規)・
   `ideas/osm-community-oauth.md`
2. hfuさんからGitHub issue経由のレビューが来たら、それに対応する(2026-09-09時点、
   dwg7/cafebabeに未対応issue無し確認済み)
3. zukaku#9(renderScaleバグ)がzukaku本体側でどう対応されるか、余裕があればフォロー

## Known open items

- `patterns/verification-discipline.md`が315行まで増え300行の目安を超えた(2026-09-15)。
  次の棚卸しでテーマ分割(自己申告の検証/cross-session主張/観測の食い違い決着/検査自体の
  検証、あたりで分けられそう)を検討する
- `patterns/`が26テーマまで増えた。ファイルサイズの閾値は「行数」だけでなく「バイト数」も
  見ること(open-mct.mdの教訓、D17・D18)
- 「個別事情」タグと「プロジェクト固有すぎて`patterns/`に置かない」の境界線は運用しながら
  見極めている段階(D3参照。実例3件以上蓄積してから明文化、D10 C3)
- 実例1件のまま長期間増えていない「一般則」タグは2026-09-08に棚卸し済み(下記Resolved
  参照)。今後も同じ基準(実例1件のまま長期間増えていない一般則→個別事情見直し)を
  定期的に適用すること
- D1'は計6ファイルのレビューが完了し、残り約9ファイルが対象。1サイクルに数件ずつ
  提示する運用を継続
- 「知見をcafebabeが与え、実装先が検証し、結果をまた知見に還元する」という助言サイクル
  (starsの実例)は、独立収束による知見とは証拠の重みが異なる点を毎回明記すること
  (`patterns/open-mct-object-model.md`のstars注記が実例)
- 「機能を切り出す作業自体が元実装の潜在バグの発見機会になる」(zukaku→maplibre-gl-atlas、
  2026-09-09、zukaku#9)は実例1件のみでまだパターン化していない。他プロジェクトでも
  似た切り出し作業(例: stars-cdの相談等)があれば2件目を待ってから`patterns/`へ追加を
  検討する

## Where to look

- D1〜D19の経緯 → [DECISIONS.md](DECISIONS.md)(番号順)
- dwg7組織文脈・エージェンシー経済学 → [DWG7-CONTEXT.md](DWG7-CONTEXT.md)
- staccato-spec 4パーティモデルと一般化拡張議論 → [STACCATO-CONTEXT.md](STACCATO-CONTEXT.md)
- 各プロジェクトのリポジトリ → [PROJECTS.md](PROJECTS.md)
- 実装済みの知見 → [README.md](README.md)の`patterns/`一覧参照
- 実装未検証のアイデア → [`ideas/README.md`](ideas/README.md)
- 運用ガイド(鮮度と分量を保つ責務、判断待ち事項の捌き方、横断ヒアリングの作法、dwg7組織
  文脈の注意点含む) → [CLAUDE.md](CLAUDE.md)
- 貢献の仕方(patterns/ vs ideas/の判断基準含む) → [CONTRIBUTING.md](CONTRIBUTING.md)

## Resume prompt

次にこのリポジトリを触るときにやること:
1. このHANDOVER.mdと直近のDECISIONS.mdエントリ(D17・D18・D19)を読んで経緯を把握する
2. `dwg7/cafebabe`や`unopengis/7`にhfuさんからのissueが立っていないか確認する
3. D1'の次のバッチ(残り約12ファイルから数件)を、機会を見て提示する
4. cross-session messageで届いている新しい知見・確認依頼があれば、まずそれに対応する
5. 判断事項が2〜3件溜まったら会話内でまとめて確認、5件超か複数テーマならPlanモード(D14)
