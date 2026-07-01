# SEC Data Model

Compass stores SEC EDGAR filings as primary-source artifacts before analysis.

Storage:

```text
storage/raw/sec/{ticker}/
  filings/
  metadata/
  index.json
```

Metadata fields:

- ticker
- company_name
- cik
- filing_type
- filing_date
- report_date
- accession_number
- source_url
- document_title
- primary_document
- acceptance_datetime
- items
- size
- is_xbrl
- is_inline_xbrl
- local_filing_path

Index:

```json
{
  "ticker": "NVDA",
  "filings": [
    {
      "type": "10-K",
      "date": "2026-02-15",
      "accession_number": "...",
      "source_url": "...",
      "document_title": "..."
    }
  ]
}
```

Filing documents are stored as facts. AI interpretation belongs in a later analysis layer.
