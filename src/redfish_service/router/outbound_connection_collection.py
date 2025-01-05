from typing import Any, cast

from fastapi import APIRouter

from ..model.outbound_connection_collection import OutboundConnectionCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/AccountService/OutboundConnections", response_model_exclude_none=True)
@authenticate
async def get1() -> OutboundConnectionCollection:
    s: Service = find_service(OutboundConnectionCollection)
    b: dict[str, Any] = {}
    return cast(OutboundConnectionCollection, s.get(**b))
