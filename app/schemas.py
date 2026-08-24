from pydantic import BaseModel, Field
from enum import StrEnum


class EstimatedWaterLevel(StrEnum):
    BELOW_ANKLE = "0-0.3m"
    KNEE_LEVEL = "0.3-1.0m"
    WAIST_LEVEL = "1.0-1.8m"
    ABOVE_CHEST = "1.8m+"


class WaterTrend(StrEnum):
    RISING_FAST = "Rising Fast"
    RISING_SLOWLY = "Rising Slowly"
    STABLE = "Stable"
    FALLING = "Falling"


class VolunteerReport(BaseModel):
    constituency: str = Field(..., min_length=1, max_length=100)
    location: str = Field(..., min_length=1, max_length=200)
    estimated_water_level: EstimatedWaterLevel
    water_trend: WaterTrend
    photo_url: str | None = Field(default=None, max_length=2000)
    whatsapp_number: str = Field(..., min_length=3, max_length=30)
    notes: str | None = Field(default=None, max_length=2000)


class AlertRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=1000)
    location: str = Field(..., min_length=1, max_length=200)


class WhatsAppMessage(BaseModel):
    text: dict[str, str] | None = None


class WhatsAppValue(BaseModel):
    messages: list[WhatsAppMessage] | None = None


class WhatsAppChange(BaseModel):
    value: WhatsAppValue | None = None


class WhatsAppEntry(BaseModel):
    changes: list[WhatsAppChange] | None = None


class WhatsAppWebhookPayload(BaseModel):
    entry: list[WhatsAppEntry] | None = None
