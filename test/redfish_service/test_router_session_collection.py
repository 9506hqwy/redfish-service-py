from fastapi.testclient import TestClient

from redfish_service.service import app

client = TestClient(app)


def test_root() -> None:
    auth = ("admin", "admin")
    response = client.get("/redfish/v1/SessionService/Sessions", auth=auth)
    assert response.status_code == 200
