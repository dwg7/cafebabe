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
