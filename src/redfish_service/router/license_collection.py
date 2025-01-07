from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.license import License, LicenseOnCreate
from ..model.license_collection import LicenseCollection
from ..service import Service, ServiceCollection, find_service, find_service_collection

router = APIRouter()


@router.get("/redfish/v1/LicenseService/Licenses", response_model_exclude_none=True)
@router.head("/redfish/v1/LicenseService/Licenses", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> LicenseCollection:
    s: Service = find_service(LicenseCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(LicenseCollection, s.get(**b))


@router.post("/redfish/v1/LicenseService/Licenses", response_model_exclude_none=True)
@router.post("/redfish/v1/LicenseService/Licenses/Members", response_model_exclude_none=True)
@authenticate
async def post1(request: Request, response: Response, body: LicenseOnCreate) -> License:
    s: ServiceCollection = find_service_collection(LicenseCollection)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(License, s.post(**b))
