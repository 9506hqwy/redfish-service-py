from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.pcie_slots import PcieSlots, PcieSlotsOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/PCIeSlots", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis/{chassis_id}/PCIeSlots", response_model_exclude_none=True)
async def get1(chassis_id: str, request: Request, response: Response) -> PcieSlots:
    s: Service = get_service(PcieSlots, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}
    m = cast(PcieSlots, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch("/redfish/v1/Chassis/{chassis_id}/PCIeSlots", response_model_exclude_none=True)
@authenticate
async def patch1(
    chassis_id: str, request: Request, response: Response, body: PcieSlotsOnUpdate
) -> PcieSlots:
    s: Service = get_service(PcieSlots, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(PcieSlots, s.patch(**b))
