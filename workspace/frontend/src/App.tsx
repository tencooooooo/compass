import { useEffect, useState } from "react";
import { Layout } from "./components/Layout";
import { loadWorkspaceData } from "./services/dataService";
import type { WorkspaceData } from "./types/compass";
import { HomePage } from "./pages/HomePage";
import { DiscoveryPage } from "./pages/DiscoveryPage";
import { CompanyPage } from "./pages/CompanyPage";
import { ComparisonPage } from "./pages/ComparisonPage";
import { ValidationPage } from "./pages/ValidationPage";
import { ProposalPage } from "./pages/ProposalPage";
import { LearningPage } from "./pages/LearningPage";
import { SettingsPage } from "./pages/SettingsPage";

export type PageKey = "home" | "discovery" | "company" | "comparison" | "validation" | "proposal" | "learning" | "settings";

const emptyData: WorkspaceData = {
  manifest: {},
  discovery: {},
  validation: [],
  proposals: [],
  learningMetrics: {},
  market: {},
  notifications: [],
  markdown: {},
  config: {},
};

export default function App() {
  const [page, setPage] = useState<PageKey>("home");
  const [data, setData] = useState<WorkspaceData>(emptyData);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadWorkspaceData()
      .then(setData)
      .finally(() => setLoading(false));
  }, []);

  const content = (() => {
    if (loading) return <section className="panel">Loading Compass data...</section>;
    if (page === "home") return <HomePage data={data} setPage={setPage} />;
    if (page === "discovery") return <DiscoveryPage data={data} />;
    if (page === "company") return <CompanyPage data={data} />;
    if (page === "comparison") return <ComparisonPage data={data} />;
    if (page === "validation") return <ValidationPage data={data} />;
    if (page === "proposal") return <ProposalPage data={data} />;
    if (page === "learning") return <LearningPage data={data} />;
    return <SettingsPage data={data} />;
  })();

  return (
    <Layout page={page} setPage={setPage}>
      {content}
    </Layout>
  );
}
