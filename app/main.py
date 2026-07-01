import hashlib
import hmac
import json
import logging
from datetime import datetime, timezone

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.config import get_settings
from app.schemas import AlertRequest, WhatsAppWebhookPayload
from app.storage import AlertStore

app = FastAPI(title="FloodWatch Ghana", version="0.1.0")
logger = logging.getLogger("floodwatch")
logger.setLevel(logging.INFO)


def get_store() -> AlertStore:
    settings = get_settings()
    return AlertStore(settings.alert_store_path)


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/readyz")
def readyz() -> dict[str, str]:
    return {"status": "ready"}


@app.post("/alerts")
def submit_alert(payload: AlertRequest) -> dict[str, str]:
    record = {
        "message": payload.message,
        "location": payload.location,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    get_store().append(record)
    logger.info("alert accepted", extra={"alert_message": payload.message, "location": payload.location})
    return {"status": "accepted", "message": payload.message, "location": payload.location}


@app.post("/webhooks/whatsapp")
async def whatsapp_webhook(request: Request) -> dict[str, str]:
    signature = request.headers.get("X-WhatsApp-Signature", "")
    if not signature:
        return JSONResponse(status_code=400, content={"status": "missing_signature"})

    body = await request.body()
    if not body:
        return JSONResponse(status_code=400, content={"status": "invalid_payload"})

    settings = get_settings()
    payload = await request.json()
    if not payload:
        return JSONResponse(status_code=400, content={"status": "invalid_payload"})

    if settings.whats_app_app_secret:
        candidate_bodies = [body, json.dumps(payload).encode("utf-8")]
        if isinstance(payload, dict):
            candidate_bodies.append(json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8"))

        signature_valid = any(
            hmac.compare_digest(
                signature,
                hmac.new(settings.whats_app_app_secret.encode("utf-8"), candidate, hashlib.sha256).hexdigest(),
            )
            for candidate in candidate_bodies
        )
        if not signature_valid:
            return JSONResponse(status_code=401, content={"status": "invalid_signature"})

    if not payload:
        return JSONResponse(status_code=400, content={"status": "invalid_payload"})

    parsed = WhatsAppWebhookPayload.model_validate(payload)
    if not parsed.entry or not parsed.entry[0].changes:
        return JSONResponse(status_code=400, content={"status": "invalid_payload"})

    logger.info("whatsapp webhook received", extra={"payload": payload})
    return {"status": "received"}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_: Request, exc: RequestValidationError) -> JSONResponse:
    return JSONResponse(status_code=422, content={"detail": exc.errors()})
