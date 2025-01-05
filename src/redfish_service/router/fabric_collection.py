from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.fabric_collection import FabricCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Fabrics", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> FabricCollection:
    s: Service = find_service(FabricCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(FabricCollection, s.get(**b))
