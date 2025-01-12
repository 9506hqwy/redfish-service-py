from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.connection_method import ConnectionMethod, ConnectionMethodOnCreate
from ..model.connection_method_collection import ConnectionMethodCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection

router = APIRouter()


@router.get("/redfish/v1/AggregationService/ConnectionMethods", response_model_exclude_none=True)
@router.head("/redfish/v1/AggregationService/ConnectionMethods", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> ConnectionMethodCollection:
    s: Service = get_service(ConnectionMethodCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    return cast(ConnectionMethodCollection, s.get(**b))


@router.post("/redfish/v1/AggregationService/ConnectionMethods", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/AggregationService/ConnectionMethods/Members", response_model_exclude_none=True
)
@authenticate
async def post1(
    request: Request, response: Response, body: ConnectionMethodOnCreate
) -> ConnectionMethod:
    s: ServiceCollection = get_service_collection(ConnectionMethodCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(ConnectionMethod, s.post(**b))
