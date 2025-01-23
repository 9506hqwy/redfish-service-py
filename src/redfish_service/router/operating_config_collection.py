from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.operating_config_collection import OperatingConfigCollection
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/OperatingConfigs",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/OperatingConfigs",
    response_model_exclude_none=True,
)
async def get1(
    computer_system_id: str, processor_id: str, request: Request, response: Response
) -> OperatingConfigCollection:
    s: Service = get_service(OperatingConfigCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "request": request,
        "response": response,
    }
    m = cast(OperatingConfigCollection, s.get(**b))
    set_link_header(m, response)
    return m
