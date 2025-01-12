from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.aggregate import Aggregate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/AggregationService/Aggregates/{aggregate_id}", response_model_exclude_none=True
)
@authenticate
async def delete1(aggregate_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Aggregate, request)
    b: dict[str, Any] = {"aggregate_id": aggregate_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/AggregationService/Aggregates/{aggregate_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/AggregationService/Aggregates/{aggregate_id}", response_model_exclude_none=True
)
async def get1(aggregate_id: str, request: Request, response: Response) -> Aggregate:
    s: Service = get_service(Aggregate, request)
    b: dict[str, Any] = {"aggregate_id": aggregate_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(Aggregate, s.get(**b))
