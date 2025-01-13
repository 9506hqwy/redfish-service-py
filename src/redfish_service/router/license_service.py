from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.license_service import InstallRequest, LicenseService, LicenseServiceOnUpdate
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/LicenseService", response_model_exclude_none=True)
@router.head("/redfish/v1/LicenseService", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> LicenseService:
    s: Service = get_service(LicenseService, request)
    b: dict[str, Any] = {"request": request, "response": response}
    return cast(LicenseService, s.get(**b))


@router.patch("/redfish/v1/LicenseService", response_model_exclude_none=True)
@authenticate
async def patch1(
    request: Request, response: Response, body: LicenseServiceOnUpdate
) -> LicenseService:
    s: Service = get_service(LicenseService, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(LicenseService, s.patch(**b))


@router.post(
    "/redfish/v1/LicenseService/Actions/LicenseService.Install", response_model_exclude_none=True
)
@authenticate
async def install1(request: Request, response: Response, body: InstallRequest) -> RedfishError:
    s: Service = get_service(LicenseService, request)
    b: dict[str, Any] = {
        "request": request,
        "response": response,
        "body": body,
        "action": "Install",
    }
    return s.action(**b)
