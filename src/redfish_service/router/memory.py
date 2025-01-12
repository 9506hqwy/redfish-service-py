from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.memory import Memory, MemoryOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}", response_model_exclude_none=True
)
async def get1(
    computer_system_id: str, memory_id: str, request: Request, response: Response
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    return cast(Memory, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}", response_model_exclude_none=True
)
@authenticate
async def patch1(
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: MemoryOnUpdate,
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Memory, s.patch(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/CacheMemory/{memory_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/CacheMemory/{memory_id}",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str,
    processor_id: str,
    memory_id: str,
    request: Request,
    response: Response,
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    return cast(Memory, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/CacheMemory/{memory_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    computer_system_id: str,
    processor_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: MemoryOnUpdate,
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Memory, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}", response_model_exclude_none=True
)
async def get3(chassis_id: str, memory_id: str, request: Request, response: Response) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    return cast(Memory, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}", response_model_exclude_none=True
)
@authenticate
async def patch3(
    chassis_id: str, memory_id: str, request: Request, response: Response, body: MemoryOnUpdate
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Memory, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str, memory_id: str, request: Request, response: Response
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    return cast(Memory, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: MemoryOnUpdate,
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Memory, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
async def get5(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    return cast(Memory, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: MemoryOnUpdate,
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Memory, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
async def get6(
    resource_block_id: str, memory_id: str, request: Request, response: Response
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    return cast(Memory, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: MemoryOnUpdate,
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Memory, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
async def get7(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    return cast(Memory, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch7(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: MemoryOnUpdate,
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Memory, s.patch(**b))
