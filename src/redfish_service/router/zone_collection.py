from typing import Any, cast

from fastapi import APIRouter

from ..model.zone_collection import ZoneCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/Fabrics/{fabric_id}/Zones", response_model_exclude_none=True)
@authenticate
async def get1(fabric_id: str) -> ZoneCollection:
    s: Service = find_service(ZoneCollection)
    b: dict[str, Any] = {"fabric_id": fabric_id}
    return cast(ZoneCollection, s.get(**b))


@router.get("/redfish/v1/CompositionService/ResourceZones", response_model_exclude_none=True)
@authenticate
async def get2() -> ZoneCollection:
    s: Service = find_service(ZoneCollection)
    b: dict[str, Any] = {}
    return cast(ZoneCollection, s.get(**b))
