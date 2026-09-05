# 地理空間コミュニティ向けのオープンIDとしてOSM OAuthを使う

**状態**: 探索中(dwg7内に実装実績なし)
**出典**: hfuさん、2026-08-25、[UNopenGIS/7#980](https://github.com/UNopenGIS/7/issues/980)
(#979からの継続)

**動機・背景(Why)**

将来のCSS(Chat Context Sharing)やSAS Console(Situational Awareness as a Service
Console、`sas0 → sas1 → SAS Console → CSS`というロードマップ上)で、「誰が発言したかを
緩やかに共有する」ための軽量なアイデンティティ基盤が必要になる可能性がある。厳格な本人確認・
組織管理・シングルサインオンは目的ではない。

GitHub/Google/Microsoft OAuthはそれぞれ開発者向け・一般利用者向け・組織利用者向けという
印象がある一方、OpenStreetMapアカウントは既に世界中の地理空間コミュニティ(OSMマッパー、
HOTボランティア、Missing Maps参加者、FOSS4G参加者、UN Open GIS関係者)に広く普及している。
これを「地理空間コミュニティ向けのオープンID」として転用できないか、というのが提起の骨子。

**`DWG7-CONTEXT.md`の「keep open」評価軸との整合性が高い**——特定のプラットフォーム・組織
(大手IT企業)への依存を避け、地理空間コミュニティが既に共有する基盤を再利用するという発想は、
dwg7らしい判断とよく合致する(2026-09-06、cafebabeの分析)。

**未解決の問い(Open Questions)**

- コミュニティ・ポリシー面: OSM OAuthを地図編集以外の用途に使うことは、OSMコミュニティから
  見て適切か。避けるべき利用形態はあるか。「OSM OAuthによる認証」と「OpenStreetMap
  Foundationによる保証」の区別をどう明確に保つか——**これはdwg7内部の技術知見では答えられず、
  hfuさん自身がOSMコミュニティと直接対話して確かめる必要がある論点**(cafebabeの分析範囲外)
- 技術面: Hono + Cloudflare Pages/Workers + OSM OAuthというPoC構成の実装実績・参考事例
- 取得すべき情報の範囲(ユーザーID・表示名・プロフィールURL程度で十分か)

**関連(Related)**

- [`DWG7-CONTEXT.md`](../DWG7-CONTEXT.md)の「keep open」評価軸
- Cloudflare Workers/Pagesの技術的制約について、`patterns/`にはまだ知見が無い。近い実例として
  `/Users/hfu/faceless-cartographer`リポジトリのDECISIONS.md(D9/D10)に、Cloudflare Workers
  デプロイを検討し「LLM呼び出しがCLIサブプロセス依存のため`child_process`が使えないエッジ
  ランタイムとは非互換」という理由で見送った記録がある(ただしこれを書いたセッションの現在の
  所在は2026-09-06時点で確認できていない——
  [`patterns/agent-repository-boundaries.md`](../patterns/agent-repository-boundaries.md)
  参照)。OAuth固有の知見ではないが、将来このPoCがサブプロセス依存の機能と同居する設計になる
  場合は再考の価値がある

**進捗ログ(Log、追記専用)**

- 2026-09-06: cafebabeがissueを分析。dwg7内にOSM OAuth(または何らかのOAuth)の実装実績を
  持つプロジェクトは見つからず。`patterns/`に書くには実例が無く早いと判断し、hfuさんの提案で
  `ideas/`ディレクトリを新設してここに記録することにした
