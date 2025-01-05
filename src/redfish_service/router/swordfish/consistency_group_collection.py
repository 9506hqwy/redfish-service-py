from typing import Any, cast

from fastapi import APIRouter

from ...model.swordfish.consistency_group_collection import ConsistencyGroupCollection
from ...service import Service, find_service
from .. import authenticate

router = APIRouter()


@router.get("/redfish/v1/Storage/{storage_id}/ConsistencyGroups", response_model_exclude_none=True)
@authenticate
async def get1(storage_id: str) -> ConsistencyGroupCollection:
    s: Service = find_service(ConsistencyGroupCollection)
    b: dict[str, Any] = {"storage_id": storage_id}
    return cast(ConsistencyGroupCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups",
    response_model_exclude_none=True,
)
@authenticate
async def get2(computer_system_id: str, storage_id: str) -> ConsistencyGroupCollection:
    s: Service = find_service(ConsistencyGroupCollection)
    b: dict[str, Any] = {"computer_system_id": computer_system_id, "storage_id": storage_id}
    return cast(ConsistencyGroupCollection, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups",
    response_model_exclude_none=True,
)
@authenticate
async def get3(storage_service_id: str) -> ConsistencyGroupCollection:
    s: Service = find_service(ConsistencyGroupCollection)
    b: dict[str, Any] = {"storage_service_id": storage_service_id}
    return cast(ConsistencyGroupCollection, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/ConsistencyGroups",
    response_model_exclude_none=True,
)
@authenticate
async def get4(storage_service_id: str, volume_id: str) -> ConsistencyGroupCollection:
    s: Service = find_service(ConsistencyGroupCollection)
    b: dict[str, Any] = {"storage_service_id": storage_service_id, "volume_id": volume_id}
    return cast(ConsistencyGroupCollection, s.get(**b))
