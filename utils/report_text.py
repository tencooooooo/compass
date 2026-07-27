from __future__ import annotations

import re
from typing import Any


# Compassは投資判断を出さない方針のため、外部由来テキスト(ニュース見出し・要約)に含まれる
# 売買判断表現をレポート本文へそのまま持ち込まないよう中立化します。
# MANIFEST.md の「Prohibited outputs: Definitive buy or sell calls」に対応します。
INVESTMENT_LANGUAGE_REPLACEMENTS = [
    (r"\bBuy(?:ing)?\b", "投資判断表現"),
    (r"\bSell(?:ing)?\b", "投資判断表現"),
    (r"\bHold(?:ing)?\b", "投資判断表現"),
    (r"買い", "投資判断表現"),
    (r"売り", "投資判断表現"),
    (r"目標株価", "価格水準"),
]


def sanitize_report_text(value: Any) -> str:
    """レポート本文では投資判断に見える表現を中立化します。

    注意: これはHTMLエスケープではありません。生成されたMarkdownをHTMLとして描画する側
    (workspace/frontend の MarkdownView)が DOMPurify でサニタイズする責務を持ちます。
    """
    text = "" if value is None else str(value)
    for pattern, replacement in INVESTMENT_LANGUAGE_REPLACEMENTS:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text
