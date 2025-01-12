from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.assembly import Assembly, AssemblyOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/Assembly", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis/{chassis_id}/Assembly", response_model_exclude_none=True)
async def get1(chassis_id: str, request: Request, response: Response) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}
    return cast(Assembly, s.get(**b))


@router.patch("/redfish/v1/Chassis/{chassis_id}/Assembly", response_model_exclude_none=True)
@authenticate
async def patch1(
    chassis_id: str, request: Request, response: Response, body: AssemblyOnUpdate
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str, storage_id: str, drive_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/Assembly", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/Assembly", response_model_exclude_none=True
)
async def get3(chassis_id: str, drive_id: str, request: Request, response: Response) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/Assembly", response_model_exclude_none=True
)
@authenticate
async def patch3(
    chassis_id: str, drive_id: str, request: Request, response: Response, body: AssemblyOnUpdate
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str, storage_id: str, drive_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
async def get5(
    resource_block_id: str, drive_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    resource_block_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
async def get6(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
async def get7(
    resource_block_id: str, storage_id: str, drive_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch7(
    resource_block_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
async def get8(
    resource_block_id: str, drive_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch8(
    resource_block_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
async def get9(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch9(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    drive_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Assembly",
    response_model_exclude_none=True,
)
async def get10(
    computer_system_id: str, memory_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch10(
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Assembly",
    response_model_exclude_none=True,
)
async def get11(
    resource_block_id: str, memory_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch11(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Assembly",
    response_model_exclude_none=True,
)
async def get12(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch12(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Assembly",
    response_model_exclude_none=True,
)
async def get13(
    resource_block_id: str, memory_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch13(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Assembly",
    response_model_exclude_none=True,
)
async def get14(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch14(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Assembly",
    response_model_exclude_none=True,
)
async def get15(
    chassis_id: str, network_adapter_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch15(
    chassis_id: str,
    network_adapter_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/Assembly",
    response_model_exclude_none=True,
)
async def get16(
    chassis_id: str, pcie_device_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch16(
    chassis_id: str,
    pcie_device_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/Assembly",
    response_model_exclude_none=True,
)
async def get17(
    computer_system_id: str, pcie_device_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch17(
    computer_system_id: str,
    pcie_device_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Power/PowerSupplies/{power_supply_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/Power/PowerSupplies/{power_supply_id}/Assembly",
    response_model_exclude_none=True,
)
async def get18(
    chassis_id: str, power_supply_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "power_supply_id": power_supply_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/Power/PowerSupplies/{power_supply_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch18(
    chassis_id: str,
    power_supply_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "power_supply_id": power_supply_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
async def get19(
    computer_system_id: str, processor_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch19(
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
async def get20(
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch20(
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
async def get21(
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch21(
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
async def get22(
    resource_block_id: str, processor_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch22(
    resource_block_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
async def get23(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch23(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
async def get24(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch24(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
async def get25(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch25(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
async def get26(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch26(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
async def get27(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch27(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
async def get28(
    resource_block_id: str, processor_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch28(
    resource_block_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
async def get29(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch29(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
async def get30(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch30(
    resource_block_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
async def get31(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch31(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
async def get32(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch32(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
async def get33(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch33(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
async def get34(
    chassis_id: str,
    network_adapter_id: str,
    processor_id: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch34(
    chassis_id: str,
    network_adapter_id: str,
    processor_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
async def get35(
    chassis_id: str,
    network_adapter_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch35(
    chassis_id: str,
    network_adapter_id: str,
    processor_id: str,
    processor_id2: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
async def get36(
    chassis_id: str,
    network_adapter_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch36(
    chassis_id: str,
    network_adapter_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
async def get37(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch37(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
async def get38(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch38(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
async def get39(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch39(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
async def get40(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch40(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
async def get41(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch41(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
async def get42(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch42(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
async def get43(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch43(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
async def get44(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch44(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
async def get45(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch45(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
async def get46(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch46(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
async def get47(
    storage_id: str, storage_controller_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch47(
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
async def get48(
    storage_id: str, storage_controller_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch48(
    storage_id: str,
    storage_controller_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Thermal/Fans/{fan_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/Thermal/Fans/{fan_id}/Assembly",
    response_model_exclude_none=True,
)
async def get49(chassis_id: str, fan_id: str, request: Request, response: Response) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fan_id": fan_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/Thermal/Fans/{fan_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch49(
    chassis_id: str, fan_id: str, request: Request, response: Response, body: AssemblyOnUpdate
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fan_id": fan_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Fans/{fan_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Fans/{fan_id}/Assembly",
    response_model_exclude_none=True,
)
async def get50(chassis_id: str, fan_id: str, request: Request, response: Response) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fan_id": fan_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Fans/{fan_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch50(
    chassis_id: str, fan_id: str, request: Request, response: Response, body: AssemblyOnUpdate
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fan_id": fan_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}/Assembly",
    response_model_exclude_none=True,
)
async def get51(
    chassis_id: str, power_supply_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "power_supply_id": power_supply_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch51(
    chassis_id: str,
    power_supply_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "power_supply_id": power_supply_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/PowerSupplies/{power_supply_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/PowerSupplies/{power_supply_id}/Assembly",
    response_model_exclude_none=True,
)
async def get52(
    power_distribution_id: str, power_supply_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "power_supply_id": power_supply_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/PowerSupplies/{power_supply_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch52(
    power_distribution_id: str,
    power_supply_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "power_supply_id": power_supply_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/Batteries/{battery_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/Batteries/{battery_id}/Assembly",
    response_model_exclude_none=True,
)
async def get53(
    chassis_id: str, battery_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "battery_id": battery_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/Batteries/{battery_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch53(
    chassis_id: str, battery_id: str, request: Request, response: Response, body: AssemblyOnUpdate
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "battery_id": battery_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Heaters/{header_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Heaters/{header_id}/Assembly",
    response_model_exclude_none=True,
)
async def get54(chassis_id: str, header_id: str, request: Request, response: Response) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "header_id": header_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Heaters/{header_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch54(
    chassis_id: str, header_id: str, request: Request, response: Response, body: AssemblyOnUpdate
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "header_id": header_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Assembly",
    response_model_exclude_none=True,
)
async def get55(cooling_unit_id: str, request: Request, response: Response) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch55(
    cooling_unit_id: str, request: Request, response: Response, body: AssemblyOnUpdate
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Assembly",
    response_model_exclude_none=True,
)
async def get56(cooling_unit_id: str, request: Request, response: Response) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch56(
    cooling_unit_id: str, request: Request, response: Response, body: AssemblyOnUpdate
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Assembly",
    response_model_exclude_none=True,
)
async def get57(cooling_unit_id: str, request: Request, response: Response) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch57(
    cooling_unit_id: str, request: Request, response: Response, body: AssemblyOnUpdate
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Reservoirs/{reservoir_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Reservoirs/{reservoir_id}/Assembly",
    response_model_exclude_none=True,
)
async def get58(
    cooling_unit_id: str, reservoir_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Reservoirs/{reservoir_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch58(
    cooling_unit_id: str,
    reservoir_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Reservoirs/{reservoir_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Reservoirs/{reservoir_id}/Assembly",
    response_model_exclude_none=True,
)
async def get59(
    cooling_unit_id: str, reservoir_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Reservoirs/{reservoir_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch59(
    cooling_unit_id: str,
    reservoir_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Reservoirs/{reservoir_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Reservoirs/{reservoir_id}/Assembly",
    response_model_exclude_none=True,
)
async def get60(
    cooling_unit_id: str, reservoir_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Reservoirs/{reservoir_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch60(
    cooling_unit_id: str,
    reservoir_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps/{pump_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps/{pump_id}/Assembly",
    response_model_exclude_none=True,
)
async def get61(
    cooling_unit_id: str, pump_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps/{pump_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch61(
    cooling_unit_id: str,
    pump_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps/{pump_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps/{pump_id}/Assembly",
    response_model_exclude_none=True,
)
async def get62(
    cooling_unit_id: str, pump_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps/{pump_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch62(
    cooling_unit_id: str,
    pump_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps/{pump_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps/{pump_id}/Assembly",
    response_model_exclude_none=True,
)
async def get63(
    cooling_unit_id: str, pump_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps/{pump_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch63(
    cooling_unit_id: str,
    pump_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
async def get64(
    cooling_unit_id: str, filter_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch64(
    cooling_unit_id: str,
    filter_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
async def get65(
    cooling_unit_id: str, reservoir_id: str, filter_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch65(
    cooling_unit_id: str,
    reservoir_id: str,
    filter_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
async def get66(
    cooling_unit_id: str, pump_id: str, filter_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch66(
    cooling_unit_id: str,
    pump_id: str,
    filter_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
async def get67(
    cooling_unit_id: str, filter_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch67(
    cooling_unit_id: str,
    filter_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
async def get68(
    cooling_unit_id: str, reservoir_id: str, filter_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch68(
    cooling_unit_id: str,
    reservoir_id: str,
    filter_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
async def get69(
    cooling_unit_id: str, pump_id: str, filter_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch69(
    cooling_unit_id: str,
    pump_id: str,
    filter_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
async def get70(
    cooling_unit_id: str, filter_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch70(
    cooling_unit_id: str,
    filter_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
async def get71(
    cooling_unit_id: str, reservoir_id: str, filter_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch71(
    cooling_unit_id: str,
    reservoir_id: str,
    filter_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
async def get72(
    cooling_unit_id: str, pump_id: str, filter_id: str, request: Request, response: Response
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
    }
    return cast(Assembly, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def patch72(
    cooling_unit_id: str,
    pump_id: str,
    filter_id: str,
    request: Request,
    response: Response,
    body: AssemblyOnUpdate,
) -> Assembly:
    s: Service = get_service(Assembly, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "filter_id": filter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Assembly, s.patch(**b))
