from typing import Any, cast

from fastapi import APIRouter

from ..model.fabric_adapter import FabricAdapter
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(computer_system_id: str, fabric_adapter_id: str) -> FabricAdapter:
    s: Service = find_service(FabricAdapter)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
    }
    return cast(FabricAdapter, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    resource_block_id: str, computer_system_id: str, fabric_adapter_id: str
) -> FabricAdapter:
    s: Service = find_service(FabricAdapter)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
    }
    return cast(FabricAdapter, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(
    resource_block_id: str, computer_system_id: str, fabric_adapter_id: str
) -> FabricAdapter:
    s: Service = find_service(FabricAdapter)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
    }
    return cast(FabricAdapter, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get4(chassis_id: str, fabric_adapter_id: str) -> FabricAdapter:
    s: Service = find_service(FabricAdapter)
    b: dict[str, Any] = {"chassis_id": chassis_id, "fabric_adapter_id": fabric_adapter_id}
    return cast(FabricAdapter, s.get(**b))
