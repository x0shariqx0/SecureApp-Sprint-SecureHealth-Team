from flask import Flask, redirect, session, url_for
from dotenv import load_dotenv
from flask_wtf.csrf import CSRFError, CSRFProtect

from config import Config
from database import init_db, seed_db
from routes.auth_routes import auth_bp
from routes.patient_routes import patient_bp


def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(Config)
    CSRFProtect(app)

    init_db()

    # Optional seed via environment variable
    if app.config.get("SEED_DB", "false").lower() == "true":
        seed_db()

    app.register_blueprint(auth_bp)
    app.register_blueprint(patient_bp)

    @app.errorhandler(CSRFError)
    def handle_csrf_error(error):
        return f"CSRF validation failed: {error.description}", 400

    @app.after_request
    def set_security_headers(response):
        # Clickjacking protection
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Content-Security-Policy"] = "frame-ancestors 'none';"
        return response

    @app.route("/")
    def index():
        if session.get("user_id"):
            return redirect(url_for("patients.dashboard"))
        return redirect(url_for("auth.login"))

    return app


if __name__ == "__main__":
    application = create_app()
    application.run(debug=True)
