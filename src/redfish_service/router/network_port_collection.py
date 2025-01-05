from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.network_port_collection import NetworkPortCollection
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkPorts",
    response_model_exclude_none=True,
)
@authenticate
async def get1(chassis_id: str, network_adapter_id: str) -> NetworkPortCollection:
    s: Service = find_service(NetworkPortCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id, "network_adapter_id": network_adapter_id}
    return cast(NetworkPortCollection, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkPorts",
    response_model_exclude_none=True,
)
@authenticate
async def get2(computer_system_id: str, network_interface_id: str) -> NetworkPortCollection:
    s: Service = find_service(NetworkPortCollection)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
    }
    return cast(NetworkPortCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkPorts",
    response_model_exclude_none=True,
)
@authenticate
async def get3(resource_block_id: str, network_interface_id: str) -> NetworkPortCollection:
    s: Service = find_service(NetworkPortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "network_interface_id": network_interface_id,
    }
    return cast(NetworkPortCollection, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkPorts",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    resource_block_id: str, computer_system_id: str, network_interface_id: str
) -> NetworkPortCollection:
    s: Service = find_service(NetworkPortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
    }
    return cast(NetworkPortCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/NetworkInterfaces/{network_interface_id}/NetworkPorts",
    response_model_exclude_none=True,
)
@authenticate
async def get5(resource_block_id: str, network_interface_id: str) -> NetworkPortCollection:
    s: Service = find_service(NetworkPortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "network_interface_id": network_interface_id,
    }
    return cast(NetworkPortCollection, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/NetworkInterfaces/{network_interface_id}/NetworkPorts",
    response_model_exclude_none=True,
)
@authenticate
async def get6(
    resource_block_id: str, computer_system_id: str, network_interface_id: str
) -> NetworkPortCollection:
    s: Service = find_service(NetworkPortCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "network_interface_id": network_interface_id,
    }
    return cast(NetworkPortCollection, s.get(**b))
