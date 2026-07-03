from typing import Any

from api.services.data_loader import REPO_ROOT
from lab.pattern_intelligence.pattern_classifier import PatternClassifier
from lab.pattern_intelligence.pattern_extractor import PatternExtractor
from lab.pattern_intelligence.similarity_engine import SimilarityEngine


class PatternEngine:
    """Generates explainable pattern candidates for human Knowledge review."""

    @classmethod
    def run(cls) -> dict[str, Any]:
        features = PatternExtractor().extract()
        patterns = PatternClassifier().classify(features)
        similarity = SimilarityEngine().calculate(features)
        outputs = cls._write_reports(patterns, similarity, features)
        return {
            "success": True,
            "company_count": len(features.get("companies", {})),
            "success_pattern_count": len(patterns.get("success_patterns", [])),
            "failure_pattern_count": len(patterns.get("failure_patterns", [])),
            "outputs": outputs,
        }

    @classmethod
    def _write_reports(cls, patterns: dict[str, Any], similarity: dict[str, Any], features: dict[str, Any]) -> dict[str, str]:
        output_dir = REPO_ROOT / "reports" / "patterns"
        output_dir.mkdir(parents=True, exist_ok=True)
        files = {
            "success": output_dir / "success_patterns.md",
            "failure": output_dir / "failure_patterns.md",
            "similarity": output_dir / "similarity_report.md",
            "summary": output_dir / "pattern_summary.md",
        }
        files["success"].write_text(cls._pattern_report("Success Patterns", patterns.get("success_patterns", [])), encoding="utf-8")
        files["failure"].write_text(cls._pattern_report("Failure Patterns", patterns.get("failure_patterns", [])), encoding="utf-8")
        files["similarity"].write_text(cls._similarity_report(similarity), encoding="utf-8")
        files["summary"].write_text(cls._summary_report(patterns, features), encoding="utf-8")
        return {name: str(path.relative_to(REPO_ROOT)) for name, path in files.items()}

    @classmethod
    def _pattern_report(cls, title: str, patterns: list[dict[str, Any]]) -> str:
        lines = [f"# {title}", "", "Pattern candidates require human review before Knowledge updates.", ""]
        if not patterns:
            lines.append("No pattern candidates were generated.")
        for pattern in patterns:
            lines.extend(
                [
                    f"## {pattern['name']}",
                    "",
                    f"- Confidence: {pattern['confidence']}",
                    f"- Evidence: {pattern['evidence']}",
                    f"- Companies: {', '.join(pattern['tickers'])}",
                    "- Knowledge update: candidate only",
                    "",
                ]
            )
        return "\n".join(lines) + "\n"

    @classmethod
    def _similarity_report(cls, similarity: dict[str, Any]) -> str:
        lines = ["# Similarity Report", ""]
        for ticker, rows in sorted(similarity.items()):
            lines.extend([f"## {ticker}", ""])
            for row in rows:
                lines.append(f"- {row['ticker']}: {row['similarity']} ({'; '.join(row['reasons'])})")
            lines.append("")
        return "\n".join(lines)

    @classmethod
    def _summary_report(cls, patterns: dict[str, Any], features: dict[str, Any]) -> str:
        lines = [
            "# Pattern Summary",
            "",
            f"- Companies analyzed: {len(features.get('companies', {}))}",
            f"- Success patterns: {len(patterns.get('success_patterns', []))}",
            f"- Failure patterns: {len(patterns.get('failure_patterns', []))}",
            f"- Sector patterns: {len(patterns.get('sector_patterns', []))}",
            f"- Market patterns: {len(patterns.get('market_patterns', []))}",
            f"- Event patterns: {len(patterns.get('event_patterns', []))}",
            f"- Discovery history snapshots: {len(features.get('discovery_history', {}))}",
            f"- Time Machine reports: {len(features.get('time_machine', []))}",
            f"- Learning history entries: {len(features.get('learning', [])) if isinstance(features.get('learning'), list) else 0}",
            "",
            "## Confidence Note",
            "",
            "Validation history is still limited. Patterns are candidates for human review, not automatic Knowledge updates.",
            "",
            "## Pattern Groups",
            "",
        ]
        for group, group_patterns in patterns.items():
            lines.append(f"### {group.replace('_', ' ').title()}")
            for pattern in group_patterns:
                lines.append(f"- {pattern['name']}: {pattern['confidence']} confidence")
            lines.append("")
        return "\n".join(lines)


if __name__ == "__main__":
    print(PatternEngine.run())
