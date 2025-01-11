from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.pcie_slots import PcieSlots, PcieSlotsOnUpdate
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/PCIeSlots", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis/{chassis_id}/PCIeSlots", response_model_exclude_none=True)
async def get1(chassis_id: str, request: Request, response: Response) -> PcieSlots:
    s: Service = find_service(PcieSlots)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(PcieSlots, s.get(**b))


@router.patch("/redfish/v1/Chassis/{chassis_id}/PCIeSlots", response_model_exclude_none=True)
@authenticate
async def patch1(
    chassis_id: str, request: Request, response: Response, body: PcieSlotsOnUpdate
) -> PcieSlots:
    s: Service = find_service(PcieSlots)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(PcieSlots, s.patch(**b))
