import os
import secrets
from typing import Any

from fastapi import Header, HTTPException


def get_optional_client_context() -> dict[str, Any]:
    """Placeholder for future API Key, JWT, or OAuth authentication."""
    return {
        "authenticated": False,
        "method": "none",
    }


def configured_api_key() -> str | None:
    api_key = os.getenv("COMPASS_API_KEY", "").strip()
    return api_key or None


def optional_api_key_auth(x_api_key: str | None = Header(default=None, alias="X-API-Key")) -> dict[str, Any]:
    expected_key = configured_api_key()
    if expected_key is None:
        return get_optional_client_context()
    if x_api_key is None or not secrets.compare_digest(x_api_key, expected_key):
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
    return {
        "authenticated": True,
        "method": "api_key",
    }
