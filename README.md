# slot-scraping

## slot-scraping とは

- web上から特定の店舗のスロットデータ取得用のアプリケーション

- 23:00にスクリプト実行

- 取得したデータの参照用アプリケーション(Slot-Rec)は<a href="https://github.com/Reni-masa/slot-rec">こちら</a>

## 使用技術

-   python(v3.9.6)
-   mysql(cleardb)

## インフラ
- heroku

## 今後の課題 memo
- スクレイピング失敗時の通知機能
  - スクレイピング先のページ構造が変わった場合にデータ取れなくなるため
- 機械学習による設定配分予測
  - DBに蓄積したデータをもとに翌日の設定配分を予測する
-   設定推測機能の切り出しを行い API 化
    -   機能を切り取り、どこかに api 配置
