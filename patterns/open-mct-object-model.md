# Open MCT — オブジェクトモデルの設計(拡張点・type・DAG・Provider構造・addRoot)

`patterns/open-mct.md`の一部として運用。全体像・寄稿プロジェクトの一覧はそちらを参照。

## 唯一、一貫して信頼できる拡張ポイント

3プロジェクトとも同じ結論に達している：**`openmct.objects.addProvider()` + `openmct.composition.addProvider()`** の組み合わせが、GUIでの`+Create`を経ずに安定したツリー構造を構築する唯一の方法。これに加えて、

- カスタムビューが必要なら `openmct.objectViews.addProvider()`（sas0/mapterhorn-monitor）
- カスタムテレメトリ表示が必要なら `openmct.telemetry.addProvider()`（claude-mct）

を組み合わせる。独自`namespace`を作り、`get(identifier)`でオブジェクトを返し、`composition.addProvider`で親子関係を返す——この三点セットだけで、コードで完全に定義された安定したアプリが作れる。

基本プラグイン（`LocalStorage`・`UTCTimeSystem`・`Espresso`テーマ）のインストール、`openmct.types.addType()`によるカスタムタイプ登録は、3プロジェクトとも問題なく動作。

## カスタムtype登録（`openmct.types.addType()`）の使われ方

2026-09-06、hfuさん自身のOpen MCT学習に伴うヒアリングより。「組み込みtypeだけで運用しているか」という問いに対し、sas0・claude-mct・m3xx-fleet（m3xx-fleet-ops）の3プロジェクトとも**自分でtypeを登録していた**——「型そのものが要らない」という運用は今のところ見られない。

- **sas0**：`sas0.instrument`という単一のカスタムtype（`creatable: false`、全計器で共用）のみ。フォルダは組み込み`folder`のまま。telemetry/plot系typeは未登録——地震マグニチュード推移をOpen MCT純正Plotビューで表示しようとして`patterns/open-mct-telemetry.md`の壁にぶつかり、`registerInstrument`経由の素のSVGチャートに切り替えた経緯がある。
- **claude-mct**：4種類（`claude-session`、`claude-session-comm`、`fleet-summary`、`fleet-andon`）、すべて`creatable: false`（providerが返す非永続オブジェクト用）。型ごとにTable・Plot・独自ビュー（`objectViews.addProvider`）を使い分けている。
- **m3xx-fleet**：2種類（`fleet.host`、`fleet.root`）。**動機が明確**——ルートに組み込み`folder`typeを使うと、既定のGrid Viewがビュー切り替えメニューに競合して残ってしまい、「クリックすれば常に自作のアンドンボードが出る」という体験を作れなかった。ルートを独自typeにし、そのtypeにだけ`canView`するカスタムビューを紐付けることで、ビュー切り替えの選択肢を実質1つに絞った。

**共通する動機**：3プロジェクトとも、カスタムtypeを「分類ラベル」としてではなく、**「その型にだけカスタムビューを紐付けて、ユーザーに見せるビュー切り替えの選択肢を絞り込む」**という制御目的で使っている。組み込み`folder`typeで運用する場合、既定のビュー（Grid View等）がビュー切り替えメニューに残ってしまう点に注意。

## ツリーはDAGか — 実務では単一親ツリーに落ち着く

2026-09-06のヒアリングより。「同じテレメトリ点/オブジェクトを複数フォルダにリンクする」という、Open MCTのオブジェクトモデルが理論上許すDAG構造を、実務で使っている実例はまだ確認できていない（sas0・claude-mct・m3xx-fleet・mapterhorn-monitorの4プロジェクトとも未使用）。

- **sas0**：意識も利用もしていない。`registerInstrument`/`registerFolder`が単一`parentKey`しか受け取らない設計。「計器が2つ以上ある時だけフォルダを作る」という単純な木構造の運用方針そのものが、多親リンクの動機を生じさせていない。
- **m3xx-fleet**：使っていない。15台規模のフラットな1階層ツリーで「一望性」の要件が満たせてしまい、「状態別」「役割別」のように同じホストを複数の切り口で見せたいという要求自体が発生しなかった。
- **claude-mct**：**意図的に避けた実例。** 活動ログ配下と交信ログ配下の両方から同じ`sessionId`を子として参照しようとしたが、composition providerの`get(identifier)`は`{namespace, key}`だけで呼ばれ「どの親からたどってきたか」を持たないため、`claude-session`型と`claude-session-comm`型のどちらを指すか区別できず衝突した。結局`${sessionId}::comm`という別名前空間のキーに分けて回避した——DAG的リンクを試みて、provider実装上の制約（親情報を持てない）にぶつかった実例。Open MCT自体の一般的な制約かは未確認。
- **mapterhorn-monitor**：**構造上は対応可能だが未使用という3つ目の立ち位置。** `composition.addProvider`の実装が`Map<parentKey, [{identifier, order}]>`という素直な隣接リストのため、同じidentifierを複数の`parentKey`へ`pushChild`すれば多親構成自体は作れる。しかし実際のコードは6計器とも`parentKey: 'root'`のみで、フラットな一階層ツリーとしてしか使っていない——「構造的には対応可能／意識的な利用実績はゼロ」という、sas0（そもそも動機が無い設計）・claude-mct（試みて構造的制約にぶつかった）のどちらとも違う中間の立ち位置。

**現時点の結論**：DAG構造はOpen MCTのオブジェクトモデルが理論上サポートする機能で、実装（`composition.addProvider`の隣接リスト）としても対応できる場合がある。それでも4プロジェクトの実地では**需要が発生しないか、発生しても`get(identifier)`が親情報を持たないというprovider実装上の制約で回避されている**——「使える／使いたい」以前に「使う理由に達した実例がまだ無い」状態に近い。「複数の切り口で同じオブジェクトを見せたい」規模・要件に達したら、claude-mctの衝突例を踏まえて設計する必要がある。

## Object Providerの構造 — 「1 namespace = 1 provider」は共通、内部が「多役」かは割れる

2026-09-06のヒアリングより。4プロジェクトとも namespace とprovider登録は1対1（1つのnamespaceに対し`openmct.objects.addProvider()`を1回だけ呼ぶ）で共通していたが、その`get(identifier)`内部が**単一の型しか返さないか、`identifier.key`で分岐して複数の型を返す「多役」構造か**は、ちょうど2対2に分かれた。

- **単一役（型分岐なし）**：
  - sas0 — `objectsByKey`という1つのMapを`identifier.key`で引くだけ。型による分岐が無く、フォルダも計器も同じMapに平置き。
  - mapterhorn-monitor — 同じく`objectsByKey.get(identifier.key)`のフラットなMap引きのみ。sas0と同型の最小構成。
  - stars — 2026-09-07、cafebabeの設計助言に沿って新規実装。単一のカスタムtype`stars.instrument`を7計器で共有し、単一役のMap構成を採用。本番（GitHub Pages）まで問題なく反映（下記注記参照）。
- **多役（`identifier.key`で型を判別して分岐）**：
  - claude-mct — `get(identifier)`内部で、`identifier.key`がどのルートキー（活動ログ/稼働状況/交信ログ/フリートサマリ）か、あるいはセッションID（素かサフィックス`::comm`付きか）かで分岐し、4type分のオブジェクトをすべて1つのproviderから返す。
  - m3xx-fleet — `identifier.key === ROOT_KEY`かどうかで`fleet.root`/`fleet.host`の2typeを分岐。typeはnamespace/provider自体には現れず、分岐後に組み立てるdomainObjectのフィールドに過ぎない、という整理。

**stars実例についての注記**：starsのケースは「独立に同じ結論に到達した」のではなく、cafebabeがこのヒアリング結果に基づいて設計助言を行い、それに沿って実装した結果が確認できた、という順序（助言→実装→検証）である。複数プロジェクトが独立収束したsas0/mapterhorn-monitorの2例とは証拠としての重みが異なる点に注意——ただし「7計器程度の規模なら単一役構成で問題なく動く」という点自体は、本番での実地確認として十分な価値がある。

**傾向**：type数が1つ（sas0・mapterhorn-monitor）のプロジェクトは分岐が発生しようがなく自然に単一役になっているのに対し、type数が複数（claude-mct・m3xx-fleet）のプロジェクトは「1 namespace = 1 provider」の制約の中でkey分岐によって多役化している。type数がさらに増えた場合、この分岐ロジックが肥大化しやすい点は、将来の棚卸し対象として意識しておく価値がある。

## ルート登録（`addRoot`）— 4プロジェクトとも固定識別子版、関数/Promise版は未使用

2026-09-06のヒアリングより。`openmct.objects.addRoot()`には固定の識別子オブジェクトを渡す形と、関数（Promise）を渡して起動時に外部から動的に解決させる形があるが、4プロジェクトとも**前者（固定識別子）のみ**を使っていた。関数/Promise版の実例はまだ無い。

- sas0・mapterhorn-monitor・m3xx-fleet・stars：単一のルート（`{ namespace, key: 'root' }`相当）を1回`addRoot`するだけ。理由はいずれも「起動時にオブジェクト構成が決め打ちで、動的に変わるのは中身のデータだけ」という共通の設計。
- claude-mct：4つのルートキー（活動ログ/稼働状況/交信ログ/フリートサマリ）をそれぞれ別々に`addRoot`し、第2引数の優先度（`-1`〜`-4`）でツリー内の並び順を明示的に制御している——単一ルートの3プロジェクトには無い工夫。

**現時点の結論**：関数/Promise版が必要になるのは「起動時点ではルートの数や識別子が決まっておらず、外部（APIやファイル走査等）から動的に取得しないと分からない」場合のはずだが、4プロジェクトとも「ルート自体は静的、中身のデータだけが動的」という設計に収まっているため、まだ実例が無い。今後、ルート自体を動的に増減させたいプロジェクトが出てきたら、ここが最初の実地検証になる。
