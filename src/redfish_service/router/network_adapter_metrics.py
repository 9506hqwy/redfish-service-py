from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.network_adapter_metrics import NetworkAdapterMetrics
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    chassis_id: str, network_adapter_id: str, request: Request, response: Response
) -> NetworkAdapterMetrics:
    s: Service = find_service(NetworkAdapterMetrics)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(NetworkAdapterMetrics, s.get(**b))
