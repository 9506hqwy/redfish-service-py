from typing import Any, cast

from fastapi import APIRouter

from ..model.certificate_service import CertificateService
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/CertificateService", response_model_exclude_none=True)
@authenticate
async def get1() -> CertificateService:
    s: Service = find_service(CertificateService)
    b: dict[str, Any] = {}
    return cast(CertificateService, s.get(**b))
