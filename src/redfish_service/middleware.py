from http import HTTPStatus
from typing import Final

from starlette.datastructures import Headers, MutableHeaders
from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse, PlainTextResponse, Response
from starlette.routing import Match, Route, Router
from starlette.types import ASGIApp, Message, Receive, Scope, Send

from .exception import GeneralErrorError, PreconditionFailedError, PreconditionRequiredError
from .odata import OdataMetadata

FASTAPI_PATH: Final[list[str]] = [
    "/docs",
    "/openapi.json",
    "/redoc",
]

REDFISH_XML_PATH: Final[list[str]] = [
    "/redfish/v1/$metadata",
]

REDFISH_YAML_PATH: Final[list[str]] = [
    "/redfish/v1/openapi.yaml",
]


class AcceptHeaderMiddleware:
    HEADER_NAME: Final[str] = "Accept"
    SUPPORTED_JSON_MIMES: Final[list[str]] = ["*/*", "application/*", "application/json"]
    SUPPORTED_XML_MIMES: Final[list[str]] = ["*/*", "application/*", "application/xml"]
    SUPPORTED_YAML_MIMES: Final[list[str]] = ["*/*", "application/*", "application/yaml"]

    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        path = scope["path"]
        if path in FASTAPI_PATH:
            await self.app(scope, receive, send)
            return

        headers = Headers(scope=scope)

        if path in REDFISH_XML_PATH:
            if v := headers.getlist(self.HEADER_NAME):
                if not supported_headers(self.SUPPORTED_XML_MIMES, v):
                    exc = GeneralErrorError(HTTPStatus.NOT_ACCEPTABLE)
                    err = OdataMetadata(status_code=exc.status_code)
                    await err(scope, receive, send)
                    return

        elif path in REDFISH_YAML_PATH:
            if v := headers.getlist(self.HEADER_NAME):
                if not supported_headers(self.SUPPORTED_YAML_MIMES, v):
                    exc = GeneralErrorError(HTTPStatus.NOT_ACCEPTABLE)
                    perr = PlainTextResponse(status_code=exc.status_code)
                    await perr(scope, receive, send)
                    return

        elif v := headers.getlist(self.HEADER_NAME):
            if not supported_headers(self.SUPPORTED_JSON_MIMES, v):
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

        methods = get_methods(scope, self.router)

        async def decorated_send(message: Message) -> None:
            if message["type"] == "http.response.start":
                headers = MutableHeaders(scope=message)
                if not headers.get(self.HEADER_NAME, None):
                    headers.append(self.HEADER_NAME, ",".join(methods))

            await send(message)

        await self.app(scope, receive, decorated_send)


class CacheControlHeaderMiddleware(BaseHTTPMiddleware):
    HEADER_NAME: Final[str] = "Cache-Control"

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        res = await call_next(request)

        if not res.headers.get(self.HEADER_NAME, None):
            res.headers.append(self.HEADER_NAME, "no-cache")

        return res


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
    def __init__(
        self, app: ASGIApp, router: Router, dispatch: DispatchFunction | None = None
    ) -> None:
        self.router = router
        super().__init__(app, dispatch)

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        methods = get_methods(request.scope, self.router)

        if methods in ["PATCH", "PUT"] and request.method in ["PATCH", "PUT"]:
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


def get_methods(scope: Scope, router: Router) -> set[str]:
    methods: set[str] = set()
    for route in (r for r in router.routes if isinstance(r, Route)):
        match, _ = route.matches(scope)
        if match != Match.NONE and route.methods:
            methods.update(route.methods)

    return methods


def supported_headers(supported: list[str], values: list[str]) -> bool:
    for value in values:
        for v in value.split(";"):
            if v and any(s for s in supported if s == v.strip()):
                return True

    return False
