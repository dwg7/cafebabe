# HANDOVER

## Status as of 2026-11-13

パターン集は`patterns/`に39ファイル(テーマは26)。`PROJECTS.md`は約50件のリポジトリを収録
(dwg7・UNopenGIS・optgeo・tabularmaps の各org と hfu 個人名前空間)。ADRはD1〜D20。

**最大の進行中の事項は、知識表現を miso に書き換える移行(D20)。** 段階0(基準線)まで終わり、
段階1(試行)に進むかの判断を hfuさんに仰ぐところ。計画と結果は`migration/`にある:

- `migration/PLAN.md` — 妥当性の検討と計画(段階0〜5、能力C1〜C10、判断事項)
- `migration/inventory.py`・`baseline.json` — 台帳。節199・実例248・訂正12・外部URL 95 が減らないことの基準
- `migration/acceptance-tests-v0.md`・`baseline-run-1.md` — 受け入れテスト24問と基準線(pass 23、partial 1)
- `migration/inbound-links.md` — 外からのリンク(28リポジトリ。切れるURLは14件・2ファイル)

決定済み(hfuさん、2026-11-13): 正本はメインツリー(`miso/cafebabe.md`、小さいテーマを持つ)と
テーマツリー(`miso/<テーマ>.md`、大きいテーマだけ)。置き場所は`miso/`。`DECISIONS.md`と`HANDOVER.md`は
第1期は外に残す。全体の結合版は作らない。**移行が終わるまで、旧構造(`patterns/`)が正本で、寄稿は
今の形で受ける。** 移行で1つに戻るファイルを、今から分割しない(300行の目安を超えたファイルが
あるが、そのままにする)。

**運用(D14)**: 判断待ちは2〜3件溜まったら会話内でまとめて確認。1件だけ急ぐならその場で。5件超は
Planモード。
**運用(D17)**: cafebabe自身の解釈は歓迎される。ただし解釈・推論・未検証であることを明記する。
**運用(D19)**: PRIVATEリポジトリは名前・URL・技術構成の一言要約まで。第三者の識別情報も同じ。

## この期間にあったこと(2026-09-24〜11-13、要約)

- **fleetの重心が、知識を人とAIで醸す方法(kcai、miso)へ移った。** 公開のkcai系7件を登録済み
  (kcai、miso、miso-geo、kcai-terrio、kcai-un-docs、kcai-yuiseki-datasets、universe)。非公開の3件は
  未登録(登録前に本人へ確認する)
- **新規参加**: plateau-juice、rpi3-server-guide、unopengis.github.io、snow-hokkaido、do-survey(寄稿4件)、
  dorayaki。寄稿から新設したファイル: `analysis-report-verification.md`、
  `administrative-records-as-observations.md`、`static-site-publishing.md`
- **Open MCTの評価**(hfuさんの問い「採用して良かったか」)を、`open-mct.md`の「限界と選ぶ基準」に
  cafebabeの解釈として記録。起動時の`reading 'key'`エラーの原因(時刻系の未設定)を、do-surveyの特定と
  cafebabeの再現で記録
- **hfuさんの推奨を1件記録**: 静的サイトは、JSとCSSをインラインにした1ファイルの`index.html`にまとめる
- **cafebabe自身の誤りと古い記述を、4件訂正した**: Open MCT 4.3.0の正式版、MapLibre v6のワーカーの閉包
  (6.13.0以降は自己完結)、Plotの実績の書きすぎ、`.nojekyll`が無いときの挙動。後の2件は、基準線の
  実行で別のエージェントが指摘した
- **教訓調査**(2026-10-02): 稼働中の3セッションに実施、18件を反映。稼働セッションが多いときに再実施の
  価値がある

## Pending

1. **miso移行の段階1に進むかの判断**(hfuさん)。あわせて未決: 状態の語彙(6語の案)、分ける規則の
   しきい値、試行のテーマ(Open MCTは4項目の形になっていない難しい例。典型的なテーマの実測が別に要る)
2. **`dwg7/miso`の担当への照会**(未了。担当セッションが稼働していなかった)。問い: 同じ共有地の中で
   互いに参照する複数のインスタンス(メインツリーとテーマツリー)は想定の内か。検査器が本文中の
   ファイルシステムのパスを「解決しない参照」と警告する件
3. `dwg7/cafebabe`・`UNopenGIS/7`のissueとPRの定期確認(「起床」と言われたら必ず両方。`git fetch`も)
4. `PROJECTS.md`に未登録の、動いているリポジトリ(bvmap-koicha、waterloo、chigent、spiccato、caketest、
   layers-martin、oam-starc、dwg7.github.io、foil4g、adsb-survey、kikicom ほか)
5. D1'(hfuさん未レビューの.mdの棚卸し): 6ファイル完了のまま。miso移行の段階2(状態の割り当て)に
   吸収するのが自然——hfuさんには未確認
6. hfuさん側で止まっているもの: slateのOllamaをaaltoから使う件(SSHトンネルを11435番で張る案の結果待ち)、
   `unopengis.org/almanac.ics`の年末会議(2026-12-09)の反映(担当セッションは終了)
7. zukaku#9のフォロー(優先度低)

## Known open items

- 「個別事情」タグと「プロジェクト固有すぎて置かない」の境界は、運用しながら見極め中(D3)
- 「助言→実装→検証」の実例は、独立収束と証拠の重みが違うことを毎回明記する
- 未再現のまま記録している報告: MapLibreの`tileSize<512`のハング、`raster-resampling: 'nearest'`の真っ黒
- cafebabeが「聞くだけでなく自分で検証する」場面が増えている。確かめたこと、報告のままのこと、推論を
  書き分ける(miso移行の動機でもある)

## Where to look

- miso移行 → [migration/PLAN.md](migration/PLAN.md)、D20
- D1〜D20の経緯 → [DECISIONS.md](DECISIONS.md)
- dwg7の組織文脈 → [DWG7-CONTEXT.md](DWG7-CONTEXT.md)、Staccato → [STACCATO-CONTEXT.md](STACCATO-CONTEXT.md)
- 各プロジェクトのリポジトリ → [PROJECTS.md](PROJECTS.md)
- 知見 → [README.md](README.md)の一覧、未実装のアイデア → [`ideas/README.md`](ideas/README.md)
- 運用 → [CLAUDE.md](CLAUDE.md)、貢献 → [CONTRIBUTING.md](CONTRIBUTING.md)

## Resume prompt

1. このファイルと、D20、`migration/PLAN.md`の§5・§6を読む
2. `dwg7/cafebabe`・`UNopenGIS/7`のissueとPRを`gh`で確認する
3. cross-session messageが届いていれば、まず対応する。寄稿は旧構造(`patterns/`)に取り込む
4. miso移行は、hfuさんの判断が出た段階だけを進める。段階の終わりごとに報告して、判断を仰ぐ
