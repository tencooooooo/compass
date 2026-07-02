from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]

from api.services.data_loader import REPO_ROOT
from lab.knowledge_graph.graph_builder import GraphBuilder
from lab.knowledge_graph.graph_similarity import GraphSimilarity
from lab.knowledge_graph.graph_storage import GraphStorage


class KnowledgeGraphEngine:
    """Builds Compass's independent knowledge network layer."""

    @classmethod
    def run(cls) -> dict[str, Any]:
        graph = GraphBuilder().build()
        similarity = GraphSimilarity().calculate(graph)
        graph["similarity"] = similarity
        storage_outputs = GraphStorage().save(graph)
        report_outputs = cls._write_reports(graph)
        return {
            "success": True,
            "nodes": len(graph.get("nodes", [])),
            "edges": len(graph.get("edges", [])),
            "outputs": {**storage_outputs, **report_outputs},
        }

    @classmethod
    def _write_reports(cls, graph: dict[str, Any]) -> dict[str, str]:
        output_dir = REPO_ROOT / "reports" / "graph"
        output_dir.mkdir(parents=True, exist_ok=True)
        files = {
            "summary": output_dir / "graph_summary.md",
            "company_network": output_dir / "company_network.md",
            "theme_network": output_dir / "theme_network.md",
            "dashboard": output_dir / "graph.json",
        }
        files["summary"].write_text(cls._summary(graph), encoding="utf-8")
        files["company_network"].write_text(cls._network(graph, "Company"), encoding="utf-8")
        files["theme_network"].write_text(cls._network(graph, "Theme"), encoding="utf-8")
        files["dashboard"].write_text(json.dumps(graph, ensure_ascii=False, indent=2), encoding="utf-8")
        return {name: str(path.relative_to(REPO_ROOT)) for name, path in files.items()}

    @classmethod
    def _summary(cls, graph: dict[str, Any]) -> str:
        metadata = graph.get("metadata", {})
        type_counts: dict[str, int] = {}
        relationship_counts: dict[str, int] = {}
        for node in graph.get("nodes", []):
            type_counts[node.get("type", "Unknown")] = type_counts.get(node.get("type", "Unknown"), 0) + 1
        for edge in graph.get("edges", []):
            relationship_counts[edge.get("relationship", "Unknown")] = relationship_counts.get(edge.get("relationship", "Unknown"), 0) + 1
        lines = [
            "# Knowledge Graph Summary",
            "",
            "Knowledge Graph is an independent Compass knowledge layer. It stores relationships between companies, themes, sectors, events, technologies, products, countries, and ETFs.",
            "",
            f"- Generated at: {metadata.get('generated_at')}",
            f"- Nodes: {metadata.get('node_count', 0)}",
            f"- Edges: {metadata.get('edge_count', 0)}",
            "",
            "## Node Types",
            "",
        ]
        for node_type, count in sorted(type_counts.items()):
            lines.append(f"- {node_type}: {count}")
        lines.extend(["", "## Relationships", ""])
        for relationship, count in sorted(relationship_counts.items()):
            lines.append(f"- {relationship}: {count}")
        return "\n".join(lines) + "\n"

    @classmethod
    def _network(cls, graph: dict[str, Any], node_type: str) -> str:
        nodes = {node["id"]: node for node in graph.get("nodes", []) if node.get("type") == node_type}
        lines = [f"# {node_type} Network", ""]
        for node_id, node in sorted(nodes.items()):
            lines.extend([f"## {node.get('label', node_id)}", ""])
            related = [
                edge for edge in graph.get("edges", [])
                if edge.get("source") == node_id or edge.get("target") == node_id
            ][:20]
            if not related:
                lines.append("- No relationships available.")
            for edge in related:
                other = edge["target"] if edge["source"] == node_id else edge["source"]
                lines.append(f"- {edge['relationship']}: {other} ({edge.get('evidence', 'No evidence')})")
            lines.append("")
        return "\n".join(lines)


if __name__ == "__main__":
    print(KnowledgeGraphEngine.run())

