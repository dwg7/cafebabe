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
  評価)・`patterns/gatekeeping.md`、いずれもOK。D1'対象の残り約12ファイルは、今後数件ずつ
  提示する運用を継続
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

## Pending long-running tasks(急がず進める)

1. **D1'**: cafebabeが自律的に書き起こしたがhfuさん未レビューの.mdファイルの棚卸し。
   優先候補3件は全てレビュー完了(2026-09-08)。残り約12ファイルから、次のサイクルで
   数件ずつ提示する
2. hfuさんからGitHub issue経由のレビューが来たら、それに対応する
3. zukakuのPrint-in-Browser切り出し計画がhfuさんのレビューを経てどうなったか、
   フォローする

## Known open items

- `patterns/`が26テーマまで増えた。ファイルサイズの閾値は「行数」だけでなく「バイト数」も
  見ること(open-mct.mdの教訓、D17・D18)
- 「個別事情」タグと「プロジェクト固有すぎて`patterns/`に置かない」の境界線は運用しながら
  見極めている段階(D3参照。実例3件以上蓄積してから明文化、D10 C3)
- 実例1件のまま長期間増えていない「一般則」タグは2026-09-08に棚卸し済み(下記Resolved
  参照)。今後も同じ基準(実例1件のまま長期間増えていない一般則→個別事情見直し)を
  定期的に適用すること
- D1'は優先候補3件のレビューが完了し、残り約12ファイルが対象。1サイクルに数件ずつ
  提示する運用を継続
- 「知見をcafebabeが与え、実装先が検証し、結果をまた知見に還元する」という助言サイクル
  (starsの実例)は、独立収束による知見とは証拠の重みが異なる点を毎回明記すること
  (`patterns/open-mct-object-model.md`のstars注記が実例)

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
