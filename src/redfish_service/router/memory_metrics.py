from typing import Any, cast

from fastapi import APIRouter

from ..model.memory_metrics import MemoryMetrics
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def get1(computer_system_id: str) -> MemoryMetrics:
    s: Service = find_service(MemoryMetrics)
    b: dict[str, Any] = {"computer_system_id": computer_system_id}
    return cast(MemoryMetrics, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/MemoryMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def get2(computer_system_id: str, memory_id: str) -> MemoryMetrics:
    s: Service = find_service(MemoryMetrics)
    b: dict[str, Any] = {"computer_system_id": computer_system_id, "memory_id": memory_id}
    return cast(MemoryMetrics, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/CacheMemory/{memory_id}/MemoryMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def get3(computer_system_id: str, processor_id: str, memory_id: str) -> MemoryMetrics:
    s: Service = find_service(MemoryMetrics)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "memory_id": memory_id,
    }
    return cast(MemoryMetrics, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def get4(computer_system_id: str, processor_id: str) -> MemoryMetrics:
    s: Service = find_service(MemoryMetrics)
    b: dict[str, Any] = {"computer_system_id": computer_system_id, "processor_id": processor_id}
    return cast(MemoryMetrics, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/MemoryMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def get5(resource_block_id: str, memory_id: str) -> MemoryMetrics:
    s: Service = find_service(MemoryMetrics)
    b: dict[str, Any] = {"resource_block_id": resource_block_id, "memory_id": memory_id}
    return cast(MemoryMetrics, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def get6(resource_block_id: str, processor_id: str) -> MemoryMetrics:
    s: Service = find_service(MemoryMetrics)
    b: dict[str, Any] = {"resource_block_id": resource_block_id, "processor_id": processor_id}
    return cast(MemoryMetrics, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/MemoryMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def get7(resource_block_id: str, computer_system_id: str, memory_id: str) -> MemoryMetrics:
    s: Service = find_service(MemoryMetrics)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
    }
    return cast(MemoryMetrics, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def get8(resource_block_id: str, computer_system_id: str) -> MemoryMetrics:
    s: Service = find_service(MemoryMetrics)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
    }
    return cast(MemoryMetrics, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def get9(
    resource_block_id: str, computer_system_id: str, processor_id: str
) -> MemoryMetrics:
    s: Service = find_service(MemoryMetrics)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
    }
    return cast(MemoryMetrics, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/MemoryMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def get10(resource_block_id: str, memory_id: str) -> MemoryMetrics:
    s: Service = find_service(MemoryMetrics)
    b: dict[str, Any] = {"resource_block_id": resource_block_id, "memory_id": memory_id}
    return cast(MemoryMetrics, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def get11(resource_block_id: str, processor_id: str) -> MemoryMetrics:
    s: Service = find_service(MemoryMetrics)
    b: dict[str, Any] = {"resource_block_id": resource_block_id, "processor_id": processor_id}
    return cast(MemoryMetrics, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/MemoryMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def get12(resource_block_id: str, computer_system_id: str, memory_id: str) -> MemoryMetrics:
    s: Service = find_service(MemoryMetrics)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
    }
    return cast(MemoryMetrics, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def get13(resource_block_id: str, computer_system_id: str) -> MemoryMetrics:
    s: Service = find_service(MemoryMetrics)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
    }
    return cast(MemoryMetrics, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def get14(
    resource_block_id: str, computer_system_id: str, processor_id: str
) -> MemoryMetrics:
    s: Service = find_service(MemoryMetrics)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
    }
    return cast(MemoryMetrics, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/MemoryMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def get15(chassis_id: str, memory_id: str) -> MemoryMetrics:
    s: Service = find_service(MemoryMetrics)
    b: dict[str, Any] = {"chassis_id": chassis_id, "memory_id": memory_id}
    return cast(MemoryMetrics, s.get(**b))
