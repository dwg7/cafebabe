# dwg7 プロジェクト一覧

各プロジェクトへの**永続的な参照先**。エージェント(セッション)は任務が終わればアーカイブ
されて消えるが、リポジトリは残る。ここにあるのはリポジトリへのリンクであり、担当セッション名
ではない(現在どのセッションがどのプロジェクトを担当しているかは`CLAUDE.md`の「既知のピア」
を参照——ただしそちらはcross-session連携用の一時的な情報で、セッションが入れ替われば古くなる)。

プロジェクト固有すぎて`patterns/`に一般化されない知見(特定のハードウェア・データ・技術選定に
強く依存するもの)は、各リポジトリの`CLAUDE.md`/`DECISIONS.md`にある。ここから辿ること
(詳細は[DECISIONS.md D3](DECISIONS.md)参照)。

## dwg7 org

| プロジェクト | リポジトリ | 一言 |
|---|---|---|
| cafebabe | https://github.com/dwg7/cafebabe | このリポジトリ自身 |
| sas0 | https://github.com/dwg7/sas0 | 北海道防災情報ダッシュボード(Open MCT)。`patterns/open-mct.md`の旧マスター管理者 |
| height-coverage | https://github.com/dwg7/height-coverage | OSM建物高さ入力状況の啓発サイト |
| zukaku | https://github.com/dwg7/zukaku | MapLibre+Martinによる印刷アトラス生成(Field Papersの現代版) |
| kaga0 | https://github.com/dwg7/kaga0 | Kitavolca Air-Gapped Applianceの初実装(MapLibre Native) |
| kitavolca | https://github.com/dwg7/kitavolca | 北海道火山図パイプライン(VBM+VLCM→PMTiles) |
| plateau-mago-implicit | https://github.com/dwg7/plateau-mago-implicit | PLATEAU由来のImplicit 3D Tiles実験(室蘭・更別) |
| vientiane-planning-map | https://github.com/dwg7/vientiane-planning-map | ヴィエンチャンのゾーニング+ベースマップビューア(height-coverageの姉妹プロジェクト) |
| ferspas57 | https://github.com/dwg7/ferspas57 | FERSPAS×Staccato: FAO/DWG5とDWG7の連携(STAC→martin catalogインタフェース統合)。2026-09-03新規参加 |

## hfu 個人名前空間

| プロジェクト | リポジトリ | 一言 |
|---|---|---|
| mapterhorn-japan-bridge | https://github.com/hfu/mapterhorn-japan-bridge | 標高データパイプラインの司令塔(決定ログ) |
| mapterhorn | https://github.com/hfu/mapterhorn | パイプラインコード本体(`mapterhorn/mapterhorn`のフォーク) |
| mapterhorn-monitor | https://github.com/hfu/mapterhorn-monitor | Open MCT監視ダッシュボード([patterns/agent-repository-boundaries.md](patterns/agent-repository-boundaries.md)参照) |
| stars | https://github.com/hfu/stars | タイルサーバー(stars.optgeo.org)のゲートキーパー |
| claude-mct | https://github.com/hfu/claude-mct (PRIVATE) | Open MCTベースのフリート(Claude Codeエージェント/セッション)可視化ダッシュボード |

---

**更新の仕方**: 新しいプロジェクトが増えたら、または既存プロジェクトのリポジトリが移動・
リネームされたら、この表に追記・訂正する。訂正は`CONTRIBUTING.md`の型に従い、古い行を
消さず日付付きの注記を添える。
