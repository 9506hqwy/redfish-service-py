from typing import Any, cast

from fastapi import APIRouter

from ..model.trusted_component_collection import TrustedComponentCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/TrustedComponents", response_model_exclude_none=True)
@authenticate
async def get1(chassis_id: str) -> TrustedComponentCollection:
    s: Service = find_service(TrustedComponentCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id}
    return cast(TrustedComponentCollection, s.get(**b))
