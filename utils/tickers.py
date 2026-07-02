from pathlib import Path

from utils.config import load_yaml


def load_tickers(config_path: Path) -> list[str]:
    """config/tickers.yaml から監視対象の銘柄一覧を読み込みます。"""
    config = load_yaml(config_path)

    tickers = config.get("tickers", [])
    if not isinstance(tickers, list) or not tickers:
        raise ValueError("config/tickers.yaml の tickers に銘柄を1つ以上指定してください。")

    # 空文字や余分なスペースを取り除き、大文字のティッカーに揃えます。
    cleaned = [str(ticker).strip().upper() for ticker in tickers if str(ticker).strip()]
    if not cleaned:
        raise ValueError("有効な銘柄がありません。config/tickers.yaml を確認してください。")

    return cleaned


def load_benchmarks(config_path: Path) -> list[str]:
    """config/tickers.yaml の benchmarks を読み込みます。未定義の場合は空リストです。

    ベンチマークは価格収集のみの対象で、スコアリングやDiscoveryには含めません。
    """
    config = load_yaml(config_path)

    benchmarks = config.get("benchmarks", [])
    if not isinstance(benchmarks, list):
        return []

    return [str(ticker).strip().upper() for ticker in benchmarks if str(ticker).strip()]
