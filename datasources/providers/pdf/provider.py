from datasources.base.datasource import ScaffoldDataSource


class PDFProvider(ScaffoldDataSource):
    """Scaffold provider for future IR presentation and PDF parsing."""

    name = "pdf"
    source_label = "Local or remote PDF documents"
    requires_api_key = False
