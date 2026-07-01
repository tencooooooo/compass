from datasources.base.datasource import ScaffoldDataSource


class AlphaVantageProvider(ScaffoldDataSource):
    """Scaffold provider for Alpha Vantage market data."""

    name = "alpha_vantage"
    source_label = "Alpha Vantage"
    requires_api_key = True
    api_key_env = "ALPHA_VANTAGE_API_KEY"
