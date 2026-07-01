from pydantic import BaseModel, Field


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
