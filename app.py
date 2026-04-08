from flask import Flask, redirect, session, url_for
from dotenv import load_dotenv

from config import Config
from database import init_db, seed_db
from routes.auth_routes import auth_bp
from routes.patient_routes import patient_bp


def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(Config)

    init_db()

    # Optional seed via environment variable
    if app.config.get("SEED_DB", "false").lower() == "true":
        seed_db()

    app.register_blueprint(auth_bp)
    app.register_blueprint(patient_bp)

    @app.route("/")
    def index():
        if session.get("user_id"):
            return redirect(url_for("patients.dashboard"))
        return redirect(url_for("auth.login"))

    return app


if __name__ == "__main__":
    application = create_app()
    application.run(debug=True)
