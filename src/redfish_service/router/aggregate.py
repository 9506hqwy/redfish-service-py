from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.aggregate import (
    AddElementsRequest,
    Aggregate,
    RemoveElementsRequest,
    ResetRequest,
)
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete(
    "/redfish/v1/AggregationService/Aggregates/{aggregate_id}", response_model_exclude_none=True
)
@authenticate
async def delete1(aggregate_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Aggregate, request)
    b: dict[str, Any] = {"aggregate_id": aggregate_id, "request": request, "response": response}
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
    m = cast(Aggregate, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/AggregationService/Aggregates/{aggregate_id}/Actions/Aggregate.AddElements",
    response_model_exclude_none=True,
)
@authenticate
async def add_elements1(
    aggregate_id: str, request: Request, response: Response, body: AddElementsRequest
) -> RedfishError:
    s: Service = get_service(Aggregate, request)
    b: dict[str, Any] = {
        "aggregate_id": aggregate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddElements",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/AggregationService/Aggregates/{aggregate_id}/Actions/Aggregate.RemoveElements",
    response_model_exclude_none=True,
)
@authenticate
async def remove_elements1(
    aggregate_id: str, request: Request, response: Response, body: RemoveElementsRequest
) -> RedfishError:
    s: Service = get_service(Aggregate, request)
    b: dict[str, Any] = {
        "aggregate_id": aggregate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveElements",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/AggregationService/Aggregates/{aggregate_id}/Actions/Aggregate.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset1(
    aggregate_id: str, request: Request, response: Response, body: ResetRequest
) -> RedfishError:
    s: Service = get_service(Aggregate, request)
    b: dict[str, Any] = {
        "aggregate_id": aggregate_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)
