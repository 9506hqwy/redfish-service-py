from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.connection_method_collection import ConnectionMethodCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/AggregationService/ConnectionMethods", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> ConnectionMethodCollection:
    s: Service = find_service(ConnectionMethodCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ConnectionMethodCollection, s.get(**b))
