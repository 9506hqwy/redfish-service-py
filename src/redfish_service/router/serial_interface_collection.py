from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.serial_interface_collection import SerialInterfaceCollection
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/Managers/{manager_id}/SerialInterfaces", response_model_exclude_none=True)
@router.head(
    "/redfish/v1/Managers/{manager_id}/SerialInterfaces", response_model_exclude_none=True
)
async def get1(manager_id: str, request: Request, response: Response) -> SerialInterfaceCollection:
    s: Service = get_service(SerialInterfaceCollection, request)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}
    return cast(SerialInterfaceCollection, s.get(**b))
