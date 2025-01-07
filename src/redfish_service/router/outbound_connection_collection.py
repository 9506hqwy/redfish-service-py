from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.outbound_connection import OutboundConnection, OutboundConnectionOnCreate
from ..model.outbound_connection_collection import OutboundConnectionCollection
from ..service import Service, ServiceCollection, find_service, find_service_collection

router = APIRouter()


@router.get("/redfish/v1/AccountService/OutboundConnections", response_model_exclude_none=True)
@router.head("/redfish/v1/AccountService/OutboundConnections", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> OutboundConnectionCollection:
    s: Service = find_service(OutboundConnectionCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(OutboundConnectionCollection, s.get(**b))


@router.post("/redfish/v1/AccountService/OutboundConnections", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/AccountService/OutboundConnections/Members", response_model_exclude_none=True
)
@authenticate
async def post1(
    request: Request, response: Response, body: OutboundConnectionOnCreate
) -> OutboundConnection:
    s: ServiceCollection = find_service_collection(OutboundConnectionCollection)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(OutboundConnection, s.post(**b))
