from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.port_collection import PortCollection
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports", response_model_exclude_none=True
)
@authenticate
async def get1(fabric_id: str, switch_id: str) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {"fabric_id": fabric_id, "switch_id": switch_id}
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    computer_system_id: str, storage_id: str, storage_controller_id: str
) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get3(
    computer_system_id: str, storage_id: str, storage_controller_id: str
) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get4(computer_system_id: str, fabric_adapter_id: str) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get5(computer_system_id: str, network_interface_id: str) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get6(computer_system_id: str, controller_id: str) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {"computer_system_id": computer_system_id, "controller_id": controller_id}
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get7(computer_system_id: str, controller_id: str) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {"computer_system_id": computer_system_id, "controller_id": controller_id}
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get8(computer_system_id: str, processor_id: str) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {"computer_system_id": computer_system_id, "processor_id": processor_id}
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/MediaControllers/{media_controller_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get9(chassis_id: str, media_controller_id: str) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id, "media_controller_id": media_controller_id}
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get10(chassis_id: str, fabric_adapter_id: str) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id, "fabric_adapter_id": fabric_adapter_id}
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get11(chassis_id: str, network_adapter_id: str) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id, "network_adapter_id": network_adapter_id}
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get12(
    resource_block_id: str, storage_id: str, storage_controller_id: str
) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get13(
    resource_block_id: str, storage_id: str, storage_controller_id: str
) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get14(resource_block_id: str, network_interface_id: str) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "network_interface_id": network_interface_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get15(resource_block_id: str, processor_id: str) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {"resource_block_id": resource_block_id, "processor_id": processor_id}
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get16(
    resource_block_id: str, computer_system_id: str, storage_id: str, storage_controller_id: str
) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get17(
    resource_block_id: str, computer_system_id: str, storage_id: str, storage_controller_id: str
) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get18(
    resource_block_id: str, computer_system_id: str, fabric_adapter_id: str
) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get19(
    resource_block_id: str, computer_system_id: str, network_interface_id: str
) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get20(
    resource_block_id: str, computer_system_id: str, controller_id: str
) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get21(
    resource_block_id: str, computer_system_id: str, controller_id: str
) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get22(
    resource_block_id: str, computer_system_id: str, processor_id: str
) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get23(
    resource_block_id: str, storage_id: str, storage_controller_id: str
) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get24(
    resource_block_id: str, storage_id: str, storage_controller_id: str
) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get25(resource_block_id: str, network_interface_id: str) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "network_interface_id": network_interface_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get26(resource_block_id: str, processor_id: str) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {"resource_block_id": resource_block_id, "processor_id": processor_id}
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get27(
    resource_block_id: str, computer_system_id: str, storage_id: str, storage_controller_id: str
) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get28(
    resource_block_id: str, computer_system_id: str, storage_id: str, storage_controller_id: str
) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get29(
    resource_block_id: str, computer_system_id: str, fabric_adapter_id: str
) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get30(
    resource_block_id: str, computer_system_id: str, network_interface_id: str
) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get31(
    resource_block_id: str, computer_system_id: str, controller_id: str
) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get32(
    resource_block_id: str, computer_system_id: str, controller_id: str
) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get33(
    resource_block_id: str, computer_system_id: str, processor_id: str
) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
    }
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get34(storage_id: str, storage_controller_id: str) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {"storage_id": storage_id, "storage_controller_id": storage_controller_id}
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports",
    response_model_exclude_none=True,
)
@authenticate
async def get35(storage_id: str, storage_controller_id: str) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {"storage_id": storage_id, "storage_controller_id": storage_controller_id}
    return cast(PortCollection, s.get(**b))


@router.get("/redfish/v1/Managers/{manager_id}/USBPorts", response_model_exclude_none=True)
@authenticate
async def get36(manager_id: str) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {"manager_id": manager_id}
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/DedicatedNetworkPorts", response_model_exclude_none=True
)
@authenticate
async def get37(manager_id: str) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {"manager_id": manager_id}
    return cast(PortCollection, s.get(**b))


@router.get(
    "/redfish/v1/Managers/{manager_id}/SharedNetworkPorts", response_model_exclude_none=True
)
@authenticate
async def get38(manager_id: str) -> PortCollection:
    s: Service = find_service(PortCollection)
    b: dict[str, Any] = {"manager_id": manager_id}
    return cast(PortCollection, s.get(**b))
