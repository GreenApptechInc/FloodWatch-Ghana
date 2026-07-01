from fastapi import FastAPI

from app.schemas import AlertRequest

app = FastAPI(title="FloodWatch Ghana", version="0.1.0")


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/readyz")
def readyz() -> dict[str, str]:
    return {"status": "ready"}


@app.post("/alerts")
def submit_alert(payload: AlertRequest) -> dict[str, str]:
    return {"status": "accepted", "message": payload.message, "location": payload.location}
