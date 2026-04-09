# Secure Patient Record System

A Flask-based patient management application for secure software development practice.  
The project demonstrates role-based access, patient CRUD workflows, and practical security hardening against common web risks.

## Highlights

- Role-based access control (`admin`, `doctor`)
- Session-based authentication with hashed passwords
- Patient record CRUD with object-level authorization
- CSRF protection on state-changing requests (`Flask-WTF`)
- Clickjacking defenses through response security headers
- SQLite-backed persistence with optional seed data

## Security Improvements Implemented

- IDOR mitigation:
  - Patient view/edit routes validate access using object-level checks.
  - Doctors can access only patients assigned to them; admins can access all.
- CSRF mitigation:
  - `CSRFProtect` enabled at application level.
  - CSRF failures are handled with explicit 400 responses.
- Clickjacking mitigation:
  - `X-Frame-Options: DENY`
  - `Content-Security-Policy: frame-ancestors 'none';`

## Tech Stack

- Python 3
- Flask
- Flask-WTF
- SQLite
- Jinja2 templates
- Bootstrap UI
- python-dotenv

## Project Structure

```text
SSD-Mid/
  app.py
  config.py
  database.py
  models.py
  requirements.txt
  routes/
    auth_routes.py
    patient_routes.py
  middleware/
    auth_middleware.py
  templates/
  static/
  docs/
    PNE_Report.md
    Threat_Model.pdf
    diagrams/
```

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/x0shariqx0/SecureApp-Sprint-PatientRecordSystem.git
   cd SecureApp-Sprint-PatientRecordSystem
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. (Optional) Configure environment variables in `.env`.
5. Run the app:
   ```bash
   python app.py
   ```
6. Open:
   - `http://127.0.0.1:5000`

## Configuration

Environment variables used by `config.py`:

- `SECRET_KEY` (default: `dev-insecure-secret-key`)
- `DATABASE_PATH` (default: `patient_records.db`)
- `SEED_DB` (default: `true`)

Example `.env`:

```env
SECRET_KEY=replace-with-a-strong-secret
DATABASE_PATH=patient_records.db
SEED_DB=true
```

## Default Seed Accounts

When `SEED_DB=true` and database is empty:

- Admin: `admin@example.com` / `admin123`
- Doctor: `doctor@example.com` / `doctor123`

## Core Routes

- Auth:
  - `/login`
  - `/register`
  - `/logout`
- App:
  - `/dashboard`
  - `/patients`
  - `/patients/<id>`
  - `/patients/new` (admin only)
  - `/patients/<id>/edit`
  - `/patients/<id>/delete` (admin only)

## Notes

- This project is intended for educational and assessment use.
- For production readiness, add:
  - centralized logging and monitoring
  - automated tests (unit/integration/security)
  - stronger secret management and deployment hardening
