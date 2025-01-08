from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.coolant_connector import CoolantConnector
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/CoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/CoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str, coolant_connector_id: str, request: Request, response: Response
) -> CoolantConnector:
    s: Service = find_service(CoolantConnector)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CoolantConnector, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CoolingLoops/{cooling_unit_id}/PrimaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CoolingLoops/{cooling_unit_id}/PrimaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
async def get2(
    cooling_unit_id: str, coolant_connector_id: str, request: Request, response: Response
) -> CoolantConnector:
    s: Service = find_service(CoolantConnector)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CoolantConnector, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CoolingLoops/{cooling_unit_id}/SecondaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CoolingLoops/{cooling_unit_id}/SecondaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
async def get3(
    cooling_unit_id: str, coolant_connector_id: str, request: Request, response: Response
) -> CoolantConnector:
    s: Service = find_service(CoolantConnector)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CoolantConnector, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/PrimaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/PrimaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
async def get4(
    cooling_unit_id: str, coolant_connector_id: str, request: Request, response: Response
) -> CoolantConnector:
    s: Service = find_service(CoolantConnector)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CoolantConnector, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/SecondaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/SecondaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
async def get5(
    cooling_unit_id: str, coolant_connector_id: str, request: Request, response: Response
) -> CoolantConnector:
    s: Service = find_service(CoolantConnector)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CoolantConnector, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/PrimaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/PrimaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
async def get6(
    cooling_unit_id: str, coolant_connector_id: str, request: Request, response: Response
) -> CoolantConnector:
    s: Service = find_service(CoolantConnector)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CoolantConnector, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/SecondaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/SecondaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
async def get7(
    cooling_unit_id: str, coolant_connector_id: str, request: Request, response: Response
) -> CoolantConnector:
    s: Service = find_service(CoolantConnector)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CoolantConnector, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/PrimaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/PrimaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
async def get8(
    cooling_unit_id: str, coolant_connector_id: str, request: Request, response: Response
) -> CoolantConnector:
    s: Service = find_service(CoolantConnector)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CoolantConnector, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/SecondaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/SecondaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
async def get9(
    cooling_unit_id: str, coolant_connector_id: str, request: Request, response: Response
) -> CoolantConnector:
    s: Service = find_service(CoolantConnector)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CoolantConnector, s.get(**b))
