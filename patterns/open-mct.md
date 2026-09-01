# Open MCT 実地ノウハウ集

複数の独立したOpen MCT導入から得られた、実地の知見をまとめたドキュメントです。sas0が dwg7 内でのOpen MCT使用のフラッグシップという位置づけのため、このリポジトリでマスターを管理しています。他リポジトリ（`mapterhorn-japan-bridge`、`claude-mct`）はここへのリンクを張り、内容を重複させません。

各プロジェクトの立場は対等です——sas0が「本家」で他が「参考」という上下関係ではなく、3つの独立した実装が別々に得た知見を持ち寄っています。矛盾する知見（特にPlot APIまわり）は、無理に一本化せず、対立したまま記録します。

## 寄稿プロジェクトと構成

| プロジェクト | バージョン | 入手経路 | 用途 |
|---|---|---|---|
| sas0 | `4.3.0-rc1` | CDN（unpkg） | 静的な状況認識ダッシュボード（人間が時々見る、バックエンドなし） |
| mapterhorn-japan-bridge/mapterhorn-monitor | `4.3.0-rc1` | CDN（unpkg） | 生産パイプラインの静的スナップショット表示 |
| claude-mct | `4.2.0` | npm（自前ホスティング、Vite） | 実セッションのライブテレメトリ |

## 唯一、一貫して信頼できる拡張ポイント

3プロジェクトとも同じ結論に達している：**`openmct.objects.addProvider()` + `openmct.composition.addProvider()`** の組み合わせが、GUIでの`+Create`を経ずに安定したツリー構造を構築する唯一の方法。これに加えて、

- カスタムビューが必要なら `openmct.objectViews.addProvider()`（sas0/mapterhorn-monitor）
- カスタムテレメトリ表示が必要なら `openmct.telemetry.addProvider()`（claude-mct）

を組み合わせる。独自`namespace`を作り、`get(identifier)`でオブジェクトを返し、`composition.addProvider`で親子関係を返す——この三点セットだけで、コードで完全に定義された安定したアプリが作れる。

基本プラグイン（`LocalStorage`・`UTCTimeSystem`・`Espresso`テーマ）のインストール、`openmct.types.addType()`によるカスタムタイプ登録は、3プロジェクトとも問題なく動作。

## ブートストラップの落とし穴

- **CDNバージョン固定**：存在しないバージョンを指定すると、エラーも出ずに真っ白な画面になる（sas0はかつて`3.3.0`で被弾）。`docs/dist/openmct.js`と`docs/dist/espressoTheme.css`（`openmct.css`ではない——3.x→4.x系のどこかで名前が変わった）の両方が実在するか、`curl -sI`で確認してから固定する。〔sas0〕
- **`SharedWorker`のクロスオリジン/初期化エラー——症状は同じでも原因は2系統ある**：
  - 原因A（CDN経由）：Open MCT内蔵の検索インデクサがSharedWorkerを自分のCDNオリジンから起動しようとしてブラウザにブロックされる。`window.SharedWorker = undefined`を先に設定し、Open MCT組み込みの同期フォールバック（元々iOS向け）に倒すのが対策。〔sas0、mapterhorn-monitor〕
  - 原因B（npm自前ホスティング）：`openmct.setAssetPath()`を`install()`より前に設定していないと、ワーカースクリプトの相対パス解決が失敗し、SPAフォールバックがHTMLを返してパースエラー（`Unexpected token '<'`）になる。`openmct.setAssetPath('/node_modules/openmct/dist/')`を先に呼ぶことで解消。〔claude-mct〕
  - 同じ"Error with InMemorySearch worker"系の症状でも、構成によって原因が異なる。両方をチェックリストに入れる。
- **`openmct.start()`のセレクタ文字列対応**：4.3系では`openmct.start('#app')`のようにCSSセレクタ文字列を渡せる。ドキュメントがまだ読み込み中なら`DOMContentLoaded`まで自動的に待つ。`document.getElementById(...)`を渡す旧形式より扱いやすい。〔sas0〕
- **`openmct.on('start', callback)`の信頼性——プロジェクト間で結果が割れている**：
  - sas0（4.3.0-rc1、CDN）：確実に発火する。本番コードがこれに依存して動いている。
  - mapterhorn-monitor（同じく4.3.0-rc1、CDN、同じ「リスナーを`start()`より先に登録」という順序）：**一度も発火しない**。登録順序の違いという仮説は、両者が同じ順序だったため否定された。手がかりは、起動時に一貫して発生する`Uncaught (in promise) TypeError: Cannot read properties of undefined (reading 'key')`という未処理のPromise rejectionで、これが`'start'`のemit前に非同期チェーンを中断させている可能性がある（未確定）。
  - claude-mct（4.2.0、npm）：このイベントに依存しない設計のため未検証。
  - **現状の結論**：バージョン・環境依存で、原因は特定できていない。対策としては、リスナーは`start()`より先に登録した上で、**初期化処理をイベント経由だけに頼らず、`openmct.start()`の直後に直接（同期的に）書く**フォールバックを持たせるのが安全。
- **起動時の無害なコンソールエラー**：`Uncaught (in promise) TypeError: Cannot read properties of undefined (reading 'key')`が1回だけ出ることがある。ローカル検索インデクサの既知の癖で、再現性はあるが実害はない（tree navigation・Inspector等は正常動作）。新しいバグと誤認しないよう記録。〔sas0〕

## Plot / Telemetry API — 結論はまだ出ていない、証拠が対立している

- **sas0の経験（4.3.0-rc1、CDN）**：providerが返す非永続オブジェクトに対し、メタデータ・合成・`request()`（実測30件を直接計測）・凡例（Min/Max表示）はすべて正しく動作するのに、**実際のグラフ描画（点・線）だけが最後まで空**。WebGLキャンバスは健全（`preserveDrawingBuffer: true`で「本当に何も描かれていない」ことを確認）。素のテレメトリオブジェクトではなく`telemetry.plot.overlay`タイプでラップし`configuration.series`を事前注入しても同じ。`markers: true`にすると別の内部エラー`getXVal is not a function`。差分検証のため純正「+CREATE」でOverlay Plotを新規作成しようとしたが、sas0のツリーが読み取り専用プロバイダのため保存先が存在せず断念——「`+Create`された永続オブジェクトなら動くのか」は**未検証のまま**。
- **claude-mctの検証（4.2.0、npm）**：`telemetry.values`に`hints: { domain: 1 }`（時間軸）と`hints: { range: 1 }`（値、`format`が`string`以外）を正しく揃えれば、providerが返す非永続オブジェクトでもPlotは正常に描画される、と報告。ただし——
- **判明した本物のバグ——`telemetry.values`配列の並び順**：claude-mctがsas0のメタデータ形状（`mag`/`timestamp`、`float`/`utc`）を最小構成で再現・検証した結果、**配列内で`hints.domain`の値が`hints.range`の値より後ろに書かれていると、`PlotSeriesData.onXKeyChange()`が`this.formats[e]`を見つけられず`this.getXVal`が一度も設定されない**ことを特定した（`4.3.0-rc1`のnpmビルドで再現、`4.3.1`でも再現）。sas0の元のメタデータは`mag`（range）が先、`timestamp`（domain）が後——まさにこの順序だった。これは`markers: true`で出ていた`getXVal is not a function`エラーの実際の原因として確度が高い。**対策：`telemetry.values`は必ずdomain値（時間軸）を先に、range値（データ値）を後に書く。**
- **それでも残る食い違い**：配列順を修正しても、claude-mctの**最小再現環境ではバージョンを問わず（4.2.0/4.3.0-rc1/4.3.1すべて）描画されなかった**。一方、claude-mctの本体アプリ（複数フィールド・ツリー経由のナビゲーション・実際に動くsubscribe）では`4.2.0`で正常に描画されている。つまりバージョン差では説明がつかず、**「最小構成 vs フルアプリ」の何らかの構造差**（root直下か子オブジェクトか、他プラグインの有無、subscribeの実動作有無等）が影響している可能性が高い——ここは未特定のまま。sas0の元のコードは当時のセッション内でのみ存在し、コミットされる前に元に戻されたため、リポジトリ履歴には残っていない（DECISIONS.md D53に記録された形状の引用のみが手がかり）。**この節は未確定として扱うこと。**
- **`openmct.plugins.PlanLayout()`（タイムライン/ガントチャート）**：sas0・mapterhorn-monitorとも、providerが返すオブジェクトに対して`.c-plan__contents`が常に空になり、「Attempted to mutate immutable object」というエラーが出る（sas0はPlotの`xKey`/`yKey`/`interpolate`等のカスタムフィールドを試した際にも同文言のエラーに遭遇）。claude-mctはコード読解のみでの判断だが、`plan`タイプはアップロードされたJSON blobと`getMutable()`ベースの永続化を前提にしていると推測——3者の情報は矛盾なく一致しており、確度は高い。**providerパターンとは相性が悪いと考えてよく、独自SVG/Canvasでの代替を推奨。**
- **実践的な結論（現時点）**：Plot/Telemetryの高機能ビューは、自分の正確なバージョン・構成で直接試すまで動作を仮定しない方がよい。3プロジェクトとも、素のSVG/Canvasを自前のビュープロバイダで描画するアプローチは確実に動いており、実績のある安全な代替手段になっている。

## フルスクリーン／キオスクモードのパターン（巡回モード）

Open MCT自体には「フルスクリーン表示用のビュー」のような組み込み機能は無い。素のブラウザFullscreen APIと、Open MCT自身のUI chromeを隠すCSSを組み合わせて自前で実装する。〔sas0 D58、mapterhorn-monitorで再現・確認済み〕

- **2層構成**：①ブラウザ本体のFullscreen API（`document.documentElement.requestFullscreen()`、タブ・アドレスバーを消すだけ）。②Open MCT（Espressoテーマ）自身のヘッダー・左ツリー・右Inspectパネル・パンくずバーを隠すCSS——実地でDOM検査して見つけた、以下の安定したクラス名を使う：

  ```css
  .kiosk-mode-active .l-shell__head,
  .kiosk-mode-active .l-shell__pane-tree,
  .kiosk-mode-active .l-shell__pane-inspector,
  .kiosk-mode-active .l-browse-bar {
    display: none !important;
  }
  ```

  `document.body`にトグルクラスを付け外しするだけでよい。

- **最重要の落とし穴——状態のスコープ**：Open MCTは巡回先の計器に遷移するたびに、巡回モード自身のview/renderを破棄する。停止用UIや`setInterval`のハンドル・現在位置を、個々のview/renderのクロージャ内に置くと、次の計器に切り替わった瞬間に消える。**モジュールスコープ（ページ全体で1回だけ実行される場所）に状態を持たせ、停止UIは`document.body`に直接appendする**（Open MCTのビュー階層の外）——これでSPAの画面遷移をまたいで生き続ける。
- **Escキー対応**：ブラウザ標準のEsc→フルスクリーン解除を、`fullscreenchange`イベントで検知して巡回停止のトリガーにする。これをしないと「フルスクリーンだけ終わって、裏で画面が切り替わり続ける」という分かりにくい状態になる。

  ```js
  document.addEventListener('fullscreenchange', () => {
    if (!document.fullscreenElement && isRunning()) {
      stopCycling();
    }
  });
  ```

- **`requestFullscreen()`は必ずユーザー操作（クリック等）から呼ぶ**。ブラウザの仕様上の要件。失敗・拒否された場合は`.catch(() => {})`で握りつぶし、巡回ロジック自体（画面切り替え）は続行する——フルスクリーン化はあくまで付加的な演出として扱う。
- **未検証の領域**：ブラウザ自動化ツールでの実機確認では、sas0・mapterhorn-monitorとも、CSSによるOpen MCT chrome非表示は screenshot で視覚的に確認できたが、**ブラウザ本体レベルのフルスクリーン化（タブ・アドレスバーが消えるか）自体は自動化ツールでは確認できていない**——サンドボックス制限と見られる。マルチモニタ環境での挙動も、3プロジェクトとも未検証。
- **矢印キーでの手動送り**：巡回中に左右矢印キーで前後の計器へ手動遷移する機能を、mapterhorn-monitor・sas0の両方が独立に実装（sas0 D66）。自動tick・手動キー操作・タイマーリセットを1つの関数（`goToIndex`/`goToCycleIndex`）に集約するのが両者で一致した設計。落とし穴：①JavaScriptの`%`は負数をラップしない（`-1 % 5`は`-1`のまま）ので、後方遷移には`((newIndex % length) + length) % length`が必要。②`event.target`が`INPUT`/`TEXTAREA`/`SELECT`/`isContentEditable`の時はキー処理を素通しする防御を入れる。③手動遷移時は`clearInterval`→`setInterval`でタイマーを仕切り直し、直後に自動tickが割り込んで二重遷移しないようにする。

## デバッグ手法

**`console.log`/`console.error`の出力を信用せず、`window.__debug`のようなグローバル変数に副作用を記録してから直接読み出す方が確実な場合がある。** sas0（ブラウザ自動化ツールのタイミング起因と推測）、mapterhorn-monitor（同様の推測）、claude-mct（コンソール出力の切り詰め起因と特定）——原因は異なるが、対策は独立に収束した。Open MCTの複雑な起動シーケンスをデバッグする際の標準手法として記録する価値がある。

## バージョン選択：RCを含む最新を追うか、安定版で固定するか

観測された相関：

- **CDN経由・低ステークス（表示専用、壊れても実害が小さい）** → sas0・mapterhorn-monitorともRCを含む最新（`4.3.0-rc1`）を選択。
- **npm自前ホスティング・運用に組み込まれる高ステークス** → claude-mctは`4.2.0`（ただしこれは意図的な安定版選択ではなく、検証時点でnpmの`latest`タグがたまたまこれを指していただけ、との報告）。

**重要な補足**：sas0はD2で存在しないバージョン指定により一度完全に壊れた経験があり、D8で`4.2.0`→`4.3.0-rc1`に上げたのは「他に選択肢がない、唯一の現行アクティブ系列だから」という理由に近い。その後複数回再確認しているが（sas0 D45）、**`4.3.0`の正式版は現時点まで一度も出ていない**。つまり「RCを含む最新を追う」という選択は、実際には「不安定な最先端を追いかけるリスク」というより、「唯一メンテナンスされている系列に乗り続けているだけ」という状態に近い——`4.3.0-rc1`が長期にわたって事実上の「現行版」になっている。

また、npm経由とCDN（unpkg）経由では、同じ「latest」でも指すバージョンが異なりうる（claude-mctの指摘）——`npm install`は素直に安定版へ着地しやすいのに対し、CDN経由でバージョン指定を省略・緩めると、RCを含む最新が掴まれる可能性がある。

**さらに重要な訂正（claude-mctが2026-09-01に確認）**：openmctのnpm dist-tagsは直感に反する付け方になっている——

```
stable:   4.0.0
unstable: 4.2.0   ← claude-mctが実際に使っているバージョン
next:     4.1.0-alpha
latest:   4.3.1   ← 直近（数日前）に公開されたばかりの正式版
```

「新しいはずの`4.2.0`が`unstable`タグ、より古い`4.0.0`が`stable`タグ」という、パッケージ名だけでは読み取れない状態になっている。**「安定版で固定したい」場合、`npm install openmct@latest`はもちろん`@unstable`のような直感的な名前も罠になりうる——`npm install openmct@stable`のように、dist-tag名を明示して確認するのが確実。** また`latest`タグ（`4.3.1`）は、CDN側で複数プロジェクトが長期間rc扱いだと思っていた`4.3.0`系より新しい正式版が既に出ていたことも意味する——sas0・mapterhorn-monitorとも、次回のバージョン再確認時にはこの`4.3.1`を候補に入れる価値がある。

**暫定的な指針**：

1. CDN経由・低ステークスなら、RCを含む最新を追ってよい。ただし必ずバージョンの実在確認（`curl -sI`）をしてから固定し、定期的な再確認（sas0のD45パターン、週次CI等）を組み込む。
2. npm経由・運用に組み込まれる高ステークスなら、最後の安定版に固定し、`package.json`でロックする。
3. どちらでも、上記のブートストラップの落とし穴（SharedWorker・`'start'`イベント・Plot/Telemetryの制約）は、バージョンに関わらず共通のチェックリストに入れる。

## 未解決の論点

- Plot APIの配列順バグ（domain/rangeの並び）は特定・修正済みだが、それでも「最小構成では描画されず、フルアプリでは描画される」という食い違いが残っている——バージョン依存ではなく、アプリ構造（root直下か子オブジェクトか、他プラグインの有無、subscribeの実動作有無等）が影響している可能性が高い。原因未特定。
- `openmct.on('start', ...)`の信頼性が、バージョン依存かmapterhorn-monitor固有の環境要因かも未確定。
- マルチモニタ環境でのフルスクリーン挙動は3プロジェクトとも未検証。

## Open MCTの強み — dwg7がこれを使い続けることで何を得たいか

ここまでの節は落とし穴・未解決の論点が中心になったが、3プロジェクトとも、それでもOpen MCTを使い続けている。何がそれだけの価値を持っているのかを、意識的に言葉にしておく。これはツールの採点ではなく、**dwg7がOpen MCTを選び続けることで何を得ようとしているのか**を明らかにする作業でもある。

- **「異種混在の情報源を1人の運用者が次々切り替えて見る」という形に、骨格そのものが合っている**。Object API・Composition API・View API——「データが何か」「それがどう組織されているか」「それがどう表示されるか」を分離するこの三層構造（sas0 DECISIONS.md D16）のおかげで、sas0は天気図・警報・地震・火山・観測点データ・179市町村のリンクまで、性質の異なる20以上の情報源を、ナビゲーションを自作することなく1本のツリーに収められた。新しい情報源を足すのは「リーフをもう1つ登録する」だけで、構造そのものを変える必要がない——v0のたった2計器から始まって、この形のまま素直にスケールした。
- **「1つクリックして、フルスクリーンで見て、次をクリックする」という運用者の実際の使い方に、ツリー＋ブラウズバー＋Inspectorという標準UIがそのまま応える**。sas0は当初これを抑え込んでヘッドレスで独自UIを作ろうとして失敗し（D5）、Open MCT標準のchromeを受け入れてから初めてうまく回り出した——「消したいノイズ」だと思っていたものが、実は運用者が最初から欲しがっていた形そのものだった。
- **Providerパターンの拡張点は、独立した3つの実装が寸分違わず同じ結論に達するほど安定している**——`objects.addProvider` + `composition.addProvider` + カスタムビュー/テレメトリプロバイダの組み合わせ。これにより、Open MCT本体の込み入った実装に一切触れずに、描画は完全に自前のDOM/SVG/Canvasで書きながら、ナビゲーション・ツリー・chromeだけをOpen MCTから借りる、という理想的な分業ができる。
- **Inspectorのようなイディオム自体が、API を使わなくても借りる価値がある**。sas0は状況図のホバー情報を、Open MCT純正のInspectorプラグインではなく、「固定ペインに詳細を出す、浮動チップにしない」というInspectorの語彙だけを借りて自前実装した（D29）。UIパターンそのものが、コードより先に価値を持っている例。
- **見た目が最初から「本気の監視ツール」に見える**。Espressoテーマは外部公開用には大幅な上書きが要る（本ドキュメント既述）が、それでも初期状態から「マーケティング用のダッシュボードではなく、運用のための計器盤」という空気をまとっている——一般的なWebフレームワークのデフォルトテーマでは得られない、ただ乗りできる資産。
- **この文書自体が、最大の実証になっている**。sas0（防災ダッシュボード）・mapterhorn-monitor（生産パイプライン監視）・claude-mct（ライブセッションのテレメトリ）という、用途も規模も全く異なる3つのアプリケーションが、同じ基盤に乗っているというだけで、バグの原因を突き合わせ、パターン（キオスクモードのCSS技法等）を再利用し、互いのD53を裏付け合うことができた。共通基盤を選ぶという決定そのものが、後から思わぬ形で協働を可能にする——これがまさに実演された。

**dwg7が得ているもの**：これはD16で既に述べた通り、NASAが実際の高ステークスな有人・無人ミッション運用のために作った枠組みが、そのコアを一切変えずに、草の根の市民向け防災情報コンソールにも機能するという実証そのものである。「keep web maps open for a better world」というスローガンを、実際に動くコードで示すこと。今回の3プロジェクト間の協働は、その実証をさらに一歩進めた——同じ基盤を選んだ複数の独立プロジェクトが、知見を共有し、互いのバグを直し合えるという、開発体験そのもののレベルでの相互運用性が確認できた。

## 由来

このドキュメントは、mapterhorn-japan-bridge/mapterhorn-monitorが自分たちの実地知見をまとめた草案（`mapterhorn-japan-bridge` DECISIONS.md D91の増強として作成）から始まり、claude-mctの独立した知見を統合したv2を経て、sas0が「dwg7内でのOpen MCT使用のフラッグシップ」という位置づけからマスター管理を引き継いだ（sas0 DECISIONS.md D65）。

2026-09-02、hfuさんの依頼により、sas0からcafebabe(`dwg7/cafebabe`)へマスター管理を移管した。sas0・mapterhorn-japan-bridge・claude-mctの3リポジトリからは、このファイルへのリンクのみを保持する形に変更。今後の更新はこのファイルに対する変更として行う。

最終更新：2026-09-01(sas0時代)、2026-09-02 cafebabeへ移管
