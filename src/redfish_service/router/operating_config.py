from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.operating_config import OperatingConfig
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/OperatingConfigs/{operating_config_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/OperatingConfigs/{operating_config_id}",
    response_model_exclude_none=True,
)
async def get1(
    computer_system_id: str,
    processor_id: str,
    operating_config_id: str,
    request: Request,
    response: Response,
) -> OperatingConfig:
    s: Service = get_service(OperatingConfig, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "operating_config_id": operating_config_id,
        "request": request,
        "response": response,
    }
    return cast(OperatingConfig, s.get(**b))
