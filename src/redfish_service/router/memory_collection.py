from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.memory_collection import MemoryCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Systems/{computer_system_id}/Memory", response_model_exclude_none=True)
@router.head("/redfish/v1/Systems/{computer_system_id}/Memory", response_model_exclude_none=True)
@authenticate
async def get1(computer_system_id: str, request: Request, response: Response) -> MemoryCollection:
    s: Service = find_service(MemoryCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(MemoryCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/CacheMemory",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/CacheMemory",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    computer_system_id: str, processor_id: str, request: Request, response: Response
) -> MemoryCollection:
    s: Service = find_service(MemoryCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(MemoryCollection, s.get(**b))


@router.get("/redfish/v1/Chassis/{chassis_id}/Memory", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis/{chassis_id}/Memory", response_model_exclude_none=True)
@authenticate
async def get3(chassis_id: str, request: Request, response: Response) -> MemoryCollection:
    s: Service = find_service(MemoryCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(MemoryCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> MemoryCollection:
    s: Service = find_service(MemoryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(MemoryCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory",
    response_model_exclude_none=True,
)
@authenticate
async def get5(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> MemoryCollection:
    s: Service = find_service(MemoryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(MemoryCollection, s.get(**b))
