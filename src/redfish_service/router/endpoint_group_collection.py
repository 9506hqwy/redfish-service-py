from typing import Any, cast

from fastapi import APIRouter

from ..model.endpoint_group_collection import EndpointGroupCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/Storage/{storage_id}/EndpointGroups", response_model_exclude_none=True)
@authenticate
async def get1(storage_id: str) -> EndpointGroupCollection:
    s: Service = find_service(EndpointGroupCollection)
    b: dict[str, Any] = {"storage_id": storage_id}
    return cast(EndpointGroupCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/EndpointGroups",
    response_model_exclude_none=True,
)
@authenticate
async def get2(computer_system_id: str, storage_id: str) -> EndpointGroupCollection:
    s: Service = find_service(EndpointGroupCollection)
    b: dict[str, Any] = {"computer_system_id": computer_system_id, "storage_id": storage_id}
    return cast(EndpointGroupCollection, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/EndpointGroups",
    response_model_exclude_none=True,
)
@authenticate
async def get3(storage_service_id: str) -> EndpointGroupCollection:
    s: Service = find_service(EndpointGroupCollection)
    b: dict[str, Any] = {"storage_service_id": storage_service_id}
    return cast(EndpointGroupCollection, s.get(**b))


@router.get("/redfish/v1/Fabrics/{fabric_id}/EndpointGroups", response_model_exclude_none=True)
@authenticate
async def get4(fabric_id: str) -> EndpointGroupCollection:
    s: Service = find_service(EndpointGroupCollection)
    b: dict[str, Any] = {"fabric_id": fabric_id}
    return cast(EndpointGroupCollection, s.get(**b))
