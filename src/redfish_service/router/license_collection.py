from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.license import License, LicenseOnCreate
from ..model.license_collection import LicenseCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection

router = APIRouter()


@router.get("/redfish/v1/LicenseService/Licenses", response_model_exclude_none=True)
@router.head("/redfish/v1/LicenseService/Licenses", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> LicenseCollection:
    s: Service = get_service(LicenseCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    return cast(LicenseCollection, s.get(**b))


@router.post("/redfish/v1/LicenseService/Licenses", response_model_exclude_none=True)
@router.post("/redfish/v1/LicenseService/Licenses/Members", response_model_exclude_none=True)
@authenticate
async def post1(request: Request, response: Response, body: LicenseOnCreate) -> License:
    s: ServiceCollection = get_service_collection(LicenseCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(License, s.post(**b))
