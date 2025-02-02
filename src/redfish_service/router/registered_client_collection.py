from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.registered_client import RegisteredClient, RegisteredClientOnCreate
from ..model.registered_client_collection import RegisteredClientCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection, set_link_header

router = APIRouter()


@router.get("/redfish/v1/RegisteredClients", response_model_exclude_none=True)
@router.head("/redfish/v1/RegisteredClients", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> RegisteredClientCollection:
    s: Service = get_service(RegisteredClientCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(RegisteredClientCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post("/redfish/v1/RegisteredClients", response_model_exclude_none=True)
@router.post("/redfish/v1/RegisteredClients/Members", response_model_exclude_none=True)
@authenticate
async def post1(
    request: Request, response: Response, body: RegisteredClientOnCreate
) -> RegisteredClient:
    s: ServiceCollection = get_service_collection(RegisteredClientCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(RegisteredClient, s.post(**b))
