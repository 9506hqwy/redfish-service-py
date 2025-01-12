from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.license import License
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/LicenseService/Licenses/{license_id}", response_model_exclude_none=True
)
@authenticate
async def delete1(license_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(License, request)
    b: dict[str, Any] = {"license_id": license_id, "request": request, "response": response}
    return s.delete(**b)


@router.get("/redfish/v1/LicenseService/Licenses/{license_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/LicenseService/Licenses/{license_id}", response_model_exclude_none=True)
async def get1(license_id: str, request: Request, response: Response) -> License:
    s: Service = get_service(License, request)
    b: dict[str, Any] = {"license_id": license_id, "request": request, "response": response}
    return cast(License, s.get(**b))
