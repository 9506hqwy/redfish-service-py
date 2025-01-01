from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishObject,
    RedfishObjectId,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resolution_step import ResolutionStep


class Condition(RedfishModel):
    log_entry: IdRef | None = None
    message: str | None = None
    message_args: list[str] | None = None
    message_id: str
    origin_of_condition: IdRef | None = None
    resolution: str | None = None
    resolution_steps: list[ResolutionStep] | None = None
    severity: Health | None = None
    timestamp: str | None = None
    user_authentication_source: str | None = None
    username: str | None = None


class ContactInfo(RedfishModel):
    contact_name: str | None = None
    email_address: str | None = None
    phone_number: str | None = None


class DurableNameFormat(StrEnum):
    NAA = "NAA"
    IQN = "iQN"
    FC__WWN = "FC_WWN"
    UUID = "UUID"
    EUI = "EUI"
    NQN = "NQN"
    NSID = "NSID"
    NGUID = "NGUID"
    MACADDRESS = "MACAddress"
    GCXLID = "GCXLID"


class Health(StrEnum):
    OK = "OK"
    WARNING = "Warning"
    CRITICAL = "Critical"


class Identifier(RedfishModel):
    durable_name: str | None = None
    durable_name_format: DurableNameFormat | None = None


class IndicatorLed(StrEnum):
    LIT = "Lit"
    BLINKING = "Blinking"
    OFF = "Off"


class Links(RedfishModel):
    oem: dict[str, Any] | None = None


class Location(RedfishModel):
    altitude_meters: float | None = None
    contacts: list[ContactInfo] | None = None
    info: str | None = None
    info_format: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    oem: dict[str, Any] | None = None
    part_location: PartLocation | None = None
    part_location_context: str | None = None
    physical_address: PhysicalAddress | None = None
    placement: Placement | None = None
    postal_address: PostalAddress | None = None


class LocationType(StrEnum):
    SLOT = "Slot"
    BAY = "Bay"
    CONNECTOR = "Connector"
    SOCKET = "Socket"
    BACKPLANE = "Backplane"
    EMBEDDED = "Embedded"


class Orientation(StrEnum):
    FRONT_TO_BACK = "FrontToBack"
    BACK_TO_FRONT = "BackToFront"
    TOP_TO_BOTTOM = "TopToBottom"
    BOTTOM_TO_TOP = "BottomToTop"
    LEFT_TO_RIGHT = "LeftToRight"
    RIGHT_TO_LEFT = "RightToLeft"


class PartLocation(RedfishModel):
    location_ordinal_value: int | None = None
    location_type: LocationType | None = None
    orientation: Orientation | None = None
    reference: Reference | None = None
    service_label: str | None = None


class PhysicalAddress(RedfishModel):
    city: str | None = None
    country: str | None = None
    isocountry_code: str | None = Field(alias="ISOCountryCode", default=None)
    isosubdivision_code: str | None = Field(alias="ISOSubdivisionCode", default=None)
    postal_code: str | None = None
    state_or_province: str | None = None
    street_address: str | None = None


class Placement(RedfishModel):
    additional_info: str | None = None
    rack: str | None = None
    rack_offset: int | None = None
    rack_offset_units: RackUnits | None = None
    row: str | None = None


class PostalAddress(RedfishModel):
    additional_code: str | None = None
    additional_info: str | None = None
    building: str | None = None
    city: str | None = None
    community: str | None = None
    country: str | None = None
    district: str | None = None
    division: str | None = None
    floor: str | None = None
    gpscoords: str | None = Field(alias="GPSCoords", default=None)
    house_number: int | None = None
    house_number_suffix: str | None = None
    landmark: str | None = None
    leading_street_direction: str | None = None
    location: str | None = None
    name: str | None = None
    neighborhood: str | None = None
    pobox: str | None = Field(alias="POBox", default=None)
    place_type: str | None = None
    postal_code: str | None = None
    road: str | None = None
    road_branch: str | None = None
    road_post_modifier: str | None = None
    road_pre_modifier: str | None = None
    road_section: str | None = None
    road_sub_branch: str | None = None
    room: str | None = None
    seat: str | None = None
    street: str | None = None
    street_suffix: str | None = None
    territory: str | None = None
    trailing_street_suffix: str | None = None
    unit: str | None = None


class PowerState(StrEnum):
    ON = "On"
    OFF = "Off"
    POWERING_ON = "PoweringOn"
    POWERING_OFF = "PoweringOff"
    PAUSED = "Paused"


class RackUnits(StrEnum):
    OPEN_U = "OpenU"
    EIA_310 = "EIA_310"


class Reference(StrEnum):
    TOP = "Top"
    BOTTOM = "Bottom"
    FRONT = "Front"
    REAR = "Rear"
    LEFT = "Left"
    RIGHT = "Right"
    MIDDLE = "Middle"


class ReferenceableMember(RedfishObjectId):
    member_id: str
    oem: dict[str, Any] | None = None


class Resource(RedfishResource):
    description: str | None = None
    oem: dict[str, Any] | None = None


class ResourceCollection(RedfishObject):
    description: str | None = None
    name: str
    oem: dict[str, Any] | None = None


class State(StrEnum):
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    STANDBY_OFFLINE = "StandbyOffline"
    STANDBY_SPARE = "StandbySpare"
    IN_TEST = "InTest"
    STARTING = "Starting"
    ABSENT = "Absent"
    UNAVAILABLE_OFFLINE = "UnavailableOffline"
    DEFERRING = "Deferring"
    QUIESCED = "Quiesced"
    UPDATING = "Updating"
    QUALIFIED = "Qualified"
    DEGRADED = "Degraded"


class Status(RedfishModel):
    conditions: list[Condition] | None = None
    health: Health | None = None
    health_rollup: Health | None = None
    oem: dict[str, Any] | None = None
    state: State | None = None
