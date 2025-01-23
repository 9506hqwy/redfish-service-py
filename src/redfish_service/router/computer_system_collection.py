from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.computer_system import ComputerSystem, ComputerSystemOnCreate
from ..model.computer_system_collection import ComputerSystemCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection, set_link_header

router = APIRouter()


@router.get("/redfish/v1/Systems", response_model_exclude_none=True)
@router.head("/redfish/v1/Systems", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> ComputerSystemCollection:
    s: Service = get_service(ComputerSystemCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(ComputerSystemCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post("/redfish/v1/Systems", response_model_exclude_none=True)
@router.post("/redfish/v1/Systems/Members", response_model_exclude_none=True)
@authenticate
async def post1(
    request: Request, response: Response, body: ComputerSystemOnCreate
) -> ComputerSystem:
    s: ServiceCollection = get_service_collection(ComputerSystemCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(ComputerSystem, s.post(**b))
