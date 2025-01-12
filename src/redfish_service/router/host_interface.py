from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.host_interface import HostInterface, HostInterfaceOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Managers/{manager_id}/HostInterfaces/{host_interface_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/HostInterfaces/{host_interface_id}",
    response_model_exclude_none=True,
)
async def get1(
    manager_id: str, host_interface_id: str, request: Request, response: Response
) -> HostInterface:
    s: Service = get_service(HostInterface, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "host_interface_id": host_interface_id,
        "request": request,
        "response": response,
    }
    return cast(HostInterface, s.get(**b))


@router.patch(
    "/redfish/v1/Managers/{manager_id}/HostInterfaces/{host_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    manager_id: str,
    host_interface_id: str,
    request: Request,
    response: Response,
    body: HostInterfaceOnUpdate,
) -> HostInterface:
    s: Service = get_service(HostInterface, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "host_interface_id": host_interface_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(HostInterface, s.patch(**b))
