from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.message_registry_file_collection import MessageRegistryFileCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Registries", response_model_exclude_none=True)
@authenticate
async def get1() -> MessageRegistryFileCollection:
    s: Service = find_service(MessageRegistryFileCollection)
    b: dict[str, Any] = {}
    return cast(MessageRegistryFileCollection, s.get(**b))
