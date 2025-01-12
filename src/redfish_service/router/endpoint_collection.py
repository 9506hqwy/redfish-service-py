from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.endpoint import Endpoint, EndpointOnCreate
from ..model.endpoint_collection import EndpointCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection

router = APIRouter()


@router.get("/redfish/v1/Fabrics/{fabric_id}/Endpoints", response_model_exclude_none=True)
@router.head("/redfish/v1/Fabrics/{fabric_id}/Endpoints", response_model_exclude_none=True)
async def get1(fabric_id: str, request: Request, response: Response) -> EndpointCollection:
    s: Service = get_service(EndpointCollection, request)
    b: dict[str, Any] = {"fabric_id": fabric_id, "request": request, "response": response}
    return cast(EndpointCollection, s.get(**b))


@router.post("/redfish/v1/Fabrics/{fabric_id}/Endpoints", response_model_exclude_none=True)
@router.post("/redfish/v1/Fabrics/{fabric_id}/Endpoints/Members", response_model_exclude_none=True)
@authenticate
async def post1(
    fabric_id: str, request: Request, response: Response, body: EndpointOnCreate
) -> Endpoint:
    s: ServiceCollection = get_service_collection(EndpointCollection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Endpoint, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Endpoints", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/Endpoints", response_model_exclude_none=True
)
async def get2(
    storage_service_id: str, request: Request, response: Response
) -> EndpointCollection:
    s: Service = get_service(EndpointCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }
    return cast(EndpointCollection, s.get(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Endpoints", response_model_exclude_none=True
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Endpoints/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post2(
    storage_service_id: str, request: Request, response: Response, body: EndpointOnCreate
) -> Endpoint:
    s: ServiceCollection = get_service_collection(EndpointCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Endpoint, s.post(**b))


@router.get("/redfish/v1/Storage/{storage_id}/Endpoints", response_model_exclude_none=True)
@router.head("/redfish/v1/Storage/{storage_id}/Endpoints", response_model_exclude_none=True)
async def get3(storage_id: str, request: Request, response: Response) -> EndpointCollection:
    s: Service = get_service(EndpointCollection, request)
    b: dict[str, Any] = {"storage_id": storage_id, "request": request, "response": response}
    return cast(EndpointCollection, s.get(**b))


@router.post("/redfish/v1/Storage/{storage_id}/Endpoints", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/Storage/{storage_id}/Endpoints/Members", response_model_exclude_none=True
)
@authenticate
async def post3(
    storage_id: str, request: Request, response: Response, body: EndpointOnCreate
) -> Endpoint:
    s: ServiceCollection = get_service_collection(EndpointCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Endpoint, s.post(**b))
