import { useMemo, useState } from "react";
import { DataTable } from "../components/DataTable";
import { StatusPill } from "../components/StatusPill";
import type { DiscoveryCandidate, WorkspaceData } from "../types/compass";

export function DiscoveryPage({ data }: { data: WorkspaceData }) {
  const [sector, setSector] = useState("All");
  const [confidence, setConfidence] = useState("All");
  const [minScore, setMinScore] = useState(0);
  const candidates = data.discovery.candidates ?? [];
  const sectors = ["All", ...Array.from(new Set(candidates.map((item) => item.sector)))];
  const confidences = ["All", ...Array.from(new Set(candidates.map((item) => item.confidence)))];
  const rows = useMemo(
    () =>
      candidates.filter(
        (item) =>
          (sector === "All" || item.sector === sector) &&
          (confidence === "All" || item.confidence === confidence) &&
          item.discovery_score >= minScore,
      ),
    [candidates, confidence, minScore, sector],
  );

  return (
    <section className="panel">
      <div className="filters">
        <label>
          Sector
          <select value={sector} onChange={(event) => setSector(event.target.value)}>
            {sectors.map((item) => (
              <option key={item}>{item}</option>
            ))}
          </select>
        </label>
        <label>
          Confidence
          <select value={confidence} onChange={(event) => setConfidence(event.target.value)}>
            {confidences.map((item) => (
              <option key={item}>{item}</option>
            ))}
          </select>
        </label>
        <label>
          Min score
          <input type="number" value={minScore} min={0} max={100} onChange={(event) => setMinScore(Number(event.target.value))} />
        </label>
      </div>
      <DataTable<DiscoveryCandidate>
        rows={rows}
        columns={[
          { label: "Company", render: (row) => <strong>{row.company}</strong> },
          { label: "Sector", render: (row) => row.sector },
          { label: "Discovery Score", render: (row) => row.discovery_score },
          { label: "Confidence", render: (row) => <StatusPill value={row.confidence} /> },
          { label: "Reason", render: (row) => row.discovery_reasons?.[0] ?? "N/A" },
        ]}
      />
    </section>
  );
}
