"""
Fenwick's shared error-handling convention (section 4.4). Every endpoint
in this codebase raises APIError rather than a bare HTTPException, so
every error response has the same predictable shape — this is exactly
what few-shot examples pulled from this file are meant to teach a model
to replicate on a new endpoint.
"""

from fastapi import Request
from fastapi.responses import JSONResponse


class APIError(Exception):
    def __init__(self, code: str, status_code: int, detail: str):
        self.code = code
        self.status_code = status_code
        self.detail = detail


def register_exception_handlers(app):
    @app.exception_handler(APIError)
    async def api_error_handler(request: Request, exc: APIError):
        return JSONResponse(
            status_code=exc.status_code,
            content={"error_code": exc.code, "detail": exc.detail},
        )
