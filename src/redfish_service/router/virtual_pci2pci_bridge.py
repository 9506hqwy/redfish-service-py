from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.virtual_pci2pci_bridge import (
    VirtualPci2pciBridge,
    VirtualPci2pciBridgeOnUpdate,
)
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/VCSs/{virtual_cxl_switch_id}/VPPBs/{virtual_pci2pci_bridge_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/VCSs/{virtual_cxl_switch_id}/VPPBs/{virtual_pci2pci_bridge_id}",
    response_model_exclude_none=True,
)
async def get1(
    fabric_id: str,
    switch_id: str,
    virtual_cxl_switch_id: str,
    virtual_pci2pci_bridge_id: str,
    request: Request,
    response: Response,
) -> VirtualPci2pciBridge:
    s: Service = get_service(VirtualPci2pciBridge, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "virtual_cxl_switch_id": virtual_cxl_switch_id,
        "virtual_pci2pci_bridge_id": virtual_pci2pci_bridge_id,
        "request": request,
        "response": response,
    }
    m = cast(VirtualPci2pciBridge, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/VCSs/{virtual_cxl_switch_id}/VPPBs/{virtual_pci2pci_bridge_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    fabric_id: str,
    switch_id: str,
    virtual_cxl_switch_id: str,
    virtual_pci2pci_bridge_id: str,
    request: Request,
    response: Response,
    body: VirtualPci2pciBridgeOnUpdate,
) -> VirtualPci2pciBridge:
    s: Service = get_service(VirtualPci2pciBridge, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "virtual_cxl_switch_id": virtual_cxl_switch_id,
        "virtual_pci2pci_bridge_id": virtual_pci2pci_bridge_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VirtualPci2pciBridge, s.patch(**b))
