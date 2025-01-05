from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.vcat_entry import VcatEntry
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(fabric_id: str, switch_id: str, port_id: str, vcat_entry_id: str) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    system_id: str, fabric_adapter_id: str, port_id: str, vcat_entry_id: str
) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(system_id: str, fabric_adapter_id: str, vcat_entry_id: str) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get4(system_id: str, fabric_adapter_id: str, vcat_entry_id: str) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get5(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get6(
    resource_block_id: str, system_id: str, fabric_adapter_id: str, vcat_entry_id: str
) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get7(
    resource_block_id: str, system_id: str, fabric_adapter_id: str, vcat_entry_id: str
) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get8(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get9(
    resource_block_id: str, system_id: str, fabric_adapter_id: str, vcat_entry_id: str
) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get10(
    resource_block_id: str, system_id: str, fabric_adapter_id: str, vcat_entry_id: str
) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get11(
    chassis_id: str, fabric_adapter_id: str, port_id: str, vcat_entry_id: str
) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get12(chassis_id: str, fabric_adapter_id: str, vcat_entry_id: str) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get13(chassis_id: str, fabric_adapter_id: str, vcat_entry_id: str) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get14(fabric_id: str, switch_id: str, port_id: str, vcat_entry_id: str) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get15(
    system_id: str, fabric_adapter_id: str, port_id: str, vcat_entry_id: str
) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get16(system_id: str, fabric_adapter_id: str, vcat_entry_id: str) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get17(system_id: str, fabric_adapter_id: str, vcat_entry_id: str) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get18(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get19(
    resource_block_id: str, system_id: str, fabric_adapter_id: str, vcat_entry_id: str
) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get20(
    resource_block_id: str, system_id: str, fabric_adapter_id: str, vcat_entry_id: str
) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get21(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get22(
    resource_block_id: str, system_id: str, fabric_adapter_id: str, vcat_entry_id: str
) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get23(
    resource_block_id: str, system_id: str, fabric_adapter_id: str, vcat_entry_id: str
) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get24(
    chassis_id: str, fabric_adapter_id: str, port_id: str, vcat_entry_id: str
) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get25(chassis_id: str, fabric_adapter_id: str, vcat_entry_id: str) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get26(chassis_id: str, fabric_adapter_id: str, vcat_entry_id: str) -> VcatEntry:
    s: Service = find_service(VcatEntry)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
    }
    return cast(VcatEntry, s.get(**b))
