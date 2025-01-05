from typing import Any, cast

from fastapi import APIRouter

from ..model.switch import Switch
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}", response_model_exclude_none=True
)
@authenticate
async def get1(fabric_id: str, switch_id: str) -> Switch:
    s: Service = find_service(Switch)
    b: dict[str, Any] = {"fabric_id": fabric_id, "switch_id": switch_id}
    return cast(Switch, s.get(**b))
