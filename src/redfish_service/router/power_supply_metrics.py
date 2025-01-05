from typing import Any, cast

from fastapi import APIRouter

from ..model.power_supply_metrics import PowerSupplyMetrics
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get1(chassis_id: str, power_supply_id: str) -> PowerSupplyMetrics:
    s: Service = find_service(PowerSupplyMetrics)
    b: dict[str, Any] = {"chassis_id": chassis_id, "power_supply_id": power_supply_id}
    return cast(PowerSupplyMetrics, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/PowerSupplies/{power_supply_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get2(power_distribution_id: str, power_supply_id: str) -> PowerSupplyMetrics:
    s: Service = find_service(PowerSupplyMetrics)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "power_supply_id": power_supply_id,
    }
    return cast(PowerSupplyMetrics, s.get(**b))
