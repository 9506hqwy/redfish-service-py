from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.connection_method import ConnectionMethod
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/AggregationService/ConnectionMethods/{connection_method_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AggregationService/ConnectionMethods/{connection_method_id}",
    response_model_exclude_none=True,
)
async def get1(
    connection_method_id: str, request: Request, response: Response
) -> ConnectionMethod:
    s: Service = get_service(ConnectionMethod, request)
    b: dict[str, Any] = {
        "connection_method_id": connection_method_id,
        "request": request,
        "response": response,
    }
    m = cast(ConnectionMethod, s.get(**b))
    set_link_header(m, response)
    return m
