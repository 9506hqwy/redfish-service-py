from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.event_destination import EventDestination
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    event_destination_id: str, request: Request, response: Response
) -> EventDestination:
    s: Service = find_service(EventDestination)
    b: dict[str, Any] = {
        "event_destination_id": event_destination_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EventDestination, s.get(**b))
