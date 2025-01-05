from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.session import Session
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/SessionService/Sessions/{session_id}", response_model_exclude_none=True)
@authenticate
async def get1(session_id: str) -> Session:
    s: Service = find_service(Session)
    b: dict[str, Any] = {"session_id": session_id}
    return cast(Session, s.get(**b))
