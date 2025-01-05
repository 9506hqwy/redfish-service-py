from typing import Any, cast

from fastapi import APIRouter

from ..model.metric_definition import MetricDefinition
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/TelemetryService/MetricDefinitions/{metric_definition_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(metric_definition_id: str) -> MetricDefinition:
    s: Service = find_service(MetricDefinition)
    b: dict[str, Any] = {"metric_definition_id": metric_definition_id}
    return cast(MetricDefinition, s.get(**b))
