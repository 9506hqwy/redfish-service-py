from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.outbound_connection import OutboundConnection, OutboundConnectionOnCreate
from ..model.outbound_connection_collection import OutboundConnectionCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection, set_link_header

router = APIRouter()


@router.get("/redfish/v1/AccountService/OutboundConnections", response_model_exclude_none=True)
@router.head("/redfish/v1/AccountService/OutboundConnections", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> OutboundConnectionCollection:
    s: Service = get_service(OutboundConnectionCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(OutboundConnectionCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post("/redfish/v1/AccountService/OutboundConnections", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/AccountService/OutboundConnections/Members", response_model_exclude_none=True
)
@authenticate
async def post1(
    request: Request, response: Response, body: OutboundConnectionOnCreate
) -> OutboundConnection:
    s: ServiceCollection = get_service_collection(OutboundConnectionCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(OutboundConnection, s.post(**b))
