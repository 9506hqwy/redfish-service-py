from typing import Any, cast

from fastapi import APIRouter

from ..model.message_registry_file import MessageRegistryFile
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/Registries/{message_registry_file_id}", response_model_exclude_none=True)
@authenticate
async def get1(message_registry_file_id: str) -> MessageRegistryFile:
    s: Service = find_service(MessageRegistryFile)
    b: dict[str, Any] = {"message_registry_file_id": message_registry_file_id}
    return cast(MessageRegistryFile, s.get(**b))
