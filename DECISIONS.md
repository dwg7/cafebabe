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
