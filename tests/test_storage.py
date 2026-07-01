from app.storage import AlertStore


def test_alert_store_persists_to_disk(tmp_path) -> None:
    store = AlertStore(str(tmp_path / "alerts.json"))
    store.append({"message": "Flooding", "location": "Accra"})
    assert store.load()[0]["message"] == "Flooding"
