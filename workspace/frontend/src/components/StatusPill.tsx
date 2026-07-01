interface StatusPillProps {
  value: string;
}

export function StatusPill({ value }: StatusPillProps) {
  const normalized = value.toLowerCase();
  const tone = normalized.includes("approved") || normalized.includes("excellent") || normalized.includes("good")
    ? "good"
    : normalized.includes("pending") || normalized.includes("neutral") || normalized.includes("review")
      ? "watch"
      : normalized.includes("reject") || normalized.includes("poor")
        ? "risk"
        : "default";
  return <span className={`status ${tone}`}>{value}</span>;
}
