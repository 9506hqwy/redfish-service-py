from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.media_controller_collection import MediaControllerCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/MediaControllers", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis/{chassis_id}/MediaControllers", response_model_exclude_none=True)
async def get1(chassis_id: str, request: Request, response: Response) -> MediaControllerCollection:
    s: Service = find_service(MediaControllerCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(MediaControllerCollection, s.get(**b))
