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
