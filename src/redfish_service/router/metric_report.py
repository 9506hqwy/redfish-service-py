from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.metric_report import MetricReport
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/TelemetryService/MetricReports/{metric_report_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(metric_report_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(MetricReport, request)
    b: dict[str, Any] = {
        "metric_report_id": metric_report_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/TelemetryService/MetricReports/{metric_report_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/TelemetryService/MetricReports/{metric_report_id}",
    response_model_exclude_none=True,
)
async def get1(metric_report_id: str, request: Request, response: Response) -> MetricReport:
    s: Service = get_service(MetricReport, request)
    b: dict[str, Any] = {
        "metric_report_id": metric_report_id,
        "request": request,
        "response": response,
    }
    return cast(MetricReport, s.get(**b))
