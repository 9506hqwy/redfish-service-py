from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.network_port import NetworkPort
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkPorts/{network_port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(chassis_id: str, network_adapter_id: str, network_port_id: str) -> NetworkPort:
    s: Service = find_service(NetworkPort)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_port_id": network_port_id,
    }
    return cast(NetworkPort, s.get(**b))
