from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.storage_metrics import StorageMetrics
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/Storage/{storage_id}/Metrics", response_model_exclude_none=True)
@router.head("/redfish/v1/Storage/{storage_id}/Metrics", response_model_exclude_none=True)
async def get1(storage_id: str, request: Request, response: Response) -> StorageMetrics:
    s: Service = get_service(StorageMetrics, request)
    b: dict[str, Any] = {"storage_id": storage_id, "request": request, "response": response}
    return cast(StorageMetrics, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Metrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Metrics",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str, storage_id: str, request: Request, response: Response
) -> StorageMetrics:
    s: Service = get_service(StorageMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
    }
    return cast(StorageMetrics, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Metrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Metrics",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str, storage_id: str, request: Request, response: Response
) -> StorageMetrics:
    s: Service = get_service(StorageMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
    }
    return cast(StorageMetrics, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Metrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Metrics",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    request: Request,
    response: Response,
) -> StorageMetrics:
    s: Service = get_service(StorageMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
    }
    return cast(StorageMetrics, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Metrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Metrics",
    response_model_exclude_none=True,
)
async def get5(
    resource_block_id: str, storage_id: str, request: Request, response: Response
) -> StorageMetrics:
    s: Service = get_service(StorageMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
    }
    return cast(StorageMetrics, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Metrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Metrics",
    response_model_exclude_none=True,
)
async def get6(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    request: Request,
    response: Response,
) -> StorageMetrics:
    s: Service = get_service(StorageMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
    }
    return cast(StorageMetrics, s.get(**b))
