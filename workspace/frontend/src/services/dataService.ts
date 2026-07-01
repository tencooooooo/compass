import type {
  DiscoveryData,
  LearningMetrics,
  MarketDashboard,
  ProposalIndexItem,
  ValidationRow,
  WorkspaceData,
  WorkspaceManifest,
} from "../types/compass";

const ROOT = "/compass-data";

async function getJson<T>(path: string, fallback: T): Promise<T> {
  try {
    const response = await fetch(`${ROOT}/${path}`);
    if (!response.ok) return fallback;
    return (await response.json()) as T;
  } catch {
    return fallback;
  }
}

export async function getText(path: string, fallback = ""): Promise<string> {
  try {
    const response = await fetch(`${ROOT}/${path}`);
    if (!response.ok) return fallback;
    return await response.text();
  } catch {
    return fallback;
  }
}

export async function loadWorkspaceData(): Promise<WorkspaceData> {
  const [
    manifest,
    discovery,
    validation,
    proposals,
    learningMetrics,
    market,
    notificationHistory,
    marketSummary,
    validationSummary,
    learningSummary,
    companyAapl,
    comparisonMarket,
    settings,
    notificationSettings,
  ] = await Promise.all([
    getJson<WorkspaceManifest>("manifest.json", {}),
    getJson<DiscoveryData>("reports/discovery/discovery_candidates.json", {}),
    getJson<ValidationRow[]>("reports/validation/validation_history.json", []),
    getJson<ProposalIndexItem[]>("reports/proposals/proposal_index.json", []),
    getJson<LearningMetrics>("reports/learning/learning_metrics.json", {}),
    getJson<MarketDashboard>("reports/market/market_dashboard.json", {}),
    getJson<unknown[]>("storage/notifications/notification_history.json", []),
    getText("reports/market/market_summary.md"),
    getText("reports/validation/validation_summary.md"),
    getText("reports/learning/learning_summary.md"),
    getText("reports/company_analysis/AAPL.md"),
    getText("reports/comparative_analysis/market_overview.md"),
    getText("config/settings.yaml"),
    getText("config/notification.yaml"),
  ]);

  const latestProposalDate = [...proposals]
    .sort((a, b) => String(b.updated || b.created).localeCompare(String(a.updated || a.created)))
    .map((proposal) => String(proposal.created || proposal.updated).slice(0, 10))
    .find(Boolean);
  const proposalLatest = latestProposalDate ? await getText(`reports/proposals/proposal_${latestProposalDate}.md`) : "";

  return {
    manifest,
    discovery,
    validation,
    proposals,
    learningMetrics,
    market,
    notifications: notificationHistory,
    markdown: {
      marketSummary,
      validationSummary,
      learningSummary,
      proposalLatest,
      companyAapl,
      comparisonMarket,
    },
    config: {
      settings,
      notification: notificationSettings,
    },
  };
}
