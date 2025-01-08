from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.connection_method import ConnectionMethod, ConnectionMethodOnCreate
from ..model.connection_method_collection import ConnectionMethodCollection
from ..service import Service, ServiceCollection, find_service, find_service_collection

router = APIRouter()


@router.get("/redfish/v1/AggregationService/ConnectionMethods", response_model_exclude_none=True)
@router.head("/redfish/v1/AggregationService/ConnectionMethods", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> ConnectionMethodCollection:
    s: Service = find_service(ConnectionMethodCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ConnectionMethodCollection, s.get(**b))


@router.post("/redfish/v1/AggregationService/ConnectionMethods", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/AggregationService/ConnectionMethods/Members", response_model_exclude_none=True
)
@authenticate
async def post1(
    request: Request, response: Response, body: ConnectionMethodOnCreate
) -> ConnectionMethod:
    s: ServiceCollection = find_service_collection(ConnectionMethodCollection)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(ConnectionMethod, s.post(**b))
