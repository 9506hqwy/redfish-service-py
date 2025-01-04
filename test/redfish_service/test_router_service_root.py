from fastapi.testclient import TestClient

from redfish_service.server import app

client = TestClient(app)


def test_root() -> None:
    auth = ("admin", "admin")
    response = client.get("/redfish/v1/", auth=auth)
    assert response.status_code == 200


def test_root_nonauth() -> None:
    auth = ("admin", "invalid")
    response = client.get("/redfish/v1/", auth=auth)
    assert response.status_code == 401
