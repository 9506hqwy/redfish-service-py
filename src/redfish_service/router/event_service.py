from typing import Any, cast

from fastapi import APIRouter

from ..model.event_service import EventService
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/EventService", response_model_exclude_none=True)
@authenticate
async def get1() -> EventService:
    s: Service = find_service(EventService)
    b: dict[str, Any] = {}
    return cast(EventService, s.get(**b))
