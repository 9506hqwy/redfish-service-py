from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.log_entry import LogEntry, LogEntryOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete(
    "/redfish/v1/Managers/{manager_id}/LogServices/{log_service_id}/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    manager_id: str, log_service_id: str, log_entry_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "log_service_id": log_service_id,
        "log_entry_id": log_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Managers/{manager_id}/LogServices/{log_service_id}/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/LogServices/{log_service_id}/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
async def get1(
    manager_id: str, log_service_id: str, log_entry_id: str, request: Request, response: Response
) -> LogEntry:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "log_service_id": log_service_id,
        "log_entry_id": log_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(LogEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Managers/{manager_id}/LogServices/{log_service_id}/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    manager_id: str,
    log_service_id: str,
    log_entry_id: str,
    request: Request,
    response: Response,
    body: LogEntryOnUpdate,
) -> LogEntry:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "log_service_id": log_service_id,
        "log_entry_id": log_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LogEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    computer_system_id: str,
    log_service_id: str,
    log_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "log_entry_id": log_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str,
    log_service_id: str,
    log_entry_id: str,
    request: Request,
    response: Response,
) -> LogEntry:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "log_entry_id": log_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(LogEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    computer_system_id: str,
    log_service_id: str,
    log_entry_id: str,
    request: Request,
    response: Response,
    body: LogEntryOnUpdate,
) -> LogEntry:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "log_entry_id": log_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LogEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete3(
    resource_block_id: str,
    computer_system_id: str,
    log_service_id: str,
    log_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "log_entry_id": log_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str,
    computer_system_id: str,
    log_service_id: str,
    log_entry_id: str,
    request: Request,
    response: Response,
) -> LogEntry:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "log_entry_id": log_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(LogEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    resource_block_id: str,
    computer_system_id: str,
    log_service_id: str,
    log_entry_id: str,
    request: Request,
    response: Response,
    body: LogEntryOnUpdate,
) -> LogEntry:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "log_entry_id": log_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LogEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete4(
    resource_block_id: str,
    computer_system_id: str,
    log_service_id: str,
    log_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "log_entry_id": log_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str,
    computer_system_id: str,
    log_service_id: str,
    log_entry_id: str,
    request: Request,
    response: Response,
) -> LogEntry:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "log_entry_id": log_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(LogEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    resource_block_id: str,
    computer_system_id: str,
    log_service_id: str,
    log_entry_id: str,
    request: Request,
    response: Response,
    body: LogEntryOnUpdate,
) -> LogEntry:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
        "log_entry_id": log_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LogEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/LogServices/{log_service_id}/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete5(
    chassis_id: str, log_service_id: str, log_entry_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "log_service_id": log_service_id,
        "log_entry_id": log_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/LogServices/{log_service_id}/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/LogServices/{log_service_id}/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
async def get5(
    chassis_id: str, log_service_id: str, log_entry_id: str, request: Request, response: Response
) -> LogEntry:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "log_service_id": log_service_id,
        "log_entry_id": log_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(LogEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/LogServices/{log_service_id}/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    chassis_id: str,
    log_service_id: str,
    log_entry_id: str,
    request: Request,
    response: Response,
    body: LogEntryOnUpdate,
) -> LogEntry:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "log_service_id": log_service_id,
        "log_entry_id": log_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LogEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/JobService/Log/Entries/{log_entry_id}", response_model_exclude_none=True
)
@authenticate
async def delete6(log_entry_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {"log_entry_id": log_entry_id, "request": request, "response": response}
    return s.delete(**b)


@router.get("/redfish/v1/JobService/Log/Entries/{log_entry_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/JobService/Log/Entries/{log_entry_id}", response_model_exclude_none=True)
async def get6(log_entry_id: str, request: Request, response: Response) -> LogEntry:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {"log_entry_id": log_entry_id, "request": request, "response": response}
    m = cast(LogEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/JobService/Log/Entries/{log_entry_id}", response_model_exclude_none=True
)
@authenticate
async def patch6(
    log_entry_id: str, request: Request, response: Response, body: LogEntryOnUpdate
) -> LogEntry:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {
        "log_entry_id": log_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LogEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/TelemetryService/LogService/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete7(log_entry_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {"log_entry_id": log_entry_id, "request": request, "response": response}
    return s.delete(**b)


@router.get(
    "/redfish/v1/TelemetryService/LogService/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/TelemetryService/LogService/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
async def get7(log_entry_id: str, request: Request, response: Response) -> LogEntry:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {"log_entry_id": log_entry_id, "request": request, "response": response}
    m = cast(LogEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/TelemetryService/LogService/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch7(
    log_entry_id: str, request: Request, response: Response, body: LogEntryOnUpdate
) -> LogEntry:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {
        "log_entry_id": log_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LogEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/DeviceLog/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete8(
    computer_system_id: str,
    memory_id: str,
    log_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "log_entry_id": log_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/DeviceLog/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/DeviceLog/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
async def get8(
    computer_system_id: str,
    memory_id: str,
    log_entry_id: str,
    request: Request,
    response: Response,
) -> LogEntry:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "log_entry_id": log_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(LogEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/DeviceLog/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch8(
    computer_system_id: str,
    memory_id: str,
    log_entry_id: str,
    request: Request,
    response: Response,
    body: LogEntryOnUpdate,
) -> LogEntry:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "log_entry_id": log_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LogEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/DeviceLog/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete9(
    chassis_id: str,
    pcie_device_id: str,
    cxl_logical_device_id: str,
    log_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "cxl_logical_device_id": cxl_logical_device_id,
        "log_entry_id": log_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/DeviceLog/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/DeviceLog/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
async def get9(
    chassis_id: str,
    pcie_device_id: str,
    cxl_logical_device_id: str,
    log_entry_id: str,
    request: Request,
    response: Response,
) -> LogEntry:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "cxl_logical_device_id": cxl_logical_device_id,
        "log_entry_id": log_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(LogEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/DeviceLog/Entries/{log_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch9(
    chassis_id: str,
    pcie_device_id: str,
    cxl_logical_device_id: str,
    log_entry_id: str,
    request: Request,
    response: Response,
    body: LogEntryOnUpdate,
) -> LogEntry:
    s: Service = get_service(LogEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "cxl_logical_device_id": cxl_logical_device_id,
        "log_entry_id": log_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LogEntry, s.patch(**b))
