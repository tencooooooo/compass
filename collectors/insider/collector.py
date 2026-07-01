from collectors.data_expansion import DisabledCollector


class InsiderCollector(DisabledCollector):
    """Scaffold for insider buying and selling data."""

    category = "insider"
    data_categories = ("Insider Buying", "Insider Selling")
    source_name = "Insider transaction data providers"
