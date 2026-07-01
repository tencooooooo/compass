from datasources.base.datasource import ScaffoldDataSource


class SECProvider(ScaffoldDataSource):
    """Scaffold provider for SEC 10-K, 10-Q, and 8-K filings."""

    name = "sec"
    source_label = "SEC filings"
    requires_api_key = False
