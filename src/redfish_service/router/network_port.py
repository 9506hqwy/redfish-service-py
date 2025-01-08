from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.network_port import NetworkPort
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkPorts/{network_port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkPorts/{network_port_id}",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str,
    network_adapter_id: str,
    network_port_id: str,
    request: Request,
    response: Response,
) -> NetworkPort:
    s: Service = find_service(NetworkPort)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_port_id": network_port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(NetworkPort, s.get(**b))
