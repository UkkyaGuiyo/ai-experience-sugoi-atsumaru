# 63件の正式Knowledge登録と独立コンテンツ審査 — 2026-10-09

**対象：** 前回92件の個別評価で `TEXT_OK` と判定され、所有者から正式採用を明示された63候補（新規15件・旧Lesson由来48件）。既存の `EXP-000001`〜`EXP-000012` を維持して `EXP-000013`〜`EXP-000075` を発行する。

## ユーザー承認と審査範囲

- 収録の権限は所有者の「63件、正式採用／保存」という明示指示に基づく。
- 今回の審査は、**元の候補を執筆した担当とは別のAIアシスタント**が行い、候補本文・既存12件・92件の個別診断・修復記録・公開規則を照合した。文面の変換と書込みも同じアシスタントが実施しており、変換後のJSONをさらに別のAIモデルが追認したという主張はしない。
- 個人や案件の識別、識別子の組合せによる再識別、非公開URL・生ログ・生コード・credential・第三者権利、必要最小性、根拠／条件／未実施試験を確認した。安全であると判断できない元の個人・案件情報や、出所を復元できるprivate source識別子は正式Entryへ移していない。
- 新規15件の根拠区分は `inference / not reproduced / low`。評価用の合成対照試験は提案であり未実施。
- 旧Lesson由来48件は `historical`。過去の実行試験を記録するものは `direct experiment`、原資料の設計・ソースレビューを根拠とするものは `inference` と区別した。ただし**今回の登録では一件も元実験を再実行していない**ため、すべて `not reproduced / low` としている。
- `observation_date=2026-10-09` は今回の知識化・レビュー日を表す。過去の事象の発生日や新しい実測日ではない。各Entryにもその区別を残す。
- 機械検査は絶対的なプライバシー・権利保証ではない。今回のコンテンツのレビュー担当は元の採集担当と異なるが、変換後の63 JSONに対する**別モデルの追加レビューは未実施**。Schema・Safety scan・tests・GitHub Actionsの実結果は、対象コミットへ保存後に確認する。

## 全63件の正式IDと個別審査所見

| 正式ID | 元候補 | 分類 | 根拠の性質 | 審査の要点 |
|---|---|---|---|---|
| EXP-000013 | R01 | patterns | inference | 生成入力・ロード物の鮮度と試験順序依存を切り分ける。LFA-008とは一般則／事例として整理。 |
| EXP-000014 | R03 | patterns | inference | 出力分離だけでは不足し、コンパイル入力集合を固定する点が独立している。 |
| EXP-000015 | R04 | patterns | inference | 画像座標と効果座標を分離する。最終マスクの必要性はケース限定で記述。 |
| EXP-000016 | R05 | workflows | inference | 承認要求と承認成立の永続化を分離。冪等性は別条件と明記。 |
| EXP-000017 | R07 | anti-patterns | inference | 観測の安全性と進行可能性の両立を提案。安全条件の緩和とは区別済み。 |
| EXP-000018 | R08 | patterns | inference | 誤った中間状態を往復で保存できても正しさは証明されない。独立入力を要求。 |
| EXP-000019 | R10 | patterns | inference | 仮説に使用した観測と未見の判定入力を分ける方法。実証済みと扱わない。 |
| EXP-000020 | R11 | workflows | inference | 入力停止後の独立再生という能力ゲートを明示。特定SDKでの録音可能性は未証明。 |
| EXP-000021 | R12 | patterns | inference | 消去後の遅着データ・旧世代拒否を定義。スレッド安全は追加検証が必要。 |
| EXP-000022 | R13 | patterns | inference | 量子化と実保存型・ピークメモリは別指標。測定前の削減率を主張しない。 |
| EXP-000023 | R14 | workflows | inference | 製品要件／方式選択／実装を分離する設計原則。無限の方式探索を求めない。 |
| EXP-000024 | R17 | patterns | inference | 引渡し完了とスロット再利用を区別する。世代番号は結果精度の証拠ではない。 |
| EXP-000025 | R18 | patterns | inference | 復元前後の同数一致でなく対象の同一性を検証。実行時IDの適用範囲を限定。 |
| EXP-000026 | R19 | workflows | inference | 一時生成と保存・再読込の合格を区別。実クライアント証明へ過大拡張しない。 |
| EXP-000027 | R20 | agents | inference | 依頼配達と担当の実行開始を別状態にする。実基盤による差を明記。 |
| EXP-000028 | LFA-003 | failures | direct experiment | ゼロ面積三角形のImporter設定比較は限定実証。一般的なSkin保証へ広げない。 |
| EXP-000029 | LFA-005 | failures | direct experiment | GPU描画試験に実GPUが必要という条件を明記。コンパイル専用試験とは区別。 |
| EXP-000030 | LFA-009 | failures | direct experiment | 空中での方向入力と向きの基準を分離。ゲーム仕様固有であることを保持。 |
| EXP-000031 | LFA-010 | failures | direct experiment | アニメーション出力のアドレス衝突を実際の宛先形式で確認。ソースIDの代替不可。 |
| EXP-000032 | LFA-011 | failures | direct experiment | アセットRollbackはmetaと参照関係まで必要。実ファイルの復元と分離。 |
| EXP-000033 | LFA-012 | failures | direct experiment | 座標基底変換の非一様・負スケールを含む証拠。形状一致は別ゲート。 |
| EXP-000034 | LFA-014 | failures | direct experiment | 未コミット依存で通った試験とHEAD-only試験を区別。実ランタイムのPASSは未主張。 |
| EXP-000035 | LFA-015 | failures | direct experiment | MonoBehaviourの型とScriptAsset解決を区別。一般C#の1ファイル複数型は禁止しない。 |
| EXP-000036 | LFA-016 | failures | direct experiment | 作成済み版と現行Deploymentを照合。再公開の成功は未実施として保持。 |
| EXP-000037 | LFA-017 | failures | direct experiment | 明示的nullと破損参照を別種として扱う。通常nested importは未完全。 |
| EXP-000038 | LFA-019 | failures | direct experiment | Script参照IDとプロバイダー可用性を区別。第三者SDKを同梱する許可ではない。 |
| EXP-000039 | LFA-020 | failures | direct experiment | ネイティブハンドルと失敗診断を分離し応答待ちに上限を設ける。OS環境限定。 |
| EXP-000040 | LFA-021 | failures | direct experiment | 見えない階層ノードも同一性比較の対象。Renderer/骨の証明は別。 |
| EXP-000041 | LFA-022 | failures | direct experiment | Host管理のModal寿命をローカルフラグでは終了できない。Blenderの試験条件を明記。 |
| EXP-000042 | LFA-023 | failures | direct experiment | HTTP成功とWorkFlowのbody/files形式を別判定。中継を無制限Proxyにしない。 |
| EXP-000043 | LFA-024 | failures | direct experiment | テンプレート展開不良とEncoding問題を対照で分離。環境固有のNode ID仕様に限定。 |
| EXP-000044 | LFA-025 | failures | direct experiment | ローカライズ名ではなくNode typeとactive outputを使用。全描画経路の保証ではない。 |
| EXP-000045 | LFA-026 | failures | direct experiment | 自動生成の所有状態が利用者の編集を上書きしないようReceiptで検証。 |
| EXP-000046 | LFA-027 | failures | direct experiment | 必須Tool経路を制御フローで強制。局所PASSと全体Soak失敗を分離。 |
| EXP-000047 | LFA-029 | failures | direct experiment | Transform一致と評価後頂点一致は別命題。Frame条件を狭く保持。 |
| EXP-000048 | LFA-030 | failures | direct experiment | 数字と単位の対応を一緒にParseする。その他Localeは未検証。 |
| EXP-000049 | LFA-031 | failures | direct experiment | 単調時計の解像度がCallback頻度より粗い場合の誤判定を検証。時刻捏造をしない。 |
| EXP-000050 | LFA-032 | failures | direct experiment | 平均がゼロでも分散が大きい失敗。閾値の一般化を避ける。 |
| EXP-000051 | LFA-033 | failures | direct experiment | 子プロセス自身のTimerだけではNative停止を拘束できない。原失敗原因は未解明。 |
| EXP-000052 | LFA-034 | failures | direct experiment | 言語の辞書表現とJSONを混同しない。公開Deploymentの回復成功は未立証。 |
| EXP-000053 | LFA-035 | failures | direct experiment | 周期処理は仕事時間を含む位相基準を保持。全イベント処理にはそのまま適用しない。 |
| EXP-000054 | LFA-036 | failures | direct experiment | 履歴を残したReset文言では会話分離にならない。別の参照推測不具合を分離。 |
| EXP-000055 | LFA-037 | failures | direct experiment | Rollbackは意図でなく実行済み変更を逆順に戻す。途中失敗も検証。 |
| EXP-000056 | LFA-038 | failures | direct experiment | HTTP payloadに実フィールドが含まれるか別契約で検証。値の意味一致は未検証。 |
| EXP-000057 | LFA-039 | failures | direct experiment | SDKのゼロVersionが照会失敗由来の可能性を確認。旧ツール版を現行推奨にしない。 |
| EXP-000058 | LFA-040 | failures | direct experiment | 検索結果のカテゴリはProvider typeで裏付ける。0件を自動失敗と扱わない。 |
| EXP-000059 | LFA-041 | failures | direct experiment | 生成テキストをJSON文字列連結せず一度にSerialize。受信側の意味検査は別。 |
| EXP-000060 | LFA-042 | failures | direct experiment | Shortcutは実際のFocus/Event経路を通す。物理キーボード網羅とは区別。 |
| EXP-000061 | LFA-043 | failures | direct experiment | 音声案内でもLLM Tool往復遅延は消えない。ローカル制御と人間操作を別に扱う。 |
| EXP-000062 | LFA-044 | failures | direct experiment | 離陸直後の接触を着地と誤認しない。仕様・物理モデル固有の調整。 |
| EXP-000063 | LFA-045 | failures | direct experiment | 不明状態の影響を必要な範囲だけに保つ。未裏付けの別対象承認をしない。 |
| EXP-000064 | LFA-046 | failures | direct experiment | 変更前に全Batchの名前・型競合を検証。Disk rollbackの実証ではない。 |
| EXP-000065 | LFA-047 | failures | direct experiment | キャッシュ除外をRoot基準にする。復旧した30ファイル以外の完全性は未確認。 |
| EXP-000066 | LFA-049 | failures | inference | Fixture oracleを製品全体の契約へ転用しない。解釈上の設計レビュー根拠を明記。 |
| EXP-000067 | LFA-050 | failures | direct experiment | FBXの生成時metadataによりHashが変わり得る。実行ごとに証拠Hashを固定。 |
| EXP-000068 | LFA-052 | failures | direct experiment | 制限環境の一時領域は実行単位で所有。利用者資産の再生成許可ではない。 |
| EXP-000069 | LFA-055 | failures | direct experiment | Unity Package Manager無効化とNUnit参照欠落の区別。既存Lock/Cacheを維持。 |
| EXP-000070 | LFA-058 | failures | inference | 成功試行件数と成功結果件数を区別。ソースReviewの証拠で実Blender再実行は未済。 |
| EXP-000071 | LFA-061 | failures | direct experiment | 前回Cleanup済みの使い捨てFixtureに依存しない。元ユーザー資産の再生成は対象外。 |
| EXP-000072 | LFA-062 | failures | direct experiment | CRLFとGUIDの字句内容を別検証。32桁ルールを緩めない。 |
| EXP-000073 | LFA-067 | failures | direct experiment | Binary FBXのPath検閲は型と長さを尊重。方式・Version依存性を明記。 |
| EXP-000074 | LFA-070 | failures | direct experiment | Unity Importと明示Finalizer Applyを別段階にする。Applyを未実施の歴史記録は維持。 |
| EXP-000075 | LFA-071 | failures | direct experiment | LicensingClientのSession mismatchを観測。正規の利用者Session以外で迂回しない。 |

## 残存候補・保存境界

- 採用済み63件、既存12件、合計 **75件**。既存の12件のJSON・レビュー状態・根拠を変更しない。
- 未採用は **29件**（重複10件＋修復後の個別収録待ち19件）。勝手に一括採用しない。元候補Markdownも消去せず保管する。
- 旧[92件の初回判定](2026-10-08-92-candidate-triage.md)、[移行修復記録](2026-10-09-candidate-remediation.md)、[重複候補統合記録](2026-10-09-consolidated-candidates.md)はその時点の事実として保持する。
- AGENTS・Schema・検査器・公開設定・ライセンスは変更しない。新しい収集ツールや監視装置は追加しない。
- **この記録だけでは実際のGitHub ActionsのPASSは主張しない。** 保存後に対象SHAに対するCI結果と実際のKnowledge件数を別途照合する。
