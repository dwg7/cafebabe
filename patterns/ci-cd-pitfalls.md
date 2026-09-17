# CI/CDの落とし穴

GitHub Actions等のCI/CD環境特有の、ローカル環境とは異なる挙動について。
2026-09-02、全エージェントへの自由知見募集(D6)より。

---

## GitHub Actionsのcontainerジョブは、通常のジョブと挙動が地味に違う

**タグ**: 個別事情(zukaku。実例1件のまま長期間増えていないため、CONTRIBUTING.mdの棚卸し
基準に従い一般則から見直し、2026-09-08)

**状況(Context)**
GitHub Actionsのワークフローで`container:`を指定したジョブを初めて使う場面。

**問題/対立する力(Problem / Forces)**
containerジョブは、通常の(ホスト直接実行の)ジョブと表面上は同じように見えて、いくつかの
地味な差異がある。

**解決(Solution)**
実機検証で踏んだ3つの落とし穴とその対策:
- `tj-actions/changed-files`がcontainer+pushイベントの組み合わせで失敗する
  → 「既にresponseがあるリクエストはスキップ」という冪等な代替ロジックに置き換える
- デフォルトシェルが`sh`で`shopt`等bash構文が通らない → `shell: bash`を明示する
- `safe.directory`のgit所有権チェックに引っかかる →
  `git config --global --add safe.directory`が必要

**実例(Known uses)**
- `zukaku` — [ADR 0006](https://github.com/dwg7/zukaku/blob/main/adr/0006-github-actions-render-pipeline.md)
  で上記3つを実機検証

---

## 外部サイトに依存する検証はCIに入れず、手動スクリプトに分ける

**タグ**: 一般則

**状況(Context)**
自分のデータソースの正当性を、外部サイト(政府機関の公開ページ等)と突き合わせて検証する
場面。

**問題/対立する力(Problem / Forces)**
外部サイトへの依存をCIに組み込むと、相手サイトの構成変更・一時的な不調・レート制限等で
CIが不安定になる。CI自体の役割(生成物の整合性確認)と、外部との突き合わせ検証は、
失敗モードの性質が異なる。

**解決(Solution)**
外部サイトに依存する検証は手動実行のスクリプトに分離し、CIには含めない。CIは生成物内部の
整合性(セル収支・一意性・データとドキュメントの同期等)だけを見る役割に絞る。

**実例(Known uses)**
- `tabularmaps/do` — 総務省サイトへの依存を伴う市町村コード検証を手動スクリプトに分離し、
  CIは生成物の整合性確認のみに絞った(2026-09-17)
