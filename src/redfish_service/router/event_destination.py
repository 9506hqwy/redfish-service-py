from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.event_destination import (
    EventDestination,
    EventDestinationOnUpdate,
    ResumeSubscriptionRequest,
)
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(event_destination_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(EventDestination, request)
    b: dict[str, Any] = {
        "event_destination_id": event_destination_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}",
    response_model_exclude_none=True,
)
async def get1(
    event_destination_id: str, request: Request, response: Response
) -> EventDestination:
    s: Service = get_service(EventDestination, request)
    b: dict[str, Any] = {
        "event_destination_id": event_destination_id,
        "request": request,
        "response": response,
    }
    m = cast(EventDestination, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    event_destination_id: str, request: Request, response: Response, body: EventDestinationOnUpdate
) -> EventDestination:
    s: Service = get_service(EventDestination, request)
    b: dict[str, Any] = {
        "event_destination_id": event_destination_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(EventDestination, s.patch(**b))


@router.post(
    "/redfish/v1/EventService/Subscriptions/{event_destination_id}/Actions/EventDestination.ResumeSubscription",
    response_model_exclude_none=True,
)
@authenticate
async def resume_subscription1(
    event_destination_id: str,
    request: Request,
    response: Response,
    body: ResumeSubscriptionRequest,
) -> RedfishError:
    s: Service = get_service(EventDestination, request)
    b: dict[str, Any] = {
        "event_destination_id": event_destination_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ResumeSubscription",
    }
    return s.action(**b)
