from typing import Any, cast

from fastapi import APIRouter

from ..model.fabric_collection import FabricCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/Fabrics", response_model_exclude_none=True)
@authenticate
async def get1() -> FabricCollection:
    s: Service = find_service(FabricCollection)
    b: dict[str, Any] = {}
    return cast(FabricCollection, s.get(**b))
