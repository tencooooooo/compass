# Sector Analysis Rules

Sector analysis compares groups of companies using company profile sector labels.

## Basic Rules

- Use `company.sector` as the primary sector label.
- If sector is missing, use `Unknown`.
- Only sectors that exist in the current ticker list are reported.
- Do not compare sectors as investment decisions.

## Average Values

Average values are useful for structure, but they can be distorted when the number of companies is small.

Current average metrics:

- Average score
- Average PER
- Average EPS
- Average 1M momentum
- News count

## Interpretation Cautions

- A sector with one or two companies should not be treated as representative of the whole market.
- High momentum does not mean the sector is attractive.
- Low valuation does not mean the sector is attractive.
- News volume can reflect attention, risk, hype, or uncertainty.
- Sector averages should be read together with individual company explanations.

## Trend Labels

Momentum:

- Strong
- Positive
- Weak
- Risk-Off
- Unknown

News:

- High
- Medium
- Low

Financial Health:

- Good
- Neutral
- Watch
- Unknown
