from typing import Any, cast

from fastapi import APIRouter

from ...model.swordfish.data_security_line_of_service import DataSecurityLineOfService
from ...service import Service, find_service
from .. import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataSecurityLinesOfService/{data_security_line_of_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    storage_service_id: str, data_security_line_of_service_id: str
) -> DataSecurityLineOfService:
    s: Service = find_service(DataSecurityLineOfService)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "data_security_line_of_service_id": data_security_line_of_service_id,
    }
    return cast(DataSecurityLineOfService, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataSecurityLinesOfService/{data_security_line_of_service_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    storage_service_id: str, class_of_service_id: str, data_security_line_of_service_id: str
) -> DataSecurityLineOfService:
    s: Service = find_service(DataSecurityLineOfService)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "data_security_line_of_service_id": data_security_line_of_service_id,
    }
    return cast(DataSecurityLineOfService, s.get(**b))
