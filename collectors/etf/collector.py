from collectors.data_expansion import DisabledCollector


class ETFCollector(DisabledCollector):
    """Scaffold for ETF fund flows and holdings exposure data."""

    category = "etf"
    data_categories = ("Fund Flows", "Holdings Weight")
    source_name = "ETF data providers"
