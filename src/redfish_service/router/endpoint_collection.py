from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.endpoint_collection import EndpointCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Fabrics/{fabric_id}/Endpoints", response_model_exclude_none=True)
@authenticate
async def get1(fabric_id: str) -> EndpointCollection:
    s: Service = find_service(EndpointCollection)
    b: dict[str, Any] = {"fabric_id": fabric_id}
    return cast(EndpointCollection, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Endpoints", response_model_exclude_none=True
)
@authenticate
async def get2(storage_service_id: str) -> EndpointCollection:
    s: Service = find_service(EndpointCollection)
    b: dict[str, Any] = {"storage_service_id": storage_service_id}
    return cast(EndpointCollection, s.get(**b))


@router.get("/redfish/v1/Storage/{storage_id}/Endpoints", response_model_exclude_none=True)
@authenticate
async def get3(storage_id: str) -> EndpointCollection:
    s: Service = find_service(EndpointCollection)
    b: dict[str, Any] = {"storage_id": storage_id}
    return cast(EndpointCollection, s.get(**b))
