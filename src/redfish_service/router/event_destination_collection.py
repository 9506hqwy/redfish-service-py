from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.event_destination import EventDestination, EventDestinationOnCreate
from ..model.event_destination_collection import EventDestinationCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection, set_link_header

router = APIRouter()


@router.get("/redfish/v1/EventService/Subscriptions", response_model_exclude_none=True)
@router.head("/redfish/v1/EventService/Subscriptions", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> EventDestinationCollection:
    s: Service = get_service(EventDestinationCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(EventDestinationCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post("/redfish/v1/EventService/Subscriptions", response_model_exclude_none=True)
@router.post("/redfish/v1/EventService/Subscriptions/Members", response_model_exclude_none=True)
@authenticate
async def post1(
    request: Request, response: Response, body: EventDestinationOnCreate
) -> EventDestination:
    s: ServiceCollection = get_service_collection(EventDestinationCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(EventDestination, s.post(**b))
