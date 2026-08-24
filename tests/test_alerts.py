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


def test_submit_volunteer_report_maps_water_level_to_alert(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("ALERT_STORE_PATH", str(tmp_path / "reports.json"))
    response = client.post(
        "/reports",
        json={
            "constituency": "Ablekuma Central",
            "location": "Kaneshie Bridge",
            "estimated_water_level": "1.8m+",
            "water_trend": "Rising Fast",
            "whatsapp_number": "+233200000000",
            "notes": "Road flooded",
        },
    )

    assert response.status_code == 200
    assert response.json() == {"status": "accepted", "alert_level": "CRITICAL"}


def test_submit_volunteer_report_rejects_unknown_constituency() -> None:
    response = client.post(
        "/reports",
        json={
            "constituency": "Unknown",
            "location": "Somewhere",
            "estimated_water_level": "0-0.3m",
            "water_trend": "Stable",
            "whatsapp_number": "+233200000000",
        },
    )

    assert response.status_code == 422
