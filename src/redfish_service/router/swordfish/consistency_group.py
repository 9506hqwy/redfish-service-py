from typing import Any, cast

from fastapi import APIRouter

from ...authenticate import authenticate
from ...model.swordfish.consistency_group import ConsistencyGroup
from ...service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(storage_id: str, consistency_group_id: str) -> ConsistencyGroup:
    s: Service = find_service(ConsistencyGroup)
    b: dict[str, Any] = {"storage_id": storage_id, "consistency_group_id": consistency_group_id}
    return cast(ConsistencyGroup, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    computer_system_id: str, storage_id: str, consistency_group_id: str
) -> ConsistencyGroup:
    s: Service = find_service(ConsistencyGroup)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
    }
    return cast(ConsistencyGroup, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(storage_service_id: str, consistency_group_id: str) -> ConsistencyGroup:
    s: Service = find_service(ConsistencyGroup)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
    }
    return cast(ConsistencyGroup, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/ConsistencyGroups/{consistency_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    storage_service_id: str, volume_id: str, consistency_group_id: str
) -> ConsistencyGroup:
    s: Service = find_service(ConsistencyGroup)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "consistency_group_id": consistency_group_id,
    }
    return cast(ConsistencyGroup, s.get(**b))
