# ローカル開発・スクリプトの落とし穴

ローカル開発環境やシェルスクリプトの、環境依存で気づきにくい落とし穴について。
2026-09-02、全エージェントへの自由知見募集(D6)より。

---

## JSON部分編集は「読み込み→書き出し」ではなく行単位の手術で

**タグ**: 一般則

**状況(Context)**
大きな設定ファイル(MapLibreスタイルJSON等)の一部だけを、Pythonの`json.load`/`json.dump`で
変更する場面。

**問題/対立する力(Problem / Forces)**
`json.load`→`json.dump(indent=2)`は、触っていない箇所まで再フォーマットしてしまう
(コンパクトな1行配列が9行に展開される等)。意図した変更の何倍もの無関係な差分が出て、
レビューが困難になる。

**解決(Solution)**
パーサーの正規化力を信用せず、`readlines()`+行番号指定+「期待値と一致することをassertして
から置換」するヘルパーで、行単位の最小差分になるよう書き換える。

**実例(Known uses)**
- `kitavolca` — MapLibreスタイルJSONの一部変更で意図の3倍近い無関係な差分が出たため、
  `git checkout --`で一旦破棄し、行単位の置換ヘルパーに書き直した
  ([コミット2dc4523](https://github.com/hfu/kitavolca/commit/2dc4523))

---

## `python3 -m http.server`でのローカル動作確認は、ブラウザキャッシュに騙される

**タグ**: 一般則

**状況(Context)**
`python3 -m http.server`のような簡易サーバーでフロントエンドの動作確認をする場面。

**問題/対立する力(Problem / Forces)**
`Cache-Control`ヘッダを送らないため、ブラウザのヒューリスティックキャッシュが古いJSファイル
を配信し続けることがある。しかも通常のハードリロードや新規タブでも治らない(プロファイル
共有キャッシュのため)、「コードは直したのに挙動が変わらない」という分かりにくい状態になる。

**解決(Solution)**
ポート番号を変えて新しいキャッシュ名前空間に逃げるのが手っ取り早い回避策。

**実例(Known uses)**
- `kitavolca` — この現象に遭遇し、ポート変更で解決

---

## macOS標準のbash 3.2に`declare -A`(連想配列)は無い

**タグ**: 一般則

**状況(Context)**
シェルスクリプトをmacOSで実行する場面。

**問題/対立する力(Problem / Forces)**
GNU bash 4+前提のスクリプト(`declare -A`等)は、macOS標準シェル(bash 3.2)では動かない。

**解決(Solution)**
移植性を優先するなら`case`文で代替する。

**実例(Known uses)**
- `kitavolca` — `scripts/fetch-vlcm.sh`で`case`文による代替を採用

---

## 非UTF-8シェルロケールは、`grep`が日本語を文字境界の途中で欠けさせることがある

**タグ**: 一般則

**状況(Context)**
日本語URLやテキストを含むファイルを、シェルスクリプトで`grep`スキャンする場面。

**問題/対立する力(Problem / Forces)**
シェルの`LANG`が未設定(`LC_CTYPE=C`)だと、`grep -o`が日本語URLを文字境界の途中で欠けさせ、
意味不明な偽陽性(文字化けした一致)を生む。CI環境(GitHub Actions等)は元々UTF-8ロケールの
ことが多く実害が出にくいため、ローカルで手動実行する人だけが同じ罠に落ちる可能性がある。

**解決(Solution)**
`export LC_ALL=en_US.UTF-8`をスクリプト冒頭に置く。

**実例(Known uses)**
- `sas0` — `scripts/check-links.sh`で日本語URLが途中で欠ける偽陽性に遭遇
  ([Issue #4](https://github.com/dwg7/sas0/issues/4)、DECISIONS.md D68)

---

## macOSでSSH経由の外部ボリュームアクセスが`Operation not permitted`になるのはTCC、Full Disk Accessは`sshd`本体ではなく`sshd-keygen-wrapper`に付与する

**タグ**: 一般則

**状況(Context)**
macOSで、Remote Login(SSH)を有効化したMacに外付けドライブ(USB/Thunderbolt)を接続し、
SSHセッションからそのボリューム(`/Volumes/`配下)にアクセスする場面。

**問題/対立する力(Problem / Forces)**
FinderやTerminal.app(GUIアプリ)からは普通にアクセスできるのに、SSH経由では
`ls: /Volumes/X: Operation not permitted`のように拒否される。エラー文言が`Permission
denied`(Unixパーミッション)ではなく`Operation not permitted`である点が手がかりで、これは
macOSのTCC(プライバシー保護、リムーバブルボリュームへのアクセス制御)による拒否の
シグネチャ。GUIアプリはアクセス許可ダイアログを表示して承認を得られるが、SSH経由の
ヘッドレスセッションにはそのダイアログを出す経路が無いため、常に拒否され続ける。

**解決(Solution)**
System Settings → Privacy & Security → Full Disk Access で許可を付与するが、
**`/usr/sbin/sshd`本体に付与しても効かないことがある**。実際にSSHセッションのシェルを
起動しているのは`/usr/libexec/sshd-keygen-wrapper`であり、Full Disk Accessは**こちらに**
付与する必要がある(Finderのファイル選択では出てこないので、ダイアログ内で
`Cmd+Shift+G`を押しパスを直接入力して追加する)。付与後は既存のSSHセッションでは反映
されないため、一度切断して再接続する。

**実例(Known uses)**
- `slate`(hfuさんの個人マシン、mapterhorn-japan-bridge等の生データ保管先) —
  `/Volumes/Migrate-2025-04`・`/Volumes/pmtiles-store`へのSSH経由アクセスが
  `Operation not permitted`になっていたが、`/usr/libexec/sshd-keygen-wrapper`に
  Full Disk Accessを付与したところ解決した(2026-09-12)

---

## フリート運用でのローカル開発サーバーのポート衝突は、拒否されるだけでは終わらない——「別プロジェクトのサーバーを自分のものと誤認する」方が怖い

**タグ**: 一般則

**状況(Context)**
複数のClaude Codeセッションが同一マシン上で並行稼働するフリート運用で、各セッションが
固定ポートでローカル開発サーバーを起動する場面。

**問題/対立する力(Problem / Forces)**
ポート番号が別セッションのサーバーと衝突し、起動自体が拒否されるのは安全側の失敗
(気づきやすい)。しかし拒否された状態のまま`curl http://localhost:<port>/...`のような
検証を行うと、**既に起動している別プロジェクトのサーバーが200を返してしまう**。ブラウザで
開けば「表示はされるが自分の変更が全く反映されない」という、原因が分かりにくい形で
時間を失う。

**解決(Solution)**
プロジェクトごとにポート番号を変える(固定の既定値に頼らない)。検証の最初に、自分の変更に
固有の文字列がレスポンスに含まれているかを確認する一手間を入れる——含まれていなければ、
自分のサーバーではなく別プロジェクトのサーバーを見ている可能性を疑う。

**実例(Known uses)**
- `tabularmaps/do` — `.claude/launch.json`のポート8765番が別セッションのサーバーで
  使用中となり`preview_start`が拒否された。その状態で`curl`すると別プロジェクトの
  ファイルが200で返っていた。`grep -c`で自分の変更の痕跡が0件と出たことで気づき、
  ポートを8766に変更して解決した(2026-09-19)

---

## ローカル開発サーバーのアクセスログを潰さない

**タグ**: 一般則

**状況(Context)**
エージェントがブラウザを直接見られない状態で、ローカル配信したフロントエンドを人間に
確認してもらいながらデバッグする場面。

**問題/対立する力(Problem / Forces)**
`SimpleHTTPRequestHandler`の`log_message`を握り潰した静かなサーバーを書きたくなる
(出力が邪魔なので)。しかしブラウザが見えない側にとって、**サーバーのアクセスログは
唯一の客観的な証拠**になる。特に「何が要求され、何が404になったか」は、コンソールにも
`map.on('error')`にも出てこない失敗を一発で暴く。

ログが無いと、ブラウザ側の状態(コンソール・DOM・API)だけで推論することになり、
**沈黙する失敗**(要求はされたがファイルが無い、等)に対して何往復も空振りする。

**解決(Solution)**
開発用サーバーではアクセスログを必ず出す。時刻・クライアント・リクエスト行・ステータス。

```python
def log_message(self, fmt, *args):
    sys.stderr.write("%s  %s  %s\n" % (
        time.strftime("%H:%M:%S"), self.address_string(), fmt % args))
    sys.stderr.flush()
```

ログをファイルに落としておけば、人間に「リロードして」と頼んだ後、エージェント側が
自分で読める。**人間にコンソールを転記してもらうより、サーバーログの方が早く確実**。

あわせて、`Cache-Control: no-store`(古いJSを掴ませない)と`Range`対応(PMTiles等は
Rangeが無いと読めない。`SimpleHTTPRequestHandler`は標準では応答しない)も入れておくと、
開発中の事故が一通り塞がる。

**実例(Known uses)**
- `doverture` — MapLibre のワーカーが404になる問題を、コンソールとページ内自己診断だけで
  6往復追って特定できなかった。アクセスログを有効にした**次の1回**で
  `GET /spatialid/assets/maplibre-gl-worker.mjs 404`が出て即座に確定した(2026-09-20)
