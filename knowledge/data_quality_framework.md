# Data Quality Framework

Data Quality Engine evaluates Compass input data before analysis starts.

It assigns a provider-level score for:

- Freshness
- Completeness
- Reliability
- Duplicate risk
- Consistency

The engine writes quality artifacts to `storage/quality/` and user-facing reports to `reports/data_quality/`.

Data Quality does not stop the Compass workflow. Low scores create warnings so humans can understand how reliable the next analysis run is.

