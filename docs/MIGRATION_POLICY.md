# Migration Policy

既存Failure Atlas等は将来のMigration Sourceになり得るが、今回の初期構築では内容を移植しない。自動コピー、全文転記、raw conversationやraw logの保存をしない。

将来の移行は明示された許可と対象範囲の下で、1件ずつ次の手順で行う。

1. Repositoryへraw sourceを置かず、再利用可能な知見を抽出する。
2. 人物・組織・固有案件・非公開Repository・private sourceの識別情報を除去し、条件の組み合わせによる再識別も確認する。
3. 権利・利用条件・契約・法令・秘密・必要最小性について、ファイル作成前にSafety Reviewする。
4. 安全に一般化できる内容だけ新Schemaへ変換する。安全性が不明なら移行しない。
5. Validator、unit tests、独立レビューを通し、承認済み運用で保存する。

元の人物ID、固有案件名、非公開URL、会話本文を追跡のために残さない。重複確認は安全な知識IDと一般化した内容で行う。Failureだけでなく成功・実験・改善も同じSafety Ruleを適用する。

情報を失うことを理由に危険情報を残さない。Automated validation != privacy guarantee。
