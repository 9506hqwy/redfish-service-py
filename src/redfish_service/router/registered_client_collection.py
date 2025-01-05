from typing import Any, cast

from fastapi import APIRouter

from ..model.registered_client_collection import RegisteredClientCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/RegisteredClients", response_model_exclude_none=True)
@authenticate
async def get1() -> RegisteredClientCollection:
    s: Service = find_service(RegisteredClientCollection)
    b: dict[str, Any] = {}
    return cast(RegisteredClientCollection, s.get(**b))
