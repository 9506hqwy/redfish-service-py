from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.switch_collection import SwitchCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Fabrics/{fabric_id}/Switches", response_model_exclude_none=True)
@authenticate
async def get1(fabric_id: str, request: Request, response: Response) -> SwitchCollection:
    s: Service = find_service(SwitchCollection)
    b: dict[str, Any] = {"fabric_id": fabric_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(SwitchCollection, s.get(**b))
