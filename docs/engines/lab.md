# Lab Engines

日次パイプラインから独立して、週次または手動で動く実験・評価エンジン群です。

[← README に戻る](../../README.md)

## Time Machine Engine

Compass Lab 01 adds a Historical Replay engine.

Files:

```text
lab/time_machine/time_machine.py
lab/time_machine/snapshot_loader.py
lab/time_machine/timeline_builder.py
lab/time_machine/historical_context.py
```

Run:

```python
from lab.time_machine.time_machine import TimeMachine

TimeMachine.run(date="2024-03-01")
```

Output:

```text
reports/timemachine/snapshot_YYYY-MM-DD.md
reports/timemachine/discovery_YYYY-MM-DD.md
reports/timemachine/market_YYYY-MM-DD.md
```

Time Machine loads only data dated on or before the snapshot date:

```text
Price
Company identity metadata
Financials
News
Events
Knowledge
Memory
```

Time-sensitive company metrics without historical dates are excluded from historical scoring. Knowledge versions created after the snapshot date are excluded. Undated Knowledge markdown is only included when an active Knowledge version exists for the snapshot date.

Difference from Backtesting:

```text
Backtesting
↓
Evaluates what happened after a Discovery signal.

Time Machine
↓
Replays what Compass could have known before future outcomes existed.
```

The purpose is not prediction. It is to reproduce the research environment and inspect what Compass would have surfaced at that point in time.

## Pattern Intelligence Engine

Compass Lab 02 adds Pattern Intelligence.

Files:

```text
lab/pattern_intelligence/pattern_engine.py
lab/pattern_intelligence/pattern_extractor.py
lab/pattern_intelligence/pattern_classifier.py
lab/pattern_intelligence/similarity_engine.py
```

Run:

```python
from lab.pattern_intelligence.pattern_engine import PatternEngine

PatternEngine.run()
```

Inputs:

```text
Discovery History
Validation History
Memory
Learning History
Time Machine results
Financials
Prices
News
Market Intelligence
```

Output:

```text
reports/patterns/success_patterns.md
reports/patterns/failure_patterns.md
reports/patterns/similarity_report.md
reports/patterns/pattern_summary.md
```

Pattern groups:

```text
Success Pattern
Failure Pattern
Sector Pattern
Market Pattern
Event Pattern
Similarity Pattern
```

Pattern Intelligence is connected to Knowledge and Learning, but it does not update either automatically. It creates explainable Knowledge update candidates with evidence and confidence. Human review is required before any pattern becomes Knowledge or influences Learning.

## Theme Intelligence Engine

Compass Lab 03 adds Theme Intelligence.

Files:

```text
lab/theme_intelligence/theme_engine.py
lab/theme_intelligence/theme_classifier.py
lab/theme_intelligence/theme_tracker.py
lab/theme_intelligence/theme_similarity.py
```

Theme definitions:

```text
config/themes.yaml
```

Run:

```python
from lab.theme_intelligence.theme_engine import ThemeEngine

ThemeEngine.run()
```

Inputs:

```text
Companies
Financials
News
Discovery
Validation
Market Intelligence
Pattern Intelligence
Memory
Knowledge
```

Output:

```text
reports/themes/theme_summary.md
reports/themes/theme_ranking.md
reports/themes/theme_similarity.md
reports/themes/{Theme}.md
```

Theme Intelligence organizes Compass research through:

```text
Theme
↓
Market
↓
Sector
↓
Company
```

Companies can belong to multiple themes. For example, one company may be classified into AI, Semiconductor, Cloud, and Robotics when the evidence supports more than one long-term lens.

Relationship with Pattern Intelligence:

```text
Pattern Intelligence
↓
Finds repeated success, failure, sector, market, event, and similarity structures.

Theme Intelligence
↓
Uses those structures as context for long-term theme-level research.
```

Relationship with Discovery:

```text
Discovery
↓
Surfaces company candidates.

Theme Intelligence
↓
Groups candidates into themes and compares theme-level momentum, validation, news, and confidence.
```

Theme Intelligence does not update Knowledge automatically. It creates explainable research views that humans can review before deciding whether a theme should become formal Knowledge.

## Performance Evaluation Engine

Compass Lab 04 adds Performance Evaluation.

Files:

```text
lab/performance/performance_engine.py
lab/performance/evaluator.py
lab/performance/benchmark.py
lab/performance/metrics.py
lab/performance/report_generator.py
```

Run:

```python
from lab.performance.performance_engine import PerformanceEngine

PerformanceEngine.run()
```

Evaluation targets:

```text
Discovery
Discovery Score
Confidence
Theme
Pattern
Market Intelligence
Sector Intelligence
```

Standard periods:

```text
30 days
90 days
180 days
365 days
```

Benchmarks:

```text
S&P500
Nasdaq100
Russell2000
```

Metrics:

```text
Discovery Success Rate
Average Return
Median Return
Win Rate
Loss Rate
Alpha vs Benchmark
Max Drawdown
Average Holding Return
```

Output:

```text
reports/performance/performance_summary.md
reports/performance/discovery_accuracy.md
reports/performance/benchmark_comparison.md
reports/performance/sector_accuracy.md
reports/performance/theme_accuracy.md
reports/performance/dashboard_metrics.json
memory/performance/history.json
```

GitHub Actions:

```text
.github/workflows/performance_evaluation.yml
```

The workflow runs weekly and is independent from the daily pipeline.

Performance Evaluation is not Feedback, Decision, or Learning. It is Compass's scorecard. Future Portfolio integration can use these metrics to compare research signals with realized portfolio outcomes.

## Strategy Evaluation Engine

Compass Lab 05 adds Strategy Evaluation.

Files:

```text
lab/strategy/strategy_engine.py
lab/strategy/strategy_runner.py
lab/strategy/strategy_metrics.py
lab/strategy/portfolio_simulator.py
lab/strategy/allocation_engine.py
```

Configuration:

```text
config/strategy.yaml
```

Initial strategies:

```text
Discovery Score 90+
Discovery Score 85+
High Confidence Only
AI Theme
Semiconductor Theme
Momentum Top
Growth Pattern Match
Composite Strategy
```

Simulation:

```text
Initial capital: 100000 USD
Position sizing: equal weight
Default holding period: 180 days
No real orders
No brokerage connection
```

Risk and portfolio metrics:

```text
CAGR
Total Return
Win Rate
Sharpe Ratio
Max Drawdown
Alpha
Beta
Volatility
Average Holding Period
```

Benchmarks:

```text
S&P500
Nasdaq100
```

Output:

```text
reports/strategy/strategy_summary.md
reports/strategy/portfolio_report.md
reports/strategy/benchmark_report.md
reports/strategy/strategy_ranking.md
reports/strategy/dashboard.json
memory/strategy/strategy_history.json
```

GitHub Actions:

```text
.github/workflows/strategy_evaluation.yml
```

The workflow runs weekly and can also be started manually.

Strategy Evaluation is research-only. It evaluates Compass algorithms and rule sets; it is not investment advice, trade execution, or portfolio management.

## Experiment Engine

Compass Lab 06 adds Experiment Evaluation.

Files:

```text
lab/experiments/experiment_engine.py
lab/experiments/experiment_runner.py
lab/experiments/experiment_registry.py
lab/experiments/comparator.py
lab/experiments/experiment_report.py
```

Configuration:

```text
config/experiments.yaml
```

Experiment fields:

```text
Experiment ID
Name
Description
Target
Baseline Version
Candidate Version
Start Date
End Date
Status
```

Targets:

```text
Discovery Rule
Scoring Rule
Theme Rule
Pattern Rule
Learning Rule
Data Source
```

Comparison metrics:

```text
Discovery Success Rate
Average Return
Alpha
Win Rate
Max Drawdown
Sharpe Ratio
Strategy Ranking
Performance Score
```

Output:

```text
reports/experiments/experiment_summary.md
reports/experiments/experiment_results.md
reports/experiments/experiment_comparison.md
reports/experiments/dashboard.json
memory/experiments/registry.json
```

Winner:

```text
Baseline
Candidate
Tie
Inconclusive
```

GitHub Actions:

```text
.github/workflows/experiment_evaluation.yml
```

Experiments run weekly or manually. They are not part of the daily production workflow.

Experiment Engine is Compass's reproducible A/B testing layer. It records whether a change improved Compass, but it does not promote candidates or modify Knowledge automatically.

## Knowledge Graph Engine

Compass Lab 07 adds a Knowledge Graph Engine for managing relationships between companies, themes, sectors, events, products, technologies, countries, and ETFs.

Files:

```text
lab/knowledge_graph/graph_engine.py
lab/knowledge_graph/graph_builder.py
lab/knowledge_graph/graph_storage.py
lab/knowledge_graph/graph_query.py
lab/knowledge_graph/graph_similarity.py
```

Run locally:

```bash
python -m lab.knowledge_graph.graph_engine
```

Storage:

```text
storage/knowledge_graph/graph.json
storage/knowledge_graph/nodes.json
storage/knowledge_graph/edges.json
```

Reports:

```text
reports/graph/graph_summary.md
reports/graph/company_network.md
reports/graph/theme_network.md
reports/graph/graph.json
```

Node types:

```text
Company
Theme
Sector
Event
Product
Technology
CEO
Country
ETF
```

Relationships:

```text
BELONGS_TO
RELATED_TO
SUPPLIES
COMPETES_WITH
PARTNERS_WITH
USES
INVESTS_IN
ACQUIRES
```

Query API:

```python
Graph.find_related("NVDA")
Graph.find_theme("AI")
Graph.shortest_path("TSMC", "OpenAI")
```

GitHub Actions:

```text
.github/workflows/knowledge_graph.yml
```

The graph is refreshed weekly or manually. It is a Knowledge Layer and does not change scoring, Discovery rules, or Learning automatically.
