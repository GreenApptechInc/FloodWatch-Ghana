# FloodWatch-Ghana 🌊🇬🇭

*FloodWatch Ghana*

*AI-powered flood early warning system for Accra, Ghana*  
_Founded by Patrick Akyea-Addo_

Delivering real-time WhatsApp alerts to help vulnerable communities evacuate and stay safe before floods hit.

The Problem
Over 300,000 Ghanaians are affected by floods every year. In Accra, warnings from NADMO and GMet often arrive too late for communities in low-lying areas. The gap between data and action costs lives and property.

The Solution
*FloodWatch* combines real-time weather + community data to send instant flood alerts via WhatsApp. 
- *Monitor*: Rainfall, river levels, and GMet forecasts
- *Alert*: Instant English WhatsApp messages with risk level + safe actions
- *Report*: Community members can report flooding in 2 clicks to improve local accuracy
- *Accessible*: Works without smartphone data. No app download needed.

Why This Matters Now
Accra’s floods are getting more frequent. With climate change, early warning is the most cost-effective way to reduce loss of life. FloodWatch puts that warning directly in people’s hands.

Tech Stack
- *Backend*: Python, FastAPI
- *Messaging*: WhatsApp Cloud API, Meta WABA
- *AI*: OpenAI GPT-4 for risk analysis and clear, actionable alert summaries
- *Data*: GMet, Hydrological Service, Community Ushahidi reports
- *Cloud*: Built to deploy on Azure and GCP. Applying for Microsoft for Startups + Google for Startups credits to scale.

*Traction* *and* *Status*
*Stage:* MVP - Live Pilot  
*Communities:* 3 pilot communities in Accra  
*Users:* 250+ on waitlist  
*Built by:* Solo Founder with passion for tackling climate related pain-points via AI.

About the Founder
*Patrick Akyea-Addo* - Self-taught AI software creator, Accra, Ghana  
I built FloodWatch after seeing floods disrupt my own community. My interest is in using tech to build open-source AI Systems to solve local problems. I’m currently operating FloodWatch as an independent project and seeking grants, credits, and partnerships to scale to 5 zones across Accra by end of 2026.

Roadmap 2026
- Integrate live GMet + river gauge APIs
- Launch 5 WhatsApp alert channels - one per major flood zone
- Formalize partnerships with NADMO + local assemblies
- Publish open-source alert engine for other African cities

*Partners* *and* *Support*
I am applying to:
- *Microsoft for Startups Founders Hub* - for Azure credits + mentorship
- *Google for Startups Accelerator Africa* - for GCP credits + technical support

Open to collaborators, mentors, NGOs, and grant partners.

Contact
*Founder*: Patrick Akyea-Addo  
*Email*: patrakyaddo@gmail.com  
*Location*: Accra, Ghana

License
MIT © 2026 Patrick Akyea-Addo

---

**Community flood reporting for Accra. WhatsApp → AI → FastAPI → Supabase.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Security: Policy](https://img.shields.io/badge/Security-Policy-blue.svg)](SECURITY.md)
[![Contributions: Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Status: Active](https://img.shields.io/badge/Status-Active-green.svg)](https://github.com/patrakyaddo/floodwatchgh)

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

