from http import HTTPStatus
from typing import Final

from starlette.datastructures import Headers, MutableHeaders
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Match, Route, Router
from starlette.types import ASGIApp, Message, Receive, Scope, Send

from .exception import GeneralErrorError, PreconditionFailedError, PreconditionRequiredError

FASTAPI_PATH: Final[list[str]] = [
    "/docs",
    "/openapi.json",
]


class AcceptHeaderMiddleware:
    HEADER_NAME: Final[str] = "Accept"
    SUPPORTED_MIMES: Final[list[str]] = ["*/*", "application/*", "application/json"]

    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        if scope["path"] in FASTAPI_PATH:
            await self.app(scope, receive, send)
            return

        headers = Headers(scope=scope)
        if v := headers.getlist(self.HEADER_NAME):
            if not supported_headers(self.SUPPORTED_MIMES, v):
                exc = GeneralErrorError(HTTPStatus.NOT_ACCEPTABLE)
                res = JSONResponse(
                    exc.error.model_dump(exclude_none=True), status_code=exc.status_code
                )
                await res(scope, receive, send)
                return

        await self.app(scope, receive, send)


class AllowHeaderMiddleware:
    HEADER_NAME: Final[str] = "Allow"

    def __init__(self, app: ASGIApp, router: Router) -> None:
        self.app = app
        self.router = router

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        if scope["path"] in FASTAPI_PATH:
            await self.app(scope, receive, send)
            return

        async def decorated_send(message: Message) -> None:
            if message["type"] == "http.response.start":
                headers = MutableHeaders(scope=message)
                if not headers.get(self.HEADER_NAME, None):
                    headers.append(self.HEADER_NAME, ",".join(methods))

            await send(message)

        methods: set[str] = set()
        for route in (r for r in self.router.routes if isinstance(r, Route)):
            match, _ = route.matches(scope)
            if match != Match.NONE and route.methods:
                methods.update(route.methods)

        await self.app(scope, receive, decorated_send)


class ContentTypeHeaderMiddleware:
    HEADER_NAME: Final[str] = "Content-Type"
    SUPPORTED_MIMES: Final[list[str]] = ["application/json"]

    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        if scope["path"] in FASTAPI_PATH:
            await self.app(scope, receive, send)
            return

        if scope["method"] not in ["PATCH", "POST", "PUT"]:
            await self.app(scope, receive, send)
            return

        headers = Headers(scope=scope)
        if v := headers.getlist(self.HEADER_NAME):
            if not supported_headers(self.SUPPORTED_MIMES, v):
                exc = GeneralErrorError(HTTPStatus.UNSUPPORTED_MEDIA_TYPE)
                res = JSONResponse(
                    exc.error.model_dump(exclude_none=True), status_code=exc.status_code
                )
                await res(scope, receive, send)
                return

        await self.app(scope, receive, send)


class IfMatchHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        if request.method in ["PATCH", "PUT"]:
            if not request.headers.get("If-Match", None):
                exc = PreconditionRequiredError()
                return JSONResponse(
                    exc.error.model_dump(exclude_none=True), status_code=exc.status_code
                )

        return await call_next(request)


class OdataVersionHeaderMiddleware:
    HEADER_NAME: Final[str] = "ODATA-Version"
    SUPPORTED_VETRSIONS: Final[list[str]] = ["4.0"]

    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        if scope["path"] in FASTAPI_PATH:
            await self.app(scope, receive, send)
            return

        async def decorated_send(message: Message) -> None:
            if message["type"] == "http.response.start":
                headers = MutableHeaders(scope=message)
                headers.append(self.HEADER_NAME, self.SUPPORTED_VETRSIONS[-1])

            await send(message)

        headers = Headers(scope=scope)
        if v := headers.getlist(self.HEADER_NAME):
            if not supported_headers(self.SUPPORTED_VETRSIONS, v):
                exc = PreconditionFailedError()
                res = JSONResponse(
                    exc.error.model_dump(exclude_none=True), status_code=exc.status_code
                )
                await res(scope, receive, decorated_send)
                return

        await self.app(scope, receive, decorated_send)


def supported_headers(supported: list[str], values: list[str]) -> bool:
    for value in values:
        for v in value.split(";"):
            if v and any((s for s in supported if s == v.strip())):
                return True

    return False
