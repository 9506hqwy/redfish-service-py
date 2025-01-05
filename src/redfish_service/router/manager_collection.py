from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.manager_collection import ManagerCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Managers", response_model_exclude_none=True)
@authenticate
async def get1() -> ManagerCollection:
    s: Service = find_service(ManagerCollection)
    b: dict[str, Any] = {}
    return cast(ManagerCollection, s.get(**b))
