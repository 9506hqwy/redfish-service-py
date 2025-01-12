from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.environment_metrics import EnvironmentMetrics, EnvironmentMetricsOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get1(
    computer_system_id: str, processor_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str, memory_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get3(
    computer_system_id: str, storage_id: str, drive_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get4(
    computer_system_id: str, pcie_device_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    computer_system_id: str,
    pcie_device_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{controller_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{controller_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get5(
    computer_system_id: str,
    storage_id: str,
    controller_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{controller_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    computer_system_id: str,
    storage_id: str,
    controller_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get6(
    resource_block_id: str, processor_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    resource_block_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get7(
    resource_block_id: str, memory_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch7(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get8(
    resource_block_id: str, storage_id: str, drive_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch8(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get9(
    resource_block_id: str, drive_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch9(
    resource_block_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get10(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch10(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get11(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch11(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get12(
    resource_block_id: str,
    computer_system_id: str,
    pcie_device_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch12(
    resource_block_id: str,
    computer_system_id: str,
    pcie_device_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get13(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch13(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{controller_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{controller_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get14(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    controller_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{controller_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch14(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    controller_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{controller_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{controller_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get15(
    resource_block_id: str,
    storage_id: str,
    controller_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{controller_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch15(
    resource_block_id: str,
    storage_id: str,
    controller_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get16(
    resource_block_id: str, processor_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch16(
    resource_block_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get17(
    resource_block_id: str, memory_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch17(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get18(
    resource_block_id: str, storage_id: str, drive_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch18(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{controller_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{controller_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get19(
    resource_block_id: str,
    storage_id: str,
    controller_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{controller_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch19(
    resource_block_id: str,
    storage_id: str,
    controller_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get20(
    resource_block_id: str, drive_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch20(
    resource_block_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get21(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch21(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get22(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch22(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get23(
    resource_block_id: str,
    computer_system_id: str,
    pcie_device_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch23(
    resource_block_id: str,
    computer_system_id: str,
    pcie_device_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get24(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch24(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{controller_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{controller_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get25(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    controller_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{controller_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch25(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    controller_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get26(
    chassis_id: str, memory_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch26(
    chassis_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get27(
    chassis_id: str, drive_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch27(
    chassis_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/EnvironmentMetrics", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/EnvironmentMetrics", response_model_exclude_none=True
)
async def get28(chassis_id: str, request: Request, response: Response) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/EnvironmentMetrics", response_model_exclude_none=True
)
@authenticate
async def patch28(
    chassis_id: str, request: Request, response: Response, body: EnvironmentMetricsOnUpdate
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get29(
    chassis_id: str, pcie_device_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch29(
    chassis_id: str,
    pcie_device_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get30(
    chassis_id: str, network_adapter_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch30(
    chassis_id: str,
    network_adapter_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/MediaControllers/{media_controller_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/MediaControllers/{media_controller_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get31(
    chassis_id: str, media_controller_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "media_controller_id": media_controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/MediaControllers/{media_controller_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch31(
    chassis_id: str,
    media_controller_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "media_controller_id": media_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Facilities/{facility_id}/EnvironmentMetrics", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Facilities/{facility_id}/EnvironmentMetrics", response_model_exclude_none=True
)
async def get32(facility_id: str, request: Request, response: Response) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {"facility_id": facility_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Facilities/{facility_id}/EnvironmentMetrics", response_model_exclude_none=True
)
@authenticate
async def patch32(
    facility_id: str, request: Request, response: Response, body: EnvironmentMetricsOnUpdate
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "facility_id": facility_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Facilities/{facility_id}/AmbientMetrics", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Facilities/{facility_id}/AmbientMetrics", response_model_exclude_none=True
)
async def get33(facility_id: str, request: Request, response: Response) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {"facility_id": facility_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Facilities/{facility_id}/AmbientMetrics", response_model_exclude_none=True
)
@authenticate
async def patch33(
    facility_id: str, request: Request, response: Response, body: EnvironmentMetricsOnUpdate
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "facility_id": facility_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get34(
    fabric_id: str, switch_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch34(
    fabric_id: str,
    switch_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/Controllers/{controller_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/Controllers/{controller_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get35(
    storage_id: str, controller_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Storage/{storage_id}/Controllers/{controller_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch35(
    storage_id: str,
    controller_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get36(
    fabric_id: str, switch_id: str, port_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch36(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get37(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch37(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get38(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch38(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get39(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch39(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get40(
    computer_system_id: str, controller_id: str, port_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch40(
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get41(
    computer_system_id: str, controller_id: str, port_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch41(
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get42(
    computer_system_id: str, processor_id: str, port_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch42(
    computer_system_id: str,
    processor_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/MediaControllers/{media_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/MediaControllers/{media_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get43(
    chassis_id: str, media_controller_id: str, port_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "media_controller_id": media_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/MediaControllers/{media_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch43(
    chassis_id: str,
    media_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "media_controller_id": media_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get44(
    chassis_id: str, fabric_adapter_id: str, port_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch44(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get45(
    chassis_id: str, network_adapter_id: str, port_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch45(
    chassis_id: str,
    network_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get46(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch46(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get47(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch47(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get48(
    resource_block_id: str, processor_id: str, port_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch48(
    resource_block_id: str,
    processor_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get49(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch49(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get50(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch50(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get51(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch51(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get52(
    resource_block_id: str,
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch52(
    resource_block_id: str,
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get53(
    resource_block_id: str,
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch53(
    resource_block_id: str,
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get54(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch54(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get55(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch55(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get56(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch56(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get57(
    resource_block_id: str, processor_id: str, port_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch57(
    resource_block_id: str,
    processor_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get58(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch58(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get59(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch59(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get60(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch60(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get61(
    resource_block_id: str,
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch61(
    resource_block_id: str,
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get62(
    resource_block_id: str,
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch62(
    resource_block_id: str,
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get63(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch63(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get64(
    storage_id: str, storage_controller_id: str, port_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch64(
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get65(
    storage_id: str, storage_controller_id: str, port_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch65(
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/USBPorts/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/USBPorts/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get66(
    manager_id: str, port_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Managers/{manager_id}/USBPorts/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch66(
    manager_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/DedicatedNetworkPorts/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/DedicatedNetworkPorts/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get67(
    manager_id: str, port_id: str, request: Request, response: Response
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/Managers/{manager_id}/DedicatedNetworkPorts/{port_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch67(
    manager_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: EnvironmentMetricsOnUpdate,
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get68(cooling_unit_id: str, request: Request, response: Response) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch68(
    cooling_unit_id: str, request: Request, response: Response, body: EnvironmentMetricsOnUpdate
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get69(cooling_unit_id: str, request: Request, response: Response) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch69(
    cooling_unit_id: str, request: Request, response: Response, body: EnvironmentMetricsOnUpdate
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
async def get70(cooling_unit_id: str, request: Request, response: Response) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/EnvironmentMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def patch70(
    cooling_unit_id: str, request: Request, response: Response, body: EnvironmentMetricsOnUpdate
) -> EnvironmentMetrics:
    s: Service = get_service(EnvironmentMetrics, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EnvironmentMetrics, s.patch(**b))
