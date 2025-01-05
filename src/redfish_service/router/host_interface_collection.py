from typing import Any, cast

from fastapi import APIRouter

from ..model.host_interface_collection import HostInterfaceCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/Managers/{manager_id}/HostInterfaces", response_model_exclude_none=True)
@authenticate
async def get1(manager_id: str) -> HostInterfaceCollection:
    s: Service = find_service(HostInterfaceCollection)
    b: dict[str, Any] = {"manager_id": manager_id}
    return cast(HostInterfaceCollection, s.get(**b))
