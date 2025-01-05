from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.session_collection import SessionCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/SessionService/Sessions", response_model_exclude_none=True)
@authenticate
async def get1() -> SessionCollection:
    s: Service = find_service(SessionCollection)
    b: dict[str, Any] = {}
    return cast(SessionCollection, s.get(**b))
