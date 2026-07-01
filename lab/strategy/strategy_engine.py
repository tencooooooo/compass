from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from api.services.data_loader import REPO_ROOT
from lab.strategy.strategy_runner import StrategyRunner


class StrategyEngine:
    """Generates research-only virtual strategy evaluation outputs."""

    @classmethod
    def run(cls) -> dict[str, Any]:
        result = StrategyRunner().run()
        outputs = cls._write_reports(result)
        history_path = cls._write_history(result)
        return {
            "success": True,
            "evaluation_date": result["evaluation_date"],
            "strategies": len(result.get("results", [])),
            "outputs": outputs,
            "history": str(history_path.relative_to(REPO_ROOT)),
        }

    @classmethod
    def _write_reports(cls, result: dict[str, Any]) -> dict[str, str]:
        output_dir = REPO_ROOT / "reports" / "strategy"
        output_dir.mkdir(parents=True, exist_ok=True)
        files = {
            "summary": output_dir / "strategy_summary.md",
            "portfolio": output_dir / "portfolio_report.md",
            "benchmark": output_dir / "benchmark_report.md",
            "ranking": output_dir / "strategy_ranking.md",
            "dashboard": output_dir / "dashboard.json",
        }
        files["summary"].write_text(cls._summary(result), encoding="utf-8")
        files["portfolio"].write_text(cls._portfolio_report(result), encoding="utf-8")
        files["benchmark"].write_text(cls._benchmark_report(result), encoding="utf-8")
        files["ranking"].write_text(cls._ranking(result), encoding="utf-8")
        files["dashboard"].write_text(json.dumps(cls._dashboard(result), ensure_ascii=False, indent=2), encoding="utf-8")
        return {name: str(path.relative_to(REPO_ROOT)) for name, path in files.items()}

    @classmethod
    def _write_history(cls, result: dict[str, Any]) -> Path:
        path = REPO_ROOT / "memory" / "strategy" / "strategy_history.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        history = []
        if path.exists():
            try:
                history = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                history = []
        for row in result.get("results", []):
            history.append(
                {
                    "evaluation_date": result["evaluation_date"],
                    "strategy_id": row["strategy_id"],
                    "label": row["label"],
                    "total_return": row["metrics"].get("total_return"),
                    "cagr": row["metrics"].get("cagr"),
                    "win_rate": row["metrics"].get("win_rate"),
                    "max_drawdown": row["metrics"].get("max_drawdown"),
                    "selected_count": row.get("selected_count"),
                }
            )
        path.write_text(json.dumps(history, ensure_ascii=False, indent=2), encoding="utf-8")
        return path

    @classmethod
    def _summary(cls, result: dict[str, Any]) -> str:
        lines = [
            "# Strategy Summary",
            "",
            "Strategy Evaluation is a research simulation. It is not trading, portfolio management, or investment advice.",
            "",
            f"- Evaluation date: {result['evaluation_date']}",
            f"- Signal date: {result['signal_date']}",
            f"- Initial capital: {result['initial_capital']} USD",
            f"- Strategies: {len(result.get('results', []))}",
            "",
        ]
        for row in result.get("results", []):
            metrics = row["metrics"]
            lines.extend(
                [
                    f"## {row['label']}",
                    "",
                    f"- Selected positions: {row['selected_count']}",
                    f"- Total Return: {cls._fmt(metrics.get('total_return'))}",
                    f"- CAGR: {cls._fmt(metrics.get('cagr'))}",
                    f"- Win Rate: {cls._fmt(metrics.get('win_rate'))}",
                    f"- Sharpe Ratio: {metrics.get('sharpe_ratio') if metrics.get('sharpe_ratio') is not None else 'N/A'}",
                    f"- Max Drawdown: {cls._fmt(metrics.get('max_drawdown'))}",
                    "",
                ]
            )
        return "\n".join(lines)

    @classmethod
    def _portfolio_report(cls, result: dict[str, Any]) -> str:
        lines = ["# Portfolio Report", ""]
        for row in result.get("results", []):
            simulation = row["simulation"]
            lines.extend([f"## {row['label']}", "", "### Holdings", ""])
            if not simulation.get("holdings"):
                lines.append("- No holdings selected.")
            for holding in simulation.get("holdings", []):
                lines.append(f"- {holding['ticker']}: weight {holding['weight']}, score {holding.get('discovery_score')}, confidence {holding.get('confidence')}")
            lines.extend(["", "### Trades", ""])
            if not simulation.get("trades"):
                lines.append("- No trades simulated.")
            for trade in simulation.get("trades", []):
                maturity = "matured" if trade.get("matured") else "partial"
                lines.append(
                    f"- {trade['ticker']}: {trade['entry_date']} -> {trade['exit_date']} "
                    f"(target {trade.get('target_exit_date')}, {maturity}), return {trade['return_percent']}%"
                )
            lines.append("")
        return "\n".join(lines)

    @classmethod
    def _benchmark_report(cls, result: dict[str, Any]) -> str:
        lines = ["# Benchmark Report", "", "Benchmarks: S&P500 and Nasdaq100. Benchmark values are N/A until SPY/QQQ price files are available.", ""]
        for row in result.get("results", []):
            lines.extend(
                [
                    f"## {row['label']}",
                    "",
                    f"- Strategy return: {cls._fmt(row['metrics'].get('total_return'))}",
                    f"- Benchmark return: {cls._fmt(row.get('benchmark_return'))}",
                    f"- Alpha: {cls._fmt(row['metrics'].get('alpha'))}",
                    "",
                ]
            )
        return "\n".join(lines)

    @classmethod
    def _ranking(cls, result: dict[str, Any]) -> str:
        rows = sorted(result.get("results", []), key=lambda row: row["metrics"].get("total_return") or -999, reverse=True)
        lines = ["# Strategy Ranking", ""]
        for index, row in enumerate(rows, start=1):
            lines.append(f"{index}. {row['label']} - Total Return {cls._fmt(row['metrics'].get('total_return'))}, Positions {row['selected_count']}")
        return "\n".join(lines) + "\n"

    @classmethod
    def _dashboard(cls, result: dict[str, Any]) -> dict[str, Any]:
        return {
            "evaluation_date": result["evaluation_date"],
            "signal_date": result["signal_date"],
            "initial_capital": result["initial_capital"],
            "strategies": [
                {
                    "strategy_id": row["strategy_id"],
                    "label": row["label"],
                    "selected_count": row["selected_count"],
                    "metrics": row["metrics"],
                    "status": row["simulation"].get("status"),
                }
                for row in result.get("results", [])
            ],
        }

    @classmethod
    def _fmt(cls, value: Any) -> str:
        if value is None:
            return "N/A"
        return f"{value:.2f}%" if isinstance(value, float) else str(value)


if __name__ == "__main__":
    print(StrategyEngine.run())
