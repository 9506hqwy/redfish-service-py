from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.log_entry import LogEntry, LogEntryOnCreate
from ..model.log_entry_collection import LogEntryCollection
from ..service import Service, ServiceCollection, find_service, find_service_collection

router = APIRouter()


@router.get(
    "/redfish/v1/Managers/{manager_id}/LogServices/{log_service_id}/Entries",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/LogServices/{log_service_id}/Entries",
    response_model_exclude_none=True,
)
async def get1(
    manager_id: str, log_service_id: str, request: Request, response: Response
) -> LogEntryCollection:
    s: Service = find_service(LogEntryCollection)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LogEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/LogServices/{log_service_id}/Entries",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Managers/{manager_id}/LogServices/{log_service_id}/Entries/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post1(
    manager_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: LogEntryOnCreate,
) -> LogEntry:
    s: ServiceCollection = find_service_collection(LogEntryCollection)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LogEntry, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str, log_service_id: str, request: Request, response: Response
) -> LogEntryCollection:
    s: Service = find_service(LogEntryCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LogEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post2(
    computer_system_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: LogEntryOnCreate,
) -> LogEntry:
    s: ServiceCollection = find_service_collection(LogEntryCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LogEntry, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str,
    computer_system_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
) -> LogEntryCollection:
    s: Service = find_service(LogEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LogEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post3(
    resource_block_id: str,
    computer_system_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: LogEntryOnCreate,
) -> LogEntry:
    s: ServiceCollection = find_service_collection(LogEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LogEntry, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str,
    computer_system_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
) -> LogEntryCollection:
    s: Service = find_service(LogEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LogEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post4(
    resource_block_id: str,
    computer_system_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: LogEntryOnCreate,
) -> LogEntry:
    s: ServiceCollection = find_service_collection(LogEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LogEntry, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/LogServices/{log_service_id}/Entries",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/LogServices/{log_service_id}/Entries",
    response_model_exclude_none=True,
)
async def get5(
    chassis_id: str, log_service_id: str, request: Request, response: Response
) -> LogEntryCollection:
    s: Service = find_service(LogEntryCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LogEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/LogServices/{log_service_id}/Entries",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/LogServices/{log_service_id}/Entries/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post5(
    chassis_id: str,
    log_service_id: str,
    request: Request,
    response: Response,
    body: LogEntryOnCreate,
) -> LogEntry:
    s: ServiceCollection = find_service_collection(LogEntryCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "log_service_id": log_service_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LogEntry, s.post(**b))


@router.get("/redfish/v1/JobService/Log/Entries", response_model_exclude_none=True)
@router.head("/redfish/v1/JobService/Log/Entries", response_model_exclude_none=True)
async def get6(request: Request, response: Response) -> LogEntryCollection:
    s: Service = find_service(LogEntryCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(LogEntryCollection, s.get(**b))


@router.post("/redfish/v1/JobService/Log/Entries", response_model_exclude_none=True)
@router.post("/redfish/v1/JobService/Log/Entries/Members", response_model_exclude_none=True)
@authenticate
async def post6(request: Request, response: Response, body: LogEntryOnCreate) -> LogEntry:
    s: ServiceCollection = find_service_collection(LogEntryCollection)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(LogEntry, s.post(**b))


@router.get("/redfish/v1/TelemetryService/LogService/Entries", response_model_exclude_none=True)
@router.head("/redfish/v1/TelemetryService/LogService/Entries", response_model_exclude_none=True)
async def get7(request: Request, response: Response) -> LogEntryCollection:
    s: Service = find_service(LogEntryCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(LogEntryCollection, s.get(**b))


@router.post("/redfish/v1/TelemetryService/LogService/Entries", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/TelemetryService/LogService/Entries/Members", response_model_exclude_none=True
)
@authenticate
async def post7(request: Request, response: Response, body: LogEntryOnCreate) -> LogEntry:
    s: ServiceCollection = find_service_collection(LogEntryCollection)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(LogEntry, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/DeviceLog/Entries",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/DeviceLog/Entries",
    response_model_exclude_none=True,
)
async def get8(
    computer_system_id: str, memory_id: str, request: Request, response: Response
) -> LogEntryCollection:
    s: Service = find_service(LogEntryCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LogEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/DeviceLog/Entries",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/DeviceLog/Entries/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post8(
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: LogEntryOnCreate,
) -> LogEntry:
    s: ServiceCollection = find_service_collection(LogEntryCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LogEntry, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/DeviceLog/Entries",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/DeviceLog/Entries",
    response_model_exclude_none=True,
)
async def get9(
    chassis_id: str,
    pcie_device_id: str,
    cxl_logical_device_id: str,
    request: Request,
    response: Response,
) -> LogEntryCollection:
    s: Service = find_service(LogEntryCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "cxl_logical_device_id": cxl_logical_device_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LogEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/DeviceLog/Entries",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/DeviceLog/Entries/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post9(
    chassis_id: str,
    pcie_device_id: str,
    cxl_logical_device_id: str,
    request: Request,
    response: Response,
    body: LogEntryOnCreate,
) -> LogEntry:
    s: ServiceCollection = find_service_collection(LogEntryCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "cxl_logical_device_id": cxl_logical_device_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LogEntry, s.post(**b))
