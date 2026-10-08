# Securityと危険情報の対応

機械検査は第一防衛線であり、個人情報・機密情報・適法性の完全な検出器ではない。

危険情報、credential、個人情報、非公開source、検査回避に使える秘密値をPublic Issue、PR、comment、discussion、commit messageへ貼らない。

## 非公開の報告

Security上の問題に機密情報を含む可能性がある場合は、GitHubの **Report a vulnerability** からPrivate vulnerability reportingを使用する。報告には必要最小限の再現情報だけを含め、実credentialや個人データを再投稿しない。

Private vulnerability reportingが利用できない場合、危険値をPublicに投稿しない。安全な非公開窓口が確認できるまで、具体値の送信を止める。

## Secretや危険情報が疑われる場合

通常の収集・公開・mergeを止める。credential失効、アクセス制限、履歴rewrite、外部複製への対応はRepository管理者が正規の権限で判断する。勝手に既存データ削除、履歴rewrite、credential生成を行わない。ファイル削除だけで履歴・fork・clone・cacheから消えたと判断しない。

テスト再現には完全な合成値を使う。PUBLICであることも、PRIVATEであることも保存許可の代替ではない。禁止情報はRepository visibilityに関係なく保存しない。
