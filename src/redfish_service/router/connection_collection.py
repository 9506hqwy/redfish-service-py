from typing import Any, cast

from fastapi import APIRouter

from ..model.connection_collection import ConnectionCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/Fabrics/{fabric_id}/Connections", response_model_exclude_none=True)
@authenticate
async def get1(fabric_id: str) -> ConnectionCollection:
    s: Service = find_service(ConnectionCollection)
    b: dict[str, Any] = {"fabric_id": fabric_id}
    return cast(ConnectionCollection, s.get(**b))


@router.get("/redfish/v1/Storage/{storage_id}/Connections", response_model_exclude_none=True)
@authenticate
async def get2(storage_id: str) -> ConnectionCollection:
    s: Service = find_service(ConnectionCollection)
    b: dict[str, Any] = {"storage_id": storage_id}
    return cast(ConnectionCollection, s.get(**b))
