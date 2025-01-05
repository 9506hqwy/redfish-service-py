from typing import Any, cast

from fastapi import APIRouter

from ..model.memory import Memory
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}", response_model_exclude_none=True
)
@authenticate
async def get1(computer_system_id: str, memory_id: str) -> Memory:
    s: Service = find_service(Memory)
    b: dict[str, Any] = {"computer_system_id": computer_system_id, "memory_id": memory_id}
    return cast(Memory, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/CacheMemory/{memory_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(computer_system_id: str, processor_id: str, memory_id: str) -> Memory:
    s: Service = find_service(Memory)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "memory_id": memory_id,
    }
    return cast(Memory, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}", response_model_exclude_none=True
)
@authenticate
async def get3(chassis_id: str, memory_id: str) -> Memory:
    s: Service = find_service(Memory)
    b: dict[str, Any] = {"chassis_id": chassis_id, "memory_id": memory_id}
    return cast(Memory, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get4(resource_block_id: str, memory_id: str) -> Memory:
    s: Service = find_service(Memory)
    b: dict[str, Any] = {"resource_block_id": resource_block_id, "memory_id": memory_id}
    return cast(Memory, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get5(resource_block_id: str, computer_system_id: str, memory_id: str) -> Memory:
    s: Service = find_service(Memory)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
    }
    return cast(Memory, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get6(resource_block_id: str, memory_id: str) -> Memory:
    s: Service = find_service(Memory)
    b: dict[str, Any] = {"resource_block_id": resource_block_id, "memory_id": memory_id}
    return cast(Memory, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get7(resource_block_id: str, computer_system_id: str, memory_id: str) -> Memory:
    s: Service = find_service(Memory)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
    }
    return cast(Memory, s.get(**b))
