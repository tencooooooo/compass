# Research Engines

日次パイプラインで動く分析エンジン群です。スコアリングからValidation、通知までを担当します。

[← README に戻る](../../README.md)

## Explainable Scoring Engine

Compass Research 01 adds an Explainable Scoring Engine.

Output:

```text
reports/scoring/company_scores.csv
reports/scoring/company_scores.json
reports/scoring/explanations/{ticker}.md
```

The score is 100 points total:

```text
Growth: 20
Financial Health: 20
Valuation: 20
Momentum: 20
News: 20
```

Each category maximum is actually reachable. Momentum splits its 20 points into four benchmark-relative windows worth 4 points each (1M/3M/6M/1Y) plus 4 points for volume; it previously topped out at 16, which quietly discounted Momentum inside Signal Strength.

Each score includes:

- Reason
- Evidence
- Used metrics
- Missing data
- Confidence

Confidence is one of:

```text
High
Medium
Low
```

The score is not a ranking or investment decision. It is an evidence-based research aid. A high score with low confidence must be reviewed carefully.

## Market Intelligence Engine

Compass Research 02 adds a Market Intelligence Engine.

Output:

```text
reports/market/market_summary.md
reports/market/sector_summary.md
reports/market/market_dashboard.json
```

It summarizes:

- Covered company count
- Sector composition
- Market momentum
- Notable news
- Event count
- Sector averages
- Rule-based market trends
- Rule-based market psychology

Market Intelligence does not generate company rankings. It builds the market and sector context that future Growth Hunter screening will use.

## Discovery Engine

Compass Research 03 adds a Discovery Engine.

Output:

```text
reports/discovery/discovery_candidates.md
reports/discovery/discovery_candidates.json
reports/discovery/candidate_details/{ticker}.md
```

Discovery Engine uses:

- Price
- Company
- Financials
- News
- Events
- Company Analysis
- Comparative Analysis
- Scoring Engine
- Market Intelligence
- Knowledge

It does not generate investment rankings. It identifies companies that may deserve additional research and explains why.

Discovery Score is 100 points total. The budget is declared in one place as `DISCOVERY_POINTS` in `engines/discovery/candidate_selector.py`:

```text
Scoring Engine carry-over   Growth 18 / Financial Health 14 / Valuation 8 / News 8
Fundamental flags           Revenue 2 / EPS 2 / R&D 3 / Free Cash Flow 3
Benchmark-relative momentum 1M 4 / 3M 5 / 6M 5 / 1Y 8
News                        Positive headlines 4 / Recent coverage 2
Events                      Average price reaction 5
Sector context              Above sector average 3 / News trend 1 / Financial health trend 2
Scoring total bonus         3
```

Every point that reaches `discovery_score` also enters the `signal_rate` denominator, so the two always describe the same basis. Items that cannot be evaluated because data is missing are excluded from both and recorded in `missing_data`.

`tests/test_discovery_score_scale.py` asserts that the budget sums to 100, that a best-case candidate actually reaches it, and that every threshold configured in `config/notification.yaml` and `config/strategy.yaml` is within reach.

Discovery Engine is the foundation for the future Growth Hunter engine.

## Backtesting & Validation Engine

Compass Research 04 adds a Backtesting & Validation Engine.

Output:

```text
reports/validation/validation_summary.md
reports/validation/validation_history.csv
reports/validation/validation_history.json
```

Validation Engine checks Discovery candidates against stored price history for:

```text
1w
1m
3m
6m
1y
```

It records:

- Discovery date
- Discovery Score
- Discovery reasons
- Start price
- End price
- Return
- Benchmark difference when benchmark data exists
- Sector difference when peer data exists
- Validation result
- Confidence

Validation result labels:

```text
Excellent
Good
Neutral
Poor
```

Periods that are not complete yet are kept as `Neutral` and marked as incomplete. This avoids pretending that Compass has evidence before enough time has passed.

Validation is the foundation for the future Learning Engine. It stores what happened after Discovery so humans can later review whether Scoring and Discovery rules should be improved. It does not perform automatic learning yet.

## Slack Notification Engine

Compass Research 05 adds a Slack Notification Engine.

Files:

```text
integrations/slack/slack_notifier.py
integrations/slack/slack_formatter.py
config/notification.yaml
```

GitHub Secret:

```text
SLACK_WEBHOOK_URL
```

To configure Slack:

1. Create a Slack Incoming Webhook in your Slack workspace.
2. Copy the webhook URL.
3. Open the GitHub repository settings.
4. Go to `Settings > Secrets and variables > Actions`.
5. Add a repository secret named `SLACK_WEBHOOK_URL`.

Success notification:

- Execution timestamp
- Success status
- Covered ticker count
- Discovery candidate count
- Top candidates with Discovery Score and Confidence
- Score changes when previous score data is available
- Market Intelligence sector summary
- Important news titles
- Validation result counts
- Artifact name

Failure notification:

- Failed workflow status
- Step hint
- Error hint
- Timestamp
- GitHub Actions run number

Slack notifications are intentionally brief. They are a Morning Research Brief, not a replacement for generated reports. Detailed analysis remains in the Markdown, CSV, and JSON artifacts.

## Notification Engine

Compass Research 06 adds an event-driven Notification Engine.

Files:

```text
engines/notification/notification_engine.py
engines/notification/event_detector.py
engines/notification/notification_router.py
integrations/slack/slack_connector.py
```

Notification Engine detects:

- Discovery Alert: Discovery Score 90 or higher
- Score Change Alert: score changed by 5 points or more
- Market Trend Alert: Market Intelligence sector trend changed
- Important News Alert: important news categories from `knowledge/news_analysis_rules.md`
- Validation Alert: Validation result became Excellent
- Workflow Failure: GitHub Actions failure

Notifications are routed through `NotificationRouter`. Slack is the first connector. Future connectors can be added for:

```text
Discord
Teams
LINE
Email
Push notification
```

Event history is saved to:

```text
storage/notifications/notification_history.json
```

The workflow restores `storage/notifications/` from the `compass-data` branch so Score Change and Market Trend alerts can compare with the previous run. Important News alerts are limited to high-signal patterns published within the previous 36 hours, and the scheduled pipeline runs on weekdays. GitHub Actions cache is kept temporarily as a migration fallback. The folder is ignored by the main Git branch and uploaded as part of the generated artifact.

Notification Engine is intentionally selective. It sends alerts for action-worthy changes, not every data point.
