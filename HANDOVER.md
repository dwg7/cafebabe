# HANDOVER

## Status as of 2026-09-06

パターン集は23テーマ(`patterns/`実ファイル数)。`ideas/`ディレクトリを新設(D16)——
実装に裏打ちされていない技術的アイデアを`patterns/`と分離して置く場所。`PROJECTS.md`
(dwg7組織10件+hfu個人7件のリポジトリ)、`DWG7-CONTEXT.md`(組織文脈、エージェンシー
経済学セクション含む)、`STACCATO-CONTEXT.md`(staccato-spec 4パーティモデルと一般化拡張
議論、ferspas57のnarrative libraryを追記済み)を保有。

D1〜D17まで17件のADRが完了。直近の4件: D14(判断待ち事項の捌き方を「2〜3件の小分け+
定期」に更新、5件超/複数テーマならPlanモード)、D15(全プロジェクト共通の
`~/.claude/CLAUDE.md`策定にcafebabeが協力、ピアセッションの主張を鵜呑みにしない原則を
verification-discipline.mdへ一般化)、D16(`ideas/`新設)、D17(Fableによる知見ベース全体
レビューと「局面 vs 大局」の区別)。

**運用(D14で更新済み)**: 判断待ち事項は2〜3件溜まったら通常の会話内でまとめて確認するのが
基本形。1件だけ即時性が高ければその場で確認してよい。5件を超える、または複数テーマに
またがる棚卸しはPlanモードでのレビュー(D10方式)に切り替える。hfuさんはGitHub issue経由でも
直接レビューする運用のため、定期的にissueをチェックする習慣を持つこと。

**運用(D17で追加)**: cafebabe自身の解釈・分析は知識創造として恒常的に歓迎される——
hfuさんの確認が無いことそれ自体を問題視しない。他者からの指摘(外部モデルによるレビュー等)
を評価する際は、「局面での方針」と「大局的な方針」を区別してから食い違いの有無を判断する
こと(詳しくは`CLAUDE.md`の該当節、経緯はD17参照)。

**2026-09-06、外部モデル(Fable)による知見ベース全体レビューを実施した(D17)。** 見つかった
問題のうち機械的に直せるものは下記「Resolved」の通り修正済み。「判断吸い上げの欠落」として
挙げられた項目(STACCATO-CONTEXT.mdのnarrative判断等)は、上記のhfuさんのフィードバックに
より、実際には問題ではなかったと判明した。

## Resolved since last handover

- D1〜D13(創設〜maplibre-gl-js.md分割+terrain/hillshadeヒアリング)完了
- D14「判断待ち事項の捌き方を更新」完了。zukakuでの`.claude/rules/`symlink試行を提案中
  (zukakuセッション不在のため未達、再送待ち)
- D15「グローバル`~/.claude/CLAUDE.md`策定への協力」完了。9セッションからの提起
  (kitavolca/sas0/stars-fd)を1原則に統合し採用された。同じ一般化を
  `patterns/verification-discipline.md`にも追記
- D16「`ideas/`ディレクトリ新設」完了。`ideas/osm-community-oauth.md`を初回エントリとして
  作成
- **D17「Fableによる知見ベース全体レビューとその対応」**完了(2026-09-06):
  - `PROJECTS.md`のkitavolcaリンクを`dwg7/kitavolca`(古いフォーク、2026-07-19で更新停止)
    から`hfu/kitavolca`(本体、直近push 2026-08-30)に訂正。`m3xx-fleet-ops`・`m3xx-fleet`・
    `kitaphoto17-navara`の3件を追加登録
  - `patterns/style-composition.md`(317行、閾値超過)から「中心固定型の放射状コントロール」
    パターンを`patterns/maplibre-gl-js-embedding.md`へ移動(UI/インタラクション寄りの
    内容のため、既存の「ホバー情報は固定ドッキングパネル」パターンと隣接させる形に整理)。
    両ファイルとも300行以下に収まった
  - `patterns/open-mct.md`は139行だが24KBで実は全パターン中バイト数最大(行数だけを見た
    D13の判断は指標として不適切だった)——ただし3プロジェクト共同のマスタードキュメントで
    あり、分割は関係者への周知が要るため、機械的修正の対象外としPlanモード送りとした
  - `CONTRIBUTING.md`(投稿時)と`CLAUDE.md`(棚卸し時)の「一般則/個別事情」タグの既定値の
    違いは、矛盾ではなく局面の違いであることを明記して両ファイルに解説を追記
  - `DWG7-CONTEXT.md`の出自宣言(「一次情報として原文のまま保存」)と、D12「エージェンシーの
    経済学」節(hfuさんとの対話をcafebabeが再構成したもの)との食い違いを、補足として追記し
    明確化。あわせて「独立収束の記録」原則とD15(収束を根拠に規約へ昇格させた実例)の関係も
    補足として整理
  - 複数パターンファイルの冒頭にあった鮮度切れの「Xプロジェクトから」という記述を追記で更新
  - D6の「9プロジェクト全員への結果共有」がResume promptに残ったまま未達だったことが判明。
    4日以上経過し状況も変化しているため、今更り追わずクローズ(教訓として記録)

## Pending long-running tasks(急がず進める)

1. `patterns/open-mct.md`(24KB、sas0/mapterhorn-monitor/claude-mct共同管理)の分割方針を
   Planモードで検討する。3プロジェクトへの周知も必要
2. **D1'**: cafebabeが自律的に書き起こしたがhfuさん未レビューの.mdファイルの棚卸し。
   優先候補3件(`STACCATO-CONTEXT.md`・`patterns/gatekeeping.md`・`patterns/open-mct.md`)を
   提示済み、フィードバック待ち
3. zukakuへの`.claude/rules/`symlink試行の依頼(D14)——セッション不在で未達、再送する
4. hfuさんからGitHub issue経由のレビューが来たら、それに対応する

## Known open items

- `patterns/`が23テーマまで増えた。ファイルサイズの閾値は「行数」だけでなく「バイト数」も
  見ること(open-mct.mdの教訓)
- 「個別事情」タグと「プロジェクト固有すぎて`patterns/`に置かない」の境界線は運用しながら
  見極めている段階(D3参照。実例3件以上蓄積してから明文化、D10 C3)
- 実例1件のまま長期間増えていない「一般則」タグが複数残っている
  (`interoperability.md`・`ci-cd-pitfalls.md`・`robust-pipeline-design.md`等)。次の棚卸しで
  「個別事情」への見直しを検討する
- D1'(未レビューファイルの棚卸し)は約15ファイルが対象。1サイクルに数件ずつ提示する運用
- claude-mctから「フリート全体の定期スタンドアップ」の1回限りテストがあり、常態化するかは
  claude-mct側の判断待ち

## Where to look

- D1〜D17の経緯 → [DECISIONS.md](DECISIONS.md)(番号順)
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
1. このHANDOVER.mdと直近のDECISIONS.mdエントリ(D16・D17)を読んで経緯を把握する
2. `dwg7/cafebabe`や`unopengis/7`にhfuさんからのissueが立っていないか確認する
3. `patterns/open-mct.md`の分割方針をPlanモードで検討する(上記Pending 1番)
4. zukakuセッションが復帰していたら、`.claude/rules/`symlink試行の依頼を送る
5. D1'への、hfuさんからのフィードバックが届いていれば対応する
6. cross-session messageで届いている新しい知見・確認依頼があれば、まずそれに対応する
7. 判断事項が2〜3件溜まったら会話内でまとめて確認、5件超か複数テーマならPlanモード(D14)
