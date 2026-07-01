# Event Classification

Notification Engineで扱うイベント分類です。

## discovery_alert

Discovery Scoreが高く、追加調査候補として優先度が上がった企業。

## score_change_alert

前回実行と比較して、企業スコアが大きく変化した状態。

## market_trend_alert

Market IntelligenceでセクターのMomentum、News、Financial Healthなどのトレンドが変化した状態。

## important_news_alert

M&A、決算、CEO交代、大型契約、新製品など、企業評価や市場心理に影響する可能性があるニュース。

## validation_alert

過去のDiscovery候補がValidationでExcellentなどの重要な結果になった状態。

## workflow_failure

GitHub ActionsやCompass Pipelineの失敗。

## Non-Alert Events

以下は原則として即時通知しません。

- 通常ニュース
- 小さなスコア変動
- 期間未完了のValidation
- データ欠損のみの通知
- 投資判断を促す表現
