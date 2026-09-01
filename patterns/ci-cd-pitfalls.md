# CI/CDの落とし穴

GitHub Actions等のCI/CD環境特有の、ローカル環境とは異なる挙動について。
2026-09-02、全エージェントへの自由知見募集(D6)より。

---

## GitHub Actionsのcontainerジョブは、通常のジョブと挙動が地味に違う

**タグ**: 一般則

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
