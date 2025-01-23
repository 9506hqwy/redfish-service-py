from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.power_supply_metrics import PowerSupplyMetrics
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}/Metrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}/Metrics",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str, power_supply_id: str, request: Request, response: Response
) -> PowerSupplyMetrics:
    s: Service = get_service(PowerSupplyMetrics, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "power_supply_id": power_supply_id,
        "request": request,
        "response": response,
    }
    m = cast(PowerSupplyMetrics, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/PowerSupplies/{power_supply_id}/Metrics",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/PowerSupplies/{power_supply_id}/Metrics",
    response_model_exclude_none=True,
)
async def get2(
    power_distribution_id: str, power_supply_id: str, request: Request, response: Response
) -> PowerSupplyMetrics:
    s: Service = get_service(PowerSupplyMetrics, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "power_supply_id": power_supply_id,
        "request": request,
        "response": response,
    }
    m = cast(PowerSupplyMetrics, s.get(**b))
    set_link_header(m, response)
    return m
