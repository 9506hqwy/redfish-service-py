from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.certificate_locations import CertificateLocations
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/CertificateService/CertificateLocations", response_model_exclude_none=True
)
@authenticate
async def get1(request: Request, response: Response) -> CertificateLocations:
    s: Service = find_service(CertificateLocations)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CertificateLocations, s.get(**b))
