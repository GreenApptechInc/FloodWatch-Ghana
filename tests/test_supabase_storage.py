from app.storage import SupabaseAlertStore


def test_supabase_store_stays_noop_without_credentials() -> None:
    store = SupabaseAlertStore(url="", key="")
    store.append({"message": "Flooding", "location": "Accra"})
    assert store.load() == []
