from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from middleware.auth_middleware import admin_required, login_required
from models import Patient, User

patient_bp = Blueprint("patients", __name__)


@patient_bp.route("/dashboard")
@login_required
def dashboard():
    patients = Patient.all_records()
    return render_template("dashboard.html", patients=patients)


@patient_bp.route("/patients")
@login_required
def patients():
    records = Patient.all_records()
    return render_template("patients.html", patients=records)


@patient_bp.route("/patients/<int:patient_id>")
@login_required
def patient_detail(patient_id):
    # Intentional vulnerability (IDOR): no ownership check
    patient = Patient.find_by_id(patient_id)
    if not patient:
        flash("Patient record not found.", "warning")
        return redirect(url_for("patients.patients"))
    return render_template("patient_detail.html", patient=patient)


@patient_bp.route("/patients/new", methods=["GET", "POST"])
@login_required
@admin_required
def create_patient():
    doctors = User.all_doctors()

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        age = request.form.get("age", "").strip()
        diagnosis = request.form.get("diagnosis", "").strip()
        assigned_doctor_id = request.form.get("assigned_doctor_id", "").strip()

        if not name or not age or not diagnosis:
            flash("Name, age, and diagnosis are required.", "danger")
            return render_template("patient_form.html", doctors=doctors, patient=None)

        try:
            Patient.create(name, int(age), diagnosis, int(assigned_doctor_id) if assigned_doctor_id else None)
            flash("Patient created successfully.", "success")
            return redirect(url_for("patients.patients"))
        except ValueError:
            flash("Age and doctor id must be valid numbers.", "danger")
        except Exception:
            flash("Failed to create patient record.", "danger")

    return render_template("patient_form.html", doctors=doctors, patient=None)


@patient_bp.route("/patients/<int:patient_id>/edit", methods=["GET", "POST"])
@login_required
def edit_patient(patient_id):
    # Intentional vulnerability (IDOR): no ownership check
    patient = Patient.find_by_id(patient_id)
    doctors = User.all_doctors()

    if not patient:
        flash("Patient record not found.", "warning")
        return redirect(url_for("patients.patients"))

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        age = request.form.get("age", "").strip()
        diagnosis = request.form.get("diagnosis", "").strip()
        assigned_doctor_id = request.form.get("assigned_doctor_id", "").strip()

        if not name or not age or not diagnosis:
            flash("Name, age, and diagnosis are required.", "danger")
            return render_template("patient_form.html", doctors=doctors, patient=patient)

        try:
            Patient.update(patient_id, name, int(age), diagnosis, int(assigned_doctor_id) if assigned_doctor_id else None)
            flash("Patient updated successfully.", "success")
            return redirect(url_for("patients.patient_detail", patient_id=patient_id))
        except ValueError:
            flash("Age and doctor id must be valid numbers.", "danger")
        except Exception:
            flash("Failed to update patient record.", "danger")

    return render_template("patient_form.html", doctors=doctors, patient=patient)


@patient_bp.route("/patients/<int:patient_id>/delete", methods=["POST"])
@login_required
@admin_required
def delete_patient(patient_id):
    patient = Patient.find_by_id(patient_id)
    if not patient:
        flash("Patient record not found.", "warning")
        return redirect(url_for("patients.patients"))

    try:
        Patient.delete(patient_id)
        flash("Patient deleted successfully.", "success")
    except Exception:
        flash("Failed to delete patient record.", "danger")

    return redirect(url_for("patients.patients"))
