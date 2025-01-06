from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.switch_metrics import SwitchMetrics
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/SwitchMetrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/SwitchMetrics",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    fabric_id: str, switch_id: str, request: Request, response: Response
) -> SwitchMetrics:
    s: Service = find_service(SwitchMetrics)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(SwitchMetrics, s.get(**b))
