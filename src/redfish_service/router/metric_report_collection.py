from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.metric_report_collection import MetricReportCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/TelemetryService/MetricReports", response_model_exclude_none=True)
@router.head("/redfish/v1/TelemetryService/MetricReports", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> MetricReportCollection:
    s: Service = find_service(MetricReportCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(MetricReportCollection, s.get(**b))
