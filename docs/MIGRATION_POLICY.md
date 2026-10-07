# Migration Policy

Migrationは、既存Failure Atlas、過去Project、過去会話、既存の知識庫など、すでに蓄積された過去データを後から取り込む作業を指す。進行中の作業から新たに発生した経験を、その都度安全に一般化してKnowledge Entryへ保存する通常収集とは区別する。

既存Failure Atlas等はMigration Sourceになり得るが、無差別な自動コピー、一括backfill、全文転記、raw conversationやraw logの保存をしない。Migrationはユーザーが対象範囲を明示的に許可した場合だけ実施する。

許可された移行は1件ずつ次の手順で行う。

1. Repositoryへraw sourceを置かず、再利用可能な知見を抽出する。
2. 人物・組織・固有案件・非公開Repository・private sourceの識別情報を除去し、条件の組み合わせによる再識別も確認する。
3. 権利・利用条件・契約・法令・秘密・必要最小性について、ファイル作成前にSafety Reviewする。
4. 安全に一般化できる内容だけ新Schemaへ変換する。安全性が不明なら移行しない。
5. Validator、unit tests、独立レビューを通し、承認済み運用で保存する。

元の人物ID、固有案件名、非公開URL、private repository識別子、会話本文を追跡のために残さない。重複確認は安全な知識IDと一般化した内容で行う。Failureだけでなく成功・実験・改善も同じSafety Ruleを適用する。

通常収集の新規経験はMigration許可を待つ必要はない。ただし、過去データを広く探索・再処理してEntry候補を掘り起こす場合はMigrationとして扱う。

情報を失うことを理由に危険情報を残さない。Automated validation != privacy guarantee。
