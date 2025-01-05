from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.license_service import LicenseService
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/LicenseService", response_model_exclude_none=True)
@authenticate
async def get1() -> LicenseService:
    s: Service = find_service(LicenseService)
    b: dict[str, Any] = {}
    return cast(LicenseService, s.get(**b))
