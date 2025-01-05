from typing import Any, cast

from fastapi import APIRouter

from ..model.network_adapter_collection import NetworkAdapterCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/NetworkAdapters", response_model_exclude_none=True)
@authenticate
async def get1(chassis_id: str) -> NetworkAdapterCollection:
    s: Service = find_service(NetworkAdapterCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id}
    return cast(NetworkAdapterCollection, s.get(**b))
