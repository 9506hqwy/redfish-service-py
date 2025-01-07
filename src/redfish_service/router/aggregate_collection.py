from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.aggregate import Aggregate, AggregateOnCreate
from ..model.aggregate_collection import AggregateCollection
from ..service import Service, ServiceCollection, find_service, find_service_collection

router = APIRouter()


@router.get("/redfish/v1/AggregationService/Aggregates", response_model_exclude_none=True)
@router.head("/redfish/v1/AggregationService/Aggregates", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> AggregateCollection:
    s: Service = find_service(AggregateCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(AggregateCollection, s.get(**b))


@router.post("/redfish/v1/AggregationService/Aggregates", response_model_exclude_none=True)
@router.post("/redfish/v1/AggregationService/Aggregates/Members", response_model_exclude_none=True)
@authenticate
async def post1(request: Request, response: Response, body: AggregateOnCreate) -> Aggregate:
    s: ServiceCollection = find_service_collection(AggregateCollection)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(Aggregate, s.post(**b))
