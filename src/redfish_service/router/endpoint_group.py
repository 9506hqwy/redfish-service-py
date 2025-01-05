from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.endpoint_group import EndpointGroup
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Storage/{storage_id}/EndpointGroups/{endpoint_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(storage_id: str, endpoint_group_id: str) -> EndpointGroup:
    s: Service = find_service(EndpointGroup)
    b: dict[str, Any] = {"storage_id": storage_id, "endpoint_group_id": endpoint_group_id}
    return cast(EndpointGroup, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/EndpointGroups/{endpoint_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(computer_system_id: str, storage_id: str, endpoint_group_id: str) -> EndpointGroup:
    s: Service = find_service(EndpointGroup)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "endpoint_group_id": endpoint_group_id,
    }
    return cast(EndpointGroup, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/EndpointGroups/{endpoint_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(storage_service_id: str, endpoint_group_id: str) -> EndpointGroup:
    s: Service = find_service(EndpointGroup)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "endpoint_group_id": endpoint_group_id,
    }
    return cast(EndpointGroup, s.get(**b))


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/EndpointGroups/{endpoint_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get4(fabric_id: str, endpoint_group_id: str) -> EndpointGroup:
    s: Service = find_service(EndpointGroup)
    b: dict[str, Any] = {"fabric_id": fabric_id, "endpoint_group_id": endpoint_group_id}
    return cast(EndpointGroup, s.get(**b))
