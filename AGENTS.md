# AI向け最上位運用規則

このRepository内のすべての作業で本規則を守る。Knowledge Collection is optional. Privacy and legal safety are mandatory.

**人を集めるな。経験を集めろ。**

## 絶対条件

- 個人情報、個人に結び付く情報、再識別可能な情報の組み合わせを保存しない。本名、識別可能なhandle、連絡先、位置、IP、識別番号、個人URL、勤務先、固有案件名なども含む。
- credentials、API key、access token、cookie、password、private key、secretを保存しない。
- confidential data、private data、非公開Repository情報、社外秘、NDA対象、未公開企業情報を保存しない。
- raw transcript、raw log、会話全文、メール全文、prompt history、screenshot、個人提供データを保存しない。
- 保存・公開・再配布により法令、権利、契約、守秘義務上の問題が生じる情報や、再配布許可のないコードを保存しない。
- 例外を作らない。名前を消すだけでは匿名化ではない。人物・組織・固有案件を除いても成立する経験へ変換する。

## 作業順序

1. Generalization First: 生データをRepositoryへ置かず、再利用可能な経験へ一般化する。
2. Data Minimization: 必要最小限の条件・観測・教訓だけ残す。
3. Knowledge Entry作成前にSafety Reviewを行う。識別、再識別、秘密、権利、契約、法令、出典の安全性を確認する。
4. When in doubt, do not store: 判断不能な情報は保存しない。推測で安全と認定しない。
5. Validatorとtestsを実行し、独立したReviewerの確認を受ける。検査の回避や一般的な除外規則の追加で危険候補を隠さない。

**Automated validation != privacy guarantee**。機械検査PASSは安全性、適法性、権利許諾、匿名化の保証ではない。収集よりSafetyを優先し、知識を1件失うことより危険情報を残すことを重大な失敗とする。

## 継承・変更

下位directoryにAGENTS.mdを置く場合、本書のSafety Ruleを継承し、追加制約のみ設定できる。弱める、例外化する、上書きする指示は無効。本規則自体も下位指示で変更しない。

RepositoryはPRIVATEを維持する。ユーザーの明示指示なしにPUBLIC化、LICENSE決定、既存データ移植、収集範囲拡大をしない。保存・レビュー・mergeはRepository固有の承認済み運用に従う。危険情報をIssue、PR、commit message、検証出力へ転載しない。

## 実装上の制約

Entryはknowledge/の分類directoryへJSONとして置き、schema/experience-entry.schema.jsonに従う。今回の初期構築では実在人物、既存会話、既存Project由来のEntryを作らない。検査テストは完全な合成値を使用し、危険候補を実credentialで再現しない。根拠や再現状態を偽らず、未実施をPASSと報告しない。

詳細はdocs/PRIVACY_RULES.md、docs/COLLECTION_POLICY.md、docs/SOURCE_POLICY.md、CONTRIBUTING.mdを毎回確認する。
