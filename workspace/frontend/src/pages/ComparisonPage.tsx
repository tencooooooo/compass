import { useEffect, useState } from "react";
import { MarkdownView } from "../components/MarkdownView";
import { getText } from "../services/dataService";
import type { WorkspaceData } from "../types/compass";

const reports = [
  ["Market Overview", "reports/comparative_analysis/market_overview.md"],
  ["Mega Tech", "reports/comparative_analysis/mega_tech_comparison.md"],
  ["Technology Sector", "reports/comparative_analysis/sector_technology.md"],
  ["Semiconductor", "reports/comparative_analysis/semiconductor_comparison.md"],
];

export function ComparisonPage({ data }: { data: WorkspaceData }) {
  const [path, setPath] = useState(reports[0][1]);
  const [markdown, setMarkdown] = useState(data.markdown.comparisonMarket ?? "");

  useEffect(() => {
    getText(path).then(setMarkdown);
  }, [path]);

  return (
    <section className="panel">
      <div className="filters">
        <label>
          Report
          <select value={path} onChange={(event) => setPath(event.target.value)}>
            {reports.map(([label, value]) => (
              <option key={value} value={value}>
                {label}
              </option>
            ))}
          </select>
        </label>
      </div>
      <MarkdownView markdown={markdown} />
    </section>
  );
}
