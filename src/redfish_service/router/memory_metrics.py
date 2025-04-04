from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.memory_metrics import MemoryMetrics
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
async def get1(computer_system_id: str, request: Request, response: Response) -> MemoryMetrics:
    s: Service = get_service(MemoryMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryMetrics, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/MemoryMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/MemoryMetrics",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str, memory_id: str, request: Request, response: Response
) -> MemoryMetrics:
    s: Service = get_service(MemoryMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryMetrics, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/CacheMemory/{memory_id}/MemoryMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/CacheMemory/{memory_id}/MemoryMetrics",
    response_model_exclude_none=True,
)
async def get3(
    computer_system_id: str,
    processor_id: str,
    memory_id: str,
    request: Request,
    response: Response,
) -> MemoryMetrics:
    s: Service = get_service(MemoryMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryMetrics, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
async def get4(
    computer_system_id: str, processor_id: str, request: Request, response: Response
) -> MemoryMetrics:
    s: Service = get_service(MemoryMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryMetrics, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/MemoryMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/MemoryMetrics",
    response_model_exclude_none=True,
)
async def get5(
    resource_block_id: str, memory_id: str, request: Request, response: Response
) -> MemoryMetrics:
    s: Service = get_service(MemoryMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryMetrics, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
async def get6(
    resource_block_id: str, processor_id: str, request: Request, response: Response
) -> MemoryMetrics:
    s: Service = get_service(MemoryMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryMetrics, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/MemoryMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/MemoryMetrics",
    response_model_exclude_none=True,
)
async def get7(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
) -> MemoryMetrics:
    s: Service = get_service(MemoryMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryMetrics, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
async def get8(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> MemoryMetrics:
    s: Service = get_service(MemoryMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryMetrics, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
async def get9(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
) -> MemoryMetrics:
    s: Service = get_service(MemoryMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryMetrics, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/MemoryMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/MemoryMetrics",
    response_model_exclude_none=True,
)
async def get10(
    resource_block_id: str, memory_id: str, request: Request, response: Response
) -> MemoryMetrics:
    s: Service = get_service(MemoryMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryMetrics, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
async def get11(
    resource_block_id: str, processor_id: str, request: Request, response: Response
) -> MemoryMetrics:
    s: Service = get_service(MemoryMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryMetrics, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/MemoryMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/MemoryMetrics",
    response_model_exclude_none=True,
)
async def get12(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
) -> MemoryMetrics:
    s: Service = get_service(MemoryMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryMetrics, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
async def get13(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> MemoryMetrics:
    s: Service = get_service(MemoryMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryMetrics, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/MemorySummary/MemoryMetrics",
    response_model_exclude_none=True,
)
async def get14(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
) -> MemoryMetrics:
    s: Service = get_service(MemoryMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryMetrics, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/MemoryMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/MemoryMetrics",
    response_model_exclude_none=True,
)
async def get15(
    chassis_id: str, memory_id: str, request: Request, response: Response
) -> MemoryMetrics:
    s: Service = get_service(MemoryMetrics, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    m = cast(MemoryMetrics, s.get(**b))
    set_link_header(m, response)
    return m
