from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.update_service import UpdateService
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/UpdateService", response_model_exclude_none=True)
@authenticate
async def get1() -> UpdateService:
    s: Service = find_service(UpdateService)
    b: dict[str, Any] = {}
    return cast(UpdateService, s.get(**b))
