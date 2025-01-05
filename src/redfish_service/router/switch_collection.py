from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.switch_collection import SwitchCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Fabrics/{fabric_id}/Switches", response_model_exclude_none=True)
@authenticate
async def get1(fabric_id: str) -> SwitchCollection:
    s: Service = find_service(SwitchCollection)
    b: dict[str, Any] = {"fabric_id": fabric_id}
    return cast(SwitchCollection, s.get(**b))
