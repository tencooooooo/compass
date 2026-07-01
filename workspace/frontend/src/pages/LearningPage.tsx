import { StatCard } from "../components/StatCard";
import { MarkdownView } from "../components/MarkdownView";
import type { WorkspaceData } from "../types/compass";

export function LearningPage({ data }: { data: WorkspaceData }) {
  return (
    <div className="stack">
      <section className="summaryGrid">
        <StatCard label="Approved" value={data.learningMetrics.approved ?? 0} />
        <StatCard label="Applied" value={data.learningMetrics.applied ?? 0} />
        <StatCard label="Adoption rate" value={`${data.learningMetrics.adoption_rate ?? "N/A"}%`} />
        <StatCard label="Version" value={data.learningMetrics.knowledge_version ?? "v1"} />
      </section>
      <section className="panel">
        <MarkdownView markdown={data.markdown.learningSummary ?? ""} />
      </section>
    </div>
  );
}
