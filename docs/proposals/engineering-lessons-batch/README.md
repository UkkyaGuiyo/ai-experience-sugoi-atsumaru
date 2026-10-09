# 一般化したエンジニアリング知見の収録候補

Review status: PENDING_REVIEW

**20候補のうち15件を2026-10-09に正式Knowledgeへ収録。残る5件は重複整理後の独立審査待ち。** 文書先頭の `Review status: PENDING_REVIEW` は未採用候補が含まれるための文書全体の表示。収録済み15件は[正式化対応表](../../reviews/2026-10-09-63-knowledge-formalization.md)を参照。

許可された複数作業の実装・検証・失敗・計画記録を調べ、既存項目との重複を整理した。ここに残すのは、元案件を知らなくても評価・応用できる方法論と反例の設計である。元記録の移植、成功件数の転載、製品仕様の複製ではない。

## 根拠と状態

全候補は `inference` / `not reproduced`。提案の一般的な効果への確信度は `low` とする。元の作業で実験が行われたことと、この一般化した方法を別環境で再現したことを混同しない。各候補の対照試験は新しく構成した評価案であり、実施済みではない。録音、追跡、変換、描画、性能について未確認の成功を主張しない。

実行日時、元の数値・テスト件数、個人・組織・案件名、非公開リポジトリ識別子、個人パス、元コミット・原資料のハッシュ、原文引用、生ログ、生コード、音声・画像は含めない。モデル名や運用モード名も保存しない。草稿の一次内容確認と機械検査は、別担当の独立レビューを意味しない。

## 候補一覧

| 候補 | 主題 | 本文 |
|---|---|---|
| R01 | 本体を直す前に、生成済み入力の鮮度を確かめる | [generated-assets-and-builds.md](generated-assets-and-builds.md) |
| R02 | 画面を開く操作も、検証対象を書き換え得る | [generated-assets-and-builds.md](generated-assets-and-builds.md) |
| R03 | ビルド出力の隔離だけでなく、コンパイル入力も固定する | [generated-assets-and-builds.md](generated-assets-and-builds.md) |
| R04 | 画像座標と演出座標を分け、最終出力にも表示範囲を適用する | [generated-assets-and-builds.md](generated-assets-and-builds.md) |
| R05 | 承認要求の保存と、承認完了の保存を分離する | [process-workflows.md](process-workflows.md) |
| R06 | 作業の失敗を維持しながら、安全な後片付けは進める | [process-workflows.md](process-workflows.md) |
| R07 | 安全側の観測器にも、永久に進めなくなる条件がないか調べる | [process-workflows.md](process-workflows.md) |
| R08 | 往復で同じになっただけでは、最初から正しかったとは言えない | [semantic-roundtrips.md](semantic-roundtrips.md) |
| R09 | 形状の対応、面の向き、属性の所属を別の命題として検証する | [semantic-roundtrips.md](semantic-roundtrips.md) |
| R10 | 見たデータで作った仮説は、未見データで確かめる | [semantic-roundtrips.md](semantic-roundtrips.md) |
| R11 | 入力を止めてから別経路で再生し、一時保持を検証する | [audio-capability-probes.md](audio-capability-probes.md) |
| R12 | 消去操作の後から届くデータも、旧セッションとして拒否する | [audio-capability-probes.md](audio-capability-probes.md) |
| R13 | 精度を下げることと、メモリを減らすことを区別する | [audio-capability-probes.md](audio-capability-probes.md) |
| R14 | 製品要求と候補方式の実験計画を分ける | [approach-and-identity.md](approach-and-identity.md) |
| R15 | 異なるラベルを区別できても、送信元を認証したことにはならない | [approach-and-identity.md](approach-and-identity.md) |
| R16 | ローカル模擬試験と、複数クライアントの一致を別の表で追う | [approach-and-identity.md](approach-and-identity.md) |
| R17 | 一時スロットは、結果の引渡し完了を確認してから再利用する | [state-and-scene-lifecycle.md](state-and-scene-lifecycle.md) |
| R18 | 復元確認では件数だけでなく、元の対象そのものを比較する | [state-and-scene-lifecycle.md](state-and-scene-lifecycle.md) |
| R19 | 一時オブジェクトの成立と、保存・再読込後の成立を分ける | [state-and-scene-lifecycle.md](state-and-scene-lifecycle.md) |
| R20 | 依頼がキューに入ったことと、担当が動き出したことを区別する | [agent-resumption.md](agent-resumption.md) |

## 候補の重複整理（2026-10-09）

内容審査で新規20件のうち15件は記述上の重大阻害なし、5件は既存の正式Knowledgeや移行Lessonとの統合候補と判定した。具体的な統合先と再利用規則は[7組の統合レビュー](../../reviews/2026-10-09-consolidated-candidates.md)に保存済み。R01はLFA-008の事例を参照するが、別個の正式Entryにはまだ採用していない。

**独立Safety/rights/technicalレビューが完了したことや、統合先の正式EXP本文を更新したことを意味しない。** 未承認候補は引き続き `PENDING_REVIEW` とし、重複した個別採番を避ける。

## 既存項目との関係

既存のEXP-000001〜EXP-000004と、別ブランチの一般化ワークフロー候補A〜Iを重複確認の対象にした。正式Knowledgeの上書き・採用は行っていない。対応する統合案はレビュー資料へ保存済みだが、正式なKnowledge Entryへの反映は別の承認を要する。結果ゲートの分離、調べた範囲だけの結論、一時ファイルの所有、限定委譲などの一般原則を、同じ主張の新規Entryとして増やしてはいない。

本候補は具体的な失敗の切り分けや対照試験を追加するもの。関連が深い項目は、独立レビュー時に既存項目への追記へ統合してよい。候補数は新規で独立した規則の確定数ではない。R05とR06、R08とR09、R11とR12、R17とR19も、対象が近いので最終採番前に統合の必要性を確認する。

## 保存前の一次確認

本文は独自の説明として書き直し、元資料の文章やコードを転記していない。人物・案件・アクセス先を示す情報と、再識別につながる具体的な実行条件を除いた。権利の確認できない実装や、許可を回避する操作手順は含めない。個別製品の一般化不能な設計や未確認の成功主張は見送った。

これは作成担当の一次確認であり、独立した安全レビュー・法的保証ではない。元資料に対するコードレビューが通っていても、本知見の安全レビューが通ったとは扱わない。

## 正式収録への引渡し

1. 別担当が安全性、再識別リスク、根拠の表現、既存項目との差分、提案の妥当性を確認する。
2. 承認した候補だけを最新Schemaへ変換する。観測日は合成・検討日と元実行日を混同せず、安全に記録できない必須項目は捏造しない。
3. 全ブランチでID・重複を再確認し、正式採番する。レビュー前に `independent_review: true` を付けない。
4. RepositoryのValidatorとunit testsを実行し、対象コミットのCI結果を確認する。機械検査は独立レビューの代替ではない。
5. 承認済みの運用に従って採用する。元プロジェクトの停止・実行許可・公開状態を変更しない。

この資料を保存したことは、正式採用、実験再開、公開設定変更、過去の失敗判定の書換えを意味しない。
