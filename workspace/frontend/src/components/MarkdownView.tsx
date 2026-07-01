import { marked } from "marked";

interface MarkdownViewProps {
  markdown: string;
}

export function MarkdownView({ markdown }: MarkdownViewProps) {
  const html = marked.parse(markdown || "No report available.") as string;
  return <article className="markdown" dangerouslySetInnerHTML={{ __html: html }} />;
}
