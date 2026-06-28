from pathlib import Path
from typing import Any

import yaml


def load_yaml(path: Path) -> dict[str, Any]:
    """YAMLファイルを読み込み、空ファイルの場合は空のdictを返します。"""
    if not path.exists():
        raise FileNotFoundError(f"設定ファイルが見つかりません: {path}")

    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file) or {}

    if not isinstance(data, dict):
        raise ValueError(f"YAMLの形式が正しくありません: {path}")

    return data

