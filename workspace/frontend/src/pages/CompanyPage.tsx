import { useEffect, useState } from "react";
import { MarkdownView } from "../components/MarkdownView";
import { getText } from "../services/dataService";
import type { WorkspaceData } from "../types/compass";

export function CompanyPage({ data }: { data: WorkspaceData }) {
  const tickers = Array.from(new Set((data.discovery.all_companies ?? data.discovery.candidates ?? []).map((item) => item.ticker))).sort();
  const [ticker, setTicker] = useState(tickers[0] ?? "AAPL");
  const [markdown, setMarkdown] = useState(data.markdown.companyAapl ?? "");

  useEffect(() => {
    getText(`reports/company_analysis/${ticker}.md`).then(setMarkdown);
  }, [ticker]);

  return (
    <section className="panel">
      <div className="filters">
        <label>
          Company
          <select value={ticker} onChange={(event) => setTicker(event.target.value)}>
            {tickers.map((item) => (
              <option key={item}>{item}</option>
            ))}
          </select>
        </label>
      </div>
      <MarkdownView markdown={markdown} />
    </section>
  );
}
