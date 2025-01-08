from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.computer_system import ComputerSystem, ComputerSystemOnCreate
from ..model.computer_system_collection import ComputerSystemCollection
from ..service import Service, ServiceCollection, find_service, find_service_collection

router = APIRouter()


@router.get("/redfish/v1/Systems", response_model_exclude_none=True)
@router.head("/redfish/v1/Systems", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> ComputerSystemCollection:
    s: Service = find_service(ComputerSystemCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ComputerSystemCollection, s.get(**b))


@router.post("/redfish/v1/Systems", response_model_exclude_none=True)
@router.post("/redfish/v1/Systems/Members", response_model_exclude_none=True)
@authenticate
async def post1(
    request: Request, response: Response, body: ComputerSystemOnCreate
) -> ComputerSystem:
    s: ServiceCollection = find_service_collection(ComputerSystemCollection)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(ComputerSystem, s.post(**b))
