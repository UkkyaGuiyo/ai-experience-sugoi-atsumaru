# Collection Policy

保存対象はAIを利用した経験から一般化した、再利用可能な知識。成功、失敗、実験、改善、パターン、アンチパターン、prompt技法、tool利用、agent運用、協調、Human-in-the-loopを扱う。

生データをRepositoryへ取り込まず、Experience → Analysis → Generalization → Reusable Knowledgeの順で知見へ変換する。人物・組織・固有案件を除いて成立する内容のみを残す。収集量、会話の忠実な再現、詳細さよりPrivacy/Safetyを優先する。

Coding専用ではない。task_typeは拡張可能な分野名として、Coding、Software Engineering、Research、Writing、Creative Work、Image Generation、Audio、Office Work、Data Analysis、Education、Agent Operations、Sub-agent Operations、Computer Use、RAG、MCP / Tool Integration、Local LLM、Multi-agent Systems、Human-AI Collaboration、Prompting、Verification、Safety、Workflow Automation等を扱える。新分野でも識別情報を分類名に使わない。

Entry作成前のSafety Review、Schema検査、automated scan、unit tests、独立レビューを必須とする。Automated validation != privacy guarantee。判断に迷う情報は保存しない。

初期構築では実在人物・既存会話・既存Project由来のEntryを作らない。sampleが必要なら完全な架空データのみ。テストの危険候補も合成値を動的に作成し、実secretは使わない。過去データの自動収集・自動移植は許可しない。
