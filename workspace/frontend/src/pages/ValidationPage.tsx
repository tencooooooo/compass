import { DataTable } from "../components/DataTable";
import { MarkdownView } from "../components/MarkdownView";
import { StatusPill } from "../components/StatusPill";
import type { ValidationRow, WorkspaceData } from "../types/compass";

export function ValidationPage({ data }: { data: WorkspaceData }) {
  return (
    <div className="stack">
      <section className="panel">
        <MarkdownView markdown={data.markdown.validationSummary ?? ""} />
      </section>
      <section className="panel">
        <h2>History</h2>
        <DataTable<ValidationRow>
          rows={data.validation}
          columns={[
            { label: "Ticker", render: (row) => row.ticker },
            { label: "Period", render: (row) => row.period },
            { label: "Score", render: (row) => row.discovery_score },
            { label: "Result", render: (row) => <StatusPill value={row.validation_result} /> },
            { label: "Confidence", render: (row) => row.confidence },
          ]}
        />
      </section>
    </div>
  );
}
