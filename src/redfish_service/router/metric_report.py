from typing import Any, cast

from fastapi import APIRouter

from ..model.metric_report import MetricReport
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/TelemetryService/MetricReports/{metric_report_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(metric_report_id: str) -> MetricReport:
    s: Service = find_service(MetricReport)
    b: dict[str, Any] = {"metric_report_id": metric_report_id}
    return cast(MetricReport, s.get(**b))
