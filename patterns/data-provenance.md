# データ出自調査(Data Provenance Research)

プロジェクトが依拠する外部データ・基盤・略語の来歴を検証する営みについて。
[`patterns/case-study-research.md`](case-study-research.md)(先行事例研究)と調査ツール
キットは共通するが、目的の方向が逆——「外を見て、自分の設計に借用できるものを探す」のでは
なく「内(自分が既に依拠しているデータソース)を見て、その来歴・正当性を検証する」——のため
別ファイルとして分離。
2026-09-02、vientiane-planning-mapからの提供より。

2026-09-24、内容量が閾値(300行)を超えたため2ファイルに分割した:

- [`patterns/data-provenance-source-verification.md`](data-provenance-source-verification.md) —
  外部ソースの正当性・鮮度を検証する(来歴調査、成果物への来歴埋め込み、上流データの
  チェックサム固定、気象庁bosaiの静的化とJSON配列走査、CSVダウンロード機能の裏側)
- [`patterns/data-provenance-wrangling.md`](data-provenance-wrangling.md) —
  整形・集計の実務(北海道市町村コードの罠、行政・領土的地位への言及、xlsx直接パース、
  複数値カラムの扱い、旧市町村名の管理、GeoParquetの実装知見)
