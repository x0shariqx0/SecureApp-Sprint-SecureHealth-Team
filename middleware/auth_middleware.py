from functools import wraps
from flask import flash, redirect, session, url_for


def login_required(view_func):
    @wraps(view_func)
    def wrapped_view(*args, **kwargs):
        if "user_id" not in session:
            flash("Please login to continue.", "warning")
            return redirect(url_for("auth.login"))
        return view_func(*args, **kwargs)

    return wrapped_view


def admin_required(view_func):
    @wraps(view_func)
    def wrapped_view(*args, **kwargs):
        if session.get("role") != "admin":
            flash("Only admins can perform this action.", "danger")
            return redirect(url_for("patients.dashboard"))
        return view_func(*args, **kwargs)

    return wrapped_view
