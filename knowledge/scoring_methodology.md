# Scoring Methodology

Compass Research 01 introduces the Explainable Scoring Engine.

The score is not an investment decision. It is a structured research signal that helps humans compare companies and decide where to investigate next.

## Score Structure

Total score: 100 points

Each category: 20 points

```text
Growth
Financial Health
Valuation
Momentum
News
```

## Growth

Uses:

- Revenue
- EPS
- Profit
- Research and development
- Quarterly financial time series

Method:

- The financial collector stores the latest four quarters plus the prior-year comparison quarter when available.
- Growth scoring uses revenue YoY growth and EPS YoY growth against the same quarter one year earlier.
- To reduce single-quarter noise, YoY growth is averaged across up to the latest four quarters that have a prior-year comparison quarter. The latest-quarter YoY is still reported in metrics, and acceleration or deceleration of 5 points or more versus the previous quarter is noted in reasons.
- Average YoY of +30% or more receives the strongest growth credit; +15% or more receives partial credit; negative growth receives no growth-rate credit.
- If quarterly time series data is unavailable, Compass falls back to the previous latest-value logic and records `revenue_growth` in missing data so Confidence reflects the gap.

## Financial Health

Uses:

- Cash
- Liabilities
- Shareholders' equity
- Long-term debt
- Current Ratio

The goal is to evaluate whether a company has enough financial strength to continue investing and operating through difficult periods.

## Valuation

Uses:

- PER
- Forward PER
- PEG
- PBR

Method:

- Valuation is scored relative to companies in the same sector when at least five sector peers are available.
- Lower PER, Forward PER, PEG, and PBR percentiles receive more credit: bottom 25% receives full credit, middle 50% receives partial credit, and top 25% receives no valuation credit.
- If fewer than five sector peers are available, Compass falls back to the previous fixed-threshold rules and records that fallback in the reasons.

Valuation score is not a cheapness judgment. It is a way to flag valuation pressure for additional research.

## Momentum

Uses:

- 1 month price change
- 3 month price change
- 6 month price change
- 1 year price change
- Benchmark (SPY) price change over the same windows
- Volume

Method:

- When benchmark prices are available, each window is scored on the excess return versus the benchmark (relative strength): +10pt or more over the benchmark receives full credit, at or above the benchmark receives partial credit, and small underperformance receives minimal credit.
- This removes market-wide direction from the signal: in a broad rally, only stocks that outperform the market receive strong momentum credit.
- When benchmark prices are unavailable, Compass falls back to absolute return scoring and records `benchmark_prices` in missing data so Confidence reflects the gap.

Momentum is context, not a standalone decision rule.

## News

Uses:

- Recent news count
- Boundary-aware positive, negative, and neutral keyword classification
- Event Database price reaction when available

News classification uses shared rules with word-boundary matching, phrase overrides such as cost cuts versus guidance cuts, and simple negation handling. A labeled fixture is used to measure classification accuracy and prevent silent degradation.

Sentiment scoring uses the net ratio of positive minus negative items over all classified items, not raw counts. This keeps sentiment comparable between heavily covered mega caps and lightly covered companies: 10 positive and 8 negative headlines is a mixed signal, not a strong positive one. When no item can be classified, sentiment is treated as neutral.

## Explainability Rule

Every score must include:

- Score
- Reasons
- Evidence sources
- Used metrics
- Missing data

No black-box score is allowed.
