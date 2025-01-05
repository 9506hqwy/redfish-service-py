from typing import Any, cast

from fastapi import APIRouter

from ..model.service_conditions import ServiceConditions
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/ServiceConditions", response_model_exclude_none=True)
@authenticate
async def get1() -> ServiceConditions:
    s: Service = find_service(ServiceConditions)
    b: dict[str, Any] = {}
    return cast(ServiceConditions, s.get(**b))
