# Earnings Call Structure

Compass stores earnings call transcripts as long-term primary-source commentary.

Storage:

```text
storage/raw/earnings/{ticker}/
  transcripts/
  metadata/
  index.json
```

Transcript body:

- paragraphs
- opening_remarks
- financial_highlights
- guidance
- qa_section
- closing_remarks

Metadata:

- ticker
- company_name
- fiscal_quarter
- earnings_date
- transcript_date
- source
- language
- participants
- ceo_name
- cfo_name

The transcript text should be preserved before any AI-generated summary or scoring is added.
