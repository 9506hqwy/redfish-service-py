from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.manager import Manager
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Managers/{manager_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/Managers/{manager_id}", response_model_exclude_none=True)
@authenticate
async def get1(manager_id: str, request: Request, response: Response) -> Manager:
    s: Service = find_service(Manager)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(Manager, s.get(**b))
