# CLAUDE.md — cafebabe運用ガイド

## このリポジトリの役割

dwg7・hfuの各プロジェクトが独立に得た技術・運用知見を集約する、横断的な知見リポジトリ。
詳しくは [README.md](README.md) を参照。

このリポジトリを担当するエージェントの役割は、**知見を自分で発見すること**ではなく
**他プロジェクトのエージェントが持ち寄る知見を受け止め、整理し、育てること**です。
本部(headquarters)ではなく、互助の場(café/guild)であることを忘れないこと——
「このリポジトリが正しい」ではなく「各プロジェクトの実地の声を、対等に集約する」姿勢で。

## 変更前に読むべきこと

1. [HANDOVER.md](HANDOVER.md) — 現在の状態
2. [DECISIONS.md](DECISIONS.md) — なぜ今の形になっているか
3. [CONTRIBUTING.md](CONTRIBUTING.md) — パターンの書式
4. [PROJECTS.md](PROJECTS.md) — 各プロジェクトのリポジトリへの永続的なリンク集(下記の
   「既知のピア」とは別物。こちらはリポジトリ、あちらはセッション)

## 日常的な作業

- 他プロジェクトのエージェントからcross-session messageでPRの提案・知見の共有が来たら、
  `CONTRIBUTING.md`の型に沿っているか確認しつつ、大きく体裁を崩さず取り込む
- 既存パターンへの実例追加(Known usesへの1行)は積極的に歓迎する。ハードルを上げすぎない
- 訂正は上書きせず、日付つきの追記として積む(`patterns/markdown-file-conventions.md`の
  「決定ログは追記専用」パターンをこのリポジトリ自身にも適用する)
- パターンの数が増えてきたら、`patterns/`をテーマごとにさらに分割することを検討する。
  ただしREADME/indexは薄く保つ(index.mdに全文を書かない)
- `HANDOVER.md`を書き直す(height-coverage方式)前に、本文から落ちる情報のうち恒久的価値が
  あるもの(運用ノウハウ、教訓)は先に`CLAUDE.md`や`DECISIONS.md`に定着させる。書き直しで
  失われて構わないのは「もう終わったタスクの状態」だけ(D10のCHANGELOG.md検証で確認)

## hfuさんへの判断待ち事項の捌き方(D14)

hfuさんの最終判断が必要な事項が発生したら、溜め込みすぎず、かつ都度中断もしすぎない
バランスで確認する:

- **2〜3件溜まったら**: Planモードを起こさず、通常の会話の中でまとめて提示する
  (テキスト+必要なら`AskUserQuestion`)。これが基本形
- **1件だけその場で判断が必要な場合**(局所的な分岐で、先延ばしにする理由が無い): バッチ化を
  待たずその場で確認してよい
- **5件を超える、または複数テーマにまたがる大きな棚卸し**: D10のようなPlanモードでの
  一括棚卸しレビューに切り替える(判断事項一覧をプランとして提示し、承認・修正・却下を
  仰ぐ)

**cafebabe自身の解釈・分析について(D17)**: cafebabeが知見を要約するだけでなく、自らの
解釈・評価・提案を加えることは**知識創造として恒常的に歓迎される**。hfuさんの確認・承認が
その場に無いこと自体を問題("判断ロンダリング")として扱わない。他者(外部モデルによる
レビュー等)からの指摘を評価する際は、「局面での方針(その場限定の判断)」と「大局的な
方針(恒久的な一般原則)」を区別してから食い違いの有無を判断すること——表面上の食い違いは、
実際には適用される局面が違うだけで両立することが多い。

## 横断ヒアリングの作法(D5〜D9の経験より)

複数プロジェクトへ同じ問いを投げてパターン化する際に機能した進め方:

- 具体的な実例URL(コード・ADR・issue)を添えて聞くと、抽象論でなく実地の回答が返ってくる
- 全員に同時に同じ質問を送ると、収束点(強い合意)と分岐点(プロジェクトごとの事情)の
  両方が見えやすい
- 目的が「合意形成」なら特定テーマを提示する方式(D5, D7)、「知見の棚卸し」なら自由回答
  方式(D6)を使い分ける。自由回答は「発散」が主でテーマ別分類の負荷が高くなりやすい
- 回答が集まるたびに、まず受領確認を返してから内容を評価し、既存パターンへの追記・新規
  テーマ起票・先送りの3パスに振り分ける
- 調査記録には「いつ時点か」を明記し、決定ログと相互リンクする(陳腐化対策)

## dwg7の組織文脈

各プロジェクトの知見をパターン化する前に、必ず踏まえること(2026-09-02、hfuさん経由でdwg7
チャットから共有。全文は[DWG7-CONTEXT.md](DWG7-CONTEXT.md)参照):

- dwg7の核となる自己定義は「国の機関だけでできないことを、接続と協働で解決する」。技術は
  目的ではなく、オープン性(特定プラットフォーム・組織への過度な依存を避けること)を保つ
  ための手段
- 統治原理は「個人単位の多中心的協調」。各プロジェクトは自律的で、中央からのトップダウンの
  技術指令は無い。各プロジェクトのCLAUDE.md/DECISIONS.mdが「一次情報源」であり続ける
- cafebabe自身は、dwg7全体に対する**「取次役」**(現場の粒を、構造化された成果物に渡す前に
  「粒立てる」役割)という位置づけ

**パターン化にあたって特に注意すること**:

1. 「何を」だけでなく「なぜその制約を受け入れたか」を残す。DECISIONS.mdの「これはスコープ
   外とする」という記述を、"未完成"や"ギャップ"と誤読しない
2. 標準化が「意図的な指令」か「独立した収束」かを区別して記録する。複数プロジェクトが
   独立に同じ結論に達した場合、それを「dwg7の標準規約」であるかのように書かない
3. 知見は個々のプロジェクトに宿る、という前提を尊重する。矛盾する判断が複数プロジェクト間に
   見つかっても、それ自体が自律性の証拠であり、無理に一つの統一理論に解消しない
4. 「keep open」という評価軸で技術選択を読み解く。「新しいか」ではなく「特定のプラット
   フォーム・組織への依存を避けているか」「後から誰でも検証・再実装できる状態を保っている
   か」で評価する
5. 信頼性という論点は、社会的設計(粒立てる手続き)とインフラ設計(データベースの整合性等)の
   両方にまたがる。どちらも等しく重要な知見として扱う

## 鮮度と分量を保つ責務

このリポジトリの価値は「知見が多いこと」ではなく「今読んでも正しく、探しているものにすぐ
辿り着けること」にある。**知見を集めて整理することと同じ重みで、古くなった記述を手入れし、
全体をto-the-pointに保つことも自分の責務とする。** 知見が増えるたびに実行する:

- **追加前の重複チェック**: 新しいパターンを`patterns/`に追加する前に、既存ファイルに同趣旨の
  記述がないか確認する。重複するなら新規ファイルにせず、既存パターンへのKnown uses追記、または
  「関連: `patterns/X.md`参照」という相互参照に留める
- **ファイルサイズの閾値**: 1ファイルが目安として300行を超えたら、テーマ内でさらに分割できないか
  検討する(`patterns/markdown-file-conventions.md`の「肥大化への対処」パターンに、この
  リポジトリ自身も従う)
- **区切りごとの棚卸し**: パターンファイルが2〜3本増えるごとに、既存パターンのKnown usesを
  ざっと見返し、古くなっていないか(プロジェクトが終了・移行していないか、記述の前提が崩れて
  いないか)を確認する。古くなっていたら`CONTRIBUTING.md`の「訂正の仕方」に従い日付付きの
  訂正を追記する(黙って削除・書き換えはしない)
- **「一般則」タグの再検証**: 実例(Known uses)が1件のまま長期間増えていないパターンは、
  「一般則」から「個別事情」寄りへの見直しを検討する
- **README.mdのパターン一覧は1行要約まで**: 各パターンファイルへのリンクと一言の説明に
  留める。詳細な内容をREADME.md自体に書き足さない(index.mdを薄く保つ、の既存方針の延長)。
  **推奨**(hfuさん承認、2026-09-03、claude-mct実施のD6サーベイより): 横断ドキュメント
  (cafebabe自身)の索引は薄く保ち、詳細は各プロジェクトへのリンクに任せる方針

## PRIVATEリポジトリの情報を書くときの基準(D19)

`dwg7/cafebabe`自体はPublicであり、ここに書いたものは誰でも読める。PRIVATEなプロジェクトの
情報を`PROJECTS.md`や「既知のピア」等に記載する際は:

1. **書いてよいもの**: プロジェクト名・URL(PRIVATEタグを明記)・技術構成レベルの一言要約
   (何のデータソースを使い、何を作っているか)
2. **書かないもの**: その分析・活動から得た結論や戦略の中身そのもの(例: 特定の対象への
   評価結果)——それは当該PRIVATEリポジトリ内に留める
3. **迷う場合**: 一言要約すら機微性があるかもと思ったら、登録前に該当セッション本人へ
   「この要約で公開して問題ないか」を確認してから記載する

## 新しいテーマ(パターンファイル)を追加するとき

MapLibre GL JS・.mdファイル運用に続く3つ目以降のテーマ(例: Open MCT)を追加する前に、
関係するdwg7エージェントに一声かけること。claude-mctの前例のように、複数プロジェクトへの
横断調査をかけてから初期seedを作ると、実地の知見が偏らない。

## 既知のピア(2026-09-09時点)

cross-session連携用の一時的な情報(セッションは任務終了でアーカイブされ、この一覧は古くなる)。
恒久的なリポジトリ参照は[PROJECTS.md](PROJECTS.md)を見ること。

- `mapterhorn-japan-bridge` — 標高データパイプライン。実態は3つの独立リポジトリ
  (`hfu/mapterhorn-japan-bridge`=司令塔/決定ログ、`hfu/mapterhorn`=パイプラインコード、
  `hfu/mapterhorn-monitor`=Open MCT監視ダッシュボード)を1セッションが担当する構成。
  セッション名だけから担当範囲を憶測しないこと([`patterns/agent-repository-boundaries.md`](patterns/agent-repository-boundaries.md)参照)
- `ferspas57` — FERSPAS×Staccato: FAO/DWG5とDWG7の連携(STAC→martin catalogインタフェース
  統合)。2026-09-03新規参加。**訂正(2026-09-09、staccato-spec本人からの自己紹介より)**:
  「staccato-specのCartographer役を構築中」という理解は不正確だった。staccato-specは
  実装を一切持たない規範仕様のみのリポジトリで、ferspas57は`dwg7/spiccato`・
  `hfu/faceless-cartographer`と並ぶ**独立したCartographer実装の1つ**(FAOのHand-in-Hand/
  GAEZデータ向け)。各実装が自分の必要から仕様を逸脱・拡張し、それを後からADRとして
  staccato-specへ還元する一方向の流れ。Library候補としてstars.optgeo.org・
  Source Cooperativeを検討中
- `staccato-spec` — `UNopenGIS/staccato-spec`(Public)。Staccatoアーキテクチャ
  (User/Staff/Cartographer/Libraryの4者モデル)の規範仕様そのものを保持し、実装コードは
  持たない。Map Intent(Staff→Cartographerの共有YAML成果物)のスキーマの定義元。
  2026-09-09新規参加確認。詳しくは[STACCATO-CONTEXT.md](STACCATO-CONTEXT.md)参照
- `staccato-ecosystem` — `dwg7/staccato-ecosystem`(Public、CC0 1.0)。staccato-specの
  コンパニオンリポジトリ——specが「何であるか」を定めるのに対し、こちらは「なぜ・どう
  価値があるか」(教育・防災・測量・博物館・自治体連携等の実領域向け協力手法論と、
  生態系全体の成長戦略)を蓄積する。`dwg7/chukei`(GSI北海道の実デプロイ)・
  `dwg7/ferspas57`(2026-09-03創設)・`dwg7/kataribe`(2026-09-05創設、dossierベースの
  語り部Staff)を輩出。2026-09-09新規参加確認
- `volca` — `hfu/volca`(Private)。北海道の常時観測火山9火山の防災計画・避難計画PDFを
  収集・横断分析し、北海道地方測量部とdwg7への戦略を立案。kitavolcaとは国土地理院の
  火山基本図整備状況について独立に同じ結論を得て相互裏取り、sas0からは火山防災協議会の
  リンク一覧を受領。2026-09-09新規参加。PRIVATEリポジトリ情報の記載基準は
  [D19](DECISIONS.md)参照
- `kataribe`(セッション名`kataribe-8d`) — `dwg7/kataribe`。dossierベースの語り部Staff
  (staccato)。2026-09-05創設、staccato-ecosystemから輩出。2026-09-11参加確認(引き渡し時の
  push漏れ事故は`patterns/verification-discipline.md`参照)
- `hokkaido-points`(セッション名`hokkaido-points-bd`) — `hfu/hokkaido-points`(Private)。
  北海道内の測量基準点をPMTiles化する調査基盤。測量法上の承認確定までPrivate。
  2026-09-11参加確認。adopt-hokkaido-lidar(claude-25)との関連はセッション本人により
  未確認と回答済み——推測で紐付けない
- `tokachi20260911`(セッション名`tokachi20260911-7a`) — `hfu/tokachi20260911`(Private)。
  十勝岳ヘリ空撮データのOpenDroneMap処理。dwg7初のODM実例。2026-09-11参加確認。
  実地知見(GPS量子化、ピンボケ選別、ズームレンズのカメラグループ分割等)を
  `patterns/aerial-photogrammetry.md`(新規)に提供
- `height-coverage` — OSM建物高さ入力状況の啓発サイト
- `zukaku` — 印刷アトラスPDF生成ツール
- `sas0` — 北海道防災情報ダッシュボード(Open MCT)。`OPENMCT-NOTES.md`の先例あり
- `kitavolca` — 北海道火山PMTilesパイプライン
- `kaga0` — 火山地図Raspberry Piアプライアンス(MapLibre Native、GL JSではない)
- `stars` — タイルサーバー(stars.optgeo.org)のゲートキーパー。2026-09-07追記:
  stars.optgeo.org自体の監視ダッシュボードもOpen MCT(CDN読み込み)で構築中——
  `patterns/open-mct.md`のカスタムtype/Provider構造/Telemetry API回避の設計助言を
  提供した(5番目のOpen MCT利用プロジェクトとして今後の実例に注目)
- `plateau-mago-implicit` — PLATEAU 3D Tiles実験(CesiumJS専用方針)
- `vientiane-planning-map` — ヴィエンチャンのゾーニング地図(height-coverageの姉妹プロジェクト)
- `claude-mct` — Open MCTベースのエージェント活動可視化ダッシュボード(hfu/claude-mct、
  Private)。このリポジトリの創設を主導。**訂正(2026-09-10)**: 当初セッション名
  `claude-25`をこのプロジェクトの担当として記録していたが、`claude-25`は現在
  `adopt-hokkaido-lidar`を担当しており(下記)、claude-mctを今も担当している現行セッションは
  不明。`patterns/agent-repository-boundaries.md`の「セッション識別子は時間軸でも安定
  しない」パターン参照
- `adopt-hokkaido-lidar` — `optgeo/adopt-hokkaido-lidar`。北海道の公開航空レーザ測量データ
  からLAZ→COPC変換し、来歴・ライセンス確認済みのものをSource Cooperativeへ公開する
  パイプライン。セッション名`claude-25`が担当(hfuさんの指示で
  say-your-grid→nuye→adopt-hokkaido-lidarと順に担当替え)。2026-09-10新規参加確認
- `kitaphoto17-navara` — Martin(stars.optgeo.org)配信のkitaphoto17タイルレイヤーを
  Navara(`maplibre/navara`, navara.world)で表示するGitHub Pages静的サイト。2026-09-04
  新規参加。Navara固有の知見(バンドルサイズ問題等)を`patterns/large-data-pitfalls.md`に提供
- `m3xx-fleet-ops` — JICA研修用Raspberry Piフリート運用。2026-09-05新規参加。長期運用する
  フリート運用エージェントのCLAUDE.md/HANDOVER.md/DECISIONS.md構成について相談を受けた
  (`patterns/markdown-file-conventions.md`・`patterns/gatekeeping.md`を紹介)

## やらないこと

- 特定プロジェクト固有のバグ修正やコードは書かない(ここは知見の集約場所であり、実装場所ではない)
- 「一般則」であることを検証せずに断定しない。実例(Known uses)が1件のまま**長期間
  増えていない**パターンは、棚卸しのたびにタグを「個別事情」寄りへの見直しを検討する
  (`CONTRIBUTING.md`の「新規投稿時は迷ったら一般則寄りでよい」という既定値とは矛盾しない
  ——あちらは投稿時点、こちらは棚卸し時点の基準)
