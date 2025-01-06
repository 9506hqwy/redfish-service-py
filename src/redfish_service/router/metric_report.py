from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.metric_report import MetricReport
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/TelemetryService/MetricReports/{metric_report_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/TelemetryService/MetricReports/{metric_report_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(metric_report_id: str, request: Request, response: Response) -> MetricReport:
    s: Service = find_service(MetricReport)
    b: dict[str, Any] = {
        "metric_report_id": metric_report_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(MetricReport, s.get(**b))
