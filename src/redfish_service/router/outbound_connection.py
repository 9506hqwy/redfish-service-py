from typing import Any, cast

from fastapi import APIRouter

from ..model.outbound_connection import OutboundConnection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(outbound_connection_id: str) -> OutboundConnection:
    s: Service = find_service(OutboundConnection)
    b: dict[str, Any] = {"outbound_connection_id": outbound_connection_id}
    return cast(OutboundConnection, s.get(**b))
