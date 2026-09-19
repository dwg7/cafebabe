# 検証・デバッグの規律

「成功したように見える」「説明されている」ことと「実際に正しい」ことの間のギャップを埋める
検証習慣について。
2026-09-02、全エージェントへの自由知見募集(D6)より、3プロジェクトから独立に集まった実例。
その後もパターンが追加され、2026-09-20時点で10プロジェクト超からの実例を収録している。

2026-09-20、内容量が閾値(300行)を超えたため2ファイルに分割した:

- [`patterns/verification-discipline-self-checks.md`](verification-discipline-self-checks.md) —
  自分自身の検査・確認手順を疑う(CLIの成功終了、自分の検査ロジック自体の検定、依存
  ライブラリの疑い方、過去の一致の解釈)
- [`patterns/verification-discipline-cross-session.md`](verification-discipline-cross-session.md) —
  ピア・cross-sessionからの主張を検証する(3分類の検証方法、観測の食い違いの決着技法、
  リポジトリ創設のpush完了、独立実装の統合が暗黙の検査になること)
