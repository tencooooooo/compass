export type Confidence = "High" | "Medium" | "Low" | string;

export type SignalStrength = "Strong" | "Moderate" | "Weak" | string;

export interface DiscoveryCandidate {
  ticker: string;
  company: string;
  sector: string;
  industry?: string;
  discovery_score: number;
  status: string;
  confidence: Confidence;
  signal_strength?: SignalStrength;
  signal_rate?: number | null;
  discovery_reasons: string[];
}

export interface DiscoveryData {
  generated_at?: string;
  market?: Record<string, unknown>;
  candidates?: DiscoveryCandidate[];
  all_companies?: DiscoveryCandidate[];
}

export interface ValidationRow {
  ticker: string;
  company: string;
  sector: string;
  period: string;
  discovery_score: number;
  validation_result: string;
  confidence: Confidence;
  signal_strength?: SignalStrength;
  return_percent?: number;
  period_complete?: boolean;
}

export interface ProposalIndexItem {
  proposal_id: string;
  title: string;
  target: string;
  status: "Pending" | "Approved" | "Rejected" | "Deferred";
  created: string;
  updated: string;
  reviewer: string;
}

export interface LearningMetrics {
  approved?: number;
  rejected?: number;
  deferred?: number;
  pending?: number;
  applied?: number;
  proposal_count?: number;
  adoption_rate?: number | null;
  knowledge_version?: string;
}

export interface MarketDashboard {
  market?: Record<string, unknown>;
  sectors?: Array<Record<string, unknown>>;
  top_events?: Array<Record<string, unknown>>;
  summary?: Record<string, unknown>;
}

export interface WorkspaceManifest {
  generatedAt?: string;
  project?: string;
  dataRoot?: string;
  counts?: {
    discovery?: number;
    validation?: number;
    proposals?: number;
    learningApplied?: number;
  };
}

export interface WorkspaceData {
  manifest: WorkspaceManifest;
  discovery: DiscoveryData;
  validation: ValidationRow[];
  proposals: ProposalIndexItem[];
  learningMetrics: LearningMetrics;
  market: MarketDashboard;
  notifications: unknown[];
  markdown: Record<string, string>;
  config: Record<string, string>;
}
