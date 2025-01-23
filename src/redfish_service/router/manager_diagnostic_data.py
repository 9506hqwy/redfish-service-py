from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.manager_diagnostic_data import ManagerDiagnosticData
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Managers/{manager_id}/ManagerDiagnosticData", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/ManagerDiagnosticData", response_model_exclude_none=True
)
async def get1(manager_id: str, request: Request, response: Response) -> ManagerDiagnosticData:
    s: Service = get_service(ManagerDiagnosticData, request)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}
    m = cast(ManagerDiagnosticData, s.get(**b))
    set_link_header(m, response)
    return m
