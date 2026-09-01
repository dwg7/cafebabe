# データ出自調査(Data Provenance Research)

プロジェクトが依拠する外部データ・基盤・略語の来歴を検証する営みについて。
[`patterns/case-study-research.md`](case-study-research.md)(先行事例研究)と調査ツール
キットは共通するが、目的の方向が逆——「外を見て、自分の設計に借用できるものを探す」のでは
なく「内(自分が既に依拠しているデータソース)を見て、その来歴・正当性を検証する」——のため
別ファイルとして分離。
2026-09-02、vientiane-planning-mapからの提供より。

---

## 依拠先の来歴を辿り、謝辞・説明文の正確性を担保する

**タグ**: 一般則

**状況(Context)**
プロジェクトが依拠する外部データ・基盤・略語(例: `GLUP2030`、`Virgo`)の名前をそのまま
使っているが、なぜその名前なのか・誰が資金提供したのか・技術基盤は何かを検証していない場面。

**問題/対立する力(Problem / Forces)**
不正確・浅い謝辞のまま公開してしまうリスクがある。また、来歴を辿ることで見えてくる「兄弟
プロジェクト」(同じ基盤技術を使う他の取り組み)や、そこから示唆される制約・品質の含意を
見逃す。

**解決(Solution)**
先行事例研究(`patterns/case-study-research.md`)と同じ調査ツールキット(About/沿革ページの
fetch、資金提供機関の実績調査、実装者個人の発見)を、外部の先行事例ではなく**自分自身の
依存先に向ける**。得られた事実は謝辞・CLAUDE.mdの説明文に還元する。

**実例(Known uses)**
- `vientiane-planning-map` — データソース(Virgo)のAboutページから正式名称・JICA支援・
  GeoNode基盤・2023-09-26ローンチを発見。さらに調査を進め、`GLUP2030`の"2030"がJICAの
  2010-2011年ヴィエンチャン都市圏開発マスタープラン調査の成果物"Vientiane Master Plan
  2030"に由来することを突き止め、GeoNodeの実装者(Sylvain Dorey氏)まで特定した。詳細は
  [`CASE_STUDIES.md`#JICA都市地域開発グループの実績重点調査](https://github.com/dwg7/vientiane-planning-map/blob/main/CASE_STUDIES.md#jica都市地域開発グループの実績重点調査2026-09-02)
  参照。この調査を受け、README.md/CLAUDE.mdの謝辞・説明文を正確化した
