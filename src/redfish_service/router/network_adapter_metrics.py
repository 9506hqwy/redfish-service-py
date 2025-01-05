from typing import Any, cast

from fastapi import APIRouter

from ..model.network_adapter_metrics import NetworkAdapterMetrics
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get1(chassis_id: str, network_adapter_id: str) -> NetworkAdapterMetrics:
    s: Service = find_service(NetworkAdapterMetrics)
    b: dict[str, Any] = {"chassis_id": chassis_id, "network_adapter_id": network_adapter_id}
    return cast(NetworkAdapterMetrics, s.get(**b))
