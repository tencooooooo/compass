import { ArrowRight } from "lucide-react";
import { DataTable } from "../components/DataTable";
import { StatCard } from "../components/StatCard";
import { StatusPill } from "../components/StatusPill";
import type { PageKey } from "../App";
import type { DiscoveryCandidate, WorkspaceData } from "../types/compass";

interface HomePageProps {
  data: WorkspaceData;
  setPage: (page: PageKey) => void;
}

export function HomePage({ data, setPage }: HomePageProps) {
  const candidates = data.discovery.candidates ?? [];
  const top = [...candidates].sort((a, b) => b.discovery_score - a.discovery_score).slice(0, 3);
  const validations = data.validation.length;
  const proposalCount = data.proposals.length;
  const sectors = data.market.sectors ?? [];
  const latestNotifications = data.notifications.slice(-10).reverse();
  const syncedAt = data.manifest.generatedAt ? new Date(data.manifest.generatedAt).toLocaleString() : "No local sync";

  return (
    <div className="stack">
      <section className="summaryGrid">
        <StatCard label="Today's processing" value={data.manifest.generatedAt ? "Success" : "Unknown"} note={`Failures 0 / Synced ${syncedAt}`} />
        <StatCard label="Discovery" value={candidates.length} note="Candidates" />
        <StatCard label="Validation" value={validations} note="Rows" />
        <StatCard label="Proposals" value={proposalCount} note="Human review queue" />
      </section>

      <section className="panel">
        <div className="panelHeader">
          <h2>Top Discovery</h2>
          <button className="ghost" onClick={() => setPage("discovery")}>
            Open <ArrowRight size={16} />
          </button>
        </div>
        <DataTable<DiscoveryCandidate>
          rows={top}
          columns={[
            { label: "Company", render: (row) => <strong>{row.company}</strong> },
            { label: "Score", render: (row) => row.discovery_score },
            { label: "Confidence", render: (row) => <StatusPill value={row.confidence} /> },
            { label: "Reason", render: (row) => row.discovery_reasons?.[0] ?? "N/A" },
          ]}
        />
      </section>

      <section className="twoCol">
        <div className="panel">
          <h2>Market Summary</h2>
          <div className="sectorList">
            {sectors.map((sector, index) => (
              <div className="sectorRow" key={index}>
                <strong>{String(sector.sector ?? "Unknown")}</strong>
                <span>Score {String(sector.average_score ?? "N/A")}</span>
                <span>1M {String(sector.average_momentum_1m ?? "N/A")}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="panel">
          <h2>Notification</h2>
          <div className="eventList">
            {latestNotifications.length ? (
              latestNotifications.map((item, index) => <pre key={index}>{JSON.stringify(item, null, 2)}</pre>)
            ) : (
              <p className="muted">No notifications in the current artifact.</p>
            )}
          </div>
        </div>
      </section>

      <section className="panel">
        <h2>Workflow Status</h2>
        <div className="statusGrid">
          <StatusPill value="Artifact generated" />
          <StatusPill value="Read-only workspace" />
          <StatusPill value={`Last sync: ${syncedAt}`} />
          <StatusPill value={`Learning applied: ${data.learningMetrics.applied ?? 0}`} />
        </div>
      </section>
    </div>
  );
}
