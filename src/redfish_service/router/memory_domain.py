from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.memory_domain import MemoryDomain
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(computer_system_id: str, memory_domain_id: str) -> MemoryDomain:
    s: Service = find_service(MemoryDomain)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_domain_id": memory_domain_id,
    }
    return cast(MemoryDomain, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/MemoryDomains/{memory_domain_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(chassis_id: str, memory_domain_id: str) -> MemoryDomain:
    s: Service = find_service(MemoryDomain)
    b: dict[str, Any] = {"chassis_id": chassis_id, "memory_domain_id": memory_domain_id}
    return cast(MemoryDomain, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(
    resource_block_id: str, computer_system_id: str, memory_domain_id: str
) -> MemoryDomain:
    s: Service = find_service(MemoryDomain)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_domain_id": memory_domain_id,
    }
    return cast(MemoryDomain, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    resource_block_id: str, computer_system_id: str, memory_domain_id: str
) -> MemoryDomain:
    s: Service = find_service(MemoryDomain)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_domain_id": memory_domain_id,
    }
    return cast(MemoryDomain, s.get(**b))
