# Agent Operations

AIはroot AGENTS.mdとCollection/Privacy/Source Policyを最初に読む。何を載せるか、どう載せるかはこのRepositoryの規則を参照する。生会話を知識Entryへ貼り付けることは収集ではない。

作業担当は一般化とData Minimizationを行い、Entry作成前にSafety Reviewを実施する。不明な情報は保存しない。個人や元Projectを識別する情報を、根拠・レビュー・handoff・commit messageへ漏らさない。

実装担当と独立Reviewerを分ける。ReviewerはPrivacy/Security、Schemaとの整合、根拠と再現性、CI、AI指示、将来拡張性を確認する。指摘の修正後に検査を再実行し、未実施の検証を合格としない。

複数agentは独立したファイル範囲のみ分業し、共有ファイルの統合担当を一人にする。安全性が不明なデータをagent間で再配布しない。通常の承認範囲で継続するが、Safety gateや明示停止を勝手に解除しない。

Validatorは第一防衛線。Automated validation != privacy guarantee。PASSをもって収集許可、公開許可、merge許可と解釈しない。下位AGENTSはroot Safety Ruleを継承し追加制約だけを設定する。
