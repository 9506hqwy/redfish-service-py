from typing import Any, cast

from fastapi import APIRouter

from ..model.serial_interface_collection import SerialInterfaceCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/Managers/{manager_id}/SerialInterfaces", response_model_exclude_none=True)
@authenticate
async def get1(manager_id: str) -> SerialInterfaceCollection:
    s: Service = find_service(SerialInterfaceCollection)
    b: dict[str, Any] = {"manager_id": manager_id}
    return cast(SerialInterfaceCollection, s.get(**b))
