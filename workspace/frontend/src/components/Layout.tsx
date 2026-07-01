import { BarChart3, Bell, Building2, CheckCircle2, GitPullRequestDraft, Home, Layers3, LineChart, Settings, Sparkles } from "lucide-react";
import type { ReactNode } from "react";
import type { PageKey } from "../App";

interface LayoutProps {
  page: PageKey;
  setPage: (page: PageKey) => void;
  children: ReactNode;
}

const nav: Array<{ key: PageKey; label: string; icon: ReactNode }> = [
  { key: "home", label: "Home", icon: <Home size={18} /> },
  { key: "discovery", label: "Discovery", icon: <Sparkles size={18} /> },
  { key: "company", label: "Company", icon: <Building2 size={18} /> },
  { key: "comparison", label: "Comparison", icon: <Layers3 size={18} /> },
  { key: "validation", label: "Validation", icon: <CheckCircle2 size={18} /> },
  { key: "proposal", label: "Proposal", icon: <GitPullRequestDraft size={18} /> },
  { key: "learning", label: "Learning", icon: <LineChart size={18} /> },
  { key: "settings", label: "Settings", icon: <Settings size={18} /> },
];

export function Layout({ page, setPage, children }: LayoutProps) {
  return (
    <div className="shell">
      <aside className="sidebar">
        <div className="brand">
          <BarChart3 size={22} />
          <div>
            <strong>Compass</strong>
            <span>Workspace</span>
          </div>
        </div>
        <nav>
          {nav.map((item) => (
            <button className={page === item.key ? "active" : ""} key={item.key} onClick={() => setPage(item.key)}>
              {item.icon}
              <span>{item.label}</span>
            </button>
          ))}
        </nav>
      </aside>
      <main>
        <header className="topbar">
          <div>
            <p>Research Workspace</p>
            <h1>{nav.find((item) => item.key === page)?.label}</h1>
          </div>
          <div className="topStatus">
            <Bell size={18} />
            <span>Read-only</span>
          </div>
        </header>
        {children}
      </main>
    </div>
  );
}
