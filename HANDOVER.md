# HANDOVER

## Status as of 2026-09-24

パターン集は`patterns/`実ファイル数で36テーマ(直近で急増——tabularmaps/do・do-survey等、
dwg7外を含む複数プロジェクトからの大量寄稿による)。`ideas/`ディレクトリ(D16)も稼働中。
`PROJECTS.md`は42件のリポジトリを収録(dwg7 org・UNopenGIS org・optgeo org・
tabularmaps org・hfu個人名前空間)。`DWG7-CONTEXT.md`(組織文脈、エージェンシー経済学+
「潜水艦原則」セクション)、`STACCATO-CONTEXT.md`(staccato-spec 4パーティモデル)を保有。

D1〜D19まで19件のADRが完了(直近はD19「PRIVATEリポジトリ情報の記載基準」、
2026-09-13にrpi-geoserver0の実例で「第三者の識別情報」への適用拡張を追記)。この期間の
実質的な活動量はADRの数ではなく、cross-session経由の知見取り込みに集中している——
以下「この期間にあったこと」参照。

**運用(D14)**: 判断待ち事項は2〜3件溜まったら会話内でまとめて確認。1件だけ即時性が
高ければその場で確認。5件超・複数テーマならPlanモード(D10方式)。

**運用(D17)**: cafebabe自身の解釈・分析は知識創造として歓迎される。他者の指摘は
「局面 vs 大局」を区別してから評価する。

**運用(D19)**: PRIVATEリポジトリの情報は技術構成レベルの一言要約まで。分析結論・戦略は
書かない。第三者(協力者等)の識別情報にも同じ基準を適用する。迷ったら本人に確認する。

## この期間にあったこと(2026-09-09〜24、要約)

cafebabeが「知見を待つ」だけでなく「能動的に確認する」役割を強く担うようになった期間。
具体的な内訳:

- **新規プロジェクトの継続的な受け入れ**: volca・staccato-spec・staccato-ecosystem・
  kataribe・hokkaido-points・tokachi20260911・rpi-geoserver0・kikimimi・
  tabularmaps/do・tabularmaps/cldr・bvmap・doverture・ferspas-html-demo・do-survey・
  adopt-hokkaido-lidar(既存セッションの担当替えで再認識)など多数が新規参加。うち
  `tabularmaps/do`系列(do・cldr・do-survey)は**dwg7外**のプロジェクトだが、横断的に
  価値の高い知見(カルトグラム配置最適化・GeoParquet・Open MCT実装知見)を多数寄稿し、
  そのまま収録している(cafebabeの「互助の場」という位置づけがdwg7の外にも自然に開いた
  実例)
- **PR経由の直接寄稿を初めてマージ**(`dwg7/bvmap`・`dwg7/doverture`、2026-09-20)。
  従来のcross-session message経由の取り込みに加え、CONTRIBUTING.md準拠のPRを直接
  レビュー・マージする運用が実際に機能した
- **dwg7初の実例が2つ生まれた**: OpenDroneMap/SfM写真測量(`tokachi20260911`、
  `patterns/aerial-photogrammetry*.md`4ファイル)、GeoParquet(`do-survey`、
  `patterns/data-provenance-wrangling.md`)
- **cafebabe自身の誤りを2回、公開で訂正した**: (1) 伝聞+類似セッション名からの憶測で
  「grep戻り値」バグを誤って`mapterhorn-japan-bridge`に帰属(2026-09-15、
  `patterns/agent-repository-boundaries.md`に3回目の再発例として自戒記録)。(2)
  starsの先行発見をtokachi20260911の発見と誤記載(2026-09-14、`patterns/
  aerial-photogrammetry-pipeline.md`で訂正)
- **知見ベース自体の分割が進んだ**(いずれも300行の目安超過による): `verification-
  discipline.md`→self-checks/cross-session、`data-provenance.md`→
  source-verification/wrangling、`aerial-photogrammetry.md`→
  capture/screening/pipeline(既存)。分割時は必ずREADME.mdのリンクと、他ファイルからの
  相互参照リンクの更新もセットで行うこと
- **DWG7-CONTEXT.mdに「潜水艦原則」(技術は開く、データは必要時のみ閉じる)を追記**
  (2026-09-16)。他DWGへの名指しは避け「他のDWG」に一般化した(hfuさん判断)
- **ferspas57がミッション転換**(2026-09-18、unopengis/7 #997→#1011)。「Staccatoを
  当てはめようとしすぎてUserの問いを取り逃していた」という振り返りから、FAO担当者の
  実際のユーザーストーリーに立ち返る方針へ。後継`dwg7/ferspas-html-demo`
- **D1'棚卸し**: 計6ファイルレビュー完了・hfuさん承認済み(open-mct系4・
  STACCATO-CONTEXT.md・gatekeeping.md・markdown-file-conventions.md・
  verification-discipline.md・case-study-research.md)。残り候補は下記参照
- 個別の技術知見(ODM非決定性、検証規律の新パターン多数、カルトグラム最適化、Open MCT
  実装ノウハウ等)は`patterns/`本体を参照。ここでは列挙しない——DECISIONS.mdや過去の
  コミットログの方が正確

## Pending long-running tasks(急がず進める)

1. **D1'**: cafebabeが自律的に書き起こしたがhfuさん未レビューの.mdファイルの棚卸み。
   計6ファイル完了。残り候補(優先度低、未提示。一部はこの期間に大幅拡張されている):
   `patterns/agent-execution-gotchas.md`・`patterns/agent-personification.md`・
   `patterns/agent-repository-boundaries.md`・`patterns/data-provenance*.md`(分割後2+概要)・
   `patterns/interoperability.md`・`patterns/large-data-pitfalls.md`・
   `patterns/local-dev-pitfalls.md`・`patterns/maplibre-gl-js-*.md`(4ファイル)・
   `patterns/progress-reporting.md`・`patterns/raspberry-pi-appliance.md`・
   `patterns/robust-pipeline-design.md`・`patterns/style-composition.md`・
   `patterns/unattended-progress-visibility.md`・`patterns/vector-tile-sizing.md`・
   `patterns/licensing.md`・`patterns/aerial-photogrammetry*.md`(4ファイル)・
   `patterns/cartogram-layout-optimization.md`・`ideas/osm-community-oauth.md`
2. `dwg7/cafebabe`・`unopengis/7`のissue/PRを定期的に確認する(この期間に確立した習慣。
   「起床」等の一言で明示的に促されたら必ず`gh issue list`/`gh pr list`両方を確認する
   こと——issueだけでなくPRも見落としやすい。マージ済みPRのブランチにその後pushされた
   孤立コミットが残ることもあるので、`git fetch`後の差分にも注意)
3. zukaku#9(renderScaleバグ)がzukaku本体側でどう対応されるか、余裕があればフォロー
   (長期間動きなし、優先度低)

## Known open items

- `patterns/`が36ファイルまで増えた。ファイルサイズの閾値は「行数」だけでなく実質的な
  情報密度も見ること(open-mct.mdの教訓、D17・D18)。300行を超えたら分割を検討
- 「個別事情」タグと「プロジェクト固有すぎて`patterns/`に置かない」の境界線は運用しながら
  見極めている段階(D3参照。実例3件以上蓄積してから明文化、D10 C3)
- 実例1件のまま長期間増えていない「一般則」タグの棚卸しは2026-09-08に実施済み。今後も
  定期的に適用すること
- 「知見をcafebabeが与え、実装先が検証し、結果をまた知見に還元する」という助言サイクルは、
  独立収束による知見とは証拠の重みが異なる点を毎回明記すること
  (`patterns/open-mct-object-model.md`のstars注記が実例)
- 「機能を切り出す作業自体が元実装の潜在バグの発見機会になる」(zukaku→maplibre-gl-atlas、
  zukaku#9)は実例1件のみでまだパターン化していない。2件目が出たら`patterns/`へ追加を検討
- ローカルクローンでの直接確認(git log/grep)や実機ブラウザでの視覚確認など、cafebabeが
  「聞くだけでなく自分で検証する」場面が増えている。これは`patterns/verification-
  discipline-*.md`の精神をcafebabe自身が実践している例であり、今後も維持すること

## Where to look

- D1〜D19の経緯 → [DECISIONS.md](DECISIONS.md)(番号順)
- dwg7組織文脈・エージェンシー経済学・潜水艦原則 → [DWG7-CONTEXT.md](DWG7-CONTEXT.md)
- staccato-spec 4パーティモデルと一般化拡張議論 → [STACCATO-CONTEXT.md](STACCATO-CONTEXT.md)
- 各プロジェクトのリポジトリ(dwg7外含む) → [PROJECTS.md](PROJECTS.md)
- 実装済みの知見 → [README.md](README.md)の`patterns/`一覧参照
- 実装未検証のアイデア → [`ideas/README.md`](ideas/README.md)
- 運用ガイド → [CLAUDE.md](CLAUDE.md)
- 貢献の仕方 → [CONTRIBUTING.md](CONTRIBUTING.md)

## Resume prompt

次にこのリポジトリを触るときにやること:
1. このHANDOVER.mdと直近のDECISIONS.mdエントリ(D19)を読んで経緯を把握する
2. `dwg7/cafebabe`・`unopengis/7`にissue/PRが立っていないか`gh`で確認する(issueと
   PRの両方、マージ済みブランチへの追加pushも)
3. cross-session messageで届いている知見・確認依頼があれば、まずそれに対応する
4. D1'の次のバッチ(残り候補から数件)を、機会を見て提示する
5. 判断事項が2〜3件溜まったら会話内でまとめて確認、5件超か複数テーマならPlanモード(D14)
