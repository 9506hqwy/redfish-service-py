from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.connection_method_collection import ConnectionMethodCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/AggregationService/ConnectionMethods", response_model_exclude_none=True)
@authenticate
async def get1() -> ConnectionMethodCollection:
    s: Service = find_service(ConnectionMethodCollection)
    b: dict[str, Any] = {}
    return cast(ConnectionMethodCollection, s.get(**b))
