from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from api.routes import companies, discovery, learning, market, notifications, proposals, scoring, validation
from api.schemas.response import error_response, success_response


API_PREFIX = "/api/v1"


app = FastAPI(
    title="Compass API",
    description="Read-only API for Compass generated research data.",
    version="v1",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(status_code=exc.status_code, content=error_response(exc.status_code, str(exc.detail)).model_dump())


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(status_code=400, content=error_response(400, "Invalid request parameters").model_dump())


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content=error_response(500, "Internal server error").model_dump())


@app.get(f"{API_PREFIX}/health", tags=["Health"])
def health():
    return success_response({"status": "ok", "api_version": "v1"})


app.include_router(companies.router, prefix=API_PREFIX)
app.include_router(discovery.router, prefix=API_PREFIX)
app.include_router(scoring.router, prefix=API_PREFIX)
app.include_router(market.router, prefix=API_PREFIX)
app.include_router(validation.router, prefix=API_PREFIX)
app.include_router(proposals.router, prefix=API_PREFIX)
app.include_router(learning.router, prefix=API_PREFIX)
app.include_router(notifications.router, prefix=API_PREFIX)
