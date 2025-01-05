from typing import Any, cast

from fastapi import APIRouter

from ..model.assembly import Assembly
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/Assembly", response_model_exclude_none=True)
@authenticate
async def get1(chassis_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"chassis_id": chassis_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get2(computer_system_id: str, storage_id: str, drive_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Drives/{drive_id}/Assembly", response_model_exclude_none=True
)
@authenticate
async def get3(chassis_id: str, drive_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"chassis_id": chassis_id, "drive_id": drive_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get4(resource_block_id: str, storage_id: str, drive_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get5(resource_block_id: str, drive_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"resource_block_id": resource_block_id, "drive_id": drive_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get6(
    resource_block_id: str, computer_system_id: str, storage_id: str, drive_id: str
) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get7(resource_block_id: str, storage_id: str, drive_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get8(resource_block_id: str, drive_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"resource_block_id": resource_block_id, "drive_id": drive_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Drives/{drive_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get9(
    resource_block_id: str, computer_system_id: str, storage_id: str, drive_id: str
) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "drive_id": drive_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get10(computer_system_id: str, memory_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"computer_system_id": computer_system_id, "memory_id": memory_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get11(resource_block_id: str, memory_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"resource_block_id": resource_block_id, "memory_id": memory_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get12(resource_block_id: str, computer_system_id: str, memory_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get13(resource_block_id: str, memory_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"resource_block_id": resource_block_id, "memory_id": memory_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get14(resource_block_id: str, computer_system_id: str, memory_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get15(chassis_id: str, network_adapter_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"chassis_id": chassis_id, "network_adapter_id": network_adapter_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PCIeDevices/{pcie_device_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get16(chassis_id: str, pcie_device_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"chassis_id": chassis_id, "pcie_device_id": pcie_device_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/PCIeDevices/{pcie_device_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get17(computer_system_id: str, pcie_device_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "pcie_device_id": pcie_device_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Power/PowerSupplies/{power_supply_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get18(chassis_id: str, power_supply_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"chassis_id": chassis_id, "power_supply_id": power_supply_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get19(computer_system_id: str, processor_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"computer_system_id": computer_system_id, "processor_id": processor_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get20(computer_system_id: str, processor_id: str, processor_id2: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get21(
    computer_system_id: str, processor_id: str, processor_id2: str, processor_id3: str
) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get22(resource_block_id: str, processor_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"resource_block_id": resource_block_id, "processor_id": processor_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get23(resource_block_id: str, processor_id: str, processor_id2: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get24(
    resource_block_id: str, processor_id: str, processor_id2: str, processor_id3: str
) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get25(resource_block_id: str, computer_system_id: str, processor_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get26(
    resource_block_id: str, computer_system_id: str, processor_id: str, processor_id2: str
) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get27(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get28(resource_block_id: str, processor_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"resource_block_id": resource_block_id, "processor_id": processor_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get29(resource_block_id: str, processor_id: str, processor_id2: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get30(
    resource_block_id: str, processor_id: str, processor_id2: str, processor_id3: str
) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get31(resource_block_id: str, computer_system_id: str, processor_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get32(
    resource_block_id: str, computer_system_id: str, processor_id: str, processor_id2: str
) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get33(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get34(chassis_id: str, network_adapter_id: str, processor_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "processor_id": processor_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get35(
    chassis_id: str, network_adapter_id: str, processor_id: str, processor_id2: str
) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Processors/{processor_id}/SubProcessors/{processor_id2}/SubProcessors/{processor_id3}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get36(
    chassis_id: str,
    network_adapter_id: str,
    processor_id: str,
    processor_id2: str,
    processor_id3: str,
) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "processor_id": processor_id,
        "processor_id2": processor_id2,
        "processor_id3": processor_id3,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get37(computer_system_id: str, storage_id: str, storage_controller_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get38(computer_system_id: str, storage_id: str, storage_controller_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get39(resource_block_id: str, storage_id: str, storage_controller_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get40(resource_block_id: str, storage_id: str, storage_controller_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get41(
    resource_block_id: str, computer_system_id: str, storage_id: str, storage_controller_id: str
) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get42(
    resource_block_id: str, computer_system_id: str, storage_id: str, storage_controller_id: str
) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get43(resource_block_id: str, storage_id: str, storage_controller_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get44(resource_block_id: str, storage_id: str, storage_controller_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get45(
    resource_block_id: str, computer_system_id: str, storage_id: str, storage_controller_id: str
) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get46(
    resource_block_id: str, computer_system_id: str, storage_id: str, storage_controller_id: str
) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get47(storage_id: str, storage_controller_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"storage_id": storage_id, "storage_controller_id": storage_controller_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get48(storage_id: str, storage_controller_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"storage_id": storage_id, "storage_controller_id": storage_controller_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Thermal/Fans/{fan_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get49(chassis_id: str, fan_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"chassis_id": chassis_id, "fan_id": fan_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Fans/{fan_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get50(chassis_id: str, fan_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"chassis_id": chassis_id, "fan_id": fan_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get51(chassis_id: str, power_supply_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"chassis_id": chassis_id, "power_supply_id": power_supply_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/PowerSupplies/{power_supply_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get52(power_distribution_id: str, power_supply_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "power_supply_id": power_supply_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/Batteries/{battery_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get53(chassis_id: str, battery_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"chassis_id": chassis_id, "battery_id": battery_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Heaters/{header_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get54(chassis_id: str, header_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"chassis_id": chassis_id, "header_id": header_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get55(cooling_unit_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get56(cooling_unit_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get57(cooling_unit_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Reservoirs/{reservoir_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get58(cooling_unit_id: str, reservoir_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id, "reservoir_id": reservoir_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Reservoirs/{reservoir_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get59(cooling_unit_id: str, reservoir_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id, "reservoir_id": reservoir_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Reservoirs/{reservoir_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get60(cooling_unit_id: str, reservoir_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id, "reservoir_id": reservoir_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps/{pump_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get61(cooling_unit_id: str, pump_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id, "pump_id": pump_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps/{pump_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get62(cooling_unit_id: str, pump_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id, "pump_id": pump_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps/{pump_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get63(cooling_unit_id: str, pump_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id, "pump_id": pump_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get64(cooling_unit_id: str, filter_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id, "filter_id": filter_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get65(cooling_unit_id: str, reservoir_id: str, filter_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "filter_id": filter_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get66(cooling_unit_id: str, pump_id: str, filter_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "filter_id": filter_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get67(cooling_unit_id: str, filter_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id, "filter_id": filter_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get68(cooling_unit_id: str, reservoir_id: str, filter_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "filter_id": filter_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get69(cooling_unit_id: str, pump_id: str, filter_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "filter_id": filter_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get70(cooling_unit_id: str, filter_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id, "filter_id": filter_id}
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Reservoirs/{reservoir_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get71(cooling_unit_id: str, reservoir_id: str, filter_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "reservoir_id": reservoir_id,
        "filter_id": filter_id,
    }
    return cast(Assembly, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Pumps/{pump_id}/Filters/{filter_id}/Assembly",
    response_model_exclude_none=True,
)
@authenticate
async def get72(cooling_unit_id: str, pump_id: str, filter_id: str) -> Assembly:
    s: Service = find_service(Assembly)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "pump_id": pump_id,
        "filter_id": filter_id,
    }
    return cast(Assembly, s.get(**b))
