from typing import cast

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
    ResourceNotFoundError,
)
from .exception import RedfishError as RedfishException
from .middleware import (
    AcceptHeaderMiddleware,
    AllowHeaderMiddleware,
    CacheControlHeaderMiddleware,
    ContentTypeHeaderMiddleware,
    IfMatchHeaderMiddleware,
    OdataVersionHeaderMiddleware,
)
from .model.service_root import ServiceRoot
from .odata import OdataMetadata, OdataService, OdataServiceValue
from .repository import instances
from .router import swordfish

## TODO: 7 Service requests
## TODO: 8 Service responses

app = FastAPI()
app.add_middleware(AcceptHeaderMiddleware)
app.add_middleware(AllowHeaderMiddleware, app.router)
app.add_middleware(CacheControlHeaderMiddleware)
app.add_middleware(ContentTypeHeaderMiddleware)
app.add_middleware(IfMatchHeaderMiddleware, app.router)
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
async def odata() -> OdataService:
    root = instances.find_by_type(ServiceRoot)
    if root is None:
        raise ResourceNotFoundError("ServiceRoot", "ServiceRoot")

    response = OdataService(odata_context="/redfish/v1/$metadata", value=[])
    response.value.append(OdataServiceValue(name="Service", url=root.odata_id))

    if id := root.account_service:
        response.value.append(OdataServiceValue(name="Account", url=cast(str, id.odata_id)))

    return response


@app.get("/redfish/v1/$metadata", response_model_exclude_none=True)
async def metadata() -> OdataMetadata:
    # TODO:
    models: list[str] = [
        "AccountService.v1_17_0.AccountService",
        "ManagerAccount.v1_13_0.ManagerAccount",
        "ManagerAccountCollection.ManagerAccountCollection",
        "Role.v1_3_3.Role",
        "RoleCollection.RoleCollection",
        "ServiceRoot.v1_17_0.ServiceRoot",
        "Session.v1_8_0.Session",
        "SessionCollection.SessionCollection",
    ]

    content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    content += '<edmx:Edmx xmlns:edmx="http://docs.oasis-open.org/odata/ns/edmx" Version="4.0">\n'
    for model in models:
        m = model.split(".")
        content += f'  <edmx:Reference Uri="http://redfish.dmtf.org/schemas/v1/{m[0]}_v1.xml">\n'
        content += f'    <edmx:Include Namespace="{m[0]}"/>\n'
        if len(m) > 2:
            content += f'    <edmx:Include Namespace="{m[0]}.{m[1]}"/>\n'
        content += "  </edmx:Reference>\n"

    content += "  <edmx:DataServices>\n"
    content += '    <Schema xmlns="http://docs.oasis-open.org/odata/ns/edm" Namespace="Service">\n'
    content += (
        '      <EntityContainer Name="Service" Extends="ServiceRoot.v1_17_0.ServiceContainer"/>\n'
    )
    content += "    </Schema>\n"
    content += "  </edmx:DataServices>\n"

    content += "</edmx:Edmx>\n"
    return OdataMetadata(content=content)
