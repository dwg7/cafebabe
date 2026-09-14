# 空撮写真測量(SfM/ODM)の実地知見

一眼レフ等の非計測カメラによる空撮データを、OpenDroneMap(ODM)のようなSfMパイプラインに
かける際の、実データ調査で確定した落とし穴について。dwg7初のOpenDroneMap実例。
2026-09-11〜14、tokachi20260911(十勝岳ヘリ同乗取材データ)より。

3つのテーマファイルに分割している(2026-09-14、内容量が閾値を超えたため):

- [`patterns/aerial-photogrammetry-capture.md`](aerial-photogrammetry-capture.md) —
  撮影・再構成の成立条件(GPS量子化、ズームレンズのカメラ群自動分割、交差パスのバンドル
  調整、間引きによる精度劣化、ヘイズと基線の上限)
- [`patterns/aerial-photogrammetry-screening.md`](aerial-photogrammetry-screening.md) —
  事前スクリーニング(ファイルサイズと鮮鋭度の無相関、ラプラシアン分散のボケ/ヘイズ混同、
  JPEG DRIの部分デコード)
- [`patterns/aerial-photogrammetry-pipeline.md`](aerial-photogrammetry-pipeline.md) —
  処理環境・配信・応用(Apple SiliconでのDocker版ODM、OOMの真因、PMTiles配信、starsの
  キャッシュ、二時期オルソの共登録可能性の見積もり)

## 由来

2026-09-11、十勝岳(噴火警戒レベル2)ヘリ同乗取材データをOpenDroneMapで処理する
`tokachi20260911`プロジェクトが、dwg7として初めてOpenDroneMap(SfM写真測量)を扱う
実例となった。開始時点ではcafebabeにODM固有の蓄積は無く(正直にその旨を回答)、以後の
実地調査から得られた知見を継続的にここへ集約している。焦点距離混在によるカメラ校正の
サイレントな破綻(`aerial-photogrammetry-capture.md`)は、当初の対策案(手動分割)を
実測に基づき訂正した経緯を含む——最初の仮説が実地検証で覆るプロセスそのものも記録として
残している。
