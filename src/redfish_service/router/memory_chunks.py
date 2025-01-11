from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.memory_chunks import MemoryChunks, MemoryChunksOnUpdate
from ..service import Service, find_service

router = APIRouter()


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks/{memory_chunks_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    computer_system_id: str,
    memory_domain_id: str,
    memory_chunks_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = find_service(MemoryChunks)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_domain_id": memory_domain_id,
        "memory_chunks_id": memory_chunks_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks/{memory_chunks_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks/{memory_chunks_id}",
    response_model_exclude_none=True,
)
async def get1(
    computer_system_id: str,
    memory_domain_id: str,
    memory_chunks_id: str,
    request: Request,
    response: Response,
) -> MemoryChunks:
    s: Service = find_service(MemoryChunks)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_domain_id": memory_domain_id,
        "memory_chunks_id": memory_chunks_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(MemoryChunks, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks/{memory_chunks_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    computer_system_id: str,
    memory_domain_id: str,
    memory_chunks_id: str,
    request: Request,
    response: Response,
    body: MemoryChunksOnUpdate,
) -> MemoryChunks:
    s: Service = find_service(MemoryChunks)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_domain_id": memory_domain_id,
        "memory_chunks_id": memory_chunks_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(MemoryChunks, s.patch(**b))


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/MemoryDomains/{memory_domain_id}/MemoryChunks/{memory_chunks_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    chassis_id: str,
    memory_domain_id: str,
    memory_chunks_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = find_service(MemoryChunks)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_domain_id": memory_domain_id,
        "memory_chunks_id": memory_chunks_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/MemoryDomains/{memory_domain_id}/MemoryChunks/{memory_chunks_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/MemoryDomains/{memory_domain_id}/MemoryChunks/{memory_chunks_id}",
    response_model_exclude_none=True,
)
async def get2(
    chassis_id: str,
    memory_domain_id: str,
    memory_chunks_id: str,
    request: Request,
    response: Response,
) -> MemoryChunks:
    s: Service = find_service(MemoryChunks)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_domain_id": memory_domain_id,
        "memory_chunks_id": memory_chunks_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(MemoryChunks, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/MemoryDomains/{memory_domain_id}/MemoryChunks/{memory_chunks_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    chassis_id: str,
    memory_domain_id: str,
    memory_chunks_id: str,
    request: Request,
    response: Response,
    body: MemoryChunksOnUpdate,
) -> MemoryChunks:
    s: Service = find_service(MemoryChunks)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_domain_id": memory_domain_id,
        "memory_chunks_id": memory_chunks_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(MemoryChunks, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks/{memory_chunks_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete3(
    resource_block_id: str,
    computer_system_id: str,
    memory_domain_id: str,
    memory_chunks_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = find_service(MemoryChunks)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_domain_id": memory_domain_id,
        "memory_chunks_id": memory_chunks_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks/{memory_chunks_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks/{memory_chunks_id}",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str,
    computer_system_id: str,
    memory_domain_id: str,
    memory_chunks_id: str,
    request: Request,
    response: Response,
) -> MemoryChunks:
    s: Service = find_service(MemoryChunks)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_domain_id": memory_domain_id,
        "memory_chunks_id": memory_chunks_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(MemoryChunks, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks/{memory_chunks_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    resource_block_id: str,
    computer_system_id: str,
    memory_domain_id: str,
    memory_chunks_id: str,
    request: Request,
    response: Response,
    body: MemoryChunksOnUpdate,
) -> MemoryChunks:
    s: Service = find_service(MemoryChunks)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_domain_id": memory_domain_id,
        "memory_chunks_id": memory_chunks_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(MemoryChunks, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks/{memory_chunks_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete4(
    resource_block_id: str,
    computer_system_id: str,
    memory_domain_id: str,
    memory_chunks_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = find_service(MemoryChunks)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_domain_id": memory_domain_id,
        "memory_chunks_id": memory_chunks_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks/{memory_chunks_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks/{memory_chunks_id}",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str,
    computer_system_id: str,
    memory_domain_id: str,
    memory_chunks_id: str,
    request: Request,
    response: Response,
) -> MemoryChunks:
    s: Service = find_service(MemoryChunks)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_domain_id": memory_domain_id,
        "memory_chunks_id": memory_chunks_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(MemoryChunks, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemoryDomains/{memory_domain_id}/MemoryChunks/{memory_chunks_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    resource_block_id: str,
    computer_system_id: str,
    memory_domain_id: str,
    memory_chunks_id: str,
    request: Request,
    response: Response,
    body: MemoryChunksOnUpdate,
) -> MemoryChunks:
    s: Service = find_service(MemoryChunks)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_domain_id": memory_domain_id,
        "memory_chunks_id": memory_chunks_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(MemoryChunks, s.patch(**b))
