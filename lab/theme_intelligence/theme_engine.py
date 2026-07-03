from typing import Any

from api.services.data_loader import REPO_ROOT
from lab.theme_intelligence.theme_classifier import ThemeClassifier
from lab.theme_intelligence.theme_similarity import ThemeSimilarity
from lab.theme_intelligence.theme_tracker import ThemeTracker


class ThemeEngine:
    """Generates investment theme intelligence reports without changing Knowledge."""

    @classmethod
    def run(cls) -> dict[str, Any]:
        classified = ThemeClassifier().classify()
        tracker = ThemeTracker()
        themes = tracker.track(classified)
        ranking = tracker.ranking(themes)
        similarity = ThemeSimilarity().calculate(themes)
        outputs = cls._write_reports(themes, ranking, similarity)
        active_themes = sum(1 for item in themes.values() if item.get("company_count", 0) > 0)
        return {
            "success": True,
            "theme_count": len(themes),
            "active_theme_count": active_themes,
            "outputs": outputs,
        }

    @classmethod
    def _write_reports(
        cls,
        themes: dict[str, Any],
        ranking: list[dict[str, Any]],
        similarity: dict[str, Any],
    ) -> dict[str, str]:
        output_dir = REPO_ROOT / "reports" / "themes"
        output_dir.mkdir(parents=True, exist_ok=True)
        files = {
            "summary": output_dir / "theme_summary.md",
            "ranking": output_dir / "theme_ranking.md",
            "similarity": output_dir / "theme_similarity.md",
        }
        files["summary"].write_text(cls._summary_report(themes), encoding="utf-8")
        files["ranking"].write_text(cls._ranking_report(ranking), encoding="utf-8")
        files["similarity"].write_text(cls._similarity_report(similarity), encoding="utf-8")
        for theme, item in themes.items():
            path = output_dir / f"{cls._safe_name(theme)}.md"
            path.write_text(cls._detail_report(theme, item, similarity.get(theme, [])), encoding="utf-8")
            files[f"detail_{theme}"] = path
        return {name: str(path.relative_to(REPO_ROOT)) for name, path in files.items()}

    @classmethod
    def _summary_report(cls, themes: dict[str, Any]) -> str:
        lines = [
            "# Theme Summary",
            "",
            "Theme Intelligence connects market, sector, company, Discovery, and Pattern context. Reports are candidates for human research, not investment advice.",
            "",
        ]
        for theme, item in sorted(themes.items()):
            representatives = ", ".join(row["ticker"] for row in item.get("representative_companies", [])[:3]) or "None"
            market = cls._market_line(item.get("market_status", []))
            news = item.get("major_news", [])
            lines.extend(
                [
                    f"## {theme}",
                    "",
                    f"- Target companies: {item.get('company_count', 0)}",
                    f"- Average Score: {cls._fmt(item.get('average_score'))}",
                    f"- Average Discovery: {cls._fmt(item.get('average_discovery'))}",
                    f"- Market status: {market}",
                    f"- Representative companies: {representatives}",
                    f"- Confidence: {item.get('confidence', 'Low')}",
                ]
            )
            if news:
                lines.append("- Major news:")
                for row in news[:3]:
                    lines.append(f"  - {row['ticker']}: {row['title']}")
            lines.append("")
        return "\n".join(lines)

    @classmethod
    def _ranking_report(cls, ranking: list[dict[str, Any]]) -> str:
        lines = ["# Theme Ranking", "", "Ranking combines Score, Discovery, momentum, validation, and theme breadth.", ""]
        for index, row in enumerate(ranking, start=1):
            validation = row.get("validation", {})
            lines.extend(
                [
                    f"## {index}. {row['theme']}",
                    "",
                    f"- Momentum: {cls._fmt(row.get('momentum'))}",
                    f"- Discovery companies: {row.get('discovery_count', 0)}",
                    f"- Validation: Excellent {validation.get('Excellent', 0)}, Good {validation.get('Good', 0)}, Neutral {validation.get('Neutral', 0)}, Poor {validation.get('Poor', 0)}",
                    f"- Ranking score: {row.get('rank_score')}",
                    "",
                ]
            )
        return "\n".join(lines)

    @classmethod
    def _similarity_report(cls, similarity: dict[str, Any]) -> str:
        lines = ["# Theme Similarity", ""]
        for theme, rows in sorted(similarity.items()):
            lines.extend([f"## {theme}", ""])
            if not rows:
                lines.append("- No comparable themes yet.")
            for row in rows:
                lines.append(f"- {row['theme']}: {row['similarity']} ({'; '.join(row['reasons'])})")
            lines.append("")
        return "\n".join(lines)

    @classmethod
    def _detail_report(cls, theme: str, item: dict[str, Any], similarity: list[dict[str, Any]]) -> str:
        lines = [
            f"# {theme}",
            "",
            f"- Target companies: {item.get('company_count', 0)}",
            f"- Average Score: {cls._fmt(item.get('average_score'))}",
            f"- Average Discovery: {cls._fmt(item.get('average_discovery'))}",
            f"- Momentum: {cls._fmt(item.get('momentum', {}).get('average_1m'))}",
            f"- Confidence: {item.get('confidence', 'Low')}",
            "",
            "## Companies",
            "",
        ]
        if not item.get("companies"):
            lines.append("No companies are classified into this theme yet.")
        for company in item.get("companies", []):
            evidence = "; ".join(company.get("evidence", [])) or "No evidence"
            lines.append(f"- {company['ticker']} - {company['company_name']} ({company.get('confidence', 'Low')}): {evidence}")
        lines.extend(["", "## Market", ""])
        for sector in item.get("market_status", []):
            trend = sector.get("trend", {})
            lines.append(
                f"- {sector.get('sector')}: score {cls._fmt(sector.get('average_score'))}, "
                f"momentum {cls._fmt(sector.get('average_momentum_1m'))}, trend {trend}"
            )
        lines.extend(["", "## Major News", ""])
        for row in item.get("major_news", []):
            lines.append(f"- {row['ticker']}: {row['title']}")
        if not item.get("major_news"):
            lines.append("No theme news available yet.")
        lines.extend(["", "## Similar Themes", ""])
        for row in similarity[:5]:
            lines.append(f"- {row['theme']}: {row['similarity']} ({'; '.join(row['reasons'])})")
        if not similarity:
            lines.append("No similar themes available yet.")
        lines.extend(["", "## Review Note", "", "Theme reports support long-term research context and do not update Knowledge automatically.", ""])
        return "\n".join(lines)

    @classmethod
    def _market_line(cls, sectors: list[dict[str, Any]]) -> str:
        if not sectors:
            return "Unknown"
        return ", ".join(f"{row.get('sector')} {row.get('trend', {}).get('momentum', 'Unknown')}" for row in sectors[:3])

    @classmethod
    def _safe_name(cls, value: str) -> str:
        return value.replace("/", "_").replace(" ", "_")

    @classmethod
    def _fmt(cls, value: Any) -> str:
        if value is None:
            return "N/A"
        if isinstance(value, float):
            return f"{value:.2f}"
        return str(value)


if __name__ == "__main__":
    print(ThemeEngine.run())
