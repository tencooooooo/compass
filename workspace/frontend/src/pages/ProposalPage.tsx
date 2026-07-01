import { DataTable } from "../components/DataTable";
import { MarkdownView } from "../components/MarkdownView";
import { StatusPill } from "../components/StatusPill";
import type { ProposalIndexItem, WorkspaceData } from "../types/compass";

export function ProposalPage({ data }: { data: WorkspaceData }) {
  return (
    <div className="stack">
      <section className="panel">
        <DataTable<ProposalIndexItem>
          rows={data.proposals}
          columns={[
            { label: "Proposal ID", render: (row) => row.proposal_id },
            { label: "Target", render: (row) => row.target },
            { label: "Status", render: (row) => <StatusPill value={row.status} /> },
            { label: "Reviewer", render: (row) => row.reviewer || "N/A" },
            { label: "Updated", render: (row) => row.updated },
          ]}
        />
      </section>
      <section className="panel">
        <MarkdownView markdown={data.markdown.proposalLatest ?? ""} />
      </section>
    </div>
  );
}
