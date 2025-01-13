from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.event_service import (
    EventService,
    EventServiceOnUpdate,
    SubmitTestEventRequest,
)
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/EventService", response_model_exclude_none=True)
@router.head("/redfish/v1/EventService", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> EventService:
    s: Service = get_service(EventService, request)
    b: dict[str, Any] = {"request": request, "response": response}
    return cast(EventService, s.get(**b))


@router.patch("/redfish/v1/EventService", response_model_exclude_none=True)
@authenticate
async def patch1(request: Request, response: Response, body: EventServiceOnUpdate) -> EventService:
    s: Service = get_service(EventService, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(EventService, s.patch(**b))


@router.post(
    "/redfish/v1/EventService/Actions/EventService.SubmitTestEvent",
    response_model_exclude_none=True,
)
@authenticate
async def submit_test_event1(
    request: Request, response: Response, body: SubmitTestEventRequest
) -> RedfishError:
    s: Service = get_service(EventService, request)
    b: dict[str, Any] = {
        "request": request,
        "response": response,
        "body": body,
        "action": "SubmitTestEvent",
    }
    return s.action(**b)
