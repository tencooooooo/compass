# Data Validation Policy

Compass validates data before analysis.

Policy:

- Warnings are preferred over workflow failure.
- Analysis should continue unless a collector itself fails.
- Data quality output must explain the issue category and provider.
- Primary source data is not modified by validation.
- Quality history is retained for trend review.

Future policy additions may include provider-specific thresholds, quarantine folders, and source-level confidence propagation into scoring.

