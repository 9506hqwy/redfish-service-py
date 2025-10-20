from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.coolant_connector import (
    CoolantConnector,
    CoolantConnectorOnUpdate,
    ValveControlRequest,
)
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service, set_link_header

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
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
    }
    m = cast(CoolantConnector, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/CoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    chassis_id: str,
    coolant_connector_id: str,
    request: Request,
    response: Response,
    body: CoolantConnectorOnUpdate,
) -> CoolantConnector:
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CoolantConnector, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/CoolantConnectors/{coolant_connector_id}/Actions/CoolantConnector.ValveControl",
    response_model_exclude_none=True,
)
@authenticate
async def valve_control1(
    chassis_id: str,
    coolant_connector_id: str,
    request: Request,
    response: Response,
    body: ValveControlRequest,
) -> RedfishError:
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ValveControl",
    }
    return s.action(**b)


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
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
    }
    m = cast(CoolantConnector, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ThermalEquipment/CoolingLoops/{cooling_unit_id}/PrimaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    cooling_unit_id: str,
    coolant_connector_id: str,
    request: Request,
    response: Response,
    body: CoolantConnectorOnUpdate,
) -> CoolantConnector:
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CoolantConnector, s.patch(**b))


@router.post(
    "/redfish/v1/ThermalEquipment/CoolingLoops/{cooling_unit_id}/PrimaryCoolantConnectors/{coolant_connector_id}/Actions/CoolantConnector.ValveControl",
    response_model_exclude_none=True,
)
@authenticate
async def valve_control2(
    cooling_unit_id: str,
    coolant_connector_id: str,
    request: Request,
    response: Response,
    body: ValveControlRequest,
) -> RedfishError:
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ValveControl",
    }
    return s.action(**b)


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
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
    }
    m = cast(CoolantConnector, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ThermalEquipment/CoolingLoops/{cooling_unit_id}/SecondaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    cooling_unit_id: str,
    coolant_connector_id: str,
    request: Request,
    response: Response,
    body: CoolantConnectorOnUpdate,
) -> CoolantConnector:
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CoolantConnector, s.patch(**b))


@router.post(
    "/redfish/v1/ThermalEquipment/CoolingLoops/{cooling_unit_id}/SecondaryCoolantConnectors/{coolant_connector_id}/Actions/CoolantConnector.ValveControl",
    response_model_exclude_none=True,
)
@authenticate
async def valve_control3(
    cooling_unit_id: str,
    coolant_connector_id: str,
    request: Request,
    response: Response,
    body: ValveControlRequest,
) -> RedfishError:
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ValveControl",
    }
    return s.action(**b)


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
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
    }
    m = cast(CoolantConnector, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/PrimaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    cooling_unit_id: str,
    coolant_connector_id: str,
    request: Request,
    response: Response,
    body: CoolantConnectorOnUpdate,
) -> CoolantConnector:
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CoolantConnector, s.patch(**b))


@router.post(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/PrimaryCoolantConnectors/{coolant_connector_id}/Actions/CoolantConnector.ValveControl",
    response_model_exclude_none=True,
)
@authenticate
async def valve_control4(
    cooling_unit_id: str,
    coolant_connector_id: str,
    request: Request,
    response: Response,
    body: ValveControlRequest,
) -> RedfishError:
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ValveControl",
    }
    return s.action(**b)


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
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
    }
    m = cast(CoolantConnector, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/SecondaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    cooling_unit_id: str,
    coolant_connector_id: str,
    request: Request,
    response: Response,
    body: CoolantConnectorOnUpdate,
) -> CoolantConnector:
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CoolantConnector, s.patch(**b))


@router.post(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/SecondaryCoolantConnectors/{coolant_connector_id}/Actions/CoolantConnector.ValveControl",
    response_model_exclude_none=True,
)
@authenticate
async def valve_control5(
    cooling_unit_id: str,
    coolant_connector_id: str,
    request: Request,
    response: Response,
    body: ValveControlRequest,
) -> RedfishError:
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ValveControl",
    }
    return s.action(**b)


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
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
    }
    m = cast(CoolantConnector, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/PrimaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    cooling_unit_id: str,
    coolant_connector_id: str,
    request: Request,
    response: Response,
    body: CoolantConnectorOnUpdate,
) -> CoolantConnector:
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CoolantConnector, s.patch(**b))


@router.post(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/PrimaryCoolantConnectors/{coolant_connector_id}/Actions/CoolantConnector.ValveControl",
    response_model_exclude_none=True,
)
@authenticate
async def valve_control6(
    cooling_unit_id: str,
    coolant_connector_id: str,
    request: Request,
    response: Response,
    body: ValveControlRequest,
) -> RedfishError:
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ValveControl",
    }
    return s.action(**b)


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
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
    }
    m = cast(CoolantConnector, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/SecondaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch7(
    cooling_unit_id: str,
    coolant_connector_id: str,
    request: Request,
    response: Response,
    body: CoolantConnectorOnUpdate,
) -> CoolantConnector:
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CoolantConnector, s.patch(**b))


@router.post(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/SecondaryCoolantConnectors/{coolant_connector_id}/Actions/CoolantConnector.ValveControl",
    response_model_exclude_none=True,
)
@authenticate
async def valve_control7(
    cooling_unit_id: str,
    coolant_connector_id: str,
    request: Request,
    response: Response,
    body: ValveControlRequest,
) -> RedfishError:
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ValveControl",
    }
    return s.action(**b)


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
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
    }
    m = cast(CoolantConnector, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/PrimaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch8(
    cooling_unit_id: str,
    coolant_connector_id: str,
    request: Request,
    response: Response,
    body: CoolantConnectorOnUpdate,
) -> CoolantConnector:
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CoolantConnector, s.patch(**b))


@router.post(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/PrimaryCoolantConnectors/{coolant_connector_id}/Actions/CoolantConnector.ValveControl",
    response_model_exclude_none=True,
)
@authenticate
async def valve_control8(
    cooling_unit_id: str,
    coolant_connector_id: str,
    request: Request,
    response: Response,
    body: ValveControlRequest,
) -> RedfishError:
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ValveControl",
    }
    return s.action(**b)


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
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
    }
    m = cast(CoolantConnector, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/SecondaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch9(
    cooling_unit_id: str,
    coolant_connector_id: str,
    request: Request,
    response: Response,
    body: CoolantConnectorOnUpdate,
) -> CoolantConnector:
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CoolantConnector, s.patch(**b))


@router.post(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/SecondaryCoolantConnectors/{coolant_connector_id}/Actions/CoolantConnector.ValveControl",
    response_model_exclude_none=True,
)
@authenticate
async def valve_control9(
    cooling_unit_id: str,
    coolant_connector_id: str,
    request: Request,
    response: Response,
    body: ValveControlRequest,
) -> RedfishError:
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ValveControl",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ThermalEquipment/RPUs/{cooling_unit_id}/PrimaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/RPUs/{cooling_unit_id}/PrimaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
async def get10(
    cooling_unit_id: str, coolant_connector_id: str, request: Request, response: Response
) -> CoolantConnector:
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
    }
    m = cast(CoolantConnector, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ThermalEquipment/RPUs/{cooling_unit_id}/PrimaryCoolantConnectors/{coolant_connector_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch10(
    cooling_unit_id: str,
    coolant_connector_id: str,
    request: Request,
    response: Response,
    body: CoolantConnectorOnUpdate,
) -> CoolantConnector:
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CoolantConnector, s.patch(**b))


@router.post(
    "/redfish/v1/ThermalEquipment/RPUs/{cooling_unit_id}/PrimaryCoolantConnectors/{coolant_connector_id}/Actions/CoolantConnector.ValveControl",
    response_model_exclude_none=True,
)
@authenticate
async def valve_control10(
    cooling_unit_id: str,
    coolant_connector_id: str,
    request: Request,
    response: Response,
    body: ValveControlRequest,
) -> RedfishError:
    s: Service = get_service(CoolantConnector, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "coolant_connector_id": coolant_connector_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ValveControl",
    }
    return s.action(**b)
