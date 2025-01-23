from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.memory_chunks import MemoryChunks, MemoryChunksOnCreate
from ..model.memory_chunks_collection import MemoryChunksCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks",
    response_model_exclude_none=True,
)
async def get1(
    computer_system_id: str, memory_domain_id: str, request: Request, response: Response
) -> MemoryChunksCollection:
    s: Service = get_service(MemoryChunksCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_domain_id": memory_domain_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryChunksCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post1(
    computer_system_id: str,
    memory_domain_id: str,
    request: Request,
    response: Response,
    body: MemoryChunksOnCreate,
) -> MemoryChunks:
    s: ServiceCollection = get_service_collection(MemoryChunksCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_domain_id": memory_domain_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(MemoryChunks, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/MemoryDomains/{memory_domain_id}/MemoryChunks",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/MemoryDomains/{memory_domain_id}/MemoryChunks",
    response_model_exclude_none=True,
)
async def get2(
    chassis_id: str, memory_domain_id: str, request: Request, response: Response
) -> MemoryChunksCollection:
    s: Service = get_service(MemoryChunksCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_domain_id": memory_domain_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryChunksCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/MemoryDomains/{memory_domain_id}/MemoryChunks",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/MemoryDomains/{memory_domain_id}/MemoryChunks/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post2(
    chassis_id: str,
    memory_domain_id: str,
    request: Request,
    response: Response,
    body: MemoryChunksOnCreate,
) -> MemoryChunks:
    s: ServiceCollection = get_service_collection(MemoryChunksCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_domain_id": memory_domain_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(MemoryChunks, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str,
    computer_system_id: str,
    memory_domain_id: str,
    request: Request,
    response: Response,
) -> MemoryChunksCollection:
    s: Service = get_service(MemoryChunksCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_domain_id": memory_domain_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryChunksCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post3(
    resource_block_id: str,
    computer_system_id: str,
    memory_domain_id: str,
    request: Request,
    response: Response,
    body: MemoryChunksOnCreate,
) -> MemoryChunks:
    s: ServiceCollection = get_service_collection(MemoryChunksCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_domain_id": memory_domain_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(MemoryChunks, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str,
    computer_system_id: str,
    memory_domain_id: str,
    request: Request,
    response: Response,
) -> MemoryChunksCollection:
    s: Service = get_service(MemoryChunksCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_domain_id": memory_domain_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryChunksCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post4(
    resource_block_id: str,
    computer_system_id: str,
    memory_domain_id: str,
    request: Request,
    response: Response,
    body: MemoryChunksOnCreate,
) -> MemoryChunks:
    s: ServiceCollection = get_service_collection(MemoryChunksCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_domain_id": memory_domain_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(MemoryChunks, s.post(**b))
