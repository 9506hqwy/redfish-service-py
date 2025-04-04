from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.memory_domain import MemoryDomain
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}",
    response_model_exclude_none=True,
)
async def get1(
    computer_system_id: str, memory_domain_id: str, request: Request, response: Response
) -> MemoryDomain:
    s: Service = get_service(MemoryDomain, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_domain_id": memory_domain_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryDomain, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/MemoryDomains/{memory_domain_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/MemoryDomains/{memory_domain_id}",
    response_model_exclude_none=True,
)
async def get2(
    chassis_id: str, memory_domain_id: str, request: Request, response: Response
) -> MemoryDomain:
    s: Service = get_service(MemoryDomain, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_domain_id": memory_domain_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryDomain, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str,
    computer_system_id: str,
    memory_domain_id: str,
    request: Request,
    response: Response,
) -> MemoryDomain:
    s: Service = get_service(MemoryDomain, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_domain_id": memory_domain_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryDomain, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str,
    computer_system_id: str,
    memory_domain_id: str,
    request: Request,
    response: Response,
) -> MemoryDomain:
    s: Service = get_service(MemoryDomain, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_domain_id": memory_domain_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryDomain, s.get(**b))
    set_link_header(m, response)
    return m
