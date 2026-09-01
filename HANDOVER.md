# HANDOVER

## Status as of 2026-09-02

パターン集は18テーマに成長(maplibre-gl-js, markdown-file-conventions, progress-reporting,
gatekeeping, agent-repository-boundaries, open-mct, unattended-progress-visibility,
large-data-pitfalls, style-composition, case-study-research, data-provenance,
agent-execution-gotchas, verification-discipline, local-dev-pitfalls,
robust-pipeline-design, ci-cd-pitfalls, interoperability, raspberry-pi-appliance)。
`PROJECTS.md`(9プロジェクトのリポジトリ永続リンク集)、`DWG7-CONTEXT.md`(組織のビジョン・
カルチャー・技術方針)を保有。cafebabe自身の立ち上げも`unopengis/7#993`として対外報告済み。
`OPENMCT-NOTES.md`のsas0からの移管完了。

「先行事例研究」パターン(D5)・「全エージェントパターン提案募集」(D6)の2つの横断タスクが
完了。D6では9プロジェクト全員(vientiane-planning-map, zukaku, stars-fd, height-coverage,
kaga0, kitavolca, plateau-mago-implicit, mapterhorn-japan-bridge, sas0)から合計約36件の
知見が届き、すべて処理済み。

hfuさんが約10時間離席中(2026-09-02開始、途中Dispatch経由でフリート状況照会1回あり、
cafebabeからは「要判断事項なし」と回答済み)。「自律的にpush・大きな構造変更もDECISIONS.md
にADRとして記録した上で裁量で進めてよい」という方針の承認を得て運用中。

## Resolved since last handover

- D1の保留事項だった`OPENMCT-NOTES.md`移管を完了(D2)
- プロジェクト固有知見と横断知見の粒立てについて`PROJECTS.md`を新設して対応(D3)
- `CLAUDE.md`に「鮮度と分量を保つ責務」を新設
- dwg7組織文脈ブリーフィングを`DWG7-CONTEXT.md`として保存、`CLAUDE.md`に反映(D4)
- 「リポジトリ埋め込みの先行事例研究」パターンを9プロジェクトから意見収集して取りまとめ
  完了(D5)。「専用ファイルに切り出す」の一般則を「専用ファイル化は規模に応じた判断」に修正
- **「全エージェントからのパターン提案募集」完了(D6)**。9プロジェクト全員から自由回答形式で
  知見を集め、新規テーマ7本(agent-execution-gotchas, verification-discipline,
  local-dev-pitfalls, robust-pipeline-design, ci-cd-pitfalls, interoperability,
  raspberry-pi-appliance)+既存9ファイルへの追記として反映。全員へ結果共有まで完了

## Pending long-running tasks(急がず進める)

1. ~~「リポジトリ埋め込みの先行事例研究」パターン~~ — **完了(D5)**
2. ~~全エージェントからのパターン提案募集~~ — **完了(D6)**
3. **次はこれに着手する**: 「スタイル設計・カートグラフィーの実地ノウハウ」
   (`patterns/style-composition.md`)の本格的な横断ヒアリング。zoom-stop設計、ラベル衝突
   回避、色のトーンマネジメント等。まだ1実例のみ(vientiane-planning-map)。stars-fd・
   height-coverage-a5・zukakuに同種の知見が個別に溜まっているはず、とvientiane-planning-map
   から示唆あり。D5・D6と同じ進め方(まずvientiane-planning-mapを深掘り→案作成→他プロジェクト
   へ展開)が有効だと思われる

## Known open items

- `patterns/open-mct.md`(300行超)・`patterns/case-study-research.md`(約280行)が
  「鮮度と分量を保つ責務」のサイズ閾値に近い/超えている。パターン集が18テーマまで増えたため、
  そろそろ**`patterns/`のサブディレクトリ化(テーマ分類)を検討するタイミング**かもしれない
  (README.mdの一覧が長大になってきている)
- 「個別事情」タグと「プロジェクト固有すぎて`patterns/`に置かない(`PROJECTS.md`経由で
  リポジトリを指すだけにする)」の境界線は、運用しながら見極めている段階(D3参照)
- まだ他プロジェクトからのPRは来ていない。現状はcafebabeセッションがcross-session message
  でヒアリングし、自分で書き起こす運用になっている
- D6で得た教訓(D6のDECISIONS.md追記参照): 自由回答形式は「発散」が主で、テーマ別分類の
  負荷が高い。次に知見募集をするなら、合意形成が目的か棚卸しが目的かで、特定テーマ提示
  (D5方式)と自由回答(D6方式)を使い分けるとよい

## Where to look

- リポジトリ創設の経緯 → [DECISIONS.md](DECISIONS.md) D1
- `OPENMCT-NOTES.md`移管の経緯 → [DECISIONS.md](DECISIONS.md) D2
- プロジェクト固有/横断知見の粒立てと`PROJECTS.md`新設の経緯 → [DECISIONS.md](DECISIONS.md) D3
- dwg7組織文脈の取り込みの経緯 → [DECISIONS.md](DECISIONS.md) D4、全文は[DWG7-CONTEXT.md](DWG7-CONTEXT.md)
- 「先行事例研究」パターンの取りまとめ経緯 → [DECISIONS.md](DECISIONS.md) D5
- 「全エージェントパターン提案募集」の経緯 → [DECISIONS.md](DECISIONS.md) D6
- 各プロジェクトのリポジトリ → [PROJECTS.md](PROJECTS.md)
- 現在のパターン集 → [README.md](README.md)の一覧参照
- 運用ガイド(鮮度と分量を保つ責務、dwg7組織文脈の注意点含む) → [CLAUDE.md](CLAUDE.md)
- 貢献の仕方 → [CONTRIBUTING.md](CONTRIBUTING.md)

## Resume prompt

次にこのリポジトリを触るときにやること:
1. このHANDOVER.mdと直近のDECISIONS.mdエントリ(D5・D6)を読んで経緯を把握する
2. 上記「Pending long-running tasks」の3番(スタイル設計の横断ヒアリング)に着手する。
   ListAgentsで現在アクティブなエージェント一覧を確認し(セッション名は変わっている可能性が
   ある)、vientiane-planning-mapに詳細ヒアリング→案作成→他プロジェクトへ展開、という
   D5・D6と同じ流れで進める
3. `patterns/`のサブディレクトリ化(18テーマまで増えた)を検討するかどうか判断する
4. cross-session messageで届いている新しい知見・確認依頼があれば、まずそれに対応する
5. hfuさんが不在の間に大きな判断をした場合は、DECISIONS.mdにADRとして記録しておく
