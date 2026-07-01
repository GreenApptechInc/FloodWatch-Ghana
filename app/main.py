from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.schemas import AlertRequest, WhatsAppWebhookPayload

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


@app.post("/webhooks/whatsapp")
async def whatsapp_webhook(request: Request) -> dict[str, str]:
    signature = request.headers.get("X-WhatsApp-Signature", "")
    if not signature:
        return JSONResponse(status_code=400, content={"status": "missing_signature"})

    payload = await request.json()
    if not payload:
        return JSONResponse(status_code=400, content={"status": "invalid_payload"})

    parsed = WhatsAppWebhookPayload.model_validate(payload)
    if not parsed.entry or not parsed.entry[0].changes:
        return JSONResponse(status_code=400, content={"status": "invalid_payload"})

    return {"status": "received"}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_: Request, exc: RequestValidationError) -> JSONResponse:
    return JSONResponse(status_code=422, content={"detail": exc.errors()})
