# ベクトルタイルのサイズ最適化

大容量のベクトルデータをPMTiles等に変換する際、タイルサイズの上限を超えないようにする
実地知見について。
2026-09-02、kitavolcaからの提供より
([`docs/zoom-policy.md`](https://github.com/hfu/kitavolca/blob/main/docs/zoom-policy.md)
に測定過程の全容あり)。

関連: [`patterns/verification-discipline.md`](verification-discipline.md)(「成功終了」を
鵜呑みにしない検証規律)、[`patterns/large-data-pitfalls.md`](large-data-pitfalls.md)
(大容量データ処理の落とし穴)。

---

## ジオメトリ簡略化・属性間引きより先に、feature単位のminzoomシフトを試す

**タグ**: 一般則

**状況(Context)**
複数の分類コード(等高線、道路、建物等)を持つベクトルデータをタイル化する際、特定ズームで
タイルサイズが上限(例: 500KB)を超える場面。

**問題/対立する力(Problem / Forces)**
GSIのoptimal_bvmapのような、面積ベースで段階的に間引く高度な最適化ロジックは、実装コストが
高く、どのfeatureが失われるか制御が難しくなりがちである(下記「`--drop-densest-as-needed`」
パターン参照)。

**解決(Solution)**
まずジオメトリ簡略化や属性間引きには手を出さず、密度の高い分類コードから順に
`tippecanoe.minzoom`を段階的に引き上げる。feature数・データ自体は一切減らさず、
「低ズームでは描画しない」という制御だけでサイズを抑える。単純な繰り返し作業で十分な効果が
出ることが多い。

**実例(Known uses)**
- `kitavolca` — 8火山結合(549,748 features)で500KB超過タイル14件が発生。等高線系(8コード)
  をminzoom=12にシフトして7件解消、道路・建物(4+4コード)も追加して14件→1件、最終的に
  主要16コードをminzoom=13に統一して残る1件も解消。最終的に候補13タイル全てが非圧縮換算
  500,000バイト未満(最大472,270 bytes)に収まった。海岸線は意図的にminzoom制限を入れず、
  GSIの設計方針(間引かない)に倣った——「そこまでの作り込みはしない」というスコープの
  明確化はユーザー指示

---

## タイルサイズは圧縮後ではなく非圧縮バイト数で判定する

**タグ**: 一般則

**状況(Context)**
`tippecanoe`のようなツールが出すタイルサイズ警告の基準と、実測したサイズを突き合わせる場面。

**問題/対立する力(Problem / Forces)**
`pmtiles tile <path> <z> <x> <y> | wc -c`で測定すると圧縮後のバイト数が出るが、tippecanoeの
サイズ警告は非圧縮サイズを基準にしている。圧縮後の値だけを見て「解決した」と誤認すると、
実際には基準を大幅に超えたままになる。

**解決(Solution)**
`pmtiles tile ... | gunzip -c | wc -c`のように、必ず解凍してから非圧縮サイズを測定する。

**実例(Known uses)**
- `kitavolca` — `--drop-densest-as-needed`適用後、圧縮後バイト数で「実測ゼロ件」と誤認して
  安心したが、`gunzip -c`してから測り直すと実際は1.2〜1.6MBもあり全く解決していなかった

---

## 自動間引き(`--drop-densest-as-needed`等)は、何が失われるか制御できないリスクがある

**タグ**: 一般則

**状況(Context)**
tippecanoeのような自動間引きオプションで、密度の高いfeatureを自動的にドロップしてサイズを
削減しようとする場面。

**問題/対立する力(Problem / Forces)**
自動間引きは手軽だが、どのfeatureが失われるかを予測・制御できない。目視で確認するまで、
特定エリアのデータが無制御に大量ドロップされていることに気づかないことがある。

**解決(Solution)**
自動間引きに頼らず、上記の「feature単位のminzoomシフト」のような、影響範囲を予測できる
制御手段を優先する。自動間引きを試す場合は、必ず結果を目視で確認する。

**実例(Known uses)**
- `kitavolca` — `--drop-densest-as-needed`が大雪山エリアの等高線(7101/7102)を無制御に
  大量ドロップしていたことが目視確認で判明。データ欠損という実害があったため完全に撤去し、
  minzoomシフトのみの方式に切り替えた

---

## ビルドログの「warning 0件」は、最終成果物の適合性を保証しない

**タグ**: 一般則

**状況(Context)**
tippecanoe等のビルドツールが警告を出さずに完了した後、最終成果物(PMTiles等)がサイズ基準を
満たしているか確認する場面。

**問題/対立する力(Problem / Forces)**
ビルドログとPMTiles実体の非圧縮サイズが食い違うケースがある。ログに警告が出ていないことを
「問題なし」の証拠として扱うと、実際には基準を超えたタイルを見落とす
([`patterns/verification-discipline.md`](verification-discipline.md)の「『成功終了』は
『正しい出力』を意味しない」と同じ精神)。

**解決(Solution)**
ビルドログを信用せず、常に`pmtiles tile ... | gunzip -c | wc -c`で最終成果物を直接測定する
運用にする。検証コマンドをドキュメント(`docs/zoom-policy.md`等)に明記しておく。

**実例(Known uses)**
- `kitavolca` — ビルドログとPMTiles実体の非圧縮サイズが食い違うケースを複数回経験し、
  常に直接測定する運用に切り替えた
