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
| maplibre-gl-atlas | https://github.com/dwg7/maplibre-gl-atlas | zukakuのPrint-in-Browser機能を切り出したMapLibre GL JSコントロール(`AtlasControl`/`AtlasSheet`)。CC0 1.0。2026-09-09新規参加 |
| kaga0 | https://github.com/dwg7/kaga0 | Kitavolca Air-Gapped Applianceの初実装(MapLibre Native) |
| plateau-mago-implicit | https://github.com/dwg7/plateau-mago-implicit | PLATEAU由来のImplicit 3D Tiles実験(室蘭・更別) |
| vientiane-planning-map | https://github.com/dwg7/vientiane-planning-map | ヴィエンチャンのゾーニング+ベースマップビューア(height-coverageの姉妹プロジェクト) |
| ferspas57 | https://github.com/dwg7/ferspas57 | FERSPAS×Staccato: FAO/DWG5とDWG7の連携(STAC→martin catalogインタフェース統合)。2026-09-03新規参加 |
| m3xx-fleet-ops | https://github.com/dwg7/m3xx-fleet-ops | JICA研修用Raspberry Piフリート運用(意思決定ログ)。2026-09-05新規参加 |
| m3xx-fleet | https://github.com/dwg7/m3xx-fleet | m3xx-fleet-opsのOpen MCT監視ダッシュボード(GitHub Pages、Publicに分離。理由は`patterns/unattended-progress-visibility.md`参照) |
| staccato-ecosystem | https://github.com/dwg7/staccato-ecosystem | staccato-specのコンパニオンリポジトリ。教育・防災・測量等の実領域向け協力手法論と生態系成長戦略。2026-09-09新規参加 |
| kataribe | https://github.com/dwg7/kataribe | dossierベースの語り部Staff(staccato)。2026-09-05創設、staccato-ecosystemから輩出。2026-09-11、専任セッション(kataribe-8d)への引き渡し時にpush漏れが発覚・解決した実例として`patterns/verification-discipline.md`参照 |

## UNopenGIS org(関連組織)

dwg7本体の外だが、staccato関連プロジェクト群の規範仕様を保持する組織。

| プロジェクト | リポジトリ | 一言 |
|---|---|---|
| staccato-spec | https://github.com/UNopenGIS/staccato-spec | Staccatoアーキテクチャ(User/Staff/Cartographer/Library)の規範仕様。実装コードは持たない。2026-09-09新規参加 |

## optgeo org(関連組織)

dwg7本体の外、hfuさん関連のインフラ・データ公開プロジェクトを置く組織
(`stars.optgeo.org`等のドメインとも関連)。

| プロジェクト | リポジトリ | 一言 |
|---|---|---|
| adopt-hokkaido-lidar | https://github.com/optgeo/adopt-hokkaido-lidar | 北海道の公開航空レーザ測量データをLAZ→COPC変換し、来歴・ライセンス確認済みのものをSource Cooperativeへ公開するパイプライン。2026-09-10新規参加 |

## hfu 個人名前空間

| プロジェクト | リポジトリ | 一言 |
|---|---|---|
| kitavolca | https://github.com/hfu/kitavolca | 北海道火山図パイプライン(VBM+VLCM→PMTiles)。`dwg7 org`に同名のフォークがあるが2026-07-19で更新停止、本体はこちら(下記訂正参照) |
| mapterhorn-japan-bridge | https://github.com/hfu/mapterhorn-japan-bridge | 標高データパイプラインの司令塔(決定ログ) |
| mapterhorn | https://github.com/hfu/mapterhorn | パイプラインコード本体(`mapterhorn/mapterhorn`のフォーク) |
| mapterhorn-monitor | https://github.com/hfu/mapterhorn-monitor | Open MCT監視ダッシュボード([patterns/agent-repository-boundaries.md](patterns/agent-repository-boundaries.md)参照) |
| stars | https://github.com/hfu/stars | タイルサーバー(stars.optgeo.org)のゲートキーパー |
| claude-mct | https://github.com/hfu/claude-mct (PRIVATE) | Open MCTベースのフリート(Claude Codeエージェント/セッション)可視化ダッシュボード |
| kitaphoto17-navara | https://github.com/hfu/kitaphoto17-navara (PRIVATE) | Martin(stars.optgeo.org)配信のkitaphoto17タイルレイヤーをNavara(`maplibre/navara`)で表示するGitHub Pages静的サイト。2026-09-04新規参加 |
| volca | https://github.com/hfu/volca (PRIVATE) | 北海道の常時観測火山9火山の防災計画・避難計画PDFを収集・横断分析し、北海道地方測量部とdwg7への戦略を立案。2026-09-09新規参加 |
| hokkaido-points | https://github.com/hfu/hokkaido-points (PRIVATE) | 北海道内の測量基準点(電子基準点・三角点・水準点・多角点等)を、基盤地図情報の母集団から市区町村単位の分割取得でPMTiles化しMapLibre GL JSで探索可能にする調査基盤。測量法上の承認確定までPrivate。2026-09-11新規参加。adopt-hokkaido-lidarとの関連は未確認 |

---

**更新の仕方**: 新しいプロジェクトが増えたら、または既存プロジェクトのリポジトリが移動・
リネームされたら、この表に追記・訂正する。訂正は`CONTRIBUTING.md`の型に従い、古い行を
消さず日付付きの注記を添える。

**訂正 (2026-09-06)**: `kitavolca`の行を`dwg7 org`表から`hfu 個人名前空間`表へ移動し、
リンクを`dwg7/kitavolca`から`hfu/kitavolca`に修正した。`dwg7/kitavolca`は`hfu/kitavolca`の
フォークで、2026-07-19以降更新が止まっている(古いスナップショット)。実際に開発が続いて
いる本体は`hfu/kitavolca`(直近push: 2026-08-30)。`patterns/`内の複数のコミットリンクは
元々`hfu/kitavolca`を指しており正しかった——この表の方が誤っていた(外部モデル(Fable)
による知見ベース全体レビューで発覚、2026-09-06)。
