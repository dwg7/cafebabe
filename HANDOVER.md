# HANDOVER

## Status as of 2026-09-02

パターン集は18テーマ。`PROJECTS.md`(9プロジェクトの永続リンク集)、`DWG7-CONTEXT.md`
(組織文脈)、`STACCATO-CONTEXT.md`(staccato-spec 4パーティモデルと一般化拡張議論)を保有。
cafebabe自身の立ち上げも`unopengis/7#993`として対外報告済み。`OPENMCT-NOTES.md`の
sas0からの移管完了。

横断タスクが4つ完了: D5(先行事例研究パターン)、D6(全エージェントパターン提案募集、
約36件)、D7(スタイル設計・カートグラフィーの横断ヒアリング)、D8(staccato-spec
4ロールモデルの一般化拡張議論、9プロジェクト+stars参加)。

hfuさんが約10時間離席中(2026-09-02開始)。「自律的にpush・大きな構造変更もDECISIONS.mdに
ADRとして記録した上で裁量で進めてよい」方針で運用中。**新しい運用**: hfuさんは今後cafebabeの
成果をGitHub上で直接見て、issue経由でレビューする(2026-09-02指示)。つまり今後のフィードバック
はcross-session messageだけでなく、`dwg7/cafebabe`(または`unopengis/7`)のissueコメントとして
届く可能性がある——**定期的にissueをチェックする習慣を持つこと**。

## Resolved since last handover

- D1〜D4(創設、OPENMCT-NOTES.md移管、PROJECTS.md新設、dwg7組織文脈取り込み)完了
- D5「リポジトリ埋め込みの先行事例研究」完了。「専用ファイルに切り出す」の一般則を
  「専用ファイル化は規模に応じた判断」に修正
- D6「全エージェントからのパターン提案募集」完了。新規テーマ7本+既存9ファイルへの追記
- D7「スタイル設計・カートグラフィーの実地ノウハウ」完了。4プロジェクト(vientiane-planning-map,
  stars-fd, height-coverage, zukaku)から9パターンに集約。「視覚的ヒエラルキーの独立収束」
  「配色戦略の分岐(独自設計 vs 権威ある元データの忠実再現)」という2つの発見
- D8「staccato-spec 4パーティモデルの一般化拡張議論」完了。9プロジェクト全員+stars-fdから
  回答。「動的生成型 vs 静的キュレーション型」の軸、「Live vs Frozen Library」の提案、
  cafebabe自身への外部評価(Staff+Libraryのハイブリッド)等、`STACCATO-CONTEXT.md`に統合

## Pending long-running tasks(急がず進める)

1. ~~先行事例研究パターン(D5)~~ / ~~全エージェントパターン提案募集(D6)~~ /
   ~~スタイル設計横断ヒアリング(D7)~~ / ~~staccato-spec一般化拡張議論(D8)~~ — 全て完了
2. **次はこれに着手候補**: hfuさんが同時に提起した残る2テーマ
   - ベクトルタイルデザイン、特にサイズ最適化
   - スタイルデザイン、特にレイヤの上下関係・terrain・hillshadeの扱い
   
   進め方はD5-D8と同様(まず詳しそうな1プロジェクトを深掘り→案作成→他プロジェクトへ展開)。
   候補: サイズ最適化はkitavolca(PMTilesパイプライン)・mapterhorn-japan-bridge・height-coverage・
   stars-fdあたりが詳しそう。terrain/hillshadeは`patterns/maplibre-gl-js.md`に既にzukakuの
   terrain無効化パターンがあるので、そこからの発展も考えられる
3. hfuさんからGitHub issue経由のレビューが来たら、それに対応する(新しい運用、上記参照)

## Known open items

- `patterns/`が18テーマまで増え、README.mdの一覧が長大。サブディレクトリ化を検討する
  タイミングかもしれない(`patterns/open-mct.md`・`patterns/case-study-research.md`は
  既にサイズ閾値に近い/超えている)
- 「個別事情」タグと「プロジェクト固有すぎて`patterns/`に置かない」の境界線は運用しながら
  見極めている段階(D3参照)
- まだ他プロジェクトからのPRは来ていない。cafebabeセッションがcross-session messageで
  ヒアリングし自分で書き起こす運用が続いている
- D6の教訓: 自由回答形式は「発散」が主で分類作業の負荷が高い。特定テーマ提示(D5/D7方式)と
  自由回答(D6方式)を目的に応じて使い分けるとよい
- claude-mctから「フリート全体の定期スタンドアップ」の1回限りテストがあり、cafebabeとして
  週次頻度・4項目形式・opt-out重視を提案した(常態化するかは未定、claude-mct側の判断待ち)

## Where to look

- D1〜D8の経緯 → [DECISIONS.md](DECISIONS.md)(番号順)
- dwg7組織文脈 → [DWG7-CONTEXT.md](DWG7-CONTEXT.md)
- staccato-spec 4パーティモデルと一般化拡張議論 → [STACCATO-CONTEXT.md](STACCATO-CONTEXT.md)
- 各プロジェクトのリポジトリ → [PROJECTS.md](PROJECTS.md)
- 現在のパターン集 → [README.md](README.md)の一覧参照
- 運用ガイド(鮮度と分量を保つ責務、dwg7組織文脈の注意点含む) → [CLAUDE.md](CLAUDE.md)
- 貢献の仕方 → [CONTRIBUTING.md](CONTRIBUTING.md)

## Resume prompt

次にこのリポジトリを触るときにやること:
1. このHANDOVER.mdと直近のDECISIONS.mdエントリ(D7・D8)を読んで経緯を把握する
2. `dwg7/cafebabe`や`unopengis/7`にhfuさんからのissueが立っていないか確認する(新しい
   レビュー運用)
3. 上記「Pending long-running tasks」の2番(ベクトルタイルサイズ最適化、terrain/hillshade)
   に着手する。ListAgentsで現在アクティブなエージェント一覧を確認してから進める
4. `patterns/`のサブディレクトリ化を検討するかどうか判断する
5. cross-session messageで届いている新しい知見・確認依頼があれば、まずそれに対応する
