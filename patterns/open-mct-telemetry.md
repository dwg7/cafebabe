# Open MCT — Plot/Telemetry API(結論はまだ出ていない)とrequest/subscribe

`patterns/open-mct.md`の一部として運用。全体像・寄稿プロジェクトの一覧はそちらを参照。

## Plot / Telemetry API — 結論はまだ出ていない、証拠が対立している

- **sas0の経験（4.3.0-rc1、CDN）**：providerが返す非永続オブジェクトに対し、メタデータ・合成・`request()`（実測30件を直接計測）・凡例（Min/Max表示）はすべて正しく動作するのに、**実際のグラフ描画（点・線）だけが最後まで空**。WebGLキャンバスは健全（`preserveDrawingBuffer: true`で「本当に何も描かれていない」ことを確認）。素のテレメトリオブジェクトではなく`telemetry.plot.overlay`タイプでラップし`configuration.series`を事前注入しても同じ。`markers: true`にすると別の内部エラー`getXVal is not a function`。差分検証のため純正「+CREATE」でOverlay Plotを新規作成しようとしたが、sas0のツリーが読み取り専用プロバイダのため保存先が存在せず断念——「`+Create`された永続オブジェクトなら動くのか」は**未検証のまま**。
- **claude-mctの検証（4.2.0、npm）**：`telemetry.values`に`hints: { domain: 1 }`（時間軸）と`hints: { range: 1 }`（値、`format`が`string`以外）を正しく揃えれば、providerが返す非永続オブジェクトでもPlotは正常に描画される、と報告。ただし——
- **判明した本物のバグ——`telemetry.values`配列の並び順**：claude-mctがsas0のメタデータ形状（`mag`/`timestamp`、`float`/`utc`）を最小構成で再現・検証した結果、**配列内で`hints.domain`の値が`hints.range`の値より後ろに書かれていると、`PlotSeriesData.onXKeyChange()`が`this.formats[e]`を見つけられず`this.getXVal`が一度も設定されない**ことを特定した（`4.3.0-rc1`のnpmビルドで再現、`4.3.1`でも再現）。sas0の元のメタデータは`mag`（range）が先、`timestamp`（domain）が後——まさにこの順序だった。これは`markers: true`で出ていた`getXVal is not a function`エラーの実際の原因として確度が高い。**対策：`telemetry.values`は必ずdomain値（時間軸）を先に、range値（データ値）を後に書く。**
- **それでも残る食い違い（未解決）**：配列順を修正しても、claude-mctの**最小再現環境ではバージョンを問わず（4.2.0/4.3.0-rc1/4.3.1すべて）描画されなかった**。一方、claude-mctの本体アプリ（複数フィールド・ツリー経由のナビゲーション・実際に動くsubscribe）では`4.2.0`で正常に描画されている。つまりバージョン差では説明がつかず、**「最小構成 vs フルアプリ」の何らかの構造差**（root直下か子オブジェクトか、他プラグインの有無、subscribeの実動作有無等）が影響している可能性が高い——ここは未特定のまま。sas0の元のコードは当時のセッション内でのみ存在し、コミットされる前に元に戻されたため、リポジトリ履歴には残っていない（DECISIONS.md D53に記録された形状の引用のみが手がかり）。**この節は未確定として扱うこと。**
- **2026-09-06、sas0自身によるD53の再検証と分類**：hfuさんからの「メタデータ問題／datum形問題／表現力問題のどれに近かったか」という問いに対し、sas0は2段階の問題だったと回答した。①まず`UTCTimeSystem()`の明示アクティベート必須・テレメトリオブジェクトへの`composition`バケット必須・`telemetry.plot.overlay`型でのラップ必須、といった非自明な設定要件を潰し、メタデータ・合成・`request()`・軸ラベル・凡例が全て正しく動作すると確認した。②それでも**線も点も一切描画されない（エラーも出ない）という主障壁は最後まで残った**。`markers: true`時の`getXVal is not a function`は、sas0の元メタデータが実際に`mag`（range）を`timestamp`（domain）より先に書く「間違った順序」だったため、上記の配列順序バグでほぼ説明がつくと確認された——一方で**主障壁（無描画・無エラー）の方は、順序修正だけで直るかは未検証**（D53でコード自体を削除したため再テスト機会が無かった）で、claude-mctの最小再現環境が順序修正後も描画に失敗し続けた報告と整合する。**「表現力（見せ方）の判断は一切混ざっていない**——単純な折れ線ですら一度も描画されなかったため、見せ方の比較検討の土俵にすら立てなかった」とも明言している。**結論：sas0のケースは主にメタデータ形状／設定面の壁であり、SVGへの切り替えは表現力上の好みではなく純粋なブロッカー回避だった。**
- **`openmct.plugins.PlanLayout()`（タイムライン/ガントチャート）**：sas0・mapterhorn-monitorとも、providerが返すオブジェクトに対して`.c-plan__contents`が常に空になり、「Attempted to mutate immutable object」というエラーが出る（sas0はPlotの`xKey`/`yKey`/`interpolate`等のカスタムフィールドを試した際にも同文言のエラーに遭遇）。claude-mctはコード読解のみでの判断だが、`plan`タイプはアップロードされたJSON blobと`getMutable()`ベースの永続化を前提にしていると推測——3者の情報は矛盾なく一致しており、確度は高い。**providerパターンとは相性が悪いと考えてよく、独自SVG/Canvasでの代替を推奨。**
- **実践的な結論（現時点）**：Plot/Telemetryの高機能ビューは、自分の正確なバージョン・構成で直接試すまで動作を仮定しない方がよい。3プロジェクトとも、素のSVG/Canvasを自前のビュープロバイダで描画するアプローチは確実に動いており、実績のある安全な代替手段になっている。

## `request()`/`subscribe()` — 5プロジェクト中4プロジェクトがTelemetry API自体を使っていない

2026-09-06のヒアリングより。Open MCTのTelemetry API（`request()`＝履歴取得、`subscribe()`＝リアルタイム購読）を実際に使っているのは、当時ヒアリングした4プロジェクト中1つだけだった（starsは2026-09-07に追加確認）。

| プロジェクト | request | subscribe | 実際の更新方式 |
|---|---|---|---|
| sas0 | ✗ | ✗ | telemetryプロバイダ自体をD53で完全撤去（`registerTelemetry`型・`openmct.time`設定含む）。更新は`registerInstrument`の`autoRefresh`（`setInterval`による再描画）または手動更新ボタンのみ |
| mapterhorn-monitor | ✗ | ✗ | 同上の結論に**独立に到達**。`registerInstrument`の`autoRefresh`オプション（内部`setInterval`）＋`render(container)`内で直接`fetch()`しDOMへ手で描画 |
| m3xx-fleet | ✗ | ✗ | 同じく独立に到達。ビュー（`hostViewProvider`/`andonViewProvider`）の`view()`内で直接`fetch()`し、結果をDOMに手で描画。Open MCTはツリー（`addProvider`/`addRoot`）としてのみ利用 |
| stars | ✗ | ✗ | cafebabeの設計助言（Telemetry API回避を明示的に推奨）に沿って実装。`objectViews.addProvider()`＋自前SVG描画のまま7オブジェクトに分割し、本番まで問題なく反映 |
| claude-mct | ○ | ○ | telemetry providerに`request()`（feedClientのキャッシュ）と`subscribe()`（型ごとに`subscribe`/`subscribeEdges`/`subscribeFleetSummary`を呼び分け）を実装。ただし**feedClient自体は5秒間隔のポーリングで、真のプッシュ型ではない**——Open MCT側にはsubscribe/callbackのインターフェースとして見せているだけ、という補足あり |

**共通する背景**：sas0・mapterhorn-monitor・m3xx-fleetの3プロジェクトはいずれも「静的スナップショットが一定間隔（2時間おき、15分おき等）で更新される」性質のデータを扱っており、Telemetry APIの購読モデルに乗る必要が生じなかった。3者は互いに参照せず**独立に同じ結論**（ツリー＋ビュー差し込み機構だけを借り、データ取得・描画は自前のfetch+DOM/Canvasで完結させる）に到達している。starsは同じ結論を、独立発見ではなくcafebabeの助言を受けて採用し、実地で確認した——証拠としての性質は異なる（`patterns/open-mct-object-model.md`のProvider構造セクション末尾の注記も参照）が、「助言通りに実装して問題が起きなかった」という点自体は推奨の妥当性を補強する。

**現時点の結論**：Open MCTを選ぶ理由は必ずしも「Telemetry APIのpush/pull抽象化を使いたいから」ではない——**「異種混在の情報源を1つのツリー・ブラウズUIで束ねたい」という価値だけを目的に、Telemetry API自体は使わないという選択も十分に実用的な標準構成になっている**（`patterns/open-mct.md`の「Open MCTの強み」の三層分離の議論とも整合する）。真のリアルタイム性・大量データの効率的な差分配信が要る場合にのみ、claude-mctのようにTelemetry APIへ乗る価値が出てくる。
