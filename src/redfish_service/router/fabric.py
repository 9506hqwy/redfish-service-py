from typing import Any, cast

from fastapi import APIRouter

from ..model.fabric import Fabric
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/Fabrics/{fabric_id}", response_model_exclude_none=True)
@authenticate
async def get1(fabric_id: str) -> Fabric:
    s: Service = find_service(Fabric)
    b: dict[str, Any] = {"fabric_id": fabric_id}
    return cast(Fabric, s.get(**b))
