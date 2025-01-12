from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.update_service import UpdateService, UpdateServiceOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/UpdateService", response_model_exclude_none=True)
@router.head("/redfish/v1/UpdateService", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> UpdateService:
    s: Service = get_service(UpdateService, request)
    b: dict[str, Any] = {"request": request, "response": response}
    return cast(UpdateService, s.get(**b))


@router.patch("/redfish/v1/UpdateService", response_model_exclude_none=True)
@authenticate
async def patch1(
    request: Request, response: Response, body: UpdateServiceOnUpdate
) -> UpdateService:
    s: Service = get_service(UpdateService, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(UpdateService, s.patch(**b))
