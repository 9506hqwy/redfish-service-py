from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.manager_diagnostic_data import ManagerDiagnosticData
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Managers/{manager_id}/ManagerDiagnosticData", response_model_exclude_none=True
)
@authenticate
async def get1(manager_id: str) -> ManagerDiagnosticData:
    s: Service = find_service(ManagerDiagnosticData)
    b: dict[str, Any] = {"manager_id": manager_id}
    return cast(ManagerDiagnosticData, s.get(**b))
