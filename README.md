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
- environment-based configuration via `.env`.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -m app
```

The API will be available at http://127.0.0.1:8000.

---

