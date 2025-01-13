from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.manager_network_protocol import (
    ManagerNetworkProtocol,
    ManagerNetworkProtocolOnUpdate,
)
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/Managers/{manager_id}/NetworkProtocol", response_model_exclude_none=True)
@router.head("/redfish/v1/Managers/{manager_id}/NetworkProtocol", response_model_exclude_none=True)
async def get1(manager_id: str, request: Request, response: Response) -> ManagerNetworkProtocol:
    s: Service = get_service(ManagerNetworkProtocol, request)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}
    return cast(ManagerNetworkProtocol, s.get(**b))


@router.patch(
    "/redfish/v1/Managers/{manager_id}/NetworkProtocol", response_model_exclude_none=True
)
@authenticate
async def patch1(
    manager_id: str, request: Request, response: Response, body: ManagerNetworkProtocolOnUpdate
) -> ManagerNetworkProtocol:
    s: Service = get_service(ManagerNetworkProtocol, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(ManagerNetworkProtocol, s.patch(**b))
