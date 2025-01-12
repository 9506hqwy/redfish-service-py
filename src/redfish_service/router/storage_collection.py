from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.storage_collection import StorageCollection
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/Storage", response_model_exclude_none=True)
@router.head("/redfish/v1/Storage", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> StorageCollection:
    s: Service = get_service(StorageCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    return cast(StorageCollection, s.get(**b))


@router.get("/redfish/v1/Systems/{computer_system_id}/Storage", response_model_exclude_none=True)
@router.head("/redfish/v1/Systems/{computer_system_id}/Storage", response_model_exclude_none=True)
async def get2(computer_system_id: str, request: Request, response: Response) -> StorageCollection:
    s: Service = get_service(StorageCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    return cast(StorageCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage",
    response_model_exclude_none=True,
)
async def get3(resource_block_id: str, request: Request, response: Response) -> StorageCollection:
    s: Service = get_service(StorageCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "request": request,
        "response": response,
    }
    return cast(StorageCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> StorageCollection:
    s: Service = get_service(StorageCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    return cast(StorageCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage", response_model_exclude_none=True
)
async def get5(resource_block_id: str, request: Request, response: Response) -> StorageCollection:
    s: Service = get_service(StorageCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "request": request,
        "response": response,
    }
    return cast(StorageCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage",
    response_model_exclude_none=True,
)
async def get6(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> StorageCollection:
    s: Service = get_service(StorageCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    return cast(StorageCollection, s.get(**b))
