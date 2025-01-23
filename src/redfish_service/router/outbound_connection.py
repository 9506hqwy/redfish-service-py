from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.outbound_connection import OutboundConnection, OutboundConnectionOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(outbound_connection_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(OutboundConnection, request)
    b: dict[str, Any] = {
        "outbound_connection_id": outbound_connection_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}",
    response_model_exclude_none=True,
)
async def get1(
    outbound_connection_id: str, request: Request, response: Response
) -> OutboundConnection:
    s: Service = get_service(OutboundConnection, request)
    b: dict[str, Any] = {
        "outbound_connection_id": outbound_connection_id,
        "request": request,
        "response": response,
    }
    m = cast(OutboundConnection, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    outbound_connection_id: str,
    request: Request,
    response: Response,
    body: OutboundConnectionOnUpdate,
) -> OutboundConnection:
    s: Service = get_service(OutboundConnection, request)
    b: dict[str, Any] = {
        "outbound_connection_id": outbound_connection_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(OutboundConnection, s.patch(**b))
