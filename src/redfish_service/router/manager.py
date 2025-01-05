from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.manager import Manager
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Managers/{manager_id}", response_model_exclude_none=True)
@authenticate
async def get1(manager_id: str) -> Manager:
    s: Service = find_service(Manager)
    b: dict[str, Any] = {"manager_id": manager_id}
    return cast(Manager, s.get(**b))
