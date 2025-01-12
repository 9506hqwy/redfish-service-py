from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...model.swordfish.consistency_group_collection import ConsistencyGroupCollection
from ...service import Service
from ...util import get_service

router = APIRouter()


@router.get("/redfish/v1/Storage/{storage_id}/ConsistencyGroups", response_model_exclude_none=True)
@router.head(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups", response_model_exclude_none=True
)
async def get1(
    storage_id: str, request: Request, response: Response
) -> ConsistencyGroupCollection:
    s: Service = get_service(ConsistencyGroupCollection, request)
    b: dict[str, Any] = {"storage_id": storage_id, "request": request, "response": response}
    return cast(ConsistencyGroupCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str, storage_id: str, request: Request, response: Response
) -> ConsistencyGroupCollection:
    s: Service = get_service(ConsistencyGroupCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
    }
    return cast(ConsistencyGroupCollection, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups",
    response_model_exclude_none=True,
)
async def get3(
    storage_service_id: str, request: Request, response: Response
) -> ConsistencyGroupCollection:
    s: Service = get_service(ConsistencyGroupCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }
    return cast(ConsistencyGroupCollection, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/ConsistencyGroups",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/ConsistencyGroups",
    response_model_exclude_none=True,
)
async def get4(
    storage_service_id: str, volume_id: str, request: Request, response: Response
) -> ConsistencyGroupCollection:
    s: Service = get_service(ConsistencyGroupCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    return cast(ConsistencyGroupCollection, s.get(**b))
