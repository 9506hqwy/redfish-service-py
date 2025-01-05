from typing import Any, cast

from fastapi import APIRouter

from ..model.media_controller_collection import MediaControllerCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/MediaControllers", response_model_exclude_none=True)
@authenticate
async def get1(chassis_id: str) -> MediaControllerCollection:
    s: Service = find_service(MediaControllerCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id}
    return cast(MediaControllerCollection, s.get(**b))
