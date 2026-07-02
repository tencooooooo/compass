from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]

from collectors.earnings.transcript_client import TranscriptClient  # noqa: E402
from collectors.earnings.transcript_index import TranscriptIndex  # noqa: E402
from collectors.earnings.transcript_normalizer import TranscriptNormalizer  # noqa: E402
from collectors.earnings.transcript_parser import TranscriptParser  # noqa: E402


class EarningsTranscriptCollector:
    """Collects, parses, and stores earnings call transcripts."""

    def __init__(self, project_root: Path = PROJECT_ROOT) -> None:
        self.project_root = project_root
        self.client = TranscriptClient()
        self.parser = TranscriptParser()
        self.normalizer = TranscriptNormalizer()
        self.output_root = project_root / "storage" / "raw" / "earnings"

    def collect_ticker(
        self,
        ticker: str,
        source_path: str | None = None,
        source_url: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        raw = self.client.fetch(source_path=source_path, source_url=source_url)
        merged_metadata = {**raw.get("metadata", {}), **(metadata or {})}
        parsed = self.parser.parse(raw.get("text", ""))
        payload = self.normalizer.normalize(ticker, parsed, merged_metadata, raw["source"])
        valid, missing = self.normalizer.validate(payload)
        if not valid:
            return {"ticker": ticker.upper(), "saved": 0, "skipped": [], "errors": [f"Missing fields: {', '.join(missing)}"]}
        metadata_payload = payload["metadata"]
        transcript_id = self._transcript_id(metadata_payload)
        metadata_payload["transcript_id"] = transcript_id
        company_dir = self.output_root / ticker.upper()
        transcripts_dir = company_dir / "transcripts"
        metadata_dir = company_dir / "metadata"
        transcripts_dir.mkdir(parents=True, exist_ok=True)
        metadata_dir.mkdir(parents=True, exist_ok=True)
        transcript_path = transcripts_dir / f"{transcript_id}.json"
        metadata_path = metadata_dir / f"{transcript_id}.json"
        index = TranscriptIndex(company_dir)
        if index.exists(transcript_id) and transcript_path.exists() and metadata_path.exists():
            return {
                "ticker": ticker.upper(),
                "saved": 1,
                "skipped": [transcript_id],
                "errors": [],
                "index_path": str(index.path.relative_to(self.project_root)),
            }
        transcript_path.write_text(json.dumps(payload["transcript"], ensure_ascii=False, indent=2), encoding="utf-8")
        metadata_path.write_text(json.dumps(metadata_payload, ensure_ascii=False, indent=2), encoding="utf-8")
        json.loads(transcript_path.read_text(encoding="utf-8"))
        json.loads(metadata_path.read_text(encoding="utf-8"))
        index_path = index.update(ticker, [metadata_payload])
        return {
            "ticker": ticker.upper(),
            "saved": 1,
            "skipped": [],
            "errors": [],
            "transcript_id": transcript_id,
            "index_path": str(index_path.relative_to(self.project_root)),
        }

    def run(
        self,
        ticker: str,
        source_path: str | None = None,
        source_url: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        result = self.collect_ticker(ticker, source_path=source_path, source_url=source_url, metadata=metadata)
        return {"success": not result.get("errors"), "results": [result]}

    def _transcript_id(self, metadata: dict[str, Any]) -> str:
        seed = "|".join(
            [
                str(metadata.get("ticker")),
                str(metadata.get("fiscal_quarter")),
                str(metadata.get("earnings_date")),
                str(metadata.get("source")),
            ]
        )
        digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()[:12]
        return f"{metadata.get('ticker')}_{metadata.get('fiscal_quarter')}_{digest}".replace(" ", "_")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch and store earnings call transcripts.")
    parser.add_argument("--ticker", required=True)
    parser.add_argument("--source-path")
    parser.add_argument("--source-url")
    parser.add_argument("--company-name")
    parser.add_argument("--fiscal-quarter", default="Unknown")
    parser.add_argument("--earnings-date")
    parser.add_argument("--transcript-date")
    parser.add_argument("--source")
    parser.add_argument("--language", default="en")
    parser.add_argument("--ceo-name")
    parser.add_argument("--cfo-name")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    metadata = {
        "company_name": args.company_name or args.ticker.upper(),
        "fiscal_quarter": args.fiscal_quarter,
        "earnings_date": args.earnings_date,
        "transcript_date": args.transcript_date,
        "source": args.source,
        "language": args.language,
        "ceo_name": args.ceo_name,
        "cfo_name": args.cfo_name,
    }
    metadata = {key: value for key, value in metadata.items() if value}
    result = EarningsTranscriptCollector().run(
        ticker=args.ticker,
        source_path=args.source_path,
        source_url=args.source_url,
        metadata=metadata,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("success") else 1


if __name__ == "__main__":
    raise SystemExit(main())
