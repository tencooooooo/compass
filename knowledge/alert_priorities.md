# Alert Priorities

Notification EngineのPriority定義です。

## Emergency

即時確認が必要な障害。

例:

- GitHub Actions失敗
- データ取得パイプライン停止

## High

重要な変化。人間が優先的に確認すべきもの。

例:

- Discovery Score 90以上
- Validation Excellent
- 大きなスコア変化

## Medium

確認価値がある変化。

例:

- Score Change ±5以上
- Market Trend変化
- 重要ニュース

## Low

記録はするが、即時通知は抑制してもよい情報。

例:

- 軽微なスコア変動
- 通常のニュース
- 期間未完了のValidation

## Principle

Priorityは投資判断ではありません。確認順序を整理するための運用ラベルです。
