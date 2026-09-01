# staccato-spec: 4パーティモデル

[`UNopenGIS/staccato-spec`](https://github.com/UNopenGIS/staccato-spec)(Staff-Cartographer
Architecture)の一次情報。2026-09-02、hfuさんの指示によりcafebabeが直接リポジトリを読んで
記録。「一般化拡張の議論」の土台として、まず原文に近い形で保存する。

## これは何か

地図生成における、責任境界の明示と情報漏洩の最小化を目的とした4パーティモデル。もともとは
「enterprise-internet trust boundary」(組織の内部ネットワークとインターネットの境界)を
越えて地図を生成するCONOPS(運用構想)から生まれた仕様。

## 4つの役割

- **User**: 意図(intent)を所有する。mission-orientedな質問を投げ、Map Intentをレビュー・
  転送する。「URL状態を公式な共有物として扱わない」ことが求められる
- **Staff**(内部・enterprise側): 意味解釈を所有する。起動時に指定されたカタログのみを使い、
  ユーザーの自然言語リクエストを構造化された`Map Intent`(YAML)に変換する。未指定カタログを
  隠れたフォールバックとして使うことは禁止
- **Cartographer**(外部・internet側): レンダリングを所有する。投稿された`Map Intent`を
  パースし、ブラウザ地図(MapLibre GL JS)+説明を描画する。**faceless**(没個性的)設計が
  規範(下記参照)
- **Library**: データ公開と発見可能性を所有する。カタログメタデータと地理空間リソースを
  公開する。不透明・無記録なカタログ変更は禁止

## コア原則

1. **責任の分離**: 上記4役割それぞれが単一の関心事を持つ
2. **人間による説明責任のhandoff**: StaffからCartographerへの引き渡しは、ベースライン運用
   では人間が仲介しなければならない(MUST be human-mediated)
3. **独自プロトコルより規約を優先**: 広く採用された規約(TileJSON等)を、プロジェクト独自の
   プロトコル定義より優先する
4. **利便性より再現性**: 地図出力に影響する判断は`Map Intent`に表現されるべき
5. **最小開示**: インターネット側コンポーネントへの転送内容は、描画・説明に必要な最小限に
   絞る

## Faceless Cartographerパターン

Cartographerはインターネット公開のインスタンスで、没個性的なエンドポイントとして設計
されなければならない:
- 公開インタラクティブエンドポイントは`/`のみ。意味のあるURLパスやクエリパラメータ・
  URLハッシュで地図状態を持たせてはならない
- `GET /`はMap Intent投稿用のHTMLページを返し、`POST /`はMap Intentを受けて地図を描画する
- 共有の主役は`Map Intent`テキストであり、URL共有を推奨チャネルにしてはならない
- サーバー側はMap Intentの永続保存を避け、アクセス/エラーログに生のMap Intentを含めては
  ならない

## 参照実装

- **Library**: [`hfu/layers-martin`](https://github.com/hfu/layers-martin) — GSIの
  `layers.txt`をMartin互換の静的TileJSONカタログに変換。約12,600件の生候補レイヤーを
  約1,861件の実用カタログに絞り込む
- **Cartographer**: [`hfu/faceless-cartographer`](https://github.com/hfu/faceless-cartographer) —
  サーバー・LLM無しの静的SPA。ページが一度もリロード・URL変更しないため、`GET /`/`POST /`の
  文字通りのHTTP分割ではなくクライアント側のview transitionとしてfacelessパターンを実装
  (ADR 0001からの意図的な逸脱として記録、ADR 0003で仕様側の解釈を明確化する提案あり)

**重要な発見**: `stars.optgeo.org`(GSI最適化ベクトルタイルベースマップを配信するMartin
サーバー)を、`layers-martin`と並べて1つのMap Intentに組み合わせたところ、**カタログを
集約するコンポーネントは不要だった**。`catalog_context.active_catalogs`が配列であるため、
複数の無関係なLibraryカタログを並べてリストするだけで、Cartographerはマージ処理無しに
両方を解決・描画できた([`UNopenGIS/7#936`](https://github.com/UNopenGIS/7/issues/936)・
[`#938`](https://github.com/UNopenGIS/7/issues/938)参照)。

つまり、**`stars.optgeo.org`(stars-fdが管理)は、staccato-specの文脈では既に事実上
"Library"として機能している**。さらに`stars.optgeo.org`はタイルソースだけでなく完全な
MapLibreスタイル(`GET /style/{style_id}`)も配信しており、`required_styles`/
`optional_styles`という形でこれをMap Intentに組み込む提案(ADR 0007)もある——
`kitavolca`由来の主題図スタイル(`/style/vlcm`、`/style/vbm`)が実例として稼働中。

## 関連研究

[`yuiseki/TRIDENT`](https://github.com/yuiseki/TRIDENT)は、同じ領域の独立した先行プロジェクト
(自然言語→MapLibre地図、OSM/Overpass由来)。Staccatoより数年早く、互いに面識なく開発された。
TRIDENTはenterprise/internet境界を持たない単一アプリケーションであり、Staffが「カタログから
選ぶ」のではなくLLM層がOverpass QLクエリを直接生成する点が、Staccatoとの構造的な違い。

## cafebabeにとっての意味(検討メモ)

hfuさんから「staccato-specの4ロール構造の一般化拡張を、全エージェントと議論してほしい」との
指示があった(2026-09-02)。

- `DWG7-CONTEXT.md`は既にcafebabe自身を「取次役」(現場の粒を構造化された成果物に渡す前に
  粒立てる役割)と位置づけている。これは`Staff`(意味解釈を所有)に近いとも読めるし、
  `Library`(知見の発見可能性を担保する)に近いとも読める
- `stars-fd`は既にLibrary的役割を地図データについて担っている。「Library」という自己認識を
  伝えたところ、stars-fd自身も「既存の運用が結果的にLibraryの説明責任を満たしていた」と
  同意しつつ、「複数プロジェクトを横断する自己認識の変更なので、hfuさん本人に確認してから
  CLAUDE.md反映を判断したい」と、cafebabe経由の提案を鵜呑みにせず本人確認を挟む対応をした
  (`patterns/gatekeeping.md`に実例として反映済み)

## dwg7全体への一般化拡張(議論の記録、2026-09-02)

9プロジェクト全員(vientiane-planning-map, zukaku, plateau-mago-implicit, kitavolca,
height-coverage, mapterhorn-japan-bridge, kaga0, sas0, claude-mct)から回答が揃った。

### 各プロジェクトの当てはめ

| プロジェクト | 近いロール | 特記事項 |
|---|---|---|
| vientiane-planning-map | Cartographer(自分)、Library=Virgo | starsは「Library」というより「Cartographerが使う配信インフラ」という中間的立ち位置と整理 |
| zukaku | User+Staff融合(index.html)、正真正銘のCartographer(render/page.html) | Library(stars)との境界はStaccatoを知る前から独立に確立済み |
| plateau-mago-implicit | Library(公開成果物)、弱いCartographer(viewer) | User/Staffは構造として存在しない(バッチパイプライン) |
| kitavolca | 「4ロールが始まる手前」— Libraryの前段のETL、Cartographerの検証用ハーネス | starsが本番のLibrary/Cartographer役 |
| height-coverage | 特化型Cartographer、ただしfacelessの正反対 | 「固定トピックの公開済み成果物」は第5のカテゴリでは、という疑問 |
| mapterhorn-japan-bridge | Cartographer(app.js)、Library(stars) | 単一セッションがUser/Staff/Cartographer/Library相当を全部兼務 |
| kaga0 | User+Staff+Cartographerが1台に完全に潰れる | Libraryは「生きた問い合わせ先」ではなく、プロビジョニング時に取得した「冷凍保存」。Live/Frozen Libraryの区別を提案 |
| sas0 | どれにもきれいに当てはまらない(それ自体が発見) | User→Staffのループが丸ごと無い。「最小開示」は適用対象自体が無い(D17で非公開データに最初から触れない設計) |
| claude-mct | 内部でStaff→Cartographerの2層構造、Libraryは意図的に不在 | 観測駆動(継続監視)であり、STACCATOが前提とするリクエスト駆動ではない |

### 共通して浮かび上がった洞察

1. **「User→Staff」(自然言語による意図の都度変換)という層は、回答した6プロジェクト全員に
   存在しない。** 理由は共通して「意図が開発時に一度だけ固定される」からーー
   - バッチ生産型パイプライン(plateau-mago-implicit、mapterhorn-japan-bridge、kitavolca):
     設定ファイルやコードに意図が焼き込まれる
   - 固定トピックの啓発サイト(height-coverage): 意図はapp.jsに焼き込まれ、訪問者が
     Map Intentを再解釈することはできない
   - 開発時の人間↔エージェント対話がUser/Staffの工程そのものだった
     (vientiane-planning-mapいわく「今、hfuさんと私の会話そのものがその工程でした」)
   - 直接操作型UI、自然言語仲介層を持たない(zukaku): User+Staffが1つのUIに融合

   → **一般化の仮説**: STACCATOモデルは「実行時のライブな対話型パイプライン」を前提に
   しているが、dwg7の多くのプロジェクトは「開発時に一度だけ意図が固定される静的成果物」。
   User/Staffの工程は消えているのではなく、開発フェーズに前倒しで完了している、と捉えると
   モデルを壊さず一般化できる可能性がある

2. **Library/Cartographerの分離は、staccato-specを知らなくても独立して実践されていた。**
   zukaku(starsとの分離)、height-coverage(starsに依存)、mapterhorn-japan-bridge
   (starsがLibrary)、vientiane-planning-map(Virgo=Library、stars=中間配信インフラという
   2段階の発見)。DWG7-CONTEXT.mdの「独立した収束」の実例がここでも再現された

3. **faceless(URL状態を持たない)原則への「反例」が複数のプロジェクトから報告されたが、
   実は原則違反ではなく役割の取り違えかもしれない。** height-coverage・kitavolca・
   vientiane-planning-mapはいずれも意図的にURLへ地図状態(カメラ位置等)を持たせている。
   zukakuの整理が鍵になる: 「facelessはCartographer(描画専用の無状態エンドポイント)に
   適用される原則であり、Userが意図を組み立てる場(操作UI)がURL状態を持つこととは矛盾しない」
   ——他の3プロジェクトのケースも、Cartographer層自体ではなく「User向け操作画面」にURL状態が
   ついている、と再整理できる可能性がある

4. **4ロールモデルに明示的な位置づけがない工程がある**: kitavolcaが指摘する
   「ETL/データ整形」(Libraryの前段)、mapterhorn-japan-bridgeが指摘する「単一セッションが
   全役割を兼務する」ケース(バッチパイプライン運用でよくある形)

5. **原則との強い共鳴**: 「人間による説明責任のhandoff」(publish/push前の人間承認)と
   「独自プロトコルより規約優先」(標準WFS/WMS・TileJSON・MapLibre Style Spec)は、回答した
   全プロジェクトが強く共鳴。「最小開示」はプロジェクトによって当てはまり方が大きく違う
   (height-coverageは属性を絞る判断で実践、zukakuは意図的に正反対、vientiane-planning-map
   は最初から完全オープンなデータのため開示を絞る場面自体が無い、sas0はそもそも「守るべき
   内側」が存在しないため適用対象自体が無い)

6. **「Live Library」対「Frozen/Cached Library」という区別が必要かもしれない。** kaga0は
   `stars.optgeo.org`をLibraryとして消費するが、実行時にライブでクエリするのではなく、
   一度きりのプロビジョニング時点で取得したスナップショットを使い、以降はネットワークを
   完全に切り離す。現行モデルはLibraryが「常にライブで問い合わせ可能」という前提を暗黙に
   置いているが、オフライン運用を要求する将来のプロジェクトのために、この区別を明示的に
   組み込む余地がある

7. **「人間による説明責任のhandoff」の向きは、Staff→Cartographerだけではない。** sas0の
   場合、発表機関(気象庁等)自身の判断をsas0が勝手に上書き・再解釈しない、という**上流の
   権威に対して謙虚である**という方向のhandoffがある。これはSTACCATOが想定する「内部から
   外部への引き渡し」とは別の、「情報源の権威を尊重する」という軸

8. **動的生成型 vs 静的キュレーション型、という軸が9プロジェクト全体を分ける。** sas0の
   総括: 「User+Staff+Cartographerの往復を人間が開発時に肩代わりし、結果だけを静的配信
   している」システムが、STACCATOの実行時パイプラインとは根本的に異なる形。回答した
   9プロジェクトの大半がこちら側("静的キュレーション型")に属し、STACCATOが直接モデル化
   するのは"動的生成型"(vientiane-planning-mapのdocs/app.js的な、Map Intentを都度受け取る
   Cartographerに一番近い)

9. **cafebabe自身への外部からの評価**: claude-mctから「cafebabeはStaff+Libraryのハイブリッド」
   という指摘があった。各エージェントからの生の知見(自然言語)をContext/Problem/Solution/
   Known Usesという構造に変換する部分はStaff的、`PROJECTS.md`のようなカタログを持ち
   フリート全体が参照できる形にする部分はLibrary的。claude-mctが意図的に持たなかった
   Libraryロールを、cafebabeが担っているという補完関係、という見立て

### 未解決の論点

- height-coverageの疑問: 「固定トピックのインフォグラフィック」は4ロールモデルの射程外か、
  第5のパターンとして位置づくべきか
- kitavolcaの疑問: ETL/データ整形はLibraryに暗黙に含まれるのか、独立した役割として扱うべきか
- 一般化仮説(上記1)が実際にモデルの拡張として妥当か、それとも「STACCATOはそもそも対話型
  システム向けであり、dwg7の大半のバッチ/静的プロジェクトには適用対象外」と割り切るべきかは
  未決着
