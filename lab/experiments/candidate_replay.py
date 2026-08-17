from __future__ import annotations

import json
from pathlib import Path
from statistics import mean
from typing import Any, Callable

from api.services.data_loader import REPO_ROOT
from engines.discovery.candidate_selector import DISCOVERY_MAX_SCORE, DISCOVERY_POINTS
from lab.performance.evaluator import Evaluator
from lab.performance.metrics import PerformanceMetrics


# candidate_selector.build_candidate と同じPrimary Candidate閾値。
PRIMARY_THRESHOLD = 75

# 過熱テーパー: ベンチマーク超過(または絶対リターン)がこの水準を超えたモメンタムは、
# 「市場を大きく上回る」満点扱いではなく既存の0.25×ティア(小幅マイナスと同じ慎重評価)に落とす仮説。
# Validation実績で3Mモメンタム20%超・高スコア帯が1mで平均回帰していたことに基づく候補ルール。
OVEREXTENSION_THRESHOLD = 30.0
OVEREXTENSION_TIER = 0.25

# Newsスコア上限: 17-20点帯(注目度の極端な高さ)が1mでマイナスαだったため、寄与を16/20で頭打ちにする仮説。
NEWS_SCORE_CAP = 16.0

MOMENTUM_KEYS = ("1m", "3m", "6m", "1y")


def baseline_momentum_award(value: float, points: float, relative: bool) -> float:
    """candidate_selector.score_from_momentum / score_from_relative_momentum と同じ配点(理由文なし)。"""
    if relative:
        if value >= 10:
            return points
        if value >= 0:
            return points * 0.65
        if value >= -10:
            return points * 0.25
        return 0.0
    if value >= 15:
        return points
    if value >= 0:
        return points * 0.65
    if value >= -10:
        return points * 0.25
    return 0.0


def tapered_momentum_award(value: float, points: float, relative: bool) -> float:
    if value >= OVEREXTENSION_THRESHOLD:
        return points * OVEREXTENSION_TIER
    return baseline_momentum_award(value, points, relative)


def momentum_taper_delta(metrics: dict[str, Any]) -> float:
    """過熱テーパーを適用した場合のDiscovery Score差分(<=0)。"""
    delta = 0.0
    momentum = metrics.get("momentum") or {}
    excess = metrics.get("excess_momentum") or {}
    use_benchmark = bool(metrics.get("benchmark"))
    for key in MOMENTUM_KEYS:
        points = DISCOVERY_POINTS[f"momentum_{key}"]
        excess_value = excess.get(key) if use_benchmark else None
        if excess_value is not None:
            value, relative = float(excess_value), True
        elif momentum.get(key) is not None:
            value, relative = float(momentum[key]), False
        else:
            continue
        delta += tapered_momentum_award(value, points, relative) - baseline_momentum_award(value, points, relative)
    return delta


def news_cap_delta(metrics: dict[str, Any]) -> float:
    """Newsスコアを上限で頭打ちにした場合のDiscovery Score差分(<=0)。"""
    news_score = metrics.get("news_score")
    if not isinstance(news_score, (int, float)) or news_score <= NEWS_SCORE_CAP:
        return 0.0
    return (NEWS_SCORE_CAP - float(news_score)) / 20 * DISCOVERY_POINTS["news_score"]


ADJUSTMENTS: dict[str, tuple[Callable[[dict[str, Any]], float], ...]] = {
    "EXP-MOM-TAPER-001": (momentum_taper_delta,),
    "EXP-NEWS-CAP-001": (news_cap_delta,),
    "EXP-OVEREXT-001": (momentum_taper_delta, news_cap_delta),
}


class CandidateReplay:
    """過去のDiscoveryスナップショットを候補ルールで再採点し、Experiment Engine用のメトリクスを生成します。

    本番のスコアリングは変更しません。スナップショットに保存された構造化メトリクス
    (momentum / excess_momentum / news_score)から候補スコアを再計算し、
    「Primary Candidate(score >= 75)を選んだ場合」の成績をbaselineと同一の価格結果で比較します。
    """

    def __init__(self, repo_root: Path = REPO_ROOT) -> None:
        self.repo_root = repo_root
        self.output_dir = repo_root / "reports" / "experiments" / "candidates"

    def run(self) -> dict[str, Any]:
        rows = Evaluator(repo_root=self.repo_root).evaluate()["rows"]
        if not rows:
            return {"success": False, "reason": "No discovery snapshots to replay."}
        metrics_by_key = self._snapshot_metrics()
        self.output_dir.mkdir(parents=True, exist_ok=True)
        outputs: dict[str, dict[str, str]] = {}
        baseline_rows = [row for row in rows if self._score(row) >= PRIMARY_THRESHOLD]
        baseline_metrics = self._scorecard(baseline_rows)
        for experiment_id, adjustments in ADJUSTMENTS.items():
            candidate_rows = []
            for row in rows:
                snapshot = metrics_by_key.get((row.get("discovery_date"), row.get("ticker")))
                score = self._score(row)
                if snapshot is not None:
                    score = max(0.0, min(float(DISCOVERY_MAX_SCORE), score + sum(adjust(snapshot) for adjust in adjustments)))
                if score >= PRIMARY_THRESHOLD:
                    candidate_rows.append(row)
            outputs[experiment_id] = self._write(experiment_id, baseline_metrics, self._scorecard(candidate_rows))
        return {"success": True, "experiments": sorted(outputs), "outputs": outputs}

    def _snapshot_metrics(self) -> dict[tuple[str, str], dict[str, Any]]:
        output: dict[tuple[str, str], dict[str, Any]] = {}
        memory_root = self.repo_root / "memory" / "discoveries"
        if not memory_root.exists():
            return output
        for path in sorted(memory_root.glob("*.json")):
            try:
                snapshot = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            if not isinstance(snapshot, dict):
                continue
            discovery_date = str(snapshot.get("date") or path.stem)
            for candidate in snapshot.get("candidates", []):
                ticker = str(candidate.get("ticker", "")).upper()
                metrics = candidate.get("metrics")
                if ticker and isinstance(metrics, dict):
                    output[(discovery_date, ticker)] = metrics
        return output

    def _score(self, row: dict[str, Any]) -> float:
        try:
            return float(row.get("discovery_score"))
        except (TypeError, ValueError):
            return 0.0

    def _scorecard(self, rows: list[dict[str, Any]]) -> dict[str, Any]:
        summary = PerformanceMetrics().summarize(rows)
        core = [summary.get("discovery_success_rate"), summary.get("average_return"), summary.get("alpha_vs_benchmark")]
        numeric = [float(value) for value in core if isinstance(value, (int, float))]
        return {
            "discovery_success_rate": summary.get("discovery_success_rate"),
            "average_return": summary.get("average_return"),
            "alpha": summary.get("alpha_vs_benchmark"),
            "win_rate": summary.get("win_rate"),
            # StrategyメトリクスはPrimary選定の再採点では再現できないため比較対象にしない。
            "max_drawdown": None,
            "sharpe_ratio": None,
            "strategy_ranking": None,
            "performance_score": round(mean(numeric), 2) if numeric else None,
            # 以下は比較キーではなく解釈用の文脈情報。
            "selected_rows": summary.get("evaluated_count"),
            "completed_rows": summary.get("completed_count"),
            "unique_tickers": summary.get("unique_ticker_count"),
            "ticker_equal_weight_alpha": summary.get("ticker_equal_weight_alpha"),
        }

    def _write(self, experiment_id: str, baseline: dict[str, Any], candidate: dict[str, Any]) -> dict[str, str]:
        paths = {
            "baseline": self.output_dir / f"{experiment_id}_baseline.json",
            "candidate": self.output_dir / f"{experiment_id}_candidate.json",
        }
        paths["baseline"].write_text(json.dumps(baseline, ensure_ascii=False, indent=2), encoding="utf-8")
        paths["candidate"].write_text(json.dumps(candidate, ensure_ascii=False, indent=2), encoding="utf-8")
        return {name: str(path.relative_to(self.repo_root)) for name, path in paths.items()}


if __name__ == "__main__":
    print(CandidateReplay().run())
