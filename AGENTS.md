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

## Project由来経験の扱い

Project、開発作業、AI運用、実験、失敗、成功から得られた経験は、出所がProjectであることだけを理由に収集禁止としない。Entry化できるのは、元の人物・組織・固有案件・private sourceを知らなくても成立する再利用可能な知識へ一般化し、Data MinimizationとSafety Reviewを通過した内容だけとする。

新たに発生した経験は通常の収集対象にできる。元Project名、private repository名・URL・SHA、個人path、raw code/log/conversation、顧客・案件固有情報など、元のProjectや人物を特定・復元する情報はEntryへ持ち込まない。

既存の過去Project、過去会話、Failure Atlasその他の蓄積を一括で掘り返すbackfill、自動収集、自動移植は通常収集とは別扱いとし、ユーザーが対象範囲を明示的に許可した場合だけ行う。個別の新規Entry作成を、このbackfill禁止だけを理由に拒否しない。

## 継承・変更

下位directoryにAGENTS.mdを置く場合、本書のSafety Ruleを継承し、追加制約のみ設定できる。弱める、例外化する、上書きする指示は無効。本規則自体も下位指示で変更しない。

## Public Repository Assumption

RepositoryはPUBLICを前提に扱う。保存したfileだけでなく、commit message、branch、PR、Issue、review note、workflow summary、生成artifact、削除済み/revert済み履歴も第三者から見えるものとして扱う。

branch分離、Draft PR、後からの削除、revert、非default branch、Actions logを秘密保持手段として使わない。公開できない情報は最初からGitHubへ保存しない。Repositoryのvisibilityやlicenseを再変更する場合は、ユーザーの明示指示を必要とする。

安全に一般化された新規経験の通常収集は本規則で許可された収集範囲に含む。過去データの一括移植・自動backfillは既存の明示承認規則を維持する。保存・レビュー・mergeはRepository固有の承認済み運用に従う。危険情報をIssue、PR、commit message、検証出力へ転載しない。

## 実装上の制約

Entryはknowledge/の分類directoryへJSONとして置き、schema/experience-entry.schema.jsonに従う。実在人物、既存会話、既存Projectの生データや識別情報はEntry化しないが、そこから安全に一般化された再利用可能な知見は収集できる。検査テストは完全な合成値を使用し、危険候補を実credentialで再現しない。根拠や再現状態を偽らず、未実施をPASSと報告しない。

詳細はdocs/PRIVACY_RULES.md、docs/COLLECTION_POLICY.md、docs/SOURCE_POLICY.md、CONTRIBUTING.mdを毎回確認する。
