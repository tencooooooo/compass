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

Current limitation:

- Historical revenue growth is not fully modeled yet.
- The current version uses latest available financial data as a proxy.
- Future versions should use multi-period financial statements.

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

Valuation score is not a cheapness judgment. It is a way to flag valuation pressure for additional research.

## Momentum

Uses:

- 1 month price change
- 3 month price change
- 6 month price change
- 1 year price change
- Volume

Momentum is context, not a standalone decision rule.

## News

Uses:

- Recent news count
- Simple positive and negative keyword classification
- Event Database price reaction when available

News scoring should improve over time with better event classification and market psychology analysis.

## Explainability Rule

Every score must include:

- Score
- Reasons
- Evidence sources
- Used metrics
- Missing data

No black-box score is allowed.
