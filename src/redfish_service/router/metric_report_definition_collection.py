from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.metric_report_definition_collection import MetricReportDefinitionCollection
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/TelemetryService/MetricReportDefinitions", response_model_exclude_none=True
)
@authenticate
async def get1(request: Request, response: Response) -> MetricReportDefinitionCollection:
    s: Service = find_service(MetricReportDefinitionCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(MetricReportDefinitionCollection, s.get(**b))
