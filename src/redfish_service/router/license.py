from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.license import License
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/LicenseService/Licenses/{license_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/LicenseService/Licenses/{license_id}", response_model_exclude_none=True)
@authenticate
async def get1(license_id: str, request: Request, response: Response) -> License:
    s: Service = find_service(License)
    b: dict[str, Any] = {"license_id": license_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(License, s.get(**b))
