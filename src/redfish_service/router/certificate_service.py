from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.certificate_service import CertificateService
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/CertificateService", response_model_exclude_none=True)
@router.head("/redfish/v1/CertificateService", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> CertificateService:
    s: Service = get_service(CertificateService, request)
    b: dict[str, Any] = {"request": request, "response": response}
    return cast(CertificateService, s.get(**b))
