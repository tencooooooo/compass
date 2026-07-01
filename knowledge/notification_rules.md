# Notification Rules

Notification Engineは、重要な変化だけを通知するためのルールを管理します。

Compassは通知を大量に送るシステムではありません。通知対象は、投資判断そのものではなく、人間が追加確認すべき変化です。

## Initial Rules

```yaml
notification:
  discovery_score: 90
  score_change: 5
  market_change: true
  important_news: true
  validation: Excellent
```

## Discovery Alert

- Discovery Scoreが90点以上の場合に通知する。
- Confidenceと主要理由を添える。
- 買い判断ではなく、追加調査候補として扱う。

## Score Change Alert

- 前回スコアとの差が±5点以上の場合に通知する。
- 前回スナップショットがない初回実行では通知しない。

## Market Trend Alert

- Market Intelligenceのセクタートレンドが変化した場合に通知する。
- Momentum, News, Financial Healthの変化を記録する。

## Important News Alert

- `knowledge/news_analysis_rules.md` にある分類を参考に、重要ニュースのみ通知する。
- 初期分類はM&A、決算、CEO交代、大型契約、新製品、配当、自社株買い、規制、訴訟、設備投資。

## Validation Alert

- Validation ResultがExcellentになった場合に通知する。
- Return、期間、Discovery Score、Confidenceを添える。

## Workflow Failure

- GitHub Actionsが失敗した場合に通知する。
- 失敗ステップ、エラー概要、Run Numberを記録する。
