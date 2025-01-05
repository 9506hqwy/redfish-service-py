from typing import Any, cast

from fastapi import APIRouter

from ..model.key_service import KeyService
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/KeyService", response_model_exclude_none=True)
@authenticate
async def get1() -> KeyService:
    s: Service = find_service(KeyService)
    b: dict[str, Any] = {}
    return cast(KeyService, s.get(**b))
