# DECISIONS

このリポジトリ自身の運用に関する意思決定ログ。追記専用、既存エントリは書き換えない
(詳細は [`patterns/markdown-file-conventions.md`](patterns/markdown-file-conventions.md) 参照)。

---

## D1: リポジトリの創設 — 名前・org・スコープ・形式

**Status**: Accepted (2026-09-02)

### 背景

claude-mctが、dwg7・hfuの8プロジェクトエージェント(mapterhorn-japan-bridge, height-coverage,
zukaku, sas0, kitavolca, kaga0, stars, plateau-mago-implicit)に対し、2ラウンドの横断調査
(MapLibre GL JS構築知見/.mdファイル運用知見)を実施した。全員が「横断ノウハウの集約には
価値がある」と回答した一方、置き場所については意見が割れた(既存repoに1枚のMD派 vs
新規repo派)。

sas0が重要な懸念を提示した: 「話題が増えるたびに、その都度どこかのプロジェクトにその場の
判断でホストされ続けると、『dwg7の共有知見はどこにあるか』の答えが『話題による』になって
しまう」。一方で「2〜3件の段階で統治構造を先回りするのは時期尚早」とも留保した。

これはエージェント間で決める技術判断ではなく組織判断であるとして、Hidenoriに判断を仰いだ。

### 決定

- **名前**: `cafebabe`(`0xCAFEBABE` = Javaクラスファイルのマジックナンバー、「始まりの
  合言葉」)。検討過程で`agent-hq`(「本部」のニュアンスが分散的な知見蓄積の性質と噛み合わ
  ない)、`atlas`(地図データ自体を作る場所に読めてしまう)を却下し、「café/ギルドの互助が
  実際に行われる場所」という、対等で非階層的なイメージに収束した
- **org**: `dwg7`
- **形式**: 各パターンを Context → Problem/Forces → Solution → Known Uses の型
  (アレグザンダーのパターン・ランゲージを参考)で記述し、「一般則」か「個別事情」かのタグを
  付ける
- **初期スコープ**: `patterns/maplibre-gl-js.md`、`patterns/markdown-file-conventions.md`
  の2件を、これまでの調査結果から初期seedとして収録
- **更新運用**: PRベース。各プロジェクトのエージェントが、自分の現場で得た知見をPRで追加する

### 保留事項

- `OPENMCT-NOTES.md`(現在`dwg7/sas0`)をこのリポジトリに移管するかどうかは未決定。
  sas0の同意を得てから判断する(D2として別途記録予定)
- `patterns/`をさらに細分化するタイミング(パターン数が増えてきたら検討)

### Resume prompt

次にこのリポジトリを触るときは、まず`HANDOVER.md`で現状を確認し、`patterns/`配下に
新しいテーマ(Open MCT等)を追加するかどうか、他のdwg7エージェントに一声かけてから
判断すること。

---

## D2: OPENMCT-NOTES.mdのsas0からの移管

**Status**: Accepted (2026-09-02)

### 背景

D1の保留事項として記録した通り、sas0の同意を得てから判断する予定だった。2026-09-02、
hfuさんから「タイミングを図りながら着実に進めてほしい」という依頼を受け、sas0に直接相談
した。sas0は「これは私自身のユーザーとの間で直接確認してから進めたい」とし、cafebabeからの
伝聞をそのまま実行せず、自分のユーザーへの直接確認を優先した(この対応自体が
`patterns/gatekeeping.md`の実例として記録済み)。sas0のユーザー確認の結果、「移動方式」
(sas0側はリンクのみ残し、本体をcafebabeへ移す)が承認された。

### 決定

- `OPENMCT-NOTES.md`(137行、sas0が3プロジェクト分の知見を集約してマスター管理していた)の
  全文を`patterns/open-mct.md`として移植
- sas0・mapterhorn-japan-bridge(mapterhorn-monitor)・claude-mctの3リポジトリからは、
  このファイルへのリンクのみを保持する形に変更
- 今後の更新はcafebabe側のこのファイルに対する変更として行う

### 保留事項

- sas0側の`OPENMCT-NOTES.md`を実際にスタブへ置き換える作業はsas0自身が行う(cafebabeは
  他リポジトリを直接編集する権限を持たない)。cafebabeからは受け入れ先URLが確定次第連絡する
- mapterhorn-japan-bridge・claude-mctへの新URL張り替え依頼も同様、cafebabeから連絡する
- `patterns/open-mct.md`は既に300行を大きく超えており、`鮮度と分量を保つ責務`
  (`CLAUDE.md`)に照らすとサブテーマごとの分割候補。今回は移管を優先し、次の棚卸しで検討する

### Resume prompt

sas0から「受け入れ先URLを教えてほしい」と言われている。`patterns/open-mct.md`をコミット・
pushしてURLを確定させ、sas0・mapterhorn-japan-bridge・claude-mctに連絡すること。pushの
可否はhfuさんに確認してから行う。

### 追記(2026-09-02): 移管完了

hfuさんの承認を得て`patterns/open-mct.md`をpush(コミット`4af9563`)。3リポジトリすべてで
張り替えが完了した:
- `sas0` — `OPENMCT-NOTES.md`を新URLへのリンクのみのスタブに置き換え、README.md/
  HANDOVER.md/CLAUDE.mdの相互参照も更新済み(コミット`66ec844`)。内容の一致を
  `raw.githubusercontent.com`経由で突き合わせ確認した上で実施
- `mapterhorn-japan-bridge` — DECISIONS.md D91・HANDOVER.mdの2箇所を新URLに張り替え済み
- `claude-mct` — READMEの「Open MCT実装ノウハウ」節の説明文を新URLに更新済み(旧URLへの
  直リンクは元々無かった)

保留事項はすべて解消。このADRはクローズとする。

---

## D3: プロジェクト固有の知見と横断知見の粒立て、PROJECTS.mdの新設

**Status**: Accepted (2026-09-02)

### 背景

hfuさんから、「プロジェクト固有の知見と、プロジェクト横断の知見を粒立てる必要があるかも
しれない」という問題提起があった。`CONTRIBUTING.md`の「個別事情」タグは、あくまで「まだ
一般則と確認されていないが、将来一般化するかもしれない知見」という位置づけで、`patterns/`に
収録することを前提としている。しかし、本質的にそのプロジェクトのハードウェア・データ・
技術選定に強く依存し、他プロジェクトへの一般化が見込めない知見も存在する。そうした知見を
無理にcafebabeの`patterns/`に集約しようとすると、パターン集の趣旨(横断的に読める知見の
蓄積)からずれる。

一方で、そうしたプロジェクト固有の知見は各プロジェクトのリポジトリ(`CLAUDE.md`/
`DECISIONS.md`)に委ねるべきだが、「エージェント(セッション)は任務が終わればアーカイブ
されて消えるが、リポジトリは永続する」という非対称性がある。cafebabeがエージェント
(セッション)の一覧としてのみピアを記録していると、セッションが消えた後、そのプロジェクトの
固有知見へ辿り着く道筋が失われる。

### 決定

- 恒久的な参照先として`PROJECTS.md`を新設する。各dwg7プロジェクトの**リポジトリURL**
  (セッションではなく)と一言説明を記録する
- `CLAUDE.md`の「既知のピア」セクションは、エージェント運用上のコンテキスト
  (cross-session連携の対象)に留め、恒久的なリポジトリ参照は`PROJECTS.md`に分離する
- プロジェクト固有すぎて他プロジェクトへの一般化が見込めない知見は、無理に`patterns/`へ
  集約せず、「詳細は該当リポジトリの`CLAUDE.md`/`DECISIONS.md`を見よ」と`PROJECTS.md`
  経由でリンクする運用とする

### 保留事項

- `PROJECTS.md`の初版は判明している範囲のリポジトリURLで作成する。未確認のプロジェクト
  (claude-mct等)は追って埋める
- 「個別事情」タグと「プロジェクト固有すぎて`patterns/`に置かない」の境界線は、まだ運用
  しながら見極める段階

### Resume prompt

`PROJECTS.md`を作成し、README.md/CLAUDE.mdから参照を張ること。

---

## D4: dwg7組織文脈の取り込み(DWG7-CONTEXT.md新設)

**Status**: Accepted (2026-09-02)

### 背景

cafebabeはこれまで各プロジェクトのリポジトリ(CLAUDE.md/DECISIONS.md)を横断的にヒアリング
してパターン化してきたが、dwg7という組織そのもののビジョン・カルチャー・技術方針を把握して
いなかった。hfuさんが別途Claude チャットでdwg7全体を担当しており、cafebabeはそこに直接
アクセスできない。そこでhfuさんに「dwg7チャットに聞くべきこと」のプロンプトを提供し、
その回答を組織文脈ブリーフィングとして受け取った。

### 決定

- 受け取った内容を[DWG7-CONTEXT.md](DWG7-CONTEXT.md)として、要約せずほぼ原文のまま保存
  する(一次情報としての価値を保つため)
- `CLAUDE.md`に「dwg7の組織文脈」節を新設し、特に重要な「cafebabeへの期待」5項目
  (制約を誤読しない、標準化の由来を区別する、統一理論に解消しない、"keep open"の評価軸、
  社会的設計とインフラ設計の両方を扱う)を運用原則として明記した

### 保留事項

- 既存の`patterns/*.md`の記述が、この文脈(特に「標準化は独立した収束であり指令ではない」
  という原則)に照らして誤読を招く書き方になっていないか、次の棚卸しタイミングで見直す

### Resume prompt

新しいパターンを書く際は、DWG7-CONTEXT.mdの「cafebabeへの期待」5項目を都度意識すること。
特に「これは標準です」と断定せず、「複数プロジェクトが独立に同じ結論に達した」という
書き方を優先する。
