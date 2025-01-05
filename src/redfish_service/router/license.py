from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.license import License
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/LicenseService/Licenses/{license_id}", response_model_exclude_none=True)
@authenticate
async def get1(license_id: str) -> License:
    s: Service = find_service(License)
    b: dict[str, Any] = {"license_id": license_id}
    return cast(License, s.get(**b))
