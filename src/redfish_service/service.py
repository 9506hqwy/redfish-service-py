from http import HTTPStatus

from fastapi import FastAPI
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

from .exception import InternalErrorError, InvalidURIError
from .exception import RedfishError as RedfishException
from .router import PATH_SERVICE_ROOT, PATH_SESSION_COLLECTION, service_root, session_collection

## TODO: 7 Service requests
## TODO: 8 Service responses

app = FastAPI()
app.include_router(service_root.router, prefix=PATH_SERVICE_ROOT)
app.include_router(session_collection.router, prefix=PATH_SESSION_COLLECTION)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(req: Request, exc: StarletteHTTPException) -> JSONResponse:
    match exc.status_code:
        case 404:
            error = InvalidURIError(req.url.path).error
        case _:  # pragma: no cover
            error = InternalErrorError().error
    return JSONResponse(error.model_dump(exclude_none=True), status_code=exc.status_code)


@app.exception_handler(RedfishException)
async def redfish_exception_handler(req: Request, exc: RedfishException) -> JSONResponse:
    error = exc.error
    return JSONResponse(error.model_dump(exclude_none=True), status_code=exc.status_code)


@app.get("/redfish", response_model_exclude_none=True)
async def root() -> dict[str, str]:
    return {"v1": f"{PATH_SERVICE_ROOT}/"}


@app.get("/redfish/v1/odata", response_model_exclude_none=True)
async def odata() -> dict[str, str]:
    raise InternalErrorError(HTTPStatus.NOT_IMPLEMENTED)


@app.get("/redfish/v1/$metadata", response_model_exclude_none=True)
async def metadata() -> dict[str, str]:
    raise InternalErrorError(HTTPStatus.NOT_IMPLEMENTED)
