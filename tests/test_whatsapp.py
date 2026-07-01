import hashlib
import hmac
import importlib
import json

from fastapi.testclient import TestClient


def build_client(monkeypatch, tmp_path):
    monkeypatch.setenv("WHATSAPP_APP_SECRET", "test-secret")
    monkeypatch.setenv("ALERT_STORE_PATH", str(tmp_path / "alerts.json"))
    import app.main as main_module

    return TestClient(importlib.reload(main_module).app)


def make_signature(payload: dict, secret: str) -> str:
    body = json.dumps(payload).encode("utf-8")
    return hmac.new(secret.encode("utf-8"), body, hashlib.sha256).hexdigest()


def test_whatsapp_webhook_requires_signature_and_body(monkeypatch, tmp_path) -> None:
    client = build_client(monkeypatch, tmp_path)
    response = client.post("/webhooks/whatsapp", json={})
    assert response.status_code == 400


def test_whatsapp_webhook_rejects_invalid_signature(monkeypatch, tmp_path) -> None:
    client = build_client(monkeypatch, tmp_path)
    payload = {"entry": [{"changes": [{"value": {"messages": [{"text": {"body": "Flooding near school"}}]}}]}]}
    response = client.post(
        "/webhooks/whatsapp",
        json=payload,
        headers={"X-WhatsApp-Signature": "wrong-signature"},
    )
    assert response.status_code == 401


def test_whatsapp_webhook_accepts_valid_payload(monkeypatch, tmp_path) -> None:
    client = build_client(monkeypatch, tmp_path)
    payload = {"entry": [{"changes": [{"value": {"messages": [{"text": {"body": "Flooding near school"}}]}}]}]}
    response = client.post(
        "/webhooks/whatsapp",
        json=payload,
        headers={"X-WhatsApp-Signature": make_signature(payload, "test-secret")},
    )
    assert response.status_code == 200
    assert response.json()["status"] == "received"


def test_alert_is_persisted(monkeypatch, tmp_path) -> None:
    client = build_client(monkeypatch, tmp_path)
    response = client.post(
        "/alerts",
        json={"message": "Flooding near school", "location": "Accra"},
    )
    assert response.status_code == 200

    stored = json.loads((tmp_path / "alerts.json").read_text())
    assert len(stored) == 1
    assert stored[0]["message"] == "Flooding near school"
    assert stored[0]["location"] == "Accra"
