from typing import Any, cast

from fastapi import APIRouter

from ..model.log_service import LogService
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Managers/{manager_id}/LogServices/{log_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(manager_id: str, log_service_id: str) -> LogService:
    s: Service = find_service(LogService)
    b: dict[str, Any] = {"manager_id": manager_id, "log_service_id": log_service_id}
    return cast(LogService, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/LogServices/{log_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(computer_system_id: str, log_service_id: str) -> LogService:
    s: Service = find_service(LogService)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
    }
    return cast(LogService, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(resource_block_id: str, computer_system_id: str, log_service_id: str) -> LogService:
    s: Service = find_service(LogService)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
    }
    return cast(LogService, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/LogServices/{log_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get4(resource_block_id: str, computer_system_id: str, log_service_id: str) -> LogService:
    s: Service = find_service(LogService)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "log_service_id": log_service_id,
    }
    return cast(LogService, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/LogServices/{log_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get5(chassis_id: str, log_service_id: str) -> LogService:
    s: Service = find_service(LogService)
    b: dict[str, Any] = {"chassis_id": chassis_id, "log_service_id": log_service_id}
    return cast(LogService, s.get(**b))


@router.get("/redfish/v1/JobService/Log", response_model_exclude_none=True)
@authenticate
async def get6() -> LogService:
    s: Service = find_service(LogService)
    b: dict[str, Any] = {}
    return cast(LogService, s.get(**b))


@router.get("/redfish/v1/TelemetryService/LogService", response_model_exclude_none=True)
@authenticate
async def get7() -> LogService:
    s: Service = find_service(LogService)
    b: dict[str, Any] = {}
    return cast(LogService, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/DeviceLog",
    response_model_exclude_none=True,
)
@authenticate
async def get8(computer_system_id: str, memory_id: str) -> LogService:
    s: Service = find_service(LogService)
    b: dict[str, Any] = {"computer_system_id": computer_system_id, "memory_id": memory_id}
    return cast(LogService, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/CXLLogicalDevices/{cxl_logical_device_id}/DeviceLog",
    response_model_exclude_none=True,
)
@authenticate
async def get9(chassis_id: str, pcie_device_id: str, cxl_logical_device_id: str) -> LogService:
    s: Service = find_service(LogService)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "cxl_logical_device_id": cxl_logical_device_id,
    }
    return cast(LogService, s.get(**b))
