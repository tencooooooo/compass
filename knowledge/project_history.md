# Project History

## v0.1

AI Growth Hunter started with daily OHLCV market data collection for selected US stocks. The first goal was to create a simple data foundation for later screening, analysis, and backtesting.

## v0.2

The project was refactored for long-term operation. The structure was separated into collectors, storage, analyzers, reports, utils, logs, and tests. `settings.yaml` and logging were introduced.

## v0.3

Company profile collection was added. The `knowledge/` directory was introduced as human-maintained reference material for future AI analysis.

## v0.4

Financial data collection was added. The project documented its future direction toward a ticker/entity-based data model.

## v0.5

News collection and Event Database generation were added. The project began connecting news with factual price and volume reactions.

## v0.6

Company analysis report generation was added. Reports summarize company overview, price facts, financials, recent news, event data, analysis, research priority, and AI comments without investment advice.

## v0.7

Comparative analysis reports were added. The project can now compare multiple tickers across fundamentals, financials, momentum, news, events, strengths, watch points, and research priority.

## v0.7.1

The project was prepared for GitHub-based long-term operation. Documentation, license, changelog, contribution rules, and Git ignore rules were organized.

## v1.0-alpha

The first Alpha milestone was prepared. Phase1 Foundation was marked complete, Phase2 Intelligence was marked in progress, and the project philosophy was formalized through the Manifest, Project Philosophy, future architecture, development principles, release strategy, and new Knowledge files.

The project was rebranded from AI Growth Hunter to Compass. AI Growth Hunter remains as the historical original name, while Growth Hunter is reserved for the future growth stock screening engine.

## Compass Research 01

Explainable Scoring Engine was added. Compass began assigning company scores with reasons, evidence, and confidence instead of black-box rankings.

## Compass Research 02

Market Intelligence Engine was added. Compass began summarizing market and sector context before company-level discovery.

## Compass Research 03

Discovery Engine was added. Compass began identifying additional research candidates with Discovery Score, reasons, strengths, watch points, confidence, and evidence.

## Compass Research 04

Backtesting & Validation Engine was added. Compass began comparing Discovery candidates with later price movement and preserving validation history for the future Learning Engine.

## Compass Research 05

Slack Notification Engine was added. Compass can now send a concise Morning Research Brief and workflow failure notification through a Slack Incoming Webhook configured in GitHub Secrets.

## Compass Research 06

Notification Engine was added. Compass can now detect important event-driven alerts, route them through a Notification Router, send them through the Slack Connector, and store notification history for duplicate prevention and next-run comparison.

## Compass Core 01

Memory Engine was added. Compass can now preserve company, sector, discovery, validation, market, and lessons memory through a provider-based Local JSON layer designed for future S3 or database migration.

## Compass Core 02

Feedback Engine was added. Compass can now compare Discovery and Validation results, summarize Discovery, Score, Confidence, Sector, and Event accuracy, and generate Knowledge update candidates for human review without automatically changing Knowledge.
