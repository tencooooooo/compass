import type { WorkspaceData } from "../types/compass";

export function SettingsPage({ data }: { data: WorkspaceData }) {
  return (
    <div className="twoCol">
      <section className="panel">
        <h2>settings.yaml</h2>
        <pre className="codeBlock">{data.config.settings || "No settings data synced."}</pre>
      </section>
      <section className="panel">
        <h2>notification.yaml</h2>
        <pre className="codeBlock">{data.config.notification || "No notification data synced."}</pre>
      </section>
    </div>
  );
}
