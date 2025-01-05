from typing import Any, cast

from fastapi import APIRouter

from ..model.metric_definition_collection import MetricDefinitionCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/TelemetryService/MetricDefinitions", response_model_exclude_none=True)
@authenticate
async def get1() -> MetricDefinitionCollection:
    s: Service = find_service(MetricDefinitionCollection)
    b: dict[str, Any] = {}
    return cast(MetricDefinitionCollection, s.get(**b))
