from typing import Any, cast

from fastapi import APIRouter

from ..model.license_collection import LicenseCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/LicenseService/Licenses", response_model_exclude_none=True)
@authenticate
async def get1() -> LicenseCollection:
    s: Service = find_service(LicenseCollection)
    b: dict[str, Any] = {}
    return cast(LicenseCollection, s.get(**b))
