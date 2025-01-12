from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.certificate_locations import CertificateLocations
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/CertificateService/CertificateLocations", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/CertificateService/CertificateLocations", response_model_exclude_none=True
)
async def get1(request: Request, response: Response) -> CertificateLocations:
    s: Service = get_service(CertificateLocations, request)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateLocations, s.get(**b))
