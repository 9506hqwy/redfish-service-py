from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.redfish_error import RedfishError
from ..model.telemetry_service import (
    CollectTelemetryDataRequest,
    SubmitTestMetricReportRequest,
    TelemetryService,
    TelemetryServiceOnUpdate,
)
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get("/redfish/v1/TelemetryService", response_model_exclude_none=True)
@router.head("/redfish/v1/TelemetryService", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> TelemetryService:
    s: Service = get_service(TelemetryService, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(TelemetryService, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch("/redfish/v1/TelemetryService", response_model_exclude_none=True)
@authenticate
async def patch1(
    request: Request, response: Response, body: TelemetryServiceOnUpdate
) -> TelemetryService:
    s: Service = get_service(TelemetryService, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(TelemetryService, s.patch(**b))


@router.post(
    "/redfish/v1/TelemetryService/Actions/TelemetryService.CollectTelemetryData",
    response_model_exclude_none=True,
)
@authenticate
async def collect_telemetry_data1(
    request: Request, response: Response, body: CollectTelemetryDataRequest
) -> RedfishError:
    s: Service = get_service(TelemetryService, request)
    b: dict[str, Any] = {
        "request": request,
        "response": response,
        "body": body,
        "action": "CollectTelemetryData",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/TelemetryService/Actions/TelemetryService.SubmitTestMetricReport",
    response_model_exclude_none=True,
)
@authenticate
async def submit_test_metric_report1(
    request: Request, response: Response, body: SubmitTestMetricReportRequest
) -> RedfishError:
    s: Service = get_service(TelemetryService, request)
    b: dict[str, Any] = {
        "request": request,
        "response": response,
        "body": body,
        "action": "SubmitTestMetricReport",
    }
    return s.action(**b)
