from datetime import datetime, timezone
from typing import Any

from pydantic import BaseModel, Field


API_VERSION = "v1"


class ErrorBody(BaseModel):
    code: int
    message: str


class ApiResponse(BaseModel):
    success: bool
    data: Any = None
    timestamp: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    version: str = API_VERSION
    error: ErrorBody | None = None


def success_response(data: Any) -> ApiResponse:
    return ApiResponse(success=True, data=data)


def error_response(status_code: int, message: str) -> ApiResponse:
    return ApiResponse(success=False, data=None, error=ErrorBody(code=status_code, message=message))
