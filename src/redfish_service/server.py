from http import HTTPStatus

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

from . import router as redfish
from . import service_impl  # noqa: F401
from .exception import (
    InternalErrorError,
    InvalidURIError,
    MalformedJsonError,
    OperationNotAllowedError,
)
from .exception import RedfishError as RedfishException
from .middleware import (
    AcceptHeaderMiddleware,
    AllowHeaderMiddleware,
    ContentTypeHeaderMiddleware,
    OdataVersionHeaderMiddleware,
)
from .router import swordfish

## TODO: 7 Service requests
## TODO: 8 Service responses

app = FastAPI()
app.add_middleware(AcceptHeaderMiddleware)
app.add_middleware(AllowHeaderMiddleware, app.router)
app.add_middleware(ContentTypeHeaderMiddleware)
app.add_middleware(OdataVersionHeaderMiddleware)
redfish.include_router(app)
swordfish.include_router(app)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(req: Request, exc: StarletteHTTPException) -> JSONResponse:
    match exc.status_code:
        case 404:
            error = InvalidURIError(req.url.path).error
        case 405:
            error = OperationNotAllowedError(None).error
        case _:  # pragma: no cover
            error = InternalErrorError().error
    return JSONResponse(error.model_dump(exclude_none=True), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def request_validation_error_handler(
    req: Request, exc: RequestValidationError
) -> JSONResponse:
    error = MalformedJsonError()
    return JSONResponse(error.error.model_dump(exclude_none=True), status_code=error.status_code)


@app.exception_handler(RedfishException)
async def redfish_exception_handler(req: Request, exc: RedfishException) -> JSONResponse:
    error = exc.error
    headers = None

    if isinstance(exc, OperationNotAllowedError):
        allow: list[str] = []
        if getattr(exc.service, "delete", None):
            allow.append("DELETE")
        if getattr(exc.service, "get", None):
            allow.append("GET")
            allow.append("HEAD")
        if getattr(exc.service, "patch", None):
            allow.append("PATCH")
        if getattr(exc.service, "post", None):
            allow.append("POST")

        headers = {"Allow": ",".join(allow)}

    return JSONResponse(
        error.model_dump(exclude_none=True), status_code=exc.status_code, headers=headers
    )


@app.get("/redfish", response_model_exclude_none=True)
async def root() -> dict[str, str]:
    return {"v1": "/redfish/v1/"}


@app.get("/redfish/v1/odata", response_model_exclude_none=True)
async def odata() -> dict[str, str]:
    raise InternalErrorError(HTTPStatus.NOT_IMPLEMENTED)


@app.get("/redfish/v1/$metadata", response_model_exclude_none=True)
async def metadata() -> dict[str, str]:
    raise InternalErrorError(HTTPStatus.NOT_IMPLEMENTED)
