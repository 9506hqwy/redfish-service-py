from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.serial_interface_collection import SerialInterfaceCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Managers/{manager_id}/SerialInterfaces", response_model_exclude_none=True)
@router.head(
    "/redfish/v1/Managers/{manager_id}/SerialInterfaces", response_model_exclude_none=True
)
async def get1(manager_id: str, request: Request, response: Response) -> SerialInterfaceCollection:
    s: Service = find_service(SerialInterfaceCollection)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(SerialInterfaceCollection, s.get(**b))
