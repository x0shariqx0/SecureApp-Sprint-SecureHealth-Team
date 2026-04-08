import sqlite3
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from models import User

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        role = request.form.get("role", "doctor")

        if not name or not email or not password or role not in ["admin", "doctor"]:
            flash("All fields are required.", "danger")
            return render_template("register.html")

        try:
            hashed_password = generate_password_hash(password)
            User.create(name, email, hashed_password, role)
            flash("Registration successful. Please login.", "success")
            return redirect(url_for("auth.login"))
        except sqlite3.IntegrityError:
            flash("Email is already registered.", "danger")
        except Exception:
            flash("Unable to register user right now.", "danger")

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not email or not password:
            flash("Email and password are required.", "danger")
            return render_template("login.html")

        user = User.find_by_email(email)

        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            session["name"] = user["name"]
            session["role"] = user["role"]
            flash("Login successful.", "success")
            return redirect(url_for("patients.dashboard"))

        flash("Invalid email or password.", "danger")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))
