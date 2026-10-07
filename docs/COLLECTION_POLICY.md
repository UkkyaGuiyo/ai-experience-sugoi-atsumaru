# Collection Policy

保存対象はAIを利用した経験から一般化した、再利用可能な知識。成功、失敗、実験、改善、パターン、アンチパターン、prompt技法、tool利用、agent運用、協調、Human-in-the-loopを扱う。

生データをRepositoryへ取り込まず、Experience → Analysis → Generalization → Reusable Knowledgeの順で知見へ変換する。人物・組織・固有案件を除いて成立する内容のみを残す。収集量、会話の忠実な再現、詳細さよりPrivacy/Safetyを優先する。

Coding専用ではない。task_typeは拡張可能な分野名として、Coding、Software Engineering、Research、Writing、Creative Work、Image Generation、Audio、Office Work、Data Analysis、Education、Agent Operations、Sub-agent Operations、Computer Use、RAG、MCP / Tool Integration、Local LLM、Multi-agent Systems、Human-AI Collaboration、Prompting、Verification、Safety、Workflow Automation等を扱える。新分野でも識別情報を分類名に使わない。

## Project由来の経験

既存または進行中のProject、開発作業、AI運用、実験から得られた経験は、それがProject由来であること自体を収集拒否理由にしない。通常収集できるのは、元Projectの識別情報やprivate dataを除去しても成立し、第三者へ内容を開示しても人物・組織・固有案件・private sourceを特定または復元できない再利用可能な知識へ一般化されたものだけとする。

Project名、private repository名・URL・SHA、個人path、raw conversation、raw log、raw code、credentials、顧客・案件固有情報、権利上再配布できない内容はKnowledge Entryへ移さない。必要な技術条件は安全な粒度へ一般化する。

新たに発生した経験は通常の収集フローでEntry化できる。過去Project・過去会話・既存知識庫を対象にした一括backfill、自動収集、自動移植は別のMigration作業であり、対象範囲についてユーザーの明示許可を必要とする。個別の新規経験を、このbackfill制限だけで拒否しない。

Entry作成前のSafety Review、Schema検査、automated scan、unit tests、独立レビューを必須とする。Automated validation != privacy guarantee。判断に迷う情報は保存しない。

sampleが必要なら完全な架空データのみを使う。テストの危険候補も合成値を動的に作成し、実secretは使わない。
