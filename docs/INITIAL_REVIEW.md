# 初期構築のSafety Review

## 対象と確認

初期構築のコード、Schema、CI、運用規則、Contribution手順を独立GPT6.1 SOL Reviewerが確認した。Knowledge Entryは0件であり、実在人物・既存会話・既存Project由来の知識、sample、生会話、生ログ、認証情報、移植データを投入していない。LICENSEは未設定。

## 指摘と修正

- JSON Unicode escapeによる検査回避を、デコード後のkey/string/assignmentの検査で修正。
- cache directoryの一括除外を撤廃し、bytecodeを生成しない実行手順とCI設定に変更。
- 不正なSchema keyword値が制約を弱める問題を、Schema定義の厳格な検査で修正。
- 不正な出典URL portを拒否する検証を追加。

合成値の回帰テストで上記を確認した。検査診断は候補内容を表示しない。検査器はroot .git以外を対象とし、読取不能、binary、リンク、不正JSONを黙って除外しない。

## 限界と今後

**Automated validation != privacy guarantee**。再識別可能な情報の組合せ、自然言語に含まれる個人・機密・権利上の問題は機械検査だけでは保証できない。Entry作成前のSafety Reviewと独立レビューを継続する。

将来は機械検査の検出範囲・誤検出の改善、分類・検索・Historical Knowledgeの再検証支援を検討する。実データ投入、外部情報収集、自動移植、公開範囲の拡大はこの初期構築に含まれない。
