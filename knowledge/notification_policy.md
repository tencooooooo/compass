# Notification Policy

Compassの通知は、毎日のResearch Briefを短く届けるためのものです。

## What To Notify

- Workflowの成功または失敗
- 実行日時
- 対象銘柄数
- Discovery候補のTop3
- Discovery Score
- Confidence
- Market Intelligenceのセクター要約
- 重要ニュースのタイトル
- Validation結果の件数
- Artifact名

## What Not To Notify

- 買い、売り、保有などの投資判断
- 目標株価
- 個別投資助言
- 長い企業分析本文
- 全ニュース本文
- APIキーやSecrets
- 個人情報

## Frequency

- GitHub Actionsの毎日実行後に1回送信する。
- 失敗時はエラー通知を送信する。
- 手動実行でも同じ通知方針を使う。

## Principle

Slack通知は詳細レポートの代替ではありません。投資家が「今日どこを見るべきか」を把握するための入口です。
