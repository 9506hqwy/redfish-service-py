from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.session_service import SessionService
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/SessionService", response_model_exclude_none=True)
@authenticate
async def get1() -> SessionService:
    s: Service = find_service(SessionService)
    b: dict[str, Any] = {}
    return cast(SessionService, s.get(**b))
