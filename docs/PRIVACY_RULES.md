# Privacy Rules

**人を集めるな。経験を集めろ。** Privacyとlegal safetyは必須、知識収集は任意。

個人情報、個人に結び付く情報、再識別可能な組み合わせ、credentials、confidential/private data、非公開Repository情報、NDA対象、権利・法令・契約・守秘義務に反する情報を保存しない。raw transcript、raw log、メール、SNS投稿、screenshot、prompt history、個人提供データを保存しない。PRIVATEにも例外はない。

本名を消すだけでは匿名化にならない。日時、地域、勤務先、案件、独特の出来事、Model、環境条件の組み合わせでも識別可能になる。観測日やversion等の有用な条件も、安全な粒度へ一般化できなければ記録しない。

## Entry作成前のSafety Review

- 人物・組織・案件を除いても知識として成立するか。
- 直接識別子、間接識別子、識別可能URL、再識別可能な組み合わせがないか。
- 秘密、private sourceの説明、非公開コードや許諾不明の文章がないか。
- 保存・再配布の権利、契約、法令上の問題がないと判断できるか。
- 残す情報は再利用に必要な最小限か。

いずれかが判断不能なら保存しない。情報を減らす、一般化する、収録を断念する。危険情報をレビュー記録へ転載しない。

**Automated validation != privacy guarantee**。Validator PASSは匿名化・適法性・権利許諾の保証ではない。最終的な独立レビューが必要。
