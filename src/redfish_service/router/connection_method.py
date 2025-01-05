from typing import Any, cast

from fastapi import APIRouter

from ..model.connection_method import ConnectionMethod
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/AggregationService/ConnectionMethods/{connection_method_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(connection_method_id: str) -> ConnectionMethod:
    s: Service = find_service(ConnectionMethod)
    b: dict[str, Any] = {"connection_method_id": connection_method_id}
    return cast(ConnectionMethod, s.get(**b))
