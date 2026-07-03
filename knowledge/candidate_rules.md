# Candidate Rules

Candidate selection is rule-based in the initial version.

## Inputs

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

## Candidate Signals

Growth:

- Revenue exists and is positive
- EPS is positive
- Profit is positive
- Research and development exists

Financial:

- Cash exists
- FCF is positive
- Current Ratio is not weak
- Debt burden is not excessive

Momentum:

- 1M
- 3M
- 6M
- 1Y
- Scored on excess return versus the SPY benchmark when benchmark prices are available, using the same relative-strength rule as the Scoring Engine. Falls back to absolute returns and records `benchmark_prices` in missing data otherwise.

News:

- Positive material keywords
- Recent news activity
- Event count
- Event reaction when available

Sector:

- Sector score relative to market
- Sector news activity
- Sector financial health
- Sector momentum context

## Important Rule

Discovery Score is not an investment score.

It is a research-candidate score. A company can be a candidate even if it has watch points, as long as the reasons are visible.
