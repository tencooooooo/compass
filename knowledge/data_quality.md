# Data Quality

Compass should evaluate every data source before using it in research output.

Quality dimensions:

- Source reliability
- Timeliness
- Historical depth
- Field completeness
- Ticker/entity mapping quality
- Revision policy
- Duplicate handling
- Survivorship bias
- Licensing and redistribution limits
- Explainability of derived values

Data quality rules:

- Missing data must be explicit.
- Source timestamps must be retained.
- Normalized values should not hide raw-source uncertainty.
- Derived sentiment, consensus, and trend scores require confidence labels.
- Low-quality data should reduce confidence instead of silently influencing conclusions.

The Data Expansion Engine is a foundation for better evidence. It should not create investment conclusions by itself.
