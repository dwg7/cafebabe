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
