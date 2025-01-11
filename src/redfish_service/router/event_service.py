from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.event_service import EventService, EventServiceOnUpdate
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/EventService", response_model_exclude_none=True)
@router.head("/redfish/v1/EventService", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> EventService:
    s: Service = find_service(EventService)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(EventService, s.get(**b))


@router.patch("/redfish/v1/EventService", response_model_exclude_none=True)
@authenticate
async def patch1(request: Request, response: Response, body: EventServiceOnUpdate) -> EventService:
    s: Service = find_service(EventService)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(EventService, s.patch(**b))
