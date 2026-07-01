from __future__ import annotations

from typing import Any


class AllocationEngine:
    """Selects strategy holdings and assigns simulated position weights."""

    def select(self, strategy: dict[str, Any], candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
        strategy_type = strategy.get("type")
        if strategy_type == "score_threshold":
            selected = [row for row in candidates if self._num(row.get("discovery_score")) >= self._num(strategy.get("score"))]
        elif strategy_type == "confidence":
            selected = [row for row in candidates if row.get("confidence") == strategy.get("confidence")]
        elif strategy_type == "theme":
            selected = [row for row in candidates if strategy.get("theme") in row.get("themes", [])]
        elif strategy_type == "momentum_top":
            selected = sorted(candidates, key=lambda row: self._num(row.get("momentum_3m")), reverse=True)[: int(strategy.get("limit", 3))]
        elif strategy_type == "pattern":
            token = str(strategy.get("pattern", "")).lower()
            selected = [row for row in candidates if any(token in item.lower() for item in row.get("patterns", []))]
        elif strategy_type == "composite":
            selected = self._composite(strategy, candidates)
        else:
            selected = []
        return self.equal_weight(selected)

    def equal_weight(self, candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
        if not candidates:
            return []
        weight = round(1 / len(candidates), 6)
        return [{**candidate, "weight": weight} for candidate in candidates]

    def _composite(self, strategy: dict[str, Any], candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
        themes = set(strategy.get("themes", []))
        patterns = [str(item).lower() for item in strategy.get("patterns", [])]
        minimum_score = self._num(strategy.get("score"))
        output = []
        for row in candidates:
            score_ok = self._num(row.get("discovery_score")) >= minimum_score
            theme_ok = bool(themes.intersection(set(row.get("themes", []))))
            pattern_ok = any(pattern in item.lower() for pattern in patterns for item in row.get("patterns", []))
            if score_ok and (theme_ok or pattern_ok):
                output.append(row)
        return output

    def _num(self, value: Any) -> float:
        try:
            return float(value or 0)
        except (TypeError, ValueError):
            return 0.0
