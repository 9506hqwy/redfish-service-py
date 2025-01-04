from typing import cast

from fastapi import APIRouter

from ..model.session_collection import SessionCollection
from ..service import find_service
from . import authenticate

router = APIRouter()


@router.get("", response_model_exclude_none=True)
@authenticate
async def root() -> SessionCollection:
    s = find_service(SessionCollection)
    return cast(SessionCollection, s.get())
