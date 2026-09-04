# HANDOVER

## Status as of 2026-09-04

パターン集は22テーマ(`maplibre-gl-js.md`をD13で4分割したため実ファイル数は増加)。
`PROJECTS.md`(dwg7組織9件+hfu個人5件のリポジトリ)、`DWG7-CONTEXT.md`(組織文脈、
エージェンシー経済学セクション追加済み)、`STACCATO-CONTEXT.md`(staccato-spec
4パーティモデルと一般化拡張議論)を保有。cafebabe自身の立ち上げも`unopengis/7#993`として
対外報告済み。

D5〜D13まで9件のADRが完了。直近では、hfuさんとのPlanモード棚卸し(D10)を起点に、
D6サーベイ反映(D10)、CHANGELOG.md不要の結論(D11)、呼称習慣パターン+エージェンシー
経済学の記録(D12)、`maplibre-gl-js.md`のテーマ別4分割+terrain/hillshade横断ヒアリング
完了(D13)、と連続して処理した。

**運用**: Planモードでの棚卸し→レビューの流れを定例化(D10 D1)。判断事項が3〜5件溜まるか、
大きな横断タスクが完了するたびに実施する。hfuさんはGitHub issue経由でも直接レビューする
運用のため、定期的にissueをチェックする習慣を持つこと。

## Resolved since last handover

- D1〜D9(創設〜ベクトルタイルサイズ最適化の横断ヒアリング)完了
- D10「Planモード棚卸しレビュー」完了。hfuさんとのレビューサイクルを定例化し、A1
  (D6サーベイの推奨ステータス付与)・C2(maplibre-gl-js.mdの独立収束チェック)を実施
- D11「HANDOVER.md肥大化対策」完了。CHANGELOG.mdは新設せず、`CLAUDE.md`に
  「横断ヒアリングの作法」を定着させる方向で結論
- D12「呼称習慣パターン+エージェンシー経済学の記録」完了。
  `patterns/agent-personification.md`新設、`DWG7-CONTEXT.md`にエージェンシー経済学
  セクション追加
- D13「`maplibre-gl-js.md`のテーマ別4分割+terrain/hillshade横断ヒアリング」完了。
  300行閾値超え(425行)を機に4ファイルへ分割、mapterhorn-japan-bridge・kitavolca・kaga0
  への横断ヒアリングで3方向の独立分岐(terrain封印/terrain併用/両方未実装)を記録

## Pending long-running tasks(急がず進める)

1. **D1'(D10で追加された運用)**: cafebabeが自律的に書き起こしたがhfuさん未レビューの
   .mdファイルの棚卸し。2026-09-04に初回リストを提示し、優先候補3件
   (`STACCATO-CONTEXT.md`・`patterns/gatekeeping.md`・`patterns/open-mct.md`)から
   見てもらうようお願い済み。フィードバックが来たら反映する
2. hfuさんからGitHub issue経由のレビューが来たら、それに対応する

## Known open items

- `patterns/`が22テーマ(実ファイル)まで増えた。D13でmaplibre-gl-js系を4分割したため、
  次に300行に近づくファイルが出たら同じ要領で対応する。現時点で閾値に近いものは無い
- 「個別事情」タグと「プロジェクト固有すぎて`patterns/`に置かない」の境界線は運用しながら
  見極めている段階(D3参照。D10 C3で「実例3件以上蓄積してから明文化」と確認済み)
- まだ他プロジェクトからのPRは来ていない。cafebabeセッションがcross-session messageで
  ヒアリングし自分で書き起こす運用が続いている
- D1'(未レビューファイルの棚卸し)は約15ファイルが対象。1サイクルに数件ずつ提示する運用
  なので、今後の棚卸しでも継続的に候補を出すこと
- claude-mctから「フリート全体の定期スタンドアップ」の1回限りテストがあり、cafebabeとして
  週次頻度・4項目形式・opt-out重視を提案した(常態化するかは未定、claude-mct側の判断待ち)

## Where to look

- D1〜D13の経緯 → [DECISIONS.md](DECISIONS.md)(番号順)
- dwg7組織文脈・エージェンシー経済学 → [DWG7-CONTEXT.md](DWG7-CONTEXT.md)
- staccato-spec 4パーティモデルと一般化拡張議論 → [STACCATO-CONTEXT.md](STACCATO-CONTEXT.md)
- 各プロジェクトのリポジトリ → [PROJECTS.md](PROJECTS.md)
- 現在のパターン集 → [README.md](README.md)の一覧参照
- 運用ガイド(鮮度と分量を保つ責務、横断ヒアリングの作法、dwg7組織文脈の注意点含む) →
  [CLAUDE.md](CLAUDE.md)
- 貢献の仕方 → [CONTRIBUTING.md](CONTRIBUTING.md)

## Resume prompt

次にこのリポジトリを触るときにやること:
1. このHANDOVER.mdと直近のDECISIONS.mdエントリ(D12・D13)を読んで経緯を把握する
2. `dwg7/cafebabe`や`unopengis/7`にhfuさんからのissueが立っていないか確認する
3. D1'(未レビューファイル棚卸し)への、hfuさんからのフィードバックが届いていれば対応する
4. cross-session messageで届いている新しい知見・確認依頼があれば、まずそれに対応する
5. 判断事項が3〜5件溜まったら、Planモードでの棚卸しレビューを再度提案する(D10 D1)
