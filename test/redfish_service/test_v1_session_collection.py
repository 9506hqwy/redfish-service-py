from redfish_service.model.session_collection import SessionCollection


def test_session_collection_min() -> None:
    obj_info = {
        "members": [],
        "members_odata_count": 0,
        "name": "c",
        "odata_id": "d",
    }
    SessionCollection.model_validate(obj_info)
