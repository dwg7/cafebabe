# Open MCT — 運用面の落とし穴(ブートストラップ・キオスクモード・デバッグ・バージョン選択)

`patterns/open-mct.md`の一部として運用。全体像・寄稿プロジェクトの一覧はそちらを参照。

## ブートストラップの落とし穴

- **CDNバージョン固定**：存在しないバージョンを指定すると、エラーも出ずに真っ白な画面になる（sas0はかつて`3.3.0`で被弾）。`docs/dist/openmct.js`と`docs/dist/espressoTheme.css`（`openmct.css`ではない——3.x→4.x系のどこかで名前が変わった）の両方が実在するか、`curl -sI`で確認してから固定する。〔sas0〕
- **`SharedWorker`のクロスオリジン/初期化エラー——症状は同じでも原因は2系統ある**：
  - 原因A（CDN経由）：Open MCT内蔵の検索インデクサがSharedWorkerを自分のCDNオリジンから起動しようとしてブラウザにブロックされる。`window.SharedWorker = undefined`を先に設定し、Open MCT組み込みの同期フォールバック（元々iOS向け）に倒すのが対策。〔sas0、mapterhorn-monitor〕
  - 原因B（npm自前ホスティング）：`openmct.setAssetPath()`を`install()`より前に設定していないと、ワーカースクリプトの相対パス解決が失敗し、SPAフォールバックがHTMLを返してパースエラー（`Unexpected token '<'`）になる。`openmct.setAssetPath('/node_modules/openmct/dist/')`を先に呼ぶことで解消。〔claude-mct〕
  - 同じ"Error with InMemorySearch worker"系の症状でも、構成によって原因が異なる。両方をチェックリストに入れる。
- **`openmct.start()`のセレクタ文字列対応**：4.3系では`openmct.start('#app')`のようにCSSセレクタ文字列を渡せる。ドキュメントがまだ読み込み中なら`DOMContentLoaded`まで自動的に待つ。`document.getElementById(...)`を渡す旧形式より扱いやすい。〔sas0〕
- **`openmct.on('start', callback)`の信頼性——プロジェクト間で結果が割れている（未解決）**：
  - sas0（4.3.0-rc1、CDN）：確実に発火する。本番コードがこれに依存して動いている。
  - mapterhorn-monitor（同じく4.3.0-rc1、CDN、同じ「リスナーを`start()`より先に登録」という順序）：**一度も発火しない**。登録順序の違いという仮説は、両者が同じ順序だったため否定された。手がかりは、起動時に一貫して発生する`Uncaught (in promise) TypeError: Cannot read properties of undefined (reading 'key')`という未処理のPromise rejectionで、これが`'start'`のemit前に非同期チェーンを中断させている可能性がある（未確定）。
  - claude-mct（4.2.0、npm）：このイベントに依存しない設計のため未検証。
  - **現状の結論**：バージョン・環境依存で、原因は特定できていない（この信頼性の食い違いがバージョン依存かmapterhorn-monitor固有の環境要因かも未確定）。対策としては、リスナーは`start()`より先に登録した上で、**初期化処理をイベント経由だけに頼らず、`openmct.start()`の直後に直接（同期的に）書く**フォールバックを持たせるのが安全。
- **起動時の無害なコンソールエラー**：`Uncaught (in promise) TypeError: Cannot read properties of undefined (reading 'key')`が1回だけ出ることがある。ローカル検索インデクサの既知の癖で、再現性はあるが実害はない（tree navigation・Inspector等は正常動作）。新しいバグと誤認しないよう記録。〔sas0〕

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
3. どちらでも、上記のブートストラップの落とし穴（SharedWorker・`'start'`イベント・Plot/Telemetryの制約は`patterns/open-mct-telemetry.md`参照）は、バージョンに関わらず共通のチェックリストに入れる。
