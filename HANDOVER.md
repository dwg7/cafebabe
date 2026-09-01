# HANDOVER

## Status as of 2026-09-02

パターン集は6テーマに成長(maplibre-gl-js, markdown-file-conventions, progress-reporting,
gatekeeping, agent-repository-boundaries, open-mct, unattended-progress-visibility)。
`PROJECTS.md`(各プロジェクトのリポジトリへの永続リンク集)を新設。cafebabe自身の立ち上げも
`unopengis/7#993`として対外報告済み。`OPENMCT-NOTES.md`のsas0からの移管が完了し、
sas0/mapterhorn-japan-bridge/claude-mctの3リポジトリすべてでリンク張り替え済み。

hfuさんが約10時間離席中(2026-09-02開始)。「自律的にpush・大きな構造変更もDECISIONS.mdに
ADRとして記録した上で裁量で進めてよい」という方針の承認を得て運用中。

## Resolved since last handover

- D1の保留事項だった`OPENMCT-NOTES.md`移管を完了(D2)。sas0の同意プロセスも含め全工程完了
- プロジェクト固有知見と横断知見の粒立てについてhfuさんから問題提起があり、`PROJECTS.md`を
  新設して対応(D3)
- `CLAUDE.md`に「鮮度と分量を保つ責務」を新設(サイズ閾値・重複チェック・定期棚卸しのルール)
- vientiane-planning-map・stars-fd・mapterhorn-japan-bridge・sas0への横断ヒアリングから、
  5つの新パターンテーマを起こした

## Pending long-running tasks(急がず進める)

1. ~~「リポジトリ埋め込みの先行事例研究」パターン~~ — **完了(2026-09-02、DECISIONS.md D5)**。
   `patterns/case-study-research.md`(6パターン)・`patterns/data-provenance.md`(3パターン)
   として確定。9者(vientiane-planning-map, zukaku, stars-fd, height-coverage, kaga0,
   kitavolca, plateau-mago-implicit, mapterhorn-japan-bridge, claude-mct)から意見収集済み
2. 上記の経験を踏まえた上で、**全エージェントからのパターン提案募集**という次の段階に進む。
   10時間規模でゆっくり進めてよい(hfuさんの明示的な指示)。1で得た教訓(専用ファイル化は
   規模次第、陳腐化に注意、9者同時に聞くと収束が見えやすい)を活かして設計すること
3. 「スタイル設計・カートグラフィーの実地ノウハウ」(`patterns/style-composition.md`)の本格的な
   横断ヒアリング。zoom-stop設計、ラベル衝突回避、色のトーンマネジメント等。まだ1実例のみ
   (vientiane-planning-map)。stars-fd・height-coverage-a5・zukakuに同種の知見が個別に
   溜まっているはず、とvientiane-planning-mapから示唆あり。2が一段落してから着手する

## Known open items

- `patterns/open-mct.md`が300行を大きく超えている。「鮮度と分量を保つ責務」に照らすと
  サブテーマ(ブートストラップ/Plot API/キオスクモード/バージョン選択)ごとの分割候補だが、
  まだ未着手
- 「個別事情」タグと「プロジェクト固有すぎて`patterns/`に置かない(`PROJECTS.md`経由で
  リポジトリを指すだけにする)」の境界線は、運用しながら見極めている段階(D3参照)
- まだ他プロジェクトからのPRは来ていない。現状はcafebabeセッションがcross-session message
  でヒアリングし、自分で書き起こす運用になっている

## Where to look

- リポジトリ創設の経緯 → [DECISIONS.md](DECISIONS.md) D1
- `OPENMCT-NOTES.md`移管の経緯 → [DECISIONS.md](DECISIONS.md) D2
- プロジェクト固有/横断知見の粒立てと`PROJECTS.md`新設の経緯 → [DECISIONS.md](DECISIONS.md) D3
- 各プロジェクトのリポジトリ → [PROJECTS.md](PROJECTS.md)
- 現在のパターン集 → [README.md](README.md)の一覧参照
- 運用ガイド(鮮度と分量を保つ責務含む) → [CLAUDE.md](CLAUDE.md)
- 貢献の仕方 → [CONTRIBUTING.md](CONTRIBUTING.md)

## Resume prompt

次にこのリポジトリを触るときにやること:
1. このHANDOVER.mdと直近のDECISIONS.mdエントリ(D2・D3)を読んで経緯を把握する
2. `patterns/open-mct.md`の分割を検討するタイミングか判断する(次にテーマが1〜2件増えた
   タイミングが目安)
3. cross-session messageで届いている新しい知見・確認依頼があれば、まずそれに対応する
4. hfuさんが不在の間に大きな判断(構造変更・新規PR受け入れ等)をした場合は、DECISIONS.mdに
   ADRとして記録しておき、hfuさんが戻ってきたときに一覧で確認できるようにする
