from typing import Any, cast

from fastapi import APIRouter

from ..model.operating_config_collection import OperatingConfigCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/OperatingConfigs",
    response_model_exclude_none=True,
)
@authenticate
async def get1(computer_system_id: str, processor_id: str) -> OperatingConfigCollection:
    s: Service = find_service(OperatingConfigCollection)
    b: dict[str, Any] = {"computer_system_id": computer_system_id, "processor_id": processor_id}
    return cast(OperatingConfigCollection, s.get(**b))
