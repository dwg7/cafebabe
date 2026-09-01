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
指示があった(2026-09-02)。まだ議論は始まったばかりだが、検討の出発点として:

- `DWG7-CONTEXT.md`は既にcafebabe自身を「取次役」(現場の粒を構造化された成果物に渡す前に
  粒立てる役割)と位置づけている。これは`Staff`(意味解釈を所有)に近いとも読めるし、
  `Library`(知見の発見可能性を担保する)に近いとも読める——cafebabe自身がどちらの性質を
  強く持つかは、今後の一般化拡張の議論で扱う論点
- `stars-fd`は既にLibrary的役割を地図データについて担っている。この「Library」という
  自己認識を明示的に持ってもらうことが、hfuさんから重要だと指摘されている
