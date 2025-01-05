from typing import Any, cast

from fastapi import APIRouter

from ..model.chassis_collection import ChassisCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/Chassis", response_model_exclude_none=True)
@authenticate
async def get1() -> ChassisCollection:
    s: Service = find_service(ChassisCollection)
    b: dict[str, Any] = {}
    return cast(ChassisCollection, s.get(**b))
