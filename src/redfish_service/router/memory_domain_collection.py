from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.memory_domain_collection import MemoryDomainCollection
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/MemoryDomains", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/MemoryDomains", response_model_exclude_none=True
)
async def get1(
    computer_system_id: str, request: Request, response: Response
) -> MemoryDomainCollection:
    s: Service = get_service(MemoryDomainCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(MemoryDomainCollection, s.get(**b))


@router.get("/redfish/v1/Chassis/{chassis_id}/MemoryDomains", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis/{chassis_id}/MemoryDomains", response_model_exclude_none=True)
async def get2(chassis_id: str, request: Request, response: Response) -> MemoryDomainCollection:
    s: Service = get_service(MemoryDomainCollection, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(MemoryDomainCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> MemoryDomainCollection:
    s: Service = get_service(MemoryDomainCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(MemoryDomainCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> MemoryDomainCollection:
    s: Service = get_service(MemoryDomainCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(MemoryDomainCollection, s.get(**b))
