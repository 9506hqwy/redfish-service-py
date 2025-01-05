from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.pcie_slots import PcieSlots
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/PCIeSlots", response_model_exclude_none=True)
@authenticate
async def get1(chassis_id: str) -> PcieSlots:
    s: Service = find_service(PcieSlots)
    b: dict[str, Any] = {"chassis_id": chassis_id}
    return cast(PcieSlots, s.get(**b))
