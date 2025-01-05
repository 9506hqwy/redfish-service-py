from typing import Any, cast

from fastapi import APIRouter

from ..model.event_destination_collection import EventDestinationCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/EventService/Subscriptions", response_model_exclude_none=True)
@authenticate
async def get1() -> EventDestinationCollection:
    s: Service = find_service(EventDestinationCollection)
    b: dict[str, Any] = {}
    return cast(EventDestinationCollection, s.get(**b))
