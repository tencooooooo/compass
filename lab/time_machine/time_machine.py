import json
from typing import Any

from api.services.data_loader import REPO_ROOT
from lab.time_machine.historical_context import HistoricalContext
from lab.time_machine.snapshot_loader import SnapshotLoader
from lab.time_machine.timeline_builder import TimelineBuilder


class TimeMachine:
    """Historical Replay engine that blocks future data."""

    @classmethod
    def run(cls, date: str) -> dict[str, Any]:
        snapshot = SnapshotLoader(date).load()
        context = HistoricalContext(snapshot).build()
        timeline = TimelineBuilder().build(context)
        discovery = cls._build_discovery(timeline)
        market = context.get("market", {})
        outputs = cls._write_reports(date, snapshot, context, discovery, market)
        return {
            "success": True,
            "date": date,
            "data_range": context.get("data_range"),
            "company_count": len(context.get("companies", {})),
            "discovery_count": len(discovery),
            "outputs": outputs,
        }

    @classmethod
    def _build_discovery(cls, timeline: list[dict[str, Any]]) -> list[dict[str, Any]]:
        candidates = []
        for item in timeline[:10]:
            score = item.get("score") or 0
            if score < 50:
                continue
            candidates.append(
                {
                    "ticker": item.get("ticker"),
                    "score": score,
                    "confidence": item.get("confidence"),
                    "reason": "Historical replay score and available evidence met the discovery threshold.",
                }
            )
        return candidates

    @classmethod
    def _write_reports(
        cls,
        snapshot_date: str,
        snapshot: dict[str, Any],
        context: dict[str, Any],
        discovery: list[dict[str, Any]],
        market: dict[str, Any],
    ) -> dict[str, str]:
        output_dir = REPO_ROOT / "reports" / "timemachine"
        output_dir.mkdir(parents=True, exist_ok=True)
        paths = {
            "snapshot": output_dir / f"snapshot_{snapshot_date}.md",
            "discovery": output_dir / f"discovery_{snapshot_date}.md",
            "market": output_dir / f"market_{snapshot_date}.md",
        }
        paths["snapshot"].write_text(cls._snapshot_report(snapshot_date, snapshot, context, discovery, market), encoding="utf-8")
        paths["discovery"].write_text(cls._discovery_report(snapshot_date, discovery), encoding="utf-8")
        paths["market"].write_text(cls._market_report(snapshot_date, market), encoding="utf-8")
        return {name: str(path.relative_to(REPO_ROOT)) for name, path in paths.items()}

    @classmethod
    def _snapshot_report(cls, snapshot_date: str, snapshot: dict[str, Any], context: dict[str, Any], discovery: list[dict[str, Any]], market: dict[str, Any]) -> str:
        data_range = context.get("data_range", {})
        lines = [
            f"# Time Machine Snapshot {snapshot_date}",
            "",
            "## Historical Replay Policy",
            "",
            "Only data dated on or before the snapshot date was loaded. Future-dated records were excluded before scoring, discovery, or market summaries were generated.",
            "",
            "## Data Range",
            "",
            f"- Snapshot date: {snapshot_date}",
            f"- Price start: {data_range.get('price_start')}",
            f"- Price end: {data_range.get('price_end')}",
            f"- Company count: {len(context.get('companies', {}))}",
            f"- Discovery candidates: {len(discovery)}",
            f"- Sector count: {market.get('sector_count', 0)}",
            "",
            "## Discovery Candidates",
            "",
        ]
        lines.extend(f"- {item['ticker']}: score {item['score']} / confidence {item['confidence']}" for item in discovery)
        lines.extend(["", "## Snapshot Metadata", "", "```json", json.dumps({"knowledge_policy": snapshot.get("knowledge", {}).get("policy")}, indent=2), "```"])
        return "\n".join(lines) + "\n"

    @classmethod
    def _discovery_report(cls, snapshot_date: str, discovery: list[dict[str, Any]]) -> str:
        lines = [f"# Time Machine Discovery {snapshot_date}", ""]
        if not discovery:
            lines.append("No historical discovery candidates were generated for this snapshot.")
        for item in discovery:
            lines.extend(
                [
                    f"## {item['ticker']}",
                    "",
                    f"- Score: {item['score']}",
                    f"- Confidence: {item['confidence']}",
                    f"- Reason: {item['reason']}",
                    "",
                ]
            )
        return "\n".join(lines) + "\n"

    @classmethod
    def _market_report(cls, snapshot_date: str, market: dict[str, Any]) -> str:
        lines = [
            f"# Time Machine Market {snapshot_date}",
            "",
            f"- Ticker count: {market.get('ticker_count', 0)}",
            f"- Sector count: {market.get('sector_count', 0)}",
            "",
            "## Sectors",
            "",
        ]
        for sector in market.get("sectors", []):
            lines.append(f"- {sector['sector']}: average score {sector['average_score']} / tickers {', '.join(sector['tickers'])}")
        return "\n".join(lines) + "\n"


if __name__ == "__main__":
    print(json.dumps(TimeMachine.run(date="2024-03-01"), indent=2))
