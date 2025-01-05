from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.trusted_component import TrustedComponent
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/TrustedComponents/{trusted_component_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(chassis_id: str, trusted_component_id: str) -> TrustedComponent:
    s: Service = find_service(TrustedComponent)
    b: dict[str, Any] = {"chassis_id": chassis_id, "trusted_component_id": trusted_component_id}
    return cast(TrustedComponent, s.get(**b))
