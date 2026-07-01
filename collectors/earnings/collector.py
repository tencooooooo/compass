from collectors.data_expansion import DisabledCollector


class EarningsCollector(DisabledCollector):
    """Scaffold for earnings presentations and guidance data."""

    category = "earnings"
    data_categories = ("Earnings Presentations", "Guidance")
    source_name = "Earnings data providers"
