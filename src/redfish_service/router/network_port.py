from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.network_port import NetworkPort, NetworkPortOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

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
    s: Service = get_service(NetworkPort, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_port_id": network_port_id,
        "request": request,
        "response": response,
    }
    m = cast(NetworkPort, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/NetworkPorts/{network_port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    chassis_id: str,
    network_adapter_id: str,
    network_port_id: str,
    request: Request,
    response: Response,
    body: NetworkPortOnUpdate,
) -> NetworkPort:
    s: Service = get_service(NetworkPort, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "network_port_id": network_port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(NetworkPort, s.patch(**b))
