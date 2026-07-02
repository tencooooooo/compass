import json
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]

from mcp.prompts import get_prompt, list_prompts
from mcp.resources import list_resources, read_resource
from mcp.tools import call_tool, list_tools


SERVER_INFO = {"name": "compass-mcp-server", "version": "v1"}
PROTOCOL_VERSION = "2024-11-05"


def handle_request(request: dict[str, Any]) -> dict[str, Any] | None:
    request_id = request.get("id")
    method = request.get("method")
    params = request.get("params") or {}

    try:
        if method == "initialize":
            result = {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {
                    "tools": {},
                    "resources": {},
                    "prompts": {},
                },
                "serverInfo": SERVER_INFO,
            }
        elif method == "tools/list":
            result = {"tools": list_tools()}
        elif method == "tools/call":
            result = {"content": call_tool(params.get("name", ""), params.get("arguments") or {})}
        elif method == "resources/list":
            result = {"resources": list_resources()}
        elif method == "resources/read":
            result = {"contents": read_resource(params.get("uri", ""))}
        elif method == "prompts/list":
            result = {"prompts": list_prompts()}
        elif method == "prompts/get":
            result = get_prompt(params.get("name", ""), params.get("arguments") or {})
        elif method == "notifications/initialized":
            return None
        else:
            return _error(request_id, -32601, f"Method not found: {method}")
        return {"jsonrpc": "2.0", "id": request_id, "result": result}
    except Exception as exc:
        return _error(request_id, -32000, str(exc))


def serve_stdio() -> None:
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            request = json.loads(line.lstrip("\ufeff"))
            response = handle_request(request)
        except json.JSONDecodeError as exc:
            response = _error(None, -32700, f"Parse error: {exc}")
        if response is not None:
            sys.stdout.write(json.dumps(response, ensure_ascii=False) + "\n")
            sys.stdout.flush()


def _error(request_id: Any, code: int, message: str) -> dict[str, Any]:
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "error": {
            "code": code,
            "message": message,
        },
    }


if __name__ == "__main__":
    serve_stdio()
