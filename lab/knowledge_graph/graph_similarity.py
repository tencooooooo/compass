from __future__ import annotations

from collections import defaultdict
from typing import Any


class GraphSimilarity:
    """Calculates simple graph-distance similarity for nodes."""

    def calculate(self, graph: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
        neighbors = self._neighbors(graph.get("edges", []))
        output: dict[str, list[dict[str, Any]]] = {}
        node_types = {node["id"]: node.get("type") for node in graph.get("nodes", [])}
        for node_id, node_neighbors in neighbors.items():
            rows = []
            for other_id, other_neighbors in neighbors.items():
                if node_id == other_id or node_types.get(node_id) != node_types.get(other_id):
                    continue
                score = self._jaccard(node_neighbors, other_neighbors)
                if score <= 0:
                    continue
                rows.append(
                    {
                        "node": other_id,
                        "type": node_types.get(other_id),
                        "similarity": round(score, 3),
                        "shared_neighbors": sorted(node_neighbors & other_neighbors)[:10],
                    }
                )
            output[node_id] = sorted(rows, key=lambda row: row["similarity"], reverse=True)[:10]
        return output

    def _neighbors(self, edges: list[dict[str, Any]]) -> dict[str, set[str]]:
        neighbors: dict[str, set[str]] = defaultdict(set)
        for edge in edges:
            source = edge.get("source")
            target = edge.get("target")
            if not source or not target:
                continue
            neighbors[source].add(target)
            neighbors[target].add(source)
        return neighbors

    def _jaccard(self, left: set[str], right: set[str]) -> float:
        union = left | right
        return len(left & right) / len(union) if union else 0.0

