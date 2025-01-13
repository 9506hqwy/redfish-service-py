from http import HTTPStatus
from typing import Final

from starlette.datastructures import Headers, MutableHeaders
from starlette.responses import JSONResponse
from starlette.types import ASGIApp, Message, Receive, Scope, Send

from .exception import GeneralErrorError, PreconditionFailedError


class AcceptHeaderMiddleware:
    HEADER_NAME: Final[str] = "Accept"
    SUPPORTED_MIMES: Final[list[str]] = ["*/*", "application/*", "application/json"]

    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        headers = Headers(scope=scope)
        if v := headers.getlist(self.HEADER_NAME):
            if all((s not in v for s in self.SUPPORTED_MIMES)):
                exc = GeneralErrorError(HTTPStatus.NOT_ACCEPTABLE)
                res = JSONResponse(
                    exc.error.model_dump(exclude_none=True), status_code=exc.status_code
                )
                await res(scope, receive, send)
                return

        await self.app(scope, receive, send)


class ContentTypeHeaderMiddleware:
    HEADER_NAME: Final[str] = "Content-Type"
    SUPPORTED_MIMES: Final[list[str]] = ["application/json"]

    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        if scope["method"] not in ["PATCH", "POST", "PUT"]:
            await self.app(scope, receive, send)
            return

        headers = Headers(scope=scope)
        if v := headers.getlist(self.HEADER_NAME):
            if all((s not in v for s in self.SUPPORTED_MIMES)):
                exc = GeneralErrorError(HTTPStatus.UNSUPPORTED_MEDIA_TYPE)
                res = JSONResponse(
                    exc.error.model_dump(exclude_none=True), status_code=exc.status_code
                )
                await res(scope, receive, send)
                return

        await self.app(scope, receive, send)


class OdataVersionHeaderMiddleware:
    HEADER_NAME: Final[str] = "ODATA-Version"
    SUPPORTED_VETRSIONS: Final[list[str]] = ["4.0"]

    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        async def decorated_send(message: Message) -> None:
            if message["type"] == "http.response.start":
                headers = MutableHeaders(scope=message)
                headers.append(self.HEADER_NAME, self.SUPPORTED_VETRSIONS[-1])

            await send(message)

        headers = Headers(scope=scope)
        if v := headers.get(self.HEADER_NAME):
            if v not in self.SUPPORTED_VETRSIONS:
                exc = PreconditionFailedError()
                res = JSONResponse(
                    exc.error.model_dump(exclude_none=True), status_code=exc.status_code
                )
                await res(scope, receive, decorated_send)
                return

        await self.app(scope, receive, decorated_send)
