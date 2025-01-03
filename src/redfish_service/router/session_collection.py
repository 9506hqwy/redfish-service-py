from fastapi import APIRouter

from ..v1.session_collection import SessionCollection
from . import PATH_SESSION_COLLECTION, authenticate

router = APIRouter()

sessions_info = {
    "odata_id": PATH_SESSION_COLLECTION,
    "odata_type": "#SessionCollection.SessionCollection",
    "members": [],
    "members_odata_count": 0,
    "name": "Session Collection",
}


@router.get("", response_model_exclude_none=True)
@authenticate
async def root() -> SessionCollection:
    return SessionCollection.model_validate(sessions_info)
