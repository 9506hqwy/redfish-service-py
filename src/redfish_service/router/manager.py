from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.manager import Manager, ManagerOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/Managers/{manager_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/Managers/{manager_id}", response_model_exclude_none=True)
async def get1(manager_id: str, request: Request, response: Response) -> Manager:
    s: Service = get_service(Manager, request)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}
    return cast(Manager, s.get(**b))


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
