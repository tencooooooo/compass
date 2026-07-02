# Quality Metrics

Data Quality Score is a 100 point score.

Initial weighting:

- Freshness: 25%
- Completeness: 30%
- Reliability: 25%
- Duplicate score: 10%
- Consistency: 10%

Freshness measures file update recency against expected provider cadence.

Completeness checks required fields, missing values, and null rate.

Reliability scores source strength: primary, market data, secondary, derived, estimated, or future provider.

Duplicate checks detect repeated local records or copied files.

Consistency checks detect simple cross-record conflicts such as malformed ticker identity.

