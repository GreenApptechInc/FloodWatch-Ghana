from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "FloodWatch Ghana"
    environment: str = "development"
    whats_app_app_secret: str = Field(
        default="",
        validation_alias=AliasChoices("WHATSAPP_APP_SECRET", "WHATS_APP_APP_SECRET"),
    )
    alert_store_path: str = Field(default="alerts.json", validation_alias="ALERT_STORE_PATH")


def get_settings() -> Settings:
    return Settings()
