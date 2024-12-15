from redfish_service.v1.session_collection import SessionCollection


def test_session_collection_min() -> None:
    obj_info = {
        "id": "a",
        "members": [],
        "members_count": 0,
        "name": "c",
        "odata_id": "d",
        "odata_type": "e",
    }
    SessionCollection.model_validate(obj_info)
