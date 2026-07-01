from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_submit_alert_requires_message_and_location() -> None:
    response = client.post(
        "/alerts",
        json={"message": "", "location": ""},
    )
    assert response.status_code == 422


def test_submit_alert_accepts_valid_payload() -> None:
    response = client.post(
        "/alerts",
        json={"message": "Flooding near school", "location": "Accra"},
    )
    assert response.status_code == 200
    assert response.json()["status"] == "accepted"
