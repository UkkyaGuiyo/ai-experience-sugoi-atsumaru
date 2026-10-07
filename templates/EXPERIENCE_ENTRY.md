# Experience Entry記入ガイド

これは記入手順であり、生データや実際の経験のsampleではない。Entryはknowledge/内へJSONとして保存する。必ずschema/experience-entry.schema.jsonの型、列挙値、required、additionalPropertiesに従う。

**作成前Safety Review必須。人を集めるな。経験を集めろ。** 個人・組織・固有案件を除いて成立しない情報、秘密、private data、raw transcript/log、法的問題がある情報は記入しない。判断に迷えば保存しない。

| Schema field | 記入する内容 |
| --- | --- |
| id / title / category | 知識用のID、一般化した題名、分類 |
| task_type | 作業分野。個人や固有案件を分類名に使わない |
| ai_system | AI systemまたはtoolの一般名称 |
| model / tool_version | 分かる場合のみ。未知を推測しない |
| observation_date | 安全に記録可能なISO日付。未知・安全に記録不能なら捏造せず収録を見送る。個人を識別する時刻は残さない |
| environment | 再利用に必要な一般条件だけ |
| goal / approach | 目的と試した手順 |
| what_worked / what_failed / why | 成功、失敗、原因分析。観測と推論を区別 |
| improved_method | 改善した方法または提案。未検証ならその旨を明示 |
| when_to_use / when_not_to_use | 適用条件と避ける条件 |
| known_limitations | 制約と未確認事項 |
| evidence_type | 実験、反復実験、公式資料、公開研究、一般化したcommunity報告、推論の区別 |
| reproduction_status / confidence | 再現状態と根拠への確信度 |
| related_knowledge_ids | 関連する知識ID。人・案件のIDは禁止 |
| safety_review | status=approved、independent_review/data_minimization/no_identifiers/no_private_data/rights_checkedがすべてtrueのobject。reviewerの個人名・handleは記入しない |
| knowledge_status | currentまたはhistorical |
| sources（任意） | official documentationまたはpublic researchの安全な出典のみ。URLはHTTPS、credentials/query/fragment/IPなし、source_safety_review=true |

failures分類ではfailure_details objectにfailure、impact、cause、detection、recovery、prevention、generalized_lessonを必須記録する。時間により古くなった知見はknowledge_status=historicalとして扱う。

idはEXP-に6桁の数字を続ける。reproduction_statusはreproducedまたはnot reproduced、confidenceはlow/medium/high。approvedやtrueを未確認のまま埋めてはならない。独立レビューが終わる前の草稿をknowledge/へ保存しない。

個人SNSの投稿者ID・profile・個人URL・引用文を出典にしない。公式資料や研究も権利と利用条件を守り、大量コピーをしない。実データや元sourceをtemplateへ貼らない。

記入後はValidator、unit tests、独立レビューを通す。**Automated validation != privacy guarantee**。
