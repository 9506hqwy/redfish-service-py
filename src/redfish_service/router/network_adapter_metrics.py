from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.network_adapter_metrics import NetworkAdapterMetrics
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Metrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Metrics",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str, network_adapter_id: str, request: Request, response: Response
) -> NetworkAdapterMetrics:
    s: Service = get_service(NetworkAdapterMetrics, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "request": request,
        "response": response,
    }
    return cast(NetworkAdapterMetrics, s.get(**b))
