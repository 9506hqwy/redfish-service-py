from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.graphics_controller_collection import GraphicsControllerCollection
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/GraphicsControllers",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/GraphicsControllers",
    response_model_exclude_none=True,
)
async def get1(
    computer_system_id: str, request: Request, response: Response
) -> GraphicsControllerCollection:
    s: Service = get_service(GraphicsControllerCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(GraphicsControllerCollection, s.get(**b))
