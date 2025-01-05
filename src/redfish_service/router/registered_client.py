from typing import Any, cast

from fastapi import APIRouter

from ..model.registered_client import RegisteredClient
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/RegisteredClients/{registered_client_id}", response_model_exclude_none=True
)
@authenticate
async def get1(registered_client_id: str) -> RegisteredClient:
    s: Service = find_service(RegisteredClient)
    b: dict[str, Any] = {"registered_client_id": registered_client_id}
    return cast(RegisteredClient, s.get(**b))
