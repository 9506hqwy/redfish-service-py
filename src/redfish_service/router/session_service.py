from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.session_service import SessionService, SessionServiceOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/SessionService", response_model_exclude_none=True)
@router.head("/redfish/v1/SessionService", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> SessionService:
    s: Service = get_service(SessionService, request)
    b: dict[str, Any] = {"request": request, "response": response}
    return cast(SessionService, s.get(**b))


@router.patch("/redfish/v1/SessionService", response_model_exclude_none=True)
@authenticate
async def patch1(
    request: Request, response: Response, body: SessionServiceOnUpdate
) -> SessionService:
    s: Service = get_service(SessionService, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(SessionService, s.patch(**b))
