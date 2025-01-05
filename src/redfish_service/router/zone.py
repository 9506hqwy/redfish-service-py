from typing import Any, cast

from fastapi import APIRouter

from ..model.zone import Zone
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/Fabrics/{fabric_id}/Zones/{zone_id}", response_model_exclude_none=True)
@authenticate
async def get1(fabric_id: str, zone_id: str) -> Zone:
    s: Service = find_service(Zone)
    b: dict[str, Any] = {"fabric_id": fabric_id, "zone_id": zone_id}
    return cast(Zone, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceZones/{zone_id}", response_model_exclude_none=True
)
@authenticate
async def get2(zone_id: str) -> Zone:
    s: Service = find_service(Zone)
    b: dict[str, Any] = {"zone_id": zone_id}
    return cast(Zone, s.get(**b))
