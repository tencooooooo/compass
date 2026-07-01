from collectors.data_expansion import DisabledCollector


class AnalystCollector(DisabledCollector):
    """Scaffold for analyst consensus and EPS estimate data."""

    category = "analyst"
    data_categories = ("Consensus", "EPS Estimates")
    source_name = "Analyst data providers"
