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

---

## D5: 「リポジトリ埋め込みの先行事例研究」パターンの取りまとめ

**Status**: Accepted (2026-09-02)

### 背景

hfuさんから、「vientiane-planning-mapが先行事例研究をリポジトリに埋め込む形で蓄積している。
これが新しいパターンとなる可能性がある。vientiane-planning-mapにまず相談し、パターン案が
できたら、現在アクティブなすべてのエージェントに紹介をして、その可否も含めて取りまとめて
みてほしい」という依頼があった。急がず、エージェント自律でノウハウを集約するよう指示された。

進め方: vientiane-planning-mapへの詳細ヒアリング(`CASE_STUDIES.md`実例確認)→
`patterns/case-study-research.md`案作成→本人確認→他8プロジェクト
(zukaku, stars-fd, height-coverage, kaga0, kitavolca, plateau-mago-implicit,
mapterhorn-japan-bridge, claude-mct)全員への紹介・意見収集、という順で進めた。

### 決定

9者の回答から強い収束が見られた:

1. **「専用ファイル化は無条件の一般則ではなく、規模に応じた判断」** — 当初案は「先行事例
   研究は専用ファイルに切り出す」を一般則としていたが、修正した。閾値の目安: 参照事例が
   4〜5件以上、同じ事例が複数の決定に重複して現れる、量が決定ログ本流を圧迫する、読者層が
   明確に違う。sas0・kaga0・height-coverage・kitavolca・stars-fd・plateau-mago-implicitは
   いずれも「現状の規模では専用ファイルは時期尚早」と判断し、決定ログへのインライン記録に
   留めている。vientiane-planning-map・claude-mctは実際に専用ファイルを運用中
2. **「見送った理由を記録する」規律は、専用ファイルの有無に関わらず全員が価値を認めた**
3. **陳腐化リスクへの注意**が複数プロジェクト(plateau-mago-implicit、stars-fd、
   mapterhorn-japan-bridge)から共通して指摘された。調査記録には「いつ時点か」の明記と、
   決定ログとの相互リンク(一方向でなく双方向)が対策として提案された
4. 新パターンとして2件追加:
   - kaga0からの提案: 「一つの前例を鵜呑みにせず、適用範囲を検証する」(複数事例比較の逆——
     単一の前例をそのまま踏襲する際の検証漏れリスク)
   - mapterhorn-japan-bridgeからの提案: 「データ出自を文書ではなく成果物自体に埋め込む」
     (lineageタイルの実装)。`patterns/data-provenance.md`に追加

最終的に`patterns/case-study-research.md`(6パターン)と`patterns/data-provenance.md`
(3パターン)として確定。

### 保留事項

- `patterns/case-study-research.md`が既に300行に近づいている。次の棚卸しタイミングで
  分割を検討する余地あり

### Resume prompt

このタスクは完了。次にこの領域を触るときは、まず`patterns/case-study-research.md`と
`patterns/data-provenance.md`を読んで、今回の9者の知見を前提にすること。

---

## D6: 全エージェントからのパターン提案募集(開始)

**Status**: Accepted (2026-09-02)

### 背景

hfuさんから、「D5(先行事例研究パターン)の経験が一通り積めたら、次の段階として全エージェント
からパターン提案を取り付けてみてほしい。10時間くらいのオーダーでゆっくり進めてよい」という
依頼があった。D5との違い: D5は特定テーマ(先行事例研究)を提示して意見を聞く形だったが、
今回はテーマを固定せず、各プロジェクトが「他プロジェクトに共有する価値がある」と考える知見を
自由回答で募る。

### 決定

- 9プロジェクト(vientiane-planning-map, zukaku, stars-fd, height-coverage, kaga0,
  kitavolca, plateau-mago-implicit, mapterhorn-japan-bridge, claude-mct)に、自由回答形式の
  募集メッセージを送る。観点の例(技術的発見・運用上の工夫・失敗から得た教訓・プロジェクト
  固有だが再現性のある課題)を示しつつ、それに縛られないことを明記する
- 受け取った提案の整理方針: ①既存パターンファイルへの追記、②新規テーマとして起票、③今は
  規模的に時期尚早(該当プロジェクトの決定ログへのインライン記録のままで良い、とD5の結論を
  踏まえて助言する)、の3パスに振り分ける
- D5で得た教訓(専用ファイル化は規模次第、陳腐化への注意、具体的な実例URLを添えて聞くと
  実地の回答が返ってくる)を踏まえて設計する

### 保留事項

- 返信の粒度・形式がD5よりバラつく可能性が高い。集まった内容次第で、取りまとめの構成
  (テーマ別か、プロジェクト別か)は柔軟に判断する

### Resume prompt

返信が集まるたびに、まず該当プロジェクトへの受領確認を返し、内容を評価してから
①②③のいずれかに振り分ける。全員から返信が揃うか、相当な時間が経過したら、D5と同様に
取りまとめをDECISIONS.mdに記録し、全員に結果を共有する。

### 追記(2026-09-02): 一次取りまとめ完了(kaga0のみ待ち)

9プロジェクト中8プロジェクト(vientiane-planning-map, zukaku, stars-fd, height-coverage,
kitavolca, plateau-mago-implicit, mapterhorn-japan-bridge, sas0)から、合計約30件の知見が
届いた。kaga0のみ「6件の草稿を用意中、プロジェクト側の最終確認後に提出」と連絡あり、未着。

届いた知見は以下のパターンファイルに反映した:
- 既存ファイルへの追記: `maplibre-gl-js.md`(3件)、`markdown-file-conventions.md`(2件)、
  `case-study-research.md`(2件)、`gatekeeping.md`(1件)、`data-provenance.md`(1件)、
  `verification-discipline.md`(2件、新規作成直後に追加)
- 新規テーマ: `agent-execution-gotchas.md`(5実例、Claude Codeエージェント自身の実行環境の
  癖)、`verification-discipline.md`(4実例、検証・デバッグの規律)、`local-dev-pitfalls.md`
  (4実例)、`robust-pipeline-design.md`(2実例)、`ci-cd-pitfalls.md`(1実例)、
  `interoperability.md`(1実例)

作業用一時ファイル`patterns/_intake-2026-09-02.md`に生データを保存してから整理し、処理完了
後に削除した(compact対策として一時的に使用)。

kaga0からの提出が届き次第、同様に振り分けて追記する。全員分が出揃った時点で、D5のように
全員へ結果を共有する。

### 追記(2026-09-02): kaga0提出分を反映、9/9プロジェクト完了

kaga0から6件の提出([`docs/rpi4b-patterns-draft.md`](https://github.com/dwg7/kaga0/blob/main/docs/rpi4b-patterns-draft.md))
が届いた。既にCONTRIBUTING.mdの型に沿って書かれた高品質な草稿だったため、大きな書き直しは
せず、タグをcafebabeの規則(一般則/個別事情)に合わせて`patterns/raspberry-pi-appliance.md`
として新規起票した。RPi4B固有の実例が1件(kaga0)のみのパターンは「個別事情」寄り、
appliance設計として一般化できるもの(`Conflicts=`によるgetty自動排他)は「一般則」とした。

これで9プロジェクト全員からの提出が完了。合計約36件の知見が、新規テーマ7本
(`agent-execution-gotchas.md`, `verification-discipline.md`, `local-dev-pitfalls.md`,
`robust-pipeline-design.md`, `ci-cd-pitfalls.md`, `interoperability.md`,
`raspberry-pi-appliance.md`)+既存9ファイルへの追記として反映された。パターン集は
maplibre-gl-js・markdown-file-conventionsを含め計18テーマに成長。

D5との違いとして記録に値する点: D5(先行事例研究)は特定テーマを提示して意見を聞いたため
「収束」(強い合意点)が見えやすかった。D6(自由回答)は逆に「発散」(各プロジェクト固有の
知見が大量に出る)が主で、収束よりも「テーマ別の分類作業」が主な負荷だった。次に同様の
募集をするなら、自由回答と特定テーマ提示のどちらを選ぶかは、知りたいものが「合意形成」か
「知見の棚卸し」かで使い分けるとよい。

### Resume prompt(更新)

D6は完了。9プロジェクト全員への結果共有を行うこと。次のタスクは
[HANDOVER.md](../HANDOVER.md)の「Pending long-running tasks」3番
(スタイル設計・カートグラフィーの横断ヒアリング)に進む。

---

## D7: スタイル設計・カートグラフィーの実地ノウハウ(横断ヒアリング完了)

**Status**: Accepted (2026-09-02)

### 背景

hfuさんから「頭出し」として提起され(D6完了後の指示)、vientiane-planning-mapの1実例
(symbolレイヤーの安定ソート)を起点に、D5・D6と同じ進め方(深掘り→他プロジェクトへ展開)で
本格的な横断ヒアリングを実施した。

### 決定

vientiane-planning-mapへの深掘り(zoom-stop設計・ラベル衝突回避・色のトーンマネジメント)、
続けてstars-fd(配信元・ゲートキーパーの視点)・height-coverage・zukaku(印刷特化)への
展開を行い、`patterns/style-composition.md`に9パターンとして集約した:

1. symbolレイヤーは合成後に配列末尾へ安定ソートする
2. 色相・彩度・明度による強調は、1つのレイヤーだけに独占させる(視覚的ヒエラルキー)
3. zoom-stopの閾値は勘で決めず、先行事例の実装コードを参考にする
4. 権威ある元データの配色は、独自解釈を加えず忠実に再現する
5. ラベルの衝突検出を、あえて無効化した方がよい場合がある
6. 自作の重ね書き要素は、ベースマップに依存しない固定スタイルで押し通す
7. 印刷物はズームレベルが焼き付けで固定される

特筆すべき発見:
- **視覚的ヒエラルキー原則の独立収束**: height-coverageは結果論的に(意図せず)この原則を
  満たしていたが、vientiane-planning-mapは同じ原則に意図的に辿り着いた。時系列としては
  height-coverageの経験が先。これはDWG7-CONTEXT.mdが言う「独立した収束」の実例
- **配色戦略の分岐**: vientiane-planning-map(独自に視覚的ヒエラルキーを設計する)と
  stars-fd(権威ある元データの配色を忠実に再現する)は対照的なアプローチだが、どちらも
  「複数レイヤーが独立に色分けを競合させない」という同じ上位原則を別の手段で実現している
- 副産物として`patterns/gatekeeping.md`に「政治的にセンシティブな判断は技術レビューと別枠で
  確認する」を追加(stars-fdの海洋境界線表示の実例)

### 保留事項

- `patterns/style-composition.md`が211行まで成長。次の棚卸しで分割候補
- kaga0・kitavolca・plateau-mago-implicit・sas0・mapterhorn-japan-bridge・claude-mctへの
  スタイル設計ヒアリングはまだ行っていない(地図描画を持たないプロジェクトもあるため、
  全員に聞く必要はない可能性がある)

### Resume prompt

このタスクは一旦完了。地図描画を持つ他のプロジェクト(kaga0、kitavolca等)にも展開する
価値があるか判断してから、必要なら追加ヒアリングする。次の大きなタスクは未定——
HANDOVER.mdのKnown open items(`patterns/`のサブディレクトリ化検討等)から選ぶか、
hfuさんの新しい指示を待つ。

---

## D8: staccato-spec 4パーティモデルの取り込みと一般化拡張の議論(開始)

**Status**: Accepted (2026-09-02)

### 背景

hfuさんから、以下3テーマが「インターエージェントで議論をして進められそう」と提起された:
- ベクトルタイルデザイン(サイズ最適化)
- スタイルデザイン(レイヤの上下関係、terrain/hillshadeの扱い)
- `staccato-spec`にあるUser/Staff/Cartographer/Library概念の一般化拡張

3番目について、「staccato-specに解説してもらうかリンクをもらってから、全エージェントとの
議論を始めるといい。特にstarsにLibrary概念を踏まえてもらうことが重要」との指示があった。

`staccato-spec`という名前のアクティブなエージェントセッションは存在しなかったため、代わりに
リポジトリ本体([`UNopenGIS/staccato-spec`](https://github.com/UNopenGIS/staccato-spec))を
cafebabeが直接読んで理解し、`STACCATO-CONTEXT.md`として一次情報を保存した。

### 決定

- `STACCATO-CONTEXT.md`を新設。4パーティモデル(User=意図所有、Staff=意味解釈所有、
  Cartographer=描画所有、Library=データ公開・発見可能性所有)の定義、faceless
  Cartographerパターン、参照実装(`layers-martin`、`faceless-cartographer`)を記録
- 重要な発見として、`stars.optgeo.org`(stars-fd管理)が実は既にstaccato文脈での
  "Library"として機能している(複数のLibraryカタログをMap Intentに並べるだけでよく、
  集約コンポーネント不要という実証)ことを記録
- starsへ、この「Library」という自己認識を持ってもらうよう個別に連絡する
- 全エージェントへ、4ロールモデルのdwg7全体への一般化拡張について議論を呼びかける

### 保留事項

- 「一般化拡張」の具体的な問い(cafebabe自身はどのロールに近いか、各プロジェクトをどう
  マッピングするか等)は、議論が始まってから形になる。現時点では土台の共有に留める
- 「ベクトルタイルデザインのサイズ最適化」「terrain/hillshadeの扱い」の2テーマは、
  staccato議論と並行して、別途横断ヒアリングの対象として控えている(未着手)

### Resume prompt

starsへLibrary概念の連絡を送り、全エージェントへ一般化拡張の議論を呼びかけること。
議論が進んだら、結果を`STACCATO-CONTEXT.md`または新規`patterns/`テーマとして記録する。
その後、残る2テーマ(ベクトルタイルサイズ最適化、terrain/hillshade)にも着手する。

### 追記(2026-09-02): 9プロジェクト全員から回答、議論を統合

stars-fd(Library役割について)+9プロジェクト全員(vientiane-planning-map, zukaku,
plateau-mago-implicit, kitavolca, height-coverage, mapterhorn-japan-bridge, kaga0, sas0,
claude-mct)から回答が揃った。`STACCATO-CONTEXT.md`に「dwg7全体への一般化拡張」節として
統合済み。

主な発見:
1. dwg7の大半のプロジェクトは「開発時に一度だけ意図が固定される静的成果物」であり、
   STACCATOが前提とする「実行時のライブな対話型パイプライン」とは根本的に異なる
   (sas0の言う「動的生成型 vs 静的キュレーション型」の軸)
2. Library/Cartographerの分離は、staccato-specを知らずに独立して実践されていた
   プロジェクトが複数(DWG7-CONTEXT.mdの「独立した収束」の再現)
3. facelessの「反例」に見えたものの多くは、実はCartographer層ではなくUser向け操作画面の
   URL状態であり、役割を正しく再整理すれば矛盾しない(zukakuの整理)
4. kaga0から「Live Library」対「Frozen/Cached Library」という新しい軸の提案
5. sas0から「人間による説明責任のhandoff」には、Staff→Cartographerだけでなく「上流の
   権威(発表機関等)に対する謙虚さ」という別方向もあるという指摘
6. claude-mctから、cafebabe自身は「Staff+Libraryのハイブリッド」という外部評価

一般化拡張の「答え」を確定させることはせず、議論の記録として保存する形で一区切りとした。
今後、具体的な設計判断(例: あるプロジェクトが新しい機能を作る際にこのモデルを参照する)が
出てきたときに、改めて参照・発展させる。

### Resume prompt(更新)

D8は議論の記録として一区切り。次は残る2テーマ(ベクトルタイルサイズ最適化、
terrain/hillshadeの扱い)に着手するか、hfuさんの新しい指示を待つ。

---

## D9: ベクトルタイルのサイズ最適化(横断ヒアリング完了)

**Status**: Accepted (2026-09-02)

### 背景

hfuさんが同時に提起した3テーマ(ベクトルタイルサイズ最適化、スタイルデザインのterrain/
hillshade扱い、staccato-spec一般化拡張)のうち、D8(staccato)に続いて着手。

### 決定

kitavolca(詳細な実測データ)→mapterhorn-japan-bridge・height-coverage・stars-fd(消費側・
配信側の視点)という順で展開し、`patterns/vector-tile-sizing.md`に8パターンとして集約:

1. ジオメトリ簡略化・属性間引きより先に、feature単位のminzoomシフトを試す
2. タイルサイズは圧縮後ではなく非圧縮バイト数で判定する
3. 自動間引き(`--drop-densest-as-needed`等)は制御不能なデータ欠損リスクがある
4. ビルドログの「warning 0件」は最終成果物の適合性を保証しない
5. PMTilesはタイル内容の重複を自動的にハッシュベースで排除する
6. 「データセット全体のサイズ」と「1タイルあたりのペイロード」を分けて評価する
7. 圧縮・簡略化の限界を超えたら、自前ホストを諦めてリモートプロキシに切り替える

kitavolcaの「`--drop-densest-as-needed`を二段階の失敗の末に撤回した」という具体的な
失敗談(圧縮後バイト数での誤認→データ欠損の発見)が特に価値が高かった。生成側
(kitavolca、mapterhorn-japan-bridge)と消費・配信側(height-coverage、stars-fd)の両方の
視点が揃ったことで、「タイル生成時のminzoom」と「style.json表示制御のminzoom」の混同、
「データセット全体」と「1タイルのペイロード」の混同、という2つの重要な区別が明確になった。

### 保留事項

- zukaku・vientiane-planning-map・kaga0・plateau-mago-implicit・sas0・claude-mctへは
  展開していない(タイル生成・配信に直接関わらないプロジェクトが多いため、優先度低)

### Resume prompt

このタスクは一区切り。残るテーマは「スタイルデザイン、特にレイヤの上下関係・terrain・
hillshadeの扱い」。`patterns/maplibre-gl-js.md`に既にzukakuのterrain無効化パターンが
あるので、そこからの発展を検討する。

---

## D10: 溜まった判断事項の棚卸し(Planモードでのレビュー)

**Status**: Accepted (2026-09-03)

### 背景

hfuさんの提案で、D1〜D9で溜まった「cafebabeの裁量に一任された事項」「保留のまま未解決の
事項」を一箇所に整理し、Planモード(`EnterPlanMode`/`ExitPlanMode`)を使ってまとめて
レビューを仰いだ。今後、判断事項が溜まるたびにこの型を定例化する(D1参照)。

### 決定

1. **D6サーベイ(claude-mct実施)8項目に「推奨」ステータスを付与**——実行する
   (`patterns/maplibre-gl-js.md`・`patterns/markdown-file-conventions.md`に反映)
2. **HANDOVER.md肥大化対策としてのCHANGELOG.md**——結論を急がず、過去3回の書き直しで
   実際に本文から落ちた情報がDECISIONS.mdでカバーされているかを検証してから判断する
   (hfuさんの指摘: 定期書き直しの「退避先」という役割で位置づけ直せば、DECISIONS.md・
   HANDOVER.mdと直交しうる)
3. **タグ体系への「dwg7固有」中間区分の追加**——見送り。実例が複数出るまで待つ
4. **`patterns/`のサブディレクトリ化**——今回は着手せず先送り。ただし`open-mct.md`
   (3プロジェクトが参照)は次回優先候補
5. **既存パターンの「独立収束 vs 指令」誤読チェック(D4保留)**——`maplibre-gl-js.md`から
   着手する(D6反映と同時に実施)
6. **「個別事情」タグと「patterns/に置かない」の境界線明文化(D3保留)**——見送り。実例が
   3件以上蓄積してから`CONTRIBUTING.md`に基準を追記する
7. **D7残りプロジェクトへのスタイル設計ヒアリング**——しない(D9と同じ理由)
8. **残りテーマ「terrain・hillshadeの扱い」**——着手する。
   mapterhorn-japan-bridge/kitavolca/kaga0への横断ヒアリングを開始する
9. **Planモードでの棚卸しレビューを定例化**——DECISIONS.mdの保留事項が3〜5件溜まるか、
   大きな横断タスク完了ごとに実施
10. **hfuさん未レビューの.mdファイルの洗い出し**——新規プロセスとして追加。数件ずつ
    棚卸しのたびに提示する
11. **GitHub issue vs cross-session messageの使い分け**——厳密なラインを引かず、運用
    しながら柔軟に確立する

### 保留事項

- 上記2(CHANGELOG.md)は次のセッションで検証作業を行い、別ADRとして結論を記録する
- 上記4(`open-mct.md`の分割)は次回の棚卸しで優先着手する

### Resume prompt

D6サーベイ反映(`maplibre-gl-js.md`・`markdown-file-conventions.md`)→CHANGELOG.md検証→
未レビューファイルの洗い出し→terrain/hillshadeヒアリング開始、の順で進める。

---

## D11: HANDOVER.md肥大化対策 — CHANGELOG.mdは新設しない(D10 B1の検証結果)

**Status**: Accepted (2026-09-03)

### 背景

D10 B1で保留した「CHANGELOG.mdをHANDOVER.md定期書き直しの退避先として位置づけるべきか」を
検証した。過去3回の全面書き直し(コミット`ea05720`=D2完了時、`4f1d6f8`=D5完了時、
`955aca3`=D7/D8完了時)の差分を実際に比較した。

### 決定

- **1・2回目の書き直しでは、実質的な情報喪失はほぼ無かった。** 削除された旧記述(「初回
  起動時にやること」等)は、実行済みタスクの一時的な指示であり、DECISIONS.mdの該当ADR
  (D1〜D5)に経緯として既に残っている
- **3回目の書き直しでは、「横断ヒアリングの進め方」に関する運用ノウハウ**(9者同時に聞くと
  収束点と分岐点が見えやすい、実例URLを添えると実地の回答が返る、自由回答vs特定テーマ提示の
  使い分け等)**が、圧縮されて薄れかけていた。** これはDECISIONS.mdのD5/D6本文にも完全な
  形では残っておらず、実質的に失われかけていた唯一の実例
- ただし根本原因は「CHANGELOG.mdという退避先が無かったこと」ではなく、**その教訓自体を
  恒久的な場所(CLAUDE.md)に定着させないまま、HANDOVER.mdという「今のスナップショット」
  だけに書いていたこと**だった。退避先を追加するより、定着させるタイミングを早める方が
  直接的な解決になる
- **結論: CHANGELOG.mdは新設しない。** 代わりに、`CLAUDE.md`に「横断ヒアリングの作法」節を
  新設して失われかけていた教訓を定着させ、「HANDOVER.md書き直し前に恒久的価値のある情報を
  先に定着させる」というチェック項目を「日常的な作業」に追加した

### 保留事項

なし。このADRはクローズとする。

### Resume prompt

次にHANDOVER.mdを書き直す際は、`CLAUDE.md`の新チェック項目(恒久的価値のある情報を先に
定着させる)に従うこと。

---

## D12: エージェントへの呼称習慣とエージェンシーの経済学

**Status**: Accepted (2026-09-04)

### 背景

hfuさんから、「GitHubリポジトリを担当するエージェントを『XXXさん』(例: starsさん、
cafebabeさん)と呼ぶ習慣は、パターンとして記録する価値があるか」という問いが提起された。
「関係エージェントに時間差をつけて確認し、問題なければcafebabeとして記録すること」と、
「時間差付き呼び出しの練習」も兼ねる指示があった。

これとは別に、D10完了後の対話の中で、hfuさんから「エージェント組織におけるエージェンシー
(主体性)の希少性」についての一連の洞察(スーパーエージェント、クレジット→エージェンシー→
計算量の変換連鎖)が語られ、これも記録する価値があると判断した。

### 決定

**呼称習慣について**: stars-fd→mapterhorn-japan-bridge→height-coverageの順に時間差を
つけてヒアリングし、`patterns/agent-personification.md`として3パターンに集約した:
1. 「XXXさん」呼びは、セッションではなくリポジトリという役職への三人称的参照
   (hfuさん自身の観察: 「starsさんと相談して」のように他エージェントへの指示の中で使われる。
   直接呼びかける二人称としてはあまり使われない)
2. 呼称が指す「継続性」の性質は、プロジェクトの運用形態によって「制度的」(stars、
   `CONTRIBUTING.md`のような明文化された手続きを持つ)か「物語的」(height-coverage、
   まだ世代交代を経ておらず日記・回顧録に近い)かに分かれる
3. (個別事情)1つの呼称が、複数リポジトリへの職掌の分業実装を指すことがある
   (mapterhorn-japan-bridge: 「兼務」ではなく「1つの職掌が3つのツールに分業実装されている」)

**エージェンシーの経済学について**: `DWG7-CONTEXT.md`に新セクションとして記録した。
エージェント組織における最も希少なリソースはエージェンシーの発揮そのものであり、
クレジット(計算資源)はエージェンシーによって初めて生産に変換される、という洞察。
cafebabe自身は「hfuさんのエージェンシーを代替するのではなく増幅する装置」として
位置づけ直した。

### 保留事項

なし。

### Resume prompt

`patterns/agent-personification.md`は3人からの回答をもとに確定。今後、新しいプロジェクトの
参加時にも、この呼称習慣(役職としての三人称参照)を意識して名指しするとよい。
`DWG7-CONTEXT.md`のエージェンシー経済学セクションは、今後cafebabeの設計判断(棚卸し・
優先順位付け・先送りの明示化)の根拠として参照すること。

---

## D13: `patterns/maplibre-gl-js.md`のテーマ別4分割、terrain/hillshade横断ヒアリング完了(C1・C5)

**Status**: Accepted (2026-09-04)

### 背景

D10 C1では「`open-mct.md`(当時300行超)を次回棚卸しで優先分割」としたが、その後の整理で
`open-mct.md`は139行まで縮み閾値を下回った。一方`patterns/maplibre-gl-js.md`はD6反映・
terrain/hillshade追加(D9〜D12の過程)で425行・21パターンまで増え、`CLAUDE.md`の
「1ファイル300行」閾値を超えていた。hfuさんに状況を報告し、C1の優先対象をこちらに切り替えて
今すぐ着手するか確認したところ、承認を得た。

同時に、D10 C5で計画していたterrain/hillshadeの横断ヒアリング(mapterhorn-japan-bridgeへの
深掘りから、kitavolca・kaga0への展開)も実施した。

### 決定

**分割**: `patterns/maplibre-gl-js.md`を以下4ファイルに分割し、旧ファイルは削除した:
- `patterns/maplibre-gl-js-rendering.md`(バージョン選定、globe+fill-extrusion、
  zoomLevelsToOverscale、terrain/hillshade、ラベル装飾、GetLegendGraphic)
- `patterns/maplibre-gl-js-data-serving.md`(ランタイムハイドレーション、CORS、attribution、
  tileSize、PMTiles+Martin)
- `patterns/maplibre-gl-js-output-testing.md`(ヘッドレスレンダリング、印刷とPlaywrightの
  コードパス差、非表示ペイン0x0問題、fitBoundsズームレベルシフト)
- `patterns/maplibre-gl-js-embedding.md`(折りたたみパネル、ホバーパネル、hash名前空間化、
  UIトグルの状態同期、`map.remove()`、iframe vs ネイティブ)

旧ファイルを参照していた`README.md`・`patterns/style-composition.md`(2箇所)・
`patterns/agent-execution-gotchas.md`(2箇所)のリンクを新ファイルへ更新した。DECISIONS.mdの
過去エントリ(D6・D9・D10・D11)内の`maplibre-gl-js.md`表記は、決定ログの追記専用原則
(訂正は追記、書き換えはしない)に従い**そのまま残す**——当時はまだ分割前だったので、当時の
記述として正しい。

**terrain/hillshadeヒアリング(C5)**: mapterhorn-japan-bridge・kitavolca・kaga0の3プロジェクト
から回答を得て、`maplibre-gl-js-rendering.md`の1パターンに統合した。3者の判断が
「terrainを封印しhillshadeのみ」(mapterhorn-japan-bridge)・「terrain+hillshade併用、
データ規模が小さく問題未発生」(kitavolca)・「両方とも意図的に未実装、パフォーマンス制約が
理由でhillshadeをterrainより先にロードマップへ」(kaga0)と3方向に分かれる独立分岐だった。
「新しいか」ではなく「データ規模・ハードウェア制約に応じた合理的判断か」という軸で3例とも
対等に記録し、どれか1つを標準として扱わなかった(`CLAUDE.md`の「keep open」原則・
「標準化は独立収束か指令かを区別する」原則に従う)。kitavolcaからは副産物として
「UIトグルの初期状態をHTML属性で決め打ちせず、map状態変化イベントで同期する」という
再利用可能なUIパターンも得られ、`maplibre-gl-js-embedding.md`に追加した。

### 保留事項

なし。C1・C5とも今回でクローズ。

### Resume prompt

`patterns/maplibre-gl-js-*.md`の4分割は完了。他のパターンファイルが今後300行に近づいた場合も
同じ要領(テーマで自然に割れる単位を見極め、README.md・相互参照リンクを一括更新)で対応する。
D10 C1で優先候補だった`open-mct.md`は今回の時点では閾値以下のため見送り。

---

## D14: 判断待ち事項の捌き方を「小分け・定期」に更新、`.claude/rules/`symlink共有をzukakuで小規模試行

**Status**: Accepted (2026-09-05)

### 背景

claude-mct経由でhfuさんから、著名ユーザーのClaude Code運用(1つの巨大ルート+AGENTS.md
階層発見)についての相談が転送され、cafebabeとして意見を返した(AGENTS.md階層化はhfuさんの
「多数の独立フリートセッション」モデルには限定的な価値、symlinkでのディレクトリ階層化は
低リスクだが今のところ実際の痛みが証拠不足、という趣旨)。

その過程でhfuさんから明示的に「これはclaude-mctではなくcafebabeさんとhfuさんで直接やって
いく話」として、**cafebabeに溜まった知見の整理・棚卸しを、hfuさんが気持ちよく行える方法**の
設計を依頼された。D10(Planモード一括棚卸し)は効果があったが、まとまった時間が要る形式
だった。あわせてclaude-25から、`.claude/rules/`ディレクトリがsymlink共有を公式サポートして
いる(`ln -s ~/shared-rules .claude/rules/shared`)という技術情報が共有された。

### 決定

**棚卸しの捌き方**: 2つの選択肢(①都度1件ずつ会話の流れで確認 / ②小分け(2〜3件)で定期的に
/ ③非同期ダイジェスト+Artifactコメント)をhfuさんに提示し、②を選択。運用は以下:

- D10 D1で決めた「保留事項が3〜5件溜まったら、または大きな横断タスク完了ごとにPlanモード
  棚卸し」という大掛かりな形式は、**5件を超える、または複数テーマにまたがる場合に限定**する
- それ未満(2〜3件)の判断待ち事項が溜まったら、Planモードを起こさず、**通常の会話の中で
  まとめて提示し、AskUserQuestionまたは簡単な確認で捌く**(2026-09-05のmaplibre-gl-js.md
  分割+D1'優先ファイル提示を1ターンにまとめた進め方が実例)
- 1件だけ即座に判断が必要な場合(その場で発生した局所的な分岐)は、従来通りその場で確認して
  よい——バッチ化を待って先延ばしにしない

**`.claude/rules/`symlink共有**: 小規模試行することで合意。`zukaku`を試行対象に選定した
(`patterns/maplibre-gl-js-rendering.md`・`patterns/maplibre-gl-js-output-testing.md`・
`patterns/maplibre-gl-js-embedding.md`・`patterns/ci-cd-pitfalls.md`・
`patterns/markdown-file-conventions.md`と、参照密度が最も高いため)。実装(実際の`ln -s`)は
cafebabeが他リポジトリに直接手を入れるのではなく、**zukaku自身のセッションに提案し、
採否・対象ファイルの選定はzukaku側の裁量に委ねる**(`CLAUDE.md`の「プロジェクト固有の
バグ修正やコードは書かない」原則、および`DWG7-CONTEXT.md`の「個人単位の多中心的協調」に
従う)。効果が見えたら他プロジェクトへの展開を検討する。

### 保留事項

- `.claude/rules/`試行の結果(効果があったか、pull型からpush型への移行が実際に知見の
  鮮度・的中率にどう影響するか)は、zukakuからのフィードバック待ち
- 棚卸しの「定期的」の具体的トリガー(カレンダー的な間隔なのか、2〜3件という件数トリガー
  なのか)は、件数トリガーを基本としつつ運用しながら調整する

### Resume prompt

今後、判断待ち事項が発生したら都度メモしておき、2〜3件溜まった時点(または1件でも即時性が
高い場合はその場)で会話内にまとめて提示する。5件を超えたり複数テーマにまたがる場合のみ
Planモード棚卸しを起こす。zukakuからの`.claude/rules/`試行フィードバックが届いたら、
このADRへの追記として結果を記録する。
