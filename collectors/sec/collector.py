from collectors.data_expansion import DisabledCollector


class SECCollector(DisabledCollector):
    """Scaffold for SEC filings including 10-K, 10-Q, and 8-K."""

    category = "sec"
    data_categories = ("10-K", "10-Q", "8-K")
    source_name = "SEC filings"
    requires_api_key = False
