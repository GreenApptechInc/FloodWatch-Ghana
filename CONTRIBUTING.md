# Contributing to FloodWatch-Ghana

Thank you for helping build Ghana’s public-safety flood reporting system 🙏  
FloodWatch-Ghana is open source and community-first. Every report, PR, and idea makes Accra safer during rainy season.

## Code of Conduct
Be respectful, inclusive, and solution-focused. This project supports emergency response. Keep discussions technical and safe. See `SECURITY.md` to report vulnerabilities privately.

## How You Can Contribute

### 1. Ways to Help Right Now
| Area | What We Need |
| --- | --- |
| **Code** | FastAPI endpoints, YOLO model tuning, WhatsApp bot fixes, Supabase RLS policies |
| **Data** | Label flood images, test reports from different Accra zones |
| **Docs** | Setup guides for `vscode.dev`, Twi/Pidgin translations, screenshots |
| **QA** | Test on low-bandwidth, Android phones, offline scenarios |

### 2. Development Setup
```bash
# 1. Fork and clone
git clone https://github.com/GreenApptechInc/floodwatchgh.git
cd floodwatchgh

# 2. Backend setup
cd backend 
python -m venv && source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # Add Supabase + WhatsApp keys

# 3. Frontend setup 
cd ../frontend
npm install
npm run dev
```
