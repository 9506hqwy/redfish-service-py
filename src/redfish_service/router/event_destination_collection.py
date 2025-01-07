from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.event_destination import EventDestination, EventDestinationOnCreate
from ..model.event_destination_collection import EventDestinationCollection
from ..service import Service, ServiceCollection, find_service, find_service_collection

router = APIRouter()


@router.get("/redfish/v1/EventService/Subscriptions", response_model_exclude_none=True)
@router.head("/redfish/v1/EventService/Subscriptions", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> EventDestinationCollection:
    s: Service = find_service(EventDestinationCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(EventDestinationCollection, s.get(**b))


@router.post("/redfish/v1/EventService/Subscriptions", response_model_exclude_none=True)
@router.post("/redfish/v1/EventService/Subscriptions/Members", response_model_exclude_none=True)
@authenticate
async def post1(
    request: Request, response: Response, body: EventDestinationOnCreate
) -> EventDestination:
    s: ServiceCollection = find_service_collection(EventDestinationCollection)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(EventDestination, s.post(**b))
