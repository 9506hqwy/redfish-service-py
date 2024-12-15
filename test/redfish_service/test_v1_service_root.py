from redfish_service.v1.service_root import (
    ServiceRoot,
    ServiceRootLinks,
)


def test_service_root_min() -> None:
    obj_info = {
        "id": "a",
        "links": {
            "sessions": {
                "odata_id": "b",
            },
        },
        "name": "c",
        "odata_id": "d",
        "odata_type": "e",
    }
    ServiceRoot.model_validate(obj_info)


def test_service_root_link_min() -> None:
    obj_info = {"sessions": {"odata_id": "a"}}
    ServiceRootLinks.model_validate(obj_info)
