# Contribution手順

人間・AIともにroot AGENTS.mdを適用する。情報量を減らすことは失敗ではない。安全に一般化できない経験は収録しない。

Project、実験、AI運用、開発作業から得た経験は、それがProject由来であること自体を理由に除外しない。元Projectを知らなくても役立つ再利用可能な知識へ一般化し、第三者へ開示しても個人・組織・固有案件・private sourceを特定または復元できない内容だけを収録する。

1. Raw sourceをそのまま保存しない。会話、log、スクリーンショット、メール、prompt履歴を添付しない。
2. Experienceを一般化する。目的、条件、方法、結果、改善を抽出する。
3. 個人・組織・固有案件・非公開Repository情報を除去する。複数条件の組み合わせによる再識別も確認する。Project名、private repository識別子、個人path、raw artifactはEntryへ持ち込まない。
4. **ファイル作成前にSafety Review**を行う。秘密、private data、権利、契約、法令、必要最小性を確認する。判断に迷えば保存しない。
5. templates/EXPERIENCE_ENTRY.mdとSchemaに従ってJSONを作成し、Validatorとunit testsを実行する。
6. 独立したReviewerが内容、出典、一般化、安全性、根拠、再現状態を確認する。根拠が推論なら推論と記録する。
7. 検査・レビュー合格後、承認済み運用でmergeする。CI PASSだけでmerge可と判断しない。

過去Projectや既存Knowledge Baseを広く探索して候補を掘り起こす一括backfill・自動移植は通常ContributionではなくMigration Policyの対象とし、明示された対象範囲が必要。

Automated validation != privacy guarantee。検査結果に危険候補があれば、元の値をIssueやPRへ転載せず、内容を除去・抽象化して再検査する。誤検出でも安全性を独立レビューし、理由を記録する際に危険値を再掲しない。特定の検出規則を修正する場合は、必要最小の変更と合成データの回帰testsを追加し、別Reviewerに確認してもらう。広範なallowlistやdirectory除外、検査全体の無効化で通過させない。

個人URLやhandleを出典として追加しない。出典を合法的かつ安全に残せない場合、保存しない。外部本文やコードの大量コピーをしない。下位AGENTSは追加制約のみ認められる。


## Contribution licensing

By contributing material you have the right to submit, you agree that accepted contributions are distributed under the license that applies to their destination:

- Knowledge, documentation, templates and other written content: CC BY 4.0.
- Software, validators, tests, schemas and GitHub Actions/workflow code: MIT License.

See `LICENSE` for the exact repository-level scope. Do not submit third-party material under these licenses unless you are authorized to do so. A contribution must still pass the repository's privacy, source, rights and independent-review rules before acceptance.
