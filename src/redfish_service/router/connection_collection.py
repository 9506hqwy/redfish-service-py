from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.connection import Connection, ConnectionOnCreate
from ..model.connection_collection import ConnectionCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection

router = APIRouter()


@router.get("/redfish/v1/Fabrics/{fabric_id}/Connections", response_model_exclude_none=True)
@router.head("/redfish/v1/Fabrics/{fabric_id}/Connections", response_model_exclude_none=True)
async def get1(fabric_id: str, request: Request, response: Response) -> ConnectionCollection:
    s: Service = get_service(ConnectionCollection, request)
    b: dict[str, Any] = {"fabric_id": fabric_id, "request": request, "response": response}
    return cast(ConnectionCollection, s.get(**b))


@router.post("/redfish/v1/Fabrics/{fabric_id}/Connections", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Connections/Members", response_model_exclude_none=True
)
@authenticate
async def post1(
    fabric_id: str, request: Request, response: Response, body: ConnectionOnCreate
) -> Connection:
    s: ServiceCollection = get_service_collection(ConnectionCollection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Connection, s.post(**b))


@router.get("/redfish/v1/Storage/{storage_id}/Connections", response_model_exclude_none=True)
@router.head("/redfish/v1/Storage/{storage_id}/Connections", response_model_exclude_none=True)
async def get2(storage_id: str, request: Request, response: Response) -> ConnectionCollection:
    s: Service = get_service(ConnectionCollection, request)
    b: dict[str, Any] = {"storage_id": storage_id, "request": request, "response": response}
    return cast(ConnectionCollection, s.get(**b))


@router.post("/redfish/v1/Storage/{storage_id}/Connections", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/Storage/{storage_id}/Connections/Members", response_model_exclude_none=True
)
@authenticate
async def post2(
    storage_id: str, request: Request, response: Response, body: ConnectionOnCreate
) -> Connection:
    s: ServiceCollection = get_service_collection(ConnectionCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Connection, s.post(**b))
