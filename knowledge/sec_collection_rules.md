# SEC Collection Rules

SEC EDGAR is a primary-source data provider.

Collection rules:

- Declare a User-Agent for every request.
- Prefer `SEC_USER_AGENT` from GitHub Secrets or local environment.
- Respect SEC fair access guidance.
- Keep requests below SEC's current maximum request rate.
- Use retry handling for transient failures.
- Avoid duplicate downloads by checking accession numbers and existing files.
- Store raw filings separately from metadata.
- Sort filing indexes by filing date in descending order.
- Validate required metadata before saving.
- Confirm JSON metadata and index files can be parsed after writing.

Compass currently collects and stores filings only. It does not summarize, score, or interpret filing text in this layer.
