import { useMemo } from "react";
import DOMPurify from "dompurify";
import { marked } from "marked";

interface MarkdownViewProps {
  markdown: string;
}

// レポート本文には外部由来のニュース見出しがそのまま入るため、HTML化した後に必ずサニタイズします。
// marked はv5以降サニタイズ機能を持たないので、<script>・onerror等の属性・javascript: リンクは
// DOMPurify 側で除去します。比較レポートが意図的に出力する <br> は許可されたまま残ります。
export function MarkdownView({ markdown }: MarkdownViewProps) {
  const html = useMemo(
    () => DOMPurify.sanitize(marked.parse(markdown || "No report available.") as string),
    [markdown],
  );
  return <article className="markdown" dangerouslySetInnerHTML={{ __html: html }} />;
}
