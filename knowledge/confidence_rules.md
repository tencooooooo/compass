# Confidence Rules

Confidence explains how reliable the score is based on available data.

It is not a judgment about whether a company is good or bad, and it is not a measure of how strong the signals are. Signal strength is reported separately (see Signal Strength below).

## Levels

```text
High
Medium
Low
```

## High

Use High when:

- Prices are available
- Financial data is available
- Company profile and valuation data are available
- News data is available
- Missing data is limited

## Medium

Use Medium when:

- Most major data sources are available
- Some fields are missing
- Event reaction data may be incomplete
- The score can be used, but should be reviewed with caution

## Low

Use Low when:

- Multiple major data sources are missing
- Financial or price data is unavailable
- News data is sparse
- Event reaction data is unavailable

## What does not affect Confidence

Data that is present but weak must not lower Confidence:

- Negative EPS, FCF, revenue, or missing-growth signals with data present are weak signals, not missing data
- A category score of 0 with full data means the signals are weak, not that data is unavailable

These cases are recorded as `weak_signals` and reflected in Signal Strength instead.

## Signal Strength

Signal Strength explains how strong the observed signals are, evaluated only on the data that is actually available.

```text
Strong    signal_rate >= 65%
Moderate  signal_rate >= 40%
Weak      below 40% (or nothing evaluable)
```

`signal_rate` = earned points / maximum points achievable with the available data. Categories whose data is missing are excluded from both numerator and denominator, so Signal Strength stays independent of data coverage.

## Interpretation

Confidence and Signal Strength should always be shown beside the score.

- High Confidence + Weak Signal: the data is complete and it clearly shows weak signals
- Low Confidence + Strong Signal: the signals look strong but too much data is missing to trust them
- A high score with Low Confidence should not be treated as strong evidence

## History

Until 2026-07-20 Confidence mixed data availability with signal strength (zero-score sections counted as unavailable, and negative fundamentals counted as missing data). Confidence groupings before and after that date are not directly comparable, and validation rows recorded before it have no signal strength (they aggregate as Unknown).
