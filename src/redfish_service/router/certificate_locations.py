from typing import Any, cast

from fastapi import APIRouter

from ..model.certificate_locations import CertificateLocations
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/CertificateService/CertificateLocations", response_model_exclude_none=True
)
@authenticate
async def get1() -> CertificateLocations:
    s: Service = find_service(CertificateLocations)
    b: dict[str, Any] = {}
    return cast(CertificateLocations, s.get(**b))
