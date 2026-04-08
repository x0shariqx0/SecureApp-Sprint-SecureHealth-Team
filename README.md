# Secure Patient Record System (Intentionally Vulnerable - Version 1)

This is a minimal Flask web app for an academic security project.  
It includes authentication, role-based UI behavior, and CRUD for patient records.

## Stack

- Python
- Flask
- SQLite (`sqlite3`)
- Jinja2 templates
- Bootstrap
- Session-based authentication
- `python-dotenv`

## Project Structure

```text
project/
  app.py
  config.py
  database.py
  models.py
  requirements.txt
  .env
  routes/
    auth_routes.py
    patient_routes.py
  middleware/
    auth_middleware.py
  templates/
    base.html
    login.html
    register.html
    dashboard.html
    patients.html
    patient_detail.html
    patient_form.html
  static/
    css/
      style.css
```

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run app:
   ```bash
   python app.py
   ```
4. Open:
   `http://127.0.0.1:5000`

## Seed Data

If `SEED_DB=true` in `.env`, the app seeds:
- Admin: `admin@example.com` / `admin123`
- Doctor: `doctor@example.com` / `doctor123`
- 3 sample patient records

## Intentional Vulnerabilities (for later fixing)

1. IDOR (Insecure Direct Object Reference)
- `/patients/<id>` and `/patients/<id>/edit` only check login.
- No check that patient belongs to logged-in doctor.

2. CSRF
- No CSRF tokens in any POST form.
- POST endpoints accept requests without anti-CSRF protection.

3. Clickjacking
- No `X-Frame-Options` header.
- No CSP `frame-ancestors` policy.

Do not use this project in production.
