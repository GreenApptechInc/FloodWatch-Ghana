from pydantic import BaseModel, Field


class AlertRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=1000)
    location: str = Field(..., min_length=1, max_length=200)
