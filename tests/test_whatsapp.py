from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_whatsapp_webhook_requires_signature_and_body() -> None:
    response = client.post("/webhooks/whatsapp", json={})
    assert response.status_code == 400


def test_whatsapp_webhook_accepts_valid_payload() -> None:
    response = client.post(
        "/webhooks/whatsapp",
        json={"entry": [{"changes": [{"value": {"messages": [{"text": {"body": "Flooding near school"}}]}}]}]},
        headers={"X-WhatsApp-Signature": "test-signature"},
    )
    assert response.status_code == 200
    assert response.json()["status"] == "received"
