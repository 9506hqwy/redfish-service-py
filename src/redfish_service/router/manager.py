from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.manager import (
    ForceFailoverRequest,
    Manager,
    ManagerOnUpdate,
    ModifyRedundancySetRequest,
    ResetRequest,
    ResetToDefaultsRequest,
)
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get("/redfish/v1/Managers/{manager_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/Managers/{manager_id}", response_model_exclude_none=True)
async def get1(manager_id: str, request: Request, response: Response) -> Manager:
    s: Service = get_service(Manager, request)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}
    m = cast(Manager, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch("/redfish/v1/Managers/{manager_id}", response_model_exclude_none=True)
@authenticate
async def patch1(
    manager_id: str, request: Request, response: Response, body: ManagerOnUpdate
) -> Manager:
    s: Service = get_service(Manager, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Manager, s.patch(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/Actions/Manager.ForceFailover",
    response_model_exclude_none=True,
)
@authenticate
async def force_failover1(
    manager_id: str, request: Request, response: Response, body: ForceFailoverRequest
) -> RedfishError:
    s: Service = get_service(Manager, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ForceFailover",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Managers/{manager_id}/Actions/Manager.ModifyRedundancySet",
    response_model_exclude_none=True,
)
@authenticate
async def modify_redundancy_set1(
    manager_id: str, request: Request, response: Response, body: ModifyRedundancySetRequest
) -> RedfishError:
    s: Service = get_service(Manager, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ModifyRedundancySet",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Managers/{manager_id}/Actions/Manager.Reset", response_model_exclude_none=True
)
@authenticate
async def reset1(
    manager_id: str, request: Request, response: Response, body: ResetRequest
) -> RedfishError:
    s: Service = get_service(Manager, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Managers/{manager_id}/Actions/Manager.ResetToDefaults",
    response_model_exclude_none=True,
)
@authenticate
async def reset_to_defaults1(
    manager_id: str, request: Request, response: Response, body: ResetToDefaultsRequest
) -> RedfishError:
    s: Service = get_service(Manager, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResetToDefaults",
    }
    return s.action(**b)
