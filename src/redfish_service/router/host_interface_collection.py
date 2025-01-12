from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.host_interface_collection import HostInterfaceCollection
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/Managers/{manager_id}/HostInterfaces", response_model_exclude_none=True)
@router.head("/redfish/v1/Managers/{manager_id}/HostInterfaces", response_model_exclude_none=True)
async def get1(manager_id: str, request: Request, response: Response) -> HostInterfaceCollection:
    s: Service = get_service(HostInterfaceCollection, request)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(HostInterfaceCollection, s.get(**b))
