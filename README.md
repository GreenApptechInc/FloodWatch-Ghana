# FloodWatch-Ghana 🌊🇬🇭

**Community flood reporting for Accra. WhatsApp → AI → FastAPI → Supabase.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Security: Policy](https://img.shields.io/badge/Security-Policy-blue.svg)](SECURITY.md)
[![Contributions: Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Status: Active](https://img.shields.io/badge/Status-Active-green.svg)](https://github.com/GreenApptechInc/floodwatchgh)

> Public-safety OSS project. No AR. No PII. Built for low-bandwidth + mobile-first in Ghana.

## Production-ready baseline

This repository now includes:
- a FastAPI application with health and readiness endpoints,
- automated tests covering the core API behavior,
- CI workflow for Python test execution,
- environment-based configuration via `.env`,
- 16 Accra monitoring points and their MVP alert thresholds in `monitoring_config.json`.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -m app
```

The API will be available at http://127.0.0.1:8000.

## Volunteer reporting

The community report form should submit to `POST /reports` with this JSON shape:

```json
{
	"constituency": "Ablekuma Central",
	"location": "Kaneshie Bridge",
	"estimated_water_level": "1.8m+",
	"water_trend": "Rising Fast",
	"photo_url": "https://example.com/photo.jpg",
	"whatsapp_number": "+233200000000",
	"notes": "Road flooded"
}
```

Use the title **FloodWatch-Ghana Community Report**. The water-level choices are
`0-0.3m`, `0.3-1.0m`, `1.0-1.8m`, and `1.8m+`; they map to `LOW`, `MEDIUM`,
`HIGH`, and `CRITICAL`. The form footer should say: “This data helps FloodWatch-Ghana
send alerts. Submit only if safe to do so.”

Create the Google Form and connect its response sheet to a five-minute worker that
posts normalized rows to `/reports`. Publish the form at `floodwatch-gh.org/report`
and share it with constituency WhatsApp groups. Photo upload storage and the Google
Sheets polling worker still require external credentials and deployment setup.

---

