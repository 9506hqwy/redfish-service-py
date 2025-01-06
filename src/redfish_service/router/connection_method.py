from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.connection_method import ConnectionMethod
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/AggregationService/ConnectionMethods/{connection_method_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AggregationService/ConnectionMethods/{connection_method_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    connection_method_id: str, request: Request, response: Response
) -> ConnectionMethod:
    s: Service = find_service(ConnectionMethod)
    b: dict[str, Any] = {
        "connection_method_id": connection_method_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(ConnectionMethod, s.get(**b))
