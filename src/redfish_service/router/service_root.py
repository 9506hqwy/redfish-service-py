from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.service_root import ServiceRoot
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/", response_model_exclude_none=True)
@authenticate
async def get1() -> ServiceRoot:
    s: Service = find_service(ServiceRoot)
    b: dict[str, Any] = {}
    return cast(ServiceRoot, s.get(**b))
