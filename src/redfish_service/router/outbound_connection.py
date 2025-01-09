from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.outbound_connection import OutboundConnection
from ..service import Service, find_service

router = APIRouter()


@router.delete(
    "/redfish/v1/AccountService/OutboundConnections/{outbound_connection_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(outbound_connection_id: str, request: Request, response: Response) -> None:
    s: Service = find_service(OutboundConnection)
    b: dict[str, Any] = {
        "outbound_connection_id": outbound_connection_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

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
    s: Service = find_service(OutboundConnection)
    b: dict[str, Any] = {
        "outbound_connection_id": outbound_connection_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(OutboundConnection, s.get(**b))
