from datasources.base.datasource import ScaffoldDataSource


class FREDProvider(ScaffoldDataSource):
    """Scaffold provider for FRED macroeconomic data."""

    name = "fred"
    source_label = "FRED"
    requires_api_key = True
    api_key_env = "FRED_API_KEY"
