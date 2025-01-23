from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.network_adapter import NetworkAdapter, NetworkAdapterOnUpdate, ResetRequest
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str, network_adapter_id: str, request: Request, response: Response
) -> NetworkAdapter:
    s: Service = get_service(NetworkAdapter, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "request": request,
        "response": response,
    }
    m = cast(NetworkAdapter, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    chassis_id: str,
    network_adapter_id: str,
    request: Request,
    response: Response,
    body: NetworkAdapterOnUpdate,
) -> NetworkAdapter:
    s: Service = get_service(NetworkAdapter, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(NetworkAdapter, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Actions/NetworkAdapter.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset1(
    chassis_id: str,
    network_adapter_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(NetworkAdapter, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)
