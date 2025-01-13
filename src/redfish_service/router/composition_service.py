from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.composition_service import (
    ComposeRequest,
    CompositionService,
    CompositionServiceOnUpdate,
)
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/CompositionService", response_model_exclude_none=True)
@router.head("/redfish/v1/CompositionService", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> CompositionService:
    s: Service = get_service(CompositionService, request)
    b: dict[str, Any] = {"request": request, "response": response}
    return cast(CompositionService, s.get(**b))


@router.patch("/redfish/v1/CompositionService", response_model_exclude_none=True)
@authenticate
async def patch1(
    request: Request, response: Response, body: CompositionServiceOnUpdate
) -> CompositionService:
    s: Service = get_service(CompositionService, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(CompositionService, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/Actions/CompositionService.Compose",
    response_model_exclude_none=True,
)
@authenticate
async def compose1(request: Request, response: Response, body: ComposeRequest) -> RedfishError:
    s: Service = get_service(CompositionService, request)
    b: dict[str, Any] = {
        "request": request,
        "response": response,
        "body": body,
        "action": "Compose",
    }
    return s.action(**b)
