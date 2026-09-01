# HANDOVER

## Status as of 2026-09-02

パターン集は11テーマに成長(maplibre-gl-js, markdown-file-conventions, progress-reporting,
gatekeeping, agent-repository-boundaries, open-mct, unattended-progress-visibility,
large-data-pitfalls, style-composition, case-study-research, data-provenance)。
`PROJECTS.md`(各プロジェクトのリポジトリへの永続リンク集、9プロジェクト分)、
`DWG7-CONTEXT.md`(組織のビジョン・カルチャー・技術方針、hfuさん経由でdwg7チャットから
取得)を新設。cafebabe自身の立ち上げも`unopengis/7#993`として対外報告済み。
`OPENMCT-NOTES.md`のsas0からの移管が完了し、sas0/mapterhorn-japan-bridge/claude-mctの
3リポジトリすべてでリンク張り替え済み。「先行事例研究」パターンは9プロジェクトから意見収集
して取りまとめ完了(DECISIONS.md D5)。

hfuさんが約10時間離席中(2026-09-02開始、途中Dispatch経由でフリート状況照会あり、
cafebabeからは「要判断事項なし」と回答済み)。「自律的にpush・大きな構造変更も
DECISIONS.mdにADRとして記録した上で裁量で進めてよい」という方針の承認を得て運用中。

## Resolved since last handover

- D1の保留事項だった`OPENMCT-NOTES.md`移管を完了(D2)。sas0の同意プロセスも含め全工程完了
- プロジェクト固有知見と横断知見の粒立てについてhfuさんから問題提起があり、`PROJECTS.md`を
  新設して対応(D3)
- `CLAUDE.md`に「鮮度と分量を保つ責務」を新設(サイズ閾値・重複チェック・定期棚卸しのルール)
- hfuさん経由でdwg7チャットから組織文脈ブリーフィングを取得し、`DWG7-CONTEXT.md`として
  保存、`CLAUDE.md`にパターン化時の注意5項目を反映(D4)
- 「リポジトリ埋め込みの先行事例研究」パターンを、vientiane-planning-mapへの詳細ヒアリング
  →案作成→本人確認→他8プロジェクト全員への意見収集、という手順で取りまとめ完了(D5)。
  当初「専用ファイルに切り出す」を一般則としていたが、9者中6者の「規模的に時期尚早」という
  フィードバックを受け「専用ファイル化は規模に応じた判断」に修正した
- vientiane-planning-map・stars-fd・mapterhorn-japan-bridge・sas0への横断ヒアリングから、
  複数の新パターンテーマを起こした

## Pending long-running tasks(急がず進める)

1. ~~「リポジトリ埋め込みの先行事例研究」パターン~~ — **完了(2026-09-02、DECISIONS.md D5)**
2. ~~全エージェントからのパターン提案募集~~ — **一次取りまとめ完了(2026-09-02、
   DECISIONS.md D6)**。8/9プロジェクトから約30件の知見が届き、6新規テーマ+6既存ファイルへの
   追記として反映済み。**kaga0のみ未着**(6件の草稿を用意中、プロジェクト側の最終確認後に
   提出予定)。kaga0の提出が届いたら追記し、全員に結果を共有する
3. 「スタイル設計・カートグラフィーの実地ノウハウ」(`patterns/style-composition.md`)の本格的な
   横断ヒアリング。zoom-stop設計、ラベル衝突回避、色のトーンマネジメント等。まだ1実例のみ
   (vientiane-planning-map)。stars-fd・height-coverage-a5・zukakuに同種の知見が個別に
   溜まっているはず、とvientiane-planning-mapから示唆あり。2が一段落してから着手する

## Known open items

- `patterns/open-mct.md`(300行超)・`patterns/case-study-research.md`(約210行)が
  「鮮度と分量を保つ責務」のサイズ閾値に近い/超えている。次の棚卸しタイミングで分割を検討
  (open-mctはサブテーマ: ブートストラップ/Plot API/キオスクモード/バージョン選択で分割候補)
- 「個別事情」タグと「プロジェクト固有すぎて`patterns/`に置かない(`PROJECTS.md`経由で
  リポジトリを指すだけにする)」の境界線は、運用しながら見極めている段階(D3参照)
- まだ他プロジェクトからのPRは来ていない。現状はcafebabeセッションがcross-session message
  でヒアリングし、自分で書き起こす運用になっている
- 軽微な事務ミス2件(いずれも解決済み、記録として残す): ①`case-study-research.md`のコミット
  漏れ(vientiane-planning-mapの指摘で発覚)。②mapterhorn-japan-bridgeから伝えられた
  リポジトリ名`hfu-mapterhorn`の誤り(実際は`hfu/mapterhorn`、ローカルパス名との混同)。
  どちらも「答える側は記憶で即答せず確認する」「pushし忘れがないかgit statusで確認する」
  という教訓として、`patterns/agent-repository-boundaries.md`に反映済み

## Where to look

- リポジトリ創設の経緯 → [DECISIONS.md](DECISIONS.md) D1
- `OPENMCT-NOTES.md`移管の経緯 → [DECISIONS.md](DECISIONS.md) D2
- プロジェクト固有/横断知見の粒立てと`PROJECTS.md`新設の経緯 → [DECISIONS.md](DECISIONS.md) D3
- dwg7組織文脈の取り込みの経緯 → [DECISIONS.md](DECISIONS.md) D4、全文は[DWG7-CONTEXT.md](DWG7-CONTEXT.md)
- 「先行事例研究」パターンの取りまとめ経緯 → [DECISIONS.md](DECISIONS.md) D5
- 各プロジェクトのリポジトリ → [PROJECTS.md](PROJECTS.md)
- 現在のパターン集 → [README.md](README.md)の一覧参照
- 運用ガイド(鮮度と分量を保つ責務、dwg7組織文脈の注意点含む) → [CLAUDE.md](CLAUDE.md)
- 貢献の仕方 → [CONTRIBUTING.md](CONTRIBUTING.md)

## Resume prompt

次にこのリポジトリを触るときにやること:
1. このHANDOVER.mdと直近のDECISIONS.mdエントリ(D4・D5)、`DWG7-CONTEXT.md`を読んで経緯・
   組織文脈を把握する
2. 上記「Pending long-running tasks」の2番(全エージェントからのパターン提案募集)に着手する。
   ListAgentsで現在アクティブなエージェント一覧を確認し(セッション名は変わっている可能性が
   ある)、各エージェントに「あなたのプロジェクトで他に共有する価値がある知見は何か」を
   自由回答で尋ねる。急がず、返信が来るたびに丁寧にパターン化する
3. `patterns/open-mct.md`・`patterns/case-study-research.md`の分割を検討するタイミングか
   判断する
4. cross-session messageで届いている新しい知見・確認依頼があれば、まずそれに対応する
5. hfuさんが不在の間に大きな判断(構造変更・新規PR受け入れ等)をした場合は、DECISIONS.mdに
   ADRとして記録しておき、hfuさんが戻ってきたときに一覧で確認できるようにする
