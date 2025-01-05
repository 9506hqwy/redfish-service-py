from typing import Any, cast

from fastapi import APIRouter

from ..model.host_interface import HostInterface
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Managers/{manager_id}/HostInterfaces/{host_interface_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(manager_id: str, host_interface_id: str) -> HostInterface:
    s: Service = find_service(HostInterface)
    b: dict[str, Any] = {"manager_id": manager_id, "host_interface_id": host_interface_id}
    return cast(HostInterface, s.get(**b))
