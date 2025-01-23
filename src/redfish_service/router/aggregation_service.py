from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.aggregation_service import (
    AggregationService,
    AggregationServiceOnUpdate,
    ResetRequest,
    SetDefaultBootOrderRequest,
)
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get("/redfish/v1/AggregationService", response_model_exclude_none=True)
@router.head("/redfish/v1/AggregationService", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> AggregationService:
    s: Service = get_service(AggregationService, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(AggregationService, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch("/redfish/v1/AggregationService", response_model_exclude_none=True)
@authenticate
async def patch1(
    request: Request, response: Response, body: AggregationServiceOnUpdate
) -> AggregationService:
    s: Service = get_service(AggregationService, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(AggregationService, s.patch(**b))


@router.post(
    "/redfish/v1/AggregationService/Actions/AggregationService.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset1(request: Request, response: Response, body: ResetRequest) -> RedfishError:
    s: Service = get_service(AggregationService, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body, "action": "Reset"}
    return s.action(**b)


@router.post(
    "/redfish/v1/AggregationService/Actions/AggregationService.SetDefaultBootOrder",
    response_model_exclude_none=True,
)
@authenticate
async def set_default_boot_order1(
    request: Request, response: Response, body: SetDefaultBootOrderRequest
) -> RedfishError:
    s: Service = get_service(AggregationService, request)
    b: dict[str, Any] = {
        "request": request,
        "response": response,
        "body": body,
        "action": "SetDefaultBootOrder",
    }
    return s.action(**b)
