from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.memory_domain_collection import MemoryDomainCollection
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/MemoryDomains", response_model_exclude_none=True
)
@authenticate
async def get1(computer_system_id: str) -> MemoryDomainCollection:
    s: Service = find_service(MemoryDomainCollection)
    b: dict[str, Any] = {"computer_system_id": computer_system_id}
    return cast(MemoryDomainCollection, s.get(**b))


@router.get("/redfish/v1/Chassis/{chassis_id}/MemoryDomains", response_model_exclude_none=True)
@authenticate
async def get2(chassis_id: str) -> MemoryDomainCollection:
    s: Service = find_service(MemoryDomainCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id}
    return cast(MemoryDomainCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains",
    response_model_exclude_none=True,
)
@authenticate
async def get3(resource_block_id: str, computer_system_id: str) -> MemoryDomainCollection:
    s: Service = find_service(MemoryDomainCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
    }
    return cast(MemoryDomainCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains",
    response_model_exclude_none=True,
)
@authenticate
async def get4(resource_block_id: str, computer_system_id: str) -> MemoryDomainCollection:
    s: Service = find_service(MemoryDomainCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
    }
    return cast(MemoryDomainCollection, s.get(**b))
