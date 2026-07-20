from __future__ import annotations

from typing import Any

import pandas as pd

from utils.news_dedup import dedupe_news_items
from utils.news_sentiment import sentiment_counts
from utils.price_data import trading_day_momentum
from utils.values import safe_float


GROWTH_THRESHOLDS = {
    "excellent": 30.0,
    "good": 15.0,
    "positive": 0.0,
}

VALUATION_RULES = [
    ("trailing_pe", "PER", 5, [(0, 25, 5), (25, 40, 3), (40, 70, 1)]),
    ("forward_pe", "Forward PER", 5, [(0, 25, 5), (25, 40, 3), (40, 70, 1)]),
    ("peg_ratio", "PEG", 5, [(0, 1, 5), (1, 2, 3), (2, 4, 1)]),
    ("price_to_book", "PBR", 5, [(0, 8, 5), (8, 20, 3), (20, 50, 1)]),
]


def clamp(value: float, minimum: float = 0, maximum: float = 20) -> float:
    return max(minimum, min(maximum, value))


def rounded_score(value: float) -> int:
    return int(round(clamp(value)))


def is_present(value: Any) -> bool:
    return safe_float(value) is not None if isinstance(value, (int, float, str)) else value not in (None, "", [], {})


def score_positive_number(value: Any, points: float, label: str, reasons: list[str], missing: list[str]) -> float:
    number = safe_float(value)
    if number is None:
        missing.append(label)
        reasons.append(f"{label} が取得できないため、この項目は加点していません。")
        return 0
    if number > 0:
        reasons.append(f"{label} がプラスで確認できるため加点しています。")
        return points
    reasons.append(f"{label} がプラスではないため、加点を抑えています。")
    return 0


def momentum_for_days(prices: pd.DataFrame, days: int) -> float | None:
    return trading_day_momentum(prices, days)


def score_return(change_percent: float | None, label: str, reasons: list[str], missing: list[str]) -> float:
    if change_percent is None:
        missing.append(label)
        reasons.append(f"{label} の騰落率が計算できないため加点していません。")
        return 0
    if change_percent >= 15:
        reasons.append(f"{label} が {change_percent:.2f}% と強い上昇を示しています。")
        return 3
    if change_percent >= 0:
        reasons.append(f"{label} が {change_percent:.2f}% とプラス圏です。")
        return 2
    if change_percent >= -10:
        reasons.append(f"{label} は {change_percent:.2f}% と小幅なマイナスです。")
        return 1
    reasons.append(f"{label} は {change_percent:.2f}% と大きめの下落です。")
    return 0


def classify_news(news_items: list[dict[str, Any]]) -> tuple[int, int]:
    counts = sentiment_counts(news_items)
    return counts["positive"], counts["negative"]


def yoy_growth(latest: Any, prior: Any) -> float | None:
    latest_value = safe_float(latest)
    prior_value = safe_float(prior)
    if latest_value is None or prior_value in (None, 0):
        return None
    return round((latest_value - prior_value) / abs(prior_value) * 100, 2)


def score_growth_rate(value: float | None, label: str, points: float, reasons: list[str], missing: list[str]) -> float:
    if value is None:
        missing.append(label)
        reasons.append(f"{label} が計算できないため、成長率項目は加点していません。")
        return 0
    if value >= GROWTH_THRESHOLDS["excellent"]:
        reasons.append(f"{label} は {value:.2f}% で、+{GROWTH_THRESHOLDS['excellent']:.0f}%以上の高成長です。")
        return points
    if value >= GROWTH_THRESHOLDS["good"]:
        reasons.append(f"{label} は {value:.2f}% で、+{GROWTH_THRESHOLDS['good']:.0f}%以上の成長です。")
        return points * 0.65
    if value >= GROWTH_THRESHOLDS["positive"]:
        reasons.append(f"{label} は {value:.2f}% で、プラス成長を維持しています。")
        return points * 0.35
    reasons.append(f"{label} は {value:.2f}% で、前年同期比ではマイナスです。")
    return 0


def prior_year_quarter_label(label: Any) -> str | None:
    if not isinstance(label, str) or "-Q" not in label:
        return None
    year_text, quarter = label.split("-Q", 1)
    try:
        return f"{int(year_text) - 1}-Q{quarter}"
    except ValueError:
        return None


# 単一四半期のYoYはノイズが大きいため、前年同期が揃う直近最大4四半期を平滑化に使います。
GROWTH_SMOOTHING_QUARTERS = 4


def yoy_growth_series(financials: dict[str, Any], key: str, max_quarters: int = GROWTH_SMOOTHING_QUARTERS) -> list[dict[str, Any]]:
    """直近四半期から順に、前年同期が存在する四半期のYoY成長率一覧を返します。"""
    rows = financials.get("quarterly_financials")
    if not isinstance(rows, list) or not rows:
        return []
    by_quarter = {row.get("fiscal_quarter"): row for row in rows if isinstance(row, dict)}
    series: list[dict[str, Any]] = []
    for row in rows[:max_quarters]:
        if not isinstance(row, dict):
            continue
        label = row.get("fiscal_quarter")
        prior = by_quarter.get(prior_year_quarter_label(label))
        if prior is None:
            continue
        growth = yoy_growth(row.get(key), prior.get(key))
        if growth is not None:
            series.append({"fiscal_quarter": label, "yoy_growth": growth})
    return series


def smoothed_growth(series: list[dict[str, Any]]) -> float | None:
    if not series:
        return None
    return round(sum(item["yoy_growth"] for item in series) / len(series), 2)


def append_growth_trend_reason(series: list[dict[str, Any]], label: str, reasons: list[str]) -> None:
    if len(series) < 2:
        return
    delta = series[0]["yoy_growth"] - series[1]["yoy_growth"]
    if delta >= 5:
        reasons.append(f"{label} は直近四半期が前四半期より {delta:+.2f}pt 高く、成長の加速がみられます。")
    elif delta <= -5:
        reasons.append(f"{label} は直近四半期が前四半期より {delta:+.2f}pt 低く、成長の減速に注意が必要です。")


def calculate_growth_fallback(financials: dict[str, Any], extra_missing: list[str] | None = None) -> dict[str, Any]:
    reasons: list[str] = []
    missing: list[str] = []
    score = 0.0

    revenue = safe_float(financials.get("total_revenue"))
    if revenue is None:
        missing.append("total_revenue")
        reasons.append("売上データが取得できないため、売上項目は加点していません。")
    elif revenue >= 100_000_000_000:
        score += 5
        reasons.append("売上規模が大きく、事業規模の強さが確認できます。")
    elif revenue > 0:
        score += 3
        reasons.append("売上がプラスで確認できます。")
    else:
        reasons.append("売上がプラスではないため、売上項目の加点を抑えています。")

    score += score_positive_number(financials.get("eps"), 5, "EPS", reasons, missing)
    score += score_positive_number(financials.get("net_income"), 4, "純利益", reasons, missing)
    score += score_positive_number(financials.get("operating_income"), 2, "営業利益", reasons, missing)

    rnd = safe_float(financials.get("research_and_development"))
    if rnd is None:
        missing.append("research_and_development")
        reasons.append("研究開発費が取得できないため、R&D項目は加点していません。")
    elif rnd > 0:
        score += 4
        reasons.append("研究開発費が確認でき、将来成長への投資が続いています。")
    else:
        reasons.append("研究開発費が確認できないため、R&D項目の加点を抑えています。")

    for label in extra_missing or []:
        if label not in missing:
            missing.append(label)
    reasons.append("四半期時系列が不足しているため、Growthは最新値中心の従来ロジックへフォールバックしています。")
    return {
        "score": rounded_score(score),
        "max_score": 20,
        "reasons": reasons,
        "evidence": ["Financials", "Knowledge"],
        "missing_data": missing,
        "metrics": {
            "total_revenue": financials.get("total_revenue"),
            "eps": financials.get("eps"),
            "net_income": financials.get("net_income"),
            "operating_income": financials.get("operating_income"),
            "research_and_development": financials.get("research_and_development"),
            "revenue_yoy_growth": None,
            "eps_yoy_growth": None,
        },
    }


def calculate_growth(financials: dict[str, Any]) -> dict[str, Any]:
    reasons: list[str] = []
    missing: list[str] = []
    score = 0.0

    revenue_series = yoy_growth_series(financials, "total_revenue")
    eps_series = yoy_growth_series(financials, "eps")
    revenue_growth = revenue_series[0]["yoy_growth"] if revenue_series else None
    eps_growth = eps_series[0]["yoy_growth"] if eps_series else None
    revenue_growth_avg = smoothed_growth(revenue_series)
    eps_growth_avg = smoothed_growth(eps_series)
    if revenue_growth_avg is None and eps_growth_avg is None:
        return calculate_growth_fallback(financials, ["revenue_growth"])

    revenue_label = f"revenue_growth(直近{len(revenue_series)}四半期平均)" if revenue_series else "revenue_growth"
    eps_label = f"eps_growth(直近{len(eps_series)}四半期平均)" if eps_series else "eps_growth"
    score += score_growth_rate(revenue_growth_avg, revenue_label, 5, reasons, missing)
    score += score_growth_rate(eps_growth_avg, eps_label, 5, reasons, missing)
    append_growth_trend_reason(revenue_series, "revenue_growth", reasons)
    append_growth_trend_reason(eps_series, "eps_growth", reasons)
    score += score_positive_number(financials.get("net_income"), 3, "純利益", reasons, missing)
    score += score_positive_number(financials.get("operating_income"), 2, "営業利益", reasons, missing)

    rnd = safe_float(financials.get("research_and_development"))
    if rnd is None:
        missing.append("research_and_development")
        reasons.append("研究開発費が取得できないため、R&D項目は加点していません。")
    elif rnd > 0:
        score += 4
        reasons.append("研究開発費が確認でき、将来成長への投資が続いています。")
    else:
        reasons.append("研究開発費が確認できないため、R&D項目の加点を抑えています。")

    revenue = safe_float(financials.get("total_revenue"))
    if revenue is None:
        missing.append("total_revenue")
        reasons.append("売上規模データが取得できないため、規模項目は加点していません。")
    elif revenue >= 100_000_000_000:
        score += 3
        reasons.append("売上規模が大きく、事業規模の強さが確認できます。")
    elif revenue > 0:
        score += 1.5
        reasons.append("売上がプラスで確認できます。")

    return {
        "score": rounded_score(score),
        "max_score": 20,
        "reasons": reasons,
        "evidence": ["Financials", "Knowledge"],
        "missing_data": missing,
        "metrics": {
            "total_revenue": financials.get("total_revenue"),
            "eps": financials.get("eps"),
            "net_income": financials.get("net_income"),
            "operating_income": financials.get("operating_income"),
            "research_and_development": financials.get("research_and_development"),
            "revenue_yoy_growth": revenue_growth,
            "eps_yoy_growth": eps_growth,
            "revenue_yoy_growth_avg": revenue_growth_avg,
            "eps_yoy_growth_avg": eps_growth_avg,
            "revenue_growth_quarters": [item["fiscal_quarter"] for item in revenue_series],
            "eps_growth_quarters": [item["fiscal_quarter"] for item in eps_series],
        },
    }


def calculate_financial_health(financials: dict[str, Any]) -> dict[str, Any]:
    reasons: list[str] = []
    missing: list[str] = []
    score = 0.0

    score += score_positive_number(financials.get("cash"), 4, "現金", reasons, missing)

    liabilities = safe_float(financials.get("total_liabilities"))
    equity = safe_float(financials.get("shareholders_equity"))
    debt = safe_float(financials.get("long_term_debt"))

    if equity is None:
        missing.append("shareholders_equity")
        reasons.append("自己資本が取得できないため、自己資本項目は加点していません。")
    elif equity > 0:
        score += 5
        reasons.append("自己資本がプラスで、財務基盤を確認できます。")
    else:
        reasons.append("自己資本がプラスではないため、財務健全性の加点を抑えています。")

    if liabilities is None:
        missing.append("total_liabilities")
        reasons.append("総負債が取得できないため、負債項目は加点していません。")
    elif equity and equity > 0:
        debt_to_equity = liabilities / equity
        if debt_to_equity <= 1:
            score += 5
            reasons.append(f"総負債/自己資本が {debt_to_equity:.2f} 倍で、負債負担は相対的に抑えられています。")
        elif debt_to_equity <= 2:
            score += 3
            reasons.append(f"総負債/自己資本が {debt_to_equity:.2f} 倍で、負債負担は中程度です。")
        else:
            score += 1
            reasons.append(f"総負債/自己資本が {debt_to_equity:.2f} 倍で、負債負担の確認が必要です。")
    elif liabilities >= 0:
        score += 2
        reasons.append("総負債は取得できていますが、自己資本との比較が不十分です。")

    if debt is None:
        missing.append("long_term_debt")
        reasons.append("長期債務が取得できないため、債務構成の確認が必要です。")
    elif debt == 0:
        score += 2
        reasons.append("長期債務が0として取得されており、債務負担は限定的です。")
    elif liabilities and liabilities > 0 and debt / liabilities <= 0.5:
        score += 2
        reasons.append("長期債務が総負債に対して過度に大きくないため加点しています。")
    else:
        score += 1
        reasons.append("長期債務が確認できるため、返済負担の継続確認が必要です。")

    current_ratio = safe_float(financials.get("current_ratio"))
    if current_ratio is None:
        missing.append("current_ratio")
        reasons.append("Current Ratio が取得できないため、短期支払余力は評価を控えています。")
    elif current_ratio >= 1.5:
        score += 4
        reasons.append(f"Current Ratio が {current_ratio:.2f} で、短期支払余力が確認できます。")
    elif current_ratio >= 1:
        score += 2
        reasons.append(f"Current Ratio が {current_ratio:.2f} で、最低限の短期支払余力があります。")
    else:
        reasons.append(f"Current Ratio が {current_ratio:.2f} で、短期支払余力は追加確認が必要です。")

    return {
        "score": rounded_score(score),
        "max_score": 20,
        "reasons": reasons,
        "evidence": ["Financials", "Knowledge"],
        "missing_data": missing,
        "metrics": {
            "cash": financials.get("cash"),
            "total_liabilities": financials.get("total_liabilities"),
            "shareholders_equity": financials.get("shareholders_equity"),
            "long_term_debt": financials.get("long_term_debt"),
            "current_ratio": financials.get("current_ratio"),
        },
    }


def fixed_valuation_points(value: float, bands: list[tuple[int, int, int]]) -> int:
    for lower, upper, band_points in bands:
        if lower < value <= upper:
            return band_points
    return 0


def percentile_rank_lower_is_better(value: float, values: list[float]) -> float | None:
    clean_values = sorted(item for item in values if item > 0)
    if len(clean_values) < 2:
        return None
    lower_count = sum(1 for item in clean_values if item < value)
    equal_count = sum(1 for item in clean_values if item == value)
    percentile = (lower_count + (equal_count - 1) / 2) / (len(clean_values) - 1) * 100
    return round(max(0, min(100, percentile)), 2)


def calculate_valuation(company: dict[str, Any], sector_companies: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    reasons: list[str] = []
    missing: list[str] = []
    score = 0.0

    sector_peers = sector_companies or []
    use_sector_relative = len(sector_peers) >= 5
    percentile_metrics: dict[str, Any] = {}

    for key, label, points, bands in VALUATION_RULES:
        value = safe_float(company.get(key))
        if value is None:
            missing.append(key)
            reasons.append(f"{label} が取得できないため加点していません。")
            continue
        if value <= 0:
            reasons.append(f"{label} は {value:.2f} で、指標がマイナスのため加点対象外です。")
            percentile_metrics[f"{key}_percentile"] = None
            percentile_metrics[f"{key}_peer_count"] = 0
            continue

        if use_sector_relative:
            peer_values = [number for peer in sector_peers if (number := safe_float(peer.get(key))) is not None and number > 0]
            percentile = percentile_rank_lower_is_better(value, peer_values)
            if percentile is None or len(peer_values) < 5:
                awarded = fixed_valuation_points(value, bands)
                reasons.append(f"{label} はセクター内有効データが {len(peer_values)} 件のため、固定閾値へフォールバックしています。")
            elif percentile <= 25:
                awarded = points
                reasons.append(f"{label} はセクター内 {percentile:.2f} パーセンタイル / 母数 {len(peer_values)} で、相対的に割安寄りです。")
            elif percentile <= 75:
                awarded = 3
                reasons.append(f"{label} はセクター内 {percentile:.2f} パーセンタイル / 母数 {len(peer_values)} で、中位レンジです。")
            else:
                awarded = 0
                reasons.append(f"{label} はセクター内 {percentile:.2f} パーセンタイル / 母数 {len(peer_values)} で、相対的な加点は抑えています。")
            percentile_metrics[f"{key}_percentile"] = percentile
            percentile_metrics[f"{key}_peer_count"] = len(peer_values)
        else:
            awarded = fixed_valuation_points(value, bands)
            reasons.append(f"セクター比較対象が {len(sector_peers)} 社のため、{label} は固定閾値で評価しています。")

        score += min(points, awarded)
        if not use_sector_relative or percentile_metrics.get(f"{key}_percentile") is None:
            if awarded >= 4:
                reasons.append(f"{label} は {value:.2f} で、評価ルール上は過度な割高さが抑えられています。")
            elif awarded > 0:
                reasons.append(f"{label} は {value:.2f} で、バリュエーション面は中立から注意寄りです。")
            else:
                reasons.append(f"{label} は {value:.2f} で、バリュエーション面の加点は抑えています。")

    reasons.append("バリュエーションは割安判断ではなく、追加調査のための相対評価です。")
    return {
        "score": rounded_score(score),
        "max_score": 20,
        "reasons": reasons,
        "evidence": ["Company", "Knowledge"],
        "missing_data": missing,
        "metrics": {
            "trailing_pe": company.get("trailing_pe"),
            "forward_pe": company.get("forward_pe"),
            "peg_ratio": company.get("peg_ratio"),
            "price_to_book": company.get("price_to_book"),
            "sector_peer_count": len(sector_peers),
            **percentile_metrics,
        },
    }


def score_excess_return(excess: float, benchmark_name: str, label: str, reasons: list[str]) -> float:
    if excess >= 10:
        reasons.append(f"{label} の対{benchmark_name}超過リターンが {excess:+.2f}pt と、市場を大きく上回っています。")
        return 3
    if excess >= 0:
        reasons.append(f"{label} の対{benchmark_name}超過リターンは {excess:+.2f}pt で、市場並み以上です。")
        return 2
    if excess >= -10:
        reasons.append(f"{label} の対{benchmark_name}超過リターンは {excess:+.2f}pt と、市場を小幅に下回っています。")
        return 1
    reasons.append(f"{label} の対{benchmark_name}超過リターンは {excess:+.2f}pt と、市場を大きく下回っています。")
    return 0


def calculate_momentum(
    prices: pd.DataFrame,
    benchmark_prices: pd.DataFrame | None = None,
    benchmark_name: str | None = None,
) -> dict[str, Any]:
    reasons: list[str] = []
    missing: list[str] = []
    score = 0.0

    if prices.empty:
        return {
            "score": 0,
            "max_score": 20,
            "reasons": ["価格CSVが取得できないため、Momentumは評価していません。"],
            "evidence": ["Prices", "Knowledge"],
            "missing_data": ["prices"],
            "metrics": {},
        }

    benchmark = benchmark_prices if benchmark_prices is not None else pd.DataFrame()
    use_benchmark = benchmark_name is not None and not benchmark.empty

    prices = prices.sort_values("date").reset_index(drop=True)
    returns = {
        "1M": momentum_for_days(prices, 30),
        "3M": momentum_for_days(prices, 90),
        "6M": momentum_for_days(prices, 180),
        "1Y": momentum_for_days(prices, 365),
    }
    benchmark_returns = {
        label: momentum_for_days(benchmark, days) if use_benchmark else None
        for label, days in (("1M", 30), ("3M", 90), ("6M", 180), ("1Y", 365))
    }
    excess_returns: dict[str, float | None] = {}
    for label, value in returns.items():
        benchmark_return = benchmark_returns[label]
        if value is not None and benchmark_return is not None:
            excess = value - benchmark_return
            excess_returns[label] = round(excess, 2)
            score += score_excess_return(excess, str(benchmark_name), label, reasons)
        else:
            excess_returns[label] = None
            score += score_return(value, label, reasons, missing)

    if not use_benchmark:
        missing.append("benchmark_prices")
        reasons.append("ベンチマーク価格が取得できないため、Momentumは絶対リターンで評価しています。")

    latest_volume = safe_float(prices.iloc[-1].get("volume"))
    average_volume = safe_float(prices.tail(30)["volume"].mean())
    if latest_volume is None or average_volume in (None, 0):
        missing.append("volume")
        reasons.append("出来高データが不足しているため、Volume項目は加点していません。")
    else:
        volume_ratio = latest_volume / average_volume
        if volume_ratio >= 1.2:
            score += 4
            reasons.append(f"直近出来高が30日平均の {volume_ratio:.2f} 倍で、市場関心の高まりが確認できます。")
        elif volume_ratio >= 0.8:
            score += 3
            reasons.append(f"直近出来高が30日平均の {volume_ratio:.2f} 倍で、通常水準の流動性があります。")
        else:
            score += 1
            reasons.append(f"直近出来高が30日平均の {volume_ratio:.2f} 倍で、市場関心はやや弱めです。")

    return {
        "score": rounded_score(score),
        "max_score": 20,
        "reasons": reasons,
        "evidence": ["Prices", "Knowledge"],
        "missing_data": missing,
        "metrics": {
            **returns,
            "benchmark": benchmark_name if use_benchmark else None,
            "benchmark_returns": {
                label: round(value, 2) if value is not None else None
                for label, value in benchmark_returns.items()
            },
            "excess_returns": excess_returns,
            "latest_volume": latest_volume,
            "average_volume_30d": average_volume,
        },
    }


def calculate_news(news_items: list[dict[str, Any]], events: list[dict[str, Any]]) -> dict[str, Any]:
    # 保存済みデータに再配信の重複が残っている場合に備え、評価前にも重複排除します。
    news_items = dedupe_news_items(news_items)
    reasons: list[str] = []
    missing: list[str] = []
    score = 0.0

    positive = negative = 0
    sentiment_net_ratio: float | None = None
    if not news_items:
        missing.append("news")
        reasons.append("ニュースが取得できないため、News項目は評価を控えています。")
    else:
        positive, negative = classify_news(news_items)
        coverage_points = min(6, len(news_items) / 20 * 6)
        score += coverage_points
        reasons.append(f"ニュース件数は {len(news_items)} 件で、情報量に応じて {coverage_points:.1f} 点を加点しています。")

        classified = positive + negative
        if classified == 0:
            sentiment_score = 4.0
            reasons.append("見出し・要約から好悪材料を分類できなかったため、センチメントは中立の4.0点としています。")
        else:
            # 生の件数差は報道量の多い銘柄ほど振れるため、分類済み件数に対する純比率で正規化します。
            sentiment_net_ratio = round((positive - negative) / classified, 2)
            sentiment_score = clamp(4 + 4 * sentiment_net_ratio, 0, 8)
            reasons.append(
                f"ニュース見出し・要約の簡易分類では、好材料 {positive} 件、悪材料 {negative} 件"
                f"(純比率 {sentiment_net_ratio:+.2f})で、センチメントは {sentiment_score:.1f} 点です。"
            )
        score += sentiment_score

    event_changes = [safe_float(event.get("price_change_percent")) for event in events]
    event_changes = [value for value in event_changes if value is not None]
    if not events:
        missing.append("events")
        reasons.append("イベントDBが取得できないため、イベント項目は加点していません。")
    elif not event_changes:
        missing.append("event_price_reaction")
        score += 2
        reasons.append("イベントDBはありますが、株価反応が未取得のため、イベント評価は限定的です。")
    else:
        average_reaction = sum(event_changes) / len(event_changes)
        if average_reaction > 1:
            score += 6
            reasons.append(f"イベント後の平均株価反応が {average_reaction:.2f}% とプラスです。")
        elif average_reaction >= -1:
            score += 4
            reasons.append(f"イベント後の平均株価反応が {average_reaction:.2f}% と中立圏です。")
        else:
            score += 1
            reasons.append(f"イベント後の平均株価反応が {average_reaction:.2f}% と弱く、注意が必要です。")

    return {
        "score": rounded_score(score),
        "max_score": 20,
        "reasons": reasons,
        "evidence": ["News", "Events", "Knowledge"],
        "missing_data": missing,
        "metrics": {
            "news_count": len(news_items),
            "positive_count": positive,
            "negative_count": negative,
            "sentiment_net_ratio": sentiment_net_ratio,
            "event_count": len(events),
            "events_with_price_reaction": len(event_changes),
        },
    }


# Confidence(データ充足度)とSignal Strength(シグナル強度)を分離して評価します。
# 従来はスコアが0点の領域を「データ無し」とみなしていたため、弱いシグナルがConfidenceを下げていました。
SIGNAL_STRENGTH_THRESHOLDS = {"strong": 65.0, "moderate": 40.0}

GROWTH_DATA_KEYS = ("total_revenue", "eps", "net_income", "operating_income", "research_and_development")
FINANCIAL_HEALTH_DATA_KEYS = ("cash", "total_liabilities", "shareholders_equity", "long_term_debt", "current_ratio")
VALUATION_DATA_KEYS = ("trailing_pe", "forward_pe", "peg_ratio", "price_to_book")


def signal_strength_level(signal_rate: float | None) -> str:
    if signal_rate is None:
        return "Weak"
    if signal_rate >= SIGNAL_STRENGTH_THRESHOLDS["strong"]:
        return "Strong"
    if signal_rate >= SIGNAL_STRENGTH_THRESHOLDS["moderate"]:
        return "Moderate"
    return "Weak"


def has_metric_data(part: dict[str, Any], keys: tuple[str, ...]) -> bool:
    metrics = part.get("metrics", {})
    return any(safe_float(metrics.get(key)) is not None for key in keys)


def data_availability(parts: dict[str, dict[str, Any]], prices: pd.DataFrame, news_items: list[dict[str, Any]]) -> dict[str, bool]:
    """スコアの高低ではなく、実データの有無だけで各評価領域の利用可否を判定します。"""
    return {
        "Growth": has_metric_data(parts["Growth"], GROWTH_DATA_KEYS),
        "Financial Health": has_metric_data(parts["Financial Health"], FINANCIAL_HEALTH_DATA_KEYS),
        "Valuation": has_metric_data(parts["Valuation"], VALUATION_DATA_KEYS),
        "Momentum": not prices.empty and len(prices) >= 120,
        "News": len(news_items) >= 5,
    }


def confidence_from_missing(parts: dict[str, dict[str, Any]], availability: dict[str, bool]) -> dict[str, Any]:
    """Confidenceはデータ充足度のみを表します。シグナルの強弱は signal_strength_from_parts が扱います。"""
    total_missing = sum(len(part.get("missing_data", [])) for part in parts.values())
    missing_labels = {label for part in parts.values() for label in part.get("missing_data", [])}
    available_sections = sum(1 for available in availability.values() if available)

    completeness = (available_sections / len(availability)) * 100 - min(35, total_missing * 5)
    has_event_reaction_gap = "event_price_reaction" in missing_labels
    if completeness >= 85 and total_missing == 0 and not has_event_reaction_gap:
        level = "High"
    elif completeness >= 50:
        level = "Medium"
    else:
        level = "Low"

    reasons = [
        f"利用可能な主要データ領域は{len(availability)}領域中 {available_sections} 領域です。",
        f"欠損または計算不可の項目数は {total_missing} 件です。",
    ]
    unavailable = [name for name, available in availability.items() if not available]
    if unavailable:
        reasons.append(f"データが不足している領域: {', '.join(unavailable)}。")
    if level == "Low":
        reasons.append("欠損が多いため、スコアは参考度を下げて扱う必要があります。")
    elif level == "Medium":
        reasons.append("主要データは一定程度ありますが、欠損や未取得項目が残っています。")
    else:
        reasons.append("主要データが比較的そろっており、説明可能性は高めです。")
    if has_event_reaction_gap:
        reasons.append("イベントDBの株価反応が不足しているため、ConfidenceをHighにはしていません。")
    reasons.append("Confidenceはデータ充足度のみの評価で、シグナルの強弱はSignal Strengthに分離しています。")

    return {
        "level": level,
        "completeness_score": round(max(0, min(100, completeness)), 2),
        "reasons": reasons,
    }


def signal_strength_from_parts(parts: dict[str, dict[str, Any]], availability: dict[str, bool]) -> dict[str, Any]:
    """データが確認できた領域に限定し、獲得スコア/満点の比率でシグナル強度を評価します。"""
    earned = 0.0
    evaluated_max = 0.0
    for name, part in parts.items():
        if availability.get(name):
            earned += part["score"]
            evaluated_max += part["max_score"]

    if evaluated_max == 0:
        return {
            "level": "Weak",
            "signal_rate": None,
            "evaluated_max_score": 0,
            "reasons": ["データが確認できた評価領域が無いため、シグナル強度は評価できません。"],
        }

    signal_rate = round(earned / evaluated_max * 100, 2)
    level = signal_strength_level(signal_rate)
    reasons = [
        f"データが確認できた {int(evaluated_max)} 点満点のうち {earned:.0f} 点を獲得し、シグナル充足率は {signal_rate:.1f}% です。",
        f"シグナル強度は {level}(Strong: {SIGNAL_STRENGTH_THRESHOLDS['strong']:.0f}%以上 / Moderate: {SIGNAL_STRENGTH_THRESHOLDS['moderate']:.0f}%以上)です。",
    ]
    return {
        "level": level,
        "signal_rate": signal_rate,
        "evaluated_max_score": int(evaluated_max),
        "reasons": reasons,
    }


def calculate_company_score(
    ticker: str,
    company: dict[str, Any],
    financials: dict[str, Any],
    news_items: list[dict[str, Any]],
    events: list[dict[str, Any]],
    prices: pd.DataFrame,
    sector_companies: list[dict[str, Any]] | None = None,
    benchmark_prices: pd.DataFrame | None = None,
    benchmark_name: str | None = None,
) -> dict[str, Any]:
    parts = {
        "Growth": calculate_growth(financials),
        "Financial Health": calculate_financial_health(financials),
        "Valuation": calculate_valuation(company, sector_companies),
        "Momentum": calculate_momentum(prices, benchmark_prices, benchmark_name),
        "News": calculate_news(news_items, events),
    }
    total_score = sum(part["score"] for part in parts.values())
    availability = data_availability(parts, prices, news_items)
    confidence = confidence_from_missing(parts, availability)
    signal_strength = signal_strength_from_parts(parts, availability)
    evidence_sources = sorted({source for part in parts.values() for source in part["evidence"]})

    return {
        "ticker": ticker,
        "company_name": company.get("company_name"),
        "total_score": total_score,
        "max_score": 100,
        "confidence": confidence,
        "signal_strength": signal_strength,
        "scores": parts,
        "evidence_sources": evidence_sources,
    }
