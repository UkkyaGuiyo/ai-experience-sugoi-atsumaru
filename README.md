# AIの経験がスゴーイアツマール

AIの使い方、成功、失敗、事故、工夫、妙に上手くいった方法まで。AIの経験をスゴーイアツメる、再利用可能な実践知の知識ベースです。

> **人を集めるな。経験を集めろ。**
>
> **個人情報・個人特定可能情報・機密情報・法的問題につながる情報は収集しない。例外はありません。**

収集対象はExperience → Analysis → Generalization → Reusable Knowledge。人や会話のアーカイブではなく、成功・失敗・実験・改善・運用パターン・アンチパターンを扱います。Failureは知識の一分類です。

## 最初に読む

- [AI運用規則](AGENTS.md)
- [Privacy Rules](docs/PRIVACY_RULES.md) / [Collection Policy](docs/COLLECTION_POLICY.md) / [Source Policy](docs/SOURCE_POLICY.md)
- [Knowledge Model](docs/KNOWLEDGE_MODEL.md) / [Agent Operations](docs/AGENT_OPERATIONS.md)
- [Contribution手順](CONTRIBUTING.md) / [Entry template](templates/EXPERIENCE_ENTRY.md)
- [Migration Policy](docs/MIGRATION_POLICY.md) / [Security](SECURITY.md)

## 保存と検証

knowledge/内の分類directoryに、Schemaに従うJSON Entryを保存します。観測時期、Model、tool version、一般化した環境、再現状態により適用範囲を限定します。古い知見はHistorical Knowledgeとして扱い、永遠の真理としません。

```sh
python scripts/validate_knowledge.py
python -m unittest discover -s tests -v
```

GitHub Actionsでもschema validation、automated safety scan、unit testsを実行します。**Automated validation != privacy guarantee**。PASSしても識別可能性・秘密・権利・契約・法令について独立したSafety Reviewが必要です。

## 現在の状態

初期構築の器です。実データはまだ投入していません。既存Failure Atlasからの移植は行っていません。初期状態はPRIVATEで、ユーザーの明示指示なしに公開しません。LICENSEは未設定で、自由な再配布を許諾していません。
