# Security Policy

## Supported Versions
We release patches for security vulnerabilities for the latest stable release of FloodWatch-Ghana.

| Version | Supported          |
| ------- | ------------------ |
| main    | :white_check_mark: |

## Reporting a Vulnerability

FloodWatch-Ghana is a public-safety project. If you discover a security issue, please help us fix it responsibly.

**Please DO NOT open a public GitHub Issue for security bugs.**

Instead, email: **security@floodwatchgh.org** or **patrakyaddo@gmail.com**
*If you don't have a domain yet, you can use a personal email (e.g. greenapptechinc@gmail.com).* 

Include: 
1.  A description of the vulnerability 
2.  Steps to reproduce or a proof-of-concept
3.  Your impact assessment

We aim to acknowledge receipt within 48 hours and provide a status update within 7 days.

## Scope & Impact
This project collects: flood report images, approximate location, and hashed WhatsApp identifiers. 
Key risks we protect against: false flood alerts, PII exposure, and service downtime during rain events.

## Security Measures
1.  **Code Scanning**: GitHub CodeQL + Dependabot enabled on `main`
2.  **Input Validation**: All API inputs validated and rate-limited via FastAPI
3.  **Least Data**: No full names, addresses, or unhashed phone numbers stored
4.  **Dependencies**: YOLO, FastAPI, Supabase clients kept up to date

## Responsible Disclosure
We follow coordinated disclosure. Please give us time to patch before public disclosure. We will credit reporters in release notes unless you prefer to remain anonymous. Contact: **patrakyaddo@gmail.com**

Thank you for helping keep Ghana’s flood responders safe.
